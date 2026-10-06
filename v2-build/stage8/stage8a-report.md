# Stage 8a report: domain question banks D1-D4

Builder: Stage 8a question-bank worker. Baseline: Oct 6, 2026. Work confined to
~/workspace/your_files/ccar-p-cert/v2-build/stage8/. No other directory touched.

## Deliverables

| File | Content | Status |
|---|---|---|
| qb-D1.md | 25 original questions, V2-D1.1-V2-D1.6 | Complete |
| qb-D2.md | 25 original questions, V2-D2.1-V2-D2.5 | Complete |
| qb-D3.md | 25 original questions, V2-D3.1-V2-D3.8 | Complete |
| qb-D4.md | 25 original questions, V2-D4.1-V2-D4.6 | Complete |
| stage8a-report.md | This file | Complete |

## Counts

- Total questions: 100 (25 per domain).
- Question IDs: Q-D1-01 through Q-D4-25, unique, sequential, no duplicates (verified by script).
- Multi-response items ("Select TWO" / "Select THREE"): 6 per file, 24 of 100 (24%, about a quarter). No partial credit is assumed anywhere, per the exam format.
- Every question carries: scenario, one best answer or marked multi-select, options, answer key, a §17 10-step method walk (Steps 1-10 verbatim from the stage3 lessons), and a 10-point explanation (all 10 points from §19.2, verified present on all 100 items by script).
- Every file ends with a question-to-objective coverage table.
- STE100: `ste_check.py` run on all four files. 0 hard fails on each. Remaining warnings are linter heuristics (gerund nouns, noun-cluster flags on tables, long-sentence flags), manually verified as non-issues.
- No exam dumps: every item is original. Each file header states the items are practice, not real exam questions.
- Honesty: tier names (Fast, Balanced, Capable, Most capable) are the stage3 lesson toys, and pricing cites S10-S12 secondary sources, Oct 2026, with a verify-against-official-docs note, and version-sensitive claims carry dates. Toy assumptions are labeled "not in source" or "toy" per the lesson honesty rule.

## Coverage tables

### D1 (V2-D1.1-V2-D1.6)

| Objective | Questions | Count |
|---|---|---|
| V2-D1.1 | Q-D1-01, Q-D1-02, Q-D1-03, Q-D1-04 | 4 |
| V2-D1.2 | Q-D1-05, Q-D1-06, Q-D1-07, Q-D1-08 | 4 |
| V2-D1.3 | Q-D1-09, Q-D1-10, Q-D1-11, Q-D1-12 | 4 |
| V2-D1.4 | Q-D1-13, Q-D1-14, Q-D1-15, Q-D1-16 | 4 |
| V2-D1.5 | Q-D1-17, Q-D1-18, Q-D1-19, Q-D1-20 | 4 |
| V2-D1.6 | Q-D1-21, Q-D1-22, Q-D1-23, Q-D1-24, Q-D1-25 | 5 |

### D2 (V2-D2.1-V2-D2.5)

| Objective | Questions | Count |
|---|---|---|
| V2-D2.1 | Q-D2-01, Q-D2-02, Q-D2-03, Q-D2-04, Q-D2-05 | 5 |
| V2-D2.2 | Q-D2-06, Q-D2-07, Q-D2-08, Q-D2-09, Q-D2-10 | 5 |
| V2-D2.3 | Q-D2-11, Q-D2-12, Q-D2-13, Q-D2-14, Q-D2-15 | 5 |
| V2-D2.4 | Q-D2-16, Q-D2-17, Q-D2-18, Q-D2-19, Q-D2-20 | 5 |
| V2-D2.5 | Q-D2-21, Q-D2-22, Q-D2-23, Q-D2-24, Q-D2-25 | 5 |

### D3 (V2-D3.1-V2-D3.8)

