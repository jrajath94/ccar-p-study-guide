# Lesson D3-6: retrieval strategies (V2-D3.6)

## 1. Problem this lesson solves

A support agent searches 1,000 policy documents. Semantic search
handles "how do I get my money back" and returns the refund policy.
It misses "ERR-4017" because the code is an exact string, not a
meaning. Keyword search handles "ERR-4017" and misses the paraphrase.
The team picks one retriever. Half the queries fail.

Worse, the agent answers "where is my order" from the index. The
index refreshes hourly. The order shipped six minutes ago. The answer
is stale by fifty-four minutes. Live transactional state sat in the
database, one tool call away. The team indexed it instead.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One retriever, half the queries</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Exact codes need keywords. Paraphrases need meaning. Stale data needs a tool.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">semantic only</text>
<text x="44" y="204" font-size="13" fill="#5C6B7A">"ERR-4017": missed.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">Order status: 54 min stale.</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">One tool for all queries.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">hybrid plus tool call</text>
<text x="420" y="204" font-size="13" fill="#5C6B7A">"ERR-4017": keyword hits.</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">Order status: live tool call.</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Query type picks the path.</text>
<defs><marker id="m361" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m361)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">match query to path</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The query type picks the retriever. Freshness picks index or tool.</text>
</svg>
<figcaption>Shell 3. One retriever becomes hybrid retrieval plus a live tool call. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson D3-5 | The pipeline stages. Retrieval sits between indexing and rerank |
| Lesson 7-3A | Embeddings at intuition level. Meaning as vectors |

## 3. Mental model

Five retrieval moves. Keyword search matches exact terms. It wins on
codes, names, and SKUs. Semantic search matches meaning through
embeddings. It wins on paraphrase. Hybrid runs both and merges the
lists. Metadata filters narrow by source, date, or access level
before or after the match. Reranking scores the merged candidates
harder and keeps the top few. Rank fusion merges two ranked lists
into one when both retrievers speak.

One rule governs freshness. An index is a snapshot. A tool call is
the present. Live transactional state, order status, balances,
inventory, belongs behind a tool call, not a stale index. The exam
states this as a hard rule. The index answers "what does the doc
say." The tool answers "what is true now."

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Snapshot or present</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The index refreshes hourly. The order shipped 6 minutes ago.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">index: "in warehouse"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Snapshot age: 54 minutes.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Truth: shipped.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Answer: wrong.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">tool: "shipped 6 min ago"</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">Snapshot age: 0 minutes.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">Truth: shipped.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">Answer: right.</text>
<defs><marker id="m363" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m363)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">call the live tool</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Live state belongs behind a tool call, not a stale index.</text>
</svg>
<figcaption>Shell 4. The stale index becomes a live tool call for order status. Source: original toy.</figcaption>
</figure>

:::takeaway
Keyword for exact terms. Semantic for paraphrase. Hybrid for both.
Metadata filters narrow the field. Live state always goes through
a tool call.
:::

## 4. Causal mechanism

Each strategy matches a query shape. Keyword search scores term
overlap. A query with a product code, an error number, or a proper
name needs it. Semantic search scores vector closeness. A query
phrased differently from the document needs it. Hybrid runs both,
then merges. The merge uses rank fusion: a document ranked high by
both lists outranks one ranked high by one. Metadata filters cut the
candidate pool before scoring: only this source, only this year,
only rows the user may see. That last filter is Lesson 7-2A's access
control applied at retrieval.

Reranking sits after retrieval in the pipeline (Lesson D3-5). A
cheap retriever pulls 50 candidates. A stronger scorer reorders them
and keeps 5. The exam's causal point: rerank cannot rescue a
candidate set that never contained the answer. Recall caps at
retrieval. Rerank only reorders.

The freshness rule has a mechanism. Index builds take minutes to
hours. Transactional state changes in seconds. Any question whose
answer changes faster than the index refresh must bypass the index.
The router sends "where is my order" to the order tool and "what is
the refund policy" to the index. Query type decides.

## 5. Minimal worked example

Toy: 1,000 policy documents. Two queries. Query A: "ERR-4017 refund
window." Query B: "how do I get my money back." Keyword retrieval on
A returns 5 chunks, 4 relevant: precision 4 / 5 = 0.80. Semantic
retrieval on A returns 6 chunks, 1 relevant: precision 1 / 6 = 0.17.
Semantic on B returns 8 chunks, 6 relevant: precision 6 / 8 = 0.75.
Keyword on B returns 4 chunks, 1 relevant: precision 1 / 4 = 0.25.
Hybrid on both returns the union, reranked: A keeps 4 of 4 relevant,
B keeps 6 of 6 relevant.

Mini question: "An agent answers order-status questions from an
hourly index. Customers complain the status is wrong after shipping.
Which change best fixes the complaints? A) Rebuild the index every
5 minutes. B) Route order-status questions to a live order tool.
Keep policy questions on the index. C) Add semantic search to the
index."

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
| STEP 1 | Question asks: best architecture. Fix stale order status |
| STEP 2 | Stage: operation. Customers see wrong answers now |
| STEP 3 | Objective: correct order status at answer time |
| STEP 4 | Hard constraints: status changes in minutes, index refreshes hourly |
| STEP 5 | Layer: retrieval routing, index vs tool |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | None violate stated constraints. All survive to comparison |
| STEP 8 | B matches the freshness rule: live state behind a tool call. A narrows the gap but keeps a snapshot. C changes the matcher, not the freshness |
| STEP 9 | B's consequence: the order tool needs auth and latency budget. Both are normal integration costs |
| STEP 10 | B alone answers "what is true now." A and C answer a different problem |

