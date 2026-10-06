# Comparisons 01: patterns and orchestration

Six high-confusion pairs from §18, tight matrices. Each pair: shared ground, decisive difference, constraint table, costs, security, operations, a counterexample, evidence, and three minimal pairs. Prior-stage concepts appear by name only.

:::takeaway
The scenario picks the pattern. A constraint change of one line flips the winner. Learn the flip, not the slogan.
:::

## Pair 1: workflow vs agent

Shared: both chain model calls and tools to reach an outcome. Both need timeouts, traces, and retry policy from Lesson 7-1A. Both run on the same Messages API from Lesson D2-1.

Decisive difference: the workflow fixes the step order in code. The agent lets the model choose steps at runtime. The seven-axis score from Lesson D1-patterns (predictability, reversibility, error cost, latency, cost, observability, dynamic-planning need) decides.

| Dimension | Deterministic workflow | Autonomous agent loop |
|---|---|---|
| Step order | Fixed in code | Planned by the model |
| Call count | Known before the run | Varies per run |
| Cost per run | Computable in advance | Bounded only by max steps |
| Trace shape | Same plan each run | Plan differs per run |
| Failure mode | A named step fails | Silent plan drift |
| Best fit | Steps known (V2-D1.3) | Steps unknown until runtime |

Winning constraints: the workflow wins when steps are fixed and error cost is high (V2-D1.3, V2-D1.5). The agent wins when no code can list the steps in advance (V2-D1.3 counterfactual: open research).

Losing constraints: the workflow loses when the task needs judgment at open joints (push hybrid). The agent loses on fixed cases: it varies the plan run to run and costs per-call times steps.

Costs: workflow cost equals the known call count times per-call price. Agent cost equals average steps times per-call price, plus variance. On the Lesson D1-patterns toy: augmented $0.006 per case, agentic $0.024 per case, hybrid $0.00277 per case, $55.40 versus $480 per day.

Security: the workflow shrinks attack surface. A fixed step list is a fixed permission list (V2-D3.1). The agent widens it: tool selection is model output, so prompt injection can steer it toward a dangerous tool (V2-D5.2).

Operational burden: the workflow is debuggable. Replay the step log. The agent needs trajectory tracing (V2-D3.4) and plan-change alerting. Both need the same retry and idempotency machinery.

Counterexample: a compliance review with a fixed checklist still benefits from an agent when the checklist itself is the unknown. No code can list sources in advance. The search plan is the task.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Four-stop spectrum, seven axes | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Refund toy cost arithmetic | Original toy, computed | Lesson D1-patterns | Oct 6, 2026 |
| Agent tool selection as injection path | General principle | V2-D5.2 | Long-standing |

Minimal pairs:

- MP1. Base: invoice intake. 95% follow a fixed field map. Winner: workflow. Change: invoices arrive as free-form photos with unknown layouts. Winner flips to agent or hybrid. The fixed map no longer covers the input.
- MP2. Base: open supplier research. No fixed source list. Winner: agent. Change: the task narrows to one supplier site with a known page structure. Winner flips to workflow. Steps become listable.
- MP3. Base: hybrid refund triage. Winner: hybrid. Change: the regulator demands the identical step trace on every refund. Winner flips to workflow for all cases. The identical-trace demand kills runtime planning.

## Pair 2: single agent vs multi-agent

Shared: both use the Messages API tool loop. Both need one run id across hops (V2-D3.4). Both face the same cost per call.

Decisive difference: one loop versus a coordinator with a handoff contract. The contract names input schema, output schema, and the disagree rule (V2-D1.4). Multi-agent must justify itself: parallel specialist work with clean handoffs.

| Dimension | Single agent | Coordinator plus workers |
|---|---|---|
| Planning point | One loop | Coordinator plans, workers execute |
| Parallelism | Sequential tool calls | Parallel specialists |
| Handoff cost | None | Contract design, merge logic, checkpointing |
| Failure blast radius | The loop restarts | One worker retries, rest stands |
| Debugging | One trajectory | N trajectories plus merge |
| Best fit | Default (V2-D1.4) | Independent parallel pieces |

Winning constraints: multi-agent wins when pieces are independent, need different tools or expertise, and handoffs are clean. Single agent wins everywhere else, including mixed tasks where one loop handles them.

Losing constraints: single agent loses on wall-clock latency for independent parallel work. Multi-agent loses when workers disagree without a disagree rule, or when handoffs cost more than the parallel gain.

