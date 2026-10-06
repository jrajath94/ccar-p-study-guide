# Lesson D1-1: business problem to Claude solution (V2-D1.1)

## 1. Problem this lesson solves

A team hears "use AI for invoices" and starts building. No one writes the
outcome, the constraints, or the success line. The model ships. It reads
invoices. It also invents totals. Money moves on invented numbers.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A vague ask splits the build</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One request. Three guesses. No success line.</text>
<rect x="24" y="96" width="296" height="200" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">use AI for invoices</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">No outcome written.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">No constraints named.</text>
<text x="44" y="268" font-size="14" fill="#5C6B7A">No success line.</text>
<rect x="400" y="96" width="296" height="200" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">fixed layout goes to parser</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">open layout goes to Claude plus gate</text>
<text x="420" y="264" font-size="14" fill="#5C6B7A">Outcome: totals match the source.</text>
<text x="420" y="288" font-size="14" fill="#5C6B7A">Gate: code checks every total.</text>
<defs><marker id="m-d11-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="196" x2="384" y2="196" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d11-1)"/>
<text x="360" y="180" font-size="13" text-anchor="middle" fill="#1B2838">write the fork</text>
<text x="24" y="336" font-size="15" fill="#1B2838">The fork decides the lane before the build starts.</text>
</svg>
<figcaption>Shell 3. A vague request becomes a fork with an outcome and a gate. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A gives the chain: every adjective becomes a metric, a
threshold, and an owner. Lesson 7-3A gives the sampler model: the model
predicts the next token and never verifies.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 chain | Success criteria with numbers and an owner |
| §7.3 sampler | Every model output needs a check outside the model |

## 3. Mental model

Think of a fork in the road, not a single lane. One lane is
deterministic: fixed rules, fixed mapping, no surprises. The other lane
is Claude: open inputs, language understanding, sampled output. Four
questions pick the lane. Does the input vary in ways no template
covers? Does the task need language understanding? Can a
deterministic check verify the output? Is the error cost bounded and
reversible? Fixed mapping goes deterministic. Open input with a
verifiable output goes to Claude with a gate.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Four questions pick the lane</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fixed mapping goes left. Open input with a check goes right.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">Claude for everything</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Parser tasks pay model prices.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Fixed rules get sampled answers.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No lane decision.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="480" y="173" font-size="13" text-anchor="middle" fill="#1B2838">input fixed</text>
<rect x="556" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="616" y="173" font-size="13" text-anchor="middle" fill="#1B2838">input open</text>
<rect x="420" y="196" width="120" height="40" rx="8" fill="#E7F1F8"/>
<text x="480" y="221" font-size="13" text-anchor="middle" fill="#1B2838">parser</text>
<rect x="556" y="196" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="616" y="221" font-size="13" text-anchor="middle" fill="#1B2838">Claude plus gate</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">The check verifies the output.</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Four questions. Two lanes.</text>
<defs><marker id="m-d11-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d11-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">ask the four</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The task shape picks the lane. The slogan does not.</text>
</svg>
<figcaption>Shell 3. One Claude lane becomes a fork with a deterministic lane. Source: original toy.</figcaption>
</figure>

:::takeaway
Claude is a lane, not the road. Fixed mapping goes deterministic. Open
input with a verifiable output goes to Claude with a gate in code.
:::

## 4. Causal mechanism

Translation runs as a chain of five links. First, the business outcome:
what changes in the world. Second, functional requirements: what the
system does. Third, nonfunctional requirements: how well it does it, in
numbers. Fourth, hard constraints: what must never happen, like money
moving on an unchecked total. Fifth, the Claude-fit test and the success
criteria: which lane fits, and the metric, threshold, and owner that
prove it. Each link filters the design. Skip a link and the design
guesses.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five links filter the design</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Skip a link and the design guesses. Keep all five and it is filtered.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">ask goes straight to build</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Outcome: unwritten.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Constraints: unnamed.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Success: unmeasured.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="460" y="171" font-size="12" text-anchor="middle" fill="#1B2838">outcome</text>
<rect x="508" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">function</text>
<rect x="596" y="148" width="80" height="36" rx="999" fill="#F6E7A8"/>
<text x="636" y="171" font-size="12" text-anchor="middle" fill="#1B2838">numbers</text>
<rect x="464" y="192" width="80" height="36" rx="999" fill="#F3D4D8"/>
<text x="504" y="215" font-size="12" text-anchor="middle" fill="#1B2838">limits</text>
<rect x="552" y="192" width="80" height="36" rx="999" fill="#E7F4EF"/>
<text x="592" y="215" font-size="12" text-anchor="middle" fill="#1B2838">fit plus bar</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Each link filters the design.</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">The bar proves the lane.</text>
<defs><marker id="m-d11-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d11-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">run the chain</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Five links turn an ask into a filtered design with a proof bar.</text>
</svg>
<figcaption>Shell 4. The ask gains five links: outcome, function, numbers, limits, fit plus bar. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: invoice extraction. 10,000 invoices per day. 80% have a fixed
layout. 20% are open scans.

