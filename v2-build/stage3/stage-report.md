# Stage 3 report: Domains 1 and 2 lessons (V2-D1.1 to V2-D2.5)

Date: Oct 6, 2026. Builder: Stage 3 content worker. Baseline: product
facts frozen Oct 6, 2026. Exam scope = blueprint v1.0 (July 2026) via
secondary summaries S03/S04. Work confined to
~/workspace/your_files/ccar-p-cert/v2-build/stage3/. No other directory
touched.

## What was completed

Nine markdown fragments, one per the structural contract in
pdf-print-spec.md (one H1, H2 sections, :::takeaway blocks,
<figure class="fig"> with inline SVG plus <figcaption> naming shell and
source, fenced code blocks, markdown tables only, no spaces in
filenames):

- lesson-D1-1.md (V2-D1.1): business problem to Claude solution. The
  fork: fixed mapping goes deterministic. Open input with a verifiable
  output goes to Claude with a gate. Five-link translation chain.
- lesson-D1-2.md (V2-D1.2): end-to-end architecture. Seven gates:
  input, validation, context and retrieval, model and tools,
  verification, output, feedback. The trust boundary sits in code.
- lesson-D1-patterns.md (V2-D1.3 + V2-D1.4 + V2-D1.5, the permitted
  merge): pattern spectrum (augmented call, workflow, hybrid, agent)
  scored on seven axes. Multi-agent coordinator and worker with handoff
  contracts. Five decomposition moves (route, chain, fan-out/fan-in,
  critique, validation). Each objective carries its own items
  1,2,3,4,5,9,10,11,12,13. Items 6,7,8,14 are shared at lesson level.
- lesson-D1-6.md (V2-D1.6): business-value alignment. Net value
  equals (baseline minus new) times volume, plus avoided error cost,
  minus build and run cost.
- lesson-D2-1.md (V2-D2.1): model selection and tier trade-offs.
  The cheapest tier that clears the quality floor wins. Cascade with
  a confidence check.
- lesson-D2-2.md (V2-D2.2): system prompts, templates, guardrails.
  Three zones. Prompts are contracts, never authorization.
- lesson-D2-3.md (V2-D2.3): prompt techniques. Five-rung ladder.
  Simplest technique that passes evals. Rejection examples.
- lesson-D2-4.md (V2-D2.4): context and token management. Four
  accounts and five leaks (growth, duplication, loss, exhaustion,
  dilution), with leak-to-strategy mapping.
- lesson-D2-5.md (V2-D2.5): reuse and prompt caching. Prefix rule:
  stable first, variable last. Break-even at 4% hit rate on the toy.

Each lesson follows the 14-item template, ends with a page-audit
table (no blank figure cells: 15 rows per solo lesson, 37 in the
merged lesson). It trains the canonical §17 10-step best-answer
method verbatim in its worked example, plus the anti-slogan paragraph
verbatim. Total: 50 inline SVGs (5 per solo lesson, 10 in the merged
lesson). All parse as XML. Marker ids unique across all files.
Palette check: spec colors only. No em dashes, no en dashes, no
semicolons, no contractions anywhere. ste_check.py: 0 hard
violations. Remaining warnings are noun-cluster false positives on
tables/code/SVG text, long-sentence flags on SVG markup and the
verbatim §17 block, and ing-check/apostrophe-s advisories on nouns
and possessives.

## Objectives covered (ledger S to L)

| Objective | Lesson location |
|---|---|
| V2-D1.1 | lesson-D1-1.md, full 14 items |
| V2-D1.2 | lesson-D1-2.md, full 14 items |
| V2-D1.3 | lesson-D1-patterns.md, section "Objective V2-D1.3", items 1,2,3,4,5,9,10,11,12,13 |
| V2-D1.4 | lesson-D1-patterns.md, section "Objective V2-D1.4", items 1,2,3,4,5,9,10,11,12,13 |
| V2-D1.5 | lesson-D1-patterns.md, section "Objective V2-D1.5", items 1,2,3,4,5,9,10,11,12,13 |
| V2-D1.6 | lesson-D1-6.md, full 14 items |
| V2-D2.1 | lesson-D2-1.md, full 14 items |
| V2-D2.2 | lesson-D2-2.md, full 14 items |
| V2-D2.3 | lesson-D2-3.md, full 14 items |
| V2-D2.4 | lesson-D2-4.md, full 14 items |
| V2-D2.5 | lesson-D2-5.md, full 14 items |

Each objective carries mechanism (§4), decision boundary (§9),
application example (§5 with arithmetic), and transfer assessment
(§13, answer-free) per §5.1.

## Evidence added

- Claim classification in every §14: official exam scope (S03, S04,
  Sept 2026) vs current product behavior (S10-S12 tier matrix, Oct
  2026) vs general principle vs original toy vs not in source.
- Computed arithmetic in figures and prose, each re-verified.
  Invoice fork $540 to $132/month. Pipeline $10,800/month. Refund
  hybrid $480 to $55.40/day. Review team 48 s to 24 s at +30% cost.
  Report fan-out $0.168 to $0.207 (4 cents for the trace). Contract
  review $13,333 to $2,010/week, $689K/year net. Cascade $5,000 to
  $2,850/day (43%). Prompt rewrite $500 to $160/day. Few-shot $60/day
  for $12,000/day fewer fixes. JIT context $1.53 to $0.25 per talk.
  Prompt cache $170 to $31.76/day with 4% break-even hit rate.
- "Not in source" written for: parser price $0.0001, lawyer and
  doctor hour rates, incident prices, human review and fix costs.
- Cache pricing (write 1.25x, read 0.1x, TTL 5 min) labeled current
  product behavior with an explicit verify-against-official-docs note.

## Gaps and corrections

- The §17 10-step text came verbatim from the work order, not from
  Raj's prompt text. It supersedes the Stage 2 reconstruction. If the
  coordinator holds a different canonical §17, these lessons need a
  mechanical swap of the ten steps and the anti-slogan paragraph (11
  worked examples).
- Stage 2 lessons carry a disclaimer that §17 was reconstructed.
  These Stage 3 lessons carry no disclaimer because the work order
  supplied the canonical text. Flagging the provenance difference for
  the coordinator.
- Fixed during the build: 6 ste_check hard violations (3 semicolons,
  3 -ing verbs, one of which was introduced by a fix and re-fixed),
  plus 8 exposition sentences over 25 words split into shorter ones.
  SVG text, table cells, quoted question stems, and the verbatim §17
  block were left untouched by the length pass.
- The merged lesson keeps items 6, 7, 8, 14 shared. If Stage 9
  prefers per-objective evidence tables, split §14 by objective.

## What Stage 4 needs

- These lessons reuse Stage 2 foundations by name only: §7.4 chain,
  §7.3 sampler and dilution, §7.1 caller-side reliability, §7.2
  signs-are-not-locks. No concept is re-taught. Stage 4 (D3) should
  do the same for these D1/D2 concepts: cite the fork, the seven
  gates, the spectrum, the tier ladder, and the prefix rule by name.
- Stage 8 owns all answer keys: the eleven §13 transfer questions in
  these files are answer-free by design.
- Stage 9 owns: 8px-grid measurement on the 50 plates, per-page
  render checks, the currentness appendix (tier matrix and cache
  pricing are the two most date-sensitive claims), and PDF assembly
  per the print spec.
