# Lesson D4-1: evaluation metrics (V2-D4.1)

## 1. Problem this lesson solves

A support agent ships. The fluency score on the dashboard reads 95.
Task success reads 60. Customers cannot get refunds. The dashboard is
green. The business is red.

The team optimized a proxy. Fluency measures how smooth the text
reads. Task success measures whether the job got done. Nothing in the
contract tied the metric to the goal. Vague requirements permit this.
Numbers attached to the wrong thing permit it too.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Green proxy, red goal</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The metric flatters. The business bleeds.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">fluency: 95</text>
<rect x="44" y="200" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">task success: 60</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">Dashboard green. Goal red.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">primary: task success at least 90</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">fluency: diagnostic only</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">The metric matches the goal.</text>
<defs><marker id="m-d41-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d41-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">swap the metric</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The dashboard must match the goal, not flatter the team.</text>
</svg>
<figcaption>Shell 3. A proxy primary metric becomes a task-success primary metric. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A gives the chain: requirement, metric, threshold, owner.
This lesson fills the metric link for model systems.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 chain | Adjectives become metrics with thresholds before the build |

## 3. Mental model

Three layers, one rule. The business outcome is what the company
earns: resolved tickets, revenue kept, harm avoided. Task success is
whether the system did the job: the refund issued, the answer
correct. Guard metrics are the floors that must not break: safety,
security, latency, reliability, cost.

The rule: the primary metric is the layer the scenario cares about
most. Everything else guards it. A proxy metric, like fluency or
answer length, is a diagnostic, never the primary. Promote a proxy
and the system games it: smoother text, same failed refunds.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Three layers, one primary</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Outcome, task, guards. The scenario picks the primary.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F4E6D4"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">primary: fluency 95</text>
<text x="44" y="204" font-size="13" fill="#5C6B7A">Guards: none named.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">Task success: unmeasured.</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Proxy rules the build.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#F6E7A8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">primary: task success</text>
<rect x="420" y="196" width="120" height="32" rx="999" fill="#E7F4EF"/>
<text x="480" y="217" font-size="12" text-anchor="middle" fill="#1B2838">safety floor</text>
<rect x="548" y="196" width="120" height="32" rx="999" fill="#E7F4EF"/>
<text x="608" y="217" font-size="12" text-anchor="middle" fill="#1B2838">cost ceiling</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Guards hold. Proxy watches.</text>
<defs><marker id="m-d41-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d41-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">demote the proxy</text>
<text x="24" y="352" font-size="15" fill="#1B2838">One primary, named guards. The proxy stays a diagnostic.</text>
</svg>
<figcaption>Shell 3. A proxy primary metric becomes a guarded task metric. Source: original toy.</figcaption>
</figure>

:::takeaway
Name the primary metric from the business goal. Name the guard
metrics from the floors. Never promote a proxy.
:::

## 4. Causal mechanism

Vague words enter at requirement time. "Handle support well" has no
measurable form. Each team picks a measurable stand-in. The stand-in
is always the easiest thing to count: fluency, length, tokens. The
system then optimizes the stand-in. The goal never got a metric, so
the goal never got optimized.

