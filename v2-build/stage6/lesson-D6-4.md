# Lesson D6-4: architecture documentation (V2-D6.4)

## 1. Problem this lesson solves

The original architect leaves. The successor inherits a RAG
pipeline with a reranker nobody chose on paper. She asks: "Why
this reranker? What did we reject?" The team answers: "There was
a meeting. Nobody remembers what was decided." She spends three
weeks re-running the evaluation the first team already ran.

Meetings evaporate. An architecture decision record survives
them. It holds the decision, the date, the alternatives, the
rejections, the assumptions, the trade-offs, the owner, the
evidence, the open issues, and the review criteria. A successor
reads it and runs the system without the original meetings.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Meetings evaporate. Records survive</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The architect leaves. The reranker choice stays, or it does not.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">"there was a meeting"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">3 weeks of re-evaluation</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">The eval runs twice. Pay twice.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">ADR-014: reranker chosen</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">3 days to read and run</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">The eval runs once. The record is read.</text>
<defs><marker id="m-d64-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d64-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">write the ADR</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Three weeks of re-work vs three days of reading.</text>
</svg>
<figcaption>Shell 4. A forgotten meeting becomes a readable record. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D1-2 owns the architecture the ADR describes. Lesson
D6-2 owns the trade-off fields the ADR records.

| Foundation | What it gives this lesson |
|---|---|
| V2-D1.2 pipeline | The decisions worth recording |
| V2-D6.2 trade-offs | Benefit, cost, risk, reversal per option |

## 3. Mental model

An ADR has nine fields. Decision: what was chosen, in one line.
Date: when it was chosen. Alternatives: the real options on the
table. Rejections: why each alternative lost, per option.
Assumptions: the guesses the decision stands on. Trade-offs:
the five fields from V2-D6.2. Owner: the person who owns the
decision now. Evidence: the eval or data that backed it. Open
issues: what stays unresolved. Review criteria: the trigger
that reopens the decision.

The standard: a successor operates the system from the ADR set
without the original meetings. If she must call the original
architect, the ADR failed.

:::takeaway
Nine fields. One test: the successor runs the system without
calling the person who built it.
:::

<figure class="fig">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="420" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The nine-field ADR</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each field answers one question the successor will ask.</text>
<rect x="24" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">"why this reranker?"</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">"what did we reject?"</text>
<rect x="44" y="232" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">"who owns this now?"</text>
<rect x="44" y="292" font-size="13" fill="#5C6B7A">Three questions. Zero records.</rect>
<rect x="400" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="124" height="36" rx="8" fill="#E7F4EF"/>
<text x="482" y="167" font-size="12" text-anchor="middle" fill="#1B2838">decision + date</text>
<rect x="552" y="144" width="124" height="36" rx="8" fill="#E7F1F8"/>
<text x="614" y="167" font-size="12" text-anchor="middle" fill="#1B2838">alt + rejections</text>
<rect x="420" y="188" width="124" height="36" rx="8" fill="#F6E7A8"/>
<text x="482" y="211" font-size="12" text-anchor="middle" fill="#1B2838">assumptions</text>
<rect x="552" y="188" width="124" height="36" rx="8" fill="#F4E6D4"/>
<text x="614" y="211" font-size="12" text-anchor="middle" fill="#1B2838">trade-offs</text>
<rect x="420" y="232" width="124" height="36" rx="8" fill="#E6E2DA"/>
<text x="482" y="255" font-size="12" text-anchor="middle" fill="#1B2838">owner</text>
<rect x="552" y="232" width="124" height="36" rx="8" fill="#F3D4D8"/>
<text x="614" y="255" font-size="12" text-anchor="middle" fill="#1B2838">evidence</text>
<rect x="420" y="276" width="256" height="36" rx="8" fill="#D9E8D3"/>
<text x="548" y="299" font-size="13" text-anchor="middle" fill="#1B2838">open issues + review criteria</text>
<defs><marker id="m-d64-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="216" x2="384" y2="216" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d64-3)"/>
<text x="360" y="200" font-size="13" text-anchor="middle" fill="#1B2838">fill all nine</text>
<text x="24" y="376" font-size="15" fill="#1B2838">The successor test decides what counts as documentation.</text>
</svg>
<figcaption>Shell 4. Three questions become nine answered fields. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Knowledge walks out the door with people. The decision logic
lives in chat threads and call recordings. The successor
cannot find it, so she re-derives it. Re-derivation takes
weeks and can reach a different answer, because the evidence
that ruled out option B is gone.

