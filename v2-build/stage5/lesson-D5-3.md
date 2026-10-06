# Lesson D5-3: human-in-the-loop validation (V2-D5.3)

## 1. Problem this lesson solves

A refund agent auto-approves everything under $5,000. It misfires
once a month. Each misfire costs $4,000. The team adds a human
reviewer on every refund. 10,000 refunds per day. Each review takes
2 minutes. That is 333 reviewer hours per day. The review queue
collapses in a week.

The team swung from zero review to total review. Both ends fail.
Review strength must match the stakes: the consequence, the
reversibility, the uncertainty, the regulation, the money at risk.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Zero review, then total review</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Both ends fail. The stakes set the strength.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="104" y="173" font-size="12" text-anchor="middle" fill="#1B2838">none</text>
<rect x="180" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="240" y="173" font-size="12" text-anchor="middle" fill="#1B2838">all</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">None: $4,000 misfires.</text>
<text x="44" y="232" font-size="13" fill="#5C6B7A">All: 333 h a day.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">stakes set the strength</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">$500+: approve. rest: sample</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Review where it pays.</text>
<defs><marker id="m-d53-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d53-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">key to stakes</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Review strength follows consequence, not anxiety.</text>
</svg>
<figcaption>Shell 3. Binary review becomes stakes-keyed review. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A gives risk classification: impact times reversibility.
Lesson 7-2A gives the approval control. Lesson D5-1 gives the
deterministic gate.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 business | Impact times reversibility sets the stakes |
| §7.2 security | Human approval as a control |

## 3. Mental model

Three review shapes. Pre-action approval: the human approves before
the tool runs. Post-action review: the action runs, the human
reviews after, with rollback ready. Sampled review: the human
reviews a fraction on a schedule.

Five stakes set the shape. Consequence: what breaks if the action
is wrong. Reversibility: can the action be undone. Uncertainty:
how often the model is wrong here. Regulation: does a rule demand
a human. Financial or safety impact: the dollar or harm number.

Two rules govern the reviewers. Reviewers need real decision
context: the retrieved chunks, the tool arguments, the policy.
A reviewer who sees only the answer cannot judge it. And the
model's self-reported confidence is not a calibrated risk score:
"95% confident" from the model is a phrase, not a measurement.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Three shapes, five stakes</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Pre-action, post-action, sampled. The stakes pick the shape.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">reviewer on all</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">333 h a day.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No context given.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Queue collapses.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="36" rx="8" fill="#F3D4D8"/>
<text x="480" y="171" font-size="12" text-anchor="middle" fill="#1B2838">pre: $500+</text>
<rect x="548" y="148" width="120" height="36" rx="8" fill="#F6E7A8"/>
<text x="608" y="171" font-size="12" text-anchor="middle" fill="#1B2838">post: refunds</text>
<rect x="420" y="192" width="120" height="36" rx="8" fill="#E7F1F8"/>
<text x="480" y="215" font-size="12" text-anchor="middle" fill="#1B2838">sample: 2%</text>
<rect x="548" y="192" width="120" height="36" rx="8" fill="#E7F4EF"/>
<text x="608" y="215" font-size="12" text-anchor="middle" fill="#1B2838">context: full</text>
<text x="420" y="244" font-size="13" fill="#5C6B7A">Review where the stakes are.</text>
<defs><marker id="m-d53-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d53-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">shape by stakes</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Irreversible and costly gets pre-action. The rest gets lighter shapes.</text>
</svg>
<figcaption>Shell 3. One review shape becomes three stakes-keyed shapes. Source: original toy.</figcaption>
</figure>

:::takeaway
Match the review shape to the stakes. Give reviewers the full
decision context. Never trust the model's own confidence as a risk
score.
:::

## 4. Causal mechanism

Pre-action approval fits irreversible, high-consequence actions:
refunds over $500, account closures, data deletion. The human sees
the proposal, the chunks behind it, and the policy. The action
waits. The cost is latency and reviewer hours.

Post-action review fits reversible actions with audit needs: small
refunds, content publishes. The action runs. The reviewer checks a
sample after. Rollback must be real: a reviewed-and-wrong action
that cannot be undone was pre-action all along.