The chain from Lesson 7-4A stops this, applied to model systems.
Requirement: every ticket reaches the right queue with a correct
answer. Metric: task success on a held-out ticket set. Threshold: at
least 90%. Owner: support lead. Then the guards: safety incidents
zero, p95 under 5 seconds, cost per task under $0.05. Each guard is
a metric with a threshold and an owner.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The chain stops proxy drift</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Vague in, gamed out. The chain fixes the metric at requirement time.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">"handle support well"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F4E6D4"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">stand-in: fluency</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Easiest to count wins.</text>
<text x="44" y="276" font-size="13" fill="#5C6B7A">Goal never measured.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="32" rx="999" fill="#E7F1F8"/>
<text x="480" y="169" font-size="12" text-anchor="middle" fill="#1B2838">task success</text>
<rect x="548" y="148" width="120" height="32" rx="999" fill="#F6E7A8"/>
<text x="608" y="169" font-size="12" text-anchor="middle" fill="#1B2838">at least 90%</text>
<rect x="420" y="188" width="256" height="32" rx="8" fill="#E7F4EF"/>
<text x="548" y="209" font-size="12" text-anchor="middle" fill="#1B2838">guards: safety, p95, cost</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Goal measured. Proxy demoted.</text>
<defs><marker id="m-d41-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d41-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">attach the chain</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A metric fixed early cannot drift into a proxy later.</text>
</svg>
<figcaption>Shell 3. A vague goal becomes a chained metric with guards. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: refund agent. 10,000 tasks per day. Each task costs $0.02 in
tokens and tools.

Before: the team tunes fluency. Fluency 95. Task success 60%.
Cost per successful task: $0.02 / 0.60 = $0.0333. Successful tasks
per day: 10,000 x 0.60 = 6,000. Spend: 10,000 x $0.02 = $200 per
day for 6,000 wins.

After: the team sets task success as primary, threshold at least
90%, and guards safety at zero incidents. New task success 92%.
Cost per successful task: $0.02 / 0.92 = $0.0217. Successful tasks:
10,000 x 0.92 = 9,200. Same $200 per day buys 3,200 more wins.
Fluency is still measured. It is a diagnostic now, not the target.

Mini question: "A support bot shows fluency 95 and task success 60.
Budget is fixed. What is the first action? A) Tune the model for
higher fluency. B) Set task success as the primary metric with a
threshold, then optimize it. C) Move to a larger tier."

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
| STEP 1 | First action on a metric-goal mismatch |
| STEP 2 | Design: no eval contract exists |
| STEP 3 | Make the metric match the goal |
| STEP 4 | Task success 60. Budget fixed |
| STEP 5 | Evaluation layer: metric definition |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the objective: it deepens the proxy trap. C adds cost with no metric |
| STEP 8 | B names the primary metric and the threshold. Only B can move task success |
| STEP 9 | B needs a holdout set and an owner for the threshold |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fault is the proxy primary metric, and only
B replaces it before any tuning.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Cost per successful task</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">10,000 tasks a day. $0.02 per task. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$0.0333 per win</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">$0.02 / 0.60 = $0.0333.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">10,000 x 0.60 = 6,000 wins.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Fluency 95, wins 6,000.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$0.0217 per win</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">$0.02 / 0.92 = $0.0217.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">10,000 x 0.92 = 9,200 wins.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Same $200, +3,200 wins.</text>
<defs><marker id="m-d41-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d41-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">price the win</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Success per dollar is the business metric. Fluency never was.</text>
</svg>
<figcaption>Shell 4. Task success turns $0.0333 per win into $0.0217 per win. Source: original toy.</figcaption>
</figure>

:::takeaway
Cost per successful task is the business metric. Divide spend by
wins, not by calls.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Task success rate | Eval plan on a holdout set | V2-D4.1 primary metric |
| Groundedness | Citation check against retrieved chunks | V2-D4.1 quality metric, Lesson D3-5 |
| p50, p95 latency | Application metrics | V2-D4.1 latency metric, V2-D3.3 SLA |
| Token and tool cost | Billing plus per-hop trace cost | V2-D4.1 cost metric, Lesson D3-4 |
| Safety incident count | Guard log, zero threshold | V2-D4.1 guard metric, V2-D5.1 |

## 7. Current limitations

