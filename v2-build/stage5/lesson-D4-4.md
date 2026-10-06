# Lesson D4-4: diagnosis at the right layer (V2-D4.4)

## 1. Problem this lesson solves

Wrong answers spike on Monday. The team upgrades the model tier on
Tuesday. The bill doubles. The wrong answers stay. On Wednesday the
team adds a bigger prompt. Thursday: more tools. By Friday the system
is slower, pricier, and still wrong.

Every fix was a guess at a layer nobody named. The fault lived in
the prompt: a new template dropped the citation instruction. The
upgrades treated proxies. The failing component never got the fix.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Fixes at every wrong layer</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Bigger tier. Bigger prompt. More tools. Fault untouched.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="80" height="40" rx="999" fill="#E6E2DA"/>
<text x="84" y="173" font-size="12" text-anchor="middle" fill="#1B2838">tier up</text>
<rect x="132" y="148" width="80" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="12" text-anchor="middle" fill="#1B2838">prompt+</text>
<rect x="220" y="148" width="80" height="40" rx="999" fill="#E6E2DA"/>
<text x="260" y="173" font-size="12" text-anchor="middle" fill="#1B2838">tools+</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Bill x2. Errors same.</text>
<text x="44" y="232" font-size="13" fill="#5C6B7A">Fault: prompt template.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#F4E6D4"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">name the layer first</text>
<rect x="420" y="208" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="233" font-size="13" text-anchor="middle" fill="#1B2838">fix the prompt: $0</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">One fix. Fault gone.</text>
<defs><marker id="m-d44-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d44-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">diagnose first</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Name the failing layer before you buy any fix.</text>
</svg>
<figcaption>Shell 3. Three proxy upgrades become one named-layer fix. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D3-5 gives the ten RAG stages and the rule: fix the failing
component, not a proxy. Lesson D3-4 gives the trace that carries
per-stage evidence. Lesson D3-3 gives per-stage measurement.

| Foundation | What it gives this lesson |
|---|---|
| V2-D3.5 RAG stages | Named components to blame or clear |
| V2-D3.4 traces | Per-hop evidence: inputs, decisions, outputs |
| V2-D3.3 per-stage receipts | Which stage earns its slice |

## 3. Mental model

Seven layers can fail. Prompting: the instructions changed or broke.
Retrieval: the wrong chunks arrived. Model selection: the tier is too
weak or wrongly routed. Tools: the tool returned bad data or failed.
Orchestration: the agent loop lost state or planned badly. Data: the
source documents changed. Version behavior: a model or dependency
update shifted outputs.

The method is a chain. Symptom: what the user saw. Evidence: what the
trace shows per layer. Hypotheses: which layers could cause this.
Discriminating test: one test that separates the top two suspects.
Smallest correction: the least change that fixes the layer. Regression
verification: the old failure stays fixed, nothing else broke.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The diagnosis chain</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Six links. Skip one and the fix is a guess.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">symptom: wrong answers</text>
<rect x="44" y="208" width="256" height="48" rx="8" fill="#E6E2DA"/>
<text x="172" y="237" font-size="14" text-anchor="middle" fill="#1B2838">fix: upgrade tier</text>
<text x="44" y="276" font-size="13" fill="#5C6B7A">Four links skipped.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="32" rx="999" fill="#E7F1F8"/>
<text x="460" y="169" font-size="11" text-anchor="middle" fill="#1B2838">evidence</text>
<rect x="508" y="148" width="80" height="32" rx="999" fill="#F6E7A8"/>
<text x="548" y="169" font-size="11" text-anchor="middle" fill="#1B2838">hypoth</text>
<rect x="596" y="148" width="80" height="32" rx="999" fill="#F4E6D4"/>
<text x="636" y="169" font-size="11" text-anchor="middle" fill="#1B2838">test</text>
<rect x="420" y="188" width="120" height="32" rx="999" fill="#E7F4EF"/>
<text x="480" y="209" font-size="11" text-anchor="middle" fill="#1B2838">small fix</text>
<rect x="548" y="188" width="128" height="32" rx="999" fill="#D9E8D3"/>
<text x="612" y="209" font-size="11" text-anchor="middle" fill="#1B2838">regression</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Each link earns the next.</text>
<defs><marker id="m-d44-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d44-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">walk the chain</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Evidence, hypotheses, test, small fix, regression check. In order.</text>
</svg>
<figcaption>Shell 3. A skipped chain becomes a walked chain. Source: original toy.</figcaption>
</figure>

