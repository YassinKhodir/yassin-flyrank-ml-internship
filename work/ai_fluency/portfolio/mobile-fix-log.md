# Phone and readability check

AI-assisted evidence log, November 11, 2026.

Live URL: https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/

## Real phone result
The student was asked to open the site on a phone, visit Work and try the CTR
calculator. He replied: "I checked it its working." This is a reported successful
phone check, not a supplied phone screenshot or a complete link audit. No device
model, browser version, test values or work duration are inferred.

## Actual issue fixed
Before: the host required a ChatGPT sign-in, so outside reviewers could not
open the portfolio freely.
After: access was changed to public with the user's go-ahead. The cloud browser
loaded Home and Work without a sign-in gate and used the calculator successfully.
This was an access fix, not a phone-layout bug. No phone-specific bug was reported.

## Existing layout and validation
The CSS has a narrow-screen rule below 700 pixels. Navigation wraps, case columns
stack, the calculator becomes one column and buttons have visible keyboard focus.
Three pages were inspected in 390-pixel frames earlier. That check is separate
from the student's later real phone check. Normal body text is 16 pixels; small
metadata and footnotes are smaller. Line spacing is 1.7 for ordinary body text.
The calculator refuses zero-impression division and invalid event counts. It
runs locally in the browser and does not upload the entered numbers.

## Checks still needed before claiming the whole assignment complete
- Tablet-width inspection and a complete link-by-link audit, including demo/repo.
- Inspect all small text and the actual foreground/background pairings.
- Any real defects found must be logged and fixed; do not invent before screenshots.
- Phone screenshots are encouraged by the brief but no screenshot was supplied.
- No claim of a complete accessibility audit, speed score or reviewer approval.

The real phone step is reported complete. The full assignment is still being
checked. Automated build/check time is not entered as student work time.
