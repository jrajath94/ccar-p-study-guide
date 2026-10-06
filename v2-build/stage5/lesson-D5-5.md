# Lesson D5-5: responsible AI (V2-D5.5)

## 1. Problem this lesson solves

A loan-screening agent scores 94% correct overall. It ships. A
review finds applicants from one neighborhood score 68% correct
while everyone else scores 96%. The 94% was a weighted lie: the
small group drowned in the large one. The team never looked.

Aggregate metrics hide group harm. Six duties name what the team
owes: bias checked, fairness measured, transparency offered,
explainability provided, accountability assigned, traceability
kept. This lesson makes them architectural, not aspirational.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">94% hid 68%</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One number. Two realities.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">overall: 94%</text>
<rect x="44" y="200" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">groups: unmeasured</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">Ship approved.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="480" y="173" font-size="13" text-anchor="middle" fill="#1B2838">group A: 96%</text>
<rect x="556" y="148" width="120" height="40" rx="8" fill="#F3D4D8"/>
<text x="616" y="173" font-size="13" text-anchor="middle" fill="#1B2838">group B: 68%</text>
<text x="420" y="208" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="233" font-size="13" text-anchor="middle" fill="#1B2838">per-group floor set</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Ship blocked until B clears.</text>
<defs><marker id="m-d55-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d55-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">split the score</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Evaluate across subgroups. The aggregate is not the story.</text>
</svg>
<figcaption>Shell 3. An aggregate score becomes per-group scores with a floor. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A gives the metric chain. Lesson D4-2 gives subgroup
reporting. This lesson turns the subgroup report into duties.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 business | Metric, threshold, owner per requirement |
| V2-D4.2 datasets | Per-segment reporting |

## 3. Mental model

Six duties, plain form. Bias: the system must not systematically
favor or harm a group. Fairness: the same standard applies across
groups, measured, not assumed. Transparency: the affected person
knows a system decided and what it considered. Explainability: the
decision can be stated in reasons a person can check. Accountability:
a named owner answers for each decision class. Traceability: the
decision's inputs, model version, and data are recorded and
replayable.

The exam's core move: evaluate across subgroups, not aggregate
only. Per-group thresholds. Per-group reports. A floor per group
that matters.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Six duties, one page</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each duty is an artifact, not an aspiration.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="13" text-anchor="middle" fill="#1B2838">"we are fair"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No artifacts.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No owner.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No replay.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="32" rx="999" fill="#E7F1F8"/>
<text x="480" y="169" font-size="12" text-anchor="middle" fill="#1B2838">bias report</text>
<rect x="548" y="148" width="120" height="32" rx="999" fill="#F6E7A8"/>
<text x="608" y="169" font-size="12" text-anchor="middle" fill="#1B2838">floors</text>
<rect x="420" y="188" width="120" height="32" rx="999" fill="#E7F4EF"/>
<text x="480" y="209" font-size="12" text-anchor="middle" fill="#1B2838">reasons</text>
<rect x="548" y="188" width="120" height="32" rx="999" fill="#F4E6D4"/>
<text x="608" y="209" font-size="12" text-anchor="middle" fill="#1B2838">owner</text>
<rect x="476" y="228" width="144" height="32" rx="999" fill="#E6E2DA"/>
<text x="548" y="249" font-size="12" text-anchor="middle" fill="#1B2838">trace log</text>
<text x="420" y="276" font-size="13" fill="#5C6B7A">Duties become artifacts.</text>
<defs><marker id="m-d55-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d55-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">build the artifacts</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A duty without an artifact is a slogan. The exam tests the artifact.</text>
</svg>
<figcaption>Shell 3. A bare fairness claim becomes five named artifacts. Source: original toy.</figcaption>
</figure>

:::takeaway
Per-group metrics, per-group floors, recorded reasons, a named
owner, a replayable trace. That is the responsible AI page.
:::

## 4. Causal mechanism

Bias enters through data, the prompt, or the feedback loop. Data:
the training and retrieval corpus underrepresents a group. Prompt:
the template encodes an assumption about the user. Feedback loop:
the system's own decisions become tomorrow's training data, and
the gap compounds.

