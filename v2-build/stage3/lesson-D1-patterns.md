# Lesson D1-patterns: orchestration patterns (V2-D1.3, V2-D1.4, V2-D1.5)

Three objectives, one theme: how work gets organized. V2-D1.3 picks the
pattern. V2-D1.4 organizes multiple agents. V2-D1.5 splits work into
pieces. Each objective below carries its own problem, model, mechanism,
worked example with the 10-step method, constraints, and transfer
question. Mapping, limitations, alternatives, and evidence are shared at
the end.

:::takeaway
The scenario picks the pattern. Fixed steps go deterministic. Open
tasks go agentic. Mixed tasks go hybrid. Multiple agents earn their
keep only on parallel specialist work with clean handoffs.
:::

## Objective V2-D1.3: select the architectural pattern

### 1. Problem this objective solves

A team hears "agent" and builds an agent loop for a fixed refund task.
The loop makes four model calls per refund, picks different steps each
run, and costs eight times the workflow that would have done. The
pattern was chosen by fashion, not by the task.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Fashion picks the pattern</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fixed task. Agent loop. Four calls where one would do.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F4E6D4"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">agent loop, 4 calls</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Steps differ each run.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Cost: 4x per refund.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="8" fill="#E7F1F8"/>
<text x="480" y="173" font-size="13" text-anchor="middle" fill="#1B2838">workflow</text>
<rect x="556" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="616" y="173" font-size="13" text-anchor="middle" fill="#1B2838">plus call</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Same steps each run.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Cost: 1x per refund.</text>
<defs><marker id="m-p13-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p13-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">match the task</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The task shape picks the pattern. Fashion does not.</text>
</svg>
<figcaption>Shell 3. An agent loop on a fixed task becomes a workflow. Source: original toy.</figcaption>
</figure>

### 2. Prerequisites

Lesson D1-1 gives the fork: fixed mapping goes deterministic, open
input goes to Claude. Lesson 7-1A gives the cost fact: each model call
spends tokens and seconds.

| Foundation | What it gives this objective |
|---|---|
| V2-D1.1 fork | The lane question comes first |
| §7.1, §7.3 | Calls cost tokens, time, and attention |

### 3. Mental model

Think of a spectrum, not a menu. Far left: augmented single call, one
judgment plus tools. Next: deterministic workflow, fixed steps in code.
Next: hybrid, workflow bones with model joints. Far right: agentic,
the model plans the steps. Position on the spectrum comes from one
question: how much dynamic planning does the task need? None goes
left. Unknown steps go right. The seven axes score the pick:
predictability, reversibility, error cost, latency, cost,
observability, and dynamic-planning need.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One spectrum, four stops</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Dynamic-planning need moves the marker right.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F4E6D4"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">agentic, always</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No spectrum.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No axes.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">One stop for all tasks.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="60" height="36" rx="8" fill="#E7F1F8"/>
<text x="450" y="171" font-size="11" text-anchor="middle" fill="#1B2838">call</text>
<rect x="488" y="148" width="60" height="36" rx="8" fill="#E7F1F8"/>
<text x="518" y="171" font-size="11" text-anchor="middle" fill="#1B2838">flow</text>
<rect x="556" y="148" width="60" height="36" rx="8" fill="#E7F4EF"/>
<text x="586" y="171" font-size="11" text-anchor="middle" fill="#1B2838">hybrid</text>
<rect x="624" y="148" width="60" height="36" rx="8" fill="#F4E6D4"/>
<text x="654" y="171" font-size="11" text-anchor="middle" fill="#1B2838">agent</text>
<text x="420" y="224" font-size="13" fill="#5C6B7A">Left: no planning needed.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Right: steps unknown.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Seven axes score the stop.</text>
<defs><marker id="m-p13-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p13-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">place the marker</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Less planning need sits left. Unknown steps sit right.</text>
</svg>
<figcaption>Shell 3. One agentic stop becomes a four-stop spectrum. Source: original toy.</figcaption>
</figure>