Costs: single agent cost equals steps times per-call price. Multi-agent adds coordinator overhead, duplicate context per worker, and merge calls. On the Lesson V2-D1.4 toy: three reviews sequential 48 s, parallel 24 s. Time halves. Calls roughly double. Pay time or pay calls, not neither.

Security: every worker is a new tool surface. Each gets least-privilege tools only (V2-D3.1, V2-D1.4 scoped workers). The coordinator needs no worker credentials. Audit must name the worker, not only the coordinator (V2-D3.2).

Operational burden: multi-agent needs the checkpoint at each handoff, trace propagation across workers, and a merge conflict rule. Single agent needs none of this. Complexity is a cost even when it works.

Counterexample: a code review agent that runs lint, tests, and security scan in sequence. The three checks touch the same repo state. A shared-directory race breaks parallel runs. Sequential single agent wins despite independence on paper.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Coordinator, handoff contract, disagree rule | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| 48 s versus 24 s toy | Original toy, computed | Lesson D1-patterns | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: legal, financial, technical review in one loop, 48 s. Change: reviews need different tools and run in parallel. Winner flips to multi-agent. Wall-clock time halves with no shared state.
- MP2. Base: three parallel workers merge cleanly. Change: the merge rule is ambiguous and two workers routinely disagree. Winner flips to single agent. The disagree cost exceeds the parallel gain.
- MP3. Base: single agent handles a task in 30 s. Change: a new 60 s SLA arrives and the task splits into four independent pieces. Winner flips to multi-agent. The SLA is the binding constraint, and only parallelism meets it.

## Pair 3: augmented LLM vs autonomous loop

Shared: both attach tools to a model call. Both live inside V2-D1.3. Both need structured-output validation (V2-D2.2) when output shape is a contract.

Decisive difference: the augmented call makes one judgment with tool results in context. The loop iterates: call, act, observe, repeat until done or the step cap hits. The spectrum question from Lesson D1-patterns decides: how much dynamic planning does the task need?

| Dimension | Augmented single call | Autonomous loop |
|---|---|---|
| Judgment count | One | Many, until done |
| Stop rule | None needed | Step cap, stop token, or goal check |
| Error cost per extra step | Zero extra steps | Each extra step can act |
| Reversibility demand | One review point | Review point per iteration |
| Best fit | One judgment plus tools | Open multi-step tasks |

Winning constraints: the augmented call wins on one-judgment tasks with tool context (V2-D1.3). The loop wins when the next step depends on the previous tool result and no code can precompute the sequence.

Losing constraints: the augmented call loses when one prompt cannot hold all tool results and the task needs follow-ups. The loop loses when a task is really one judgment: extra iterations burn cost and add drift risk.

Costs: augmented cost is one call plus tool costs. Loop cost is steps times per-call price. Cap the steps or the budget is unbounded.

Security: the loop multiplies the injection surface. Each iteration reads new tool output that can carry injected instructions (V2-D5.2 indirect injection). The augmented call has one observation round. Fewer rounds means fewer chances.

Operational burden: the loop needs the stop rule, per-iteration tracing, and loop-abort alerting. The augmented call needs none. A loop without a step cap is a pager incident waiting for its first loop.

Counterexample: a support agent that answers from a knowledge base. One retrieval plus one judgment fits the augmented call. It never needs a loop even though it is called an agent in marketing copy.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Augmented call as left spectrum stop | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Loop injection surface per iteration | General principle | V2-D5.2 | Long-standing |

Minimal pairs:

- MP1. Base: receipt check on one scanned image. One judgment, one tool. Winner: augmented call. Change: the receipt needs a database lookup, then a vendor lookup based on the result, then a policy check. Winner flips to loop. The step sequence is data-dependent.
- MP2. Base: multi-step research with unknown sources. Winner: loop. Change: the task narrows to one known FAQ document. Winner flips to augmented call. The plan becomes one retrieval plus one judgment.
- MP3. Base: a loop runs with a 10-step cap. Change: the cap drops to 1 by policy. Winner flips to augmented call. A one-step loop is an augmented call with extra machinery.

## Pair 4: sequential vs parallel execution

Shared: both execute the same subtasks. Both come from V2-D1.5 decomposition. Both need the same tools and permissions.

Decisive difference: sequential runs pieces in order and passes state forward. Parallel runs pieces at once and merges. Independence is the gate: shared state kills parallelism.

| Dimension | Sequential | Parallel |
|---|---|---|
| Wall clock | Sum of pieces | Max piece plus merge |
| State sharing | Natural, pass forward | Forbidden or fenced |
| Merge cost | None | Contract plus disagree rule |
| Partial failure | Stop or compensate | Retry the piece alone |
| Best fit | Dependent pieces | Independent pieces |

