# Prompt Ladder: run and compare

Preparation only. Six actual outputs and the student's review are still needed.
AI helped prepare this sheet. It does not record completed work or hours.

## Simple meaning
A prompt is the instruction you type into an AI tool. The ladder tests whether
adding one instruction makes the answer more useful. Keep the same model.

## Start
Use a fresh chat with the local model `gemma4:e2b` for each version so older
messages do not affect the next answer. Save the full prompt and full output.
Keep private notes out of this public repository.

Baseline: `Explain this data.`

After reading that output, add just ONE layer that addresses its biggest
problem. Possible layers: clearer goal, audience, context, format, verification.
Make five additions, giving six total runs. Keep each earlier instruction.
Do not invent a failure or say every addition helped without comparing outputs.

The existing `prompt_ladder.py` has six fixed starting prompts. It can collect
outputs, but a fixed order alone does not show why each next layer was chosen.
For this assignment, choose after reviewing the previous output. If using that
runner, explain the fixed sequence honestly and change it when the evidence
calls for a different next layer.

## Fill this after each real run
Copy this block six times, using versions 0–5.

### Version [number]
- Model:
- Full prompt:
- Full output:
- What single layer changed:
- What actually improved compared with the last answer:
- What still failed or got worse:
- What I would try next and why:

Version 0 has no earlier answer; record its main weaknesses instead.

## Check arithmetic and claims
For a CTR example, 10 clicks / 100 impressions times 100 = 10%.
That alone does not show sales, profit, or whether a campaign worked.
Check whether the answer says what evidence is missing.

## Finish
Save the final best prompt as a reusable instruction with clear input fields.
Keep a separate template field for the user's actual data. Include enough
context for another student to use it. Do not submit this blank sheet as a
finished assignment. Do not reuse the five study-coach outputs as the six ladder
runs: they answer different questions, so they are not this experiment.

## Work time
Write down your actual start, stop and break times in your private timesheet.
Runtime timestamps and assignment estimates do not measure your work time.

## Guided runner (new)
From this study_coach folder, run:

```sh
python guided_ladder.py --model gemma4:e2b --output sessions/ladder-01
```

Start Ollama first. Keep the same model for all six versions. Answer each
question in your own words. The runner pauses after each answer so you can
choose the next single layer. It saves each model output before asking for
review notes. The next prompt includes earlier instructions plus your one
addition. Only you can check whether that addition really is one layer.
Each model call uses a fresh conversation, with no forced JSON answer format.

If it stops, partial evidence stays in sessions/ladder-01/results.json. Use a
new folder for a fresh experiment; the program refuses to overwrite it.
Keep that folder private until its content has been checked. Do not submit
incomplete results as six completed runs. Three simulated tests passed; the
runner has not been tested with a live Ollama model in this workspace.