Functional: extract 12 fields per invoice. Nonfunctional: p95 at most
30 seconds, field precision at least 98%. Hard constraint: no payment
on an unchecked total. Success criteria: precision on a 500-invoice
holdout, p95 latency, cost per invoice, owner: finance lead.

Lane math on the Fast tier ($1 in, $5 out per 1M tokens, S10-S12, Oct
2026). One invoice call: 800 in tokens, 200 out. In: 800 / 1,000,000 x
$1 = $0.0008. Out: 200 / 1,000,000 x $5 = $0.001. Total $0.0018 per
invoice.

All Claude: 10,000 x $0.0018 = $18 per day, times 30 = $540 per month.
Hybrid: 8,000 fixed go to the parser at $0.0001 each = $0.80 per day.
2,000 open go to Claude at $0.0018 each = $3.60 per day. Total $4.40
per day, times 30 = $132 per month. The hybrid saves $13.60 per day
against all Claude and keeps the gate on every total.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The fork prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fast tier, $1 in and $5 out per 1M. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">all Claude: $540 / month</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">$0.0018 x 10,000 = $18 / day.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">$18 x 30 = $540 / month.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No gate on fixed layouts.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">hybrid: $132 / month</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">8,000 x $0.0001 = $0.80 / day.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">2,000 x $0.0018 = $3.60 / day.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">$4.40 x 30 = $132 / month.</text>
<defs><marker id="m-d11-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d11-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fork by layout</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The fork cuts the bill 4x and keeps a gate on every total.</text>
</svg>
<figcaption>Shell 4. The fork turns $540 per month into $132 per month. Source: original toy.</figcaption>
</figure>

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

Mini question: "A clinic routes patient messages. A wrong route delays care. The budget is fixed. Which design fits? A) One agent handles every message end to end. B) Deterministic rules route the 70% standard cases. Claude drafts replies for the rest. Code checks every draft against the source message before send. C) The most capable tier answers every message with no checks."

| Step | Action on this question |
|---|---|
| STEP 1 | Best architecture under constraints |
| STEP 2 | Design stage |
| STEP 3 | Safe routing inside a fixed budget |
| STEP 4 | Wrong route delays care. Budget is fixed. No unchecked output reaches patients |
| STEP 5 | Application layer: orchestration plus verification |
| STEP 6 | All three are technically feasible |
| STEP 7 | A breaks the check constraint: no verification anywhere. C breaks the budget and the check constraint |
| STEP 8 | B matches: deterministic for the standard cases, Claude for the rest, a gate on every draft |
| STEP 9 | B needs the rule set maintained. The gate needs the source message. Both are owned |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive constraint is patient safety plus a fixed budget, and only B pairs the fork with a gate on every draft.

:::takeaway
On the exam, translate the stem first: objective, hard constraints, system layer. Options that skip the translation usually miss the decisive constraint.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Functional vs nonfunctional split | §7.4 chain | V2-D1.1 translation, V2-D4.1 thresholds |
| Claude-vs-deterministic fork | Pattern choice | V2-D1.3 pattern selection |
| Gate on every model output | Deterministic code | V2-D5.1 guardrails, V2-D1.2 verification stage |
| Success criteria with owner | Eval plan | V2-D4.1 metric definition |

## 7. Current limitations

