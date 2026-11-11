# Portfolio cases: review draft

Voice card: **Simple, direct, clear, honest, calm, specific.**

AI-assisted draft, November 10, 2026. Written from saved project evidence.
This file covers both projects in content-map.md. It is not a completed student
interview or a record of reading the text aloud. ChatGPT/Codex and this saved
context are used instead of a configured Claude Project.

## Reader and action
Reader: a FlyRank internship reviewer.
One action: inspect the project evidence and give feedback.

## Case 1: Which web pages should an editor check first?

### The problem
An editor has many web pages and limited time. The project asks which pages
should be checked first. A high score means "check this page," not "edit it
automatically." SEO means search engine optimization: work that helps people
find useful web pages through search.

### What was done
The saved machine learning project compares a fixed rule with a learned score.
Machine learning means finding patterns in examples. The fixed rule uses
page visibility and search position. The learned score uses logistic regression,
a model that estimates the chance of a yes-or-no outcome.

The project uses early-March information to estimate later-March decline.
Later information is kept out of the input. Whole clients are held out of
training, so the test checks different clients. The capstone notebook records
the methods, checks, and reasons an editor should review a page.
The work and documentation were AI-assisted.

### What came of it
The capstone reports that 31 of the model's first 100 choices had the later
decline label, compared with 15 for the fixed rule on the same test set.
That label means declining visibility; it does not prove editing would help.
The overall ranking measure, ROC-AUC, was only 0.510. Roughly 0.5 means little
ability to separate the two groups overall. The useful result is narrow:
a better first batch in this test, with weak overall separation.

FlyRank accepted the Machine Learning capstone on October 6. No new experiment
was run for this case draft. The reported numbers come from the saved capstone,
not from the starter README's example numbers.

### Limits
One month and one client split are not enough to promise future results.
No controlled editing experiment showed more clicks or income. A person must
check each recommendation before taking action.

### Inspect the evidence
- [Saved capstone](../../notebooks/capstone.ipynb)
- [Project repository](../../../README.md)

## Case 2: A study coach that checks local notes

### The problem
Technical notes can be hard to understand. A study helper should explain the
notes in simple words and show where its answer came from. It should not
invent a topic or silently choose between conflicting deadlines.

### What was done
The AI-assisted Python program reads small local text files and searches for
matching words. Ollama runs the downloaded Gemma model on the student's
computer. The model can search, answer, or ask a question, with at most four
turns. Code rejects an answer made before a search.

The student ran the program on Windows and checked the answer against the
practice notes. An early date answer did not ask clearly which date was current.
A local code rule was added. It now lists the different written dates and asks
which version is current. This is a code check, not proof that the model
learned to reason better.

### What came of it
The updated evidence contains five case checks: three real Gemma answers and
two checks handled by local code. The data-leakage answer matches the practice
notes. Data leakage means using information that would not be available when
making a real prediction. The click-through rate answer correctly calculates
10 clicks divided by 100 impressions as 10%.

The missing-topic check refuses to invent an answer. The date check asks which
version is current. One planted unsafe passage was blocked. Fifteen automated
coach tests passed in the assistant workspace; model decisions in those tests
are simulated. They are separate from the student's real model runs.

The student's narrated demo lasts 3 minutes 54.5 seconds. FL-09 was submitted
with that video, the setup guide, and the evaluation on November 10. It is
waiting for review.

### Limits
A source heading does not prove every sentence is correct. Word matching can
miss relevant notes. The date rule covers only some written date formats.
Blocking one unsafe passage is not a complete security test. Some answers
repeat information or miss part of a question.

### Inspect the evidence
- [Setup, architecture, and code guide](../study_coach/README.md)
- [First and second evaluations](../study_coach/EVALUATION.md)
- [Coach code](../study_coach/coach.py)
- [Unlisted live demo](https://www.youtube.com/watch?v=7VjbMP6wQds)

## Short bio: proposed wording
Yassin Khodir studies Computer Information Systems at the University of the
Incarnate Word. His internship projects include a web-page review ranking
study and a local study coach. This portfolio shows the code, checked results,
and limits. AI assistance is disclosed.

## Contact and next action
**Inspect the project evidence and give feedback.**
Open the linked source and evaluation above. Feedback can be left on the
[project review pull request](https://github.com/YassinKhodir/yassin-flyrank-ml-internship/pull/1).
No private phone number or email is needed in the public page.

## Before and after
Generic AI line: "I leverage cutting-edge AI to deliver transformative,
high-impact solutions."

Plain edit: "The study coach explains local notes. I check its answer against
the notes because it can still make mistakes."

Both lines are AI-drafted examples. The plain edit still needs the student's
review; it is not represented as an unaided student edit.

## Before this assignment can be submitted
- Ask the student about each project's problem, one decision, and the result,
  one question at a time. Save only approved public wording.
- Let the student correct the proposed voice card, bio, cases, and plain edit.
- Have the student read the final text aloud and remove anything they cannot
  explain or stand behind.
- Keep private interview notes outside the public repository.
- No interview, read-aloud check, actual work time, or assignment completion
  is claimed by this draft.