The ADR breaks the chain at the source. The decision is
written when it is made, while the evidence is fresh. The
review criteria field dates it: "reopen if rerank cost
doubles or precision drops 5 points." The successor reads,
checks the criteria, and runs. Three days instead of three
weeks.

ADR decision value: 15 days saved at $1,200 per day loaded
cost = $18,000 per handoff. Writing the ADR costs 2 hours =
$300. Payoff: $18,000 / $300 = 60 to 1.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The ADR decision value</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Two hours of writing vs fifteen days of re-derivation.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">15 days x $1,200 = $18,000</text>
<text x="44" y="200" font-size="13" fill="#5C6B7A">Successor re-runs the eval.</text>
<text x="44" y="220" font-size="13" fill="#5C6B7A">Evidence lost. Answer may differ.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">2 h x $150 = $300</text>
<text x="420" y="200" font-size="13" fill="#5C6B7A">Successor reads ADR-014.</text>
<text x="420" y="220" font-size="13" fill="#5C6B7A">Checks review criteria. Runs.</text>
<rect x="420" y="252" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="277" font-size="13" text-anchor="middle" fill="#1B2838">$18,000 / $300 = 60 to 1</text>
<defs><marker id="m-d64-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d64-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">write it now</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Write at decision time. Evidence is fresh only once.</text>
</svg>
<figcaption>Shell 4. Re-derivation cost becomes ADR writing cost. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy ADR-014. Decision: cross-encoder reranker over the top 20
retrieval hits. Date: 2026-09-18. Alternatives: no reranker,
and a bi-encoder score filter. Rejections: no reranker lost 6 points
of precision on the 500-case eval. Bi-encoder filter lost
3 points and saved little latency. Assumptions: query mix
stays short-form. Trade-offs: benefit +6 precision points.
Cost $0.012 per query rerank. Risk: added 180 ms p95. Reversal
cost: one day to remove the stage. Compliance impact: none.
Owner: retrieval lead. Evidence: eval run E-88, 2026-09-18.
Open issues: long-form queries untested. Review criteria:
reopen if rerank cost doubles or precision drops 5 points.

Mini question: "The retrieval lead leaves. A new engineer
must change the reranker stage. The repo has ADR-014 with all
nine fields. What is her correct first action? A) Re-run the
full reranker evaluation from scratch. B) Read ADR-014, check
the review criteria against current numbers, then change. C)
Remove the reranker, since its owner is gone."

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
| STEP 1 | First action for a successor on a recorded decision |
| STEP 2 | Operation: the system runs, the owner left |
| STEP 3 | Change the stage with the decision's context intact |
| STEP 4 | ADR-014 holds nine fields. The review criteria are current |
| STEP 5 | Documentation and handoff layer |
| STEP 6 | All three are feasible |
| STEP 7 | A ignores the record: re-running wastes the evidence. C breaks the system on a guess |
| STEP 8 | B uses the record as designed: read, check criteria, then change |
| STEP 9 | B needs current precision and cost numbers to test the criteria |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the ADR's purpose: the
successor operates without the original meetings. Re-running
the eval defeats the record.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| ADR | Team docs, repo | V2-D6.4 nine-field record |
| Review criteria | ADR field | V2-D6.4 decision expiry |
| Evidence link | Eval run id | V2-D6.4, V2-D4.2 eval traceability |
| Owner field | ADR | V2-D6.4, V2-D6.1 accountability |

## 7. Current limitations

