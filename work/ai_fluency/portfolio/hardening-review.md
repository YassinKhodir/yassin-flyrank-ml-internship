# Website hardening: actual checks and remaining limits
AI-assisted checks, November 12, 2026. Prepared for mentor hardening review; no passed checkpoint is claimed.

## Site
https://yassin-khodir-internship-portfolio.quickchutney32.chatgpt.site/
Source Site commit: 7f8dcb672d157071c47803d2266ae1214b50f836.
Native deployment succeeded; existing public audience was preserved.

## Calculator edge cases actually tried in the live browser
| Input/action | Observed result | Triage |
| --- | --- | --- |
| Both fields empty | Enter both clicks and impressions | Expected refusal |
| -1 clicks / 100 impressions | Whole, non-negative, safe-range counts required | Expected refusal |
| 1.5 clicks / 100 impressions | Whole, non-negative, safe-range counts required | Expected refusal |
| 10 clicks / 0 impressions | CTR cannot be calculated because impressions are zero | Expected refusal |
| 0 clicks / 100 impressions | 0% CTR and benchmark warning | Passed |
| 10 clicks / 100 impressions | 10% CTR and benchmark warning | Passed after a fresh UI observation |
| 9007199254740992 clicks / 100 impressions | Safe-range refusal | Expected refusal |
| Fast double click on Calculate after restoring 10/100 | One displayed 10% result; no duplicate records or messages observed | Passed for this browser-only calculation |

A first test-output collector tried slicing accessibility diffs and returned empty strings; those were not treated as results.
The second collector could read an old status immediately after a click, so the normal 10/100 result was checked again with a fresh UI observation.
No site failure was inferred from that test-harness timing issue.
The site has no contact submission or backend record to duplicate.

## Fix-now: social-share metadata
Before the change, the live Work page had a title and description, but no Open Graph or Twitter-card metadata.
Added to all three pages:
- Canonical URL, using each clean public page path.
- Open Graph title, description, page URL, website type and image.
- A 1200 x 630 PNG share card, with image dimensions and text alternative.
- Twitter large-image card metadata.
- robots.txt and a three-page XML sitemap.

The share image is a text graphic based on the existing identity kit, not an invented project screenshot or official badge.
Local checks verified the required fields and canonical/og:url agreement in all three generated pages.
The published Work page exposed the new fields in the browser DOM. The published PNG loaded.
Source and static assets are preserved in the Site's versioned repository.
Adding tags does not prove that a social network has refreshed its cached preview.

## Search visibility
A web search for the exact name plus this host returned no results on November 12.
The site is public and linked directly, but search-engine indexing is not established.
Do not call it indexed or promise a date. A sitemap is a discovery aid, not a ranking guarantee.

## Existing evidence
mobile-fix-log.md records the earlier student-reported phone check, 768-pixel browser view, navigation, contrast and external-link checks.
Those observations are historical evidence, not repeated phone tests today.

## Remaining known limits
- Today's edge cases used the cloud Chrome browser, not a new physical device or different browser engine.
- No actual new-device/browser check is claimed today.
- A mentor or structured peer hardening review has not happened.
- Search indexing is unconfirmed.
- A full accessibility audit and third-party social preview rendering are not established.
- Automated Lighthouse scores are a single lab run, not field-user data or a full manual accessibility/security audit.
- No assignment pass, reviewer approval, student learning time or actual hours is inferred.

This report prepares the required where-it-breaks list. The checkpoint remains incomplete until the remaining required checks and real review happen.


## Free speed check completed
Google PageSpeed Insights home-page mobile report, November 12, 2026 at 11:08 AM CST:
https://pagespeed.web.dev/analysis/https-yassin-khodir-internship-portfolio-quickchutney32-chatgpt-site/odv9cibima?form_factor=mobile

| Category/metric | Observed result |
| --- | --- |
| Performance | 100 |
| Accessibility | 100 |
| Best Practices | 100 |
| SEO | 100 |
| First Contentful Paint | 0.8 seconds |
| Largest Contentful Paint | 0.8 seconds |
| Total Blocking Time | 0 milliseconds |
| Cumulative Layout Shift | 0.012 |
| Speed Index | 0.8 seconds |

The report used Lighthouse 13.6.0, an emulated Moto G Power, slow 4G throttling and a single initial page load.
It reported no real-user field data. This is a home-page lab result, not a new physical-phone test or a score for every page.
The initial Work-page attempt did not finish with usable scores and showed an invalid-URL message; the home-page retry completed.
100 SEO does not establish search indexing. 100 Accessibility does not replace the report's manual checks.


## Request to the FlyRank reviewer
Please review the observed edge cases, deployed metadata fix, search result and completed mobile lab report.
Please identify any must-fixes before this checkpoint can pass. Remaining new-device/browser coverage and unconfirmed search indexing are disclosed above.
This submission requests the mentor review; it does not claim that a mentor or structured peer has already reviewed it or that its must-fixes have been cleared.
