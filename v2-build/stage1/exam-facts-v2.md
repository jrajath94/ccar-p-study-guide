# CCAR-P v2 , Stage 1: Exam Identity and Blueprint (Oct 6, 2026)

## 1. Exam identity (verified baseline)

- Certification: **Claude Certified Architect , Professional**, code **CCAR-P** (Anthropic).
- Not Cisco Certified Architect, not Claude Certified Architect , Foundations, not Claude Certified Developer , Foundations, not a course-completion certificate.
- Blueprint: **v1.0, effective July 2026**. No newer blueprint version found in any source as of Oct 6, 2026.
- Format: **63 items**, multiple-choice + multiple-response (each item states how many to select, multiple-response is roughly a quarter of items). No partial credit.
- Duration: **120 minutes**, closed book. Delivery: Pearson VUE (OnVUE online or test center), since June 30, 2026.
- Passing: **720 on a 100,1000 scaled score** (criterion-referenced, score report shows percent-correct per domain, but only the total decides).
- Price: **$175 USD per attempt** (list, Claude Partner Network tier discounts may apply).
- Validity: **12 months** from award. Renewal: free non-proctored assessment on Partner Academy before expiry, lapsed credential = full proctored retake at full price.
- Retakes: wait **14 days** after attempt 1, **30 days** after attempt 2, **90 days** after attempt 3, max **4 attempts per rolling 12 months**.
- Registration: Anthropic Partner Academy, requires Claude Partner Network membership (free). Badge issued via Credly.
- Eligibility: none mandatory. Recommended profile: SWE best practices, 3+ years systems architecture or platform engineering, 6+ months hands-on Claude/LLM in production, end-to-end delivery experience (discovery through operations).
- Exam guide distribution: official guide is partner-gated. **See §2 below.**

## 2. Official-source access statement (§3 of the build prompt)

- The official exam-guide PDF was not directly accessible in this session. It is distributed via the partner-gated Partner Academy page (the public Skilljar page describes the certification but gates the document behind partner login).
- Per prompt §3 this is stated explicitly, not pretended otherwise. Blueprint facts below rest on **corroborated secondary summaries** (four independent sources, each claiming to mirror the official v1.0 guide, all mutually consistent on domain names, weights, item counts, policies, and 38 objectives). They are used provisionally and labeled by provenance in the source registry.
- Objective numbering (e.g. D1.1,D7.3) is a community convention, not an official ID set. This build uses internal IDs **V2-Dx.y** and treats them as internal curriculum navigation only.
- Official questions: the guide ships **sample questions with explanations only** (no full-length practice exam since the Pearson move). No practice item in this build is presented as an actual exam question, all items are original.

## 3. Corroborated blueprint (secondary sources, consistent across all four)

| Domain | Weight | Objectives | ~Items (63) |
|---|---|---|---|
| D1 Solution Design & Architecture | 17% | 6 | ~11 |
| D2 Claude Models, Prompting & Context Engineering | 13% | 5 | ~8 |
| D3 Integration | 19% | 8 | ~12 |
| D4 Evaluation, Testing & Optimization | 16% | 6 | ~10 |
| D5 Governance, Safety & Risk Management | 14% | 5 | ~9 |
| D6 Stakeholder Communication & Lifecycle Management | 14% | 5 | ~9 |
| D7 Developer Productivity & Operational Enablement | 7% | 3 | ~4 |

Per-item counts are estimates derived from weights, not official per-domain counts (per prompt §3: do not claim exact per-domain question counts).

## 4. As-of views

- **View A (baseline, Oct 6, 2026):** everything above plus the dated model matrix in §5 and the objective list in the blueprint ledger. Product facts frozen at this date.
- **View B (post-baseline changes):** tracked in `currentness-appendix.md` (to be built in Stage 9). Model lineage note: at baseline the active lineup per independent sources (agentskit.co Oct 1 2026, izzedo.chat ~Sept 25 2026, qcode.cc Sept 29 2026) is Haiku 4.5 / Sonnet 5.5 / Opus 5.5 / Fable 5.1 , a four-tier lineup, replacing the three-tier Opus/Sonnet/Haiku framing of earlier prep material. **The exam itself is dated to blueprint v1.0 (July 2026) and independent prep material treats it as testing tier-level trade-off judgment, not memorized model IDs.** The crash course teaches tier reasoning with the Oct-2026 matrix as implementation enrichment.

## 5. Dated model matrix (Oct 6, 2026 baseline, secondary sources , verify against Anthropic docs before quoting)

| Tier | Representative model (Oct 6, 2026) | Context | Max output | In/out $ per 1M | Status |
|---|---|---|---|---|---|
| Fast | claude-haiku-4-5 | 200K | 64K | $1 / $5 | GA, retirement not before Oct 15, 2026 |
| Balanced | claude-sonnet-5-5 | 1M | 128K | $2 / $10 | GA, retirement not before Jun 30, 2027 |
| Capable | claude-opus-5-5 | 1M | 128K | $4 / $20 | GA, retirement not before Jul 24, 2027 |
| Most capable | claude-fable-5-1 | 1M | 128K | $10 / $50 | GA, retirement not before Sep 1, 2027 |

Maturity: all GA. Platform-specific IDs and feature parity across Direct API / Bedrock / Vertex / Claude Code must be re-checked per platform , the matrix assumes the Direct API as reference surface. Sources: agentskit.co (updated Oct 1, 2026), izzedo.chat (Sept 2026), qcode.cc (Sept 29, 2026), scriptbyai.com timeline (Sept 2026). All independent/secondary, official docs are the tie-breaker for any conflict.

## 6. Open/unresolved facts (kept visible)

1. Official objective IDs do not exist publicly , using internal IDs only.
2. Exact multiple-response count and unscored-item policy , not published, treated as unknown, not assumed.
3. Per-domain item counts , estimated from weights only.
4. Platform feature-parity details (Bedrock/Vertex surfaces) , to be verified against provider docs in Stages 2,4, unknown until then.
5. Post-baseline model/API changes , tracked in the Stage 9 currentness appendix.