The mechanism that stops it is measurement per group. Split the
eval set by the groups that matter. Report the primary metric per
group. Set a floor per group. When a group misses its floor, the
build stops. The fix is upstream: rebalance the data, fix the
retrieval coverage, or change the decision flow. Never fix it by
tuning the aggregate.

Transparency and explainability are outputs. The applicant sees:
a system screened your application, it weighed income stability
and debt ratio, the decision and the reasons are recorded. The
reasons must be real: the trace shows which inputs the decision
used. A generated explanation that invents reasons is worse than
none.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The loop compounds the gap</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Today's decisions train tomorrow's model. The gap grows.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">gap: 28 points</text>
<rect x="44" y="200" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">decisions train v2</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Gap: 28, then 34.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">floor blocks the ship</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">rebalance upstream</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Gap: 28, then 12.</text>
<defs><marker id="m-d55-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d55-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">break the loop</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The floor stops the compounding before the next version learns the gap.</text>
</svg>
<figcaption>Shell 3. A compounding gap becomes a floored and rebalanced gap. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: loan-screening agent. 1,000 applications. Group A: 800
applicants. Group B: 200 applicants.

Before: overall correct 940 of 1,000 = 94%. The team ships.

After: split the score. Group A: 768 of 800 = 96%. Group B:
136 of 200 = 68%. Weighted check: 0.8 x 96 + 0.2 x 68 =
76.8 + 13.6 = 90.4. The 94% was wrong, because the toy's
earlier aggregate hid a different mix. The honest aggregate is
90.4%, and group B sits at 68%.

The exam arithmetic: 96 - 68 = 28 points of gap. Per-group floor:
90%. Group B misses by 22 points. Ship blocked. Upstream fix:
the retrieval corpus lacked group B's document types. Rebalance.
New scores: group A 95%, group B 92%. Gap: 3 points. Ship.

Transparency artifact on the same toy. Each applicant receives:
the decision, the two weighed factors, the model version, and a
reference id. The trace holds the inputs. The owner is the
lending lead. The quarterly bias report re-runs the split.

Mini question: "A screening agent scores 94% overall. Group B,
20% of applicants, scores 68%. Which action fits? A) Ship: the
overall exceeds 90%. B) Block the ship, set a per-group floor,
and fix the upstream data gap. C) Tune the model for a higher
overall."

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
| STEP 1 | Decision: ship or block on a group gap |
| STEP 2 | Preproduction: the launch gate is open |
| STEP 3 | Fair decisions across groups |
| STEP 4 | Group B at 68%. Floor 90%. Gap 28 points |
| STEP 5 | Evaluation and governance layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the per-group floor. C tunes the aggregate, not the gap |
| STEP 8 | B blocks, floors, and fixes upstream |
| STEP 9 | B needs the group definitions and the floor owner agreed before launch |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the 28-point gap against a
per-group floor, and only B acts on it. The scenario names the
group score, and the answer is the group, not the aggregate.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The gap prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">800 at 96%. 200 at 68%. Weighted: 90.4%.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">claimed: 94%</text>
<rect x="44" y="208" width="256" height="48" rx="8" fill="#E6E2DA"/>
<text x="172" y="237" font-size="14" text-anchor="middle" fill="#1B2838">gap: 28 points</text>
<text x="44" y="280" font-size="13" fill="#5C6B7A">0.8 x 96 + 0.2 x 68 = 90.4.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">group B: 92%</text>
<rect x="420" y="208" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="237" font-size="14" text-anchor="middle" fill="#1B2838">gap: 3 points</text>
<text x="420" y="280" font-size="13" fill="#5C6B7A">Floor 90%: both clear.</text>
<defs><marker id="m-d55-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d55-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fix upstream</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Upstream data fixes move the group score. Aggregate tuning does not.</text>
</svg>
<figcaption>Shell 4. A 28-point gap becomes a 3-point gap with arithmetic. Source: original toy.</figcaption>
</figure>

:::takeaway
The group score is the metric. The aggregate is the footnote.
Fix the gap upstream, in the data.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Per-group eval split | Eval setup config | V2-D5.5 subgroup evaluation |
| Decision trace | Trace backend, Lesson D3-4 | V2-D5.5 traceability |
| Quarterly bias report | Governance process | V2-D5.5 accountability |
| Applicant notice | Product surface | V2-D5.5 transparency |

