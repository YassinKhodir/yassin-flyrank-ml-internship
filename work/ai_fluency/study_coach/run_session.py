"""Collect real local-model evidence. Computer runtime is not student work time."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import coach
import prompt_ladder


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Exact name from ollama list")
    parser.add_argument("--notes", default="notes")
    parser.add_argument("--question", default="Explain click-through rate")
    parser.add_argument("--output", required=True, help="New folder for private results")
    args = parser.parse_args()
    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=False)
    record = {"started_utc": datetime.now(timezone.utc).isoformat(),
              "model": args.model, "status": "running",
              "student_hours": None,
              "note": "These timestamps measure computer processing, not student work. Source notes and outputs may be private."}
    try:
        result = coach.answer(args.notes, args.question, "ollama", args.model)
        coach.save_new(root / "agent_run.json", result)
        if result.get("backend") != "ollama" or not result.get("steps"):
            raise RuntimeError("No live agent loop ran. Use a question supported by your notes.")
        print(result["answer"])
        ladder = {"model": args.model, "runs": [],
                  "note": "Suggested experiment, not a claim about past student prompts."}
        for item in prompt_ladder.prompts():
            print(f"Prompt version {item['version']}: {item['layer']}", flush=True)
            reply = coach.ollama([{"role": "user", "content": item["prompt"]}], args.model)
            ladder["runs"].append({**item, "output": reply,
                                  "student_review": "NOT REVIEWED"})
            (root / "prompt_outputs.json").write_text(
                json.dumps(ladder, indent=2), encoding="utf-8")
        record["status"] = "live outputs collected; student review and recordings pending"
    except (OSError, ValueError, RuntimeError) as exc:
        record["status"] = "stopped; not a completed assignment"
        record["error"] = str(exc)
        print(f"Stopped: {exc}")
        return 1
    finally:
        record["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (root / "session_record.json").write_text(
            json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"Saved private evidence to {root}. Read and check it before submitting.")
    print("This run does not verify internship hours or make a demo video.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
