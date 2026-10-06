# Stage 8b report: domain question banks D5-D7

Builder: Stage 8b question-bank worker. Baseline: Oct 6, 2026. Work confined to
~/workspace/your_files/ccar-p-cert/v2-build/stage8/. No other directory touched.

## Deliverables

| File | Content | Status |
|---|---|---|
| qb-D5.md | 25 original questions, V2-D5.1-V2-D5.5 | Complete |
| qb-D6.md | 25 original questions, V2-D6.1-V2-D6.5 | Complete |
| qb-D7.md | 25 original questions, V2-D7.1-V2-D7.3 | Complete |
| stage8b-report.md | This file | Complete |

## Counts

- Total questions: 75 (25 per domain).
- Question IDs: Q-D5-01 through Q-D7-25, unique, sequential, no duplicates (verified by script).
- Multi-response items ("Select TWO"): 6 per file, 18 of 75 (24%, about a quarter). No partial credit is assumed anywhere, per the exam format.
- Every question carries: scenario, one best answer or marked multi-select, options, answer key, a §17 10-step method walk (Steps 1-10), and a 10-point explanation (all 10 points from §19.2, verified present on all 75 items by script).
- Every file ends with a question-to-objective coverage table.
- STE100: `ste_check.py` run on all three files. 0 hard fails on each. Remaining warnings are linter heuristics (gerund nouns like "screening" and "backing service", noun-cluster flags on tables, long-sentence flags), manually verified as non-issues.
- No exam dumps: every item is original. Each file header states the items are practice, not real exam questions.
- Honesty: toy numbers are computed inside each scenario and labeled as such. D5.4 items carry the "architectural implications only, not legal advice" line in the file header and in evidence points. D7 config details cite lesson-D7-1 (Oct 6, 2026) with a verify-against-current-product-docs note, and every item distinguishes guidance from enforcement. Exam scope cites S03/S04, Sept 2026.

## Coverage tables

### D5 (V2-D5.1-V2-D5.5)

| Objective | Questions | Count |
|---|---|---|
| V2-D5.1 | Q-D5-01, Q-D5-02, Q-D5-03, Q-D5-04, Q-D5-05 | 5 |
| V2-D5.2 | Q-D5-06, Q-D5-07, Q-D5-08, Q-D5-09, Q-D5-10 | 5 |
| V2-D5.3 | Q-D5-11, Q-D5-12, Q-D5-13, Q-D5-14, Q-D5-15 | 5 |
| V2-D5.4 | Q-D5-16, Q-D5-17, Q-D5-18, Q-D5-19, Q-D5-20 | 5 |
| V2-D5.5 | Q-D5-21, Q-D5-22, Q-D5-23, Q-D5-24, Q-D5-25 | 5 |

### D6 (V2-D6.1-V2-D6.5)

| Objective | Questions | Count |
|---|---|---|
| V2-D6.1 | Q-D6-01, Q-D6-02, Q-D6-03, Q-D6-04, Q-D6-05 | 5 |
| V2-D6.2 | Q-D6-06, Q-D6-07, Q-D6-08, Q-D6-09, Q-D6-10 | 5 |
| V2-D6.3 | Q-D6-11, Q-D6-12, Q-D6-13, Q-D6-14, Q-D6-15 | 5 |
| V2-D6.4 | Q-D6-16, Q-D6-17, Q-D6-18, Q-D6-19, Q-D6-20 | 5 |
| V2-D6.5 | Q-D6-21, Q-D6-22, Q-D6-23, Q-D6-24, Q-D6-25 | 5 |

### D7 (V2-D7.1-V2-D7.3)

| Objective | Questions | Count |
|---|---|---|
| V2-D7.1 | Q-D7-01 through Q-D7-09 | 9 |
| V2-D7.2 | Q-D7-10 through Q-D7-17 | 8 |
| V2-D7.3 | Q-D7-18 through Q-D7-25 | 8 |

## Rewritten weak items

1. Q-D7-15 (V2-D7.2): explanation point 5 named the wrong pair ("A and B") for an A, D answer key. Fixed to "A and D" before delivery.
2. STE pass: fixed 7 hard fails in qb-D5.md, 8 in qb-D6.md, and 4 in qb-D7.md. The fixes removed gerund main verbs, conditional-perfect and perfect tenses, and one banned contrast pattern. All three files re-verified to 0 hard fails.
3. Q-D6-18 (V2-D6.4) reviewed for unique defensibility: option B (original eval numbers) answers "was the decision sound," not the asked "does it still hold," so A plus D remain the only pair that names the trip conditions. Kept as written.
4. Q-D6-20 (V2-D6.4) checked against the lesson's decisive constraint for a config flag with no trade-off. Option B offers the light ADR or the commit message. Option D (no record of any kind) stays wrong because the lesson still requires the decision, date, and owner on record somewhere.

## Design notes for the auditor

- Distractor discipline: several distractors expose documented incompatibilities rather than being merely wrong: prompts as money or secret controls (Q-D5-01, Q-D5-02, Q-D5-05, Q-D7-01, Q-D7-02, Q-D7-05), logging or monitoring as a substitute for a gate (Q-D5-02, Q-D5-08, Q-D5-10, Q-D6-21), tier upgrades for planning or retrieval faults (Q-D5-10, Q-D6-21, Q-D7-18, Q-D7-21), the aggregate trap on named groups (Q-D5-21, Q-D5-22), the confidence phrase as a score (Q-D5-11, Q-D5-13, Q-D5-14, Q-D7-17), review-everything at volume (Q-D5-11, Q-D5-13), volume metrics as productivity (Q-D7-15), blind caps (Q-D5-07), and the banned "perfect / never / zero" promises (Q-D6-06, Q-D6-08, Q-D6-13).
- Correct-answer position and length vary across items, and no option is consistently longest.
- Question types spread across the §19.1 list: best action, first action, first check, control design, control placement, root-cause investigation order, metric selection, security scenarios, compliance scenarios, stakeholder decisions, operational enablement, team configuration, lifecycle phase judgments.
- Multi-response items use 5 options (A-E) with "Select TWO" stated in the header and the question line.
- The §13 unseen-transfer questions from the stage5/stage6 lessons are answered inside this bank: the appointment-agent gate (Q-D5-04 family), the research-agent injection (Q-D5-06), the content-agent review shapes (Q-D5-13), the finance-agent EU rows (Q-D5-16, Q-D5-18), the recruiter-agent gap (Q-D5-22), the discharge-summary discovery (Q-D6-01), the honest-promise restatement (Q-D6-08), the hospital-pilot trigger (Q-D6-11), the acquihire ADR triage (Q-D6-19), the 20-person team config (Q-D7-02), the payment-module refactor evidence (Q-D7-11), and the reindex quality drop (Q-D7-21).
- Open item for the coordinator: the independent auditor should adversarially re-verify each answer key per §19.2 point 10 (if two answers are equally defensible, the item must be rewritten, not defended).
