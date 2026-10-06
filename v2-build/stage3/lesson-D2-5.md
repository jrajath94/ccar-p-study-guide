# Lesson D2-5: reuse and prompt caching (V2-D2.5)

## 1. Problem this lesson solves

A team pays for the same 8,000-token system prompt on every call.
10,000 calls a day. The prompt never changes. The bill treats it as
new every time. Nobody told the API what repeats.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Paying full price for repeats</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Same 8,000 tokens. 10,000 times a day. Priced as new.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">8,000 tokens, full price</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Every call pays all.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Nothing marked reusable.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="999" fill="#F6E7A8"/>
<text x="480" y="173" font-size="12" text-anchor="middle" fill="#1B2838">write 1.25x</text>
<rect x="556" y="148" width="120" height="40" rx="999" fill="#E7F4EF"/>
<text x="616" y="173" font-size="12" text-anchor="middle" fill="#1B2838">read 0.1x</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Write once per TTL.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Reads at a tenth.</text>
<defs><marker id="m-d25-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d25-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">mark the repeat</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Mark what repeats. Pay full price once, not 10,000 times.</text>
</svg>
<figcaption>Shell 3. Full-price repeats become write-once reads. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D2-2 gives the stable prefix: system prompt first, versioned,
cacheable. Lesson D2-4 gives the token budget: every repeated token
has a price.

| Foundation | What it gives this lesson |
|---|---|
| V2-D2.2 zones | Stable prefix enables the cache |
| V2-D2.4 budget | Repeated tokens priced per call |

## 3. Mental model

Think of the cache key as a prefix. The API caches from the first
token: everything stable must come first, everything variable last.
Break the prefix and the cache misses. The price shape: a cache write
costs 1.25x the base input price, once per TTL. A cache read costs
0.1x, on every hit. (Public pricing. Verify against official docs.)
The TTL bounds staleness: 5 minutes default, longer on request. Below
the break-even hit rate, the write costs more than the reads save.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Stable first, variable last</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The cache reads the prefix. Break it and the cache misses.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="120" height="40" rx="999" fill="#F3D4D8"/>
<text x="104" y="173" font-size="12" text-anchor="middle" fill="#1B2838">user msg</text>
<rect x="180" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="240" y="173" font-size="12" text-anchor="middle" fill="#1B2838">system</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Variable first.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Prefix breaks every call.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Hit rate near zero.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="999" fill="#E7F1F8"/>
<text x="480" y="173" font-size="12" text-anchor="middle" fill="#1B2838">system</text>
<rect x="556" y="148" width="120" height="40" rx="999" fill="#F3D4D8"/>
<text x="616" y="173" font-size="12" text-anchor="middle" fill="#1B2838">user msg</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">Stable first.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">Prefix holds.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">Reads at 0.1x.</text>
<defs><marker id="m-d25-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d25-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fix the order</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Order is the cache key. Stable content earns the discount.</text>
</svg>
<figcaption>Shell 3. A broken prefix becomes a stable prefix. Source: original toy.</figcaption>
</figure>

:::takeaway
The cache key is the prefix. Stable first, variable last. A variable
prefix means a dead cache.
:::

## 4. Causal mechanism

On a cache miss, the API writes the prefix at 1.25x the base input
price and starts the TTL clock. On a hit inside the TTL, the prefix
reads at 0.1x. The break-even hit rate h solves: cached cost equals
uncached cost. Per call on the toy: uncached $0.017. Cached: h x
$0.0026 + (1 - h) x $0.017 + $0.000576 amortized write. Set equal:
0.017 - 0.0144h + 0.000576 = 0.017. Then 0.0144h = 0.000576, so h =
0.04. Above a 4% hit rate, the cache wins. Below it, the writes cost
more than the reads save.

Reuse goes beyond one prompt. Modular prompts split shared blocks:
the policy block, the format block, each versioned alone. Skills are
governed assets: named, versioned, reviewed, shared across teams.
Version every shared component: a silent prompt edit is a silent
production change, and a new version starts a new cache.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Break-even at 4%</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Above 4% hits the cache wins. Below, the writes cost more.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">hit rate: unknown</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">Cache on, blind.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Writes maybe wasted.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No break-even math.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">break-even: 4%</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">0.0144h = 0.000576.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">h = 0.04.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Measure the hit rate.</text>
<defs><marker id="m-d25-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d25-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">solve for h</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Do the break-even math. Then measure the hit rate.</text>
</svg>
<figcaption>Shell 4. A blind cache becomes a measured break-even. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: 8,000-token system prompt, 500 variable tokens per call, 10,000
calls per day, Balanced tier ($2 in per 1M, S10-S12, Oct 2026).

No cache: 8,500 / 1,000,000 x $2 = $0.017 per call. Times 10,000 =
$170 per day.

Cache (write 1.25x, read 0.1x, TTL 5 minutes): write per refresh:
8,000 / 1,000,000 x $2 x 1.25 = $0.02. Refreshes per day: 24 x 60 /
5 = 288. Write cost: 288 x $0.02 = $5.76 per day. Reads: 8,000 /
1,000,000 x $2 x 0.1 = $0.0016 per call. Times 10,000 = $16 per day.
Variable: 500 / 1,000,000 x $2 = $0.001 per call. Times 10,000 = $10
per day. Total: $5.76 + $16 + $10 = $31.76 per day. Savings: $170 -
$31.76 = $138.24 per day, 81%.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The cache prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Balanced tier. 10K calls a day. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">no cache: $170 / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">8,500/1M x $2 = $0.017.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">10,000 x $0.017 = $170.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Repeat priced as new.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">cache: $31.76 / day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Writes: 288 x $0.02 = $5.76.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Reads: 10,000 x $0.0016 = $16.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Plus $10 variable = $31.76.</text>
<defs><marker id="m-d25-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d25-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">cache the prefix</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The cache saves 81% a day on a stable prefix.</text>
</svg>
<figcaption>Shell 4. A stable prefix turns $170 per day into $31.76 per day. Source: original toy.</figcaption>
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