### 4. Causal mechanism

Each pattern trades control for flexibility. The augmented call keeps
full control: one prompt, tools attached, no loop. The workflow keeps
the steps in code and calls the model only at the joints. The hybrid
lets the model choose among fixed branches. The agent lets the model
plan. Score each candidate on the seven axes. High error cost and low
reversibility push left, toward determinism. Unknown steps push right,
toward the agent. Cost and latency punish extra calls. Observability
punishes loops that hide their plan. The pattern with the best score
on the task's binding axes wins.

### 5. Minimal worked example

Toy: refund triage. 20,000 refunds per day. 70% follow fixed rules.
25% need one judgment call on a receipt. 5% need open investigation.

Costs on the Balanced tier ($2 in, $10 out per 1M, S10-S12, Oct 2026).
Deterministic rule check: $0.0001 per case (toy). Augmented call:
1,500 in, 300 out. In: 1,500 / 1,000,000 x $2 = $0.003. Out: 300 /
1,000,000 x $10 = $0.003. Total $0.006 per case. Agentic: 4 calls on
average = $0.024 per case.

Hybrid: 0.70 x $0.0001 + 0.25 x $0.006 + 0.05 x $0.024 = $0.00007 +
$0.0015 + $0.0012 = $0.00277 per refund. Per day: 20,000 x $0.00277 =
$55.40. All agentic: 20,000 x $0.024 = $480 per day. The hybrid costs
8.7x less and keeps fixed steps fixed.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The spectrum prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Balanced tier. 20,000 refunds a day. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">all agentic: $480 / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">$0.024 x 20,000 = $480.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Fixed steps sampled daily.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No axes scored.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">hybrid: $55.40 / day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">0.70 x 0.0001 + 0.25 x 0.006</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">+ 0.05 x 0.024 = $0.00277</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">20,000 x $0.00277 = $55.40</text>
<defs><marker id="m-p13-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p13-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">score the axes</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The hybrid costs 8.7x less and keeps fixed steps fixed.</text>
</svg>
<figcaption>Shell 4. Axis scoring turns $480 per day into $55.40 per day. Source: original toy.</figcaption>
</figure>

#### The 10-step best-answer method in action

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

Mini question: "A returns desk processes refunds. 80% follow fixed rules. 20% need judgment on scanned receipts. Error cost is high. Which pattern fits? A) One agent handles every refund end to end. B) Deterministic workflow for the fixed 80%, augmented call for the 20%, code gate on every payout. C) Augmented single call for all refunds."

| Step | Action on this question |
|---|---|
| STEP 1 | Best architecture for the refund task |
| STEP 2 | Design stage |
| STEP 3 | Cheap, correct refunds |
| STEP 4 | High error cost. 80/20 split. Every payout needs a gate |
| STEP 5 | Application layer: orchestration pattern |
| STEP 6 | All three are technically feasible |
| STEP 7 | A names no gate on payouts: violates the error-cost constraint. C pays model price for fixed rules and names no gate |
| STEP 8 | B matches the 80/20 split and the gate |
| STEP 9 | B needs the rule set and the receipt check maintained. Both are owned |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive constraints are the 80/20 split and the payout gate, and only B serves both.

### 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Steps fixed and known | Deterministic workflow |
| One judgment plus tools | Augmented single call |
| Steps unknown, task open | Agentic |
| Mixed: fixed bones, open joints | Hybrid |
| High error cost, low reversibility | Push left on the spectrum |

### 10. Valid-but-inferior option

One agent for everything. Valid: it handles every case, including the
open 5%. Inferior: on the toy it costs $480 per day against $55.40. Its
steps vary run to run on fixed cases. Traces show a plan the team
never wrote.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Agent for all | Handles the open 5% | $480 vs $55.40 per day. Unstable on fixed cases |

### 11. Counterfactual where the alternative wins

