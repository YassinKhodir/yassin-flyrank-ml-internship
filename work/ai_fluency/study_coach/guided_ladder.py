"""Run a six-step prompt experiment with a real local model and human review."""
import argparse
import json
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


def ask(message):
    while True:
        value = input(message + "\n> ").strip()
        if value:
            return value
        print("Please write an answer, or press Ctrl+C to stop.")


def model_answer(prompt, model):
    # Each call is a fresh conversation. No forced format or extra teaching rules.
    request = Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps({"model": model, "stream": False,
                         "messages": [{"role": "user", "content": prompt}]}).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=180) as response:
            result = json.load(response)
    except (URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError("Local model request failed. Check Ollama and the model name.") from exc
    if not isinstance(result, dict):
        raise RuntimeError("The model response was not an object.")
    message = result.get("message")
    text = message.get("content") if isinstance(message, dict) else None
    if not isinstance(text, str) or not text.strip():
        raise RuntimeError("The model returned no answer.")
    return text


def run(model, output, ask_fn=ask, model_fn=model_answer):
    # Reserve the folder first. Never overwrite a previous experiment.
    root = Path(output)
    root.mkdir(parents=True, exist_ok=False)
    record = {"model": model, "status": "in progress", "runs": [],
              "student_hours": None,
              "note": "AI-assisted runner. Outputs are real model replies; review text is entered by the user. No work hours inferred."}

    def save():
        temp = root / "results.tmp"
        temp.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        temp.replace(root / "results.json")

    save()
    try:
        prompt = ask_fn("Write a weak starting prompt from your own work:")
        for version in range(6):
            layer, addition, reason = "baseline", "", ""
            if version:
                layer = ask_fn("Name ONE layer to add (goal, audience, context, format, or another single layer):")
                reason = ask_fn("Which weakness in the last answer makes this the next change?")
                addition = ask_fn("Write ONLY the instruction for that one new layer:")
                prompt += "\n" + addition
            item = {"version": version, "layer": layer, "addition": addition,
                    "reason": reason, "prompt": prompt, "status": "request pending"}
            record["runs"].append(item)
            save()
            print(f"\nRunning version {version} with {model}...", flush=True)
            item["output"] = model_fn(prompt, model)
            item["status"] = "output saved; review pending"
            save()
            print("\nMODEL ANSWER:\n" + item["output"])
            item["review"] = {}
            for key, question in [
                ("what_changed", "What changed in this prompt? For baseline, say baseline."),
                ("what_improved", "What improved versus the previous answer? For baseline, describe what it does. It is fine to say nothing improved."),
                ("what_still_failed", "What still failed or got worse? Be specific."),
                ("what_to_try_next", "What would you try next, and why?")]:
                item["review"][key] = ask_fn(question)
                save()
            item["status"] = "output and user notes saved"
            save()
        record["best_version"] = ask_fn("Which version was best, and why? It need not be the last one.")
        record["final_reusable_prompt"] = ask_fn("Write the cleaned-up reusable prompt on one line. Include clear input placeholders for another person.")
        record["status"] = "six outputs and user notes collected; final checking still required"
        save()
    except (KeyboardInterrupt, EOFError, OSError, ValueError, RuntimeError) as exc:
        record["status"] = "stopped; incomplete experiment"
        record["error"] = str(exc) or type(exc).__name__
        save()
        print(f"Stopped. Partial evidence stays in {root}.")
        return 1
    print(f"Saved to {root}. Read all six comparisons before submission.")
    print("No internship hours were entered. Do not invent a failed step to satisfy the brief.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True, help="A new private results folder")
    args = parser.parse_args()
    try:
        return run(args.model, args.output)
    except OSError as exc:
        parser.exit(1, f"Could not create a new results folder: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
