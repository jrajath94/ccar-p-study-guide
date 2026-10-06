# Lesson D3-8: progressive discovery vs monolithic context (V2-D3.8)

## 1. Problem this lesson solves

A research agent serves literature review. On every call it receives
all 200 tool schemas plus their documentation: 100,000 tokens before
the user asks anything. The model picks the wrong tool twice as often
as it should. The bill shows six figures of schema tokens per day.
The attack surface holds 200 doors, though the task needs 4.

The team defends the dump: "the model needs full context to choose."
The model chooses worse with 200 options than with 10. Choice
overload is not a metaphor. It is measurable selection error.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">100,000 tokens before the question</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">200 schemas dumped upfront. The task needs 4 tools.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">200 schemas x 500 tokens</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">100,000 tokens per call.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Wrong pick rate: 18%.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">200 doors open.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">names first, schemas on demand</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">5,500 tokens per call.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">Wrong pick rate: 6%.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">4 doors open.</text>
<defs><marker id="m381" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m381)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">discover on demand</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Fewer visible options means better picks and a smaller bill.</text>
</svg>
<figcaption>Shell 3. A 200-schema dump becomes on-demand discovery. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson D3-1 | Least privilege: remove unneeded tools |
| Lesson D2-4 | Context management: active context vs retrieval vs app state |
| Lesson D2-5 | Caching: fetched schemas can be cached |

Lesson D3-1 removed tools from the config. This lesson removes them
from the context until the task needs them. Removal is permanent.
Discovery is lazy. Both shrink what the model sees.

## 3. Mental model

Treat context as a cache, not a dump. The monolithic pattern loads
everything upfront: every schema, every doc, every option. The
progressive pattern loads names first and fetches details on demand:
list the tools, search for the right one, fetch its schema, call it.

Three wins follow. Token overhead falls: names cost little, schemas
cost much. Selection confusion falls: the model picks among 10 names,
not 200 schemas. Attack surface shrinks: a tool the model cannot see,
it cannot call. Unadvertised means unavailable.

Discovery has one cost: round trips. Each fetch is a call with
latency. The exam's trade-off is token overhead and confusion versus
fetch latency. Lesson D3-3 prices the latency side.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Names first, schemas on demand</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">200 names cost 4,000 tokens. 3 fetched schemas cost 1,500.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">200 schemas upfront</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">200 x 500 = 100,000</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Paid on every call.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">200 names: 4,000</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">3 schemas: 1,500</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Total: 5,500. Cut: 94.5%.</text>
<defs><marker id="m383" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m383)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fetch on demand</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Names are cheap. Schemas are dear. Fetch the few you need.</text>
</svg>
<figcaption>Shell 4. Upfront schemas become names plus on-demand fetch. Source: original toy.</figcaption>
</figure>

:::takeaway
Discover capabilities on demand. Cut token overhead and selection
confusion. Shrink the attack surface. Pay fetch latency instead.
:::

## 4. Causal mechanism

The mechanism has three moves. First, advertise lightly. The agent
sees tool names with one-line descriptions, or a search tool that
finds tools by intent. MCP's tools/list can return the light
advertisement. The full schema arrives on request. Second, fetch
lazily. When the model picks a tool name, the host fetches the full
schema, caches it (Lesson D2-5), and the model calls the tool. Third,
scope the advertisement. The list shows only tools the user's
permissions allow (Lesson D3-2). A tool outside the user's scope
never appears.

Why selection improves: the model matches intent against 10 short
names instead of 200 long schemas. Fewer candidates, cleaner
signal. The toy shows wrong picks falling from 18% to 6%.

Why the attack surface shrinks: the model cannot call what it cannot
name. A dangerous tool stays unadvertised until the task and the
permissions justify it. This complements Lesson D3-1's removal:
removal takes the tool out of the config, discovery keeps it out of
the context.

The cost is real. Each fetch adds a round trip. For a task that uses
3 tools, the run adds 3 fetches. Lesson D3-3's budget decides whether
the latency fits. Caching fetched schemas across calls in a session
pays the fetch once.

## 5. Minimal worked example

Toy: the research agent. 200 tools, 500 tokens per schema, 20 tokens
per name. 5,000 calls per day. Monolithic: 200 x 500 = 100,000
tokens per call. Progressive: 200 x 20 = 4,000 for names, plus 3
fetched schemas x 500 = 1,500. Total 5,500 tokens per call.

Daily schema cost. Monolithic: 5,000 x 100,000 = 500,000,000 tokens
per day. Progressive: 5,000 x 5,500 = 27,500,000 tokens per day.
Savings: 472,500,000 tokens per day, a 94.5% cut.

