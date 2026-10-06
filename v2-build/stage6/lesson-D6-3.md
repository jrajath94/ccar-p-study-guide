# Lesson D6-3: feedback and expectation alignment (V2-D6.3)

## 1. Problem this lesson solves

The SLA says 99.9% success. The agent reads 98.7% this month. The
stakeholder calls it a breach and demands the vendor pay. The
vendor points at the fine print: the SLA covered uptime, not
quality. Nobody defined what a breach means for a probabilistic
system, so the argument starts after the money is gone.

An SLA without a definition, a review trigger, and a consequence
is a wish with a percentage on it. Probabilistic systems need
probabilistic contracts: measured quality, realistic ranges, named
triggers, stated consequences, and a rule for iterate versus
re-architect.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A percentage is not a contract</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">99.9% of what, measured how, and what happens at 98.7%?</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">"SLA 99.9%"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">breach at 98.7%?</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">No definition. Fight instead.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">error budget: 30 / day</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">trigger: 50 errors / day</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Defined breach, named consequence.</text>
<defs><marker id="m-d63-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d63-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">define the breach</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A contract that names the breach settles the argument before it starts.</text>
</svg>
<figcaption>Shell 3. A bare percentage becomes a defined breach. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D4-1 owns metric definitions and error budgets. Lesson
D6-1 owns owner sign-off. This lesson turns them into a standing
feedback contract.

| Foundation | What it gives this lesson |
|---|---|
| V2-D4.1 metrics | Primary metric, guard metrics, error budget |
| V2-D6.1 discovery | Owners who sign the consequences |

## 3. Mental model

A feedback contract has six parts. Measurable quality: the
primary metric and its threshold, from V2-D6.1. Realistic SLAs:
ranges, not points, because the system is probabilistic. Review
triggers: the numbers that start a review, stated in advance.
Breach consequences: what happens when a trigger fires, named
before it fires. Iterate versus re-architect: the rule that
separates tuning from a rebuild. Cost forecasting: the production
spend projection that keeps the budget honest.

:::takeaway
The trigger fires on numbers, not feelings. The consequence
was written before the crisis, not during it.
:::

<figure class="fig">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="420" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The six-part feedback contract</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One contract. Six parts. No argument about what a breach is.</text>
<rect x="24" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">"keep quality high"</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">"we will review sometime"</text>
<rect x="44" y="232" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">"costs look fine"</text>
<rect x="44" y="292" font-size="13" fill="#5C6B7A">Three wishes. Zero contracts.</rect>
<rect x="400" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="124" height="36" rx="8" fill="#E7F4EF"/>
<text x="482" y="167" font-size="12" text-anchor="middle" fill="#1B2838">quality: at least 96%</text>
<rect x="552" y="144" width="124" height="36" rx="8" fill="#E7F1F8"/>
<text x="614" y="167" font-size="12" text-anchor="middle" fill="#1B2838">trigger: 50 / day</text>
<rect x="420" y="188" width="124" height="36" rx="8" fill="#F6E7A8"/>
<text x="482" y="211" font-size="12" text-anchor="middle" fill="#1B2838">iter below 10 pts</text>
<rect x="552" y="188" width="124" height="36" rx="8" fill="#F4E6D4"/>
<text x="614" y="211" font-size="12" text-anchor="middle" fill="#1B2838">cost: $48k / mo</text>
<rect x="420" y="232" width="256" height="36" rx="8" fill="#E6E2DA"/>
<text x="548" y="255" font-size="13" text-anchor="middle" fill="#1B2838">breach: pause + human review</text>
<text x="420" y="292" font-size="13" fill="#5C6B7A">Six parts, signed by the owner.</text>
<defs><marker id="m-d63-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="216" x2="384" y2="216" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d63-3)"/>
<text x="360" y="200" font-size="13" text-anchor="middle" fill="#1B2838">write the six parts</text>
<text x="24" y="376" font-size="15" fill="#1B2838">Probabilistic systems get ranges and triggers, not points and wishes.</text>
</svg>
<figcaption>Shell 4. Three wishes become six contract parts. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Expectations drift in silence. The system ships at 96%
precision. Users adapt. The model version changes. Precision
slides to 92%. Nobody watches the metric, so nobody notices.
Users stop trusting the agent. The team learns from a churn
report, three months late.

