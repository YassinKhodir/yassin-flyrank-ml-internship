# Study coach: checked live run
AI-assisted case note, updated November 10, 2026.

## Problem
Technical notes can be hard to understand. The coach searches local notes,
explains a supported topic in simple English, and cites the source heading.

## What was done
The Python code and writing were AI-assisted. The student ran the coach on
Windows with Ollama and Gemma `gemma4:e2b`, then opened the practice notes to
check the answer. The new raw recording is 2 minutes 2 seconds long. It shows
a fresh command, the answer, and the notes comparison. The raw video stays
in private storage or the private portal, not in this public repository.

The saved `live_answer_01.json` was also inspected. It records a real Ollama
run: `search_notes` found one match, followed by `answer`.
The Windows test record shows 11 passed tests and one skipped symlink test.

## Observed result
The answer explains that data leakage means using information that would
not be available when making a real prediction. Its example uses next week's
clicks to predict this week's result. The definition and example match the
Data leakage section in the artificial practice notes. It cites that heading.
This is a checked result for one example, not proof that every answer is correct.

## Limits and next steps
- Heading checks do not prove that an answer is correct.
- The earlier raw recording does not include a practice question; the second evaluation's data-leakage answer does.
- The earlier date failure was corrected by a local code guardrail. The second
  Windows evaluation shows both dates and directly asks which version is current.
- FL-09 was submitted November 10 with a 3:54.5 narrated demo and is waiting for review.
- Prompt Ladder's six actual outputs and comparison notes were submitted October 20.
- The student's reflection remains to be written in their own words.

No broad evaluation score, measured time saving, student work duration,
new internship approval or actual student hours are claimed.

## Updated evidence
The second evaluation contains three real Gemma search/answer traces and two
local checks. The missing-topic refusal and conflicting-date check do not call
the model. See [the full evaluation](../../study_coach/EVALUATION.md).
The [unlisted demo](https://www.youtube.com/watch?v=7VjbMP6wQds) shows the live
program, checking notes, conflicting dates and the CTR calculation. The portal
shows 111 estimated hours; this case does not verify actual work time.

## Evidence
- [Coach source](../../study_coach/coach.py)
- [Build log](../../study_coach/BUILD_LOG.md)
- [Saved live result](../../study_coach/live_answer_01.json)
- [Windows test record](../../study_coach/test_results_windows.txt)
- [Practice notes](../../study_coach/notes/sample.md)
- [Setup and known limits](../../study_coach/README.md)

Keep private notes, recordings, account details and signatures out of the
public repository. Preserve earlier recordings as backup evidence.
