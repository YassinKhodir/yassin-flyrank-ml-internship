"""Run six real local-model prompts and save outputs for human comparison."""
import argparse
from datetime import datetime, timezone
import coach

BASELINE = "Explain this data."
LAYERS = [
    ("clearer goal", "Explain click-through rate and calculate it for the data below."),
    ("audience", "The reader is a CIS student who is new to search analytics."),
    ("context", "Artificial test data: 10 clicks and 100 impressions. CTR means click-through rate: clicks divided by impressions, times 100."),
    ("format", "Use exactly these headings: Meaning, Calculation, Practical use."),
    ("verification", "Check the arithmetic and distinguish what this small example shows from what it cannot prove."),
]


def prompts():
    result = [{"version": 0, "layer": "baseline", "prompt": BASELINE}]
    text = BASELINE
    for version, (layer, addition) in enumerate(LAYERS, 1):
        text += "\n" + addition
        result.append({"version": version, "layer": layer, "prompt": text})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Exact local model name from ollama list")
    parser.add_argument("--output", required=True, help="New JSON filename")
    args = parser.parse_args()
    # Reserve a new file before making model requests. Never overwrite evidence.
    from pathlib import Path
    import json
    try:
        with Path(args.output).open("x", encoding="utf-8") as stream:
            report = {"model": args.model, "started_utc": datetime.now(timezone.utc).isoformat(),
                      "status": "running", "runs": [],
                      "note": "Suggested starting prompts, not a claim about the student's past prompts. Human review required."}
            def checkpoint():
                stream.seek(0)
                json.dump(report, stream, indent=2)
                stream.truncate()
                stream.flush()
            checkpoint()
            try:
                for item in prompts():
                    print(f"Running version {item['version']}: {item['layer']}", flush=True)
                    output = coach.ollama([{"role": "user", "content": item["prompt"]}], args.model)
                    report["runs"].append({**item, "output": output,
                                           "review": {"what_changed": item["layer"],
                                                      "what_improved": "NOT REVIEWED",
                                                      "what_still_failed": "NOT REVIEWED",
                                                      "what_to_try_next": "NOT REVIEWED"}})
                    checkpoint()
                report["status"] = "six outputs collected; human comparison pending"
            except RuntimeError:
                report["status"] = "stopped: local model request failed; partial results retained"
                raise
            finally:
                checkpoint()
    except (OSError, RuntimeError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
