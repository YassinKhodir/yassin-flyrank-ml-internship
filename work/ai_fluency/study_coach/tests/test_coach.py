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
            (notes / "link.txt").symlink_to(outside)
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


if __name__ == "__main__":
    unittest.main()
