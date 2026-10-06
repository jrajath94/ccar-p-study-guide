# Lesson D4-3: A/B testing and iteration (V2-D4.3)

## 1. Problem this lesson solves

A team ships a new prompt to all users on a Friday. Task success
moves from 80% to 81%. The team celebrates. On Monday it falls to
79%. Nobody knows whether the prompt helped, hurt, or did nothing.
There was no control group. There was no hypothesis. There was only
a deploy and a feeling.

An A/B test is a comparison with a control. Without it, every change
is a guess wearing data as a costume.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A guess in a data costume</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">No control. No hypothesis. The weekend moved, not the prompt.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">100% get the new prompt</text>
<rect x="44" y="200" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">80 to 81 to 79: noise</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">No one learns anything.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="8" fill="#E7F1F8"/>
<text x="480" y="173" font-size="13" text-anchor="middle" fill="#1B2838">A: old</text>
<rect x="556" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="616" y="173" font-size="13" text-anchor="middle" fill="#1B2838">B: new</text>
<text x="420" y="200" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">hypothesis first</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">The test answers one question.</text>
<defs><marker id="m-d43-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d43-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">add the control</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A change without a control teaches nothing.</text>
</svg>
<figcaption>Shell 3. A full deploy becomes a controlled A/B test. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D4-2 gives the dataset and the primary metric. The A/B test
uses the same primary metric as its scoreboard.

| Foundation | What it gives this lesson |
|---|---|
| V2-D4.2 datasets | Primary metric, holdout discipline |

## 3. Mental model

An A/B test is a bet written before the cards are dealt. The bet has
four parts. The hypothesis is falsifiable: "the new prompt raises
task success by at least 3 points on refund tickets." The primary
metric is named first: task success, not fluency, not vibes. The
assignment is consistent: a user or ticket lands in A or B and stays
there. The sample size is fixed before launch: enough traffic to
detect the claimed lift.

Two kinds of significance. Statistical significance says the
difference is probably real. Business significance says the
difference is worth the cost of the switch. A test can pass the
first and fail the second.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The bet before the cards</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Four parts, written first. Significance is not one thing.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="13" text-anchor="middle" fill="#1B2838">"new prompt feels better"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No metric named.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No bet written.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Any result fits.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#F6E7A8"/>
<text x="548" y="173" font-size="12" text-anchor="middle" fill="#1B2838">lift at least 3 points</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="12" text-anchor="middle" fill="#1B2838">primary: task success</text>
<rect x="420" y="244" width="120" height="32" rx="999" fill="#E7F4EF"/>
<text x="480" y="265" font-size="12" text-anchor="middle" fill="#1B2838">A: old</text>
<rect x="548" y="244" width="120" height="32" rx="999" fill="#E7F4EF"/>
<text x="608" y="265" font-size="12" text-anchor="middle" fill="#1B2838">B: new</text>
<defs><marker id="m-d43-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d43-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">write the bet</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Hypothesis, metric, assignment, size. Written first, judged after.</text>
</svg>
<figcaption>Shell 3. A feeling becomes a four-part bet. Source: original toy.</figcaption>
</figure>

:::takeaway
Write the hypothesis, the primary metric, the assignment rule, and
the sample size before launch. Decide the ship rule before you see
the numbers.
:::

## 4. Causal mechanism

Assignment must be consistent: the same user or ticket always lands
in the same arm. Inconsistent assignment contaminates both arms.
Randomize at the right unit: by ticket for a support bot, by user
for a personalized agent. Sample size follows the lift you claim:
a 3-point lift needs fewer samples than a 0.5-point lift. Toy rule
of thumb, stated as assumption: to detect a 5-point lift with a
plus or minus 2.5-point margin, about 1,000 tasks per arm.

