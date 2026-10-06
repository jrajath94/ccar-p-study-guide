# Lesson D3-1: tool capability bloat (V2-D3.1)

## 1. Problem this lesson solves

A support agent ships with 38 tools. Order read. Order cancel. Refund
issue. User delete. Payroll query. Email send. Two search tools with
near-identical descriptions. The task is order status.

The model must pick among all 38 on every call. It picks the wrong
search tool half the time. One day it picks user delete. The team says
the setup is safe because every call is logged. The log did not stop
the call. Logs record. Logs never prevent.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Logs record. Logs never prevent.</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">38 tools attached. The task needs 6. The log watched the damage.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">38 tools, all attached</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">every call logged</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Permission stays. Damage logged.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">6 tools, scoped to the task</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">32 tools removed</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">No permission. No damage to log.</text>
<defs><marker id="m311" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m311)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">cut and scope</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Removal revokes permission. Logging only watches it fire.</text>
</svg>
<figcaption>Shell 3. Thirty-two unneeded tools leave the config. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson 7-2A | Least privilege. Prompts are not locks. The model cannot unsee context |
| Lesson 7-3A | Tool calling mechanics. The model picks a tool by name and schema |
| Lesson D1-patterns | Extra calls cost tokens and time |

## 3. Mental model

Each tool is a door with a label. The model reads labels and picks
doors. Three costs ride on every door. The schema rides in context on
every call, so each door costs tokens. A wrong pick has consequences,
so each door is attack surface. Broad tools return broad data, so each
door leaks visibility.

Least privilege answers with the smallest set of doors the task needs.
Each door opens only the rooms the task needs. The rest leave the
config. A log camera on a door is not a lock on it.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Every door costs tokens</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The schema of each attached tool rides along on every model call.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">38 doors x 500 tokens</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">19,000 tokens per call.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Paid on every call.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Task needs 6 doors.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">6 doors x 500 tokens</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">3,000 tokens per call.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">19,000 - 3,000 = 16,000 saved.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">16,000 / 19,000 = 84% cut.</text>
<defs><marker id="m313" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m313)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">remove 32 doors</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Tools unused by the task still bill tokens on every call.</text>
</svg>
<figcaption>Shell 3. The schema load drops from 19,000 to 3,000 tokens per call. Source: original toy.</figcaption>
</figure>

:::takeaway
Attach the tools the task needs, scoped to the task. Remove the
rest. A log entry is not a permission boundary.
:::

## 4. Causal mechanism

Bloat breaks the system through three channels. Each channel has its
own fix. Removal fixes all three. Logging fixes none.

Channel one is selection confusion. The model picks tools by matching
descriptions to intent. Two overlapping descriptions split the match.
"search_orders: find orders" and "find_orders: look up orders" differ
in name only. The model flips between them. Worse, near-duplicates of
a dangerous tool invite a wrong pick with side effects. The fix is one
description per job, and distinct jobs get distinct names.

Channel two is data visibility. A tool result enters context. Lesson
7-2A proved the model cannot unsee context. A payroll query attached
"for managers" returns payroll rows into a support conversation. The
rows are now in the model's world. Scoping the tool's data access is
the fix. Telling the model to ignore rows is not.

Channel three is write scope. A tool with write access attached "for
later" can fire now. The model needs no malice. It needs a plausible
misread of intent. Refund issue with no cap fires a $50,000 refund.
The fix is narrow writes: caps, approval gates, or removal until the
task needs the write.

