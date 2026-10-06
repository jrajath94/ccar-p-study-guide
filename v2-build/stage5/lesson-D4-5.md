# Lesson D4-5: optimization under floors (V2-D4.5)

## 1. Problem this lesson solves

A support agent is too slow and too expensive. The team removes the
reranker, shortens the context, and adds a cache. Latency falls.
Cost falls. Task success falls too, from 92% to 81%, and safety
reviews fail. The optimization had no floors.

Optimization without held floors is demolition. Every cut needs two
numbers: what it saves, and what it must not break.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Cuts with no floors</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Faster. Cheaper. Broken.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="104" y="173" font-size="12" text-anchor="middle" fill="#1B2838">fast</text>
<rect x="180" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="240" y="173" font-size="12" text-anchor="middle" fill="#1B2838">cheap</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Success: 92 to 81.</text>
<text x="44" y="232" font-size="13" fill="#5C6B7A">Safety: failed.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="480" y="173" font-size="12" text-anchor="middle" fill="#1B2838">fast</text>
<rect x="556" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="616" y="173" font-size="12" text-anchor="middle" fill="#1B2838">cheap</text>
<rect x="420" y="200" width="256" height="32" rx="8" fill="#F6E7A8"/>
<text x="548" y="221" font-size="12" text-anchor="middle" fill="#1B2838">floors held: 90%, safe</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Every cut proved its floor.</text>
<defs><marker id="m-d45-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d45-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">hold the floors</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Speed and cost are goals. Floors are the lines the goals cannot cross.</text>
</svg>
<figcaption>Shell 3. Floorless cuts become floored cuts. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D2-4 gives the context budget. Lesson D2-5 gives the cache
break-even. Lesson D3-3 gives per-stage latency receipts. This lesson
combines them under floors.

| Foundation | What it gives this lesson |
|---|---|
| V2-D2.4 context | Oversized context is the first cut |
| V2-D2.5 caching | Cache math: write 1.25x, read 0.1x |
| V2-D3.3 stage receipts | Price per stage in ms per accuracy point |

## 3. Mental model

Five levers, one order. Measure per stage first. Cut the oversized
context. Cache the stable prefix. Route easy work to cheaper tiers.
Eliminate calls that buy nothing. Each lever gets a receipt: latency
saved, cost saved, quality held.

Two floors never move: the quality floor and the safety floor. Every
cut is verified against both before it ships. p95 and p99 are the
latency numbers that matter. Users feel the tail.

Streaming is a special case. It moves the first token sooner. It
does not shorten the completion. Perceived responsiveness rises.
Completion time stays. The exam tests this split.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Streaming moves the first token</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">First token at 0.5 s. Completion at 9 s. Two different numbers.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">wait 9 s, answer lands</text>
<text x="44" y="208" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="172" y="233" font-size="13" text-anchor="middle" fill="#1B2838">completion: 9 s</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">User stares at nothing.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">first token: 0.5 s</text>
<rect x="420" y="208" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="548" y="233" font-size="13" text-anchor="middle" fill="#1B2838">completion: 9 s</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Feels fast. Takes the same.</text>
<defs><marker id="m-d45-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d45-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">stream the start</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Streaming changes perceived latency, not completion latency.</text>
</svg>
<figcaption>Shell 3. A silent wait becomes an early first token. Source: original toy.</figcaption>
</figure>

:::takeaway
Measure per stage. Cut in order: context, cache, routing, calls.
Hold the quality and safety floors on every cut. Streaming buys
perception, not completion.
:::

## 4. Causal mechanism

The levers in order. First, measure each stage at p50, p95, p99.
The slowest stage with the thinnest receipt is the first suspect.
Second, shrink the oversized context: the context budget from
Lesson D2-4 decides what the current turn actually needs. Third,
cache the stable prefix: Lesson D2-5's break-even math decides if
the hit rate pays. Fourth, route: easy tickets to the cheap tier,
hard tickets to the strong tier, with a quality floor per route.
Fifth, eliminate calls: rerank, extra tools, and verification
passes that ablation shows buy nothing.

