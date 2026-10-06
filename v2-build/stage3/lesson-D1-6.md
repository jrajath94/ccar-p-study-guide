# Lesson D1-6: business-value alignment (V2-D1.6)

## 1. Problem this lesson solves

A team ships "AI for contract review" and declares victory. No one
measured the baseline. No one priced the build. Finance asks for the
return. The team has adjectives. Adjectives are not a return.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Adjectives are not a return</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">No baseline. No price. Finance asks. Adjectives answer.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">AI saves money</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Baseline: unknown.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Build cost: unknown.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="40" rx="8" fill="#E7F1F8"/>
<text x="460" y="173" font-size="12" text-anchor="middle" fill="#1B2838">base</text>
<rect x="508" y="148" width="80" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="12" text-anchor="middle" fill="#1B2838">new</text>
<rect x="596" y="148" width="80" height="40" rx="999" fill="#F6E7A8"/>
<text x="636" y="173" font-size="12" text-anchor="middle" fill="#1B2838">cost</text>
<rect x="464" y="200" width="168" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">net value: $689K / year</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Numbers, not adjectives.</text>
<defs><marker id="m-d16-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d16-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">price the change</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Value is baseline minus new cost, times volume, plus errors avoided.</text>
</svg>
<figcaption>Shell 3. A money claim becomes a priced equation. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A gives the triage toy: manual $500 per week, with chain $51
per week. This lesson reuses that chain at business scale.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 chain | Metric, threshold, owner for every value claim |
| §7.4 triage toy | Baseline minus new cost, worked once |

## 3. Mental model

Think of one equation with four terms. Net value equals baseline cost
minus new cost, times volume, plus avoided error cost, minus build and
run cost. Four value types feed it. Efficiency does the same work cheaper.
Productivity does more with the same people. Transformation does the
impossible. Quality cuts the error bill. SLOs guard the equation: latency, reliability, and accuracy
floors keep the savings from eating the business.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Four terms, one equation</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Baseline, new cost, errors avoided, build cost. Miss one and it lies.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">savings: big</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">One term.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Build cost: missing.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Error bill: missing.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="36" rx="8" fill="#E7F1F8"/>
<text x="480" y="171" font-size="12" text-anchor="middle" fill="#1B2838">base minus new</text>
<rect x="548" y="148" width="128" height="36" rx="8" fill="#E7F4EF"/>
<text x="612" y="171" font-size="12" text-anchor="middle" fill="#1B2838">errors avoided</text>
<rect x="464" y="192" width="168" height="36" rx="8" fill="#F6E7A8"/>
<text x="548" y="215" font-size="12" text-anchor="middle" fill="#1B2838">minus build plus run</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Four terms.</text>
<text x="420" y="280" font-size="13" fill="#5C6B7A">SLOs guard the equation.</text>
<defs><marker id="m-d16-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d16-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">count all four</text>
<text x="24" y="352" font-size="15" fill="#1B2838">One term is a slogan. Four terms are a business case.</text>
</svg>
<figcaption>Shell 3. One savings term becomes four priced terms. Source: original toy.</figcaption>
</figure>

:::takeaway
Net value = (baseline cost - new cost) x volume + avoided error cost
- build and run cost. Every term needs a number and an owner.
:::

## 4. Causal mechanism

Value flows in order: baseline, improvement, cost, net. First, price
the baseline: hours times rate, or errors times incident cost. Second,
name the improvement: which value type, and the metric that proves it.
Third, price the new world: run cost per unit times volume, plus the
residual error bill, plus review labor. Fourth, subtract: the
difference is the net, and the SLOs say whether the net is honest. A
latency win that breaches the accuracy floor is not value. It is a
transfer from quality to speed.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Quality becomes dollars</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Errors times incident cost. That is the quality term.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">fewer errors</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Adjective.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No incident price.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Quality term: $0.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">2 avoided x $50K</text>
<text x="420" y="224" font-size="13" fill="#5C6B7A">2 incidents per year avoided.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Incident price: not in source.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Quality term: $100K / year.</text>
<defs><marker id="m-d16-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d16-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">price the errors</text>
<text x="24" y="352" font-size="15" fill="#1B2838">An unpriced error is a zero in the equation. Price it or drop it.</text>
</svg>
<figcaption>Shell 4. The quality term gains an incident price. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: contract review. 500 contracts per week. Lawyer rate $80 per hour
(toy assumption).