The fork is a snapshot. Inputs drift: a vendor changes its layout and a
parser case becomes an open case. The error cost can move too: a draft
that was low stakes becomes a payment instruction. Review the fork when
the input mix or the cost of a mistake changes.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The fork can rot</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Inputs drift. Costs move. The lane choice needs a review date.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">80% fixed, 20% open</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Parser wins most cases.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Fork set once.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">40% fixed, 60% open</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Vendor changed layouts.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Re-run the fork.</text>
<defs><marker id="m-d11-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d11-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">inputs drift</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A lane choice is a snapshot. Date it and re-run it when the mix moves.</text>
</svg>
<figcaption>Shell 3. A fixed fork breaks when the input mix drifts. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Claude for everything | One lane | Spike, demo, no hard constraints |
| Deterministic for everything | Rules only | Fixed mapping, zero tolerance for surprise |
| Fork by task shape (this lesson) | Two lanes plus a gate | Mixed inputs, hard constraints, real budget |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Fixed mapping, closed input set | Deterministic. No model needed |
| Open input, output verifiable in code | Claude plus a deterministic gate |
| Error cost high or irreversible | Gate is mandatory. Lane choice is second |
| No verification possible | Do not ship the Claude lane |

## 10. Valid-but-inferior option

Route everything through the most capable tier. Valid: best per-call
quality. Inferior: on the toy, the Capable tier ($4 in, $20 out per 1M)
prices the same invoice call at 800 / 1,000,000 x $4 = $0.0032 in plus
200 / 1,000,000 x $20 = $0.004 out = $0.0072 per invoice, times 10,000
= $72 per day against $18 on the Fast tier. Four times the cost for a
task the cheaper tier already passes.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Most capable tier for all | Best per-call quality | $72 per day vs $18. No eval shows the gain |

## 11. Counterfactual where the alternative wins

One vendor. One fixed layout. Ten years of identical invoices. The
parser covers 100% of cases. The Claude lane adds cost, latency, and a
gate for nothing. Deterministic wins outright.

| Situation | Winner | Why |
|---|---|---|
| Single fixed layout, frozen for years | Parser only | The open lane has no input to serve |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The four fork questions: input varies, needs language,
   output ______, error cost ______.
2. Fixed mapping goes ______.
3. Open input with a check goes to ______ plus a ______.
4. The hybrid toy costs $______ per month.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A bank classifies support tickets. A wrong class delays a fraud
review. The budget is fixed. Ten ticket types are fixed phrases.
Five are free-text complaints.
Name the lane for each group. Name the gate.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D1.1 tests translation, constraints, Claude-vs-deterministic, success criteria | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Tier prices $1/$5 in/out per 1M (Fast) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy invoice arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Fork questions and five-link chain | General principle | Architecture practice | Long-standing |
| Parser price $0.0001 per invoice | Not in source | -- | -- |

:::takeaway
The exam rewards the fork: the right lane for the task shape, a gate
where the error cost demands one, and numbers on the success bar.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Vague ask splits the build | No outcome, no constraints | Fork with outcome and gate | d11-f01 | SVG | Original |
| u02 | Chain and sampler carry over | -- | Prerequisite table | d11-f02 | Table | §7.4, §7.3 |
| u03 | Four questions pick the lane | Claude for everything | Fork: parser vs Claude plus gate | d11-f03 | SVG | Original |
| u04 | Five links filter the design | Ask straight to build | Outcome, function, numbers, limits, fit plus bar | d11-f04 | SVG | Original |
| u05 | Fork prices itself | $540 per month all Claude | $132 per month hybrid | d11-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches safety plus budget | d11-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d11-f06 | Table | S03, S04 |
| u07 | The fork can rot | Fork set once | Re-run when the mix moves | d11-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d11-f08 | Table | Original |
| u09 | Constraints decide the lane | -- | Constraint verdict table | d11-f09 | Table | Original |
| u10 | Top tier for all is valid but inferior | -- | $72 vs $18 per day | d11-f10 | Table | Original |
| u11 | Fixed layout favors the parser | -- | Counterfactual table | d11-f11 | Table | Original |
| u12 | Fork facts from memory | Blank recall card | Filled from memory | d11-f12 | ASCII | Original |
| u13 | Transfer to ticket lanes | Unseen question | Key in Stage 8 | d11-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d11-f14 | Table | Mixed |
