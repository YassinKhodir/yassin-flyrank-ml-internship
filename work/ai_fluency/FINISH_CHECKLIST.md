# Finish the live evidence on Windows
AI-assisted instructions. No hours or live-model results are claimed by this document.

## What is ready
The study-coach code, twelve automated tests, sample notes, build log, prompt-ladder runner, and portfolio identity kit are in this branch.
The identity kit was submitted October 12. FL-06 was submitted October 8.
The ML capstone was approved October 6.

## What cannot run in this workspace
Ollama is not installed or listening at the local model address here.
This environment cannot operate your Windows computer or record your voice.
The helper below collects real evidence on a computer with a working Ollama model.

## Collect the actual model outputs
1. Open the internship repository on your computer. Use branch ai-fluency-study-coach.
   Do not use the separate CIS 3370 repository.
2. In PowerShell run `ollama list`. Keep the exact name of an already installed model.
   If Ollama is unavailable, install it from its official site and choose a model your computer can run.
3. Open the folder `work/ai_fluency/study_coach` in your terminal.
4. For an initial test, keep the included artificial sample notes. For a real study task, use your own small .md or .txt class notes and ask a supported question. Do not upload private class notes publicly.
5. Run:
   `python run_session.py --model YOUR_MODEL_NAME --output sessions/run-01`
   YOUR_MODEL_NAME is a placeholder. Replace it with the actual name.
   A different notes folder and question can be provided:
   `python run_session.py --model YOUR_MODEL_NAME --notes PATH_TO_NOTES --question "YOUR_QUESTION" --output sessions/run-02`
6. Read session_record.json. A failed run is not completion. Save the full error.
7. Check agent_run.json against the source notes: arithmetic, each claim, cited headings, and missing facts.
8. Review all six prompt outputs. Write what changed, what improved, what failed, and the next step for each. Do not invent a worse result if none occurred; get reviewer guidance or test another real weak prompt.
9. Record a successful agent run from request to answer, unedited, about two minutes for FL-07.
10. For FL-09, record three to five minutes with your own narration: explain the design choice, the result, and one limitation. Show the program, not slides.

sessions/ is ignored by Git. Results may contain notes; review privacy before sharing any file.
Computer timestamps are not your worked hours.

## Other assignment gaps
FL-01 needs your true recurring task list, project setup, and course/module evidence.
FL-02 needs three real tasks with prompt iterations and your critique; the ladder alone does not replace that.
FL-04 needs a no-code workflow, five real inputs, and an actual manual timing comparison.
FL-05 needs its explainer and three real connector-call screenshots.
Portfolio cases need your decisions and outcomes; read and confirm the draft rather than claim an interview or out-loud review happened.
The capstone brief needs clarification from FlyRank before claiming all its requirements are met.

## Accurate time record
Fill this after actual work. Leave unknown values blank. Do not copy portal hour estimates.
| Date | Start | Stop | Break minutes | Actual worked minutes | Task | Evidence | Supervisor check |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

Student hours total: not established.
Supervisor verified hours: not established.
No signature has been inserted.

Arijana has been asked how to verify hours, who signs UIW's forms, whether continued work after September 30 is allowed, and what the current AI Fluency capstone requires.
UIW decides which work counts toward course credit.
