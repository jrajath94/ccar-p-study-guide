# Lesson D2-1: model selection and tier trade-offs (V2-D2.1)

## 1. Problem this lesson solves

A team runs every request on the most capable tier "for quality." The
bill lands. Simple classifications pay flagship prices. Nobody measured
whether the cheaper tier already clears the quality floor. Tier choice
was a habit, not a decision.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One tier for every task</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Simple tasks pay flagship prices. No floor was measured.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">all on most capable</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Easy task, flagship price.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Quality floor: unmeasured.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="40" rx="999" fill="#E7F1F8"/>
<text x="460" y="173" font-size="12" text-anchor="middle" fill="#1B2838">fast</text>
<rect x="508" y="148" width="80" height="40" rx="999" fill="#E7F1F8"/>
<text x="548" y="173" font-size="12" text-anchor="middle" fill="#1B2838">balanced</text>
<rect x="596" y="148" width="80" height="40" rx="999" fill="#E7F4EF"/>
<text x="636" y="173" font-size="12" text-anchor="middle" fill="#1B2838">capable</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Route by difficulty.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Escalate on low confidence.</text>
<defs><marker id="m-d21-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d21-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">route by difficulty</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The floor decides the tier. The habit does not.</text>
</svg>
<figcaption>Shell 3. One flagship tier becomes a routed cascade. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-3A gives the mechanism-versus-feature split: the exam tests
tier reasoning, not memorized model IDs. The Oct 2026 matrix below is
implementation enrichment from secondary sources, not exam scope.

| Foundation | What it gives this lesson |
|---|---|
| §7.3 sampler | Capability differences are real but task-relative |
| Oct 2026 tier matrix | Fast $1/$5, Balanced $2/$10, Capable $4/$20, Most capable $10/$50 per 1M |

## 3. Mental model

Think of a ladder with four rungs. Fast: cheapest, quickest, weakest.
Balanced: the default. Capable: harder tasks. Most capable: the top
rung, ten times the Fast input price. The rule: the cheapest tier that
clears the quality floor wins. Routing sends each task to its rung.
Cascading tries the cheap rung first and escalates on low confidence.
Fallback catches the rung that fails. The quality floor is the line
everything must clear: precision, latency, or both.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The ladder and the floor</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Input price ratio 1 to 10. The floor picks the rung.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">top rung, always</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Price ratio ignored.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Floor unmeasured.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">10x for no gain.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="548" y="169" font-size="12" text-anchor="middle" fill="#1B2838">most capable: 10x</text>
<rect x="420" y="188" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="548" y="209" font-size="12" text-anchor="middle" fill="#1B2838">capable: 4x</text>
<rect x="420" y="228" width="256" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="249" font-size="12" text-anchor="middle" fill="#1B2838">balanced: 2x, floor met</text>
<rect x="420" y="268" width="256" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="289" font-size="12" text-anchor="middle" fill="#1B2838">fast: 1x, floor met</text>
<defs><marker id="m-d21-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d21-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">measure the floor</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The cheapest rung that clears the floor wins. Measure, then climb.</text>
</svg>
<figcaption>Shell 3. One top rung becomes a priced ladder with a floor. Source: S10-S12 matrix, secondary.</figcaption>
</figure>

:::takeaway
Tier reasoning beats model memorization. The exam tests the trade:
capability against speed, latency, and cost, with a quality floor.
:::

## 4. Causal mechanism