Verdict: B. The freshness arithmetic: a 5-minute index still lags a
shipment by up to 5 minutes, and it rebuilds 1,000 documents 288
times per day for a question a tool answers in one call. The
scenario is a freshness failure, and the answer is route live state
to the tool, not a faster snapshot.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The query picks the matcher</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Precision per query per strategy, from the toy counts.</text>
<rect x="24" y="96" width="336" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">PRECISION BY STRATEGY</text>
<text x="44" y="160" font-size="13" fill="#1B2838">Query A, keyword: 4 / 5 = 0.80</text>
<text x="44" y="184" font-size="13" fill="#1B2838">Query A, semantic: 1 / 6 = 0.17</text>
<text x="44" y="208" font-size="13" fill="#1B2838">Query B, keyword: 1 / 4 = 0.25</text>
<text x="44" y="232" font-size="13" fill="#1B2838">Query B, semantic: 6 / 8 = 0.75</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">No single winner.</text>
<text x="44" y="288" font-size="13" fill="#5C6B7A">Hybrid keeps both wins.</text>
<rect x="392" y="96" width="304" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="412" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER HYBRID</text>
<rect x="412" y="148" width="264" height="40" rx="999" fill="#E7F4EF"/>
<text x="544" y="173" font-size="13" text-anchor="middle" fill="#1B2838">A: 4 of 4 kept</text>
<rect x="412" y="196" width="264" height="40" rx="999" fill="#E7F4EF"/>
<text x="544" y="221" font-size="13" text-anchor="middle" fill="#1B2838">B: 6 of 6 kept</text>
<text x="412" y="248" font-size="13" fill="#5C6B7A">Union, then rerank.</text>
<defs><marker id="m365" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="376" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m365)"/>
<text x="24" y="352" font-size="15" fill="#1B2838">Hybrid wins because each query shape has its own best matcher.</text>
</svg>
<figcaption>Shell 4. Hybrid retrieval keeps each strategy's win. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Term-overlap scoring | Keyword index | V2-D3.6 exact-term queries |
| Embedding similarity | Vector index | V2-D3.6 paraphrase queries |
| Rank fusion of two lists | Application merge | V2-D3.6 hybrid retrieval |
| Source, date, ACL filters | Metadata layer | V2-D3.6 metadata filters |
| Live state tool | Tool integration | V2-D3.6 freshness rule |

## 7. Current limitations

Hybrid costs two indexes and a merge. Rerank adds latency (Lesson
D3-3 prices it). Metadata filters only work if ingestion recorded
the metadata (Lesson D3-5). The freshness rule needs a router that
classifies queries. A misrouted query still hits the stale index.
Semantic search drifts as language changes. The index needs refresh
even when documents do not.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Hybrid plus tool routing (this lesson) | Matcher per query, tool for live state | Mixed queries, live data exists |
| Keyword only | One index, exact terms | Codes, SKUs, names only |
| Semantic only | One index, meaning | Paraphrase-heavy, no exact codes |
| Index everything, no tools | One snapshot for all | Data changes slower than refresh |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Query carries a code or name | Keyword must be in the mix |
| Query paraphrases the document | Semantic must be in the mix |
| Mixed query shapes | Hybrid with rank fusion |
| Answer changes faster than refresh | Tool call, not the index |
| Access varies by user | Metadata ACL filter before scoring |

## 10. Valid-but-inferior option

Rebuild the index every 5 minutes. Valid: fresher snapshots cut the
staleness window from 60 minutes to 5. Inferior for order status:
288 rebuilds per day of 1,000 documents, and the answer can still lag
a shipment by 5 minutes. One tool call gives the present with no
rebuild cost. The scenario is a freshness problem, and a faster
snapshot is still a snapshot.

## 11. Counterfactual where the alternative wins

An annual employee handbook. It changes once a year. The index
refreshes nightly. Every query asks "what does the doc say." Index
everything, no tools: the snapshot is always fresh enough, one
system serves all queries, and no tool wiring is needed.

| Situation | Winner | Why |
|---|---|---|
| Slow-changing corpus, doc questions only | Index everything, no tools | Snapshot always fresh enough |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Keyword wins on ______. Semantic wins on ______.
2. Rank fusion merges ______ ranked lists.
3. Rerank cannot fix a candidate set that ______.
4. Live state belongs behind a ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A bank agent answers balance questions from a nightly
index. Balances change all day. Customers see yesterday's
numbers.
Name the rule violated and the two paths the router must
split.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Keyword, semantic, hybrid, metadata filters, reranking, rank fusion | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D3.6 | Sept 2026 |
| Live transactional state belongs behind a tool call, not a stale index | Official exam scope via secondary summaries | Blueprint ledger V2-D3.6 | Sept 2026 |
| Toy arithmetic: precision per strategy per query | Original toy, computed above | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D3.6 trap offers a better matcher for a freshness
problem. Matchers fix matching. Only the tool fixes freshness.
Ask what the question is really about: the words, or the time.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | One retriever, half the queries | Semantic only, stale index | Hybrid plus live tool call | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | D3-5, 7-3A |
| u03 | Snapshot or present | 54 min stale | 0 min stale via tool | f03 | SVG | Original |
| u04 | Strategy per query shape | One matcher | Five moves, freshness rule | f04 | Text | Original |
| u05 | 10-step method picks B | Three options | B: route live state to tool | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Hybrid cost and drift limits | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | 5-minute rebuild inferior here | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Handbook favors index-only | -- | Counterfactual table | f11 | Table | Original |
| u12 | Matcher rules from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to bank agent | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