Mini question: "An agent with 200 tools shows 18% wrong-tool picks
and pays 100,000 schema tokens per call. Which change best addresses
both? A) Rewrite all 200 descriptions to be more distinct. B) Show
tool names only, fetch full schemas on demand, and scope the list to
the user's permissions. C) Remove 150 tools from the config."

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
| STEP 1 | Question asks: best architecture. Cut tokens and wrong picks |
| STEP 2 | Stage: operation. The agent is live and expensive |
| STEP 3 | Objective: fewer tokens per call, fewer wrong picks |
| STEP 4 | Hard constraints: 200 tools exist, tasks vary |
| STEP 5 | Layer: context assembly, capability advertisement |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | None violate stated constraints. All survive to comparison |
| STEP 8 | B cuts tokens 94.5% and shrinks the choice set from 200 to names. A helps confusion but keeps 100,000 tokens. C cuts tokens but breaks tasks that need the removed tools |
| STEP 9 | B's consequence: fetch latency per new tool, paid once per session via cache |
| STEP 10 | B alone answers both symptoms. A answers one. C risks breaking tasks |

Verdict: B. The arithmetic: 100,000 down to 5,500 tokens per call,
472,500,000 tokens saved per day. Wrong picks fall because the
choice set shrinks. The scenario asks for both cost and accuracy,
and only progressive discovery answers both without breaking tasks.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Both symptoms, one fix</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">5,000 calls per day. Tokens and wrong picks fall together.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">500M tokens per day</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">18% wrong picks</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">200 doors open.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">27.5M tokens per day</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">6% wrong picks</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Names shown. Schemas fetched.</text>
<defs><marker id="m385" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m385)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">advertise lightly</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Discovery pays fetch latency and buys back tokens and accuracy.</text>
</svg>
<figcaption>Shell 4. Daily schema tokens fall 94.5% and wrong picks fall by two thirds. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| tools/list advertisement | MCP server | V2-D3.8 capability discovery |
| Tool search by intent | Application layer | V2-D3.8 progressive discovery |
| Schema caching per session | Application cache | V2-D3.8 fetch cost control, Lesson D2-5 |
| Permission-scoped tool list | Application policy | V2-D3.8 attack surface, Lesson D3-2 |

## 7. Current limitations

Discovery adds round trips. Latency-sensitive tasks feel each fetch.
The discovery tool itself is a target: a poisoned document can steer
the model toward the wrong tool (indirect injection, Lesson 7-3A).
Names must be good. Cryptic names break the light advertisement.
Caching helps within a session but not across cold starts.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Progressive discovery (this lesson) | Names first, fetch on demand | Large tool surface, varied tasks |
| Monolithic context | Everything upfront | Tiny tool set, latency binds |
| Permanent removal | Tool leaves the config | Tool never needed, Lesson D3-1 |
| Static per-task subsets | Fixed small sets per task | Tasks known in advance |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Tool surface above ~20 tools | Progressive discovery |
| Token budget binds | Names first, schemas on demand |
| Wrong-tool picks rise with surface size | Shrink the visible choice set |
| Latency binds harder than tokens | Monolithic, if the set is small |
| Tasks known in advance | Static per-task subsets |

## 10. Valid-but-inferior option

Rewrite all 200 descriptions to be more distinct. Valid: clearer
descriptions do cut confusion, and the work is real. Inferior here:
it keeps 100,000 schema tokens per call and 200 open doors. The
scenario names both tokens and wrong picks. Better labels answer
only one.

## 11. Counterfactual where the alternative wins

Eight tools, fixed set, sub-second latency SLA. Monolithic wins:
8 x 500 = 4,000 tokens per call is cheap, no fetch round trips, no
discovery machinery. The surface is small enough that choice
overload never appears.

| Situation | Winner | Why |
|---|---|---|
| 8 tools, tight latency SLA | Monolithic context | Cheap tokens, zero fetch latency |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Three wins of discovery: ______, ______, ______.
2. One cost of discovery: ______.
3. 200 x 500 = ______. Names plus 3 schemas = ______.
4. Removal is ______. Discovery is ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A code agent has 120 tools. Each call carries 60,000
schema tokens. Wrong-tool picks run at 15%. The task mix
changes daily, so no static subset fits.
Name the pattern and the two numbers that justify it.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Discover capabilities on demand, cut token overhead and selection confusion, shrink attack surface | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D3.8 | Sept 2026 |
| Context as active context vs retrieval vs app state plus caching mechanics | Taught in Lessons D2-4 and D2-5 | This build | Oct 6, 2026 |
| Toy arithmetic: 100,000 to 5,500 tokens, 94.5% cut, 500M to 27.5M per day | Original toy, computed above | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D3.8 trap is "the model needs full context to choose."
Full context is what breaks the choice. Advertise lightly, fetch
on demand, scope the list.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | 100,000 tokens before the question | 200 schemas dumped | Names first, 5,500 tokens | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | D3-1, D2-4, D2-5 |
| u03 | Names first, schemas on demand | 100,000 per call | 5,500 per call, 94.5% cut | f03 | SVG | Original |
| u04 | Three moves of discovery | Dump | Advertise, fetch, scope | f04 | Text | Original |
| u05 | 10-step method picks B | Three options | B: progressive discovery | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Fetch latency and injection limits | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Rewrite descriptions inferior here | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | 8 tools favor monolithic | -- | Counterfactual table | f11 | Table | Original |
| u12 | Three wins from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to code agent | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
