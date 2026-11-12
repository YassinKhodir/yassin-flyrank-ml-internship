"""Simulated checks of evidence retention, not live-model evaluation."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import guided_ladder


class GuidedLadderTests(unittest.TestCase):
    def test_existing_evidence_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "evidence"
            path.mkdir()
            marker = path / "results.json"
            marker.write_text("keep", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                guided_ladder.run("test-model", path)
            self.assertEqual(marker.read_text(), "keep")

    def test_model_failure_keeps_prior_output_and_notes(self):
        answers = iter(["Explain this data.", "baseline", "It asked for data.",
                        "No numbers given.", "Add context.", "context",
                        "No numbers given.", "10 clicks, 100 impressions."])
        replies = iter(["Please provide the data.", RuntimeError("offline")])
        def model_fn(prompt, model):
            answer = next(replies)
            if isinstance(answer, Exception):
                raise answer
            return answer
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "evidence"
            self.assertEqual(guided_ladder.run("test", path, lambda _: next(answers), model_fn), 1)
            data = json.loads((path / "results.json").read_text())
            self.assertEqual(data["runs"][0]["output"], "Please provide the data.")
            self.assertEqual(data["runs"][0]["review"]["what_still_failed"], "No numbers given.")
            self.assertNotIn("output", data["runs"][1])
            self.assertIsNone(data["student_hours"])

    def test_six_runs_use_fresh_cumulative_prompts(self):
        answers = ["Explain this data."]
        for version in range(6):
            if version:
                answers += ["context", "missing detail", f"Add detail {version}."]
            answers += ["change", "no improvement", "still incomplete", "check next"]
        answers += ["version 2", "Explain [DATA] for [AUDIENCE]."]
        entered = iter(answers)
        prompts = []
        def model_fn(prompt, model):
            prompts.append(prompt)
            return "simulated output"
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "evidence"
            self.assertEqual(guided_ladder.run("test", path, lambda _: next(entered), model_fn), 0)
            data = json.loads((path / "results.json").read_text())
            self.assertEqual(len(data["runs"]), 6)
            for i in range(1, 6):
                self.assertEqual(prompts[i], prompts[i-1] + f"\nAdd detail {i}.")
            self.assertEqual(data["best_version"], "version 2")


if __name__ == "__main__":
    unittest.main()
