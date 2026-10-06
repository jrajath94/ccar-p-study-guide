# Stage 7 report: comparisons, artifacts, labs, capstones

Workstream completion report for the Stage 7 content builder. Baseline Oct 6, 2026.

## Deliverables

| File | Content | Status |
|---|---|---|
| comparisons-01.md | Pairs 1-6: patterns and orchestration | Complete |
| comparisons-02.md | Pairs 7-11: caching, discovery, retrieval | Complete |
| comparisons-03.md | Pairs 12-16: controls and security | Complete |
| comparisons-04.md | Pairs 17-21: verification and evaluation | Complete |
| comparisons-05.md | Pairs 22-26: operations and lifecycle | Complete |
| artifacts-01.md | A1-A11: calls, tools, retrieval, evaluation | Complete |
| artifacts-02.md | A12-A23: reliability, governance, operations | Complete |
| labs.md | Labs 1-9 | Complete |
| capstone-A.md | Enterprise knowledge assistant | Complete |
| capstone-B.md | High-impact payout workflow | Complete |
| capstone-C.md | Org-wide Claude Code enablement | Complete |
| stage-report.md | This file | Complete |

Supporting test scripts in `tests/`: `t5_structured_validation.py`, `t_retry_idempotency.py`, `t_approval_fsm.py`, `t6_rag_diagnosis.py`. All four ran locally with real output embedded in the artifacts and labs.

## Coverage check

Workstream A (§18): all 26 pairs built. Each pair carries shared ground, decisive difference, a matrix, winning and losing constraints, costs, security, operations, a counterexample, evidence, and at least 3 minimal pairs. Count: 6 + 5 + 5 + 5 + 5 = 26.

Workstream B (§21): all 23 artifacts built (11 + 12). Each carries purpose, version, assumptions, dependencies, permissions, security boundary, expected behavior, failure cases, verification, and tested-vs-illustrative status. Three artifacts executed locally: A5 structured-output validation, A12 retry plus idempotency, A13 approval state machine. Twenty marked ILLUSTRATIVE with named verification steps.

Workstream C (§23): all 9 labs built, each with goal, setup, steps, expected observations, and diagnosis practice. Cleanup documented per lab. Cost caps stated before any real-API step. All 3 capstones built with all 14 required sections: discovery brief, architecture alternatives, requirements, decision records, security review, evaluation plan, cost and latency budget, implementation contracts, deployment gates, ownership, runbook, stakeholder presentation, failure injection, related exam scenarios.

## Standards compliance

Depth and conciseness: tight matrices, no re-teaching. Prior-stage concepts appear by name only (V2-D1.3, V2-D3.2, Lesson 7-2A, and similar). Toy numbers are reused from prior stages where they exist (D1-patterns refund toy, D2-5 cache toy, 7-2A audit math) and computed fresh where new.

Figures: 9 inline SVGs total, one per comparisons file (5), one in artifacts-01, one in artifacts-02, one in labs, one per capstone (3). All use the spec palette, 8px grid, flat fills, before-left with one labeled arrow and after-right, one-sentence footer, and a caption naming the shell and the source. No gradients, no banned art.

STE100: every file self-scanned with `ste_check.py`. Hard fails fixed. See the lint log below.

Print contract: H1 per file, H2 sections, `:::takeaway` fenced divs, `<figure class="fig">` with `<figcaption>`, fenced code only, filenames with no spaces.

Honesty: version-sensitive claims carry dates and sources in per-pair and per-artifact evidence tables. Claim classes: official exam scope via secondary summaries, general principle, original toy, current product behavior. Baseline Oct 6, 2026. Pricing figures cite public pricing via secondary sources S10-S12 with a verify-against-official-docs note. No exam dumps. No fabricated execution: every unexecuted artifact says so.

## Lint log

`~/workspace/skills/ste-lint/bin/ste_check.py` run against all 12 deliverables. First pass found hard fails: semicolons, -ing main verbs, and one banned term from the STE list. Fixes applied: semicolons replaced with periods, -ing verbs rewritten as nouns or simple present verbs, and every occurrence of the banned term renamed to "runner" or "rig" (see open item 6). Second pass: 0 hard fails on all 12 files. Remaining warnings are linter heuristics (gerund section labels like "Winning constraints", nouns like "tracing") and cross-line noun-cluster false positives. Verified manually as non-issues.

## Open items for the coordinator

1. Three artifacts were executed locally against simulations, not real systems: A5, A12, A13. If Stage 8 wants execution evidence against real APIs, that needs API keys, cost approval, and a bounded runbook.
2. Pricing figures (Balanced tier $2 in, $10 out per 1M) come from secondary sources S10-S12, Oct 2026. Verify against official docs before print.
3. The §17 10-step method was not in this builder's context. Comparisons reference the method by name only. No reconstruction was attempted here.
4. Lab real-API variants are optional and capped. The default path in every lab is local.
5. Suggested Stage 8 question seeds: minimal-pair flips (change one constraint, name the new winner), right-layer diagnosis from lab traces, and artifact contract completion.
6. Naming note: §21's required artifact name contains a word on the STE banned list, so artifact A11 is delivered as "Evaluation runner" with all references renamed (code string "eval-runner", lab and artifact cross-references). Map A11 to the §21 artifact name in any downstream index.

:::takeaway
Stage 7 is complete: 26 comparisons, 23 artifacts, 9 labs, 3 capstones, 9 figures, 4 executed toys. All files pass the STE gate. Nothing claims a run that never happened.
:::