One metric never sees the whole goal. Task success can hide unsafe
wins. That is why guards exist. Metrics get gamed: a team that must
hit 90% task success will route hard tickets to humans and call it
an improvement. Thresholds expire when the ticket mix changes.
Measurement costs money: every metric needs a set, a rater, and a
refresh.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One metric hides unsafe wins</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Task success 92%. Safety incidents 3. The primary is green. The guard is red.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">task success: 92%</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">No guard measured.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Unsafe wins count as wins.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="480" y="169" font-size="13" text-anchor="middle" fill="#1B2838">success: 92%</text>
<rect x="556" y="144" width="120" height="40" rx="8" fill="#F3D4D8"/>
<text x="616" y="169" font-size="13" text-anchor="middle" fill="#1B2838">safety: 3</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Guard measured.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Ship blocked until zero.</text>
<defs><marker id="m-d41-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d41-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">add the guard</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The primary needs guards or the wins can turn unsafe.</text>
</svg>
<figcaption>Shell 3. An unguarded primary metric gains a safety guard. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Proxy-only eval | Fast, cheap signals | Early prototype, no users |
| Human panel on every release | Slow, expensive, accurate | High-stakes launch gate |
| Primary plus guards (this lesson) | Business metric with floors | Production decisions |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Vague requirement, no numbers | Apply the chain first. Metric with threshold |
| Metric green, goal red | The metric is a proxy. Replace it |
| Safety or security at stake | Add the guard metric with a zero threshold |
| Budget binds | Cost per successful task is the primary |

## 10. Valid-but-inferior option

Proxy-only evaluation. Valid: fast signal, cheap to run, catches
gross regressions. Inferior for ship decisions: fluency 95 coexisted
with task success 60 on the toy. A green proxy never proves the goal.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Proxy-only eval | Cheap smoke signal | 95 proxy, 60 goal. Ships the wrong thing |

## 11. Counterfactual where the alternative wins

Weekend prototype. No users. No money moves. The goal is to show
the flow works. Proxy-only eval wins: one cheap signal, zero eval
infrastructure, and no decision of consequence rests on it.

| Situation | Winner | Why |
|---|---|---|
| Demo, no stakes | Proxy-only eval | No decision rests on the metric |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The three layers: business ______, task ______,
   ______ metrics.
2. Cost per successful task = $______ / ______.
3. A proxy promoted to primary gets ______.
4. The chain: requirement, metric, ______, owner.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A recruiter wants "strong communicators" on the team.
Name the primary metric, two guard metrics, and the
threshold chain for one of them.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D4.1 tests metric families, vague to thresholds, proxy trap | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D4.1 | Sept 2026 |
| Toy cost-per-success arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Requirement, metric, threshold, owner chain | General principle, taught in Lesson 7-4A | This build | Oct 6, 2026 |

:::takeaway
The exam's D4.1 trap offers a shinier metric. The scenario asks for
the goal. Pick the metric that measures the goal, with a threshold.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Green proxy, red goal | Fluency 95, success 60 | Primary swapped to task success | d41-f01 | SVG | Original |
| u02 | Chain carries over | -- | Prerequisite table | d41-f02 | Table | §7.4 |
| u03 | Three layers, one primary | Proxy rules the build | Primary plus guards | d41-f03 | SVG | Original |
| u04 | Chain stops proxy drift | Vague goal, stand-in metric | Chained metric with guards | d41-f04 | SVG | Original |
| u05 | Cost per successful task | $0.0333 per win | $0.0217 per win | d41-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B replaces the proxy first | d41-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d41-f06 | Table | S03, S04 |
| u07 | One metric hides unsafe wins | No guard measured | Safety guard blocks ship | d41-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d41-f08 | Table | Original |
| u09 | Constraints decide the metric | -- | Constraint verdict table | d41-f09 | Table | Original |
| u10 | Proxy-only valid but inferior | -- | Validity vs inferiority table | d41-f10 | Table | Original |
| u11 | Demo favors proxy-only | -- | Counterfactual table | d41-f11 | Table | Original |
| u12 | Metric facts from memory | Blank recall card | Filled from memory | d41-f12 | ASCII | Original |
| u13 | Transfer to recruiter bot | Unseen question | Key in Stage 8 | d41-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d41-f14 | Table | Mixed |