Each cut is verified against the floors before it ships. The
quality floor is the task-success threshold from Lesson D4-1. The
safety floor is the zero-incident guard. A cut that breaks either
is rolled back, no matter what it saves.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five levers, one order</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Measure, context, cache, route, eliminate. Floors checked on each.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">cuts in any order</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No measurement.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Floors unchecked.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Success: 81.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="32" rx="999" fill="#E7F1F8"/>
<text x="460" y="169" font-size="11" text-anchor="middle" fill="#1B2838">measure</text>
<rect x="508" y="148" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="11" text-anchor="middle" fill="#1B2838">context</text>
<rect x="596" y="148" width="80" height="32" rx="999" fill="#F6E7A8"/>
<text x="636" y="169" font-size="11" text-anchor="middle" fill="#1B2838">cache</text>
<rect x="464" y="188" width="80" height="32" rx="999" fill="#F4E6D4"/>
<text x="504" y="209" font-size="11" text-anchor="middle" fill="#1B2838">route</text>
<rect x="552" y="188" width="80" height="32" rx="999" fill="#E6E2DA"/>
<text x="592" y="209" font-size="11" text-anchor="middle" fill="#1B2838">cut</text>
<text x="420" y="236" width="256" height="32" rx="8" fill="#F6E7A8"/>
<text x="548" y="257" font-size="12" text-anchor="middle" fill="#1B2838">floors: 90%, zero incidents</text>
<text x="420" y="284" font-size="13" fill="#5C6B7A">Success: 91. Floors hold.</text>
<defs><marker id="m-d45-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d45-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">order the levers</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Order matters. Each lever proves its floors before the next moves.</text>
</svg>
<figcaption>Shell 3. Random cuts become ordered levers with floors. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: refund agent. 50,000 calls per day. Current p95: 2,900 ms
against a 2,000 ms SLA. Task success 93% against a 90% floor.
Monthly cost $10,800 (from the Lesson D1-2 pipeline budget).

Stage p95: retrieval 200 ms, rerank 300 ms, model 1,400 ms,
assembly 100 ms. Measured tail: 2,900 ms from retries and queues.

Lever 1, context: cut oversized retrieval from 5 chunks to 3.
Saves 150 ms. Quality holds at 93%.

Lever 2, cache: stable prefix 8,000 tokens at 90% hit rate.
Daily saving from Lesson D2-5 math: $138 per day, times 30 =
$4,140 per month.

Lever 3, route: 60% of tickets are easy. Route them to the cheap
tier at half the model cost. Model spend was 60% of $10,800 =
$6,480. Easy tickets: 0.60 x $6,480 = $3,888. Half of that =
$1,944 saved per month. Quality on easy tickets: 95%, floor holds.

Lever 4, eliminate: rerank ablation shows 0.4% gain for 300 ms.
Cut it. p95: 2,900 - 300 - 150 = 2,450 ms. Still over the SLA,
so the retry fix from Lesson D3-3 follows. Honest math, staged.

Total monthly saving: $4,140 + $1,944 = $6,084 per month.
Quality: 93% to 92.6%, floor 90% holds. Safety: zero incidents,
floor holds.

Mini question: "p95 is 2,900 ms against a 2,000 ms SLA. Success
is 93% against a 90% floor. Which cut ships first? A) Cut the
context and the cache together. B) Measure per stage, then cut
the reranker with the thinnest receipt, verifying floors. C)
Route everything to the cheapest tier."

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
| STEP 1 | Optimization under constraints |
| STEP 2 | Operation: live system, binding SLA |
| STEP 3 | Restore the SLA, hold the floors |
| STEP 4 | p95 2,900 vs 2,000 SLA. Floor 90% |
| STEP 5 | Pipeline stage configuration |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates order: unmeasured cuts. C violates the floor: cheap tier on hard tickets risks quality |
| STEP 8 | B measures first, cuts the thinnest receipt, checks floors |
| STEP 9 | B needs the ablation receipts and the floor thresholds owned |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive discipline is measured cuts with held
floors, and only B follows it. The scenario asks for the SLA, and
the answer is order, not volume.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The levers price themselves</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Cache $4,140 plus routing $1,944 = $6,084 a month.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$10,800 / month</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">No cache.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">One tier for all.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">p95: 2,900 ms.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$4,716 / month</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Cache: -$4,140.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Routing: -$1,944.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">$10,800 - $6,084 = $4,716.</text>
<defs><marker id="m-d45-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d45-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">apply the levers</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Measured levers cut the bill 56% with the floors held.</text>
</svg>
<figcaption>Shell 4. Two levers turn $10,800 a month into $4,716. Source: original toy.</figcaption>
</figure>