Routing starts with a difficulty signal: task type, input length, or a
cheap classifier. Easy tasks go to the cheap rung. The attempt runs.
A confidence check follows: score, self-check, or a judge rule. Low
confidence escalates to the next rung. A failed rung falls back to a
safe default: a cached answer, a queue for human review, or a simpler
rung. Treat every tier change as a production change: new rung, new
regression test against the quality floor, new canary, same rollback
plan.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Route, check, escalate, fall back</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Four steps. The confidence check is the hinge.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">one tier, no check</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No difficulty signal.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No escalation.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No fallback.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="36" rx="999" fill="#E7F1F8"/>
<text x="480" y="171" font-size="12" text-anchor="middle" fill="#1B2838">route</text>
<rect x="556" y="148" width="120" height="36" rx="999" fill="#F6E7A8"/>
<text x="616" y="171" font-size="12" text-anchor="middle" fill="#1B2838">check</text>
<rect x="420" y="192" width="120" height="36" rx="999" fill="#E7F4EF"/>
<text x="480" y="215" font-size="12" text-anchor="middle" fill="#1B2838">escalate</text>
<rect x="556" y="192" width="120" height="36" rx="999" fill="#E6E2DA"/>
<text x="616" y="215" font-size="12" text-anchor="middle" fill="#1B2838">fall back</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">The check is the hinge.</text>
<text x="420" y="280" font-size="13" fill="#5C6B7A">Tier change: canary plus tests.</text>
<defs><marker id="m-d21-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d21-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">add the hinge</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The confidence check decides: ship, escalate, or fall back.</text>
</svg>
<figcaption>Shell 4. One tier gains route, check, escalate, and fallback. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: 1,000,000 classifications per day. Each call: 2,000 in tokens,
100 out. Prices per 1M from the Oct 2026 matrix (S10-S12, secondary).

All Balanced ($2 in, $10 out): in 2,000 / 1,000,000 x $2 = $0.004.
Out 100 / 1,000,000 x $10 = $0.001. Total $0.005 per call. Per day:
1,000,000 x $0.005 = $5,000.

Cascade: 90% clear on Fast ($1 in, $5 out): in 2,000 / 1,000,000 x $1
= $0.002. Out 100 / 1,000,000 x $5 = $0.0005. Total $0.0025. 900,000
x $0.0025 = $2,250. 8% escalate to Balanced: 80,000 x $0.005 = $400.
2% escalate to Capable ($4 in, $20 out): in 2,000 / 1,000,000 x $4 =
$0.008. Out 100 / 1,000,000 x $20 = $0.002. Total $0.01. 20,000 x
$0.01 = $200. Cascade total: $2,250 + $400 + $200 = $2,850 per day.
Savings: $5,000 - $2,850 = $2,150 per day, 43%, with the quality floor
held by the confidence check.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The cascade prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Oct 2026 matrix. 1M calls a day. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">all Balanced: $5,000 / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">$0.004 + $0.001 = $0.005.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">1M x $0.005 = $5,000.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No routing. No check.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">cascade: $2,850 / day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">900K x $0.0025 = $2,250.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">80K x $0.005 = $400.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">20K x $0.01 = $200.</text>
<defs><marker id="m-d21-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d21-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">cascade by confidence</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The cascade saves 43% a day and holds the floor with the check.</text>
</svg>
<figcaption>Shell 4. Routing turns $5,000 per day into $2,850 per day. Source: S10-S12 matrix, secondary.</figcaption>
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

Mini question: "A team classifies 1M items per day on the Balanced tier. A vendor proposes the Most capable tier for all traffic 'for quality.' The quality floor is 95% precision. The cascade already hits 96%. What is the best action? A) Move all traffic to the Most capable tier. B) Keep the cascade and add regression tests on the quality floor. C) Move all traffic to the Fast tier to cut cost."

| Step | Action on this question |
|---|---|
| STEP 1 | Optimization: cost against a quality floor |
| STEP 2 | Operation: production serving decision |
| STEP 3 | Hold quality, cut waste |
| STEP 4 | Floor is 95%. Current is 96%. No quality gap exists |
| STEP 5 | Model and serving layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | C risks the floor: Fast tier is unverified at 95%. A and B stay |
| STEP 8 | B holds the floor with tests. A spends $25,000 per day for no measured gain |
| STEP 9 | B needs the regression suite. Tier changes ship as production changes |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive fact is the absent quality gap: the floor is met, so the spend buys nothing.

:::takeaway
"For quality" is not a reason. The floor is the reason. If the floor is met, a bigger tier is waste until an eval says otherwise.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Tier ladder | Oct 2026 matrix, secondary | V2-D2.1 trade-off judgment |
| Routing and cascading | Application router | V2-D2.1 cost control |
| Confidence check | Score, judge rule, code | V2-D2.1 escalation |
| Fallback | Queue, cache, human review | V2-D1.2 fallbacks, V2-D5.3 review |
| Regression on tier change | Eval suite, canary | V2-D4.2 regression, V2-D4.6 monitoring |

