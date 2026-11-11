# Portfolio website: current state

Prepared November 11, 2026 with AI assistance.

## Deployed site
https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/

The hosting deployment succeeded. Public access was enabled November 11 after
the user's go-ahead. The cloud browser loaded Home and Work without a ChatGPT
sign-in gate, then ran the live calculator: 10 clicks / 100 impressions returned
10% with the benchmark warning. This replaces the earlier private-only status.

Source Site ID: appgprj_6af491b73ecc81918f60d29f64f74411
Hosted source commit: 4c5b23c097f9189939d823dd89fc97b52c13ecde

## What is built
- Home, Work and About pages with the existing white/teal identity kit.
- Two evidence-based cases, limitations, source links and the unlisted demo.
- One working CTR calculator: local arithmetic, no backend or model calls.
- Locally hosted DejaVu Sans fonts; no external font service or tracker.
- A narrow-screen layout, keyboard focus styles, labels and a skip link.

## What each source file does
- build_pages.py generates three HTML pages in a dist folder.
- style.css controls the colors, spacing and responsive layout.
- calculator.js checks whole event counts and prints the formula and result.

The hosted source also contains the favicon, font files and font license.
Those files came from the saved identity kit and system DejaVu package.
The generated HTML is static; no dependencies or build service are needed.

## Rebuild from this source folder
Create a dist folder and copy style.css and calculator.js into it.
Copy ../favicon.svg into dist. Create dist/assets and add DejaVuSans.ttf and
DejaVuSans-Bold.ttf from a licensed DejaVu installation, with its license.
Run: python build_pages.py
Serve dist using a static host. The Site's deployment configuration is kept in
its separate source repository; do not invent a new Site ID during updates.

## Related assignment documents
- [DNS walkthrough](../dns-walkthrough.md)
- [Feature explanation](../feature-explainer.md)
- [Website check record](../website-checks.md)
- [Case-study wording and review status](../framed-cases.md)

## What remains
| Assignment | Prepared evidence | Not yet complete |
| --- | --- | --- |
| Empty but Live | Deployed website, screenshot, loaded identity/case context | Student's actual second-device check; stack assignment status |
| PF-04 personal website | Three pages, source links, DNS explanation | Verified LinkedIn/CV/booking links; links back from LinkedIn/CV; student understanding; official badge asset |
| Make It Do Something | Browser calculator and checks, plain explanation | Live feature checked; student's own explanation remains to be confirmed |
| Open It on Your Phone | 390-pixel visual layout check | Real student phone test and any fixes |
| Frame It as Cases | Both cases, voice card, bio, before/after example | Remaining student interview and read-aloud review |

The feature can now be sent for review with AI assistance and the remaining
student-review limitation disclosed. This file alone does not record a successful
portal submission; see PROGRESS.md for that status. A browser iframe is not a physical phone. AI-drafted technical
explanations are not described as unaided student reflections. No extra portal
or actual work hours are claimed. Last observed portal total remains 111 estimates.
