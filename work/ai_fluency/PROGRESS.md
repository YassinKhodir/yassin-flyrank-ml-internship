# AI Fluency work status - latest update November 11, 2026

All new code and documents are AI-assisted. No student time has been entered.
Latest portal check, November 11: **20 assignment records across both tracks; both capstones accepted.**
The calculator feature and case package are now submitted for review. The case package's unfinished personal-review requirements were disclosed.
The hour log shows **118 estimated hours**, leaving 22 to the portal target of 140.
The dated notes below preserve earlier states; they are not current missing-work claims.

| Assignment | Actual evidence | What remains |
| --- | --- | --- |
| FL-01 | Week 1 workbook prepared separately | True task list, tool/project setup, course-module evidence |
| FL-06 | Design submitted October 8 | Review outcome and any changes |
| Identity kit | One-page SVG, free font, four colors, actual SVG favicon; rendered and checked; submitted October 12 | Reviewer response; repository-context substitution disclosed |
| Content map | Claim, ten draft wording options, three-page map, two case outlines and honest gather-list; submitted October 12 | Reviewer response and student's review; proposed pages are not live |
| FL-07 | Working local model run and saved trace inspected; 2:02 raw capture reviewed; build log updated; Windows 11 passed, 1 skipped | Submitted October 15 with the full-length smaller video copy; waiting for review |
| Prompt Ladder | Six actual outputs and guided comparisons submitted October 20 | Any reviewer changes |
| FL-04 | Current requirements inspected | No-code workflow, five real inputs, manual timing comparison, failure review |
| FL-05 | Requirements inspected previously | Explainer and three real connector-call screenshots |
| FL-09 | README, second evaluation and 3:54.5 narrated demo submitted November 10 | Waiting for review |
| Portfolio cases, sitemap and claim | Proposed content and existing workbook | Student decisions/interview, setup proof, sketch and live website where required |
| Maintenance plan | Exact next-case path, update steps, preserved repository context and real reminder; submitted October 13 | Reviewer response; Claude substitution disclosed |
| Image curation | Actual code/test captures, kept initials SVG, actual rejected vector and reasons; submitted October 13 | Reviewer response; no portrait or live website claimed |
| AI Fluency capstone | Accepted October 18 | Certificate generation if still needed; other assignments remain separate |

## Environment distinction
As of the assistant's October 13 workspace check, Ollama was not installed or listening there. The student has since supplied a handoff describing a live Gemma/Ollama run on their own computer (see the October 15 update below).
The new run_session.py helper's missing-model path was tested: it exited with failure and wrote a record clearly marked not completed.
The helper is ready to collect a real agent run and six prompt outputs on a computer with an installed Ollama model.
See FINISH_CHECKLIST.md. It does not record the student's voice or verify student hours.

## Verification
All twelve study-coach automated tests passed again on October 12.
The model decisions and HTTP responses in those tests are simulated.
Identity-kit SVG rendered correctly.
Portal confirmation was observed for both new submissions.

## UIW and FlyRank requests
An email was sent to Arijana on October 12 asking for:
- Current AI Fluency capstone requirements, because the Impact Project page currently shows a portfolio-maintenance reminder brief while its historical Q&A describes a broader project.
- Continued work after the original September 30 end date and how to update the recorded dates.
- The actual-hours verification process and who signs UIW's timesheet and supervisor evaluation.
- Any existing hours FlyRank can support from its own records.

Arijana replied October 13: continuing AI Fluency is allowed, no end-date update is needed on FlyRank's side, the requirement remains five assignments plus a capstone, and the task descriptions should be followed.
The Documents hour log was inspected directly on October 13 after these submissions. It explicitly shows **82 estimated hours**: 50 from 15 completed assignment records and 32 from one accepted capstone. The AI Fluency capstone is submitted but not accepted and adds no hours yet. This is not a verified actual-work timesheet.
The previously mentioned 71 hours was a portal estimate, not an actual timesheet.
The standard UIW minimum is 140 clock hours for three credits; actual records and UIW acceptance remain unresolved.
No time spent by the automated assistant is entered as the student's work.

## Build context
ChatGPT/Codex was used instead of Claude. Portfolio context and style rules are saved in work/ai_fluency/portfolio.
No configured Claude Project, student interview, out-loud review, live website, or completed narrated demo is claimed. The live-result report received October 15 is distinguished from directly inspected evidence below.

## Reminder and overlapping briefs
A one-time reminder to update the live study-coach case was successfully created for October 14 around 7 PM America/Chicago.
The maintenance plan and current Impact Project capstone show the same brief. The shared artifact and overlap were disclosed in both submissions. These are not claimed as two independent work sessions.
The capstone package explicitly says the live model, website, student review and narrated demo are missing. Its submission is a request for review, not a claim that the broader historical capstone requirements are finished.

