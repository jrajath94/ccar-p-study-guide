# Lesson D2-4: context and token management (V2-D2.4)

## 1. Problem this lesson solves

A support bot keeps full conversation history. By turn 40 the prompt
is 60,000 tokens. Answers degrade. The bill spikes. The team buys a
bigger window. The window fills too. Growth was never managed, only
housed.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Growth was housed, not managed</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Turn 40. 60,000 tokens. Bigger window fills too.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">full history, 60K tokens</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Answers degrade.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Bigger window: fills too.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">budget: 5K per turn</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Just in time plus compaction.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Growth managed, not housed.</text>
<defs><marker id="m-d24-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d24-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">budget the context</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A window is capacity. A budget is management.</text>
</svg>
<figcaption>Shell 3. Full history becomes a per-turn budget. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-3A gives dilution by name: fits is not focus. A full window
does not mean full attention. Lesson 7-1A gives state: conversation
memory lives in the app, not the model.

| Foundation | What it gives this lesson |
|---|---|
| §7.3 dilution | Full context dilutes attention |
| §7.1 state | Memory is app code the team owns |

## 3. Mental model

Think of a budget with four accounts. Active context is what the
model sees now. Retrieval fetches facts just in time. App state is the
system of record. Conversation memory is what the app remembers.
Five failure modes spend the budget badly. Growth: history never
stops. Duplication: the same fact three times. Loss: compaction ate
the key detail. Exhaustion: the window fills mid-task. Dilution: the
middle gets lost. Diagnose the mode first. Then pick the strategy.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five ways the budget leaks</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Name the leak before you fix it.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">slow and expensive</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Which leak? Unknown.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Fix: bigger window.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Leak continues.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="32" rx="999" fill="#E6E2DA"/>
<text x="480" y="169" font-size="12" text-anchor="middle" fill="#1B2838">growth</text>
<rect x="548" y="148" width="128" height="32" rx="999" fill="#E6E2DA"/>
<text x="612" y="169" font-size="12" text-anchor="middle" fill="#1B2838">duplication</text>
<rect x="420" y="188" width="120" height="32" rx="999" fill="#E6E2DA"/>
<text x="480" y="209" font-size="12" text-anchor="middle" fill="#1B2838">loss</text>
<rect x="548" y="188" width="128" height="32" rx="999" fill="#E6E2DA"/>
<text x="612" y="209" font-size="12" text-anchor="middle" fill="#1B2838">exhaustion</text>
<rect x="476" y="228" width="144" height="32" rx="999" fill="#F6E7A8"/>
<text x="548" y="249" font-size="12" text-anchor="middle" fill="#1B2838">dilution</text>
<text x="420" y="280" font-size="13" fill="#5C6B7A">Each leak has a strategy.</text>
<defs><marker id="m-d24-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d24-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">name the leak</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Five leaks, five strategies. The diagnosis comes first.</text>
</svg>
<figcaption>Shell 3. One slow bot becomes five named leaks. Source: original toy.</figcaption>
</figure>

:::takeaway
Active context, retrieval, app state, conversation memory: four
accounts, one budget. Spend on what the current turn needs.
:::

## 4. Causal mechanism

Each leak has a signature and a strategy. Growth: per-turn tokens
climb every turn. Strategy: just-in-time retrieval plus compaction at
a trigger. Duplication: the same chunk appears twice in one prompt.
Strategy: dedupe at assembly. Loss: the summary dropped the order
number. Strategy: checkpoints keep key facts verbatim. Exhaustion:
the call fails mid-task. Strategy: reserve headroom, compact before
the trigger. Dilution: the middle answer is wrong. Strategy: fewer,
better-placed chunks. Four context strategies cover the map. Full fits short talks.
Recent keeps the last N turns. Just-in-time retrieves per turn.
Compaction summarizes at a trigger and keeps checkpoints.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Leak to strategy</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each leak maps to one strategy. No generic fix.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">full history, always</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">One strategy for five leaks.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Growth: unhandled.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Dilution: unhandled.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">growth: just in time</text>
<rect x="420" y="192" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="215" font-size="12" text-anchor="middle" fill="#1B2838">dilution: fewer chunks</text>
<rect x="420" y="236" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="259" font-size="12" text-anchor="middle" fill="#1B2838">loss: checkpoints</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">The leak picks the strategy.</text>
<defs><marker id="m-d24-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d24-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">map the leak</text>
<text x="24" y="352" font-size="15" fill="#1B2838">No leak, no fix. Name it, then treat it.</text>
</svg>
<figcaption>Shell 4. One generic fix becomes leak-to-strategy mapping. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: support bot on the Fast tier ($1 in per 1M, S10-S12, Oct 2026).
Each turn adds 1,200 tokens. 50-turn conversation.

Full history: turn N carries 1,200 x N tokens. At turn 50: 60,000
tokens. Cost at turn 50: 60,000 / 1,000,000 x $1 = $0.06. Whole
conversation: 1,200 x (1 + 2 + ... + 50) = 1,200 x 1,275 = 1,530,000
tokens. Cost: 1,530,000 / 1,000,000 x $1 = $1.53.

Just-in-time: last 3 turns plus retrieved facts = 5,000 tokens per
turn, flat. 50 x 5,000 = 250,000 tokens. Cost: 250,000 / 1,000,000 x
$1 = $0.25. Savings: $1.53 - $0.25 = $1.28 per conversation, 6x
cheaper, and attention stays on the current turn.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The budget prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fast tier. 50 turns. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">full: $1.53 per talk</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">1,200 x 1,275 = 1,530,000.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Turn 50: 60,000 tokens.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Cost grows every turn.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">JIT: $0.25 per talk</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">50 x 5,000 = 250,000.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Flat 5,000 per turn.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">$1.53 - $0.25 = $1.28 saved.</text>
<defs><marker id="m-d24-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d24-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">retrieve per turn</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Just-in-time costs 6x less and keeps attention on now.</text>
</svg>
<figcaption>Shell 4. Per-turn retrieval turns $1.53 into $0.25. Source: original toy.</figcaption>
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

