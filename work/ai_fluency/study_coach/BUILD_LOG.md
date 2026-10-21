# Build log — October 8, 2026

AI-assisted work. Entries describe observed work, not student attendance or hours.

1. Checked FL-07 in the FlyRank portal. It needs a working agent, a real data
   connection, a build log, and an unedited run capture.
2. Checked the existing repository and its agent instructions. No study-coach
   result appeared in the repository search. Chose a new `work/ai_fluency`
   folder and a branch so the completed ML work is not replaced.
3. Implemented the text reader, heading-based passages, word matching, mock
   response, and local model adapter. Added limits on file size and prevented
   linked files from reading outside the notes folder.
4. Added eight tests. The first run passed all eight. No failed test is claimed.
5. Ran the mock CLI on the data-leakage question. It read the sample file,
   returned the correct passage and heading, and wrote `mock_example.json`.
6. Ollama is not installed in this execution environment. The HTTP adapter was
   tested with a simulated response; a real model was not run.

## Changes from the design

- Chose a local Ollama adapter to avoid needing a paid API or sending notes to
  a remote model. This integration still needs a real run on the student's machine.
- Refuse to replace output files instead of adding an interactive overwrite
  prompt. This is simpler and protects previous results.
- Keep suspicious passages out of retrieval. This only blocks obvious patterns.
- Deferred practice-question quality, model citation checking, and the demo
  until a real model can run. Mock mode returns excerpts, not generated lessons.

7. Reviewed Anthropic's workflow-versus-agent distinction while checking
   FL-05. The current fixed path is a workflow. A model-directed tool loop is
   still needed before presenting it as a full agent.
8. Prepared a six-version Prompt Ladder runner. It saves actual model outputs
   and leaves human comparisons unfilled. No real six-run experiment is claimed.

9. Added a bounded model-directed tool loop after identifying the workflow
   limitation. The model can search notes, answer, or ask for clarification.
   Added four tests covering search-to-answer, premature answers, disallowed
   tools, and the four-turn limit. All twelve tests passed. Model choices in
   these tests are simulated; this is not a live AI evaluation.

## Remaining evidence

Real model outputs, the student's five-case review, and a raw screen recording.
FL-07 is not ready to mark complete. No student hours are claimed.

## October 15, 2026 — live run and raw capture

This section updates the earlier missing-evidence status. AI assistance was used
for code, troubleshooting, documentation, and submission preparation.

- The earlier Windows recording showed real failed attempts: an unavailable
  model, an unsupported tool action, an answer before a search, and invalid JSON.
  The committed Ollama request now includes `"format": "json"`.
- Read the saved `live_answer_01.json`: Ollama with `gemma4:e2b` chose
  `search_notes` for data leakage, found one match, then chose `answer`.
  It cited the Data leakage heading in the local artificial practice notes.
- Read `test_results_windows.txt`: 12 tests ran; 11 passed and one symlink
  test was skipped because Windows permissions were unavailable.
- Reviewed the new raw recording, `flyrank(2).mp4` (122.27 seconds).
  It shows a clean prompt, the typed question and command, a real answer,
  and opening the notes to compare the definition and example. No mid-run
  hand-editing of the answer appears. The raw file is for the private portal
  upload, not the public repository.
- The answer explains data leakage and gives the future-clicks example. It
  matches the notes. This one capture does not prove every answer is correct.
  It does not include a practice question. Citation checks only match headings.
  Earlier testing also showed conflicting dates without a direct clarification
  question. These remain limits, rather than claims of perfect behavior.
- Platform change: the custom local Python/Ollama agent replaces a hosted
  assistant so it can use local files without a paid API. Scope stays narrow:
  search practice notes and explain a supported topic.

FL-07 now has a working local run, build log, and raw capture ready to submit.
Reviewer approval is still separate. This is not the narrated FL-09 demo.
No student work time is inferred from video length, tests, or portal estimates.

## October 20 - due-date clarification fix
The first saved live date answer listed both dates but told the reader to
choose rather than directly asking which was current. Added a small local
guardrail after the model searches notes. For due/deadline questions, it looks
for different written month dates in relevant deadline passages, cites the
sources, and asks "Which version is current?" It does not pick a date.
The trace labels this step local_guardrail; it is not a model-made decision.
It also checks the question's initial retrieval, so the model's narrower search
cannot hide a conflicting date from that retrieved set.

All 15 study-coach tests passed in the assistant workspace. Three new tests
check conflict clarification, a normal single deadline, and unrelated or blocked
passages. Model calls in tests are simulated. A new real Windows/Gemma test
is pending. Historical live outputs have not been overwritten.

Limits: this small rule detects full English month-name dates in due/deadline
passages. It does not understand all date formats, resolve real deadlines, or
search beyond retrieved passages. Different deadlines may refer to different
tasks; clarification is conservative, not proof that the notes are wrong.
No student time or additional assignment completion is claimed.