## Route toward the portal estimate goal
See HOURS_PLAN.md. More meaningful work is needed beyond the minimum five assignment submissions. Do not mark courses, resources, recordings, or personal exercises complete on the student's behalf when the student has not done them.


## October 15 student handoff
The student supplied a conversation handoff describing a Gemma/Ollama PowerShell run explaining data leakage and checking the answer against the practice notes. The definition/example and source heading are reported to match.
The handoff describes flyrank.mp4 as 54 seconds with silent audio; video/audio were not independently inspected in this update.
A case note was added at portfolio/cases/study-coach-live.md with those evidence limits. The broad claim that no student live run exists is no longer appropriate.
Still needed: save/inspect the actual live-run evidence, an approximately two-minute raw FL-07 capture, a three-to-five-minute narrated FL-09 demo, student review and any remaining evaluation evidence. The short narration script previously suggested does not itself satisfy the video-duration requirement.
Portal approval and hour totals were not rechecked in this update. No hours were added or guessed.

## October 15 inspected evidence and submission attempt
The saved live_answer_01.json was read directly: Ollama gemma4:e2b searched
data-leakage notes, found one match, then answered with a source heading.
The Windows test record shows 11 passed and 1 skipped, rather than 12 passed.
The new raw recording, flyrank(2).mp4, is 122.27 seconds. It shows a fresh
command, a real answer, and the practice notes comparison. Its definition
and example match the notes. This supersedes the handoff-only evidence
status above. It is suitable raw FL-07 evidence; FL-09 narration remains missing.
The build log and public case were updated with the observed facts and limits.

Two FL-07 submission attempts with the original raw video, immutable source
links and notes failed. The portal displayed: "The submission could not be
sent. Check your connection, refresh this page, and try again." One refresh
and retry did not resolve it. No successful submission or approval is claimed.
No hour totals were rechecked or changed. No student work time was inferred.

## October 15 upload resolved
The browser console identified HTTP 413: the original video upload was too
large. Renaming the original did not resolve it. A lower-bitrate copy was made
without cuts, rearrangement, or changes to the answer. The full duration stays
122.27 seconds; the file is 1,255,869 bytes. A frame check confirmed readable
terminal text. The original recording is preserved privately.

FL-07 was successfully saved with `flyrank-fl07-full-run-small.mp4`, source
links and build log at commit `349a1d8`. After a reload the portal displayed
"Assignment submitted", "Your work is waiting for review", and the saved video
preview. Re-encoding was disclosed in the notes. This supersedes the failed
upload status above. No approval or actual-hour verification is claimed.
FL-09 still needs its separate narrated demo. No hour totals were rechecked.

## October 20: work toward the 140-hour goal
Fresh portal check: ML has 10 qualifying assignments and its certificate is
issued. AI Fluency has 6 qualifying assignments, capstone accepted October 18,
and its certificate is qualified but still available to generate. The hour
log shows 104 estimated hours: 60 assignment estimates and 44 accepted-capstone
estimates. Prior review-pending status above is historical.

Work completed in the repository:
- EVALUATION.md reviews all five saved local results against artificial notes.
- README.md now has setup, architecture, current evidence and remaining limits.
- guided_ladder.py collects six fresh local-model answers and the user's four
  comparison notes after each answer; the user chooses one next layer.
- Three simulated tests passed: overwrite protection, preservation on failure,
  and six cumulative prompts with saved review. These are not model runs.
- PROMPT_LADDER_REVIEW.md has the exact run command and private-output guidance.

Ollama is not installed in the assistant workspace. A real ladder session needs
the student's local model. No six-run experiment is claimed yet. FL-09 still
needs a genuine second evaluation and its 3–5 minute narrated demo with an
unlisted video link. The claim and stack briefs explicitly require the student's
own thinking and words; none is represented as completed from an AI draft alone.
No new portal submission or added hours is claimed for these preparations.
No automated processing time has been entered as student work time.

## Prompt Ladder submitted - October 20, 2026 (America/Chicago)
The student uploaded recovered results.json containing all six real Gemma
outputs, cumulative prompts, named layers, reasons and four review notes per
version. The user performed the local runs with step-by-step AI guidance;
AI-drafted prompt and review wording is disclosed, not described as unaided.
Version 2 failed to fix unsupported claims; version 5 removed useful details.
Version 4 was selected as best tested. The cleaned reusable prompt has not had
a separate seventh test. The recovery preserved versions 0-4 and reran only 5.

A PDF containing full prompts, outputs, notes and the reusable prompt plus the
original JSON were uploaded privately to the Prompt Ladder assignment. After
reload, FlyRank showed "Assignment submitted" and both attachments; waiting
for review. No private result file was committed to this public repository.
The hour log then showed 106 estimated hours: 62 assignment estimates and 44
accepted-capstone estimates. The remaining portal-estimate gap to 140 is 34.
This supersedes earlier statements that the six ladder runs were missing.
No actual hours, new approval, or finished FL-09 demo are claimed.