Winning constraints: parallel wins on independent pieces with a wall-clock bound. Sequential wins on dependent pieces, shared mutable state, or a merge rule that costs more than the time saved.

Losing constraints: parallel loses when pieces write the same state (race) or when the merge disagrees often. Sequential loses when the pieces are independent and the user waits.

Costs: parallel costs more calls (coordinator, per-worker context, merge). Sequential costs more time. On the Lesson V2-D1.4 toy: 48 s sequential, 24 s parallel. The 24 s gain costs roughly double the calls.

Security: parallel workers must not share credentials. One compromised worker must not poison another's state. Sequential has one active identity at a time, simpler to audit.

Operational burden: parallel needs the merge rule and per-piece traces. Sequential needs a compensate or retry point between pieces. Parallel incident response asks "which piece failed". Sequential asks "where did it stop".

Counterexample: three database migrations. Independent on paper, order-dependent in fact. Schema before index before backfill. Parallel runs corrupt the rollout. Sequential wins.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| 48 s versus 24 s, independence gate | Original toy, computed | Lesson D1-patterns | Oct 6, 2026 |

<figure class="fig">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="380" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Independence unlocks the clock</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Three reviews. Same work. One arrow names the rule.</text>
<rect x="24" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: SEQUENTIAL</text>
<rect x="44" y="144" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="172" y="165" font-size="13" text-anchor="middle" fill="#1B2838">legal 16 s</text>
<rect x="44" y="184" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="172" y="205" font-size="13" text-anchor="middle" fill="#1B2838">financial 16 s</text>
<rect x="44" y="224" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="172" y="245" font-size="13" text-anchor="middle" fill="#1B2838">technical 16 s</text>
<text x="44" y="276" font-size="14" fill="#1B2838">16 + 16 + 16 = 48 s</text>
<rect x="400" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: PARALLEL</text>
<rect x="420" y="144" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="460" y="165" font-size="11" text-anchor="middle" fill="#1B2838">legal</text>
<rect x="508" y="144" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="165" font-size="11" text-anchor="middle" fill="#1B2838">fin.</text>
<rect x="596" y="144" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="636" y="165" font-size="11" text-anchor="middle" fill="#1B2838">tech.</text>
<rect x="420" y="192" width="256" height="32" rx="8" fill="#E7F1F8"/>
<text x="548" y="213" font-size="13" text-anchor="middle" fill="#1B2838">merge 8 s</text>
<text x="420" y="256" font-size="14" fill="#1B2838">16 + 8 = 24 s. Calls about 2x.</text>
<defs><marker id="mc1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="194" x2="384" y2="194" stroke="#1B2838" stroke-width="2" marker-end="url(#mc1)"/>
<text x="360" y="178" font-size="13" text-anchor="middle" fill="#1B2838">pieces independent</text>
<text x="24" y="332" font-size="15" fill="#1B2838">Parallelism buys time with extra calls. Independence is the gate.</text>
</svg>
<figcaption>Shell 4. Independent pieces move from 48 s to 24 s at about double the calls. Source: original toy.</figcaption>
</figure>

Minimal pairs:

- MP1. Base: three reviews run in sequence, 48 s, no SLA. Winner: sequential. Change: a 30 s SLA arrives. Winner flips to parallel. The SLA binds and only the max-piece math meets it.
- MP2. Base: three parallel workers merge cleanly. Change: workers must all write one shared report file. Winner flips to sequential. Shared mutable state breaks the independence gate.
- MP3. Base: parallel pipeline with a merge rule. Change: merge disagreements rise to 40% and each needs human arbitration. Winner flips to sequential. The merge cost exceeds the 24 s gain.

## Pair 5: MCP vs direct API vs CLI

Shared: all three move data between the agent and a capability. All three cross the V2-D3.7 decision: reuse, security boundaries, ownership, operational complexity.

Decisive difference: MCP is a standard host-client-server protocol with declared tools and schemas. Direct API is bespoke HTTPS with your own schema. CLI is a subprocess that shells out and parses text.

| Dimension | Direct API or SDK | MCP | CLI wrapper |
|---|---|---|---|
| Reuse across hosts | Rewrite per host | One server, many hosts | Rewrite per host |
| Schema contract | Yours to design | Declared tools, typed | Text parse, brittle |
| Transport trust | Your TLS config | Host to server channel | Local process |
| Auth pattern | Your tokens | OAuth per V2-D3.2 | Inherits user shell |
| Ops cost | Low for one pair | Server lifecycle | Subprocess babysitting |
| Best fit | One consumer, one language | Many consumers or languages | Capability exists only as CLI |