Why logging is not removal: the permission lives in the tool config.
The log lives downstream of the call. The audit reads the log after
the damage. The exam's exact trap phrase is "logged for review." A
logged unnecessary capability is still a granted capability.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Three channels, one fix</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Confusion, visibility, writes. Removal closes all three.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">overlap: 2 search tools</text>
<rect x="44" y="192" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="217" font-size="13" text-anchor="middle" fill="#1B2838">visibility: payroll in scope</text>
<rect x="44" y="240" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="265" font-size="13" text-anchor="middle" fill="#1B2838">write: refund, no cap</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">one search tool, one name</text>
<rect x="420" y="192" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="217" font-size="13" text-anchor="middle" fill="#1B2838">payroll removed</text>
<rect x="420" y="240" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="265" font-size="13" text-anchor="middle" fill="#1B2838">refund capped at $500</text>
<defs><marker id="m314" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m314)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">scope each door</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Distinct names end confusion. Narrow scope ends leaks. Caps end big mistakes.</text>
</svg>
<figcaption>Shell 4. Each channel gets its scoped fix. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: a customer support agent for order status. The team attached 25
tools. The list holds order read, order cancel, refund issue with no
cap, user delete, payroll query, email send, and two overlapping
search tools ("search_orders" and "find_orders"). 10,000 calls per day.
Each tool schema costs 500 tokens on every call.

Mini question: "The agent deleted a user record during a refund task.
The team proposes full logging of all tool calls as the fix. Which
option best addresses the incident? A) Keep all 25 tools and log every
call for review. B) Keep 5 scoped tools: order read, order cancel with
approval, refund capped at $500, one search tool, email send. Remove
the rest, merge the duplicate search. C) Keep all 25 tools but require
a second model to approve each call."

### The 10-step best-answer method in action

STEP 1: Identify what the question asks: best architecture, first action, next action, root cause, control, metric, or optimization.
STEP 2: Identify lifecycle stage: discovery, design, implementation, preproduction, operation, or incident response.
STEP 3: Extract the objective.
STEP 4: Extract hard constraints.
STEP 5: Identify the system layer.
STEP 6: Eliminate technically infeasible options.
STEP 7: Eliminate options violating hard constraints.
STEP 8: Compare remaining options against the objective.
STEP 9: Check hidden dependencies and consequences.
STEP 10: Verify the complete answer or multi-select combination.

Do not assume the exam always wants more autonomy, a larger model, more tools, more logging, a human reviewer everywhere, a new framework, or a complete redesign. Sometimes the best answer is: clarify the requirement, remove an unnecessary capability, fix retrieval, add a deterministic validation gate, narrow permissions, or preserve an existing sufficient workflow. The scenario, not a slogan, determines the answer.

| Step | Action on this question |
|---|---|
| STEP 1 | Question asks: control. Best fix for a wrong-tool incident |
| STEP 2 | Stage: incident response on a live agent |
| STEP 3 | Objective: stop wrong-tool damage, keep order status working |
| STEP 4 | Hard constraints: 10,000 calls per day, support task only, no user delete ever |
| STEP 5 | Layer: tool configuration, the agent's capability surface |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | A violates nothing stated, but it keeps user delete attached. B and C survive |
| STEP 8 | B removes the dangerous tool and the duplicates. A keeps the gun loaded. C adds a reviewer but keeps all 25 doors |
| STEP 9 | B's consequence: edge tasks that used removed tools need a new path. That is intended. A's consequence: the next misread deletes again. C's consequence: 10,000 extra model calls per day |
| STEP 10 | B alone answers the incident. C adds cost without removing risk. A answers audit, not safety |

Verdict: B. The arithmetic backs it: 25 tools x 500 tokens = 12,500
tokens per call. 5 tools = 2,500. At 10,000 calls per day the cut
saves 100,000,000 tokens per day of schema load. The scenario is a
wrong-tool incident, and the answer is remove the unnecessary
capability, not more logging.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The incident picks removal</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">25 tools, 10,000 calls per day. One wrong pick deleted a user.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">25 tools attached</text>
<rect x="44" y="192" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="217" font-size="13" text-anchor="middle" fill="#1B2838">12,500 tokens per call</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">user delete still loaded.</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Log watches. Nothing stops.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">5 scoped tools</text>
<rect x="420" y="192" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="217" font-size="13" text-anchor="middle" fill="#1B2838">2,500 tokens per call</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">user delete removed.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Refund capped at $500.</text>
<defs><marker id="m315" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m315)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">cut to the task</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A removed tool cannot fire. A logged tool still can.</text>
</svg>
<figcaption>Shell 4. The scoped set keeps the task and drops the risk. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Tool definitions with JSON Schema | Messages API tools array | V2-D3.1 capability surface |
| tools/list advertisement | MCP server capability | V2-D3.7 integration surface |
| Permission config per tool | Host application policy | V2-D3.1 least privilege, V2-D3.2 scoping |
| Approval gates on writes | Application layer | V2-D3.1 write scope |

