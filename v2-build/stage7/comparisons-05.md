# Comparisons 05: operations and lifecycle

Five high-confusion pairs from §18. Tight matrices. Prior-stage concepts appear by name only.

:::takeaway
Production is a different product from the prototype. The gap has names: owners, evidence, gates, and a runbook.
:::

## Pair 22: logging vs tracing vs compliance evidence

Shared: all three record what happened. All three live under V2-D3.4 and V2-D4.6. All three need an owner.

Decisive difference: logging writes discrete events. Tracing links events across hops with one run id, so a run reconstructs end to end. Compliance evidence maps each requirement to a control, an owner, an artifact, and a cadence (V2-D5.4: requirement, control, owner, evidence, cadence).

| Dimension | Logging | Tracing | Compliance evidence |
|---|---|---|---|
| Unit | One event | One run across hops | One requirement chain |
| Answers | What happened here | What happened across the system | Prove the control works |
| Reconstructability | Per hop only | End to end with the run id | Per requirement, on demand |
| Audience | Engineers | Engineers on call | Auditors and regulators |
| Best fit | Always, the baseline | Multi-hop agent runs | Regulated data or actions |

Winning constraints: logging wins as the universal baseline. Tracing wins when runs cross hops: model, retrieval, tools, queues. Evidence wins when a regulator or customer asks for proof, not stories.

Losing constraints: logging alone loses on a multi-hop failure: per-hop events without a run id cannot reconstruct the run. Tracing alone loses the compliance ask: a trace is not a control mapping. Evidence alone loses the 2 a.m. incident: auditors' artifacts do not page.

Costs: logging costs storage (Lesson 7-2A toy: 200 MB per day per million calls). Tracing costs propagation discipline and a trace store. Evidence costs the mapping work and the review cadence.

Security: logs and traces carry the same sensitive data as the run. Redact before storage. Evidence artifacts need their own access control: the proof of the control is itself sensitive.

Operational burden: logging needs retention and search. Tracing needs the run id on every hop and clock discipline. Evidence needs the cadence: a mapping nobody re-checks rots.

Counterexample: a single-call classifier with no tools. Tracing adds nothing: one hop, one log line. Evidence adds nothing without a regulated requirement. Logging alone fits.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Trace model calls, retrieval, tools, queues | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Requirement to control to owner to evidence to cadence | General principle | V2-D5.4 | Long-standing |

Minimal pairs:

- MP1. Base: single model call, one log line per call. Change: the design grows to an agent with retrieval, three tools, and a queue. Winner flips to add tracing with one run id. Per-hop logs can no longer reconstruct a run.
- MP2. Base: full tracing on every run. Change: a healthcare customer asks for HIPAA evidence. Winner flips to add the compliance evidence mapping. Traces record. They do not prove controls.
- MP3. Base: compliance evidence pack for an audit. Change: a 2 a.m. outage needs the failing hop in minutes. The evidence pack loses. Tracing wins the incident. Each artifact serves its own audience.

## Pair 23: project defaults vs managed policies

Shared: both configure Claude Code for teams. Both live under V2-D7.1. Both aim at consistent, safe setups.

Decisive difference: project defaults are the committed `.claude/settings.json`: team permissions, hooks, and plugins that land on every clone. Managed policies are organization-level settings deployed by admins that override everything below them.

| Dimension | Project defaults | Managed policies |
|---|---|---|
| Scope | One repo | Whole organization |
| Owner | The team | Platform or security admin |
| Override | Personal `settings.local.json` | Nothing below overrides |
| Best fit | Team workflow: hooks, plugins, deny rules | Org non-negotiables: secret paths, spend caps |

Winning constraints: project defaults win for team workflow needs. Managed policies win for controls that must hold everywhere: deny rules on secret paths, model and spend guardrails.

Losing constraints: project defaults lose when a control must survive a malicious or careless team member: anyone with repo write access can edit the committed file. Managed policies lose for workflow preferences: org-wide hooks that fight a team's real workflow get routed around.

Costs: project defaults cost team design time. Managed policies cost admin design plus the exception process. An org policy with no exception path creates shadow workflows.

Security: managed settings are the enforcement layer for org policy. Project defaults are the enforcement layer for team policy. Guidance (CLAUDE.md) is neither layer (Pair 13).