ADRs rot: decisions change in code but not in the record.
Nobody writes them under deadline pressure. They can grow
into bureaucracy: a 20-page ADR for a config flag. And they
cannot capture tacit knowledge: why the team distrusted a
vendor never makes the page.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The rotting ADR</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Code moves. The record stays. The successor trusts paper.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">ADR-014: reranker kept</text>
<rect x="44" y="208" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="233" font-size="14" text-anchor="middle" fill="#1B2838">code: reranker removed</text>
<text x="44" y="260" font-size="13" fill="#5C6B7A">Record lies. Successor misled.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">ADR-015: reranker removed</text>
<rect x="420" y="208" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="233" font-size="14" text-anchor="middle" fill="#1B2838">supersedes ADR-014</text>
<text x="420" y="260" font-size="13" fill="#5C6B7A">Records chain. Never edited in place.</text>
<defs><marker id="m-d64-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d64-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">supersede, not edit</text>
<text x="24" y="312" font-size="15" fill="#1B2838">ADRs are append-only. A change is a new ADR that supersedes.</text>
</svg>
<figcaption>Shell 3. An edited record becomes a chained record. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| No records, tribal knowledge | Memory only | Two-person team, no handoffs |
| Design doc per feature | Long prose doc | Greenfield design review |
| ADR per decision (this lesson) | Nine fields, append-only | Handoffs, reversals, audits |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Successor must operate the system | ADR with all nine fields |
| Decision is reversible in a day | Light ADR: decision, date, owner, criteria |
| Audit or compliance review | ADRs plus evidence links |
| Config flag, no trade-off | Skip the ADR. Commit message suffices |

## 10. Valid-but-inferior option

Re-run the evaluation from scratch. Valid: fresh numbers are
trustworthy. Inferior here: the evidence already exists in
ADR-014, and re-running costs 15 days to reproduce a result
the team already paid for.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Fresh re-evaluation | Fresh numbers | Pays twice for known evidence |

## 11. Counterfactual where the alternative wins

The review criteria fired: rerank cost doubled and precision
dropped 6 points. The evidence is stale. Re-running the eval
wins: the ADR itself orders a fresh measurement when its
criteria fire.

| Situation | Winner | Why |
|---|---|---|
| Review criteria fired | Fresh evaluation | The ADR orders it |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Nine fields: decision, date, ______,
   rejections, ______, trade-offs, owner,
   ______, open issues, ______ criteria.
2. ADRs are ______-only.
3. The successor test: run the system
   without ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A startup acquihires a three-person ML team.
Their repo has no ADRs and 40 config flags.
Name the three flags that deserve ADRs first,
and write the review criterion for each.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D6.4 tests ADR nine fields and successor-operable documentation | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D6.4 | Sept 2026 |
| Toy arithmetic: $18,000 re-derivation vs $300 writing, 60 to 1 | Original toy, computed above | This lesson | Oct 6, 2026 |
| ADR append-only practice | General principle | Industry practice | Long-standing |

:::takeaway
Write the ADR when the decision is made. Nine fields, the
evidence link, the review criteria. The exam's successor
scenario is won by the record, not by memory.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Meetings evaporate, records survive | "there was a meeting" | ADR-014, 3 days to run | d64-f01 | SVG | Original |
| u02 | Pipeline and trade-offs carry over | -- | Prerequisite table | d64-f02 | Table | V2-D1.2, V2-D6.2 |
| u03 | Nine-field ADR | Three questions | Nine answered fields | d64-f03 | SVG | Original |
| u04 | ADR decision value | $18,000 re-derivation | $300 writing, 60 to 1 | d64-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B uses the record | d64-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d64-f06 | Table | S03, S04 |
| u07 | The rotting ADR | Record lies | Supersede, never edit | d64-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d64-f08 | Table | Original |
| u09 | Constraints decide the record | -- | Constraint verdict table | d64-f09 | Table | Original |
| u10 | Re-evaluation valid but inferior | -- | Validity vs inferiority table | d64-f10 | Table | Original |
| u11 | Fired criteria favor fresh eval | -- | Counterfactual table | d64-f11 | Table | Original |
| u12 | Nine fields from memory | Blank recall card | Filled from memory | d64-f12 | ASCII | Original |
| u13 | Transfer to acquihire | Unseen question | Key in Stage 8 | d64-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d64-f14 | Table | Mixed |