Shadow testing is the quiet cousin. The new version runs on logged
traffic or a copy of live traffic. Users never see it. It measures
the primary metric without exposure risk. Use shadow before direct
exposure when the change can harm: new tools, new permissions, new
model tiers. Direct exposure follows only if the shadow run clears
the guard metrics.

Iteration closes the loop. The test answers the hypothesis. Ship,
roll back, or iterate. One change per test. Two changes at once
write a check no one can cash.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Shadow before exposure</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Measure first without users. Expose only after the guards clear.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">direct to 100%</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Users feel the bug first.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Rollback costs trust.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No guard data exists.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">shadow: 5,000 logged tasks</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">guards clear, then 10% live</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Zero users exposed first.</text>
<text x="420" y="276" font-size="13" fill="#5C6B7A">Then measured exposure.</text>
<defs><marker id="m-d43-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d43-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">shadow first</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Harmful changes prove themselves in shadow before they touch a user.</text>
</svg>
<figcaption>Shell 3. Direct exposure becomes shadow then measured exposure. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: refund agent, new prompt candidate. Baseline task success 80%.
Hypothesis: the new prompt raises task success by at least 3 points
on refund tickets. Primary metric: task success. Guard metrics:
safety incidents zero, p95 under 5 seconds.

Sample math (toy assumptions, stated): target lift 3 points, margin
plus or minus 1.5 points. Rule of thumb used here: 1,000 tasks per
arm detects a 5-point lift at plus or minus 2.5. A 3-point lift
needs roughly 2,700 per arm. At 10,000 tasks per day, each arm
fills in under a day with a 50/50 split.

Result: B reaches 83.2%, A stays 80.1%. Lift 3.1 points. Passes
the statistical bar. Business check: the switch costs $50,000 in
migration work. Extra wins per day: 10,000 x 0.031 = 310. Each win
saves $0.40 in handling. Value per day: 310 x $0.40 = $124.
Payback: $50,000 / $124 = 403 days. Business significance fails.
Decision: do not ship. The test was honest. The math said no.

Mini question: "A test shows B beats A by 3.1 points, statistically
significant. The switch costs $50,000 and pays back in 403 days.
Which decision fits? A) Ship, because the lift is significant. B)
Do not ship: significance is statistical, not business. C) Run the
test longer to find a bigger lift."

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
| STEP 1 | Decision: ship or not after a test |
| STEP 2 | Operation: the test finished, the decision is live |
| STEP 3 | Ship only changes worth their cost |
| STEP 4 | Lift 3.1 points. Payback 403 days |
| STEP 5 | Evaluation and decision layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the business-significance rule: real but not worth it |
| STEP 8 | B separates the two significances. C chases a bigger number the test did not promise |
| STEP 9 | B's consequence: keep the old prompt, bank the method |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive split is statistical versus business
significance, and only B applies it. The scenario names the cost,
and the answer is no.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Two significances, one decision</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">+3.1 points. Real. Payback 403 days. Not worth it.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">lift: +3.1, p real</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">80.1 to 83.2.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Statistical: passes.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Ship reflex: yes.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">payback: 403 days</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">310 x $0.40 = $124 / day.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">$50,000 / $124 = 403.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Business: fails. No ship.</text>
<defs><marker id="m-d43-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d43-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">price the lift</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A real lift can still be a bad buy.</text>
</svg>
<figcaption>Shell 4. Statistical significance becomes a priced business decision. Source: original toy.</figcaption>
</figure>

:::takeaway
Statistical significance answers "is it real." Business
significance answers "is it worth it." Ship needs both.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Consistent assignment key | App code: user or ticket id hashed to an arm | V2-D4.3 assignment integrity |
| Logged traffic replay | Eval setup on stored traces | V2-D4.3 shadow testing |
| Guard metric alerts | Monitoring, Lesson D4-6 | V2-D4.3 guardrails during exposure |

## 7. Current limitations

