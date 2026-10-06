# Lesson D3-3: accuracy-latency trade-offs (V2-D3.3)

## 1. Problem this lesson solves

A support agent misses the mark on 12% of answers. The team adds a
reranker. Then a bigger tier. Then deeper reasoning. Accuracy climbs to
93%. Latency climbs past the 2,000 ms SLA. Users leave before the
answer arrives.

Nobody can say which stage bought the gain. The reranker added 300
ms. Did it add accuracy, or did the bigger tier? The team cannot
answer, because they added everything at once and measured nothing per
stage. Complexity without measurement is a tax with no receipt.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Everything at once, measured never</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Three stages added together. One SLA broken. No receipt per stage.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">p95: 2,900 ms</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">accuracy: 93%</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">SLA: 2,000 ms. Broken.</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Which stage helped? Unknown.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">p95: 1,800 ms</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">accuracy: 92%</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">SLA met. 1% traded.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Each stage has a receipt.</text>
<defs><marker id="m331" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m331)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">measure per stage</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A stage without a measured gain is a tax without a receipt.</text>
</svg>
<figcaption>Shell 3. Per-stage measurement trades 1% accuracy for the SLA. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson 7-4A | Numbers first: fast and accurate mean nothing without thresholds |
| Lesson D2-1 | Routing, cascading, escalation between tiers and their costs |
| Lesson D2-5 | Caching cuts repeated cost |

Stage 5 will deepen measurement. This lesson needs only Lesson 7-4A's
rule: define the SLA and the accuracy floor before you optimize.

## 3. Mental model

Think of latency as a budget pie. Each pipeline stage takes a slice:
retrieval, rerank, model call, reasoning, tool calls, assembly. The
SLA is the whole pie. Think of accuracy as a receipt per slice. Each
stage must show the gain it bought. A slice with no receipt leaves the
pie.

Two more facts complete the model. Tail latency is the pie at its
worst: p95 and p99, not the average. Users feel the tail. And gains
shrink: the first fix buys the most accuracy, the fourth buys the
least. The exam calls this "no unmeasurable complexity." Plain form:
if you cannot measure the gain, you cannot justify the slice.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The budget pie</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">SLA 2,000 ms. Every stage takes a slice. The tail is the pie at its worst.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="36" rx="8" fill="#E6E2DA"/>
<text x="172" y="171" font-size="12" text-anchor="middle" fill="#1B2838">retrieve 200 ms</text>
<rect x="44" y="192" width="256" height="36" rx="8" fill="#E6E2DA"/>
<text x="172" y="215" font-size="12" text-anchor="middle" fill="#1B2838">rerank 300 ms</text>
<rect x="44" y="236" width="256" height="36" rx="8" fill="#E6E2DA"/>
<text x="172" y="259" font-size="12" text-anchor="middle" fill="#1B2838">model 1,400 ms</text>
<text x="44" y="280" font-size="13" fill="#5C6B7A">Sum: 1,900. p95: 2,900.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">retrieve 200 ms</text>
<rect x="420" y="192" width="256" height="36" rx="8" fill="#E7F1F8"/>
<text x="548" y="215" font-size="12" text-anchor="middle" fill="#1B2838">rerank cut: +0.4%</text>
<rect x="420" y="236" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="259" font-size="12" text-anchor="middle" fill="#1B2838">model 1,400 ms</text>
<text x="420" y="280" font-size="13" fill="#5C6B7A">Sum: 1,600. p95: 1,800.</text>
<defs><marker id="m333" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m333)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">cut the thin slice</text>
<text x="24" y="312" font-size="15" fill="#1B2838">300 ms for 0.4% accuracy is a bad trade under a binding SLA.</text>
</svg>
<figcaption>Shell 4. The rerank slice costs 300 ms for a 0.4% gain. Source: original toy.</figcaption>
</figure>

:::takeaway
Budget latency per stage. Receipt accuracy per stage. Optimize to
the SLA. Cut the stage whose receipt cannot cover its slice.
:::

## 4. Causal mechanism

Four questions drive the trade-off. Each maps to a measurement.

Question one: what does each stage cost? Time every stage at p50 and
p95. Retrieval, rerank, each model call, reasoning depth, each tool
call, assembly. The sum at p95 is the number that meets or breaks the
SLA. Averages hide the tail. The tail is what the user feels.

