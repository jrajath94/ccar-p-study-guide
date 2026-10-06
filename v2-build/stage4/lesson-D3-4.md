# Lesson D3-4: observability at scale (V2-D3.4)

## 1. Problem this lesson solves

An agent fleet runs 10,000 tasks per day. Each task makes model
calls, retrieval calls, and tool calls. One task refunds $8,000 to the
wrong account. The team opens the logs. They find model prompts and
model answers. They do not find which retrieval result fed the answer,
which tool call issued the refund, how many retries fired, or what the
task cost.

The failure cannot be replayed. The cost cannot be attributed. The
fix cannot be targeted, because the team cannot see the trajectory.
They log text. They do not trace the run.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Text logs, no trajectory</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The refund fired. The trail stops at the model answer.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">prompt and answer logged</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">retrieval, tools: missing</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Which call refunded? Unknown.</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Replay impossible.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">full trace, one id</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">cost per task attached</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Tool call #4 refunded.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Replay from the trace.</text>
<defs><marker id="m341" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m341)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">trace every hop</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A run you cannot replay is a run you cannot fix.</text>
</svg>
<figcaption>Shell 3. Text logs become a traced trajectory with cost. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson 7-1A | Traces with one request id across model, tools, retries |
| Lesson 7-3A | Tokens are the cost unit |
| Lesson D1-2 | Pipeline stages, each a hop that must emit a trace |

## 3. Mental model

Observability answers one question: can you reconstruct the run? A
reconstructable run has four records per hop. The input the hop
received. The decision the hop made. The output the hop produced. The
cost the hop spent. One id ties every hop of one run together.

At scale the question gets harder. Ten thousand runs per day times
fifty hops per run is 500,000 spans per day. Full detail on all of
them is unaffordable. The model becomes: trace everything cheaply,
keep everything briefly, sample deeply, and reconstruct on demand.
Metrics watch the herd. Traces dissect the sick animal.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Reconstruct the run</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One id. Every hop. Input, decision, output, cost.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">run id on 2 of 6 hops</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">cost: not recorded</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Hops float free.</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Reconstruction fails.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">run id on 6 of 6 hops</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">cost per hop recorded</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">One id binds the hops.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Replay possible.</text>
<defs><marker id="m343" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m343)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">propagate one id</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The id is the thread. Without it the hops are loose beads.</text>
</svg>
<figcaption>Shell 4. One propagated id binds every hop of the run. Source: original toy.</figcaption>
</figure>

:::takeaway
Trace the hops that change state or spend money: model calls,
retrieval, tools, queues, dependencies, retries, errors. One id
binds them. Cost rides along.
:::

## 4. Causal mechanism

The trace surface has nine parts. The exam names all nine. Each part
answers a different failure question.

Model calls: which model, which prompt version, token counts in and
out, latency. Answers "what did the model see and say."

Retrieval: the query, the index version, the documents returned, the
scores. Answers "where did the facts come from."

Tools: the tool name, the arguments, the result, the approval record.
Answers "what acted on the world."

Queues: wait time before each hop. Answers "where did the tail
latency hide."

Dependencies: downstream service, status, latency. Answers "who else
was slow or down."

Retries: attempt count per hop, backoff, idempotency key. Answers
"did it run twice."

Errors: the error, the hop, the handling. Answers "what broke and
what caught it."

Trajectories: the ordered hop list, the plan the agent followed.
Answers "what path did it take."

Cost and tokens: per hop and per run, in dollars. Answers "what did
this run cost and which hop spent it."

Two mechanisms keep this affordable. Sampling: keep full traces for
a fraction of runs, keep skeletons for the rest, and always keep full
traces for errors. Redaction: strip secrets and PII before the trace
leaves the trust boundary, because traces become a data store of
their own.

## 5. Minimal worked example

Toy: the refund agent. 10,000 tasks per day. Each task averages 6
model calls, 4 retrieval calls, 5 tool calls: 15 hops. Full trace per
hop averages 2,000 bytes. The team must find which tool call issued a
wrong $8,000 refund, and which task type costs the most.

Mini question: "A wrong refund fired somewhere in a 15-hop agent run.
The team has model prompts and answers only. Which observability
change best enables root-cause analysis? A) Log full prompts for all
runs. B) Emit structured traces with one run id across model calls,
retrieval, tools, queues, retries, and errors, with token and cost
per hop. C) Raise log retention from 7 to 90 days."

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
| STEP 1 | Question asks: control. Best observability change for root cause |
| STEP 2 | Stage: incident response on a live fleet |
| STEP 3 | Objective: find which hop issued the refund, at what cost |
| STEP 4 | Hard constraints: 10,000 runs per day, 15 hops per run |
| STEP 5 | Layer: observability across the trajectory |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | None violate stated constraints. All survive to comparison |
| STEP 8 | B traces the acting hops: tools, retries, cost. A logs only prompts. C keeps the same blind data longer |
| STEP 9 | B's consequence: trace volume. 10,000 x 15 x 2,000 bytes = 300,000,000 bytes per day = 300 MB per day. Sampling handles it |
| STEP 10 | B alone names the refunding hop. A and C cannot |

