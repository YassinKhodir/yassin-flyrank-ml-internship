# Portfolio website: current state

Updated November 12, 2026. Code and documents are AI-assisted.

## Live website
https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/
Analytics: https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/analytics

Site ID: appgprj_6af491b73ecc81918f60d29f64f74411
Current deployment: version 5.
Hosted source commit: 9f0eaa04848ee9c525eff0cc72008f149b21de2a

## What works
- Home, Work and About pages with two project cases and evidence links.
- A browser-only click-through rate (CTR) calculator. It makes no model call.
- Local fonts, keyboard focus, input labels and a skip link.
- Canonical URLs, sharing metadata, a share image, favicon, robots and sitemap.
- The official badge for the already-issued Machine Learning certificate.
- A server-side page-view counter and public seven-day dashboard.

The calculator returned 10% for 10 clicks / 100 impressions on the live site.
A test visit increased Work from 0 to 1. Dashboard counts include testing and
automated requests; they are not counts of different people.

## Source and rebuild
The complete source, including binary fonts and share image, is in the existing
Site source repository. This folder keeps earlier static source references.
It is not a complete mirror of the current deployed app.

In the full Site checkout:
- public/ contains the web pages, styles, calculator, dashboard and assets.
- build_pages.py generates the three main pages in public/.
- worker/index.js serves assets, records eligible views and returns totals.
- scripts/build_worker.py embeds assets in dist/server/index.js.
- R2 BUCKET stores view events. The app does not use a database binding.

Run these commands from that full checkout:

```sh
python build_pages.py
python scripts/build_worker.py
node scripts/test_analytics.mjs
node scripts/validate-artifact.mjs
```

Publish through the existing Site project. Do not replace its ID or deploy the
old static mirror over the current Worker. The backend test file uses simulated
storage. It does not create production visitors or student work hours.
Reference code is in ../analytics/. Full checks are in ../launch-evidence.md.

## Counter limits
The counter stores page/date events without IP addresses, user agents, referrers,
cookies or reusable visitor IDs. Hosting providers may keep their own normal
service logs. Do Not Track, Global Privacy Control and no_count=1 requests are
excluded. The dashboard is a rolling seven-day view; stored event files are
not automatically deleted. Storage failures are reported rather than shown
as made-up zero totals. Large capped reports are marked as lower bounds.

## Assignment status
Calculator, cases, phone check, sitemap, hardening and launch packages are
submitted for review. Submission does not mean approval.
The launch notes disclose the free subdomain, AI assistance, pending hardening
review and lack of a new physical-phone check after the backend update.
The student reported the earlier phone test worked on November 11.

Remaining personal-review, account, CV/booking, backlink and independent
explanation requirements are not claimed complete. See ../PROJECT_CONTEXT.md
and ../../PROGRESS.md for current evidence and historical updates.

The portal now shows 147 estimated hours. This is not a verified student
timesheet or a statement of UIW acceptance.
