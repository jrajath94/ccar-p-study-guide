# Lesson D3-5: the RAG pipeline (V2-D3.5)

## 1. Problem this lesson solves

A team wires "search over the docs" into their agent. It becomes one
box labeled "RAG." Answers cite the wrong section. A table splits
across two chunks, and the numbers land in different answers. Nobody
can say which stage failed, because nobody named the stages.

The fix lands at the wrong layer twice. The team enlarges the chunks.
Citations get worse. The team swaps the embedding model. Nothing
changes. The real fault is the chunker: it cuts mid-table. Until the
pipeline carries named stages, every fix is a guess.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One box, no stages</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The chunker cuts a table in half. The team blames the model.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">"RAG" box</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Wrong citation.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Which stage failed? Unknown.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Fix: bigger chunks. Worse.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">10 named stages</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">chunker cuts at headings</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Table stays whole.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Citation checks pass.</text>
<defs><marker id="m351" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m351)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">name the stages</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Named stages turn guesses into targeted fixes.</text>
</svg>
<figcaption>Shell 3. One "RAG" box becomes ten named stages. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson 7-3A | Retrieval vs parametric knowledge. Generation samples. It does not verify |

Lesson 7-3A decided when retrieval beats the model's memory. This
lesson builds the retrieval machine itself.

## 3. Mental model

Ten stages, in order. Ingestion takes documents in. Parsing extracts
text and structure. Chunking cuts text into pieces. Metadata tags
each piece. Indexing files the pieces for search. Retrieval pulls
candidate pieces for a query. Rerank reorders the candidates.
Assembly builds the context. Generation writes the answer. Grounding
checks every claim against the pieces.

Each stage owns its failure mode. A wrong answer is never "the RAG
failed." It is the chunker, the retriever, the assembler, or the
generator. The exam tests this layer discipline: fix the failing
component, not a proxy.

Chunking follows the document, not the ruler. Cut at structure:
headings, sections, table boundaries. Size follows the query type:
fact lookup wants small tight chunks, synthesis wants larger chunks
with context. A fixed 500-token cut through a table is a ruler
decision. The document is the authority.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Cut at structure, not at 500</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The ruler cuts the table. The document keeps it whole.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">fixed 500-token cuts</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">table split in two</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Numbers land apart.</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Citations point wrong.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">cuts at headings</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">table kept whole</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">One chunk, one table.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Size follows query type.</text>
<defs><marker id="m353" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m353)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">follow the document</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Structure decides the cut. Query type decides the size.</text>
</svg>
<figcaption>Shell 4. Fixed cuts become structure-aware cuts. Source: original toy.</figcaption>
</figure>

:::takeaway
Ten stages. Each owns its failures. Chunk by document structure
and query type. Ground every claim with a citation check.
:::

## 4. Causal mechanism

The stages form a chain, and each link transforms the data. Ingestion
collects the documents. Parsing turns PDFs, HTML, and slides into
clean text with structure: headings, tables, lists. Chunking cuts the
text into retrievable pieces. Metadata records the source, the
section, the date, the access level. Indexing builds the search
structures over chunks. Retrieval scores chunks against the query and
returns candidates. Rerank scores the candidates harder and keeps the
top few. Assembly packs them into context with citations attached.
Generation writes the answer from the packed context. Grounding
checks each claim against its cited chunk and rejects the ungrounded.

Three causal facts matter for the exam. First, errors compound
downstream. A bad chunk poisons retrieval, rerank, assembly, and the
answer. Fix upstream first. Second, metadata is a first-class
citizen. Source, date, and access level enable filters, freshness,
and the security scoping of Lesson 7-2A. Third, grounding is a
deterministic check, not a model judgment. A script verifies that
each claim has a supporting cited span. The model does not grade its
own homework.

## 5. Minimal worked example

Toy: 100 policy documents. Each averages 20 sections. Chunking at
section boundaries gives 2,000 chunks. Each chunk averages 400
tokens. A query asks for the refund limit. Ten chunks truly answer
it. Retrieval returns 8 chunks. Six of the eight answer the query.

Precision: 6 relevant of 8 returned = 6 / 8 = 0.75. Recall: 6
relevant of 10 existing = 6 / 10 = 0.60. The grounding check finds
one claim with no cited span and rejects it.

Mini question: "A RAG agent cites the wrong policy section. The
chunks cut tables in half. Which fix addresses the root cause? A)
Swap to a larger embedding model. B) Re-chunk at document structure
boundaries and keep tables whole. C) Add a bigger generation tier."

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
| STEP 1 | Question asks: root cause. Fix at the failing layer |
| STEP 2 | Stage: operation. The pipeline is live and misfiring |
| STEP 3 | Objective: correct citations from whole tables |
| STEP 4 | Hard constraints: none stated beyond correct citations |
| STEP 5 | Layer: chunking, upstream of retrieval |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | None violate stated constraints. All survive to comparison |
| STEP 8 | B fixes the named fault: tables split by the chunker. A and C change stages the scenario never indicted |
| STEP 9 | B's consequence: re-index 2,000 chunks. One-time cost, upstream fix |
| STEP 10 | B alone answers the root cause. A and C are proxy fixes |