Verdict: B. The arithmetic: full traces cost 300 MB per day for the
fleet, and sampling cuts that further. The question asks for root
cause, and only the trajectory with per-hop cost answers it. More
prompt text (A) and longer retention of blind data (C) are the exam's
"more logging" trap from Lesson D3-1 in new clothes.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The trace volume prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">10,000 runs x 15 hops x 2,000 bytes per hop.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">prompts only</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">Cheap. Blind.</text>
<text x="44" y="240" font-size="13" fill="#5C6B7A">Refund hop: unknown.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">300 MB per day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">10,000 x 15 x 2,000 B.</text>
<text x="420" y="240" font-size="13" fill="#5C6B7A">Refund hop: named.</text>
<defs><marker id="m345" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m345)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">trace the hops</text>
<text x="24" y="312" font-size="15" fill="#1B2838">300 MB per day buys the answer that prompts alone cannot give.</text>
</svg>
<figcaption>Shell 4. Full traces cost 300 MB per day and name the acting hop. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Spans with one trace id | OpenTelemetry-style tracing | V2-D3.4 end-to-end reconstructability |
| Request and run ids | Application code, Lesson 7-1A | V2-D3.4 hop binding |
| Token usage per call | Model API response | V2-D3.4 cost per hop |
| Sampled retention | Trace backend config | V2-D3.4 scale control |

## 7. Current limitations

Full traces of everything are unaffordable at large scale. Sampling
misses rare failures. The one run you need may be the one you
dropped. Traces carry secrets and PII, so they need their own access
control and redaction. Clock skew across services muddies ordering.
Trace volume itself needs monitoring, or the observer becomes the
outage.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Sampled deep traces (this lesson) | Full detail on a fraction | Agent fleets, multi-hop runs |
| Metrics plus skeletons | Counts and timings only | High volume, simple tasks |
| Full traces on errors only | Detail where it hurts | Rare failures, tight budget |
| Prompt logging only | Text in and out | Single-call tasks, no tools |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Must replay a failed run | Full trajectory with one id |
| Must attribute cost per task | Tokens and dollars per hop |
| Volume forbids full traces | Sample deep, skeleton the rest, keep all errors |
| Traces cross a trust boundary | Redact secrets and PII first |
| Single model call, no tools | Prompt logging suffices |

## 10. Valid-but-inferior option

Raise log retention from 7 to 90 days. Valid: longer history helps
trend analysis and compliance. Inferior for this incident: ninety
days of blind data still cannot name the refunding hop. Retention
extends what you have. It does not add what you lack.

## 11. Counterfactual where the alternative wins

A single-call classification task. One model call, no tools, no
retrieval. Prompt logging wins: the trajectory is one hop, the cost
is one call, and full tracing machinery adds nothing. The run is
trivially reconstructable.

| Situation | Winner | Why |
|---|---|---|
| One model call, no tools | Prompt logging | One hop needs no trajectory |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Four records per hop: ______, ______, ______, ______.
2. 10,000 x 15 x 2,000 bytes = ______ MB per day.
3. Metrics watch the ______. Traces dissect the ______.
4. Redact ______ before traces cross a boundary.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A travel agent books flights through 4 tools. One booking
double-charged a customer. The trace shows 2 charge attempts
with the same idempotency key.
Name the hop to inspect first and the two fields that prove
the double charge.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Trace model calls, retrieval, tools, queues, dependencies, retries, errors, trajectories, cost, tokens | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D3.4 | Sept 2026 |
| One request id across hops, retry in caller with idempotency key | General principle, taught in Lesson 7-1A | This build | Oct 6, 2026 |
| Toy arithmetic: 300 MB per day | Original toy, computed above | This lesson | Oct 6, 2026 |
| Sampling and redaction as scale controls | General principle | Observability canon | Long-standing |

:::takeaway
The exam's D3.4 trap offers more text logs or longer retention.
Both keep the blind spot. The fix is the trajectory: every
state-changing hop, one id, cost attached.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Text logs, no trajectory | Prompts only | Full trace, one id, cost | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | 7-1A, 7-3A, D1-2 |
| u03 | Reconstruct the run | Id on 2 of 6 hops | Id on 6 of 6, cost per hop | f03 | SVG | Original |
| u04 | Nine trace parts | Blind spots | Part per failure question | f04 | Text | Spec + original |
| u05 | 10-step method picks B | Three options | B: trajectory with cost | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Sampling and redaction limits | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Longer retention inferior here | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Single call favors prompt logging | -- | Counterfactual table | f11 | Table | Original |
| u12 | Four records from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to travel agent | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