## 7. Current limitations

Escalation adds latency: two rungs cost two calls. The cascade needs
calibration: a bad confidence check escalates everything or nothing.
Quality floors need evals: without a labeled set, the floor is a wish.
Tiers change: prices, windows, and retirements move, so the matrix is a
snapshot dated Oct 6, 2026, not a constant.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Escalation costs a call</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each escalation adds latency. Calibrate the check.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">check escalates all</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Every call pays twice.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Cascade is theater.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">check escalates 10%</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">90% pay once.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Calibrated on labels.</text>
<defs><marker id="m-d21-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d21-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">calibrate the check</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A bad check makes the cascade theater. Calibrate it on labels.</text>
</svg>
<figcaption>Shell 3. An uncalibrated check becomes a calibrated one. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Single tier for all | One rung | Tiny volume, no cost pressure |
| Fixed tier per task type | Static routing | Task types stable, difficulty known |
| Cascade with check (this lesson) | Dynamic routing | Mixed difficulty, cost pressure, floor held |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Quality floor unmet on the cheap tier | Climb until the floor holds |
| Floor met on the cheap tier | Stay. Bigger is waste |
| Latency SLA tight | Fewer rungs, maybe one |
| Tier change proposed | Regression tests plus canary first |

## 10. Valid-but-inferior option

Most capable tier for all traffic. Valid: best per-call quality,
simplest ops. Inferior: on the toy, the Most capable tier ($10 in, $50 out per
1M) prices the call at $0.025. Times 1M calls, that is $25,000 per day
against $2,850. No eval shows a gain above the floor.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Top tier for all | Best per-call quality | $25,000 vs $2,850 per day. Floor already met |

## 11. Counterfactual where the alternative wins

Latency SLA of 500 milliseconds, hard. The cascade's second call
cannot fit. One tier, the fastest that clears the floor, wins: the
latency constraint deletes the cascade.

| Situation | Winner | Why |
|---|---|---|
| Hard 500 ms latency SLA | Single fast tier | Escalation cannot fit the budget |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The rule: cheapest tier that clears the
   ______ wins.
2. The cascade hinge is the ______ check.
3. A tier change ships as a ______ change.
4. The cascade toy saves ______% per day.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A fraud team scores 500,000 transactions per day. The floor
is 99% recall on fraud. The Fast tier hits 97%. The Balanced
tier hits 99.2%. Escalation adds 400 ms. The SLA is 800 ms.
Name the routing. Name what the check must prove.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D2.1 tests tier trade-offs, routing, cascading, fallback, floors | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Four-tier matrix and prices | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy cascade arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Exam tests tier judgment, not model IDs | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Most capable tier $10/$50 per 1M | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |

:::takeaway
The exam's tier questions are floor questions. Find the floor in the
stem, find the cheapest rung that clears it, and distrust "for
quality" with no measurement.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | One tier for every task | All on most capable | Routed cascade | d21-f01 | SVG | Original |
| u02 | Mechanism split carries over | -- | Prerequisite table | d21-f02 | Table | §7.3, S10-S12 |
| u03 | Ladder and floor | Top rung always | Priced ladder, floor picks rung | d21-f03 | SVG | S10-S12 |
| u04 | Route, check, escalate, fall back | One tier, no check | Four steps with hinge | d21-f04 | SVG | Original |
| u05 | Cascade prices itself | $5,000 per day all Balanced | $2,850 per day cascade | d21-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B holds floor with tests | d21-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d21-f06 | Table | S03, S04 |
| u07 | Escalation costs a call | Check escalates all | Calibrated check | d21-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d21-f08 | Table | Original |
| u09 | Constraints decide the tier | -- | Constraint verdict table | d21-f09 | Table | Original |
| u10 | Top tier for all is valid but inferior | -- | $25,000 vs $2,850 per day | d21-f10 | Table | Original |
| u11 | Hard latency favors one tier | -- | Counterfactual table | d21-f11 | Table | Original |
| u12 | Ladder facts from memory | Blank recall card | Filled from memory | d21-f12 | ASCII | Original |
| u13 | Transfer to fraud scoring | Unseen question | Key in Stage 8 | d21-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d21-f14 | Table | Mixed |
