# Comparisons 03: controls and security

Five high-confusion pairs from §18. Tight matrices. Prior-stage concepts appear by name only.

:::takeaway
Guidance shapes behavior. Only code stops tools. The exam asks what runs before the data reaches the model.
:::

## Pair 12: skills vs tools vs subagents

Shared: all three extend what the system can do. All three live under V2-D2.5 and V2-D7.1. All three need governance at team scale.

Decisive difference: a tool is one callable function with a schema. A skill is a governed reusable asset: named, versioned, reviewed procedures or prompt blocks shared across teams (V2-D2.5). A subagent is a separate loop with its own tool list and context (V2-D1.4, V2-D7.1 scoped subagents).

| Dimension | Tool | Skill | Subagent |
|---|---|---|---|
| Unit | One function call | Reusable procedure or prompt block | Separate agent loop |
| Context cost | Schema tokens per call | Shared block, versioned | Own context window |
| Permissions | Per-tool scope | Inherits the caller's scope | Own scoped tool list |
| Governance | Least-privilege review (V2-D3.1) | Name, version, review (V2-D2.5) | Contract, owner, disagree rule |
| Best fit | One action | Repeated procedure | Bounded subtask with own tools |

Winning constraints: tools win for single actions. Skills win for procedures repeated across teams. Subagents win for subtasks that need a different tool set or a separate context.

Losing constraints: a tool loses when the same 20-step procedure is pasted into five prompts: version drift follows. A skill loses when the procedure needs its own tools and context: it is a subagent wearing a skill's name. A subagent loses on a single action: loop overhead with no planning gain.

Costs: tools cost schema tokens and per-call price. Skills cost governance: review and versioning. Subagents cost a full loop: context plus coordination. The cheapest correct unit wins.

Security: tools get least-privilege scoping. Skills inherit the caller's envelope, so a skill used by two teams needs the narrower team's envelope. Subagents get fenced tool lists: the research subagent gets Read and Grep only and cannot write (V2-D7.1).

Operational burden: tools need pruning. Skills need version discipline: a silent edit is a silent production change. Subagents need owners and contracts. All three rot without an owner.

Counterexample: a team turns every tool into a subagent for "clean separation." Ten subagents coordinate to answer one question. Latency and cost triple. One loop with shared tools was the answer.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Skills as governed assets | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Scoped subagents, per-agent tool lists | General principle | Lesson D7-1 | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: one refund lookup action. Winner: tool. Change: five teams repeat the same 15-step refund procedure with pasted prompts. Winner flips to skill. Version drift across five copies is the binding cost.
- MP2. Base: a skill that runs a research procedure. Change: the procedure needs web search and file writes with different permissions than the caller. Winner flips to subagent. The procedure needs its own tool envelope.
- MP3. Base: a subagent handles document summarization. Change: the subtask shrinks to one extraction call with a fixed schema. Winner flips to tool. The loop adds cost with no planning to do.

## Pair 13: instructions vs enforceable permissions

Shared: both aim to control what the agent does. Both live in the Claude Code team config (V2-D7.1). Both appear in `.claude/settings.json`.

Decisive difference: instructions (CLAUDE.md, memory) shape the model's choices. Permissions (`allow`, `ask`, `deny` rules) and hooks decide without asking. The model reads instructions. Code enforces permissions.

| Dimension | Instructions | Enforceable permissions |
|---|---|---|
| Mechanism | Guidance text | Rules checked before the tool runs |
| Stops a tool | No: the model may comply | Yes: deny rules block |
| Failure mode | Ignored under pressure | Misconfigured rule |
| Audit value | Intent | Enforcement record |
| Best fit | Trusted team, no destructive tools | Secrets, destructive tools, teams |

Winning constraints: instructions win for style and workflow guidance on trusted teams. Permissions win wherever a security control is needed (V2-D7.1 decisive constraint: never CLAUDE.md alone for controls).

Losing constraints: instructions lose the moment a secret path or a destructive command exists. Permissions lose when they are so tight that developers route around them: the config must match the real workflow.

Costs: instructions cost writing time. Permissions cost design time: each deny rule needs a test that it fires and a path for legitimate work. A blocked legitimate workflow costs more than the rule saves.

Security: a deny rule for `Read(.env)` and `Bash(rm -rf:*)` is a lock. A CLAUDE.md note saying "do not read secrets" is a sign (Lesson 7-2A). The exam's favorite trap is a prompt doing a lock's job.

