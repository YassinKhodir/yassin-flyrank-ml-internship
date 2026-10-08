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