Sampled review fits high-volume, low-stakes work: 10,000 tickets
a day. The reviewer sees 2%. The sample must be random, not the
easy 2%. The sample rate follows the error rate: more errors,
bigger sample.

The reviewer-context rule is causal, not decorative. A reviewer
shown only the answer approves the fluent wrong answer. The same
reviewer shown the retrieved chunks catches the missing citation.
Context is what makes the review real.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Confidence is a phrase, not a score</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The model says 95%. Measured correctness says 70%. Trust the measure.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">"95% confident"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Auto-approve on the phrase.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Measured: 70% correct.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Misfires ship.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">calibrated rate: 70%</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">Review keyed to the measure.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">High-stakes: pre-action.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">The phrase is ignored.</text>
<defs><marker id="m-d53-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d53-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">calibrate, not trust</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Self-reported confidence is decoration. Measured rates decide.</text>
</svg>
<figcaption>Shell 3. A trusted confidence phrase becomes a measured correctness rate. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: refund agent. 10,000 refunds per day. 5% are over $500.
Error rate on auto-approved refunds: 0.5%. Average misfire cost:
$4,000.

Option A, review all: 10,000 x 2 minutes = 20,000 minutes =
333 hours per day. At $40 per reviewer hour: 333 x $40 = $13,320
per day. The queue collapses.

Option B, stakes-keyed: pre-action approval on the 5% over $500.
500 x 2 minutes = 1,000 minutes = 16.7 hours per day. Cost:
16.7 x $40 = $668 per day. Sampled review at 2% on the rest:
9,500 x 0.02 = 190 reviews x 2 minutes = 380 minutes = 6.3
hours. Cost: 6.3 x $40 = $252 per day. Total: $668 + $252 =
$920 per day.

Loss math: auto-approved misfires without review: 10,000 x
0.005 x $4,000 = $200,000 per day in the worst telling. With
pre-action on the costly 5%: the 500 big refunds get real
review. The 9,500 small ones carry bounded loss.

Reviewers get the full context: the ticket, the retrieved policy
chunks, the tool arguments, the amount. A reviewer without the
chunks approved 60% of the bad refunds in the toy's pilot. With
the chunks: 10%.

Mini question: "10,000 refunds per day. 5% exceed $500. Review
costs 2 minutes each. Which review plan fits? A) Review every
refund. B) Pre-action approval over $500, sampled review on the
rest, full context for reviewers. C) Auto-approve all and rely on
the model's confidence."

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
| STEP 1 | Architecture of the review plan |
| STEP 2 | Design: review strength is unassigned |
| STEP 3 | Catch costly errors at a payable review cost |
| STEP 4 | 10,000 per day. 5% high stakes. 2 minutes per review |
| STEP 5 | Human-in-the-loop layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates cost: 333 hours per day. C violates the stakes: confidence is uncalibrated |
| STEP 8 | B keys review to the stakes and gives reviewers context |
| STEP 9 | B needs the $500 line, the sample rate, and the context bundle owned |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive split is stakes-keyed review with real
context, and only B provides it. The scenario names the volume,
and the answer is proportion, not totality.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Review workload prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">10,000 refunds a day. 2 minutes a review. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$13,320 / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">10,000 x 2 = 20,000 min.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">20,000 / 60 = 333 h.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">333 x $40 = $13,320.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$920 / day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Pre-action: $668.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Sampled: $252.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Total: $668 + $252 = $920.</text>
<defs><marker id="m-d53-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d53-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">key to stakes</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Stakes-keyed review costs 93% less and catches the costly errors.</text>
</svg>
<figcaption>Shell 4. Total review becomes stakes-keyed review with arithmetic. Source: original toy.</figcaption>
</figure>

:::takeaway
Review where the money and the irreversibility are. Sample the
rest. Context makes the review real.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Approval queue | App workflow, pre-action gate | V2-D5.3 pre-action approval |
| Review context bundle | Ticket plus chunks plus tool args | V2-D5.3 real decision context |
| Sample scheduler | Review job on a cadence | V2-D5.3 sampled review |
| Rollback path | Refund reversal procedure | V2-D5.3 post-action viability |

