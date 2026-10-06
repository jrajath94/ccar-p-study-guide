# Lesson D2-3: prompt techniques (V2-D2.3)

## 1. Problem this lesson solves

A team runs zero-shot on a 12-queue ticket classifier. It hits 80%.
The bar is 95%. The team jumps to fine-tuning: 50,000 labels, a
training run, a new deployment. Nobody tried five examples first.
The ladder was skipped.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The ladder was skipped</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Zero-shot at 80%. Fine-tune next. Five examples never tried.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">zero-shot: 80%</text>
<rect x="44" y="200" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">jump to fine-tune</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">50,000 labels. New deploy.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">few-shot: 94%</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Five examples.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">No training run.</text>
<defs><marker id="m-d23-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d23-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">climb one rung</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Climb one rung at a time. Evals say when to stop.</text>
</svg>
<figcaption>Shell 3. A skipped ladder becomes one climbed rung. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-3A gives the sampler: examples steer sampling, they do not
install facts. Lesson 7-4A gives evals: the bar decides, not taste.

| Foundation | What it gives this lesson |
|---|---|
| §7.3 sampler | Examples shape the distribution |
| §7.4 chain | The technique must pass a measured bar |

## 3. Mental model

Think of a ladder with five rungs. Zero-shot: instructions only.
Few-shot: add positive examples. Rejection examples: add the
near-misses the model must refuse. Explicit reasoning: ask for steps
on hard tasks. Structured output: fix the shape in the contract. The
climb rule: start at zero-shot, climb one rung, re-run evals. Stop at
the simplest technique that passes. Each rung costs tokens, latency,
or both.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Climb one rung at a time</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Evals decide the stop. Taste does not.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">jump to the top</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Fine-tune first.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Reasoning everywhere.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No eval between.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="548" y="169" font-size="12" text-anchor="middle" fill="#1B2838">zero-shot</text>
<rect x="420" y="188" width="256" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="209" font-size="12" text-anchor="middle" fill="#1B2838">few-shot plus rejection: 94%</text>
<rect x="420" y="228" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="548" y="249" font-size="12" text-anchor="middle" fill="#1B2838">explicit reasoning</text>
<rect x="420" y="268" width="256" height="32" rx="999" fill="#E6E2DA"/>
<text x="548" y="289" font-size="12" text-anchor="middle" fill="#1B2838">structured output</text>
<defs><marker id="m-d23-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d23-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">stop at the pass</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The simplest passing rung wins. Higher rungs cost more.</text>
</svg>
<figcaption>Shell 3. A jumped ladder becomes a climbed ladder. Source: original toy.</figcaption>
</figure>

:::takeaway
Simplest technique that passes evals. Rejection examples are the
underused rung: show the model what to refuse, not only what to do.
:::

## 4. Causal mechanism

Examples work by redrawing the boundary. Positive examples show the
shape of a right answer. Rejection examples show the near-miss: the
input that looks right but is wrong, with the refusal attached. Edge
cases pin the corners the zero-shot misses. Explicit reasoning helps
only where steps can be checked: the steps expose the error, they do
not prevent it. Structured output fixes the shape: the contract names
fields, types, and allowed values, and code validates them. Each rung
adds tokens: examples cost input tokens on every call, reasoning
costs output tokens on every call.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Rejection redraws the line</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Positive examples show the shape. Rejection examples show the edge.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">3 positive examples</text>
<rect x="44" y="200" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="229" font-size="14" text-anchor="middle" fill="#1B2838">near-miss accepted</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Boundary too wide.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">plus 2 rejection examples</text>
<rect x="420" y="200" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="229" font-size="14" text-anchor="middle" fill="#1B2838">near-miss refused</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Boundary redrawn.</text>
<defs><marker id="m-d23-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d23-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">add the refusal</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Show the refusal, not only the success. The boundary follows.</text>
</svg>
<figcaption>Shell 4. Positive-only examples gain rejection examples. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: ticket classifier, 200,000 tickets per day. Zero-shot: 82%.
Few-shot with 3 positive and 2 rejection examples per queue: 94% on
the holdout. Bar: 95%. One more edge-case example per queue: 95.4%.
Stop. The ladder ends here.

Technique cost on the Fast tier ($1 in per 1M, S10-S12, Oct 2026): 5
examples x 60 tokens = 300 tokens per call. 300 / 1,000,000 x $1 =
$0.0003 per call. Times 200,000 = $60 per day.

Error math: zero-shot errors 18% of 200,000 = 36,000 per day.
Few-shot errors 6% = 12,000 per day. Fewer errors: 24,000 per day. At
$0.50 per human fix (toy): 24,000 x $0.50 = $12,000 per day saved for
$60 per day in examples.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Examples price themselves</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fast tier. 200K tickets a day. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">zero-shot: 36,000 errors</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">200K x 0.18 = 36,000.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Fix bill: $18,000 / day.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No examples tried.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">few-shot: 12,000 errors</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">300 tokens = $0.0003 / call.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">200K x $0.0003 = $60 / day.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Saves $12,000 / day.</text>
<defs><marker id="m-d23-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d23-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">add five examples</text>
<text x="24" y="352" font-size="15" fill="#1B2838">$60 a day in examples saves $12,000 a day in fixes.</text>
</svg>
<figcaption>Shell 4. Five examples trade $60 per day for $12,000 per day. Source: original toy.</figcaption>
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