| Objective | Questions | Count |
|---|---|---|
| V2-D3.1 | Q-D3-01, Q-D3-02, Q-D3-03 | 3 |
| V2-D3.2 | Q-D3-04, Q-D3-05, Q-D3-06 | 3 |
| V2-D3.3 | Q-D3-07, Q-D3-08, Q-D3-09 | 3 |
| V2-D3.4 | Q-D3-10, Q-D3-11, Q-D3-12 | 3 |
| V2-D3.5 | Q-D3-13, Q-D3-14, Q-D3-15 | 3 |
| V2-D3.6 | Q-D3-16, Q-D3-17, Q-D3-18 | 3 |
| V2-D3.7 | Q-D3-19, Q-D3-20, Q-D3-21, Q-D3-22 | 4 |
| V2-D3.8 | Q-D3-23, Q-D3-24, Q-D3-25 | 3 |

### D4 (V2-D4.1-V2-D4.6)

| Objective | Questions | Count |
|---|---|---|
| V2-D4.1 | Q-D4-01, Q-D4-02, Q-D4-03, Q-D4-04 | 4 |
| V2-D4.2 | Q-D4-05, Q-D4-06, Q-D4-07, Q-D4-08 | 4 |
| V2-D4.3 | Q-D4-09, Q-D4-10, Q-D4-11, Q-D4-12 | 4 |
| V2-D4.4 | Q-D4-13, Q-D4-14, Q-D4-15, Q-D4-16 | 4 |
| V2-D4.5 | Q-D4-17, Q-D4-18, Q-D4-19, Q-D4-20 | 4 |
| V2-D4.6 | Q-D4-21, Q-D4-22, Q-D4-23, Q-D4-24, Q-D4-25 | 5 |

## Known weak items already rewritten

1. Q-D1-21 (V2-D1.6): the first draft's options did not match the computed net value (the scenario lacked the handle-time cut, so the arithmetic had no unique answer). Rewrote the scenario to state the 6-to-4 minute cut, recomputed all four terms (net about $138,000), and rebuilt the distractors to test the classic errors (drop the error term, forget the build cost, reflex "do not build"). The explanation now carries the full term table.
2. Q-D2-25 (V2-D2.5): first draft was "Select TWO" with option E (subagent for need 3) also defensible, which violates the uniquely-defensible rule. Rewrote as "Select THREE" with answer A, B, E.
3. Q-D3-18 (V2-D3.6): first draft was "Select TWO" with option D (tool call for daily facts) also defensible. Rewrote as "Select THREE" with answer A, B, D.
4. Q-D3-25 (V2-D3.8): first draft was "Select TWO" with option C (discovery for case 3) also defensible. Rewrote as "Select THREE" with answer A, B, C.
5. Q-D4-11 (V2-D4.3): first draft was "Select TWO" with option E (business significance) also defensible. Rewrote as "Select THREE" with answer A, B, E.
6. STE pass: fixed semicolons (replaced with commas), em dashes in headers and table cells (replaced with commas and "n/a"), -ing main verbs, perfect tenses, one banned word from the STE list and two banned contrast patterns. All fixes re-verified to 0 hard fails.

## Design notes for the auditor

- Distractor discipline: several distractors expose documented incompatibilities rather than being merely wrong: "log every tool call" as a fix for capability bloat (Q-D3-01), shared credentials when the audit must name the human (Q-D3-04), prompts as money authorization (Q-D1-02, Q-D2-06, Q-D2-10), faster index rebuilds for live data (Q-D3-17), tier upgrades for template/chunking faults (Q-D4-14, Q-D3-13), caching the variable tail (Q-D2-21), and retention extensions for missing traces (Q-D3-10).
- Correct-answer position and length vary across items, and no option is consistently longest.
- Question types spread across the §19.1 list: architecture interpretation, best/next/first action, root cause, control placement, metric selection, security scenarios, retrieval diagnosis, evaluation design, stakeholder decisions.
- Multi-response items use 5 options (A-E) with "Select TWO" or "Select THREE" stated in the header and the question line.
- Open item for the coordinator: the independent auditor should adversarially re-verify each answer key per §19.2 point 10 (if two answers are equally defensible, the item must be rewritten, not defended).