Open-ended research: "find everything about this supplier." Steps are
unknown until the search runs. No workflow can list them in advance.
The agent wins: dynamic planning is the task.

| Situation | Winner | Why |
|---|---|---|
| Steps unknown until runtime | Agentic | Planning is the task, not overhead |

### 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The four stops: augmented call, deterministic
   workflow, ______, agentic.
2. The spectrum question: how much ______ does
   the task need?
3. High error cost pushes ______ on the spectrum.
4. The hybrid toy costs $______ per day.
Uncover. Fix misses. Repeat once.
```

### 13. Unseen transfer question

```
A warehouse handles returns. 90% are unopened boxes with a
barcode. 10% are damaged goods needing a judgment call.
A wrong refund costs the margin on the item.
Name the pattern for each group. Name the gate.
Do not answer yet. The key ships in Stage 8.
```

## Objective V2-D1.4: design multi-agent orchestration

### 1. Problem this objective solves

One agent does legal, financial, and technical review in sequence. The
three reviews are independent, but the agent runs them one after
another: 48 seconds. Three specialists could run them in parallel: 24
seconds. The single agent is not wrong. It is slow on work that splits.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Sequential on splittable work</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Three independent reviews. One agent. Twice the wait.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">one agent, 6 rounds, 48 s</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Reviews wait on each other.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">No reason. They are independent.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="40" rx="999" fill="#F4E6D4"/>
<text x="460" y="173" font-size="12" text-anchor="middle" fill="#1B2838">coord</text>
<rect x="508" y="148" width="56" height="40" rx="8" fill="#E7F4EF"/>
<text x="536" y="173" font-size="12" text-anchor="middle" fill="#1B2838">L</text>
<rect x="568" y="148" width="56" height="40" rx="8" fill="#E7F4EF"/>
<text x="596" y="173" font-size="12" text-anchor="middle" fill="#1B2838">F</text>
<rect x="628" y="148" width="56" height="40" rx="8" fill="#E7F4EF"/>
<text x="656" y="173" font-size="12" text-anchor="middle" fill="#1B2838">T</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Parallel: 16 s plus merge 8 s.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Total 24 s.</text>
<defs><marker id="m-p14-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p14-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">split the work</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Independent work runs in parallel. The merge is the only serial step.</text>
</svg>
<figcaption>Shell 3. One sequential agent becomes a coordinator with three workers. Source: original toy.</figcaption>
</figure>

### 2. Prerequisites

Objective V2-D1.3 gives the spectrum: the agent is the rightmost stop.
Lesson 7-1A gives traces: one run id across every hop.

| Foundation | What it gives this objective |
|---|---|
| V2-D1.3 spectrum | Multi-agent is a choice, not a default |
| §7.1 systems | One trace id across coordinator and workers |

### 3. Mental model

Think of a coordinator with a contract, not a crowd of agents. The
coordinator splits the task, hands each worker a bounded piece, and
merges the results. The handoff contract names three things: the input
schema, the output schema, and the disagree rule. Checkpointing saves
each handoff, so a failed worker resumes without redoing the rest.
Traces carry one run id from coordinator to worker to merge. The
default stays single agent plus tools. Multi-agent must justify
itself: parallel specialist work with clean handoffs.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The contract holds the crowd</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Three handoffs. Each names input, output, and the disagree rule.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">workers chat freely</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No input schema.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No disagree rule.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Merge is a hope.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#F4E6D4"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">coordinator</text>
<rect x="420" y="196" width="80" height="40" rx="8" fill="#E7F4EF"/>
<text x="460" y="221" font-size="12" text-anchor="middle" fill="#1B2838">legal</text>
<rect x="508" y="196" width="80" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="221" font-size="12" text-anchor="middle" fill="#1B2838">finance</text>
<rect x="596" y="196" width="80" height="40" rx="8" fill="#E7F4EF"/>
<text x="636" y="221" font-size="12" text-anchor="middle" fill="#1B2838">tech</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Handoff: in, out, disagree rule.</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Checkpoint each handoff.</text>
<defs><marker id="m-p14-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p14-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">write contracts</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Contracts turn a crowd into a team. No contract, no merge.</text>
</svg>
<figcaption>Shell 3. Free chat becomes contracted handoffs with checkpoints. Source: original toy.</figcaption>
</figure>

### 4. Causal mechanism

The run opens with the coordinator: it splits the task along clean
seams and writes a contract per worker. Workers run in parallel, each
with a bounded context: its slice plus the contract, not the whole
world. Each handoff checkpoints: inputs, outputs, and the worker's
trace under one run id. Disagreement has a rule, decided in advance:
majority vote, specialist priority, or escalate to the coordinator.
The merge is a deterministic step where possible: assemble sections,
dedupe, run the totals check. The coordinator owns retries: a failed
worker reruns from its checkpoint, not from zero.

### 5. Minimal worked example

Toy: due-diligence review. Three independent reviews: legal, finance,
technical. Each needs 2 model rounds at 8 seconds each.

Single agent: 6 rounds in sequence = 48 seconds. Tokens: 6 x (2,000
in, 500 out) = 12,000 in, 3,000 out. Balanced tier ($2 in, $10 out
per 1M, S10-S12, Oct 2026): in 12,000 / 1,000,000 x $2 = $0.024. Out
3,000 / 1,000,000 x $10 = $0.03. Total $0.054 per review.

Multi-agent: 3 workers x 2 rounds in parallel = 16 seconds, plus
coordinator merge 8 seconds = 24 seconds. Tokens: workers 12,000 in,
3,000 out, plus coordinator 3,000 in, 1,000 out = 15,000 in, 4,000
out. In: 15,000 / 1,000,000 x $2 = $0.03. Out: 4,000 / 1,000,000 x $10
= $0.04. Total $0.07 per review. Latency halves. Cost rises 30%.
Multi-agent wins only when the latency is worth the premium.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Half the wait, 30% more cost</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Balanced tier. Latency halves. Cost rises. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">one agent: 48 s, $0.054</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">6 rounds x 8 s = 48 s.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">12,000 in, 3,000 out.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">$0.024 + $0.03 = $0.054.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">team: 24 s, $0.07</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">16 s parallel + 8 s merge.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">15,000 in, 4,000 out.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">$0.03 + $0.04 = $0.07.</text>
<defs><marker id="m-p14-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p14-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">parallelize</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Parallelism buys latency at a 30% premium. Buy it only when late costs more.</text>
</svg>
<figcaption>Shell 4. Parallel workers trade a 30% premium for half the latency. Source: original toy.</figcaption>
</figure>

#### The 10-step best-answer method in action

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

Mini question: "A due-diligence task needs legal, financial, and technical review of one target. The reviews are independent. The report must ship in one hour. Which design fits? A) One agent with all tools does the three reviews in sequence. B) Coordinator splits to three specialist workers in parallel with handoff contracts, then merges. C) Three separate agents with no coordinator, each sends its section by email."

| Step | Action on this question |
|---|---|
| STEP 1 | Best architecture for the review task |
| STEP 2 | Design stage |
| STEP 3 | Complete, coherent review in one hour |
| STEP 4 | Reviews are independent. One-hour deadline. One coherent report |
| STEP 5 | Application layer: orchestration |
| STEP 6 | All three are technically feasible |
| STEP 7 | C violates coherence: no merge, no contract, no single report |
| STEP 8 | B beats A on the deadline: parallel independent work halves latency |
| STEP 9 | B needs handoff contracts and a merge step. Checkpointing covers worker failure |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive constraints are independence plus the deadline, and only B parallelizes with contracts.

### 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Work splits into independent specialist tracks | Multi-agent with contracts |
| One entangled task, shared evolving context | Single agent plus tools |
| Latency deadline on parallelizable work | Multi-agent |
| Handoffs unclear or constantly shifting | Single agent. Contracts would rot |

### 10. Valid-but-inferior option

Single agent with all tools for the review task. Valid: simpler, no
contracts to write, 30% cheaper on the toy. Inferior: sequential
latency on parallelizable work, 48 seconds against 24, and one long
context holding three reviews dilutes focus.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Single agent plus tools | Simpler, cheaper, no contracts | 48 s vs 24 s. Focus dilutes across reviews |

### 11. Counterfactual where the alternative wins

One negotiation with a supplier. Each round depends on the last.
Splitting it across workers shreds the shared context, and handoffs
would carry the whole history anyway. The single agent wins: the work
is entangled, not parallel.

| Situation | Winner | Why |
|---|---|---|
| Entangled task, shared evolving context | Single agent | Splitting shreds the context handoffs must carry |

### 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The default is single agent plus ______.
2. A handoff contract names input, output, and
   the ______ rule.
3. ______ saves each handoff for resume.
4. The team toy: 24 s vs 48 s, cost up ______%.
Uncover. Fix misses. Repeat once.
```