Mini question: "A team enables prompt caching. The system prompt is 8,000 tokens but the user message is placed before it. Hit rate is 2%. Costs do not fall. What is the first fix? A) Increase the cache TTL. B) Move the stable system prompt before the variable user message so the prefix is stable. C) Disable caching and accept the cost."

| Step | Action on this question |
|---|---|
| STEP 1 | Root cause of a dead cache |
| STEP 2 | Operation: cost issue in production |
| STEP 3 | Make caching work |
| STEP 4 | Hit rate 2%. Variable content leads, so the prefix breaks every call |
| STEP 5 | Application layer: prompt assembly order |
| STEP 6 | All three are technically feasible |
| STEP 7 | No hard constraint is violated. All stay in the race |
| STEP 8 | B fixes the root cause: the prefix rule. A treats a symptom. C surrenders |
| STEP 9 | B needs the prompt builder reordered, then the hit rate re-measured |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive fact is the prefix rule: variable-first means the cache can never hit.

:::takeaway
When caching disappoints, check the order first. Stable content must
lead. The rest is detail.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Prompt caching | API cache parameter, prefix rule | V2-D2.5 cost control |
| Cache TTL | 5 minutes default, longer on request | V2-D2.5 staleness bound |
| Modular prompts | Shared prompt blocks, versioned | V2-D2.5 reuse |
| Skills as assets | Named, reviewed, versioned | V2-D2.5 governed reuse |

## 7. Current limitations

A variable prefix kills the cache: one changing token at the front
means zero hits. TTL expiry re-writes: quiet hours still pay the
write. Version skew: each prompt version starts a new cache, so ten
live versions mean ten cold caches. Low reuse loses: one-shot prompts
pay the 1.25x write for nothing. And the cache is not a store: it
holds prompts, not application state.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Versions split the cache</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Ten live versions. Ten cold caches. Version with care.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">10 versions live</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Each starts cold.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Writes paid ten times.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">1 version live</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">One warm cache.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Writes paid once.</text>
<defs><marker id="m-d25-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d25-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">version with care</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Each version is a new cache. Keep the live set small.</text>
</svg>
<figcaption>Shell 3. Ten cold caches become one warm cache. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| No cache | Pay full price | One-shot prompts, no repeats |
| Shorter prompt | Less to pay for | Bloat, rules as code |
| Cached prefix (this lesson) | Write once, read cheap | Stable prefix, high call volume |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Stable prefix, high volume | Cache it |
| Variable content leads | Reorder first, then cache |
| Hit rate below break-even | Fix the prefix or drop the cache |
| Prompt changes often | Version it. Each version is a new cache |

## 10. Valid-but-inferior option

Cache the whole conversation including the variable tail. Valid:
simple, one setting. Inferior: the tail changes every turn, so the
prefix never stabilizes and the hit rate sits near zero while writes
keep billing.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Cache everything | One setting, simple | Variable tail kills the hit rate |

## 11. Counterfactual where the alternative wins

One-shot analysis prompts: each call has a new document, a new
question, no repeats. The cache writes at 1.25x and never reads back.
No cache wins: the write is pure waste.

| Situation | Winner | Why |
|---|---|---|
| One-shot prompts, no repeats | No cache | Writes never pay back |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The cache key is the ______.
2. Write costs ______x. Read costs ______x.
3. Break-even hit rate on the toy: ______%.
4. Each prompt version starts a ______ cache.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A code-review bot reuses a 12,000-token style guide on every
call. The diff is appended after the guide. Hit rate is 90%.
A new guide version ships weekly.
Name what to cache. Name the version rule.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D2.5 tests caching, prefix rules, TTL, reuse, Skills, versioning | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Cache write 1.25x, read 0.1x, TTL 5 min default | Current product behavior. Verify against official docs | Public pricing | Oct 6, 2026 |
| Tier price $2 in per 1M (Balanced) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy cache arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Prefix rule: stable first | General principle | API practice | Long-standing |

:::takeaway
Reuse is an asset strategy: stable prefixes cached, shared blocks
modular, Skills governed, versions explicit.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Paying full price for repeats | 8,000 tokens full price | Write once, read 0.1x | d25-f01 | SVG | Original |
| u02 | Stable prefix carries over | -- | Prerequisite table | d25-f02 | Table | V2-D2.2, V2-D2.4 |
| u03 | Stable first, variable last | Variable first | Stable prefix | d25-f03 | SVG | Original |
| u04 | Break-even at 4% | Cache on, blind | Measured break-even | d25-f04 | SVG | Original |
| u05 | Cache prices itself | $170 per day | $31.76 per day | d25-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B fixes the prefix | d25-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d25-f06 | Table | S03, S04 |
| u07 | Versions split the cache | 10 versions live | 1 version live | d25-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d25-f08 | Table | Original |
| u09 | Constraints decide caching | -- | Constraint verdict table | d25-f09 | Table | Original |
| u10 | Cache-all is valid but inferior | -- | Tail kills hit rate | d25-f10 | Table | Original |
| u11 | One-shot favors no cache | -- | Counterfactual table | d25-f11 | Table | Original |
| u12 | Cache facts from memory | Blank recall card | Filled from memory | d25-f12 | ASCII | Original |
| u13 | Transfer to code review | Unseen question | Key in Stage 8 | d25-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d25-f14 | Table | Mixed |