Baseline: 500 x 20 minutes = 10,000 minutes = 166.7 hours. 166.7 x $80
= $13,333 per week.

New world: Claude first pass at $0.02 per contract = $10 per week.
Lawyers review the 30% flagged: 150 x 10 minutes = 1,500 minutes = 25
hours. 25 x $80 = $2,000 per week. Total $2,010 per week.

Savings: $13,333 - $2,010 = $11,323 per week. Times 52 = $588,796 per
year. Quality term: missed clauses caused 2 incidents per year at
$50,000 each (not in source) = $100,000 per year avoided. Net value:
$588,796 + $100,000 = $688,796 per year, before build cost.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The equation fills in</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">500 contracts a week. $80 an hour. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">manual: $13,333 / week</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">500 x 20 min = 10,000 min.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">10,000 / 60 = 166.7 h.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">166.7 x $80 = $13,333.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">net: $689K / year</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">$13,333 - $2,010 = $11,323 / week.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">$11,323 x 52 = $588,796 / year.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Plus $100K errors avoided.</text>
<defs><marker id="m-d16-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d16-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fill the terms</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Four terms filled. The business case is a number, not an adjective.</text>
</svg>
<figcaption>Shell 4. Four filled terms become a $689K yearly case. Source: original toy.</figcaption>
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

Mini question: "A clinic considers an AI scribe. Run cost is $40,000 per year. Ten doctors save 5 hours per week each. A doctor hour costs $150 (toy). Documentation errors cost $20,000 per incident (not in source): 3 per year now, 1 per year with the scribe. What is the net value? A) $40,000 cost only: too expensive. B) Time savings minus run cost: 10 x 5 x 52 x $150 = $390,000 - $40,000 = $350,000. C) Time savings plus avoided error cost minus run cost: $390,000 + $40,000 - $40,000 = $390,000."

| Step | Action on this question |
|---|---|
| STEP 1 | Optimization: compute net value |
| STEP 2 | Design stage: business case |
| STEP 3 | True net value of the scribe |
| STEP 4 | Count all four terms: time savings, error change, run cost |
| STEP 5 | Business and financial layer |
| STEP 6 | All three are arithmetic claims, all feasible |
| STEP 7 | No hard constraint is violated. All stay in the race |
| STEP 8 | C counts every term. B drops the error term. A drops the savings |
| STEP 9 | C assumes the error cut from 3 to 1 holds. Flag it as the sensitive term |
| STEP 10 | C alone. Single select |

The verdict is C. The decisive move is the count of all four terms, and only C does.

:::takeaway
On the exam, a value question is an arithmetic question. Write the four terms, fill each with the stem's numbers, and distrust any option that drops a term.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Baseline and net value | Business case, §7.4 | V2-D1.6 alignment, V2-D6.2 trade-off talk |
| SLOs as value guards | Service contract | V2-D1.6 reliability, V2-D3.3 tuning to SLAs |
| Cost per unit | Token budget, §7.3 | V2-D2.1 tier choice, V2-D4.5 cost control |
| ADR with the value math | Decision record | V2-D6.4 documentation |

## 7. Current limitations