:::takeaway
The chain is: symptom, evidence, hypotheses, discriminating test,
smallest correction, regression verification.
:::

## 4. Causal mechanism

Each layer has a signature. Prompting: failures start the day a
template changed. Retrieval: citations point at wrong chunks or no
chunks. Model: failures spread across all input types at once.
Tools: the tool result in the trace is wrong or missing. Data: the
source document changed and no one re-indexed. Version: failures
start the day the provider shipped an update.

The discriminating test is the heart. Two suspects: the prompt
template changed Monday, and the retrieval index rebuilt Sunday.
Test: replay 50 failed tickets with the old prompt template and the
new index. If they pass, the prompt is guilty. If they fail, the
index is. One test. Two suspects. One survivor.

The rule the exam drills: fix the failing component, not a proxy.
Upgrading the model when the chunker is guilty is the canonical
distractor. It costs money and fixes nothing. Default to diagnosis,
never to the bigger tier.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One test, two suspects</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Old prompt plus new index. The survivor names the guilty layer.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="104" y="173" font-size="12" text-anchor="middle" fill="#1B2838">prompt?</text>
<rect x="180" y="148" width="120" height="40" rx="999" fill="#E6E2DA"/>
<text x="240" y="173" font-size="12" text-anchor="middle" fill="#1B2838">index?</text>
<text x="44" y="204" font-size="13" fill="#5C6B7A">Two suspects.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">No test.</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Tier upgraded. Bill x2.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="12" text-anchor="middle" fill="#1B2838">old prompt + new index</text>
<rect x="420" y="196" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="480" y="221" font-size="12" text-anchor="middle" fill="#1B2838">pass: prompt</text>
<rect x="548" y="196" width="120" height="40" rx="8" fill="#F3D4D8"/>
<text x="608" y="221" font-size="12" text-anchor="middle" fill="#1B2838">fail: index</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">The test names the layer.</text>
<defs><marker id="m-d44-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d44-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">run the test</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Change one suspect at a time. The survivor is the fix address.</text>
</svg>
<figcaption>Shell 3. Two suspects become one survivor after a discriminating test. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: refund agent. Monday: wrong answers jump from 5% to 25%. Sunday:
the index rebuilt. Monday morning: the prompt template shipped.

Evidence from traces: citations point at correct chunks. Retrieval
cleared. Suspects: prompt template, version behavior.

Discriminating test: replay 50 failed tickets with the old template.
44 pass. 44 / 50 = 88%. The template is guilty.

Smallest correction: restore the citation instruction line. Cost
$0. Wrong answers fall back to 5%. Regression: the 40-case
regression file from Lesson D4-2 runs clean.

Cost of the proxy path: tier upgrade doubles the bill. Toy: $360
per day becomes $720 per day. Extra $360 per day for zero fix.
The diagnosis path cost $0 and fixed it.

Mini question: "Wrong answers jump from 5% to 25% after a template
change and an index rebuild. Traces show correct citations. What is
the first action? A) Upgrade the model tier. B) Replay failed
tickets with the old template to separate the suspects. C) Add a
reranker."

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
| STEP 1 | First action on a quality spike |
| STEP 2 | Incident response on a live system |
| STEP 3 | Name the failing layer, then fix it |
| STEP 4 | Errors 25%. Two recent changes. Citations correct |
| STEP 5 | Prompting vs retrieval vs model vs index |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the rule: upgrade is a proxy fix before diagnosis. C treats a cleared layer |
| STEP 8 | B runs the discriminating test. Only B separates the suspects |
| STEP 9 | B needs the old template kept under version control |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive move is the discriminating test, and only
B runs it. A is the exam's favorite distractor: the bigger tier
before the diagnosis.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The proxy path prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Tier upgrade: $360 extra per day. Template fix: $0.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">tier up: +$360 / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">$360 to $720 per day.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Errors: 25%, unchanged.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Fix: zero.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">template fix: $0</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Old line restored.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Errors: 25% to 5%.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Regression file: clean.</text>
<defs><marker id="m-d44-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d44-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fix the layer</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The right layer is free. The wrong layer costs $360 a day.</text>
</svg>
<figcaption>Shell 4. A proxy upgrade becomes a $0 template fix. Source: original toy.</figcaption>
</figure>