Verdict: B. The scenario names the chunker as the fault. The
verbatim method warns against the bigger-model reflex: the answer is
fix retrieval, not a larger model. Precision 0.75 and recall 0.60
are the receipts that say retrieval is the weak stage, and the weak
stage starts at the chunker.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Precision and recall price the stage</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">10 relevant chunks exist. Retrieval returns 8. 6 are relevant.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">precision: 6 / 8 = 0.75</text>
<rect x="44" y="208" width="256" height="48" rx="8" fill="#E6E2DA"/>
<text x="172" y="237" font-size="14" text-anchor="middle" fill="#1B2838">recall: 6 / 10 = 0.60</text>
<text x="44" y="280" font-size="13" fill="#5C6B7A">Split tables hide answers.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">precision: 8 / 8 = 1.00</text>
<rect x="420" y="208" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="237" font-size="14" text-anchor="middle" fill="#1B2838">recall: 9 / 10 = 0.90</text>
<text x="420" y="280" font-size="13" fill="#5C6B7A">Whole tables surface answers.</text>
<defs><marker id="m355" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m355)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fix the chunker</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Upstream fixes move both precision and recall. Downstream swaps do not.</text>
</svg>
<figcaption>Shell 4. Structure-aware chunking lifts precision and recall. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Chunk text plus metadata | Application pipeline | V2-D3.5 chunking and metadata |
| Vector and keyword indexes | Index layer | V2-D3.5 indexing, V2-D3.6 strategies |
| Citation spans in the answer | Application assembly | V2-D3.5 grounding checks |

## 7. Current limitations

Chunking loses cross-chunk context. A claim that needs two sections
may never sit in one chunk. Overlap between chunks helps and costs
tokens. Indexes go stale. A changed document needs re-ingestion.
Parsing is lossy: scanned PDFs, merged cells, and footnotes all
degrade. Grounding checks catch ungrounded claims but cannot catch a
well-cited wrong chunk.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| RAG pipeline (this lesson) | Staged retrieval plus grounding | Changing knowledge, citations needed |
| Fine-tuned model | Knowledge in weights | Stable knowledge, Lesson 7-3A decision |
| Full document in context | No pipeline at all | Tiny fixed corpus, Lesson D2-4 context |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Answers need citations | Full pipeline with grounding checks |
| Tables or structured sections split | Re-chunk at structure boundaries |
| Wrong answer, right pipeline shape | Diagnose per stage, fix upstream first |
| Knowledge changes weekly | Re-ingestion cadence beats fine-tuning |
| Tiny fixed corpus | Full document in context, skip the pipeline |

## 10. Valid-but-inferior option

Swap to a larger embedding model. Valid: better embeddings can lift
recall on paraphrased queries. Inferior here: the scenario names
split tables, an upstream chunking fault. Better vectors over broken
chunks still retrieve broken chunks. Fix the failing component, not
a proxy.

## 11. Counterfactual where the alternative wins

Fifty fixed macros, frozen text, no changes ever. Full document in
context wins: the corpus fits in the window, there is no pipeline to
build, no index to refresh, and citations point at whole documents.
The pipeline is machinery with no job.

| Situation | Winner | Why |
|---|---|---|
| Tiny frozen corpus | Full document in context | No pipeline cost, nothing to refresh |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The ten stages in order: ______, ______, ______, ... .
2. Chunk by ______ and size by ______.
3. Precision = ______ / ______. Recall = ______ / ______.
4. Grounding is a ______ check, not a model judgment.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A legal assistant cites the wrong clause. The pipeline
chunks contracts at fixed 1,000-token cuts. Clauses span
the cuts. Retrieval precision is 0.55.
Name the failing stage and the chunking rule that fixes it.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Ten-stage pipeline, chunking by document structure and query type, grounding and citation checks | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D3.5 | Sept 2026 |
| Retrieval vs parametric knowledge decision | General principle, taught in Lesson 7-3A | This build | Oct 6, 2026 |
| Toy arithmetic: precision 0.75, recall 0.60, 2,000 chunks | Original toy, computed above | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D3.5 trap fixes the wrong stage. Name the ten stages,
find the failing one, fix upstream first. When the scenario names
the chunker, the answer is the chunker.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | One box, no stages | "RAG" box, wrong fix | 10 named stages, chunker fixed | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | 7-3A |
| u03 | Cut at structure | Fixed 500-token cuts | Cuts at headings, tables whole | f03 | SVG | Original |
| u04 | Chain with upstream errors | Guessing | Fix upstream first, metadata, grounding | f04 | Text | Original |
| u05 | 10-step method picks B | Three options | B: re-chunk at structure | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Cross-chunk loss and staleness | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Bigger embeddings inferior here | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Tiny corpus favors full context | -- | Counterfactual table | f11 | Table | Original |
| u12 | Ten stages from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to legal assistant | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
