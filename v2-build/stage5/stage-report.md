# Stage 5 report — Domains 4 and 5 content build (Oct 6, 2026)

## Objective map

| Objective | Lesson file | Core decision boundary taught |
|---|---|---|
| V2-D4.1 evaluation metrics | lesson-D4-1.md | Primary metric from the business goal; guards as floors; proxy stays a diagnostic; cost per successful task |
| V2-D4.2 datasets and frameworks | lesson-D4-2.md | Five dataset drawers; cheapest reliable evaluator rung per drawer; judge calibrated against human labels; per-segment reporting |
| V2-D4.3 A/B testing and iteration | lesson-D4-3.md | Falsifiable hypothesis with primary metric first; consistent assignment; statistical vs business significance; shadow before exposure |
| V2-D4.4 diagnosis at the right layer | lesson-D4-4.md | Symptom to evidence to hypotheses to discriminating test to smallest correction to regression verification; never upgrade the model by default |
| V2-D4.5 optimization under floors | lesson-D4-5.md | Ordered levers: measure, context, cache, route, eliminate; quality and safety floors held on every cut; streaming buys perception, not completion |
| V2-D4.6 production monitoring | lesson-D4-6.md | Five watches; alert rule needs line, window, owner; eval set must mirror production; paired slow and fast lines |
| V2-D5.1 guardrails and safety controls | lesson-D5-1.md | Six controls in code; enforcement fails closed; the model never enforces its own limits |
| V2-D5.2 risks and failure modes | lesson-D5-2.md | Nine risks, each with prevention, detection, recovery; retrieved text is untrusted; caps from measured runs |
| V2-D5.3 human-in-the-loop validation | lesson-D5-3.md | Three review shapes keyed to five stakes; reviewers need full decision context; model confidence is not a calibrated risk score |
| V2-D5.4 regulatory compliance | lesson-D5-4.md | One chain per requirement: requirement, control, owner, evidence, cadence; architectural implications only, never legal advice |
| V2-D5.5 responsible AI | lesson-D5-5.md | Six duties as artifacts; per-group metrics and floors; the group score is the metric, the aggregate is the footnote |

All 11 lessons follow the mandatory §16 template: sections 1-14 plus
:::takeaway blocks, the canonical §17 10-step method trained verbatim
in every worked example (including the verbatim do-not-assume
paragraph), decisive scenario plus valid-but-inferior option plus
counterfactual in every lesson, closed-book recall prompt, unseen
transfer question with NO answer, evidence table with claim
classification, and a closing page-audit table.

## Evidence and claim classification

- Objective texts: paraphrased from corroborated secondary summaries
  of the official v1.0 guide (S03, S04, Sept 2026) via the Stage 1
  blueprint ledger. Class: official exam scope via secondary summaries.
- All toy arithmetic: original toys computed inside each lesson, dated
  Oct 6, 2026. Class: original toy.
- Tier prices ($1/$5 Fast, $2/$10 Balanced in/out per 1M tokens),
  cache write 1.25x / read 0.1x / 5-minute TTL, model windows:
  current product behavior from secondary sources (S10-S12, Oct 2026).
  Class: current product behavior, secondary. Explicitly not presented
  as exam scope; several lessons state the exam tests trade-off
  judgment, not memorized values.
- Mechanisms (retry/idempotency/backoff, authN/authZ, sampling,
  ablation, budget caps, fail-closed defaults): general principle /
  industry canon, classed as such with long-standing dates.
- Compliance content (D5-4): architectural implications only. The
  lesson opens with an explicit "not legal advice" notice, repeated
  in the recall prompt and evidence table.

## Gaps (honest, for Stage 8 and the audit)

- Exact sample-size formula for A/B tests: not in source. D4-3 uses a
  stated toy rule of thumb and labels it an assumption.
- Human label disagreement rate: not in source (D4-2 evidence table).
- 30 seconds per human review, $150 engineer hour, $40 reviewer hour,
  refund amounts, injection loss rates: toy assumptions, stated in
  each lesson.
- Feedback-loop bias compounding numbers in D5-5 §4: toy illustration,
  not measured; labeled as such.
- Transfer-question keys: intentionally absent. Stage 8 owns all keys.

## Corrections applied during this build

- STE lint (ste_check.py): all 11 files now report zero HARD fails.
  Fixed: 4 -ing-as-verb instances (missing x2, being, scheduling,
  hiring x2) reworded; 3 banned-word "harness" instances replaced with
  "eval setup"; 2 semicolons in D5-2 replaced with periods; 1 perfect
  tense ("would have approved") rewritten in simple present.
- D4-1 §13 was rewritten during the hiring/recruiter rename pass; the
  final text is a coherent transfer question on primary metric, guard
  metrics, and threshold chain, consistent with the lesson.
- Prerequisite reuse discipline: every lesson's §2 references Stages
  2-4 concepts by name only (chain, traces, per-stage receipts,
  context budget, cache break-even, RAG stages, enforcement law) and
  re-teaches nothing.

## Stage 6 needs

- The 11 fragments are print-contract conformant: H1 lesson title,
  H2 sections, :::takeaway fenced divs, <figure class="fig"> plus
  <figcaption> with shell number and source, fenced code only, no
  spaces in filenames.
- Assembly: concatenate in domain order D4-1 through D5-5 into the
  crash-course page under their domain H1s. SVG marker ids are
  prefixed per lesson (m-d41-*, m-d42-*, ...) and are unique across
  this stage's files.
- Stage 8 must write keys for the 11 unseen transfer questions (§13
  of each lesson). No answers exist in these fragments by design.
- Recommended audit focus for the independent auditor: verify every
  figure's arithmetic against its lesson prose, verify no blank
  figure cell in any page-audit table, and verify the §17 10-step
  text plus the do-not-assume paragraph are verbatim in all 11
  lessons.