Mini question: "A support bot keeps full conversation history. At turn 40, answers degrade and costs spike. What is the first action? A) Move to a 1M-token window tier. B) Profile per-turn token growth, then move to just-in-time retrieval plus compaction. C) Summarize the full history every turn."

| Step | Action on this question |
|---|---|
| STEP 1 | First action on degradation plus cost spike |
| STEP 2 | Operation: production issue |
| STEP 3 | Restore quality and bound cost |
| STEP 4 | Degradation at turn 40. Cost climbs every turn. Growth unmanaged |
| STEP 5 | Application layer: context management |
| STEP 6 | All three are technically feasible |
| STEP 7 | No hard constraint is violated. All stay in the race |
| STEP 8 | B diagnoses first, then treats the leak. A houses growth without treating it. C adds summary drift |
| STEP 9 | B needs the compaction trigger and the retrieval index owned |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive move is diagnosis before treatment, and only B profiles the growth first.

:::takeaway
A bigger window houses growth. It does not manage it. The exam rewards the
option that names the leak and treats it: profile, then budget.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Active context | Prompt assembly | V2-D2.4 window management |
| Just-in-time retrieval | Retriever plus app code | V2-D2.4, V2-D3.5 RAG |
| Conversation memory | App session store | V2-D2.4, V2-D1.2 state |
| Compaction trigger | App code at token threshold | V2-D2.4 growth control |

## 7. Current limitations

Compaction loses detail: the summary keeps the gist and drops the
order number. Retrieval can miss: the needed fact ranks fourth, not
first. Just-in-time adds a call: latency and a new failure point.
Checkpoints cost storage. And no strategy fixes a task that truly
needs the whole history: some audits do.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Compaction eats details</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The summary keeps the gist. The order number is gone.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">full history kept</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Order number present.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Cost: unbounded.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">summary kept</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Order number gone.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Checkpoint the key facts.</text>
<defs><marker id="m-d24-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d24-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">compact with care</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Summaries drop details. Checkpoints keep the ones that matter.</text>
</svg>
<figcaption>Shell 3. Blind compaction becomes compaction with checkpoints. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Full history | Keep everything | Short talks, audit needs |
| Bigger window | More capacity | One-time overflow, no growth trend |
| Budgeted context (this lesson) | Leak diagnosed, strategy picked | Production, long talks, cost pressure |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Tokens grow every turn | Just-in-time plus compaction trigger |
| Middle answers wrong | Fewer, better-placed chunks |
| Same fact repeated | Dedupe at assembly |
| Audit needs everything | Full history, priced and bounded |
| Window fills mid-task | Reserve headroom, compact early |

## 10. Valid-but-inferior option

Summarize the full history every turn. Valid: bounds the size.
Inferior: each turn pays for a big summarization call. The summary
also drifts: by turn 40, two compactions ate the details.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Summarize every turn | Bounds the size | Pays a big call per turn. Drift compounds |

## 11. Counterfactual where the alternative wins

Legal audit chat: ten turns, every word must be replayable, the
regulator reads the transcript. Full history wins: the requirement is
completeness, and ten turns fit the window with room.

| Situation | Winner | Why |
|---|---|---|
| Short talk, replay required | Full history | Completeness is the requirement |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The four accounts: active context, retrieval,
   app state, conversation ______.
2. The five leaks: growth, duplication, loss,
   ______, dilution.
3. Growth strategy: ______ plus compaction.
4. JIT saves $______ per conversation.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A travel planner holds a 30-turn itinerary chat. At turn 20
the bot forgets the departure city. Costs climb each turn.
Name the leak. Name the strategy. Name the checkpoint.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D2.4 tests window management, four accounts, five failure modes | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Tier price $1 in per 1M (Fast) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy conversation arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Dilution: fits is not focus | General principle | ML practice | Long-standing |

:::takeaway
Budget the context like money: name the accounts, watch the leaks,
and spend on the current turn.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Growth was housed, not managed | Full history, 60K | Budget 5K per turn | d24-f01 | SVG | Original |
| u02 | Dilution and state carry over | -- | Prerequisite table | d24-f02 | Table | §7.3, §7.1 |
| u03 | Five ways the budget leaks | Slow and expensive | Five named leaks | d24-f03 | SVG | Original |
| u04 | Leak to strategy | Full history always | Mapped strategies | d24-f04 | SVG | Original |
| u05 | Budget prices itself | $1.53 per talk | $0.25 per talk | d24-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B profiles growth first | d24-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d24-f06 | Table | S03, S04 |
| u07 | Compaction eats details | Full kept | Summary plus checkpoints | d24-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d24-f08 | Table | Original |
| u09 | Constraints decide the strategy | -- | Constraint verdict table | d24-f09 | Table | Original |
| u10 | Summarize-all is valid but inferior | -- | Drift compounds | d24-f10 | Table | Original |
| u11 | Audit favors full history | -- | Counterfactual table | d24-f11 | Table | Original |
| u12 | Budget facts from memory | Blank recall card | Filled from memory | d24-f12 | ASCII | Original |
| u13 | Transfer to travel planner | Unseen question | Key in Stage 8 | d24-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d24-f14 | Table | Mixed |
