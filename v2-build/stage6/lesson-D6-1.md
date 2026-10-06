# Lesson D6-1: structured discovery (V2-D6.1)

## 1. Problem this lesson solves

A finance lead says: "Build an invoice agent. Make it fast and accurate."
The team builds for six weeks. At demo day the lead says: "It approved a
$40,000 invoice with no human check. We never allow that."

Nobody asked. Nobody wrote the answer down. The requirement existed in
one person's head and never reached the builders. The six weeks are
gone.

Unasked questions become silent assumptions. Silent assumptions become
the most expensive rework in a project. Discovery is the step that
finds them before the build.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Unasked questions are silent assumptions</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Eleven questions. One catch. Forty thousand dollars of risk removed.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">"fast and accurate"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">auto-approve $40,000</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">No one asked what is forbidden.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">11 discovery questions</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">gate over $1,000</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Prohibited behavior caught on day one.</text>
<defs><marker id="m-d61-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d61-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">ask first</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The cheapest fix is a question asked before the build.</text>
</svg>
<figcaption>Shell 3. Vague scope becomes a caught prohibition. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A owns the requirement-to-metric chain. This lesson uses
the chain as input and adds the question grid that feeds it.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 chain | Adjectives become metric, threshold, owner |

## 3. Mental model

Discovery asks eleven questions before any design. Each question
hunts one silent assumption.

Business outcomes: what improves, and by how much. Capabilities:
what the agent must do. Prohibited behaviors: what it must never
do. Workflows: the steps humans run today. Cost limits: spend per
task and per month. Volume: tasks per day, peak bursts. Quality,
latency, availability expectations: numbers, not adjectives.
Compliance: GDPR, HIPAA, or other regimes that constrain data.
Dependencies: systems the agent must touch. Owners: who signs off
and who gets the page at 3 a.m. Open assumptions: guesses still
unconfirmed.

:::takeaway
Eleven questions, each with a named owner. An assumption stays
open until a person signs it or a fact closes it.
:::

<figure class="fig">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="420" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The eleven-question grid</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each cell hunts one assumption. An empty cell is an open risk.</text>
<rect x="24" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">prohibited behaviors: ?</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">cost limits: ?</text>
<rect x="44" y="232" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">owners: ?</text>
<text x="44" y="308" font-size="13" fill="#5C6B7A">8 more blank cells</text>
<rect x="400" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="167" font-size="13" text-anchor="middle" fill="#1B2838">no auto-approve over $1,000</text>
<rect x="420" y="188" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="211" font-size="13" text-anchor="middle" fill="#1B2838">at most $0.20 per invoice</text>
<rect x="420" y="232" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="255" font-size="13" text-anchor="middle" fill="#1B2838">AP lead signs off</text>
<text x="420" y="308" font-size="13" fill="#5C6B7A">all 11 cells filled</text>
<defs><marker id="m-d61-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="216" x2="384" y2="216" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d61-3)"/>
<text x="360" y="200" font-size="13" text-anchor="middle" fill="#1B2838">ask and record</text>
<text x="24" y="376" font-size="15" fill="#1B2838">A blank cell is an open risk, not a minor gap.</text>
</svg>
<figcaption>Shell 4. Eleven blank cells become eleven answered cells. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Assumptions travel downstream. A vague adjective enters discovery
unquestioned. Design guesses a meaning. Implementation hardens the
guess into code. Testing checks the wrong bar. The stakeholder sees
the wrong behavior at the demo. Rework starts from the true
requirement, which the first question would have caught.

The cost of a fix grows ten times per phase. A question costs
minutes. A rebuild costs weeks. Discovery moves the catch from the
demo to day one.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The fix cost climbs per phase</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Same misunderstanding. Caught day one vs caught at demo.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">day 1: 33 min of questions</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">skipped, "no time"</text>
<rect x="44" y="252" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="277" font-size="13" text-anchor="middle" fill="#1B2838">demo day: 6-week rebuild</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">gate rule found on day 1</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">0 rebuild weeks</text>
<rect x="420" y="252" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="277" font-size="13" text-anchor="middle" fill="#1B2838">$82.5 of questions</text>
<text x="420" y="300" font-size="13" fill="#5C6B7A">11 x 3 min = 33 min, then 0.55 h x $150 = $82.50</text>
<defs><marker id="m-d61-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d61-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">catch it early</text>
<text x="24" y="352" font-size="15" fill="#1B2838">$82.50 of questions beats a six-week rebuild.</text>
</svg>
<figcaption>Shell 4. A skipped discovery becomes a priced discovery. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: accounts-payable invoice agent. Volume 500 invoices per day.
The stakeholder says "fast and accurate."

Discovery questions and answers: outcome, cut AP processing cost
by 40%. Capabilities: read invoice, match to PO, route exceptions.
Prohibited: never auto-approve above $1,000. Workflow: AP clerks
match POs today. Cost limit: at most $0.20 per invoice. Volume:
500 per day, 2,000 at month end. Quality: match precision at
least 98%. Latency: p95 under 60 seconds. Availability: business
hours only. Compliance: invoices carry vendor bank details, so
they are sensitive. Dependencies: NetSuite API. Owners: AP lead
signs off. Open assumptions: vendor scan quality, unconfirmed.

Cost payoff: 11 questions at 3 minutes each = 33 minutes =
0.55 hours. At $150 per hour = $82.50. The prohibited-behavior
catch removes a $40,000 auto-approve risk. Payoff ratio:
$40,000 / $82.50 = 485 to 1. The arithmetic is a toy, but the
direction is real.

