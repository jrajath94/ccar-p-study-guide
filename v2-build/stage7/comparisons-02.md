# Comparisons 02: caching, discovery, and retrieval

Five high-confusion pairs from §18. Tight matrices. Prior-stage concepts appear by name only.

:::takeaway
Caching and retrieval both answer one question: where does the answer already live? The mechanism that matches the data shape wins.
:::

## Pair 7: prompt caching vs response caching

Shared: both cut repeated model cost. Both sit under V2-D2.5 and V2-D4.5. Both need measurement before claims.

Decisive difference: prompt caching reuses a stable input prefix across calls with different suffixes. Response caching reuses a full stored answer for byte-identical or semantically identical prompts. One caches the front of the request. The other caches the whole answer.

| Dimension | Prompt caching | Response caching |
|---|---|---|
| What repeats | Stable prefix (V2-D2.5) | Whole prompt, or semantic twin |
| Variable suffix | Allowed, priced at full | Breaks exact match |
| Output recompute | Full output price each call | Zero on hit |
| Staleness risk | TTL on the prefix | Stored answer goes stale |
| Correctness risk | None: model still runs | Wrong answer served fast |
| Best fit | Same system prompt, varied questions | Same question asked often |

Winning constraints: prompt caching wins when the prefix is stable and questions vary. Response caching wins when whole prompts repeat exactly and answers stay valid.

Losing constraints: prompt caching loses below the break-even hit rate (4% on the V2-D2.5 toy). Response caching loses when answers depend on fresh state: a cached balance from yesterday is a wrong answer served cheaply.

Costs: prompt caching prices: write 1.25x once per TTL, reads 0.1x (public pricing, verify against official docs). Response caching prices: hit costs near zero, miss costs full. On the toy below: 10,000 identical prompts per day, 500 in plus 300 out tokens. No cache: $0.004 per call, $40 per day. Prompt caching: $31.36 per day. Response caching at 80% exact hit: 2,000 misses times $0.004 = $8 per day.

Security: prompt caching stores your prefix on the provider side. Sensitive system content in the prefix sits in provider storage. Response caching stores answers: PII in a cached answer leaks to every later identical query. Both need the retention review from V2-D5.4.

Operational burden: prompt caching needs prefix hygiene and hit-rate monitoring. Response caching needs the invalidation rule and a stale-answer detector. A response cache without invalidation is a correctness incident.

Counterexample: a support bot answering "what are your hours?" Response caching wins at 95% hit. A support bot answering "where is my order?" must never use response caching: the answer is per-user state. Live state belongs behind a tool call (V2-D3.6).

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Prompt cache pricing 1.25x write, 0.1x read | Current product behavior, verify | Public pricing via S10-S12 | Oct 6, 2026 |
| Break-even 4% toy | Original toy, computed | Lesson D2-5 | Oct 6, 2026 |
| Response cache cost toy | Original toy, computed below | This file | Oct 6, 2026 |

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Identical questions change the cache</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">10,000 identical prompts per day. 500 in, 300 out. Balanced tier.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: PROMPT CACHE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">$31.36 / day</text>
<text x="44" y="212" font-size="13" fill="#5C6B7A">Prefix write $0.36. Prefix reads $1.</text>
<text x="44" y="232" font-size="13" fill="#5C6B7A">Output still full price: $30.</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Model runs every call.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: RESPONSE CACHE</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">$8.00 / day</text>
<text x="420" y="212" font-size="13" fill="#5C6B7A">80% exact hit. 2,000 misses.</text>
<text x="420" y="232" font-size="13" fill="#5C6B7A">2,000 x $0.004 = $8.</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Hit serves a stored answer.</text>
<defs><marker id="mc2" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mc2)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">duplicates exact</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Exact duplicates beat prefix reuse. Stale answers are the price.</text>
</svg>
<figcaption>Shell 4. Exact-duplicate traffic moves from $31.36 to $8 per day by caching whole answers. Source: original toy.</figcaption>
</figure>

Minimal pairs:

- MP1. Base: 10,000 calls per day share an 8,000-token system prompt, questions vary. Winner: prompt caching. Change: all 10,000 calls become the same five FAQ prompts. Winner flips to response caching. Exact duplication crosses the threshold.
- MP2. Base: FAQ bot with 95% exact hits on response cache. Change: answers must include the user's live account balance. Winner flips to prompt caching plus a tool call. The stored answer is now wrong per user.
- MP3. Base: response cache saves $32 per day. Change: legal requires every answer carry a fresh citation to the current policy version. Winner flips to prompt caching with grounding checks. The cache cannot certify freshness.

## Pair 8: progressive discovery vs monolithic context

Shared: both give the model its tools. Both sit under V2-D3.8. Both answer the V2-D3.1 bloat question.

Decisive difference: progressive discovery shows tool names first and fetches full schemas on demand. Monolithic context loads every name plus every schema up front.

