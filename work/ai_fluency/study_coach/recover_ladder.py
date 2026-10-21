"""Finish a saved six-version ladder without rerunning completed answers."""
import argparse
import json
from pathlib import Path
from guided_ladder import ask, model_answer

QUESTIONS = [
    ("what_changed", "What changed in this prompt?"),
    ("what_improved", "What improved compared with the previous answer?"),
    ("what_still_failed", "What still failed or got worse?"),
    ("what_to_try_next", "What would you try next, and why?")]


def recover(source, output, ask_fn=ask, model_fn=model_answer):
    source = Path(source)
    original = source.read_bytes()
    record = json.loads(original.decode("utf-8-sig"))
    runs = record.get("runs", [])
    if len(runs) != 6 or [r.get("version") for r in runs] != list(range(6)):
        raise ValueError("This recovery needs all six prompt versions already saved.")
    if not record.get("model") or any(not r.get("prompt") for r in runs):
        raise ValueError("The saved model or prompts are missing.")
    root = Path(output)
    root.mkdir(parents=True, exist_ok=False)
    (root / "original-results.json").write_bytes(original)
    record["recovered_from"] = str(source)
    record["previous_error"] = record.pop("error", None)

    def save():
        temp = root / "results.tmp"
        temp.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        temp.replace(root / "results.json")

    record["status"] = "recovery in progress"
    save()
    try:
        for item in runs:
            if not item.get("output"):
                print(f"Retrying version {item['version']} only. Please wait...", flush=True)
                item["output"] = model_fn(item["prompt"], record["model"])
                item["status"] = "output saved; review pending"
                save()
            review = item.setdefault("review", {})
            missing = [(key, question) for key, question in QUESTIONS if not review.get(key)]
            if missing:
                print(f"\nVERSION {item['version']} MODEL ANSWER:\n{item['output']}")
            for key, question in missing:
                review[key] = ask_fn(question)
                save()
            item["status"] = "output and user notes saved"
            save()
        if not record.get("best_version"):
            record["best_version"] = ask_fn("Which version was best, and why?")
            save()
        if not record.get("final_reusable_prompt"):
            record["final_reusable_prompt"] = ask_fn("Write the final reusable prompt on one line, with input placeholders:")
        record["status"] = "six outputs and user notes collected; final checking still required"
        save()
    except (KeyboardInterrupt, EOFError, OSError, ValueError, RuntimeError) as exc:
        record["status"] = "stopped; recovery incomplete"
        record["error"] = str(exc) or type(exc).__name__
        save()
        print(f"Stopped: {record['error']}\nSaved progress: {root / 'results.json'}")
        return 1
    print(f"Saved complete evidence: {root / 'results.json'}")
    print("Original file unchanged. Review before submission; no hours entered.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True, help="New private recovery folder")
    args = parser.parse_args()
    try:
        raise SystemExit(recover(args.source, args.output))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Cannot recover: {exc}\n")
