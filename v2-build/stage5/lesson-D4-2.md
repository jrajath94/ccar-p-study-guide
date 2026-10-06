# Lesson D4-2: evaluation datasets and frameworks (V2-D4.2)

## 1. Problem this lesson solves

A team evaluates its agent on 200 clean questions. Average success:
94%. It ships. In production, malformed inputs crash the parser,
adversarial prompts leak policy text, and one customer segment fails
half the time. None of those cases lived in the set.

The set was a mirror of the easy day. The eval measured the team's
comfort, not the system's behavior. A dataset is a claim about what
the world will throw. This one claimed the world is clean.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The set measured the easy day</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">94% average. The edge cases never ran.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">200 clean cases: 94%</text>
<rect x="44" y="200" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">edge cases: not present</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">Ships on a lie.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">mixed set: 81% average</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">edge segment: 55%</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Honest score. Fix ships next.</text>
<defs><marker id="m-d42-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d42-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">add the edge</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The honest set scores lower and tells the truth.</text>
</svg>
<figcaption>Shell 3. A clean-only set becomes a mixed set with an edge segment. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D4-1 gives the primary metric and the guards. This lesson
builds the dataset that measures them.

| Foundation | What it gives this lesson |
|---|---|
| V2-D4.1 metrics | Primary plus guards, each with a threshold |

## 3. Mental model

A dataset has five drawers. Representative cases mirror production
traffic. Edge cases sit at the boundary: the longest input, the
rarest format. Adversarial cases try to break the system: injection
attempts, trick questions. Malformed cases are broken inputs: empty
fields, bad encodings. Regression cases are old failures that must
never return.

The evaluator ladder has three rungs. Code is cheapest: a script
compares output to an expected answer. A judge model is next: a model
scores the output against a rubric. Human labels are last: people
decide, slowly and well. Rule: use the cheapest evaluator that stays
reliable. Calibrate each rung against the rung above it.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five drawers, three rungs</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The set covers the world. The rungs price the grading.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="13" text-anchor="middle" fill="#1B2838">one drawer: clean</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Grader: whoever is free.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No calibration.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Score: 94% of nothing.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="32" rx="999" fill="#E7F1F8"/>
<text x="480" y="169" font-size="12" text-anchor="middle" fill="#1B2838">rep</text>
<rect x="548" y="148" width="120" height="32" rx="999" fill="#F6E7A8"/>
<text x="608" y="169" font-size="12" text-anchor="middle" fill="#1B2838">edge</text>
<rect x="420" y="188" width="120" height="32" rx="999" fill="#F3D4D8"/>
<text x="480" y="209" font-size="12" text-anchor="middle" fill="#1B2838">advers</text>
<rect x="548" y="188" width="120" height="32" rx="999" fill="#E6E2DA"/>
<text x="608" y="209" font-size="12" text-anchor="middle" fill="#1B2838">malformed</text>
<rect x="476" y="228" width="144" height="32" rx="999" fill="#D9E8D3"/>
<text x="548" y="249" font-size="12" text-anchor="middle" fill="#1B2838">regression</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Code first. Judge next. Human last.</text>
<defs><marker id="m-d42-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d42-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fill the drawers</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Five drawers hold the world. Three rungs price the grading.</text>
</svg>
<figcaption>Shell 3. One clean drawer becomes five drawers with a graded ladder. Source: original toy.</figcaption>
</figure>

:::takeaway
Build the set from production, not from comfort. Grade with the
cheapest reliable rung. Calibrate each rung against the one above.
:::

## 4. Causal mechanism

Averages hide subgroups. The toy numbers below show how. The team
reports 94% average. One segment, 20% of traffic, sits at 55%.
The average buried it. The exam tests this: high average can hide
critical-subgroup failure. Report per segment. Set thresholds per
segment that matters.

