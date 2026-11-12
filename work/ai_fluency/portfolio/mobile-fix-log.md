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

## Additional checks completed
- A 768-pixel browser frame of Work was inspected. The title, navigation and
  case columns fitted in the sampled view. This was not a physical tablet test.
- Desktop Home → About → Work navigation worked. Earlier desktop Work and
  calculator checks passed, alongside the student's reported real phone check.
- All distinct external destinations were opened: public repository, capstone,
  setup README, evaluation, coach.py, review PR and the YouTube demo. GitHub
  pages loaded with their expected titles; the video player loaded at 3:55.
- Internal section destinations match the IDs in the generated HTML.
- Contrast calculations on white: teal #0F766E 5.47:1; body #111827 17.74:1;
  secondary #4B5563 7.56:1; muted #6B7280 4.83:1. These pairs exceed 4.5:1.
- The site uses one small SVG monogram and local fonts; no large gallery or
  embedded video image was added. The video is linked rather than embedded.

## Limits
No phone screenshot was supplied. The student's statement is the evidence for
physical phone use. Small metadata/footnotes are below the 16-pixel body size;
users can zoom. This is a focused readability check, not a full accessibility
certification or speed test. No phone-layout defect was reported, so no invented
before/after phone images or layout fixes are included. The actual access fix
is described above. AI assistance was used for the site and this check log.
No actual student work duration is inferred.
