# Capstone A: enterprise knowledge assistant with permission-aware retrieval

A design-and-defense exercise. The learner produces every section below as the deliverable. The scenario is fixed. The decisions are the learner's, defended against the alternatives.

Scenario: a 4,000-person company wants one assistant over 120,000 internal documents. Three business units. Two clearance levels. Answers need citations. Stale answers are a compliance risk. Budget: $8,000 per month. Latency SLA: p95 at 6 seconds.

## Discovery brief

Outcomes: employees find policy answers in under a minute. Support deflection rises. No cross-unit data leaks, ever.

Capabilities: natural-language questions. Cited answers. Per-user permission filtering. Freshness indicator per answer.

Prohibited behaviors: no answers from documents the user cannot read. No stored answers older than the source version. No PII in logs.

Workflows: question, retrieve, filter, generate, cite, log. Escalation to a human on low grounding scores.

Cost limits: $8,000 per month all-in. Volume: 30,000 questions per month. Quality: citation support at 95% on the eval set. Latency: p95 at 6 s. Availability: 99.5%.

Compliance: per-unit data walls. Audit log of every answer with the document versions cited. Retention: 1 year.

Dependencies: the document store. The identity provider. The eval set owner.

Owners: product owner, data-team lead, security reviewer.

Open assumptions: the document store exposes per-document ACLs. The identity provider resolves group membership in under 200 ms.

## Architecture alternatives

Option 1: RAG with metadata ACL filtering. Staged pipeline per V2-D3.5. Filter before scoring per V2-D3.6. Hybrid retrieval with rerank.

Option 2: per-unit deployments. Three separate stacks, one per business unit. Physical isolation.

Option 3: large-context prompting over a per-user document bundle. Assemble the user's readable set at query time.

Trade table:

| Dimension | Option 1: RAG plus ACL | Option 2: per-unit stacks | Option 3: per-user bundle |
|---|---|---|---|
| Isolation | Filter in code | Physical | Assembly in code |
| Cost | One pipeline | Three pipelines | Token-heavy per call |
| Freshness | Re-ingest cadence | Per-stack cadence | Always fresh |
| Citations | Per-chunk grounding | Per-chunk grounding | Harder to attribute |
| Ops | One system | Three systems | No pipeline |

Recommendation: Option 1. One pipeline, deterministic filtering, per-chunk citations. Option 2 is valid but triples ops for an isolation level the requirement does not demand. Option 3 fails the token budget at 30,000 questions per month.

## Requirements

Functional: answer questions from the corpus. Cite every factual claim. Filter by the caller's permissions before scoring. Show the source version per citation.

Nonfunctional: p95 latency 6 s. Citation support 95% on the eval set. Zero cross-unit leaks on the adversarial drawer. Cost ceiling $8,000 per month.

Hard constraints: no denied document reaches the model. No answer without a passing grounding check ships. Every answer is logged with the cited versions.

Success criteria: 95% citation support. Zero leaks in 90 days. p95 under 6 s. Spend under budget.

## Decision records

ADR-A1: RAG over fine-tuning. Facts change weekly. Citations required. Weights cannot cite.

ADR-A2: metadata ACL filter before scoring. The filter is the enforcement point. Missing metadata fails closed.

ADR-A3: hybrid retrieval with rerank. Queries mix codes and paraphrases. Keyword alone fails the paraphrase class.

ADR-A4: no response caching. Answers depend on per-user permissions and document versions. A cached answer is a stale or leaked answer.

## Security review

Threats: cross-unit read via filter bypass. Prompt injection via a poisoned document. Stale answer served as current. PII in logs.

Controls: the A9 filter as the enforcement point. Ingestion screening for injection patterns. Freshness probe on the index with a staleness alert. PII stripping before logs leave the trust boundary.

Fail-closed rules: policy store down means deny. Missing chunk metadata means exclude. Grounding check failure means no answer ships.

Residual risks: a permitted document can still be wrong. Accepted by the product owner with a correction workflow and a review date.

## Evaluation plan

Dataset: 500 cases across the five drawers from V2-D4.2. Adversarial drawer includes cross-unit read attempts and injection prompts. Regression drawer grows with every fixed bug.

Grading ladder: code checks for format and citation presence. Entailment check for citation support. Human labels for the disputed class. Judges calibrated before use.

Gates: 95% citation support to ship. Zero leaks on the adversarial drawer to ship. Regression drawer green on every change.