:::takeaway
Optimization is measured cuts with held floors. Unmeasured cuts
are demolition.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| p95, p99 per stage | Application metrics | V2-D4.5 tail latency |
| Prompt caching | Platform feature, Lesson D2-5 | V2-D4.5 cache lever |
| Tier routing | App router, Lesson D2-1 | V2-D4.5 routing lever |
| Streaming | API stream parameter | V2-D4.5 perceived latency |
| Quality and safety floors | Eval plan, Lesson D4-1 | V2-D4.5 held floors |

## 7. Current limitations

Routing misroutes: an easy ticket that is actually hard gets the
cheap tier and a bad answer. The router needs its own eval.
Caching hides latency: a cache miss at peak hour restores the old
tail. Context cuts can starve the model: too little context and
quality falls off a cliff, not a slope. Streaming masks slow
systems: the user reads words while the total time stays bad.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The router can misroute</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">A hard ticket on the cheap tier is a cheap wrong answer.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">router: 60% easy</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Router unevaluated.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Hard tickets slip through.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">router has its own eval</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Misroute rate measured.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Escalation on doubt.</text>
<defs><marker id="m-d45-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d45-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">eval the router</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The router is a decision. Decisions get evals.</text>
</svg>
<figcaption>Shell 3. An unevaluated router becomes an evaluated router. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Bigger tier everywhere | One strong slow call | Accuracy floor unmet, SLA loose |
| Floorless cuts | Fast and cheap, broken | Never in production |
| Ordered levers with floors (this lesson) | Measured savings | Production optimization |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| SLA binds, floor holds | Cut the thinnest receipt first |
| Quality floor unmet | No cuts. Fix quality first |
| Context dominates cost | Shrink context before caching |
| Cheap tier risks the floor | Route only what the router proves easy |

## 10. Valid-but-inferior option

Streaming alone as the latency fix. Valid: perceived responsiveness
rises, users feel the system is faster. Inferior for the SLA: the
completion time is unchanged. On the toy, p95 stays 2,900 ms while
the first token arrives at 0.5 s. The SLA measures completion.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Streaming only | Feels faster | p95 completion unchanged |

## 11. Counterfactual where the alternative wins

Chat product. Users read as the answer streams. The business
metric is perceived responsiveness, measured by time to first
token. Streaming wins: the goal is the feeling, and the feeling
arrives at 0.5 s.

| Situation | Winner | Why |
|---|---|---|
| Perception is the metric | Streaming | First token is the goal |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The levers in order: measure, ______, cache,
   ______, eliminate.
2. The two floors: ______ and ______.
3. Streaming improves ______ latency, not
   ______ latency.
4. Two levers save $______ per month on the toy.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A document QA agent has p99 of 12 seconds against a
6-second SLA. Stage p99: retrieval 1 s, model 9 s,
assembly 2 s. The quality floor holds at 91%.
Name the lever, the cut, and the floor check.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D4.5 tests per-stage measurement, context, caching, routing, call elimination, p95/p99, floors, streaming | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D4.5 | Sept 2026 |
| Toy lever arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Pipeline budget $10,800 per month | Original toy, taught in Lesson D1-2 | This build | Oct 6, 2026 |

:::takeaway
The exam's D4.5 trap offers streaming or a bigger lever count.
The scenario asks for the SLA with floors. Pick the measured cut.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Cuts with no floors | Fast, cheap, broken | Floored cuts | d45-f01 | SVG | Original |
| u02 | Context, cache, receipts carry over | -- | Prerequisite table | d45-f02 | Table | V2-D2.4, V2-D2.5, V2-D3.3 |
| u03 | Streaming moves the first token | Silent 9 s wait | First token at 0.5 s | d45-f03 | SVG | Original |
| u04 | Five levers, one order | Random cuts | Ordered levers with floors | d45-f04 | SVG | Original |
| u05 | Levers price themselves | $10,800 per month | $4,716 per month | d45-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B measures and holds floors | d45-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d45-f06 | Table | S03, S04 |
| u07 | Router can misroute | Unevaluated router | Router eval, escalation | d45-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d45-f08 | Table | Original |
| u09 | Constraints decide the cut | -- | Constraint verdict table | d45-f09 | Table | Original |
| u10 | Streaming only valid but inferior | -- | Validity vs inferiority table | d45-f10 | Table | Original |
| u11 | Perception favors streaming | -- | Counterfactual table | d45-f11 | Table | Original |
| u12 | Lever facts from memory | Blank recall card | Filled from memory | d45-f12 | ASCII | Original |
| u13 | Transfer to document QA | Unseen question | Key in Stage 8 | d45-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d45-f14 | Table | Mixed |