Leakage poisons the set. If the training data saw the eval cases,
the score measures memory, not ability. Holdouts stay locked: no
training on them, no peeking during tuning. Label quality is the
same kind of poison: bad labels make a good system look bad and a
bad system look good. Version the set. Refresh it as production
shifts. Strip customer PII before a case leaves the trust boundary.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The average buries a segment</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">94% overall. One segment at 55%. The average told no one.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">average: 94%</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">One number.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Segment invisible.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Ship approved.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">common 80%: 95%</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">edge 20%: 55%</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">0.8 x 95 + 0.2 x 55 = 87.</text>
<text x="420" y="276" font-size="13" fill="#5C6B7A">Ship blocked.</text>
<defs><marker id="m-d42-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d42-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">split the average</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Report per segment. Threshold per segment that matters.</text>
</svg>
<figcaption>Shell 3. One average becomes two segment scores with arithmetic. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: the refund agent. Eval set: 500 cases. 400 representative,
50 edge, 30 adversarial, 20 malformed, plus a regression file of
40 old failures. Locked holdout: 100 of the 500, never used in
tuning.

Evaluator choice. Code grader: exact match on the refund amount
and account id. Cost near zero per case. Judge model: rubric on
the explanation text, $0.002 per case. Human: spot labels on
disputed cases, $0.50 per case.

Calibration. The judge grades 100 human-labeled cases first. It
agrees on 82. Agreement 82%. Per segment: 80 common cases, 76
agree, 95%. 20 edge cases, 6 agree, 30%. The judge is reliable on
the common drawer and useless on the edge drawer. Decision: code
for amounts, human for edge explanations, judge only for common
explanations.

Cost arithmetic. 500 cases by code: near $0. 300 common
explanations by judge: 300 x $0.002 = $0.60. 50 edge cases by
human: 50 x $0.50 = $25. Total $25.60 per run. All-human grading
would cost 500 x $0.50 = $250. The ladder cuts grading cost 90%.

Mini question: "A judge grades 100 human-labeled cases with 82%
agreement. On the edge drawer it agrees 30% of the time. Which
grading plan fits? A) Judge grades everything. B) Code grades
amounts, the judge grades common explanations, humans grade edge
explanations. C) Humans grade everything."

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
| STEP 1 | Architecture of the grading plan |
| STEP 2 | Preproduction: the eval framework is under construction |
| STEP 3 | Reliable grades at the lowest cost |
| STEP 4 | Judge is unreliable on the edge drawer at 30% |
| STEP 5 | Evaluation framework layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates reliability: the judge fails the edge drawer. C violates cost: 10x the ladder |
| STEP 8 | B matches each drawer to the cheapest reliable rung |
| STEP 9 | B needs the calibration run first and a human label budget for edges |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the calibration: 30% agreement on
the edge drawer disqualifies the judge there, and the ladder puts
each drawer on its cheapest reliable rung.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The ladder prices grading</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">500 cases. Three rungs. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$250 per run</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">500 x $0.50 = $250.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">All human.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Runs stay rare.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$25.60 per run</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Judge: 300 x $0.002 = $0.60.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Human: 50 x $0.50 = $25.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">90% cheaper. Runs go daily.</text>
<defs><marker id="m-d42-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d42-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">grade by rung</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The cheapest reliable rung wins each drawer.</text>
</svg>
<figcaption>Shell 4. The evaluator ladder turns $250 per run into $25.60. Source: original toy.</figcaption>
</figure>

:::takeaway
Calibrate the judge against human labels per drawer. Then give
each drawer its cheapest reliable rung.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Holdout set | Eval data store, locked | V2-D4.2 leakage prevention |
| Regression file | Eval set, old failures | V2-D4.2 never-regress check |
| Judge rubric | Eval setup config | V2-D4.2 judge calibration |
| Set version | Data version tag | V2-D4.2 versioning and refresh |

## 7. Current limitations

