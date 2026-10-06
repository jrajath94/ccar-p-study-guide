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

## Stage 3 (2026-10-06 ~13:20-13:29 EDT) — COMPLETE

- Domains 1 and 2 crash-course lessons, all 11 objectives:
  lesson-D1-1 (V2-D1.1 Claude-vs-deterministic fork), lesson-D1-2 (V2-D1.2
  seven-gate pipeline), lesson-D1-patterns (merged V2-D1.3+D1.4+D1.5, each objective
  keeps its own §16 items 1-5,9-13), lesson-D1-6 (V2-D1.6 net-value equation),
  lesson-D2-1..D2-5 (tiers/cascade, prompt zones, technique ladder, context
  accounts, caching prefix rule + 4% break-even).
- Canonical §17 10-step method trained verbatim in all 11 worked examples +
  anti-slogan paragraph. Stage 2 foundations reused by name only.
- 50 inline SVGs, all parse as XML, spec palette, unique marker IDs, shell+source
  captions, shown arithmetic ("Not in source" on invented toy rates; cache
  pricing labeled current product behavior; tier matrix labeled secondary
  enrichment).
- STE100: coordinator re-ran ste_check on all 9 lesson files — 0 hard violations.
- Transfer questions answer-free (Stage 8 owns keys). Print contract honored.
- Next: Stage 4 — Domain 3 (Integration, 8 objectives, heaviest domain).

## Stage 4 (2026-10-06 ~13:30-13:38 EDT) — COMPLETE

- Domain 3 (Integration, 19%), all 8 objectives: capability bloat (logging is not
  removal), authN/authZ + MCP OAuth 2.1 profile, accuracy-latency (rerank priced
  at 750ms/accuracy point), observability (nine trace parts, one id), RAG
  pipeline (10 stages, precision/recall toy), retrieval strategies (freshness
  rule: live state behind a tool call), integration mechanisms (MCP lifecycle
  pinned, NxM vs N+M arithmetic), progressive discovery (94.5% token cut).
- Canonical §17 verbatim in all 8 worked examples. 0 hard STE violations
  (coordinator re-verified). 25 SVGs parse. Prior stages reused by name only.
- Caveats kept visible: MCP spec claims corroborated by independent sources, not
  a same-session official-spec read (Stage 9 re-verify); Claude product support
  per MCP primitive marked unverified; D3.3 prereq V2-D4.1 untaught (Stage 5).
- Next: Stage 5 — Domains 4 and 5 (Evaluation; Governance/Safety/Risk).

## Stage 5 (2026-10-06 ~13:40-13:49 EDT) — COMPLETE

- Domains 4 (16%) and 5 (14%), all 11 objectives: eval metrics, datasets/frameworks,
  A/B testing, failure diagnosis, optimization, production monitoring, guardrails,
  risk taxonomy, human-in-the-loop, compliance (not legal advice), responsible AI.
- 0 hard STE violations (coordinator re-verified). 55 SVGs parse after 2 tag fixes
  by the coordinator (rect/text mismatches in D5-3 and D5-4 figure 3).
- Canonical §17 verbatim in all 11 worked examples. Transfer questions answer-free.
- Claim classification + dates in every evidence table; toy rates marked.
- Next: Stage 6 — Domains 6 and 7 (Stakeholders/Lifecycle; Dev Productivity).

## Stage 6 (2026-10-06 ~13:50-13:58 EDT) — COMPLETE

- Domains 6 (14%) and 7 (7%), all 8 objectives: structured discovery (485:1),
  trade-off communication (five fields/five audiences), expectation alignment
  (error budgets, iterate-vs-re-architect), ADRs (nine fields, 60:1),
  lifecycle phases (five phases, four gates, no-substitution), team config
  (guidance vs enforcement, verified vs docs Oct 6), AI-assisted workflows
  (four-part evidence rule), debugging (symptom-to-suspect map, runbooks).
- All 38 objectives now have crash-course lessons (33 domain + 5? no: 11+8+11+8).
  Correction: Stage 3 built 11, Stage 4 built 8, Stage 5 built 11, Stage 6 built 8.
- 0 hard STE violations (coordinator re-verified). 32 SVGs parse.
- Next: Stage 7 — comparisons (§18), artifacts (§21), labs, 3 capstones (§23).

## Completion validation gate (2026-10-06 ~14:06 EDT, Raj's order)

