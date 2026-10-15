# Study coach: reported live run
AI-assisted case note, updated October 15, 2026.
Evidence status: based on the student's supplied conversation handoff. The video and model trace have not been independently inspected in this update.

## Problem
Technical study notes can be hard to understand. The coach is intended to explain them in simple English and cite the source heading.

## What was done
The Python prototype reads local notes and can use a Gemma model through Ollama.
The student shared a handoff describing a real PowerShell run asking the coach to explain data leakage, followed by opening the practice notes to check the answer.
The code and instructions were AI-assisted. This note does not claim the student independently wrote every line.

## Observed result reported in the handoff
The answer explained that data leakage means using information that would not be available when making a real prediction.
It used the example of next week's clicks being used to predict this week's result.
The handoff says the definition and example matched the Data leakage section and that the answer cited that heading.
This is a reported source check for one artificial practice example, not proof that every answer is correct.

The handoff's earlier video assessment describes flyrank.mp4 as a 54-second silent recording.
That assessment is preserved as supplied context; audio and duration were not re-measured in this update.
The silent recording is supporting evidence. It does not meet the narrated FL-09 demo requirement.

## What still needs evidence
- Preserve the original recording as backup; do not overwrite it.
- Save the actual model name, command, output and note comparison.
- FL-07 asks for an unedited capture about two minutes long showing the full request-to-result run.
- FL-09 asks for a three-to-five-minute live demo with clear voice narration, a design decision and a limitation. A short script alone does not establish that duration.
- Recheck the actual video before marking either recording requirement complete.
- Review all six real prompt-ladder outputs separately; one successful agent answer does not finish that assignment.

## Limits
The example uses artificial practice notes.
An answer mentioning a source heading is not an automatic factual-correctness check.
The handoff does not include a saved model-action trace, so this note does not verify the exact search/answer loop.
No broad evaluation score, measured time saving, student work duration, internship approval or additional hours are claimed.

## Evidence pointers
- [Coach source](../../study_coach/coach.py)
- [Practice notes](../../study_coach/notes/sample.md)
- [Setup and known limits](../../study_coach/README.md)
- [Evidence collection helper](../../study_coach/run_session.py)

Keep the video and any private notes in private storage or the private FlyRank submission. This public case contains no personal machine path, private note contents, account details or signatures.

## Student reflection
Still to be written by the student in their own words. No completed reflection or narration is invented.