Operational burden: project defaults need review like code. Managed policies need a change process, a rollout, and a break-glass story.

Counterexample: a two-person team with no secrets and no org. Managed policies are pure overhead. Project defaults alone fit.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Shared config, deny rules, hooks, managed settings | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: team commits `.claude/settings.json` with deny rules. Change: the org mandates secret-path deny rules that no team may weaken. Winner flips to managed policies for those rules. The committed file cannot protect against its own editors.
- MP2. Base: org-managed policy pins one model for all teams. Change: one team needs a cheaper model for a batch job and the policy has no exception path. The team routes around it. The fix is an exception process, not more enforcement.
- MP3. Base: managed policies cover secrets and spend. Change: a team wants a PostToolUse lint hook. Winner: project defaults. Workflow tooling belongs to the team, not the org.

## Pair 24: prototype success vs production readiness

Shared: both demonstrate the idea works. Both use the same model and tools. The prototype is the evidence that the idea is worth the production investment.

Decisive difference: the prototype proves the happy path on clean data. Production readiness proves the system on ugly data, at volume, with owners, evidence, and a runbook. The gap has names: the five eval drawers, the five watches, the ADR, the risk register, the runbook.

| Dimension | Prototype | Production-ready |
|---|---|---|
| Data | Clean, curated | Edge, adversarial, malformed |
| Score | Happy-path accuracy | Per-drawer scores plus floors |
| Volume | Tens of runs | Sustained load, tail latency |
| Ownership | The builder | Named owners per watch |
| Failure plan | "We will see" | Runbook, escalation, rollback |

Winning constraints: the prototype wins the funding decision: it answers "can this work." Production readiness wins the ship decision: it answers "will this hold."

Losing constraints: the prototype loses the moment real users arrive: clean-data scores do not transfer. Production hardening loses when applied before the idea is proven: hardening an idea that does not work is waste.

Costs: the prototype costs days. Readiness costs the eval set, the watches, the runbook, and the hardening loop. Skipping readiness does not save the cost. It moves it to incidents.

Security: the prototype often runs with broad permissions and real data in chat. Readiness demands the V2-D3.1 scoping, the V2-D3.2 authZ, and the V2-D5.1 gates. The prototype's shortcuts are the production incident list.

Operational burden: readiness needs the V2-D4.6 five watches with lines, windows, and owners, the regression suite on every change, and the V2-D7.3 runbook. The prototype needs none and that is fine until it ships.

Counterexample: a weekend demo for one stakeholder with no real data. Readiness is waste. The prototype is the deliverable.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Five watches, five drawers, regression on change | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Clean data flatters</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Same system. 50 clean cases versus 500 real cases across five drawers.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: PROTOTYPE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">48 / 50 = 96%</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Clean cases. Happy path.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">No edge drawer. No owner.</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Proves the idea.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: REAL CASES</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">350 / 500 = 70%</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">Edge and adversarial drawers.</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">Adversarial drawer: 12 / 100.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Names the readiness gap.</text>
<defs><marker id="mc5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mc5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">run the drawers</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The 96% proved the idea. The 70% prices the hardening.</text>
</svg>
<figcaption>Shell 4. Real-case drawers move the score from 96% to 70% and name the hardening work. Source: original toy.</figcaption>
</figure>

Minimal pairs:

- MP1. Base: prototype scores 96% on 50 clean cases. The team ships to users. Change: real traffic arrives with typos and attacks. The score drops to 70%. The fix is the readiness loop: drawers, watches, runbook. The prototype proved the idea, not the system.
- MP2. Base: full readiness hardening on an unproven idea. Change: the prototype test shows the model cannot do the core task at all. Winner flips to kill the project. Hardening a dead idea is waste.
- MP3. Base: production system with all watches green. Change: the eval drawers go stale and live quality slides. The watches stay green while users suffer. The fix is a drawer refresh (V2-D4.6). Green watches on a stale suite are theater.

## Pair 25: technical optimization vs business value

Shared: both improve the system. Both live under V2-D4.5 and V2-D1.6. Both need measurement.

Decisive difference: technical optimization improves a system metric: latency, tokens, cost per call. Business value improves an outcome: dollars saved, hours freed, errors avoided. The V2-D1.6 chain decides: baseline, improvement, cost, net value.