Runs after Stage 9, before any completion is declared. Checklist recorded at
v2-build/completion-gate-checklist.md. Four gates, all must pass:
1. Presence validation: explicit checklist of every required deliverable
   (crash-course HTML with 7 domains + diagnostics + foundations; all §18
   comparisons with 3+ minimal pairs; all §21 artifacts; 3 capstones + 9 labs;
   25/domain + 50 mixed + 4 mocks + counterfactual drills; error ledger;
   readiness dashboard; Oct 6 currentness appendix; final review sheets; source
   registry; blueprint ledger; print-spec PDF; zip). No MISSING may remain.
2. Figure validation: page audit per visual_system_generic.md; every
   AI-generated image verified on-topic and clean; regenerations logged.
3. PDF validation per print spec: type scale, line height, margins,
   widow/orphan, domain page breaks, keep-with-next, clickable TOC with verified
   page numbers, aspect-ratio-checked images, monospace no-wrap code. Visual
   inspection of every image-bearing page.
4. Repo validation: final push to jrajath94/ccar-p-study-guide, then remote vs
   local verification — every file present, no drift, README + BUILD-LOG
   current, zip + PDF downloadable and intact. Re-push gaps before done.
Results go into BUILD-LOG.md as the final section.

## Stage 7 (2026-10-06 ~14:00-14:10 EDT) — COMPLETE

- All 26 §18 comparisons as tight matrices with ≥3 minimal pairs each
  (comparisons-01..05, 78 minimal pairs total); 23 §21 artifacts
  (artifacts-01/02; A5/A12/A13 executed locally with real output, 20 marked
  ILLUSTRATIVE; "Evaluation runner" renamed from STE100-banned term);
  9 labs (local-first, cost caps, cleanup documented); 3 capstones A/B/C with
  all 14 sections, computed budgets, failure injection.
- 0 hard STE violations (coordinator re-verified). 11 SVGs parse.
- Next: Stage 8 — original assessment system (question bank + independent audit).

## Stage 8a (2026-10-06 ~14:15-14:27 EDT) — COMPLETE

- 100 original questions: 25 per domain for D1-D4 (qb-D1..qb-D4). IDs
  Q-D1-01..Q-D4-25, all unique. 24 multi-response (~a quarter). Coverage tables
  meet per-objective minimums. Every item: scenario, options, answer key,
  §17 10-step walk, all 10 §19.2 explanation points. 5 weak items rewritten
  (Q-D1-21 arithmetic; Q-D2-25, Q-D3-18, Q-D3-25, Q-D4-11 Select-TWO→THREE).
- 0 hard STE violations (coordinator re-verified). Distractors reuse the
  lessons' documented traps. Toy assumptions labeled "not in source".
- Open: independent adversarial audit of every answer key (Stage 8d).
- Next: Stage 8b — D5-D7 questions (75).

## Stage 8b (2026-10-06 ~14:28-14:41 EDT) — COMPLETE

- 75 original questions: 25 per domain for D5-D7 (qb-D5..qb-D7). IDs
  Q-D5-01..Q-D7-25, all unique. 18 multi-response (24%). Coverage tables meet
  per-objective minimums (D7: 9/8/8). Full §19.2 10-point explanations.
- 0 hard STE violations (coordinator re-verified). D5.4 items carry
  not-legal-advice labels; D7 config claims cite lesson-D7-1.
- All 12 unseen-transfer questions from stages 5-6 lessons are answered in
  the banks. (Stages 2-4 transfer answers also belong in Stage 8 — noted for
  8c/d check.)
- Next: Stage 8c — 50 mixed + counterfactual drills + diagnostic key + 4 mocks.

## Stage 8c (2026-10-06 ~14:42-15:03 EDT) — COMPLETE

- 50 mixed-domain questions (qb-mixed.md, blueprint-weighted, Q-M-01..50);
  52 counterfactual drills (CF-01..52, 2 per §18 pair); diagnostic answer key
  (diagnostic-key.md, 16 items with remediation pointers); 4 full 63-item mocks
  (mocks.md, M1-Q01..M4-Q63, domain mix per verified weights, 120-min plans,
  no raw-percentage pass promises). 370 new items, all original, none reused.
- One incident repaired by the worker: a cleanup regex deleted 18 option letters
  + 3 quote duplications; all found and hand-repaired.
- 0 hard STE violations (coordinator re-verified). Full bank now: 477 questions
  + 52 drills + 16 diagnostic items.
- Next: Stage 8d — independent adversarial audit (fresh worker, per-question
  status, fix loop max 3).

## Stage 8d (2026-10-06 ~15:05-15:15 EDT) — COMPLETE (independent adversarial audit)