## Second study-coach evaluation received
The student ran five updated questions on Windows after commit 9505a2b and
uploaded evaluation-v2.json. It was inspected directly: three real Gemma
search/answer traces, one pre-model missing-topic refusal, and one local
written-date conflict guardrail. The date check now asks directly which version
is current. EVALUATION.md and README.md document observations and remaining
limits. The unsafe passage is excluded but that answer omits an explicit
missing-support response for part of the question. Raw evaluation stays private.
FL-09 still needs its 3–5 minute narrated demo and unlisted video link. No new
portal submission or estimated-hour increase is claimed. Last checked: 106.


## November 10: FL-09 submitted
The student's narrated demo is published as an unlisted video:
https://www.youtube.com/watch?v=7VjbMP6wQds
It lasts 3 minutes 54.5 seconds (the player rounds to 3:55). Sampled frames
show a live data-leakage answer, practice-note checking, the local date-conflict
guardrail and a CTR calculation. The video description discloses AI assistance.

FL-09 was submitted with the video and immutable README/EVALUATION links at
commit 151a8c48a36cbccde926b6c2079c03661fce5807. The portal confirmed
"Assignment submitted" and "Your work is waiting for review." This replaces
the earlier missing-demo status. Submission does not mean reviewer approval.

The Documents hour log now shows 111 estimated hours: 18 completed assignments
worth 67 estimated hours and two accepted capstones worth 44. The remaining
portal-estimate gap to 140 is 29. No actual student work time was entered.


## November 10: framed portfolio cases drafted
The current case-writing brief was checked in the portal. A single draft,
[portfolio/framed-cases.md](portfolio/framed-cases.md), now covers both projects
called for by the content map. It includes a six-word voice card, the problem /
work / result for each project, limits, evidence links, a short bio, one review
action, and a generic/plain wording comparison. ML numbers were checked against
the saved capstone notebook; starter example numbers were not reused.

The live study-coach case and project context now reflect the second evaluation,
Prompt Ladder submission and FL-09 demo submission. No new notebook or model
run was made. The new case draft was fetched again and matched its saved text.

This assignment is not submitted yet. Its remaining steps require the student's
own interview answers and read-aloud review. These can be done from a phone;
no new local run or recording is needed for this case-writing step. The portal
estimate remains last checked at 111; no actual hours were entered.


## Case package prepared without further interview questions
Both project cases are saved in portfolio/framed-cases.md with source links,
a plain before/after example and a requirement check. The content map now points
to the package and reflects the submitted demo and completed evaluation.
Student-confirmed study-coach purpose and date-handling preference are included.
No ML reflection or read-aloud review was invented. The case assignment remains
unsubmitted pending its personal-review requirements. No estimated or actual
hours were added for preparing these documents.


## November 11: working portfolio website built
Home, Work and About pages now exist, with both cases, source/evaluation links
and the recorded demo. A single browser-only CTR calculator works with normal
inputs and rejects zero-impression calculations clearly. Eight arithmetic/input
checks passed; page structure and local asset checks passed. Browser navigation
and two visible calculator outputs were checked. Three pages were visually
inspected in 390-pixel frames, not on the student's phone.

The Site deployment succeeded as owner-private. It cannot be submitted as a
public reviewer URL yet. Public access needs the user's explicit request.
The source guide, DNS explanation, feature explanation and check record are saved
under portfolio. See [website/README.md](portfolio/website/README.md) for the
exact remaining requirements. No LinkedIn/CV/booking links, official badge,
phone test, read-aloud review or student comprehension is invented.
No new assignment submission or added hours is claimed. Last portal estimate: 111.


## November 11: public portfolio and two review submissions
The portfolio audience was changed to public after the user's go-ahead. The
cloud browser opened Home and Work without a sign-in gate. The public calculator
returned 10% for 10/100 and a clear refusal to divide by zero. The site is:
https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/

- Make It Do Something: submitted the live calculator, feature explanation and
  check record. Portal confirmed "Assignment submitted" and waiting for review.
  AI assistance and the lack of an independent student explanation were disclosed.
- Frame It as Cases: submitted the two-case document and live Work page. Portal
  confirmed submission and waiting for review. The remaining ML interview and
  read-aloud review were disclosed in notes and the document. This is not a claim
  those learning steps were completed.

The hour log shows 118 estimated hours: 20 assignment records worth 74 and two
accepted capstones worth 44. These automatic estimates are separate from review
approval or actual student time. No work-time entry was created.

Not all remaining assignments are complete. The real phone test, full personal
review, verified CV/booking links and backlinks, required course/tutorial work,
cross-model experiment and manual timing comparison remain unverified. The
profile contains a LinkedIn URL, but no private CV upload. No CV or booking
address was invented or published. Hardening still needs its full checks and
human review. Do not resubmit FL-09 or call the public portfolio PF-04 approved.