Production: shadow the new pipeline against the old for two weeks. Then a controlled rollout per business unit.

## Cost and latency budget

Volume: 30,000 questions per month, about 1,000 per day.

Per-question budget: retrieval plus rerank at $0.0005 (toy). Generation: 1,500 input tokens and 300 output tokens on the Balanced tier ($2 in, $10 out per 1M): $0.003 plus $0.003 = $0.006. Total per question about $0.0065. Per month: 30,000 times $0.0065 = $195. Pipeline and hosting amortized at $2,000 per month. Total about $2,195 per month, under the $8,000 ceiling with headroom for growth.

Latency budget: identity resolution 200 ms. Retrieval plus rerank 800 ms. Generation p95 3 s. Grounding check 500 ms. Total p95 about 4.5 s, under the 6 s SLA.

## Implementation contracts

Ingestion contract: input, a document with ACL metadata. Output, screened chunks with tenant, unit, clearance, and version tags. Failure: quarantine, alert, skip.

Retrieval contract: input, query plus caller identity. Output, top chunks filtered by ACL before scoring. Failure: deny on policy store outage.

Generation contract: input, filtered chunks plus the question. Output, answer with citations that pass the support check. Failure: no answer ships on grounding failure.

Logging contract: input, the run record. Output, an audit entry with the cited versions. Failure: block the answer if the audit write fails.

## Deployment gates

Gate 1: eval green on all drawers, including zero leaks on the adversarial set.

Gate 2: security review signed, with the fail-closed rules tested.

Gate 3: shadow run for two weeks with no unexplained divergence.

Gate 4: cost dashboard live with the $8,000 ceiling and an owner.

Gate 5: runbook drill completed by the receiving team.

## Ownership

Product owner: the assistant's roadmap and the quality floors. Data-team lead: the pipeline, the index, freshness. Security reviewer: the filter, the audit log, the control cadence. On-call rotation: the watches and the runbook.

## Runbook

Symptom: citation support drops. Check which drawer dropped. Retrieval drawer: check index freshness and chunk diffs. Adversarial drawer: check for a new injection pattern and add a case. Else: check the model pin and the prompt version. Mitigate: roll back the last change. Escalate to the data-team lead if the index is stale past 1 hour.

Symptom: latency p95 breaches 6 s. Check context size per call before the model. Check the reranker queue. Check the identity provider latency. Mitigate: shed the rerank depth first, never the ACL filter.

## Stakeholder presentation

One page per audience. Executives: the value case, the cost ceiling, the risk posture. Engineering: the pipeline, the contracts, the gates. Security and legal: the filter as enforcement, the audit mapping, the fail-closed rules. Each page states the decision, the cost, the risk, and the reversal cost.

## Failure injection

Inject 1: poison one document with an instruction to ignore policy. Expect: ingestion screening quarantines it. The adversarial drawer catches any escape.

Inject 2: revoke a user's clearance mid-session. Expect: the next query filters the newly denied documents. No cached answer leaks.

Inject 3: take the policy store offline. Expect: deny on all retrieval. The assistant says it cannot verify permissions. No silent pass.

Inject 4: serve a stale index version. Expect: the freshness probe fires within the cadence window. The runbook rolls back the index.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The filter decides before scoring</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Two units. One query. The filter runs before the ranker.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: FILTER AFTER SCORING</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">unit B doc ranked 1</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Ranker saw denied docs.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">Snippet leaks in the trace.</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Filter as an afterthought.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: FILTER BEFORE SCORING</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">unit A docs only</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">Denied docs never scored.</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">Nothing to leak downstream.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Missing metadata excluded.</text>
<defs><marker id="mca" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mca)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">filter first</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The model cannot leak documents it never scored.</text>
</svg>
<figcaption>Shell 3. The ACL filter moves before scoring, so denied documents never reach the ranker. Source: original toy.</figcaption>
</figure>

## Related exam scenarios

V2-D3.5: design the RAG pipeline with grounding checks. V2-D3.6: hybrid retrieval plus the metadata ACL filter. V2-D3.2: deterministic enforcement, no shared credentials. V2-D4.2: the five-drawer eval set with the adversarial leak cases. V2-D5.4: the requirement-to-evidence mapping for the audit.

:::takeaway
One pipeline. The filter before scoring. Citations that pass the support check. Every answer logged with its source versions.
:::