- Fresh worker (built none of the material) attacked all 477 questions + 16
  diagnostic keys per §19.3. Verdicts: PASS 489, FIXED 4, REJECTED 0, PENDING 0.
- Fixes: Q-M-15 Select TWO→THREE (three defensible answers); M3-Q33 key A→B
  (old key demanded an untaught requirement); Q-D3-07 explanation (residual
  200ms gap stated); Q-D5-21 arithmetic 94%→90.4%≈90% in scenario/option/key.
- 4 genuine attacks defeated (Q-D4-03, M1-Q28, M4-Q33, priority flags M2-Q13,
  M4-Q47 all stood). All scenario arithmetic spot-checked; one inconsistency
  found and fixed.
- Deliverables: audit-report.md (per-question status), audit-changelog.md,
  rejected-items.md (empty). Banks corrected in place. 0 hard STE.
- Next: Stage 9 — final coverage/accuracy/currentness/ambiguity audit.

## Stage 9 (2026-10-06 ~15:15-15:25 EDT) — COMPLETE (final quality-gate audit)

- Independent auditor ran all 12 §26 gates: 10 PASS, 2 PASS with open items.
- Open items fixed by the coordinator: (1) ledger status codes S→A for all 38
  objectives (lessons + question coverage + audit all exist); (2) Stage 2 lessons
  §17 reconstruction replaced with the canonical verbatim 10-step text +
  anti-slogan paragraph (lesson-7-4A/7-3A/7-1A/7-2A); (3) STE hard fails cleaned
  in stage1 files (ledger, exam-facts, prereq-graph, source-registry) and
  stage5/stage-report.md — all 0 hard now.
- §24 deliverables built: error-ledger.md, readiness-dashboard.md,
  currentness-appendix.md (View A baseline / View B empty-but-open), final-review-sheets.md.
- Stage 9 audit found: no post-Oct-6 claims, no fabricated execution, 3 executed
  artifacts re-ran with matching output, 20 marked ILLUSTRATIVE, mocks carry
  no-pass-prediction disclaimers.
- Next: ASSEMBLY — crash-course.html + AI images + print-spec PDF + zip, then
  the completion validation gate.

## ASSEMBLY (2026-10-06 ~15:25-15:40 EDT) — COMPLETE

- Assembler: v2-build/assemble.py (markdown fragments -> HTML, H1/H2 demotion,
  per-section id prefixes, :::takeaway -> key-takeaway divs, nested clickable
  TOC, chapter images injected).
- crash-course.html (1.26MB): 22 sections — exam facts, diagnostic, 4
  foundations, D1-D7 lessons (38 objectives), 26 comparisons, 23 artifacts,
  9 labs, 3 capstones, review sheets, readiness dashboard, error ledger,
  currentness appendix, source registry + blueprint ledger. 204 figures,
  119 key-takeaway blocks, 531 ids, 0 broken TOC links.
- question-bank.html (1.06MB): 11 sections — diagnostic key, 477 questions
  (qb-D1..D7, qb-mixed), 52 counterfactual drills, 4 full mocks. 624 ids,
  0 broken TOC links.
- 12 AI-generated chapter plates (Muse native pipeline only, per provenance
  rule): cover + D1-D7 + 4 foundations. All 12 reviewed against the visual-spec
  reject list: 12/12 pass, 0 regenerations needed.
- wm_clean.py Layer A run on both HTMLs (byte audit, no changes needed).
- PDF builder: v2-build/build_pdf.py — two-pass Chromium render (letter,
  0.5in margins), named-destination page numbers injected into the TOC,
  pypdf stamp (running header + page numbers, cover clean, /Dests preserved),
  metadata stripped (Producer: None verified).
- crash-course.pdf: 235 pages, 11MB. question-bank.pdf: 287 pages, 3.9MB.
- PDF QA: TOC page numbers verified against actual dest pages (22/22
  crash-course, 11/11 question-bank, 0 mismatches). Image pages visually
  inspected (cover, D1/D3 chapter plates, SVG figure pages, code pages):
  all render sharp, correct proportions, not clipped. Code blocks monospace,
  no wrapping. No widow/orphan or split-takeaway violations observed.
- Fixes during assembly: Chromium flaky dest creation (retry until all
  sections resolve); /tmp relative image paths (base tag); pypdf 6.19 API
  (clone as method); named-dest leading-slash keys.
- Zip: ccar-p-crash-course-v2.zip (HTMLs + PDFs + img-v2 + README + BUILD-LOG).
