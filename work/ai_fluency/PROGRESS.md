# AI Fluency work status — October 8, 2026

All new code and documents are AI-assisted. No student time has been entered.

| Assignment | Current evidence | What remains |
| --- | --- | --- |
| FL-01: workflow audit and setup | Simple Week 1 workbook prepared separately | Student confirms real weekly tasks; tool setup and course-module evidence |
| FL-06: personal agent design | Design file submitted to FlyRank; waiting for review | Student review and any reviewer changes |
| FL-07: build the agent | Study-coach prototype, twelve passing tests, bounded tool loop, mock file-to-result run, build log | Live model run, human evaluation, raw demo |
| Prompt Ladder | Six cumulative starter prompts and local-model runner prepared | Six real model outputs, student's comparison notes, final prompt |
| Portfolio sitemap | Requirements inspected | Real project configuration, sketch, pressure test and user decisions |
| What Are You Proving? | Requirements inspected | Student's own narrow claim, specific audience, action and why |
| FL-05: concepts and MCP | Requirements inspected | Explainer tied to completed FL-04 workflow and three connector-call screenshots |

## Understand the current build

The first prototype followed a fixed read/search/model path. After reviewing
the FL-05 distinction, a small model-directed loop was added. The model can
choose a note search, see its result, and search again, answer, or ask a question.
Only simulated model decisions have been tested. Real model behavior must
still be checked before claiming FL-07 is complete.

Anthropic reference: https://www.anthropic.com/engineering/building-effective-agents

## Run the Prompt Ladder

From `work/ai_fluency/study_coach`, with a local Ollama model already running:

```sh
python prompt_ladder.py --model MODEL_NAME --output ladder_run_01.json
```

Replace MODEL_NAME with the actual local model name. Each prompt adds one
layer to the previous prompt. Each request starts a fresh conversation so an
earlier answer does not leak into the next comparison. Output is saved after
each successful call. A failed call is recorded and stops the run. This script
has not been run against a real model in the assistant's environment.

The assignment asks for a weak prompt from your own work. The baseline here is
a proposed starter. Replace it with your actual weak prompt if different, and
adjust the layers before running. Do not describe these as past prompts you
used unless that is true.

Read the outputs next to each other and replace NOT REVIEWED with your notes.
Do not force every version to look better. If a layer did not help, say so and
explain the actual output. The course asks for an honest unhelpful or worse
result; that result cannot be made up before running the prompts.

## What to record for UIW

Use the actual time you spend studying, testing, editing, or developing, after
your professor confirms the work counts. A portal estimate is only a guide.
The previous 71-hour portal figure was an estimate, not a verified timesheet.
We cannot calculate how far you are from 140 without your actual work record.
The signed original application ended September 30; confirm any extension.

## Repository checks

Twelve local study-coach tests passed. The repository's smoke-test workflow
also completed successfully for the initial prototype commit. This does not
verify live AI behavior or student hours.