Value estimates rot. The baseline moves: wages rise, volume doubles,
the error mix shifts. The incident price is often a guess: label it,
do not hide it. Attribution is hard: the scribe, the new checklist,
and the new hire all claim the same error drop. Re-sign the equation
when the world moves, and keep the SLOs as the honesty check.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The baseline moves</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Volume doubles. The old equation lies. Re-sign it.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">net: $689K / year</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Volume: 500 per week.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Equation signed once.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">volume: 1,000 per week</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Review labor doubles too.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Re-run the four terms.</text>
<defs><marker id="m-d16-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d16-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">volume doubles</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A business case is a snapshot. Date it and re-sign it.</text>
</svg>
<figcaption>Shell 3. A signed equation breaks when volume doubles. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Build on vibes | Adjectives, no baseline | Hackathon, no money at stake |
| Full value equation (this lesson) | Four terms with numbers | Real budget, real stakeholders |
| Pilot then measure | Small run, real numbers | Uncertain baseline, reversible pilot |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Real budget and stakeholders | Full equation before the build |
| Net value negative | Do not build. The best answer is no |
| Baseline unknown | Pilot first, then decide |
| Quality is the value driver | Price the error term or the case lies |

## 10. Valid-but-inferior option

Optimize the easiest metric: cut latency 20% while the value driver
is error cost. Valid: latency is real value when users wait. Inferior:
on the toy, a 20% latency cut saves nobody's week, while one avoided
$50,000 incident beats a year of latency work.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Cut latency 20% | Real value when users wait | Error cost dominates. Latency is not the driver |

## 11. Counterfactual where the alternative wins

The equation comes back negative: $40,000 run cost against $25,000
savings, no error term. Building is value destruction. The best answer
is do not build: keep the manual process, or narrow the scope until
the equation turns.

| Situation | Winner | Why |
|---|---|---|
| Negative net value | Do not build | Building destroys value |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Net value = (baseline - new) x ______ plus
   avoided ______ minus build and run cost.
2. The four value types: efficiency, ______,
   transformation, quality.
3. The contract toy net: $______K per year.
4. Negative net value means ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A support team considers auto-drafting replies. Agents handle
2,000 tickets per week at 6 minutes each. Agent hour costs
$45 (toy). Wrong drafts that ship cost $500 per incident
(not in source): 10 per year now, 4 with drafts plus review.
Drafts cost $0.01 each to run.
Compute the net value. State the build decision.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D1.6 tests value types, baseline to net value, SLOs | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Toy contract arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Net value equation | General principle | Business practice | Long-standing |
| Incident price $50,000, doctor hour $150 | Not in source | -- | -- |

:::takeaway
The exam tests whether value is priced, not promised. Four terms,
numbers on each, SLOs as guards, and the courage to answer no.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Adjectives are not a return | AI saves money | Priced equation | d16-f01 | SVG | Original |
| u02 | Triage toy carries over | -- | Prerequisite table | d16-f02 | Table | §7.4 |
| u03 | Four terms, one equation | Savings: big | Base, new, errors, build | d16-f03 | SVG | Original |
| u04 | Quality becomes dollars | Fewer errors | 2 avoided x $50K | d16-f04 | SVG | Original |
| u05 | Equation fills in | Manual $13,333 per week | Net $689K per year | d16-f05 | SVG | Original |
| u05b | 10-step method picks C | Three options | C counts all four terms | d16-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d16-f06 | Table | S03, S04 |
| u07 | The baseline moves | Equation signed once | Re-run the four terms | d16-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d16-f08 | Table | Original |
| u09 | Constraints decide the case | -- | Constraint verdict table | d16-f09 | Table | Original |
| u10 | Latency cut is valid but inferior | -- | Error cost dominates | d16-f10 | Table | Original |
| u11 | Negative value means do not build | -- | Counterfactual table | d16-f11 | Table | Original |
| u12 | Equation from memory | Blank recall card | Filled from memory | d16-f12 | ASCII | Original |
| u13 | Transfer to auto-drafting | Unseen question | Key in Stage 8 | d16-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d16-f14 | Table | Mixed |