| Dimension | Progressive discovery | Monolithic context |
|---|---|---|
| Tokens per call | Names only, schemas on demand | All schemas, every call |
| Wrong-tool risk | Smaller visible choice set | Grows with surface size |
| First-call latency | Discovery round trips | No round trips |
| Best fit | Tool surface above ~20 (V2-D3.8) | Tiny tool set |

Winning constraints: discovery wins when the tool surface is large and tasks vary. Monolithic wins when latency binds harder than tokens and the set is small.

Losing constraints: discovery loses when every call needs every tool anyway: the discovery rounds add latency with no token saving. Monolithic loses past the wrong-tool threshold: choice accuracy falls as the list grows.

Costs: discovery pays round-trip latency per call. Monolithic pays schema tokens per call. On a 50-tool toy with 2 KB schemas: monolithic spends ~100 KB of schema tokens per call. Discovery spends one extra round trip and fetches 2 KB for the chosen tool.

Security: discovery shrinks the attack surface per call. Tools the model never sees cannot be picked by injection (V2-D5.2). Monolithic exposes every tool to every prompt.

Operational burden: discovery needs the discovery protocol and per-tool fetch logic. Monolithic needs nothing extra. Both need the pruning discipline from V2-D3.1.

Counterexample: a two-tool agent. Discovery adds a fetch round for each call and saves nothing. Monolithic wins on a tiny surface even under token pressure.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Discovery vs monolithic constraints | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: 8 tools, chat latency SLA 2 s. Winner: monolithic. Change: the tool catalog grows to 60 tools with overlapping names. Winner flips to progressive discovery. Wrong-tool picks rise with surface size.
- MP2. Base: 60 tools with discovery, each call uses 2 tools. Change: the task changes to a batch job where every call invokes all 60 tools. Winner flips to monolithic. The discovery rounds save nothing and cost latency.
- MP3. Base: monolithic context with 12 tools, tokens tight. Change: the SLA drops from 2 s to 800 ms. Winner stays monolithic but the real fix flips to static per-task subsets. Latency binds harder than tokens, so even discovery is too slow.

## Pair 9: RAG vs large-context prompting

Shared: both put knowledge in front of the model. Both live under V2-D3.5 and V2-D2.4. Both need citation or grounding checks when facts matter.

Decisive difference: RAG retrieves a few chunks at query time from an index. Large-context prompting stuffs the whole corpus into the window. RAG pays pipeline cost. Large context pays token cost per call and attention dilution.

| Dimension | RAG pipeline | Large-context prompt |
|---|---|---|
| Knowledge size | Unbounded index | Bounded by window |
| Per-call cost | Retrieval plus few chunks | Whole corpus tokens every call |
| Freshness | Re-ingest the changed docs | Re-send the whole corpus |
| Failure modes | Retrieval miss, chunk split | Dilution, lost in the middle |
| Citations | Per-chunk grounding (V2-D3.5) | Harder: which part said it |
| Best fit | Changing knowledge, citations | Tiny fixed corpus |

Winning constraints: RAG wins when knowledge changes, the corpus exceeds the window, or citations are required. Large context wins on a tiny fixed corpus where the pipeline is pure overhead.

Losing constraints: RAG loses when the corpus is 30 pages and never changes: build and maintain a pipeline to avoid sending 30 pages is absurd. Large context loses when the corpus is 30,000 pages or updates weekly.

Costs: RAG pays build plus per-call retrieval and rerank. Large context pays corpus tokens per call. On the toy: 10,000-token corpus, 1,000 calls per day, Balanced tier. Large context: 10,000 / 1M times $2 = $0.02 per call, $20 per day. RAG: 500-token chunks per call = $0.001 per call, $1 per day, plus pipeline amortized. RAG wins on cost at volume and loses on build cost at tiny scale.

Security: RAG needs the metadata ACL filter before scoring (V2-D3.6). The filter runs in code, not in the model. Large context needs the same care at assembly time: do not stuff other tenants' pages into the window.

Operational burden: RAG needs ingestion, chunking, indexing, and retrieval monitoring per stage (V2-D3.5, V2-D4.4). Large context needs none. A RAG pipeline is a system. A stuffed prompt is a bill.

Counterexample: a contract assistant over 12 standard contracts that never change. Full document in context wins. The pipeline adds stages, each a failure point, for zero retrieval benefit.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| RAG pipeline stages | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Cost toy arithmetic | Original toy, computed above | This file | Oct 6, 2026 |

Minimal pairs:

- MP1. Base: 12 fixed contracts, no changes. Winner: large context. Change: the library grows to 4,000 contracts updated weekly. Winner flips to RAG. The corpus exceeds any window and changes constantly.
- MP2. Base: RAG over a changing policy library with citations. Change: the regulator drops the citation requirement and the library freezes at 20 pages. Winner flips to large context. The pipeline's stages no longer buy anything.
- MP3. Base: large-context prompt over 50 pages, answers cite page numbers. Change: users report wrong answers from the middle of the corpus. Winner flips to RAG with structure-aware chunking. Dilution is the diagnosed layer, and fewer better-placed chunks fix it (V2-D2.4, V2-D4.4).

## Pair 10: RAG vs customization