Question two: what does each stage buy? Measure accuracy with the
stage on and off, one stage at a time. This is ablation. Retrieval
added 4%. Rerank added 0.4%. The bigger tier added 2%. Deeper
reasoning added 0.6%. Now each slice has a price per point of
accuracy.

Question three: does the SLA bind? If p95 sits under the SLA, spend
slices on accuracy. If p95 breaks the SLA, cut the thinnest receipt
first. In the toy, rerank costs 300 ms for 0.4%. Cutting it drops p95
from 2,900 to 1,800 and accuracy from 93% to 92.6%. The SLA binds, so
the cut wins.

Question four: is the complexity measurable? A fifth stage that "feels
smarter" but moves no metric is unmeasurable complexity. The exam
rejects it. Plain form: no receipt, no slice.

The mechanism also covers where latency hides. Sequential calls add
up. Parallel calls cost the slowest one. Retries multiply the tail.
Caches cut repeated slices (Lesson D2-5). Routing to a cheaper tier
(Lesson D2-1) shrinks the model slice for easy tasks.

## 5. Minimal worked example

Toy: the support agent. SLA: p95 under 2,000 ms. Accuracy floor: 90%.
Current pipeline per-stage p95: retrieval 200 ms, rerank 300 ms,
model call 1,400 ms, assembly 100 ms. Sum: 2,000. Measured p95:
2,900 ms, because retries and queueing stretch the tail. Accuracy:
93%. Ablation receipts: retrieval 4%, rerank 0.4%, bigger tier 2%,
deeper reasoning 0.6%.

Mini question: "p95 is 2,900 ms against a 2,000 ms SLA. Accuracy is
93% against a 90% floor. Which change best restores the SLA? A) Add
deeper reasoning to lift accuracy to 94%. B) Remove the reranker,
which ablation shows adds 0.4% accuracy for 300 ms. C) Move to a
larger tier for all calls."

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
| STEP 1 | Question asks: optimization. Restore the SLA |
| STEP 2 | Stage: operation. The system is live and breaking its SLA |
| STEP 3 | Objective: p95 under 2,000 ms, accuracy above 90% |
| STEP 4 | Hard constraints: 2,000 ms p95, 90% accuracy floor |
| STEP 5 | Layer: pipeline stage configuration |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | A violates the SLA further: deeper reasoning adds latency. C violates it too: a larger tier is slower |
| STEP 8 | B cuts 300 ms at a 0.4% cost. Accuracy stays at 92.6%, above the floor |
| STEP 9 | B's consequence: edge queries that needed the rerank lose 0.4%. The floor still holds |
| STEP 10 | B alone restores the SLA. A and C move the wrong direction |

Verdict: B. The arithmetic: 2,900 - 300 = 2,600 ms is still over, so
the honest version also needs the retry fix. But among the options,
B is the only one that moves latency down while holding the floor.
93% - 0.4% = 92.6%, above the 90% floor. The scenario asks for the
SLA, and the answer is cut the thin receipt, not add more stages.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Receipt per slice</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each stage shows its price in ms per point of accuracy.</text>
<rect x="24" y="96" width="336" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">STAGE RECEIPTS</text>
<text x="44" y="160" font-size="13" fill="#1B2838">retrieval: 200 ms / 4.0%</text>
<text x="44" y="184" font-size="13" fill="#1B2838">rerank: 300 ms / 0.4%</text>
<text x="44" y="208" font-size="13" fill="#1B2838">bigger tier: 600 ms / 2.0%</text>
<text x="44" y="232" font-size="13" fill="#1B2838">reasoning: 400 ms / 0.6%</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">Worst price: rerank.</text>
<text x="44" y="288" font-size="13" fill="#5C6B7A">300 / 0.4 = 750 ms per point.</text>
<rect x="392" y="96" width="304" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="412" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER THE CUT</text>
<rect x="412" y="148" width="264" height="40" rx="999" fill="#E7F4EF"/>
<text x="544" y="173" font-size="13" text-anchor="middle" fill="#1B2838">rerank removed</text>
<text x="412" y="216" font-size="13" fill="#5C6B7A">p95: 2,900 to 2,600 ms.</text>
<text x="412" y="240" font-size="13" fill="#5C6B7A">Accuracy: 93% to 92.6%.</text>
<text x="412" y="264" font-size="13" fill="#5C6B7A">Floor 90% holds.</text>
<defs><marker id="m335" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="376" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m335)"/>
<text x="24" y="352" font-size="15" fill="#1B2838">Cut the worst price per point first. Hold the floor.</text>
</svg>
<figcaption>Shell 4. Rerank has the worst price: 750 ms per accuracy point. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| p50, p95, p99 latency | Application metrics | V2-D3.3 tail latency |
| Tier routing and cascading | Application router | V2-D3.3 model slice sizing, Lesson D2-1 |
| Prompt caching | Platform feature | V2-D3.3 repeated slice removal, Lesson D2-5 |
| Eval setup with ablation | Test setup | V2-D3.3 per-stage receipts (Stage 5 deepens this) |