Operational burden: permissions need the shared file committed to the repo, personal overrides in `settings.local.json`, and org-managed policies for what must hold (V2-D7.1). Instructions need review for staleness.

Counterexample: a solo developer's scratch project with no secrets and no destructive tools. Permissions add config with nothing to protect. Guidance alone fits.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Permissions vs guidance in team config | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Deny rules, hooks, scoped subagents | General principle | Lesson D7-1 | Oct 6, 2026 |

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A sign stops nobody</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Team of 20. One secret read attempt each per week. 20 attempts.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: INSTRUCTION ONLY</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">CLAUDE.md: "do not read secrets"</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Model may comply. May not.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">Blocked: unknown. Audit: none.</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">A sign, not a lock.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: DENY RULE</text>
<rect x="420" y="144" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">deny: Read(.env)</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">Rule runs before the tool.</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">Blocked: 20 of 20. Audit: logged.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">A lock, with a record.</text>
<defs><marker id="mc3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mc3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">enforce in code</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The rule blocks all 20 attempts. The note blocks an unknown number.</text>
</svg>
<figcaption>Shell 3. A deny rule replaces guidance and blocks 20 of 20 secret reads with an audit record. Source: original toy.</figcaption>
</figure>

Minimal pairs:

- MP1. Base: solo dev, no secrets, no destructive tools. Winner: instructions. Change: the repo gains production credentials and a deploy script. Winner flips to enforceable permissions. A control is now needed.
- MP2. Base: deny rules block `Bash(sudo:*)` for the team. Change: the on-call workflow legitimately needs sudo for one restart script. Winner flips to allow-listed exception plus audit, not removal of the rule. The rule stands. The workflow gets a named path.
- MP3. Base: permissions block a legitimate daily workflow and developers bypass them with personal overrides. Winner flips to revised permissions that match the real workflow. Controls that the team routes around are theater.

## Pair 14: authentication vs authorization

Shared: both guard access. Both live under V2-D3.2. Both need audit.

Decisive difference: authentication answers who knocks: verify the token, signature, expiry, audience. Authorization answers which rooms open: this identity, this action, this resource, per policy. Enforcement is code before context. The model is none of the three (Lesson 7-2A).

| Dimension | Authentication | Authorization |
|---|---|---|
| Question | Who is this | What may they do |
| Check | Token validity | Policy decision |
| Failure mode | Impersonation | Excess privilege |
| User claim as proof | Never | Never: user role claims are not authZ |
| Best fit | Every hop | Every resource access |

Winning constraints: this pair is not either-or. The exam tests which one is absent. No authN means unknown callers. No authZ means known callers with unchecked power.

Losing constraints: authentication without authorization is a locked front door with open rooms. Authorization without authentication is a guest list with no ID check.

Costs: authN costs token issuance and verification per hop. AuthZ costs policy evaluation per access. Both are cheap next to a breach.

Security: the decisive rules from V2-D3.2: preserve source-system ACLs, no shared credentials when attribution matters, deterministic enforcement for side effects. A user saying "I am a manager" convinces the model and convinces no lock.

Operational burden: authN needs key rotation and expiry. AuthZ needs policy ownership and review. The confused deputy needs both: scope the tool's identity too, not only the user's.

Counterexample: a local stdio MCP server spawned by the user's own process. Inherit trust. OAuth adds nothing (V2-D3.2). A remote server over the network is the opposite: OAuth is non-negotiable.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| authN vs authZ, deterministic enforcement | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| 5,000 rows to 8 rows toy | Original toy, computed | Lesson 7-2A | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: support bot, agents see only their region. The design checks the agent's identity and filters rows. Change: the filter uses the agent's self-declared region from chat. The design now fails: a claim replaced the authZ check. Fix by checking identity against the HR policy table.
- MP2. Base: per-user delegation with token checks at each hop. Change: the deployment becomes a single-user local tool with no secrets. Both mechanisms drop out. The threat model no longer needs them.
- MP3. Base: shared service credential for a read-only internal dashboard. Change: the dashboard gains a "refund" button with money movement. The design must add per-user authN and deterministic authZ. Side effects changed the verdict.

## Pair 15: approval vs audit logging

Shared: both address accountability for agent actions. Both live under V2-D5.1 and V2-D5.3. Both need a named owner.

Decisive difference: approval gates the action before it happens: a human with real decision context says yes. Audit logging records the action after it happens: who, what, decision, timestamp. One prevents. The other explains.