A feedback loop closes the gap. The metric ships with the
product. The trigger fires at 50 errors per day. The review
happens the same week. The rule says: under 10 points of drop,
iterate the prompt and retrieval. Over 10 points, re-architect.
The consequence was signed before the crisis, so the response
is a procedure, not a panic.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The trigger closes the loop</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Silent drift vs watched drift. Same 4-point drop.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">96% slides to 92%</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">no one watches</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Found in the churn report, 90 days late.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">trigger fires at 50 / day</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">review same week</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Drop of 4 points: iterate, per the rule.</text>
<defs><marker id="m-d63-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d63-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">watch the metric</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A watched drift is a review. An unwatched drift is a surprise.</text>
</svg>
<figcaption>Shell 3. Silent drift becomes a fired trigger. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: triage agent, 10,000 tickets per day, primary metric
precision at least 96%. Error budget: 4% of 10,000 = 400 errors
per day allowed. Review trigger: 450 errors per day for two
consecutive days. Breach consequence: pause auto-routing, route
all to humans, page the owner. Iterate rule: precision drop
under 10 points, tune prompts and retrieval. Re-architect rule:
drop of 10 points or more, or three failed iterations.

Breach cost math: a breach pauses auto-routing for one day.
Manual triage of 10,000 tickets at 5 minutes each = 50,000
minutes = 833.3 hours. At $30 per hour = $25,000 for the day.
That number is the price of the consequence, written before
the crisis. The stakeholder signed it at discovery, so the
day it fires is a procedure, not a fight.

Cost forecast: $0.06 per ticket x 10,000 x 30 days = $18,000
per month, plus $30,000 per month of human review from the
4% error rate. Total $48,000 per month. The forecast is part
of the contract. When it drifts 20% above, the trigger fires
on cost too.

Mini question: "The triage agent's precision slides from 96%
to 92% over a month. The contract has review triggers and an
iterate rule for drops under 10 points. What is the correct
next action? A) Rebuild the pipeline with a larger model. B)
Run the review, tune prompts and retrieval, and re-measure. C)
Tighten the SLA to 99% and announce it."

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
| STEP 1 | Next action on a 4-point drift |
| STEP 2 | Operation: the system is live, the contract exists |
| STEP 3 | Restore precision per the signed contract |
| STEP 4 | The contract rules: iterate under 10 points, re-architect at 10 or more |
| STEP 5 | Expectation-alignment layer, not the model layer |
| STEP 6 | All three are feasible |
| STEP 7 | A violates the iterate-first rule: 4 is under 10. C violates the measurement rule: a tighter SLA changes nothing in the system |
| STEP 8 | B follows the contract: review, tune, re-measure |
| STEP 9 | B needs the error-budget dashboard to confirm the drift is real, not noise |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive rule is the signed iterate threshold.
A rebuild is the right answer only past 10 points. A new SLA
is paperwork, not a fix.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Error budget | Lesson D4-1, SRE practice | V2-D6.3 measurable quality |
| p95 SLA | Service contract | V2-D6.3 realistic probabilistic ranges |
| Review trigger | Feedback contract | V2-D6.3 triggers and consequences |
| Cost forecast | Lesson D1-2 business value | V2-D6.3 production cost forecasting |
| Iterate vs re-architect rule | Feedback contract | V2-D6.3 the boundary decision |

## 7. Current limitations