## 7. Current limitations

Reviewers fatigue: the 500th approval of the day gets a glance,
not a review. Rotate reviewers and cap sessions. Review latency
hurts users: pre-action on everything slow makes the product
unusable. Context bundles cost tokens: the full bundle on 500
reviews a day is its own bill. Sampling misses clusters: a new
failure mode can hide between samples until the sample rate
adapts.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The 500th approval gets a glance</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fatigue turns review into rubber stamping.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">one reviewer, 500 a day</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Hour 6: glances.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Stamps replace reviews.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">rotate, cap sessions</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Short shifts.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Stamps stay reviews.</text>
<defs><marker id="m-d53-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d53-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">protect the reviewer</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A tired reviewer is a rubber stamp. Design the shift, not just the queue.</text>
</svg>
<figcaption>Shell 3. A fatigued reviewer becomes a rotated reviewer. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Review everything | Total human gate | Tiny volume, extreme stakes |
| Auto-approve everything | No human | Reversible, low stakes |
| Stakes-keyed review (this lesson) | Shapes by consequence | Production with mixed stakes |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Irreversible or costly action | Pre-action approval with full context |
| Reversible with real rollback | Post-action review |
| High volume, low stakes | Sampled review, random sample |
| Regulation demands a human | Pre-action, named reviewer, logged decision |

## 10. Valid-but-inferior option

Review everything. Valid: catches the most errors, and for tiny
volumes it is the right call. Inferior at 10,000 per day: $13,320
per day, a collapsed queue, and fatigued reviewers who stamp
instead of reading.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Review all | Most errors caught | $13,320 per day. Queue collapses |

## 11. Counterfactual where the alternative wins

Three refunds a day. Each over $10,000. Review everything wins:
the volume is trivial, the stakes are extreme, and no sampling
math can beat a human on every one.

| Situation | Winner | Why |
|---|---|---|
| Tiny volume, extreme stakes | Review all | Trivial cost, maximum catch |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The three shapes: pre-action ______, post-action
   ______, ______ review.
2. The five stakes: consequence, reversibility,
   ______, regulation, ______.
3. Stakes-keyed review costs $______ per day.
4. The model's "95% confident" is a ______, not a ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A content agent publishes articles. A wrong publish is
reversible in one click. Volume is 500 a day. One article
in 200 carries legal risk.
Name the review shape for each class and what the
reviewer must see.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D5.3 tests review keyed to consequence, reversibility, uncertainty, regulation, financial and safety impact, review shapes, reviewer context, confidence not calibrated | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D5.3 | Sept 2026 |
| Toy review workload arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Reviewer context pilot numbers | Toy assumption, stated | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D5.3 trap is a human reviewer everywhere. The
scenario names the volume. The answer is proportion with
context.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Zero review, then total review | None and all | Stakes-keyed | d53-f01 | SVG | Original |
| u02 | Stakes and approval carry over | -- | Prerequisite table | d53-f02 | Table | §7.4, §7.2 |
| u03 | Three shapes, five stakes | Reviewer on all | Three shapes keyed | d53-f03 | SVG | Original |
| u04 | Confidence is a phrase | Trusted phrase | Measured rate | d53-f04 | SVG | Original |
| u05 | Review workload prices itself | $13,320 per day | $920 per day | d53-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B keys to stakes | d53-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d53-f06 | Table | S03, S04 |
| u07 | 500th approval gets a glance | One reviewer, 500 | Rotate, cap sessions | d53-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d53-f08 | Table | Original |
| u09 | Constraints decide the shape | -- | Constraint verdict table | d53-f09 | Table | Original |
| u10 | Review-all valid but inferior | -- | Validity vs inferiority table | d53-f10 | Table | Original |
| u11 | Tiny volume favors review-all | -- | Counterfactual table | d53-f11 | Table | Original |
| u12 | Review facts from memory | Blank recall card | Filled from memory | d53-f12 | ASCII | Original |
| u13 | Transfer to content agent | Unseen question | Key in Stage 8 | d53-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d53-f14 | Table | Mixed |