Winning constraints: direct API wins on one consumer and one language (V2-D3.7). MCP wins when many hosts or languages share the capability. CLI wins only when the capability exists as a CLI and nowhere else.

Losing constraints: MCP loses on a single pair: protocol tax with no reuse gain. Direct API loses when three teams reimplement the same integration. CLI loses when output format changes break the parser.

Costs: MCP pays server development and hosting once, then near-zero per consumer. Direct API pays per-pair integration. CLI pays ongoing parser maintenance: every upstream format change is an incident.

Security: MCP needs the V2-D3.2 checklist: remote server over the network means OAuth is non-negotiable. Direct API keeps tokens in your code. CLI inherits the invoking user's permissions, which is the confused deputy risk when the agent runs with broader rights than the user.

Operational burden: MCP server needs versioning, uptime, and schema migration. Direct API needs per-client updates. CLI needs pinned versions and parse tests on every upstream release.

Counterexample: a vendor SDK that already covers your one language and one host. MCP adds a protocol layer with zero new consumers. Direct API wins even though MCP is the newer standard.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Five-option mechanism table | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Remote MCP server means OAuth | Current product guidance | Lesson D3-2 | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: one Python service calls one internal API. Winner: direct API. Change: three more teams in other languages need the same capability. Winner flips to MCP. Reuse crosses the threshold.
- MP2. Base: MCP server serves four hosts. Change: three hosts drop the feature, one remains. Winner flips to direct API. The reuse count no longer pays the protocol tax.
- MP3. Base: CLI wrapper around a vendor tool. Change: the vendor ships a stable typed API. Winner flips to direct API. The parse risk disappears and the contract becomes typed.

## Pair 6: shared tools vs independent agents

Shared: both scale beyond one loop. Both need the V2-D1.4 handoff discipline.

Decisive difference: shared tools keep one planning loop and widen its action set. Independent agents keep separate loops and coordinate through contracts.

| Dimension | One agent, shared tools | Independent agents |
|---|---|---|
| Planning loops | One | Many |
| Tool namespace | Shared, names must not collide | Per agent, isolated |
| Coordination cost | None | Contracts, merge, conflict rules |
| Context per decision | Grows with tool count | Small per agent |
| Failure mode | Wrong tool pick | Stale contract, disagreeing agents |
| Best fit | Tools serve one task | Agents serve different owners |

Winning constraints: shared tools win when one task needs many actions and one brain can pick among them. Independent agents win when tasks have different owners, different permissions, or conflicting goals.

Losing constraints: shared tools lose when tool descriptions overlap and the model picks wrong (V2-D3.1 overlapping descriptions). Independent agents lose when they must agree often: coordination cost exceeds specialization gain.

Costs: shared tools pay token cost per call for every schema in context (V2-D3.1 schema tokens). Independent agents pay per-agent context plus coordination calls. Past about 20 tools, progressive discovery (V2-D3.8) or splitting agents both beat a flat shared list.

Security: shared tools share one permission envelope. A dangerous tool sits next to a safe one in the same loop. Independent agents fence permissions per loop (V2-D1.4 scoped workers). Least privilege is easier per agent.

Operational burden: shared tools need name discipline and periodic pruning (V2-D3.1). Independent agents need contract versioning and ownership per agent. Both rot without an owner.

Counterexample: a dev assistant with 40 shared tools. Splitting into two agents halves each context, but the task routinely needs tools from both sides in one plan. Coordination calls erase the gain. Pruning and progressive discovery beat the split.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Scoped workers, per-agent tool lists | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Overlapping descriptions as bloat signal | General principle | V2-D3.1 | Long-standing |

Minimal pairs:

- MP1. Base: one assistant with 8 tools, one owner. Winner: shared tools. Change: the tool count grows to 40 with overlapping descriptions. Winner flips toward independent agents or discovery. The pick accuracy collapses under the flat list.
- MP2. Base: two agents own billing and support with clean contracts. Change: every ticket now needs both agents to agree before any reply. Winner flips to shared tools. Agreement on every case makes coordination the whole job.
- MP3. Base: shared tools with one permission envelope. Change: the billing tool needs write access that support must never hold. Winner flips to independent agents. One envelope cannot carry two trust levels.

:::takeaway
Every pair above turns on one gate: steps known, pieces independent, reuse real, permissions fenced. Name the gate in the exam stem and the winner follows.
:::
