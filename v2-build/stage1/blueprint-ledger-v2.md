# Blueprint Coverage Ledger — CCAR-P v2 (all 38 objectives)

Provenance: objective texts paraphrased from corroborated secondary summaries of the
official v1.0 guide (see source-registry-v2.md). Internal IDs (V2-Dx.y) are
curriculum navigation only. Verification status codes: S=sourced, L=lesson drafted,
Q=question coverage built, A=audited.

## D1 — Solution Design & Architecture (17%, ~11 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D1.1 | Translate business problems into Claude-based solutions: outcomes, functional vs nonfunctional requirements, hard constraints, Claude-vs-deterministic decision, measurable success criteria | §7.4 business foundations | 3 | S |
| V2-D1.2 | Design end-to-end architectures: input→validation→context/retrieval→model/tools→verification→output→feedback; trust boundaries, system of record, state, retries/fallbacks, telemetry | §7.1 distributed systems | 3 | S |
| V2-D1.3 | Select architectural patterns: augmented single call, deterministic workflow, agentic, hybrid; evaluate on predictability, reversibility, error cost, latency, cost, observability, dynamic-planning need | V2-D1.1, §7.1 | 3 | S |
| V2-D1.4 | Design multi-agent systems and orchestration: coordinator/worker, specialist roles, handoff contracts, disagreement handling, checkpointing, trace propagation, justify multi-agent over single agent+tools | V2-D1.3 | 3 | S |
| V2-D1.5 | Apply decomposition: bounded tasks, deterministic/probabilistic split, parallelizable independent work, routing/chaining/fan-out/fan-in/critique/validation patterns | V2-D1.3 | 3 | S |
| V2-D1.6 | Align solutions to business value: efficiency/productivity/transformation/quality/cost/latency/reliability/SLOs; baseline→improvement→cost→net value | §7.4 | 3 | S |

## D2 — Claude Models, Prompting & Context Engineering (13%, ~8 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D2.1 | Select Claude models on trade-offs: capability/speed/latency/cost; routing, cascading, escalation, fallback, quality floors; treat upgrades as production changes with regression testing | §7.3 LLM foundations | 3 | S |
| V2-D2.2 | Design system prompts, templates, guardrails: stable vs untrusted content separation, role/scope/constraints/output contract, structural enforcement for hard guarantees; prompts are not authorization | V2-D2.1 | 3 | S |
| V2-D2.3 | Apply prompt techniques: zero-shot, few-shot with rejection examples, explicit reasoning, structured outputs, edge-case examples; simplest technique that passes evals | §7.3 | 3 | S |
| V2-D2.4 | Optimize context windows and token usage: active context vs retrieval vs app state vs conversation memory; full/recent/just-in-time/compaction; diagnose growth, duplication, loss, exhaustion, dilution | V2-D2.1 | 3 | S |
| V2-D2.5 | Implement prompt reuse: prompt caching (prefix rules, TTL, costs, break-even), modular prompts, Skills as governed assets, versioning shared components | V2-D2.3, V2-D2.4 | 3 | S |

## D3 — Integration (19%, ~12 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D3.1 | Evaluate tool/agent config for capability bloat: least privilege, remove unneeded tools, limit data visibility and writes, overlapping descriptions; logging is not removal | §7.2 security | 4 | S |
| V2-D3.2 | Analyze authentication and authorization: authN vs authZ, tenant isolation, auditability, trusted identity sources (user role claims are not authZ), preserve source-system ACLs, no shared creds when attribution matters, deterministic enforcement for side effects | §7.2 | 4 | S |
| V2-D3.3 | Evaluate accuracy-latency trade-offs: per-stage latency, whether retrieval/rerank/extra calls/deeper reasoning help, optimize to SLAs, tail latency, no unmeasurable complexity | V2-D4.1, §7.4 | 4 | S |
| V2-D3.4 | Analyze observability at scale: trace model calls, retrieval, tools, queues, dependencies, retries, errors, trajectories, cost, tokens; end-to-end reconstructability | §7.1 | 4 | S |
| V2-D3.5 | Design a RAG pipeline: ingestion→parsing→chunking→metadata→indexing→retrieval→rerank→assembly→generation→grounding/citation checks; chunking by document structure and query type | §7.3 | 4 | S |
| V2-D3.6 | Apply retrieval strategies to the data: keyword, semantic, hybrid, metadata filters, reranking/rank fusion; live transactional state belongs behind a tool call, not a stale index | V2-D3.5 | 4 | S |
| V2-D3.7 | Select integration mechanism: direct API/SDK, CLI, MCP, agent-to-agent, managed runtime; compare on reuse, security boundaries, ownership, operational complexity, compatibility, interaction pattern | §7.1 | 4 | S |
| V2-D3.8 | Evaluate progressive discovery vs monolithic context: discover capabilities on demand, cut token overhead and selection confusion, shrink attack surface | V2-D3.1, V2-D2.4 | 4 | S |

