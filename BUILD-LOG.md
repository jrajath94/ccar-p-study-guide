# CCAR-P Study Guide - Build Log

Built 2026-09-28. Coordinator: CCAR-P track (Muse Spark subagent).

## Exam identity (verified 2026-09-28)

CCAR-P = **Claude Certified Architect - Professional** (Anthropic). Exam Guide v1.0
effective July 2026. 63 items (multiple-choice + multiple-response; each item states
how many to select), 120 minutes, proctored via Pearson VUE (OnVUE or test center),
pass 720/1000 scaled (criterion-referenced), $175 USD, valid 12 months, free
non-proctored renewal assessment. Retakes: 14/30/90-day waits, max 4 per rolling year.
Recommended: SWE best practices, 3+ yrs systems architecture / platform engineering,
6+ months hands-on Claude/LLM in production. Sources: official exam guide v1.0 via
multiple independent 2026 summaries (dev.to, preporato, claudecertificationguide.com,
sarveshtalele examprep skill, karen-ux-gi); the guide PDF itself is partner-gated.

Official domain order (NOT weight order - the original draft numbered by weight and
was corrected):
- D1 Solution Design & Architecture - 17%
- D2 Claude Models, Prompting & Context Engineering - 13%
- D3 Integration - 19%
- D4 Evaluation, Testing & Optimization - 16%
- D5 Governance, Safety & Risk Management - 14%
- D6 Stakeholder Communication & Lifecycle Management - 14%
- D7 Developer Productivity & Operational Enablement - 7%

## Volumes

| File | Domain | Size | Figures |
|---|---|---|---|
| index.html | Guide home | - | - |
| 01-solution-design-architecture.html | D1 (17%) | 1.7 MB | 14 |
| 02-models-prompting-context.html | D2 (13%) | 1.1 MB | 9 |
| 03-integration.html | D3 (19%) | 4.7 MB | 9 |
| 04-evaluation-testing-optimization.html | D4 (16%) | 1.1 MB | 8 |
| 05-governance-safety-risk.html | D5 (14%) | 906 KB | 7 |
| 06-stakeholder-communication-lifecycle.html | D6 (14%) | 132 KB | 10 |
| 07-developer-productivity-enablement.html | D7 (7%) | 1.2 MB | 7 |
| 08-question-bank.html | 64 questions (21 easy / 23 medium / 20 hard) | 184 KB | - |
| 09-system-design-guide.html | 8 reference designs | 1.1 MB | 10 |

Every volume: scenario-first teaching, "How the exam asks" boxes, numbered
how-to-read walkthroughs per diagram, worked math, common-misunderstanding traps,
zero-to-one first principles, plain English, no em dashes.

## Quality gate: fact audit (2026-09-28, live sources, 2026-dated preferred)

One auditor per volume, every verifiable claim checked against docs.anthropic.com,
platform.claude.com, code.claude.com, modelcontextprotocol.io, AWS Bedrock docs.
Notable corrections:
- D1: pricing ladder updated to live Sept 2026 figures (Sonnet 5 $2/$10, Opus $5/$25);
  a Design-B p95 math error fixed (mixture percentiles are not weighted averages);
  context window corrected to 1M tokens (current generation); MCP auth OAuth 2.0 → 2.1;
  one tool-count claim marked UNVERIFIED (no official Anthropic source).
- D2: a fabricated "90.2% vs 68.5% on BrowseComp" statistic corrected. The official
  Anthropic blog reports a 90.2% *relative* multi-agent improvement; 68.5% appears
  nowhere. Harness attribution reworded to what Anthropic actually published.
- D3: cache break-even corrected to a single reuse (25% write premium repaid by first
  0.1x hit); 1-hour TTL write premium sharpened to verified 2x.
- D4: ZDR paragraph now carries the 2026 Covered Models exception (limited retention
  + safety review for designated frontier models even under ZDR).
- D5: domain misnumbering fixed (was labeled D5, officially D6); 99.99% downtime
  rounding corrected.
- D6: clean. 24 claim groups verified, zero corrections (Fable 5.1 tier confirmed real).
- D7: CLAUDE.md four scopes, MCP three scopes, hooks nested JSON schema corrected.
- Q-bank: Q7 rebuilt (defective multiple-response item had two correct pairs); Q10
  distractor fixed (direct API + ZDR *is* BAA-eligible; the differentiator is region
  pinning); Q40 updated (Claude for Government is FedRAMP High authorized); Q22
  explanation strengthened.
- Design guide: 9 corrections incl. cache minima per model, trilemma pricing table,
  OAuth 2.1 + Client ID Metadata Documents, tool_choice fourth value `tool`.

Pricing normalized across all volumes against the live Anthropic pricing page
(Sonnet 5 $2/$10 confirmed as arbiter). BAA/ZDR/FedRAMP statements normalized across
D5 volume, question bank, and design guide. Every volume carries a
"Last verified against official Anthropic sources: September 2026." note.

## Design system (2026-09-28, user spec)

