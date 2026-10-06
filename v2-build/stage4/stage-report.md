# Stage 4 Report: Domain 3 Integration (V2-D3.1 to V2-D3.8)

Built: Oct 6, 2026. Builder: Stage 4 worker 939509a5. Baseline: Oct 6, 2026.

## Objective-to-lesson map

| Objective | Lesson file | Mechanism | Decision boundary | Worked example | Transfer assessment |
|---|---|---|---|---|---|
| V2-D3.1 capability bloat | lesson-D3-1.md | 3 channels: selection confusion, data visibility, write scope | Removal revokes. Logging only watches | 25-tool support agent, 10-step picks scoped subset | Research agent, 60 tools |
| V2-D3.2 authN/authZ | lesson-D3-2.md | 5 identity rules: per-user delegation, audience binding, no passthrough, session vs identity, source ACLs | Shared credential vs delegation. Attribution decides | 50,000 actions/day, 10-step picks delegation | Clinic calendar MCP server |
| V2-D3.3 accuracy-latency | lesson-D3-3.md | 4 questions: cost per stage, gain per stage, SLA bind, measurability | Cut worst ms-per-point when SLA binds | p95 2,900 vs 2,000 SLA, 10-step cuts rerank | Translation pipeline p99 |
| V2-D3.4 observability | lesson-D3-4.md | 9 trace parts. One id. Cost per hop. Sampling plus redaction | Metrics vs traces. Reconstructability decides | 15-hop refund run, 10-step picks trajectory | Travel agent double charge |
| V2-D3.5 RAG pipeline | lesson-D3-5.md | 10 stages. Errors compound downstream. Grounding is deterministic | Fix upstream first | Split-table chunker, 10-step picks re-chunk | Legal assistant clause split |
| V2-D3.6 retrieval strategies | lesson-D3-6.md | Keyword, semantic, hybrid, metadata filters, rerank, rank fusion. Freshness rule | Matcher vs freshness. Time decides | Stale order status, 10-step routes to tool | Bank balance index |
| V2-D3.7 integration mechanisms | lesson-D3-7.md | 5 mechanisms. 6 axes. MCP lifecycle pinned. 5 layers | Reuse decides. N+M vs N x M | Single-host billing API, 10-step picks direct API | 4-host warehouse tools |
| V2-D3.8 progressive discovery | lesson-D3-8.md | Advertise lightly. Fetch lazily. Scope the list | Tokens and confusion vs fetch latency | 200-tool agent, 10-step picks discovery | 120-tool code agent |

Every lesson carries the §16 template: 14 sections plus a page-audit
table with 14 rows, no blank figure cells. Every worked example trains
the canonical §17 10-step method verbatim plus the verbatim
do-not-assume paragraph. Every transfer question ships without an
answer. Stage 8 owns all keys.

## Evidence added

- MCP spec concepts (host, 1:1 client per server, tools/resources/
  prompts, JSON-RPC, initialize, tools/list, tools/call,
  resources/read, prompts/get, stdio, Streamable HTTP) corroborated
  by independent sources against the 2026-07-28 revision. Class:
  spec concepts, corroborated, not official-doc inspected.
- MCP authorization profile (OAuth 2.1, RFC 9728 protected resource
  metadata, RFC 8707 resource indicators, audience binding, token
  passthrough forbidden, DCR deprecated in the 2026-07-28 revision,
  local stdio inherits user trust) corroborated by independent
  sources, Sept 2026. Class: spec concepts, corroborated.
- All toy arithmetic computed inline: schema token loads, per-stage
  latency sums, ms per accuracy point, precision/recall, trace
  volume, N x M vs N + M, daily token savings.
- Blueprint and exam-scope claims carried from S03/S04 via the
  stage-1 registry, labeled official-exam-scope-via-secondary.

## Gaps and corrections

- D3.3's ledger prereq V2-D4.1 (evaluation metrics) is a Stage 5
  objective, not yet taught. The lesson uses only Lesson 7-4A's
  threshold rule and notes Stage 5 deepens measurement. No content
  invented for D4.1.
- MCP exact product support per primitive is marked unverified in
  D3.7's evidence table. Product docs are the tie-breaker.
- The 2026-07-28 MCP spec revision details rest on independent
  corroboration, not a same-session read of modelcontextprotocol.io.
  Flagged in each evidence table. If Stage 9 or the coordinator
  opens the official spec, re-check the DCR-deprecated and
  passthrough-forbidden claims first.
- No SHOULD was promoted to MUST. Normative language follows the
  corroborated sources with revision labels.
- No re-teaching: 7-1A traces, 7-2A authN/authZ, 7-3A retrieval and
  tool mechanics, D1-patterns cost of calls, D2-1 routing, D2-4
  context, D2-5 caching are reused by name only.
- STE100: all 8 lessons pass ste_check.py with zero hard fails.
  Remaining warnings are nouns (logging, scoping) and possessives,
  both allowed.

## Stage 5 needs

- V2-D4.4 (diagnose at the right layer) should reference D3.5's
  ten-stage pipeline and D3.6's freshness rule as diagnosis targets.
- V2-D4.5 (optimize tokens/latency/cost) should build on D3.3's
  per-stage receipts and D3.8's discovery trade-off.
- V2-D4.6 (monitor production) should extend D3.4's trace model with
  drift detection and alert ownership.
- Stage 8 question bank: 8 transfer questions banked (one per
  lesson), keys not written.
- Stage 9 currentness appendix: re-verify MCP spec revision claims
  against modelcontextprotocol.io and product support per primitive.