Small traffic means long tests: a 1-point lift needs weeks at low
volume. Novelty effects fade: users react to the new, not the
better. Assignment bugs are silent: a sticky-bucket bug ruins the
test with no error. Peeking at results early inflates false wins.
Not in source: an exact sample-size formula for this course's toy.
The rule of thumb above is a toy assumption, not a formula.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Peeking invents wins</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Stop early and noise looks like a lift.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">peek at day 2: +4</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Noise.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Ship declared.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">read at size: +0.5</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">True lift.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">No ship.</text>
<defs><marker id="m-d43-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d43-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">wait for size</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Read the result at the planned size, not before.</text>
</svg>
<figcaption>Shell 3. Early peeking becomes a sized read. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Ship to all, watch | No control | Tiny team, reversible change, low stakes |
| Shadow only | No user exposure | Risky change, exposure unacceptable |
| Controlled A/B (this lesson) | Hypothesis, control, size | Production change with measurable goal |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Change can harm users or money | Shadow first, then controlled exposure |
| Traffic too small for the claimed lift | Do not test. The test cannot answer |
| Two changes ship together | Split them. One change per test |
| Switch has a real cost | Business significance decides, not p-values |

## 10. Valid-but-inferior option

Ship to everyone and watch the dashboard. Valid: fast, simple, and
fine for reversible low-stakes tweaks. Inferior when the change can
harm: the weekend dip taught nothing, and a harmful change reaches
every user before anyone measures it.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Ship and watch | Fast for trivial tweaks | No control. Harm reaches all |

## 11. Counterfactual where the alternative wins

Typo fix in the help text. One word. No behavior change. A/B
machinery costs more than the change. Ship and watch wins: the
stakes cannot justify the test.

| Situation | Winner | Why |
|---|---|---|
| Trivial text fix | Ship and watch | Test machinery exceeds the stakes |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The four parts of the bet: hypothesis, primary
   metric, ______, sample size.
2. Statistical significance: is it ______.
   Business significance: is it ______.
3. Payback math: $50,000 / $124 = ______ days.
4. One change per ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A checkout agent gets a new refund tool. The change can
double-charge users. Traffic is 50,000 checkouts a day.
Name the exposure order and the two guard metrics that
must clear before live users see it.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D4.3 tests hypothesis, primary metric, assignment, sample size, significance vs business significance, shadow testing | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D4.3 | Sept 2026 |
| Toy sample rule of thumb and payback arithmetic | Original toy, stated assumptions | This lesson | Oct 6, 2026 |
| Exact sample-size formula | Not in source | -- | -- |

:::takeaway
The exam's D4.3 trap ships on a significant p-value. The scenario
names the switch cost. Apply business significance.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Guess in a data costume | 100% deploy, noise | A/B with control | d43-f01 | SVG | Original |
| u02 | Dataset and metric carry over | -- | Prerequisite table | d43-f02 | Table | V2-D4.2 |
| u03 | Bet before the cards | Feeling | Hypothesis, metric, arms | d43-f03 | SVG | Original |
| u04 | Shadow before exposure | Direct to 100% | Shadow, then 10% live | d43-f04 | SVG | Original |
| u05 | Two significances | +3.1, ship reflex | Payback 403 days, no ship | d43-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B applies business significance | d43-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d43-f06 | Table | S03, S04 |
| u07 | Peeking invents wins | Peek at day 2 | Read at planned size | d43-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d43-f08 | Table | Original |
| u09 | Constraints decide the test | -- | Constraint verdict table | d43-f09 | Table | Original |
| u10 | Ship-and-watch valid but inferior | -- | Validity vs inferiority table | d43-f10 | Table | Original |
| u11 | Typo fix favors ship-and-watch | -- | Counterfactual table | d43-f11 | Table | Original |
| u12 | Bet facts from memory | Blank recall card | Filled from memory | d43-f12 | ASCII | Original |
| u13 | Transfer to checkout agent | Unseen question | Key in Stage 8 | d43-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d43-f14 | Table | Mixed |