| Dimension | Approval | Audit logging |
|---|---|---|
| Timing | Before the action | After the action |
| Stops harm | Yes, when the reviewer catches it | No: the harm already happened |
| Reviewer load | Per gated action | Near zero at write time |
| Evidence value | Decision record | Replay record |
| Best fit | Irreversible or costly actions | Everything, always |

Winning constraints: approval wins on irreversible, costly, or regulated actions (V2-D5.3: pre-action approval with full context). Audit wins everywhere as the baseline: log all tool calls regardless of gating.

Losing constraints: approval loses on high-volume low-stakes actions: reviewer fatigue turns the gate into a rubber stamp. Audit loses as the sole control on money movement: a perfect record of a theft is not prevention.

Costs: approval costs reviewer time per action and adds latency. Audit costs storage: on the Lesson 7-2A toy, 200 bytes per event times 1,000,000 calls per day = 200 MB per day = 6 GB per month.

Security: approval needs the reviewer to see the real decision context: the exact action, arguments, and consequences. A yes button without context is theater. Audit needs tamper protection: logs that the actor can edit are fiction.

Operational burden: approval needs the state machine: requested, approved, denied, expired, executed (see artifacts-02). Audit needs retention, search, and an owner who reads it.

Counterexample: a read-only research agent. Approval on every search would stall the work for zero safety gain. Audit logging alone fits: the actions are reversible and cheap.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Stakes-keyed review: pre-action, post-action, sampled | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Audit math 200 MB per day | Original toy, computed | Lesson 7-2A | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: agent drafts refunds, all reversible within 24 hours. Winner: audit logging plus post-action review. Change: refunds become instant and irreversible. Winner flips to pre-action approval. Reversibility was the gate.
- MP2. Base: pre-action approval on every database read. Change: volume hits 50,000 reads per day and reviewers rubber-stamp. Winner flips to sampled review plus audit. The gate degraded into theater.
- MP3. Base: audit-only on a deployment agent. Change: the regulator names human approval for production deploys. Winner flips to pre-action approval with a named reviewer and logged decision. The regulation is the binding constraint.

## Pair 16: removing capability vs monitoring capability

Shared: both respond to tool risk. Both live under V2-D3.1. Both need the capability inventory first.

Decisive difference: removal takes the tool out of the config. The model cannot call what it cannot see. Monitoring keeps the tool and watches its use. One shrinks the surface. The other watches the surface.

| Dimension | Removal | Monitoring |
|---|---|---|
| Attack surface | Smaller | Unchanged |
| Detection | Nothing to detect | Alerts on misuse |
| Cost | One config change | Ongoing alert triage |
| Failure mode | A needed tool is gone | Alert fatigue, missed signal |
| Exam rule | "Logging is not removal" | Monitoring never substitutes for removal |

Winning constraints: removal wins when the tool is unneeded, overlapping, or returns data the task never needs (V2-D3.1). Monitoring wins when the tool is needed but risky: watch the necessary risk, remove the unnecessary one.

Losing constraints: removal loses when the tool is actually needed: the team re-adds it under pressure with no review. Monitoring loses as the proposed fix for an unneeded dangerous tool: logging a delete-capable tool that no task needs is negligence with a dashboard.

Costs: removal costs near zero. Monitoring costs the alert pipeline and the humans who triage it. An un-triaged alert costs the full price of the incident it missed.

Security: removed tools cannot be picked by prompt injection. Monitored tools can. The V2-D3.1 exam rule is blunt: when the proposed fix is "logged for review," reject it as a substitute for removal.

Operational burden: removal needs the periodic bloat review. Monitoring needs alert ownership, thresholds, and a runbook per alert. Monitoring without an owner is a log nobody reads.

Counterexample: a production delete tool needed for the on-call workflow. Removal breaks incident response. Monitoring with approval gates fits: the capability is necessary, so it gets watched and gated.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Logging is not removal | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: agent has a delete tool it never uses. Proposal: log its calls. Winner flips to removal. The tool is unneeded and logging is not removal.
- MP2. Base: delete tool removed from the agent. Change: the on-call workflow needs it for incident response. Winner flips to a watched tool plus approval gates. The capability is necessary, so it gets watched, not deleted.
- MP3. Base: monitored write tool with alerting. Change: alerts fire weekly, nobody triages, one misuse ships. Winner flips to removal or pre-action approval. The monitoring proved itself decorative.

:::takeaway
Remove what is unneeded. Gate what is dangerous. Log everything. Never let one of the three pretend to be another.
:::