## 7. Current limitations

Group definitions are contested: who decides the groups, and the
exam will name them in the scenario. Small groups mean noisy
scores: 20 samples cannot hold a 90% floor with confidence, so
report the uncertainty. Explanations can mislead: a fluent reason
that the trace does not support is a new harm. Fairness has
competing definitions: equal rates versus equal accuracy, and the
scenario picks one.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Small groups, noisy scores</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Twenty samples cannot hold a floor. Say so.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">n = 20, floor 90%</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">One miss: 95%.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Noise decides the ship.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">report the interval</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">68% plus or minus wide.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Grow the sample first.</text>
<defs><marker id="m-d55-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d55-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">name the noise</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Report the uncertainty. Grow the sample before the floor binds.</text>
</svg>
<figcaption>Shell 3. A noisy small-group score gains a reported interval. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Aggregate only | One number | Internal tool, no affected groups |
| Fairness statement | Words, no artifacts | Nothing production |
| Six duties (this lesson) | Artifacts per duty | Decisions that affect people |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Decision affects a group | Per-group metric, per-group floor |
| Applicant is affected | Transparency notice plus real reasons |
| Audit must replay the decision | Traceability: inputs, version, data |
| Small group, noisy score | Report the interval. Grow the sample |

## 10. Valid-but-inferior option

Tune the model for a higher overall. Valid: a better model can
lift every group, and the aggregate rises. Inferior for the gap:
on the toy the aggregate moved 94 to 95 while group B stayed at
68. The gap is a data problem, not a model problem.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Tune the aggregate | Lifts all groups sometimes | Gap 28 points, unchanged |

## 11. Counterfactual where the alternative wins

Internal code-review bot. No applicant, no affected group, no
external decision. Aggregate only wins: there is no group to
protect, and the duties have no subject.

| Situation | Winner | Why |
|---|---|---|
| No affected people | Aggregate only | No group to protect |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The six duties: bias, fairness, ______,
   explainability, ______, traceability.
2. Group B: 200 of 1,000, score ______%.
3. Weighted honest aggregate: ______%.
4. The gap closes ______, in the data.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A recruiter agent screens resumes. Women score 12 points
lower than men on the agent's "culture fit" rubric.
The overall pass rate meets the target.
Name the duty, the report, and the upstream fix.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D5.5 tests bias, fairness, transparency, explainability, accountability, traceability, subgroup evaluation | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D5.5 | Sept 2026 |
| Toy subgroup arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Feedback-loop compounding rate | Toy illustration, not measured | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D5.5 trap ships on the aggregate. The scenario names
a group. The answer is the group floor.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | 94% hid 68% | Overall 94% | Group B 68%, floor set | d55-f01 | SVG | Original |
| u02 | Chain and segments carry over | -- | Prerequisite table | d55-f02 | Table | §7.4, V2-D4.2 |
| u03 | Six duties, one page | Bare claim | Five artifacts | d55-f03 | SVG | Original |
| u04 | Loop compounds the gap | Gap 28, then 34 | Floor blocks, gap 12 | d55-f04 | SVG | Original |
| u05 | Gap prices itself | Claimed 94%, gap 28 | Group B 92%, gap 3 | d55-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B blocks and fixes upstream | d55-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d55-f06 | Table | S03, S04 |
| u07 | Small groups, noisy scores | n = 20 floor | Report interval | d55-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d55-f08 | Table | Original |
| u09 | Constraints decide the duty | -- | Constraint verdict table | d55-f09 | Table | Original |
| u10 | Tune-aggregate valid but inferior | -- | Validity vs inferiority table | d55-f10 | Table | Original |
| u11 | Internal bot favors aggregate | -- | Counterfactual table | d55-f11 | Table | Original |
| u12 | Duty facts from memory | Blank recall card | Filled from memory | d55-f12 | ASCII | Original |
| u13 | Transfer to recruiter agent | Unseen question | Key in Stage 8 | d55-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d55-f14 | Table | Mixed |