Canonical system at `~/workspace/your_files/shared/design-system/` (ds.css, ds.js,
INTEGRATION.md), shared verbatim across all tracks. Pitch-black dark mode
(--bg:#000000, --surface:#0d0d0d, --border:#262626, --text:#ececec, --muted:#a8a8a8,
--accent:#f0b429, --link:#6cb2ff, --code-bg:#111111). System font stack only. Body
17px / 1.75 / 72ch / justified. Sticky sidebar: scroll-spy, search filter, collapsible
groups, localStorage checkmarks, progress bar, prev/next, keyboard nav, mobile drawer.
Learning components: .exam-ask, .takeaway, .pq, .diagram-walkthrough, .def,
.constraint (+ .constraint-block variant), .table-wrap, copy buttons on code blocks,
print stylesheet (light paper). Applied to all 10 pages; prose preserved byte-identical
(text-diffs verified per volume); heading order repaired; alt text completed; zero
horizontal scroll; native details/summary untouched.

## Pipeline

1. 9 writer workers → volumes
2. index.html + README.md
3. 9 fact auditors → corrections above
4. Renumber to official domain order (file renames + all D# refs + index/README/blueprint)
5. Design system build → 10 themers → final sweep (script-escape fix, .constraint-block
   sync, QB box retag, D1 h1 fix)
6. wm_clean.py Layer A over all HTML (byte audit)
7. Zip + private GitHub repo push

## Watermark hygiene

wm_clean.py Layer A run over all 10 HTML files before packaging; outputs byte-audited.
Publishable text under the user's name: Layer A only (Layer B default rejected
2026-09-21 for voice regression; standing order).

---

# CCAR-P CRASH COURSE v2 REBUILD — Coordinator log (2026-10-06)

Order: archive v1 (done, archive/2026-10-06-v1/, untouched), rebuild crash course
from the CCAR-P Mastery Engine v1.0 prompt. New crash course builds at
crash-course.html (same path; index links keep working). Domain pages 01-09 and
prereq-claude-fundamentals stay as-is. Fragments live in v2-build/.

## Stage 1 (2026-10-06 ~13:05-13:25 EDT) — COMPLETE

- Exam identity verified: CCAR-P, blueprint v1.0 effective July 2026, 63 items,
  120 min, 720/1000 scaled pass, $175, Pearson VUE, 14/30/90-day retakes, max 4
  per rolling year, 12-month validity, free non-proctored renewal.
- Official guide PDF is partner-gated and was NOT directly accessible — stated
  explicitly per prompt §3. Blueprint rests on four mutually consistent
  independent secondary sources (chrisbirster, preporato, vkorost, sarveshtalele).
- Files: v2-build/stage1/exam-facts-v2.md, blueprint-ledger-v2.md (38 objectives,
  internal IDs V2-Dx.y), prereq-graph-v2.md (§7.1-§7.4 + prep-path map),
  source-registry-v2.md (14 sources, convergence check).
- Model matrix dated Oct 6, 2026: four-tier lineup (Haiku 4.5 / Sonnet 5.5 /
  Opus 5.5 / Fable 5.1) per independent sources; marked secondary pending
  official-doc tie-break. Exam teaches tier-level trade-off judgment.
- Gaps kept visible: no official objective IDs, no per-domain item counts,
  platform parity unchecked (Stages 2-4), post-baseline changes → Stage 9 appendix.
- Next: Stage 2 — prerequisite diagnostic (no answers) + §7.x foundational lessons.

## PDF print spec (2026-10-06 ~13:07 EDT, Raj's order) — standing for the v2 PDF

- Drafted NOW (not at the end): v2-build/print.css + v2-build/pdf-print-spec.md.
- 10pt body / 14pt bold section headers / 18pt bold domain titles; Anthropic Sans
  stack; 1.35 line-height; 0.5in margins; widows/orphans 3; page break before each
  domain; keep-with-next on headers, figures, KEY TAKEAWAY blocks.
- Fragment structural contract (all stages): H1 = domain title, H2 = section,
  :::takeaway fenced divs, <figure class="fig"> + figcaption, fenced code only.
- Images: native size checked first, proportional, max 7.5in, centered, 12pt
  padding, visually verified in the rendered PDF.
- Interactive nested TOC: clickable in digital, physical page numbers in print.
- Depth+conciseness bar (standing law): zero-prerequisite understandability AND
  learn-in-one-sitting conciseness; auditor checks beginner-follows and no
  paragraph repeats earlier teaching. Applies to all v2 fragments.

## Stage 2 (2026-10-06 ~13:16-13:16 EDT... completed 13:15) — COMPLETE

- Prerequisite diagnostic: 16 scenario questions, 4 per foundation area (§7.1-§7.4),
  answer-free (key ships in Stage 8).
- Four foundational micro-lessons (crash-course order §7.4→§7.3→§7.1→§7.2), each on
  the §16 14-item template: lesson-7-4A (requirement→metric→threshold→owner),
  lesson-7-3A (tokens/generation/hallucination/retrieval-vs-tuning/injection),
  lesson-7-1A (timeouts/retries/idempotency/backoff/breakers),
  lesson-7-2A (authN/authZ, enforcement before context, secrets, tenants, audit).
- 20 inline SVG lesson plates, spec palette only, computed arithmetic in figures.
- STE100: 0 hard violations across all 5 files (warnings only). Coordinator verified.
- Depth+conciseness bar applied: each concept taught once, later references by name.
- Stage-2 caveat corrected: the canonical §17 10-step method text lives in the
  coordinator's build brief (it was in Raj's original prompt); Stage 3 workers get
  the canonical text, not the worker's reconstruction.
- Next: Stage 3 — Domains 1 and 2 crash-course lessons.
