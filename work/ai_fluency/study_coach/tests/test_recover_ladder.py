import json
from pathlib import Path
import tempfile
import unittest
import recover_ladder


class RecoveryTests(unittest.TestCase):
    def make_record(self, folder):
        runs = []
        for version in range(6):
            item = {"version": version, "prompt": f"prompt {version}"}
            if version < 5:
                item.update(output=f"original answer {version}",
                            review={key: "original note" for key, _ in recover_ladder.QUESTIONS})
            runs.append(item)
        path = Path(folder) / "original.json"
        path.write_text(json.dumps({"model": "test", "runs": runs, "student_hours": None,
                                    "error": "earlier failure"}), encoding="utf-8")
        return path

    def test_only_last_model_call_runs_and_original_is_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            source = self.make_record(folder)
            before = source.read_bytes()
            calls = []
            answers = iter(["format", "shorter", "no issue seen", "test again", "5: concise", "Explain [DATA]."])
            def model(prompt, name):
                calls.append(prompt)
                return "real response stand-in"
            output = Path(folder) / "recovered"
            self.assertEqual(recover_ladder.recover(source, output, lambda _: next(answers), model), 0)
            result = json.loads((output / "results.json").read_text())
            self.assertEqual(calls, ["prompt 5"])
            self.assertEqual(source.read_bytes(), before)
            self.assertEqual((output / "original-results.json").read_bytes(), before)
            self.assertEqual(result["runs"][0]["output"], "original answer 0")

    def test_failed_retry_preserves_five_answers(self):
        with tempfile.TemporaryDirectory() as folder:
            source = self.make_record(folder)
            def fail(*args):
                raise RuntimeError("HTTP 500")
            output = Path(folder) / "recovered"
            self.assertEqual(recover_ladder.recover(source, output, model_fn=fail), 1)
            result = json.loads((output / "results.json").read_text())
            self.assertEqual(result["error"], "HTTP 500")
            self.assertEqual(sum("output" in r for r in result["runs"]), 5)
            with self.assertRaises(FileExistsError):
                recover_ladder.recover(source, output, model_fn=fail)