The set decays. Production shifts, the set stays. Refresh is a
chore and gets skipped. Labels drift: two humans disagree on 10%
of cases. Not in source: a real disagreement rate for this toy.
The judge drifts too: a model update changes its grades. Leakage
is silent: one shared example between train and eval corrupts the
score with no error message. Privacy review slows case collection.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The set decays silently</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Production moves. The set stays. The score lies by age.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">set frozen, v3</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Production adds new intents.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Score: still 90.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">refresh cadence, v4</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">New intents enter the set.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Version bumped. Score honest.</text>
<defs><marker id="m-d42-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d42-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">refresh on cadence</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Version the set. Refresh it as production shifts.</text>
</svg>
<figcaption>Shell 3. A frozen set becomes a versioned set on a refresh cadence. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Clean-only set | Fast to build | Demo, no stakes |
| Adversarial-only set | Red team signal | Security review gate |
| Five drawers plus ladder (this lesson) | Full coverage, priced grading | Production eval |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Production has ugly inputs | Edge, adversarial, and malformed drawers are mandatory |
| Old bugs must stay fixed | Regression drawer, run on every change |
| Grading budget is small | Calibrate once, then use the ladder |
| Judge uncalibrated | Human labels first. No judge without a calibration run |
| PII in production cases | Strip before the case leaves the trust boundary |

## 10. Valid-but-inferior option

Human grading of everything. Valid: the most reliable grades.
Inferior at scale: $250 per run on the toy versus $25.60 on the
ladder. Daily runs become monthly runs. The framework dies from
its own cost.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| All-human grading | Best grade quality | 10x the cost. Runs go rare |

## 11. Counterfactual where the alternative wins

Launch gate for a medical triage agent. Fifty cases. Each wrong
grade risks a bad ship decision. Humans grade all fifty: $25
total. The ladder's machinery exceeds the stakes.

| Situation | Winner | Why |
|---|---|---|
| Tiny high-stakes set | All-human grading | Fifty cases. Cost is trivial |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The five drawers: representative, edge,
   adversarial, ______, regression.
2. The ladder, cheapest first: ______, judge, human.
3. Judge agreement on the toy: ______% overall,
   ______% on the edge drawer.
4. The ladder costs $______ per run vs $______ all human.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A loan-approval agent fails on non-English applications.
The eval set is 100% English. The average is 93%.
Name the missing drawer, the report that would expose
the failure, and the grading rung for the new drawer.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D4.2 tests dataset drawers, holdouts, leakage, label quality, versioning, refresh, privacy, evaluator ladder, judge calibration, subgroup masking | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D4.2 | Sept 2026 |
| Toy agreement and cost arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Human label disagreement rate | Not in source | -- | -- |

:::takeaway
The exam's D4.2 trap reports one average. The right answer splits
it by segment and calibrates the grader.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Set measured the easy day | 200 clean, 94% | Mixed set, edge 55% | d42-f01 | SVG | Original |
| u02 | Metrics carry over | -- | Prerequisite table | d42-f02 | Table | V2-D4.1 |
| u03 | Five drawers, three rungs | One clean drawer | Five drawers, ladder | d42-f03 | SVG | Original |
| u04 | Average buries a segment | Average 94% | 0.8 x 95 + 0.2 x 55 = 87 | d42-f04 | SVG | Original |
| u05 | Ladder prices grading | $250 per run | $25.60 per run | d42-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches calibration | d42-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d42-f06 | Table | S03, S04 |
| u07 | Set decays silently | Frozen v3 | Refresh cadence, v4 | d42-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d42-f08 | Table | Original |
| u09 | Constraints decide the set | -- | Constraint verdict table | d42-f09 | Table | Original |
| u10 | All-human valid but inferior | -- | Validity vs inferiority table | d42-f10 | Table | Original |
| u11 | Tiny set favors all-human | -- | Counterfactual table | d42-f11 | Table | Original |
| u12 | Drawers and rungs from memory | Blank recall card | Filled from memory | d42-f12 | ASCII | Original |
| u13 | Transfer to loan agent | Unseen question | Key in Stage 8 | d42-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d42-f14 | Table | Mixed |