## D4 — Evaluation, Testing & Optimization (16%, ~10 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D4.1 | Define evaluation metrics: task success, groundedness, safety, security, latency, reliability, cost, business outcome; vague requirements to acceptance thresholds | §7.4 | 5 | S |
| V2-D4.2 | Design evaluation datasets and frameworks: representative/edge/adversarial/malformed/regression cases, holdouts; cheapest reliable evaluator (code < judge < human); calibrate judges against human labels | V2-D4.1 | 5 | S |
| V2-D4.3 | Conduct A/B testing and iteration: falsifiable hypothesis, primary metric first, consistent assignment, sample size, significance vs business significance, shadow testing | V2-D4.2 | 5 | S |
| V2-D4.4 | Diagnose system issues at the right layer: prompting, retrieval, model selection, tools, orchestration, data, version behavior; fix the failing component, not a proxy | V2-D3.5, V2-D3.6 | 5 | S |
| V2-D4.5 | Optimize tokens, latency, cost-performance: per-stage measurement, oversized context, caching, routing, call elimination, p95/p99, hold quality and safety floors | V2-D2.4, V2-D2.5 | 5 | S |
| V2-D4.6 | Monitor production: operational metrics, instrumentation of model/retrieval/tools/dependencies, drift detection, regression suites, alerts with owners, representative eval data | §7.1, V2-D3.4 | 5 | S |

## D5 — Governance, Safety & Risk Management (14%, ~9 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D5.1 | Implement guardrails and safety controls: model safeguards, system instructions, input/output screening, deterministic tool authorization, sandboxing, least privilege; know which controls must fail closed | §7.2 | 5 | S |
| V2-D5.2 | Identify risks, limitations, failure modes: hallucination, direct/indirect prompt injection, excessive agency, tool abuse, data exposure, cost exhaustion, bias, supply-chain risk, silent orchestration failure; prevention/detection/recovery per risk | §7.2, §7.3 | 5 | S |
| V2-D5.3 | Apply human-in-the-loop validation: review strength keyed to consequence, reversibility, uncertainty, regulation, financial/safety impact; pre-action approval vs post-action vs sampled review; reviewers need real decision context | §7.4 | 5 | S |
| V2-D5.4 | Ensure regulatory compliance: GDPR/HIPAA/FedRAMP effects on data handling, access, logging, retention, deployment route, residency, evidence; requirement→control→owner→evidence→cadence | §7.2 | 5 | S |
| V2-D5.5 | Address responsible/ethical AI: bias, fairness, transparency, explainability, accountability, traceability; evaluate across subgroups, not aggregate only | §7.4 | 5 | S |

## D6 — Stakeholder Communication & Lifecycle Management (14%, ~9 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D6.1 | Conduct structured discovery: outcomes, capabilities, prohibited behaviors, workflows, cost limits, volume, quality/latency/availability expectations, compliance, dependencies, owners, open assumptions; turn adjectives into measurable requirements | §7.4 | 6 | S |
| V2-D6.2 | Communicate architecture decisions and trade-offs: benefit, cost, risk, reversal cost, compliance impact per option; adapt message to exec, engineering, security, legal, product | §7.4 | 6 | S |
| V2-D6.3 | Manage feedback and expectation alignment: measurable quality, realistic SLAs for probabilistic systems, review triggers, breach consequences, iterate vs re-architect, production cost forecasting | V2-D6.1, V2-D4.1 | 6 | S |
| V2-D6.4 | Document architectures: ADRs with decision/date/alternatives/rejections/assumptions/trade-offs/owner/evidence/open issues/review criteria; successor-operable without original meetings | V2-D1.2 | 6 | S |
| V2-D6.5 | Support lifecycle phases: discovery→design→handoff→monitoring→iteration; no substituting later-phase work for unfinished discovery/design | §7.4 | 6 | S |

## D7 — Developer Productivity & Operational Enablement (7%, ~4 items)

| ID | Objective (paraphrased) | Prereqs | Stage | Status |
|---|---|---|---|---|
| V2-D7.1 | Configure Claude tools for teams: project/team guidance, shared config, MCP/tool config, permission modes, hooks, sandboxing, scoped subagents, reusable Skills, model/spend guardrails; instructions vs enforceable permissions | §7.1, §7.2 | 6 | S |
| V2-D7.2 | Improve developer workflows with AI tooling: repo exploration, implementation, refactoring, testing, review, debugging, docs, incident investigation; verification requirements (tests ran, results inspected, secrets protected) | V2-D7.1 | 6 | S |
| V2-D7.3 | Support debugging and operational resolution: symptom→investigation mapping (quality→prompt/model/retrieval drift; latency→context/deps/cache; tools→creds/perms/throttling; cost→routing/context/caching; lost agent work→orchestration state/traces); runbooks, escalation, ownership | V2-D4.4, V2-D7.1 | 6 | S |

Ledger rule: an objective moves from S to L only when its lesson carries a mechanism explanation, a decision boundary, an application example, and a diagnostic/transfer assessment (§5.1).