Mini question: "A team classifies tickets into 12 queues. Zero-shot hits 80%. The bar is 95%. What is the first technique to try? A) Add explicit reasoning to every call. B) Add 3 positive and 2 rejection examples per queue, then re-run evals. C) Fine-tune a classifier on 50,000 labeled tickets."

| Step | Action on this question |
|---|---|
| STEP 1 | Optimization: pick the first technique |
| STEP 2 | Implementation: prompt iteration |
| STEP 3 | Reach 95% at the lowest cost |
| STEP 4 | Bar 95%, current 80%. Simplest passing technique first |
| STEP 5 | Prompt layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | No hard constraint is violated. All stay in the race |
| STEP 8 | B is the cheapest rung that can pass. A adds reasoning cost before examples are tried. C is the heaviest move |
| STEP 9 | B needs the eval re-run and edge-case coverage in the examples |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive rule is simplest-passing-first, and only B obeys it.

:::takeaway
When a stem asks for the first technique, pick the cheapest rung that
can pass. Fine-tuning and full reasoning are later rungs, not first
moves.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Few-shot examples | Prompt template | V2-D2.3 technique choice |
| Rejection examples | Prompt template | V2-D2.3 boundary control |
| Structured output | Output contract plus code check | V2-D2.2 enforcement, V2-D2.3 shape |
| Explicit reasoning | Prompt instruction | V2-D2.3 hard-task rung |

## 7. Current limitations

Examples overfit: the model learns the five examples, not the task.
Rejection examples can refuse too much: the boundary narrows past the
bar. Reasoning costs output tokens on every call and adds latency.
Examples do not fix bad framing: if the queues overlap, no example
count separates them. And examples age: the task drifts, the examples
stay.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Examples can memorize</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The model learns the five examples. The task moves on.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">94% on the holdout</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Examples frozen.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Task drifts.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">88% on new tickets</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Refresh the examples.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Re-run the evals.</text>
<defs><marker id="m-d23-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d23-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">task drifts</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Examples are a snapshot. Refresh them when the task moves.</text>
</svg>
<figcaption>Shell 3. Frozen examples decay when the task drifts. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Zero-shot only | Instructions only | Simple task, already passing |
| Few-shot ladder (this lesson) | Examples plus evals | Bar unmet, examples can close it |
| Fine-tune | Train on labels | Stable task, labels cheap, style fixed |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Bar unmet, gap small | Climb one rung, re-run evals |
| Near-misses dominate errors | Rejection examples |
| Steps checkable, task hard | Explicit reasoning |
| Output shape must hold | Structured output plus code check |
| Examples cannot close the gap | Fine-tune or reframe the task |

## 10. Valid-but-inferior option

Explicit reasoning on every call. Valid: steps expose errors on hard
tasks. Inferior: on the toy classifier, reasoning adds output tokens
and latency to 200,000 simple calls a day, while five examples already
pass the bar.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Reasoning everywhere | Exposes errors on hard tasks | Token and latency cost on simple calls. Bar already passed |

## 11. Counterfactual where the alternative wins

Multi-step logic puzzle: each step must be right for the next to
work, and a checker verifies each step. Examples alone cannot show
the chain. Explicit reasoning wins: the steps are the product.

| Situation | Winner | Why |
|---|---|---|
| Checkable multi-step logic | Explicit reasoning | Steps are the product, examples cannot show them |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The climb rule: simplest technique that
   ______ evals.
2. Rejection examples show what to ______.
3. Explicit reasoning helps where steps can
   be ______.
4. Five examples cost $______ per day.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A moderation queue flags hate speech. Zero-shot hits 88%.
The bar is 97%. Most errors are sarcastic near-misses.
Name the first rung. Name the second if the first fails.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D2.3 tests zero-shot, few-shot, rejection examples, reasoning, structured outputs | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Tier price $1 in per 1M (Fast) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy classifier arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Simplest-passing-first rule | General principle | Prompt practice | Long-standing |
| Human fix cost $0.50 per ticket | Not in source | -- | -- |

:::takeaway
Techniques are rungs, not virtues. Climb for the bar, stop at the
pass, and let evals call the stop.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | The ladder was skipped | Zero-shot to fine-tune | One rung climbed | d23-f01 | SVG | Original |
| u02 | Sampler and evals carry over | -- | Prerequisite table | d23-f02 | Table | §7.3, §7.4 |
| u03 | Climb one rung at a time | Jump to the top | Ladder with eval stops | d23-f03 | SVG | Original |
| u04 | Rejection redraws the line | Positive only | Plus rejection examples | d23-f04 | SVG | Original |
| u05 | Examples price themselves | 36,000 errors per day | 12,000 errors, $60 per day | d23-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B is simplest passing rung | d23-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d23-f06 | Table | S03, S04 |
| u07 | Examples can memorize | 94% frozen | 88% on drift, refresh | d23-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d23-f08 | Table | Original |
| u09 | Constraints decide the rung | -- | Constraint verdict table | d23-f09 | Table | Original |
| u10 | Reasoning everywhere is valid but inferior | -- | Cost on 200K simple calls | d23-f10 | Table | Original |
| u11 | Logic puzzle favors reasoning | -- | Counterfactual table | d23-f11 | Table | Original |
| u12 | Ladder from memory | Blank recall card | Filled from memory | d23-f12 | ASCII | Original |
| u13 | Transfer to moderation | Unseen question | Key in Stage 8 | d23-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d23-f14 | Table | Mixed |
