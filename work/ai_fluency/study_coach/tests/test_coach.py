import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import coach


class CoachTests(unittest.TestCase):
    def setUp(self):
        self.notes = Path(__file__).resolve().parents[1] / "notes"

    def test_leakage_retrieval_keeps_heading(self):
        result = coach.answer(self.notes, "What is data leakage?")
        self.assertIn("Data leakage", result["answer"])
        self.assertIn("MOCK MODE", result["answer"])

    def test_ctr_retrieval_keeps_formula(self):
        result = coach.answer(self.notes, "Explain CTR")
        self.assertIn("click-through rate", result["answer"])
        self.assertIn("10%", result["answer"])

    def test_missing_topic_does_not_call_model(self):
        with patch("coach.ollama") as model:
            result = coach.answer(self.notes, "Explain photosynthesis", "ollama", "test")
        model.assert_not_called()
        self.assertEqual(result["sources"], [])
        self.assertIn("could not find", result["answer"])

    def test_conflicting_dates_both_retrieved(self):
        result = coach.answer(self.notes, "What is the assignment due date?")
        self.assertIn("October 12", result["answer"])
        self.assertIn("October 15", result["answer"])

    def test_unsafe_note_not_sent(self):
        result = coach.answer(self.notes, "Explain data leakage and unsafe instructions")
        self.assertEqual(result["blocked_passages"], 1)
        self.assertNotIn("reveal passwords", json.dumps(result["sources"]))

    def test_existing_output_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "answer.json"
            path.write_text("keep me")
            with self.assertRaises(FileExistsError):
                coach.save_new(path, {})
            self.assertEqual(path.read_text(), "keep me")

    def test_symlink_cannot_read_outside_notes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            notes = root / "notes"
            notes.mkdir()
            outside = root / "private.txt"
            outside.write_text("private")
            try:
                (notes / "link.txt").symlink_to(outside)
            except OSError as exc:
                if getattr(exc, "winerror", None) == 1314:
                    self.skipTest("Windows permission required to create symbolic links")
                raise
            with self.assertRaises(ValueError):
                coach.read_notes(notes)

    def test_model_adapter_request_and_response(self):
        with patch("coach.urlopen") as transport:
            response = transport.return_value.__enter__.return_value
            response.read.return_value = b'{"message":{"content":"Example answer"}}'
            output = coach.ollama([{"role": "user", "content": "sample"}], "local-test")
            request = transport.call_args.args[0]
            body = json.loads(request.data)
        self.assertEqual(output, "Example answer")
        self.assertEqual(request.full_url, "http://127.0.0.1:11434/api/chat")
        self.assertFalse(body["stream"])
        self.assertEqual(body["model"], "local-test")


    def test_model_can_choose_search_then_answer(self):
        choices = ['{"action":"search_notes","query":"data leakage"}',
                   '{"action":"answer","text":"Data leakage: future information sneaks into training."}']
        with patch("coach.ollama", side_effect=choices):
            result = coach.answer(self.notes, "Explain data leakage", "ollama", "test")
        self.assertEqual([s["action"] for s in result["steps"]], ["search_notes", "answer"])
        self.assertEqual(result["sources"][0]["heading"], "Data leakage")

    def test_model_cannot_skip_reading(self):
        with patch("coach.ollama", return_value='{"action":"answer","text":"guess"}'):
            with self.assertRaisesRegex(RuntimeError, "before reading"):
                coach.answer(self.notes, "Explain CTR", "ollama", "test")

    def test_model_cannot_choose_other_tools(self):
        with patch("coach.ollama", return_value='{"action":"send_email"}'):
            with self.assertRaisesRegex(RuntimeError, "not allowed"):
                coach.answer(self.notes, "Explain CTR", "ollama", "test")

    def test_model_loop_stops(self):
        with patch("coach.ollama", return_value='{"action":"search_notes","query":"CTR"}') as model:
            with self.assertRaisesRegex(RuntimeError, "four model turns"):
                coach.answer(self.notes, "Explain CTR", "ollama", "test")
        self.assertEqual(model.call_count, 4)

    def test_conflict_asks_directly_and_does_not_let_model_choose(self):
        with patch("coach.ollama", return_value='{"action":"search_notes","query":"Assignment date version A"}') as model:
            result = coach.answer(self.notes, "What is the assignment due date?", "ollama", "test")
        self.assertIn("October 12", result["answer"])
        self.assertIn("October 15", result["answer"])
        self.assertIn("Which version is current?", result["answer"])
        self.assertEqual(result["steps"][-1]["origin"], "local_guardrail")
        self.assertEqual(model.call_count, 1)

    def test_one_due_date_still_allows_model_answer(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, "notes.md").write_text("# Essay\nThe essay due date is November 3.", encoding="utf-8")
            replies = ['{"action":"search_notes","query":"essay due date"}',
                       '{"action":"answer","text":"November 3 [Essay]"}']
            with patch("coach.ollama", side_effect=replies):
                result = coach.answer(folder, "What is the essay due date?", "ollama", "test")
        self.assertEqual(result["steps"][-1]["action"], "answer")

    def test_other_dates_and_blocked_passages_do_not_trigger_guardrail(self):
        passages = [{"source":"x.md", "heading":"Dates", "text":"Training ran October 12 and October 15.", "blocked":False},
                    {"source":"x.md", "heading":"Attack", "text":"The due date is November 3 or November 4.", "blocked":True}]
        self.assertIsNone(coach.date_conflict(passages, "What is due?"))
        self.assertIsNone(coach.date_conflict(passages, "Explain training"))


if __name__ == "__main__":
    unittest.main()