### 13. Unseen transfer question

```
A product launch needs copy, visuals brief, and pricing
analysis. The three tracks are independent. Launch is in
six hours. Two reviewers disagree on the pricing.
Name the pattern. Name the disagree rule.
Do not answer yet. The key ships in Stage 8.
```

## Objective V2-D1.5: apply decomposition

### 1. Problem this objective solves

One giant call writes a 20-page report from 12 department updates. The
middle updates get lost: attention dilutes. One bad section fails the
whole call: no partial retry. The task is splittable, but nobody split
it.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One call, twelve updates</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The middle gets lost. One bad section fails all.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">one call, 12 updates</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Middle updates dilute.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">One failure kills all.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="40" rx="8" fill="#E7F4EF"/>
<text x="460" y="173" font-size="12" text-anchor="middle" fill="#1B2838">split</text>
<rect x="508" y="148" width="80" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="12" text-anchor="middle" fill="#1B2838">extract</text>
<rect x="596" y="148" width="80" height="40" rx="8" fill="#E7F1F8"/>
<text x="636" y="173" font-size="12" text-anchor="middle" fill="#1B2838">merge</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Each update gets full focus.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">One failure retries alone.</text>
<defs><marker id="m-p15-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p15-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">split on seams</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Split where the work splits. Merge where the answer joins.</text>
</svg>
<figcaption>Shell 3. One giant call becomes split, extract, merge. Source: original toy.</figcaption>
</figure>