:::takeaway
Never upgrade the model by default. Diagnose first. The bigger
tier is a proxy fix until evidence indicts the model layer.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Prompt template versions | Prompt store, versioned | V2-D4.4 prompting layer |
| Per-hop trace | Trace backend, one run id | V2-D4.4 evidence per layer |
| Regression file | Eval set, Lesson D4-2 | V2-D4.4 regression verification |
| Model tier changelog | Provider status plus deploy log | V2-D4.4 version behavior |

## 7. Current limitations

The trace can miss the fault: a tool that lies cleanly leaves no
trace of the lie. Two layers can fail at once, and the test
separates them only one at a time. Version behavior is opaque: the
provider may not publish what changed. The smallest correction can
be wrong twice: it fixes the symptom and hides the deeper fault.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The trace can miss a lie</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">A tool that returns clean wrong data leaves no error.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">trace: all green</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">No errors.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Answers wrong.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">verify the tool output</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Cross-check the data.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Green trace is not proof.</text>
<defs><marker id="m-d44-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d44-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">check the data</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A green trace means the plumbing worked, not that the data was true.</text>
</svg>
<figcaption>Shell 3. A green trace gains a data verification step. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Upgrade by default | Bigger tier first | Evidence already indicts the model layer |
| Rewrite the system | Full redesign | Multiple layers broken, architecture at fault |
| Diagnose then fix (this lesson) | Chain to the failing layer | Default for any production failure |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Failure starts on a change date | Suspect that layer first |
| Trace indicts one layer | Fix that layer, smallest correction |
| Two layers changed at once | Discriminating test before any fix |
| No evidence at any layer | Instrument first. No fix without evidence |

## 10. Valid-but-inferior option

Upgrade the model tier. Valid: when evidence shows the model layer
is the fault, the bigger tier is the right fix. Inferior by
default: on the toy it cost $360 extra per day and fixed nothing,
because the template was guilty.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Tier upgrade | Fixes a true model-layer fault | Guilty layer was the template |

## 11. Counterfactual where the alternative wins

Evidence shows failures spread across all input types, retrieval
is clean, the prompt is unchanged, and the provider shipped a model
update the same day. The tier upgrade wins: evidence indicted the
model layer.

| Situation | Winner | Why |
|---|---|---|
| Evidence indicts the model layer | Tier upgrade | The failing layer gets the fix |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The six links: symptom, evidence, hypotheses,
   ______ test, smallest ______, regression ______.
2. Two suspects on the toy: prompt ______ and index ______.
3. The discriminating test: old ______ plus new ______.
4. Never upgrade the model by ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A translation agent's quality drops 12 points overnight.
The provider shipped a model update at 2 a.m. The prompt
and the glossary are unchanged. Retrieval traces show
correct glossary hits.
Name the prime suspect layer and the one test that
confirms it.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D4.4 tests layer diagnosis, fix the failing component, no default model upgrade | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D4.4 | Sept 2026 |
| Toy cost and replay arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Layer signatures | General principle | Operations practice | Long-standing |

:::takeaway
The exam's D4.4 trap is the bigger tier. The scenario names a
change date. Follow the date, run the test, fix the layer.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Fixes at every wrong layer | Tier up, prompt up, tools up | One named-layer fix | d44-f01 | SVG | Original |
| u02 | RAG, trace, receipts carry over | -- | Prerequisite table | d44-f02 | Table | V2-D3.5, V2-D3.4, V2-D3.3 |
| u03 | Diagnosis chain | Skipped chain | Six links walked | d44-f03 | SVG | Original |
| u04 | One test, two suspects | Two suspects, no test | Survivor names the layer | d44-f04 | SVG | Original |
| u05 | Proxy path prices itself | +$360 per day, no fix | $0 template fix | d44-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B runs the test | d44-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d44-f06 | Table | S03, S04 |
| u07 | Trace can miss a lie | All green trace | Verify the data | d44-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d44-f08 | Table | Original |
| u09 | Constraints decide the fix | -- | Constraint verdict table | d44-f09 | Table | Original |
| u10 | Tier upgrade valid but inferior | -- | Validity vs inferiority table | d44-f10 | Table | Original |
| u11 | Evidence flips the winner | -- | Counterfactual table | d44-f11 | Table | Original |
| u12 | Chain facts from memory | Blank recall card | Filled from memory | d44-f12 | ASCII | Original |
| u13 | Transfer to translation agent | Unseen question | Key in Stage 8 | d44-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d44-f14 | Table | Mixed |