Mini question: "A finance lead asks for an invoice agent, fast
and accurate. Volume 500 invoices per day. One team. No existing
spec. Which is the correct first action? A) Build with the
largest model and tune later. B) Run structured discovery across
outcomes, capabilities, prohibitions, workflows, cost, volume,
quality, latency, compliance, dependencies, and owners, then
convert adjectives to measurable requirements. C) Ship a
prototype and fix what the lead dislikes."

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
| STEP 1 | First action for a vague request |
| STEP 2 | Discovery: no spec exists yet |
| STEP 3 | Find the true requirements before any design |
| STEP 4 | "Fast and accurate" are adjectives. 500 invoices per day is real |
| STEP 5 | Lifecycle layer, not the model layer |
| STEP 6 | All three are feasible |
| STEP 7 | A and C violate the discovery-first order: they build on guesses |
| STEP 8 | B asks every dimension and converts adjectives to numbers |
| STEP 9 | B needs stakeholder time, 33 minutes. Cheap |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the missing spec. When the
stem gives no requirements, the correct next action is discovery,
not implementation.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Requirement chain | Lesson 7-4A | V2-D6.1 adjective-to-number conversion |
| Open assumptions log | Discovery record | V2-D6.1 explicit unconfirmed guesses |
| Owner sign-off | Team charter | V2-D6.1, V2-D6.3 accountability |
| Prohibited behaviors | Design constraints | V2-D6.1, V2-D3.2 deterministic enforcement |

## 7. Current limitations

Discovery cannot find unknown unknowns. A stakeholder may not
know the corner cases either. Answers can be wrong: the AP lead
says $1,000, the CFO says $500. Discovery takes calendar time:
stakeholders do not reply on demand. And the grid goes stale:
volume doubles, compliance changes, owners leave.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The grid goes stale</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Volume doubles. One cell is wrong. The rest hold.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">500 / day, all cells signed</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Month-end spike hits 2,000.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">volume cell wrong</text>
<rect x="420" y="208" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="233" font-size="14" text-anchor="middle" fill="#1B2838">re-sign one cell</text>
<text x="420" y="260" font-size="13" fill="#5C6B7A">Review date catches it.</text>
<defs><marker id="m-d61-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d61-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">review the grid</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Discovery is a living record. Date it and re-sign it.</text>
</svg>
<figcaption>Shell 3. A signed grid becomes a re-signed grid. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Skip discovery, build now | Implementation first | Reversible demo, one builder, no money moves |
| Light discovery, five questions | Outcomes, prohibitions, owners, cost, volume | Small project, trusted stakeholder, low stakes |
| Full eleven-question grid (this lesson) | All dimensions plus open assumptions | Handoffs, money or compliance, real volume |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Stem gives adjectives, no numbers | Run discovery. First action, not implementation |
| Money, safety, or compliance in scope | Full grid, with prohibitions written down |
| Two or more teams hand off | Full grid, signed by owners |
| Weekend demo, no real data | Skip the grid. Build |

## 10. Valid-but-inferior option

Ship a prototype and fix complaints. Valid: prototypes surface
real reactions fast. Inferior here: the lead's first complaint
arrives after the agent already auto-approved invoices, and the
"fix" is a rebuild of the approval flow.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Prototype first | Fast feedback | Feedback arrives after the money moved |

## 11. Counterfactual where the alternative wins

Internal hackathon. No real invoices. Demo in two days. The grid
costs a day of stakeholder chasing. Building wins: the correct
discovery is "what looks good on the demo screen."

| Situation | Winner | Why |
|---|---|---|
| Hackathon, no real data | Build first | Discovery cost exceeds the stakes |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The grid asks: outcomes, capabilities, ______,
   workflows, cost limits, volume, ______,
   compliance, dependencies, owners, ______.
2. Adjectives become ______ before design.
3. A blank cell is an open ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A hospital asks for a discharge-summary agent.
"Accurate" matters for patient safety.
List the five discovery questions that find
the safety constraints. Then state which one
a builder most often skips.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D6.1 tests structured discovery across the eleven dimensions plus adjective-to-metric conversion | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D6.1 | Sept 2026 |
| Toy arithmetic: 33 min, $82.50, 485 to 1 payoff | Original toy, computed above | This lesson | Oct 6, 2026 |
| Discovery-first as correct next action on vague stems | General principle | Industry practice | Long-standing |

:::takeaway
When the stem is vague, the exam's answer is discovery.
Implementation on adjectives is the distractor. Ask the eleven
questions, then design.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Unasked questions are silent assumptions | "fast and accurate" | $40,000 auto-approve risk | d61-f01 | SVG | Original |
| u02 | Chain carries over from §7.4 | -- | Prerequisite table | d61-f02 | Table | §7.4 |
| u03 | Eleven-question grid | Blank cells | Answered cells | d61-f03 | SVG | Original |
| u04 | Fix cost climbs per phase | Skipped discovery | 33 min, $82.50 catch | d61-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B is discovery-first | d61-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d61-f06 | Table | S03, S04 |
| u07 | The grid goes stale | Signed grid | Re-sign one cell | d61-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d61-f08 | Table | Original |
| u09 | Constraints decide the method | -- | Constraint verdict table | d61-f09 | Table | Original |
| u10 | Prototype-first valid but inferior | -- | Validity vs inferiority table | d61-f10 | Table | Original |
| u11 | Hackathon favors building | -- | Counterfactual table | d61-f11 | Table | Original |
| u12 | Eleven cells from memory | Blank recall card | Filled from memory | d61-f12 | ASCII | Original |
| u13 | Transfer to hospital agent | Unseen question | Key in Stage 8 | d61-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d61-f14 | Table | Mixed |