### 2. Prerequisites

Lesson 7-3A gives dilution: a full window does not mean full
attention. Objective V2-D1.3 gives the spectrum: decomposition serves
whichever pattern wins.

| Foundation | What it gives this objective |
|---|---|
| §7.3 dilution | Split for focus, not just for fit |
| V2-D1.3 spectrum | Decomposition is pattern-agnostic |

### 3. Mental model

Think of five moves, not one. Route: send the task to the right lane.
Chain: A feeds B in order. Fan-out and fan-in: split independent work,
then merge. Critique: a second pass reviews the first. Validation: a
deterministic gate checks the result. Two splits guide the choice.
First, the deterministic and probabilistic split: code does the
certain parts, the model does the judgment parts. Second, the
independence split: parallelizable work fans out, ordered work chains.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five moves, two splits</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Route, chain, fan-out, critique, validation. Pick by the split.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">one move: giant call</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No route. No chain.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No critique. No gate.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">One failure kills all.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="460" y="171" font-size="12" text-anchor="middle" fill="#1B2838">route</text>
<rect x="508" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">chain</text>
<rect x="596" y="148" width="80" height="36" rx="999" fill="#E7F4EF"/>
<text x="636" y="171" font-size="12" text-anchor="middle" fill="#1B2838">fan</text>
<rect x="464" y="192" width="80" height="36" rx="999" fill="#F6E7A8"/>
<text x="504" y="215" font-size="12" text-anchor="middle" fill="#1B2838">critique</text>
<rect x="552" y="192" width="80" height="36" rx="999" fill="#E7F4EF"/>
<text x="592" y="215" font-size="12" text-anchor="middle" fill="#1B2838">validate</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Code takes the certain parts.</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Model takes the judgment parts.</text>
<defs><marker id="m-p15-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p15-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">learn the moves</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Five moves cover most splits. Name the move before you build it.</text>
</svg>
<figcaption>Shell 3. One giant call becomes five named moves. Source: original toy.</figcaption>
</figure>