Shared: both adapt a base model to domain knowledge. Both appear in the V2-D3.5 nearest alternatives. Both cost build effort.

Decisive difference: RAG keeps knowledge outside the weights and retrieves at runtime. Customization (fine-tuning) bakes knowledge into the weights. RAG changes the context. Fine-tuning changes the model.

| Dimension | RAG | Fine-tuning |
|---|---|---|
| Knowledge updates | Re-ingest, minutes | Retrain, hours to days |
| Citation support | Chunks ground the answer | Weights cannot cite |
| Behavior change | None: same model | Tone, format, style shift |
| Data need | Documents | Labeled examples |
| Best fit | Changing facts, citations | Stable style or format |

Winning constraints: RAG wins when facts change or citations are required. Fine-tuning wins when the need is stable behavior: format, tone, classification style, not facts.

Losing constraints: RAG loses on stable format needs: retrieval cannot teach the model your house style. Fine-tuning loses on changing facts: the weights go stale and cannot point at a source.

Costs: RAG pays pipeline build plus per-call retrieval. Fine-tuning pays training cost plus a custom model price per call. Fine-tuning on facts that change weekly is a treadmill: pay training again every week or serve stale weights.

Security: RAG keeps the ACL filter at retrieval time, per user, per query. Fine-tuning on multi-tenant data bakes tenant A's data into weights that serve tenant B. That is a cross-tenant leak by design.

Operational burden: RAG needs the pipeline plus version behavior monitoring. Fine-tuning needs the training set, eval set, and a retraining trigger. Both need regression gates on version change (V2-D2.1: upgrades are production changes).

Counterexample: a classifier that tags tickets into 40 fixed categories with stable definitions. No retrieval needed. Fine-tuning on labeled tickets wins. RAG retrieves examples that add tokens without changing the decision boundary.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Fine-tune for stable knowledge, RAG for changing | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: support answers over a weekly-changing policy library, citations required. Winner: RAG. Change: the task becomes classifying tickets into fixed categories. Winner flips to fine-tuning. The need changes from facts to behavior.
- MP2. Base: fine-tuned classifier on stable categories. Change: categories gain new members weekly and auditors demand the source rule per decision. Winner flips to RAG. Weights cannot cite and retraining weekly is a treadmill.
- MP3. Base: RAG over single-tenant docs. Change: the deployment becomes multi-tenant with strict per-tenant data walls. Winner stays RAG but the design must add the metadata ACL filter before scoring. The pair does not flip. The security layer becomes the binding constraint.

## Pair 11: retrieval failure vs model limitation

Shared: both produce a wrong answer. Both look identical to the user. The exam tests diagnosis at the right layer (V2-D4.4).

Decisive difference: retrieval failure means the right chunk never reached the model. Model limitation means the chunk arrived and the model still failed: reasoning, arithmetic, or capability gap.

| Dimension | Retrieval failure | Model limitation |
|---|---|---|
| Evidence | Right chunk absent from the trace | Right chunk present, answer still wrong |
| Fix location | Chunking, index, query, filters | Prompt, model choice, verification gate |
| Fix cost | Pipeline change | Model or architecture change |
| Recurrence | Same query class fails again | Fails across query classes |
| Best diagnostic | Trace the retrieved set | Controlled prompt with the chunk pinned |

Winning constraints: this pair is not a design choice. It is a diagnosis. The winner is the layer that the evidence names. Fix the failing component, not a proxy (V2-D4.4).

Losing constraints: treating retrieval failure as a model problem buys a bigger model that still never sees the chunk. Treating a model limitation as retrieval buys a better index that feeds the same incapable reasoner.

Costs: misdiagnosis is the most expensive line item. A model upgrade costs more per call forever and fixes nothing if the chunk never arrived. A re-chunk costs once and fixes the class.

Security: none direct. Indirect: a wrong-layer fix ships a false sense of repair. The incident recurs.

Operational burden: the V2-D4.4 habit: trace the retrieved set first. If the chunk is there, the layer is the model. If not, the layer is retrieval. One trace beats two fixes.

Counterexample: the chunk is present and the answer is right but slow. Neither diagnosis applies. The layer is performance (V2-D4.5), not correctness.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Diagnose at the right layer | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: wrong answer, retrieved set lacks the policy chunk. Diagnosis: retrieval failure. Change: the trace shows the chunk present and the answer still wrong. Diagnosis flips to model limitation. The evidence moved layers.
- MP2. Base: model limitation diagnosed, team upgrades the model. Change: the new model gets the same wrong answer on the same query class while the chunk stays missing. Diagnosis flips back to retrieval failure. The upgrade proved the layer by failing to fix it.
- MP3. Base: retrieval failure on paraphrased queries, keyword index only. Change: the team adds semantic retrieval and the class passes. Diagnosis confirmed and closed. The fix matched the layer, so the class stays fixed.

:::takeaway
Retrieval and caching are placement decisions. Put the stable prefix first, the filter before scoring, the fresh fact behind a tool call, and the fix at the failing layer.
:::
