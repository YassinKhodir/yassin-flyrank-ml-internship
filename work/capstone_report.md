# Which Content Pages Should Be Reviewed First?

- **Author:** Yassin Khodir
- **Lane:** Refresh / Content Opportunity Scoring
- **Repository:** https://github.com/YassinKhodir/yassin-flyrank-ml-internship
- **Date:** August 2026

## Abstract

Which established pages should a content editor review first when review capacity is limited? I studied the March 2026 partition of the FlyRank internship warehouse, using March 1–15 signals and a March 16–31 decline outcome. A fixed rule was compared with a five-feature logistic regression on clients excluded from training. On that held-out group, model precision@100 measured 0.310, compared with 0.150 for the fixed rule and a 0.233 outcome base rate; overall ROC-AUC was only 0.510. The result supports a small human-reviewed priority queue, not automatic content changes or a claim that refreshing causes recovery.

## 1. Problem framing

The unit is one pseudonymized client-page record. The output is a score and rank that helps an SEO or content editor decide which pages to inspect first. A false positive wastes review time; a false negative can leave an opportunity unnoticed. A model may combine several weak signals more usefully than a single fixed threshold, but the fixed rule remains the comparison.

## 2. Data safety

The source is the FlyRank internship warehouse. The study uses the March 2026 daily-performance partition: 9,841,378 source rows aggregated to 77,400 eligible page records from 38 represented clients. Features use March 1–15; the label uses March 16–31.

The five features are early log impressions, CTR, active days, average position, and position volatility. Later-window fields, product flags, GA4 fields with uneven coverage, queries, domains, URLs, and identifying fields are excluded. Pseudonymous IDs support grouping and deterministic ties only; they are never features.

## 3. Baseline

The frozen rule assigns fixed points for early impressions and average-position bands. Higher volume raises potential value, while positions 4–50 indicate possible room to improve. On the held-out-client rows it measured precision@100 of 0.150 and ROC-AUC of 0.430. The rule is intentionally readable and was frozen before modeling.

## 4. Model / analysis

Logistic regression fits the binary later-decline label and returns a probability that can order pages. Median imputation and standardization are applied in a pipeline. The five legal features all stop on March 15. The model is simple by design; complexity was not added to improve appearance.

## 5. Evaluation

The final split holds out entire clients using seed 42: 28 clients in training and 10 in testing. On 15,776 held-out rows, the base rate was 0.233, frozen-rule precision@100 was 0.150, and model precision@100 was 0.310. Model ROC-AUC was only 0.510.

A random page split produced ROC-AUC 0.594. The drop under grouped validation shows that randomly mixing pages overstates transfer to unseen clients. A deliberate label-copy feature produced ROC-AUC 1.000 and was deleted. Error review found confident false negatives, especially among pages with good CTR and position.

## 6. Interpretation

Early CTR had the largest standardized coefficient, followed by average position. That does not make either field causal. The model improved the first 100 review slots on one held-out group, but weak overall ROC-AUC means it does not reliably separate every future decline. The grouped result is kept; the better random-split number is reported only as a validation warning.

## 7. Recommendation

An editor should review the high-priority group first, use reason codes as starting questions, and check demand, intent, content quality, technical issues, cannibalization, business value, and editing cost. Low CTR suggests a title/snippet/intent check; positions 21–50 suggest a depth and internal-link review; unstable position suggests waiting.

The system must not publish, delete, merge, redirect, change metadata, request recrawls, or claim expected lift. The score orders attention only.

## 8. Reproducibility

Run the executed notebooks in order: `w03_data_contract.ipynb`, `w04_baseline_score.ipynb`, `w05_model.ipynb`, `w06_validation_audit.ipynb`, `w07_action_playbook.ipynb`, and `capstone.ipynb`. Use Python 3.12, the repository requirements, a Hugging Face READ token stored outside the notebook, and split seed 42. Aggregate metric receipts are committed under `work/outputs/`; raw data and row-level queues are not committed.

## Limitations

This study uses one mid-panel month and only 10 held-out clients. Eligibility requires observations in both halves of March, which can favor consistently tracked pages. Five search features omit query intent, content quality, technical state, and business value. The label measures later movement, not refresh benefit. No controlled intervention was run, so the study cannot claim that refreshing causes recovery.

## Acknowledgments & data credit

Built on the [FlyRank ML Internship dataset](https://flyrank.ai).
