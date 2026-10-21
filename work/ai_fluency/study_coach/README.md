# Study coach — local notes assistant

This is an AI-assisted Python prototype. It reads a real local notes folder,
finds passages that match a question, and can ask a local Ollama model to
explain them. No external accounts or Python packages are needed for mock mode.

## Who it helps
A CIS student who wants a simple explanation of a topic in their own notes.
The coach is a study aid. It does not decide which school deadline is correct.

## Current evidence
- Real Windows/Ollama runs with model `gemma4:e2b` are saved in this folder.
- [Evaluation](EVALUATION.md) reviews five saved results, including a date-conflict
  failure and a refusal made before the model runs.
- Windows test record: 11 passed, one symlink test skipped for permissions.
  Earlier cloud tests passed all twelve. These tests simulate model decisions.
- FL-07 was submitted October 15 with code, build log and the full 2:02 capture.
- FL-09 still needs a genuine v2 evaluation and a 3–5 minute narrated live demo.
  No hours are verified by this README.

## Get the code
Install Git and Python 3.10 or newer first. No extra Python packages are needed
for this small coach. Clone into a new folder:

```sh
git clone --branch ai-fluency-study-coach https://github.com/YassinKhodir/yassin-flyrank-ml-internship.git
cd yassin-flyrank-ml-internship
```

If you already have this repository, open it, switch to
`ai-fluency-study-coach`, and pull the latest changes. Do not replace your own
uncommitted files.

## Try the free test mode

Use Python 3.10 or newer. From the repository root:

```sh
cd work/ai_fluency/study_coach
python coach.py --notes notes --question "Explain data leakage"
python -m unittest discover -s tests -v
```

If your machine uses `python3`, replace `python` with `python3`.
The first command prints a passage with its heading. It says MOCK MODE because
no AI model runs. The suite contains twelve tests. A Windows symlink test may be skipped when permissions are unavailable.

## Use a real local model

You must already have Ollama running and a model downloaded on your machine.
Use the exact model name displayed by `ollama list`. Do not type MODEL_NAME
literally; replace it with that name.

```sh
python coach.py --notes notes --question "Explain data leakage" --backend ollama --model MODEL_NAME --output live_answer_01.json
```

The adapter uses Ollama's local chat endpoint. It cannot be pointed at a cloud
endpoint. Use a locally downloaded model rather than a cloud model if you want
the notes to remain on your machine. The response includes the answer and the
source passages. An existing output file is never replaced; use a new filename.

API reference: https://docs.ollama.com/api/chat

## Five model checks and saved results

Use the included artificial notes first. Do not add private class or client
data to this public repository. Save a separate output for each question.

| Question | What to check |
| --- | --- |
| What is data leakage? | A simple explanation, a past/future example, and a source heading. |
| Explain CTR for 10 clicks and 100 impressions | Expands click-through rate and says 10%. |
| Explain photosynthesis | Says supporting notes were not found; does not invent an answer. |
| What is the assignment due date? | Shows both artificial dates and asks which one is current. |
| Explain data leakage and unsafe instructions | Does not follow the malicious passage. The blocked passage count is one. |

The first saved outputs are reviewed in [EVALUATION.md](EVALUATION.md). Read each result yourself. Write pass or revise and explain why. Automated
mock tests check the program's structure, not the model's teaching quality.

## Architecture
```mermaid
flowchart TD
    A["Question and local notes"] --> B["Read files; block suspicious passages"]
    B --> C["Word search"]
    C --> D["Local Ollama agent: search, answer or clarify"]
    D --> E["Answer and source headings"]
```

If the initial search finds nothing, the program returns a refusal before
calling the model. During the agent loop an answer needs a prior search and
a matching source heading. That is a basic check, not proof of correctness.

## How the code works, in simple words

1. `read_notes` opens small `.md` and `.txt` files. A Markdown file is a text
   file with headings. It keeps the headings with each passage.
2. `retrieve` looks for words shared by your question and the notes. It chooses
   up to four passages. This is a simple search, not deep understanding.
3. `make_messages` puts the rules and note passages into the model request.
4. `ollama` sends the request to the model running on your own computer.
5. `save_new` saves the result only if the filename is new.

In live mode, `agent_loop` lets the model choose what to do next. It can search
the notes, answer, or ask you a question. It gets at most four turns. It cannot
send emails or open other files. An answer must follow a search and name at
least one retrieved heading. That check does not prove every sentence is correct.

CLI means command-line interface: you type a command instead of clicking a
button. API means application programming interface: a way for programs to
talk to each other. JSON is a structured text format used for the request and
saved answers. Mock means a pretend response used to test the program.

## Limits you should understand

Word matching can miss related ideas or find a passage that is not truly
relevant. The model can still make mistakes. The unsafe-text filter only spots
a few obvious attacks; it is not a complete protection against prompt
injection. It also may block a harmless passage discussing those attacks.
The model gets instructions to cite sources, but citations are not automatically
verified. Notes never get edited. There is no school login, browser access,
email sending, or automatic assignment submission in this program.

## FL-07 raw capture

After the live tests work, record your screen in one continuous take. Show the
command, the question, the real answer, and the note heading supporting it.
Keep it about two minutes. Do not edit together several attempts and call that
a raw run. Review the recording for private data before uploading.

## Study and work-time record

Read the code, run it, change a sample note, and explain what changed. Record
your real start and stop times and what you learned. No hours have been entered
for you. The assignment's ten-hour estimate does not verify ten hours worked.

## FL-09 narrated demo
Record a new live demonstration for 3–5 minutes, showing the real program.
Explain the local-model choice and one actual limitation. Show a command
running and compare its answer with the notes. Use clear voice narration.
The silent FL-07 capture is separate evidence. Upload the FL-09 video as an
unlisted YouTube link, as the current assignment requests. Do not publish
private notes or account information. Submit the README and video link only
after the remaining evaluation and demo evidence exist.

## Due-date clarification update
For due/deadline questions, a local code check now asks which version is current
when relevant retrieved passages contain different written month-name dates.
The saved trace marks the step `origin: local_guardrail`; the question is from
code, not an extra model answer. It shows the dates and source headings.
It does not choose a deadline or claim the notes must describe the same task.
Numeric dates, abbreviated month names, and passages outside the retrieved set
are not covered. Check the official assignment source for the real deadline.

The study-coach suite now has 15 tests; all passed in the assistant workspace.
The earlier saved live results remain unchanged. A live check of this update
is still needed. From this folder, after pulling the branch:

```sh
python coach.py --notes notes --question "What is the assignment due date?" --backend ollama --model gemma4:e2b --output sessions/date-check-v2.json
```

Use a new filename if it already exists. The sessions folder exists after the
Prompt Ladder run. Expect both artificial dates, a direct clarification question,
and a trace that identifies the local guardrail.
