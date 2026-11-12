# Finish the workflow: one real timed comparison
Prepared November 12, 2026. The student has not performed this task yet.

You can do this from a phone. No new recording or laptop command is required.

## Use this new input
Question: Why does the coach refuse to replace an existing output file?

Source: study_coach/coach.py, function save_new, lines 215–219 at the saved revision.
File blob: 0cbc69c852c706536422661c8b1b74c969fbdb1e

```python
def save_new(path, result):
    # 'x' creates only a new file: it cannot silently replace previous work.
    with Path(path).open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
```

## First: manual attempt
Start a stopwatch. Read the source. Without asking AI, write two or three simple sentences explaining what the function does and why refusing to replace an existing file could help.
Add one check question. Stop the stopwatch after you check the result.
Keep your answer and the actual elapsed time. There is no minimum duration.

## Second: assisted attempt
Start a new timer. Use the same question and source with all four stages in README.md.
Keep the returned gather, draft, check and final-card outputs.
Read the final card beside the source and correct any error. Stop the timer only after that check.
Save your real elapsed time. This includes pasting, waiting and checking, not just generation.

## Record privately
Manual answer:
Manual elapsed time:
Assisted elapsed time:
Your setup/learning time:
What you corrected:
Which result was clearer, and why:

No values are prefilled. Do not count breaks or the assistant's earlier automated work as your own time.
The earlier five examples and this new source support preparation; they do not replace these actual attempts.

## Remaining setup requirement
The current saved version is an in-chat workflow. FL-04 names a configured Claude Project, NotebookLM, custom GPT or n8n as examples.
Use an accepted structured no-code setup or obtain reviewer confirmation for the in-chat format.
Do not claim an account, custom GPT, project or deployment was configured merely because these instructions were saved in GitHub.