Triggers misfire: a data change can look like a model drop.
The iterate rule can stall: three failed iterations burn a
quarter. Consequences can be too harsh: pausing auto-routing
on a false alarm costs $25,000. And the contract itself
drifts: thresholds need the same review date as V2-D6.1
requirements.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The trigger misfires</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Data shifts. The metric moves. The model is fine.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">trigger fires</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">$25,000 pause, false alarm</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">New ticket types, same model.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">segment the drift first</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">rule: check the data cut</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Consequence waits for the diagnosis.</text>
<defs><marker id="m-d63-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d63-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">diagnose, then fire</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A trigger starts a diagnosis, not a punishment.</text>
</svg>
<figcaption>Shell 3. A firing trigger becomes a diagnosing trigger. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| No contract, react to complaints | Ad hoc firefighting | Tiny team, one user, low stakes |
| Metric dashboard only | Numbers with no triggers | Early stage, still learning the baseline |
| Six-part contract (this lesson) | Triggers, consequences, iterate rule, forecast | Production, real users, real money |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| System is probabilistic | Ranges and triggers, never a single point |
| Stakeholder demands 100% SLA | Distractor. No measurement supports it |
| Drift is under the iterate threshold | Tune, do not rebuild |
| Three failed iterations | Re-architect. The rule says so |

## 10. Valid-but-inferior option

Rebuild the pipeline with a larger model. Valid: a bigger
model can raise quality. Inferior here: the contract says
iterate under 10 points, the drop is 4, and a rebuild skips
the cheaper fix. Rebuilds also reset every tuned threshold.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Larger model rebuild | Can raise quality | Skips the contract's iterate rule |

## 11. Counterfactual where the alternative wins

Drop of 18 points after a vendor model change. Two tuning
rounds fail. The iterate rule no longer applies: the drop is
past 10 and iterations failed. Re-architect wins: the
contract itself orders the rebuild.

| Situation | Winner | Why |
|---|---|---|
| 18-point drop, tuning failed | Re-architect | The contract's own rule triggers |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Six parts: quality, SLAs, triggers,
   ______, iterate vs ______, cost ______.
2. Trigger example: ______ errors per day
   for ______ days.
3. Breach day price: $______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A hospital pilot shows 94% precision against
a 96% contract target. The error budget is
400 per day and the run rate is 420.
Name the trigger status, the iterate-vs-
rebuild verdict, and the one sentence you
tell the clinical lead.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D6.3 tests measurable quality, realistic probabilistic SLAs, triggers, consequences, iterate vs re-architect, cost forecasting | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D6.3 | Sept 2026 |
| Toy arithmetic: 400 errors/day budget, $25,000 breach day, $48,000/month forecast | Original toy, computed above | This lesson | Oct 6, 2026 |

:::takeaway
Ship the metric with the product. Write the trigger before
the drift. Name the consequence before the crisis. The
iterate rule keeps you from rebuilding on a Tuesday.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | A percentage is not a contract | "SLA 99.9%" | Defined breach and trigger | d63-f01 | SVG | Original |
| u02 | Metrics and owners carry over | -- | Prerequisite table | d63-f02 | Table | V2-D4.1, V2-D6.1 |
| u03 | Six-part feedback contract | Three wishes | Six signed parts | d63-f03 | SVG | Original |
| u04 | The trigger closes the loop | Silent drift | Review same week | d63-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B follows the contract | d63-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d63-f06 | Table | S03, S04 |
| u07 | The trigger misfires | False-alarm pause | Diagnose-then-fire rule | d63-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d63-f08 | Table | Original |
| u09 | Constraints decide the response | -- | Constraint verdict table | d63-f09 | Table | Original |
| u10 | Rebuild valid but inferior | -- | Validity vs inferiority table | d63-f10 | Table | Original |
| u11 | 18-point drop favors rebuild | -- | Counterfactual table | d63-f11 | Table | Original |
| u12 | Six parts from memory | Blank recall card | Filled from memory | d63-f12 | ASCII | Original |
| u13 | Transfer to hospital pilot | Unseen question | Key in Stage 8 | d63-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d63-f14 | Table | Mixed |
