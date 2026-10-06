# Stage 2 report: prerequisite diagnostic and foundation micro-lessons

Date: Oct 6, 2026. Builder: Stage 2 content worker. Baseline: product facts
frozen Oct 6, 2026. Exam scope = blueprint v1.0 (July 2026) via secondary
summaries S03/S04.

## What was completed

Five fragments in ~/workspace/your_files/ccar-p-cert/v2-build/stage2/:

- diagnostic.md: 16 scenario questions, 4 per foundation area, no answers.
- lesson-7-4A.md: architecture and business foundations.
- lesson-7-3A.md: LLM foundations.
- lesson-7-1A.md: software and distributed systems.
- lesson-7-2A.md: security and identity.

Each lesson follows the 14-item template, ends with a 15-row page-audit
table (no blank figure cells), and carries 5 inline SVG lesson plates plus
tables and ASCII cards. All 20 SVGs parse as XML. Palette check: only
spec colors used. No em dashes, no semicolons, no contractions anywhere.
ste_check.py: 0 hard violations.

Structural contract (pdf-print-spec.md): one H1 per file, H2 sections,
:::takeaway blocks, <figure class="fig"> with inline SVG and <figcaption>
naming shell and source, fenced code blocks for ASCII, markdown tables
only. No raw HTML tables. No file over 90MB (largest is 21KB).

## Objectives and prereqs covered

All four §7 foundations at the minimum depth in prereq-graph-v2.md:
§7.4 requirement/metric/threshold/owner chain, §7.3 tokens, sampling,
hallucination, retrieval vs fine-tuning, injection, §7.1 timeouts,
retries, idempotency, backoff, breakers, observability, §7.2 authN/authZ,
enforcement before context, secrets, tenant isolation, audit. Dependent
objectives unblocked for later stages: D1.1, D1.2, D1.6, D2.1-D2.5,
D3.1, D3.2, D3.4, D3.7, D4.1, D4.6, D5.1-D5.4, D6.1-D6.5, D7.1.

## Evidence added

- Claim classification in every lesson §14: official exam scope (via S03,
  S04, Sept 2026) vs current product behavior (S10-S12 model matrix, Oct
  2026) vs general principle vs original toy vs not in source.
- Computed arithmetic in figures: triage $500 to $51/week ($23,348/year),
  contract summary $0.025 ($750/month at 1,000/day), retry 20 to 0.4
  failures/day inside an 8s budget, audit 200MB/day (6GB/month), token
  theft window cut 96x by 15-minute lifetimes.
- "Not in source" written for the delayed-refund dollar figure (7-4A).

## Gaps and corrections

- Raj's §16/§17/§19 prompt text was not available to this builder. §16
  template items were spelled out in the work order and followed exactly.
  §17 (10-step best-answer method) was reconstructed as a standard exam
  method and is flagged inside each lesson: the coordinator must align it
  with the canonical §17 text. §19 (keys in Stage 8) was honored:
  diagnostic and all §13 transfer questions are answer-free.
- Fixed during the build: 51 ste_check hard violations (semicolons,
  "is absent", HTML entities read as semicolons, -ing verbs), pill
  radius set to 999px per spec, grid alignment on one figure row, and a
  missing §1 figure in lesson-7-3A (caught by figure-count audit).
- "Circuit breaker" uses the word "circuit" in prose. It is a term, not
  circuit artwork. Left as-is.

## What Stage 3 needs

- The canonical §17 text to replace the reconstructed 10-step method (or
  confirmation that the reconstruction is close enough).
- Domain lessons D1-D7 that reuse (not re-teach) the four chains: the
  threshold chain, the sampler model, caller-side reliability, and
  enforcement before context.
- Stage 8 owns all answer keys: diagnostic key plus the four §13 transfer
  keys.
- Stage 9 owns: full page-audit re-verification, 8px-grid measurement on
  every plate, PDF assembly per the print spec, and the currentness
  appendix for post-Oct-6 model changes.