## 7. Current limitations

Ablation costs eval runs. Small teams skip it and guess. Tail
latency has many parents: queues, retries, cold starts. The per-stage
timer shows the symptom, not always the cause. Accuracy receipts
depend on the eval set. A thin eval set writes fake receipts, and cached
stages hide their true cost until the cache misses.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Cut the thin receipt (this lesson) | Fewer stages, SLA met | SLA binds, floor holds |
| Parallel calls plus vote | More calls, same wall time | Latency binds, budget allows |
| Bigger tier everywhere | One slow strong call | Accuracy floor unmet, SLA loose |
| Deeper reasoning on hard cases only | Routed depth | Mixed difficulty, Lesson D2-1 routing |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| p95 breaks the SLA | Cut the stage with the worst ms per accuracy point |
| Accuracy below the floor | Add the stage with the best accuracy per ms |
| Stage has no measured gain | Remove it. Unmeasurable complexity loses |
| Latency binds but budget is open | Parallelize before you deepen |
| SLA loose, errors costly | Spend slices on accuracy |

## 10. Valid-but-inferior option

Add deeper reasoning to lift accuracy from 93% to 94%. Valid: the
gain is real and measured. Inferior under this SLA: deeper reasoning
adds 400 ms to a p95 already at 2,900. It moves the binding
constraint the wrong way. The scenario asks for the SLA, not for more
accuracy above the floor.

## 11. Counterfactual where the alternative wins

A medical triage agent. A wrong answer can harm a patient. The SLA is
loose: 10 seconds. The accuracy floor is 99%. Deeper reasoning plus
the bigger tier wins: every slice buys safety, and the pie is large.
The constraint set is inverted, so the winner flips.

| Situation | Winner | Why |
|---|---|---|
| Loose SLA, high error cost | Deeper reasoning, bigger tier | Accuracy buys safety. The pie is large |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The four questions: cost per ______, gain per ______,
   does the ______ bind, is it ______.
2. Users feel the ______, not the average.
3. Rerank: 300 ms / 0.4% = ______ ms per point.
4. No receipt, no ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A translation pipeline has 5 stages. p99 is 4,100 ms
against a 3,000 ms SLA. Ablation shows the grammar-polish
stage adds 700 ms for a 0.2% quality gain. The quality
floor still holds without it.
Name the cut and the two numbers that justify it.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Optimize to SLAs, per-stage latency, tail latency, no unmeasurable complexity | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D3.3 | Sept 2026 |
| Routing, cascading, caching mechanics | Current product behavior, taught in Lessons D2-1 and D2-5 | This build | Oct 6, 2026 |
| Toy arithmetic: p95 sums, ms per point | Original toy, computed above | This lesson | Oct 6, 2026 |
| Ablation as the measurement method | General principle | Evaluation canon | Long-standing |

:::takeaway
The exam's D3.3 trap offers "add a stage" when the SLA is the
binding constraint. The scenario, not the slogan, decides. Under a
binding SLA, the best answer is usually a cut.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Everything at once, measured never | p95 2,900, no receipts | p95 1,800, receipts per stage | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | 7-4A, D2-1, D2-5 |
| u03 | The budget pie | Slices with no prices | Rerank: 300 ms for 0.4% | f03 | SVG | Original |
| u04 | Four questions drive the trade | Guessing | Cost, gain, bind, measurable | f04 | Text | Original |
| u05 | 10-step method picks B | Three options | B: cut the thin receipt | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Ablation and tail limits | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Deeper reasoning inferior here | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Medical triage flips the winner | -- | Counterfactual table | f11 | Table | Original |
| u12 | Four questions from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to translation pipeline | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
