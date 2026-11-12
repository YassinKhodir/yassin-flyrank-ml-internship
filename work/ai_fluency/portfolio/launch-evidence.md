# Plant Your Flag: launch evidence
AI-assisted submission for review, November 12, 2026.
No actual student work hours or reviewer approval is claimed.

## Final address and fallback
https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/
This is the existing personal-name hosting subdomain over HTTPS, not a newly purchased domain.
No domain purchase or paid analytics subscription was made.
The assignment's public Q&A, answered August 6, says any free subdomain qualifies.
The fallback is disclosed rather than described as a domain Yassin purchased or configured.
No statement about Yassin's personal financial situation is made.

## Working analytics
Dashboard: https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/analytics
It is a first-party page-request counter. There is no separate analytics account or third-party tracking script.

Observed live check:
1. Dashboard initially showed Work = 0.
2. Opened the actual Work page over HTTPS.
3. Refreshed the dashboard and observed Work = 1.
4. Opened About through navigation. A later screenshot showed Home = 15, Work = 2, About = 2.
These are request counts including setup tests, repeat loads and automated visits, not unique people or proof of outside audience growth.
The analytics screenshot is attached privately in the portal.

## How the small counter works
A Worker is a small program running at the website host.
It serves the same website files and records eligible Home, Work and About requests.
For each counted request it writes a tiny event file in the site's R2 file storage.
The file key contains the UTC day, one of three page names and a random event identifier.
That identifier is new for each event; it is not reused to identify a visitor.
The dashboard asks for aggregate counts from the last seven UTC days.
Only aggregate counts are shown publicly.

The counter does not save IP addresses, user agents, referrers, query strings, cookies or reusable visitor IDs.
The host may retain its own standard service logs.
Do Not Track and Global Privacy Control requests are skipped.
Opening a page with ?no_count=1 skips that request.
Images, fonts, the analytics dashboard and the counts endpoint are not counted.
Stored event files are not automatically deleted; the dashboard displays only the last seven days.
Reads are bounded at five batches per UTC day. If a result is truncated, the dashboard labels counts as lower bounds.

## Launch hygiene
- Home, Work and About load correctly after the repaired deployment.
- Work's calculator still returned 10% for 10 clicks and 100 impressions.
- Existing page titles, descriptions, canonical links, Open Graph and Twitter cards are retained.
- The About DOM was checked after deployment: correct title, favicon.svg and absolute share-card image URL.
- The published 1200 x 630 share image and favicon were checked during the preceding metadata work.
- A working badge is visible in every main page footer, labeled Machine Learning.
- No new title, badge or metric claims AI Fluency certificate issuance.

## Actual issued graduate badge
Official source: https://internship-badge.netlify.app/
The generator's HTML was used; a badge was not invented.
Credential: FR-D11-46B4B-A9584.
Verified result: https://internship.flyrank.ai/verify/FR-D11-46B4B-A9584?first_name=Yassin
The verifier confirmed Yassin Khodir, Machine Learning, July 2026 cohort, issued October 6, 2026.
The badge links to that issued credential. No AI Fluency certificate was generated to obtain it.

## Deployment and checks
Latest native deployment succeeded as public Site version 5.
Full Site source commit: 9f0eaa04848ee9c525eff0cc72008f149b21de2a.
The original static pages and assets are retained in the Site source's public folder.
The server embeds and serves those assets; the calculator arithmetic still runs in the browser.
Reference source files are in [analytics](analytics/). Full deployable source, including fonts and image assets, is in the Site source repository.

Checks passed in the assistant workspace with mocked storage:
page serving, aliases, event privacy, independent event keys, opt-outs, methods,
aggregate totals, unavailable/failed storage and truncated results.
Those checks are not student sessions or live visitor traffic.
The initial compressed-response deployment displayed encoded bytes at the host.
It was corrected to serve plain bytes. Browser inspection confirmed the repaired pages and real stored counter before submission.

## Evidence limits and review request
The student reported a successful phone check on November 11 at the same address.
No fresh physical-phone check after the analytics migration is claimed; the current live checks are assistant browser checks.
The hardening checkpoint is submitted and waiting for mentor review. It is not claimed passed.
No third-party social-network cache refresh or search indexing is established.
Please review the free-subdomain fallback, first-party analytics and badge, and request any additional launch checks or revisions.
The assignment's 20-hour workload is an estimate, not a record of 20 actual student hours.