### 4. Causal mechanism

Decomposition works because each piece gets a bounded task: its own
input contract, its own size cap, its own retry. Bounded pieces fail
alone and retry alone. The deterministic and probabilistic split puts
certain work in code: totals, formats, schema checks. The model gets
only the judgment parts. Fan-out wins when pieces are independent and
each needs full attention: five sections, five calls, one merge.
Chaining wins when order matters: each step's output is the next
step's input. Critique wins when a quality bar must be met and a
second pass is cheaper than a failure. Validation closes every
decomposition: a deterministic gate checks the merged result.

### 5. Minimal worked example

Toy: quarterly report from 12 department updates. Fan-out: one call per
update extracts key numbers with citations. Fan-in: one call merges,
then code checks the totals.

Tokens per extraction: 3,000 in, 800 out. Twelve extractions: 36,000
in, 9,600 out. Fan-in: 12,000 in (cited numbers), 1,500 out. Totals:
48,000 in, 11,100 out. Balanced tier ($2 in, $10 out per 1M, S10-S12,
Oct 2026): in 48,000 / 1,000,000 x $2 = $0.096. Out 11,100 /
1,000,000 x $10 = $0.111. Total $0.207 per report.

Single giant call: 36,000 in, 9,600 out = $0.072 + $0.096 = $0.168.
Cheaper by $0.039, but the middle updates dilute and no citation
traces a number to its update. The decomposition buys traceability and
focus for four cents.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Four cents buys the trace</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Balanced tier. 12 updates. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">one call: $0.168</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">36,000 in, 9,600 out.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Middle updates dilute.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No number traces to a source.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">fan-out: $0.207</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">48,000 in = $0.096.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">11,100 out = $0.111.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Every number cites its update.</text>
<defs><marker id="m-p15-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-p15-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">split and cite</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Four cents buys focus and a trace for every number.</text>
</svg>
<figcaption>Shell 4. Fan-out trades $0.039 for focus and traceability. Source: original toy.</figcaption>
</figure>

#### The 10-step best-answer method in action

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

Mini question: "A team builds a quarterly report from 12 department updates. Each update is independent. A wrong number costs credibility. Which decomposition fits? A) One call reads all 12 updates and writes the report. B) Fan-out: one call per update extracts key numbers with citations. Fan-in merges, then code checks the totals. C) Chain: 12 sequential calls, each appending to a running draft."

| Step | Action on this question |
|---|---|
| STEP 1 | Best architecture for the report |
| STEP 2 | Design stage |
| STEP 3 | Accurate, traceable report |
| STEP 4 | Updates are independent. Every number must trace to its source |
| STEP 5 | Application layer: decomposition |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates traceability: no citation per number. C violates it too: the running draft unattributed numbers |
| STEP 8 | B matches: citations per number, deterministic totals check |
| STEP 9 | B needs the citation format contract and the totals check in code |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive constraints are independence plus traceability, and only B gives every number a source.

### 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Pieces independent, each needs focus | Fan-out and fan-in |
| Order matters, output feeds input | Chain |
| Quality bar, second pass cheaper than failure | Critique |
| Certain sub-tasks inside the work | Deterministic split: code does them |
| Every result must be checked | Validation gate on the merge |

### 10. Valid-but-inferior option

Chain everything in order. Valid: simple to reason about, one failure
points at one step. Inferior: on the toy, 12 sequential calls sum
their latencies, and each step rewrites the draft so errors compound
instead of staying local.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Chain all 12 | Simple order, clear failures | Latency sums. Errors compound across steps |