| Dimension | Technical optimization | Business value |
|---|---|---|
| Measures | p95 latency, tokens, cost | Net dollars, hours, error cost |
| Decides | What is faster or cheaper | What is worth doing |
| Blind spot | Faster at zero value | Value without feasibility |
| Best fit | After the value case is proven | Before any optimization |

Winning constraints: business value wins the priority decision: optimize what matters. Technical optimization wins the implementation: once the value case holds, make it fast and cheap.

Losing constraints: optimization without a value case is the fastest route to a system nobody needs. Value without optimization loses when the unit economics fail: a valuable task at $2 per call with a $0.05 budget is a prototype, not a product.

Costs: optimization costs engineering time. The V2-D4.5 rule: measure per stage, hold the quality and safety floors. An optimization that degrades quality below the floor is not an optimization.

Security: cost pressure tempts control removal: smaller models, fewer checks, cached authZ. The safety floor is not negotiable for savings (V2-D5.1).

Operational burden: optimization needs the per-stage measurement habit. Business value needs the baseline: measure the manual process first, then the automated one, then the net.

Counterexample: a latency optimization that cuts p95 from 9 s to 3 s on a batch job that runs overnight. No user waits. No value. The work was motion.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Baseline to improvement to cost to net value | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Ticket triage toy: $449 per week saved | Original toy, computed | Lesson 7-4A | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: team cuts tokens 40% on a triage bot. Change: the business asks for the net value. The 40% cut saves $12 per month on a bot that saves $23,348 per year in labor (Lesson 7-4A toy). The value case was already won. The optimization is garnish.
- MP2. Base: support bot with proven value at $0.50 per ticket. Change: volume grows 100x and unit cost breaks the budget. Winner flips to technical optimization: routing, caching, smaller models. The value case now depends on the unit economics.
- MP3. Base: optimization proposal: drop the grounding check to halve latency. The quality floor is 95% precision. The check holds the floor. The proposal loses. Floors outrank speed.

## Pair 26: implementation completion vs lifecycle ownership

Shared: both mark progress. Both live under V2-D6.5. Both need the handoff.

Decisive difference: implementation completion means the code is done and merged. Lifecycle ownership means someone owns each phase after: monitoring, iteration, incident response, and the decision to change or retire.

| Dimension | Implementation complete | Lifecycle owned |
|---|---|---|
| Done means | Code merged, tests pass | Owners named per phase |
| After ship | Nothing assigned | Watches, runbook, iteration loop |
| Failure response | Ad hoc | Runbook plus escalation |
| Drift response | None planned | Regression suite plus recalibration |
| Best fit | Never the finish line | The finish line |

Winning constraints: lifecycle ownership wins the ship decision. Implementation completion wins nothing on its own: it is a milestone, not a state.

Losing constraints: treating merge as done loses the first incident: no runbook, no owner, no rollback plan. Ownership without implementation is a meeting with no system.

Costs: ownership costs the on-call rotation, the watch tuning, and the iteration budget. Unowned systems pay in incidents instead.

Security: ownership includes the control review cadence: permissions re-checked, tokens rotated, audit logs read. Unowned controls rot.

Operational burden: the V2-D6.5 chain: discovery, design, handoff, monitoring, iteration. No phase substitutes for an unfinished earlier one. The handoff needs the ADR, the risk register, and the runbook (see artifacts-02).

Counterexample: a throwaway experiment with a fixed end date and no users. Implementation completion is the finish line. Ownership would be waste.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Lifecycle phases, no phase substitution | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: feature merged, tests green. The team moves on. Change: the first incident pages nobody. Winner flips to lifecycle ownership: runbook, escalation, named owner. Merge was a milestone, not done.
- MP2. Base: full ownership rituals on a prototype. Change: the prototype's end date passes with no users. The rituals were waste. Implementation completion was the right finish line.
- MP3. Base: owned system, model version pinned. Change: the provider deprecates the pinned version. The owner runs the regression suite and the upgrade as a production change (V2-D2.1). Ownership is what makes the forced change survivable.

:::takeaway
Ship the log, the trace, and the evidence. Commit the team config. Prove the idea, then earn production. Optimize the valuable. Own the lifecycle.
:::