## 7. Current limitations

Scoping cannot fix model misjudgment. A scoped tool can still fire at
the wrong moment. Coarse vendor tools force broad scope. The server
exposes "manage users" and the agent needs only "read users." Removing
a tool can break edge cases the team forgot. Overlapping descriptions
are a documentation failure first. Fix the names, then the config.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Scoped subset (this lesson) | Few tools, narrow scope | A defined task with real data |
| One flexible tool | One broad tool, approval gates | Unbounded query variety, one owner |
| Keep all, log all | Full surface, audit only | Local single-user dev tool, no secrets |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Tool can write or delete | Scope it, cap it, gate it, or remove it |
| Two tools overlap in description | Merge to one, rename for distinct jobs |
| Tool returns data the task never needs | Remove it or narrow its data scope |
| Token budget binds | Count schema tokens per call, cut the unused |
| "Logged for review" is the proposed fix | Reject: logging is not removal |

## 10. Valid-but-inferior option

Keep all 25 tools and log every call. Valid: the audit trail shows
exactly what fired, which helps forensics and compliance. Inferior
for this incident: the permission that caused the damage stays in the
config. The next misread deletes again, and the log records it
beautifully. On the toy, it also keeps paying 12,500 schema tokens per
call instead of 2,500.

## 11. Counterfactual where the alternative wins

A solo developer builds a local assistant on a laptop. No other
tenants. No production data. No secrets in reach. Speed of iteration
beats safety. Keep all tools, log everything, scope later. The
constraint set is different, so the winner changes.

| Situation | Winner | Why |
|---|---|---|
| Local single-user dev, no real data | Keep all, log all | Iteration speed beats safety. No blast radius |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Three costs of an attached tool: ______, ______, ______.
2. Two overlapping descriptions cause ______.
3. Logging a capability does / does not (pick) remove it.
4. 25 tools x 500 tokens = ______ tokens per call.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A research agent has 60 tools, including a database writer
with no row limit and three near-duplicate "summarize" tools.
The task is literature review. No writes are ever needed.
Name the three removals and the one rename.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Least privilege, model cannot unsee, prompts are not locks | General principle, official exam scope via secondary summaries | Lesson 7-2A, S03, S04 | Sept 2026 |
| Tool schema rides in context on each call | Current product behavior | Messages API tool use, secondary | Oct 6, 2026 |
| Toy arithmetic: tokens per call, daily totals | Original toy, computed above | This lesson | Oct 6, 2026 |
| "Logging is not removal" as exam trap | Official exam scope via secondary summaries | Blueprint ledger V2-D3.1 | Sept 2026 |
| MCP tools/list advertisement | Spec concept, corroborated by independent sources | Web search, Sept 2026 | Oct 6, 2026 |

:::takeaway
The exam's favorite D3.1 trap is "more logging" as the safety fix.
Ask: does the option remove a permission or only watch it? Pick
removal when the scenario names an unnecessary capability.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Logs never prevent | 38 tools, all logged | 6 tools, 32 removed | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | 7-2A, 7-3A, D1-patterns |
| u03 | Every door costs tokens | 38 x 500 = 19,000 | 6 x 500 = 3,000, 84% cut | f03 | SVG | Original |
| u04 | Three channels, one fix | Overlap, visibility, writes | Scoped fixes per channel | f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B: remove and scope | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Scoping limits stated | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Keep-and-log is valid but inferior | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Local dev favors keep-all | -- | Counterfactual table | f11 | Table | Original |
| u12 | Three costs from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to research agent | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