### 11. Counterfactual where the alternative wins

One paragraph summary of one page. The task is tiny, bounded, and
single-focus. Decomposition adds eleven extra calls, a merge step, and
contracts for nothing. The single call wins: the overhead exceeds the
task.

| Situation | Winner | Why |
|---|---|---|
| Tiny bounded single-focus task | Single call | Decomposition overhead exceeds the task |

### 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The five moves: route, chain, fan-out and
   fan-in, ______, validation.
2. Code takes the ______ parts. The model takes
   the ______ parts.
3. Fan-out wins when pieces are ______.
4. The report toy: $0.207 vs $______.
Uncover. Fix misses. Repeat once.
```

### 13. Unseen transfer question

```
A newsroom summarizes 30 local council meetings into one
briefing. Each meeting is independent. A misattributed quote
costs trust. The briefing must ship by 6 a.m.
Name the decomposition. Name the check.
Do not answer yet. The key ships in Stage 8.
```

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Augmented call with tools | Messages API tool loop | V2-D1.3 pattern choice |
| Workflow orchestration | Application code, queues | V2-D1.3, V2-D1.5 chaining |
| Coordinator and worker roles | Scoped subagents | V2-D1.4 multi-agent |
| Handoff contracts | Task schema, validation | V2-D1.4 contracts, V2-D6.4 ADRs |
| Trace propagation | One run id across hops | V2-D3.4 observability |
| MCP tool servers | Tool boundary | V2-D3.7 integration |

## 7. Current limitations

Decomposition adds joints, and joints fail. The merge is a new failure
point: five good sections can still merge badly. Handoff contracts rot
when the task shifts: a contract written for one report format breaks
on the next. Partial failure needs a policy: retry the piece, skip it
with a flag, or fail the whole run. Checkpointing costs storage and
code. And the coordinator can become the bottleneck it was built to
remove: too many workers, one slow merge.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Joints can fail</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Five good sections. One bad merge. Name the policy.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">5 sections done</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Merge fails.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">No policy. Start over.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">merge fails, sections kept</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Checkpoints hold the sections.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Retry the merge alone.</text>
<defs><marker id="m-pxx-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-pxx-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">checkpoint the joints</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Checkpoint every joint. Retry the failed piece, not the whole run.</text>
</svg>
<figcaption>Shell 3. Checkpoints turn a failed merge into a retried merge. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Single call | No split | Tiny bounded task, one focus |
| Agentic loop | Model plans steps | Steps unknown until runtime |
| Decomposed pipeline (this lesson) | Named moves with contracts | Splittable work, traceability needs |

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D1.3 tests pattern selection on seven axes | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| V2-D1.4 tests multi-agent: roles, handoffs, checkpointing, justification | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| V2-D1.5 tests decomposition moves and splits | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Tier prices $2/$10 in/out per 1M (Balanced) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy refund, review, and report arithmetic | Original toys, computed above | This lesson | Oct 6, 2026 |
| Five decomposition moves | General principle | Architecture practice | Long-standing |
| Rule-check price $0.0001 per case | Not in source | -- | -- |

:::takeaway
Decomposition is a means, not a virtue. Split on real seams, contract
every handoff, checkpoint every joint, and validate the merge.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01a | Fashion picks the pattern (D1.3) | Agent loop, 4 calls | Workflow for fixed task | p13-f01 | SVG | Original |
| u02a | Fork and cost carry over (D1.3) | -- | Prerequisite table | p13-f02 | Table | V2-D1.1, §7.1, §7.3 |
| u03a | Four-stop spectrum (D1.3) | Agentic always | Call, flow, hybrid, agent | p13-f03 | SVG | Original |
| u04a | Seven axes score the pick (D1.3) | -- | Mechanism prose | p13-f04 | Prose | Original |
| u05a | Spectrum prices itself (D1.3) | $480 per day all agentic | $55.40 per day hybrid | p13-f05 | SVG | Original |
| u05ba | 10-step method picks B (D1.3) | Three options | B matches split plus gate | p13-f05b | Table | Original |
| u09a | Constraints decide the pattern (D1.3) | -- | Constraint verdict table | p13-f09 | Table | Original |
| u10a | Agent for all is valid but inferior (D1.3) | -- | $480 vs $55.40 per day | p13-f10 | Table | Original |
| u11a | Open research favors the agent (D1.3) | -- | Counterfactual table | p13-f11 | Table | Original |
| u12a | Spectrum facts from memory (D1.3) | Blank recall card | Filled from memory | p13-f12 | ASCII | Original |
| u13a | Transfer to warehouse returns (D1.3) | Unseen question | Key in Stage 8 | p13-f13 | ASCII | Original |
| u01b | Sequential on splittable work (D1.4) | One agent, 48 s | Coordinator plus workers, 24 s | p14-f01 | SVG | Original |
| u02b | Spectrum and traces carry over (D1.4) | -- | Prerequisite table | p14-f02 | Table | V2-D1.3, §7.1 |
| u03b | Contract holds the crowd (D1.4) | Free chat | Handoff contracts | p14-f03 | SVG | Original |
| u04b | Run flow with checkpoints (D1.4) | -- | Mechanism prose | p14-f04 | Prose | Original |
| u05b | Half the wait, 30% more cost (D1.4) | 48 s, $0.054 | 24 s, $0.07 | p14-f05 | SVG | Original |
| u05bb | 10-step method picks B (D1.4) | Three options | B matches independence plus deadline | p14-f05b | Table | Original |
| u09b | Constraints decide multi-agent (D1.4) | -- | Constraint verdict table | p14-f09 | Table | Original |
| u10b | Single agent is valid but inferior (D1.4) | -- | 48 s vs 24 s | p14-f10 | Table | Original |
| u11b | Entangled task favors one agent (D1.4) | -- | Counterfactual table | p14-f11 | Table | Original |
| u12b | Team facts from memory (D1.4) | Blank recall card | Filled from memory | p14-f12 | ASCII | Original |
| u13b | Transfer to product launch (D1.4) | Unseen question | Key in Stage 8 | p14-f13 | ASCII | Original |
| u01c | One call, twelve updates (D1.5) | Giant call | Split, extract, merge | p15-f01 | SVG | Original |
| u02c | Dilution and spectrum carry over (D1.5) | -- | Prerequisite table | p15-f02 | Table | §7.3, V2-D1.3 |
| u03c | Five moves, two splits (D1.5) | One giant call | Route, chain, fan, critique, validate | p15-f03 | SVG | Original |
| u04c | Bounded pieces fail alone (D1.5) | -- | Mechanism prose | p15-f04 | Prose | Original |
| u05c | Four cents buys the trace (D1.5) | $0.168 one call | $0.207 fan-out | p15-f05 | SVG | Original |
| u05cb | 10-step method picks B (D1.5) | Three options | B matches traceability | p15-f05b | Table | Original |
| u09c | Constraints decide the move (D1.5) | -- | Constraint verdict table | p15-f09 | Table | Original |
| u10c | Chain all is valid but inferior (D1.5) | -- | Latency sums, errors compound | p15-f10 | Table | Original |
| u11c | Tiny task favors one call (D1.5) | -- | Counterfactual table | p15-f11 | Table | Original |
| u12c | Moves from memory (D1.5) | -- | Recall card | p15-f12 | ASCII | Original |
| u13c | Transfer to newsroom briefing (D1.5) | Unseen question | Key in Stage 8 | p15-f13 | ASCII | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | pxx-f06 | Table | S03, S04 |
| u07 | Joints can fail | Merge fails, start over | Checkpointed retry of the merge | pxx-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | pxx-f08 | Table | Original |
| u14 | Claims classified by date | -- | Evidence table | pxx-f14 | Table | Mixed |
