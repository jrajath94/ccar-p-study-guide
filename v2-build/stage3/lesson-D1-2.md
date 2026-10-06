# Lesson D1-2: end-to-end architecture (V2-D1.2)

## 1. Problem this lesson solves

A team wires a prompt straight to the model and the model straight to the
user. It works in the demo. In production, bad input reaches the model,
bad output reaches the user, and no stage can say where it broke. The
fix is not a better prompt. The fix is a pipeline with named gates.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Gates, not hopes</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One wire. No gates. No address for a failure.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="72" height="40" rx="999" fill="#E6E2DA"/>
<text x="80" y="173" font-size="13" text-anchor="middle" fill="#1B2838">ask</text>
<rect x="140" y="148" width="72" height="40" rx="8" fill="#E7F1F8"/>
<text x="176" y="173" font-size="13" text-anchor="middle" fill="#1B2838">model</text>
<rect x="236" y="148" width="72" height="40" rx="999" fill="#E6E2DA"/>
<text x="272" y="173" font-size="13" text-anchor="middle" fill="#1B2838">user</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Bad input in. Bad output out.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">No gate. No trace.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="460" y="171" font-size="12" text-anchor="middle" fill="#1B2838">validate</text>
<rect x="508" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">retrieve</text>
<rect x="596" y="148" width="80" height="36" rx="999" fill="#F4E6D4"/>
<text x="636" y="171" font-size="12" text-anchor="middle" fill="#1B2838">model</text>
<rect x="464" y="192" width="80" height="36" rx="999" fill="#E7F4EF"/>
<text x="504" y="215" font-size="12" text-anchor="middle" fill="#1B2838">verify</text>
<rect x="552" y="192" width="80" height="36" rx="999" fill="#E7F4EF"/>
<text x="592" y="215" font-size="12" text-anchor="middle" fill="#1B2838">guard</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Each gate owns one job.</text>
<text x="420" y="276" font-size="13" fill="#5C6B7A">Each failure has an address.</text>
<defs><marker id="m-d12-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d12-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">name the gates</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A failure with an address gets a fix. A failure without one gets a guess.</text>
</svg>
<figcaption>Shell 3. One wire becomes named gates. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-1A gives caller-side reliability: timeout, retry with a key,
backoff. Lesson 7-2A gives enforcement before context: checks run in
code, before the model sees data.

| Foundation | What it gives this lesson |
|---|---|
| §7.1 systems | Retries live in the caller. Each hop emits a trace |
| §7.2 security | The trust boundary sits before context assembly |

## 3. Mental model

Think of seven gates in a row. Input enters. Validation rejects the
malformed. Context and retrieval fetch the facts. The model and its
tools draft the answer. Verification checks the draft against the
source. Output guards scrub the unsafe. Feedback logs the run for
tomorrow. Each gate has one job. A gate never does another gate's job:
the model does not validate input, and the prompt does not enforce
access.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Seven gates, seven jobs</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One row of gates. Each gate owns exactly one job.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">prompt plus model</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Validation: hoped for.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Verification: hoped for.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Feedback: none.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="88" height="36" rx="999" fill="#E7F1F8"/>
<text x="464" y="171" font-size="12" text-anchor="middle" fill="#1B2838">input</text>
<rect x="516" y="148" width="88" height="36" rx="999" fill="#E7F1F8"/>
<text x="560" y="171" font-size="12" text-anchor="middle" fill="#1B2838">valid</text>
<rect x="612" y="148" width="72" height="36" rx="999" fill="#E7F1F8"/>
<text x="648" y="171" font-size="12" text-anchor="middle" fill="#1B2838">facts</text>
<rect x="420" y="192" width="88" height="36" rx="999" fill="#F4E6D4"/>
<text x="464" y="215" font-size="12" text-anchor="middle" fill="#1B2838">draft</text>
<rect x="516" y="192" width="88" height="36" rx="999" fill="#E7F4EF"/>
<text x="560" y="215" font-size="12" text-anchor="middle" fill="#1B2838">check</text>
<rect x="612" y="192" width="72" height="36" rx="999" fill="#E7F4EF"/>
<text x="648" y="215" font-size="12" text-anchor="middle" fill="#1B2838">ship</text>
<rect x="476" y="236" width="144" height="36" rx="999" fill="#E6E2DA"/>
<text x="548" y="259" font-size="12" text-anchor="middle" fill="#1B2838">feedback loop</text>
<text x="420" y="296" font-size="13" fill="#5C6B7A">Input, valid, facts, draft, check, ship.</text>
<defs><marker id="m-d12-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d12-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">split the jobs</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Seven gates. Seven jobs. No gate borrows another gate's job.</text>
</svg>
<figcaption>Shell 3. One model box becomes seven gates with one job each. Source: original toy.</figcaption>
</figure>

:::takeaway
The pipeline is: input, validation, context and retrieval, model and
tools, verification, output, feedback. Verification is a stage, not a
wish.
:::

## 4. Causal mechanism

A request crosses a trust boundary twice. Untrusted input enters: user
text, files, tool results. The boundary sits before context assembly:
validation and authorization run here, in code. Inside the boundary,
the model drafts with retrieved facts. Before the answer leaves, a
second check runs: verification against the source, output guards for
the unsafe. The system of record holds the truth the draft is checked
against. State lives in the application, not in the model: the model
is stateless, so retries, fallbacks, and conversation memory are code
the team owns. Every hop emits a trace, so a failure carries the name
of its gate.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The boundary sits before the model</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Untrusted on the left. Verified on the right. Code holds the line.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">user text goes straight in</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No boundary.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Model sees raw input.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">State hides in the chat.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="112" height="40" rx="999" fill="#F3D4D8"/>
<text x="476" y="173" font-size="12" text-anchor="middle" fill="#1B2838">untrusted</text>
<rect x="564" y="148" width="112" height="40" rx="999" fill="#E7F4EF"/>
<text x="620" y="173" font-size="12" text-anchor="middle" fill="#1B2838">verified</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">trust boundary: code checks</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">State lives in the app.</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">The model stays stateless.</text>
<defs><marker id="m-d12-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d12-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">draw the line</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Checks run in code at the boundary. The model never guards itself.</text>
</svg>
<figcaption>Shell 4. Raw input gains a trust boundary held by code. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: support answer bot. 50,000 answers per day on the Fast tier ($1
in, $5 out per 1M, S10-S12, Oct 2026).

Token budget per call: validation 200, retrieval 3 chunks of 500 =
1,500, system 1,200, user 300. Input total: 200 + 1,500 + 1,200 + 300
= 3,200. Output cap 800. Cost: in 3,200 / 1,000,000 x $1 = $0.0032.
Out 800 / 1,000,000 x $5 = $0.004. Total $0.0072 per call. Per day:
50,000 x $0.0072 = $360. Per month: $360 x 30 = $10,800.

Verification is deterministic: the citation check compares each claim
against the retrieved chunks in code. The output guard scrubs account
numbers with a pattern match. The feedback gate logs the trace: input
hash, chunk ids, draft, check result.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Budget the pipeline, not the call</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Fast tier. 3,200 in, 800 out. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">model call: unknown cost</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">No stage budget.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">No per-stage tokens.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Bill arrives as a shock.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$0.0072 per call</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">in: 3,200/1M x $1 = $0.0032</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">out: 800/1M x $5 = $0.004</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">50,000 x $0.0072 x 30 = $10,800</text>
<defs><marker id="m-d12-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d12-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">count each stage</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The pipeline budget turns the monthly bill into a plan.</text>
</svg>
<figcaption>Shell 4. Stage token counts become a $10,800 monthly plan. Source: original toy.</figcaption>
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

Mini question: "A support bot gives wrong answers twice a week. The team proposes a bigger model. What is the first action? A) Switch to the most capable tier. B) Instrument each stage and find which stage fails. C) Add a human reviewer on every answer."

| Step | Action on this question |
|---|---|
| STEP 1 | First action on a quality failure |
| STEP 2 | Operation: production issue |
| STEP 3 | Restore correct answers |
| STEP 4 | Wrong answers twice a week. Fix the cause, not a proxy |
| STEP 5 | Application layer: the pipeline stages |
| STEP 6 | All three are technically feasible |
| STEP 7 | None break a hard constraint, but A and C skip the diagnosis |
| STEP 8 | B matches: the failing stage decides the fix |
| STEP 9 | B needs per-stage traces. The pipeline already emits them |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive move is diagnosis at the right stage before any change, and only B names it.

:::takeaway
When a stem shows a failure, the first action is diagnosis at the right layer. A bigger model, more reviewers, or more logging are proxy fixes until the failing stage is named.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Trust boundary | Code before context assembly | V2-D1.2 architecture, V2-D5.1 guardrails |
| System of record | Source database or document store | V2-D1.2 verification, V2-D3.5 grounding |
| Caller-side retry | Application code, §7.1 | V2-D1.2 retries and fallbacks |
| Per-stage traces | Request id across hops | V2-D3.4 observability at scale |
| State in the app | Session store, queue | V2-D1.2 state, V2-D1.4 checkpointing |

## 7. Current limitations

Every gate adds latency and is itself a failure point. Seven gates mean
seven places to break, seven timeouts to set, seven traces to read. The
pipeline cannot fix a bad model or bad retrieval: gates arrange work,
they do not create quality. And a gate set too strict rejects good
answers: verification tuned for zero misses also blocks the unusual but
correct.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Gates cost too</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each gate adds latency and a failure point. Count them.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">7 gates, 0 measured</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Latency: unknown.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Strict gates block good answers.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">7 gates, each budgeted</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Each gate gets a latency slice.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Gates tuned on real misses.</text>
<defs><marker id="m-d12-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d12-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">budget each gate</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Gates are load-bearing. Budget their latency and tune them on misses.</text>
</svg>
<figcaption>Shell 3. Unmeasured gates become budgeted gates. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Single call | Prompt to model to user | Demo, no users, no side effects |
| Seven gates (this lesson) | Named stages with checks | Production, hard constraints, audit needs |
| Agent loop | Model plans each step | Open-ended tasks, dynamic planning needed |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Money moves or PII leaves | Verification and output guards are mandatory |
| Audit must reconstruct the run | Per-stage traces with one request id |
| The model is stateless | State, retries, and fallbacks live in the app |
| Latency budget is tight | Fewer gates, each with a latency slice |

## 10. Valid-but-inferior option

Add a human reviewer on every answer. Valid: catches errors the gates
miss. Inferior: on the toy, 50,000 answers per day at 30 seconds each
is 1,500,000 seconds = 417 reviewer hours per day. It also fixes
nothing: the failing stage keeps failing, and reviewers without the
retrieved chunks lack real decision context.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Reviewer on every answer | Catches gate misses | 417 reviewer hours per day. Cause unfixed |

## 11. Counterfactual where the alternative wins

Internal demo for three engineers. No users, no side effects, no PII.
Seven gates cost a week of build for a demo that runs ten times. The
single call wins: the constraints that justify gates are absent.

| Situation | Winner | Why |
|---|---|---|
| Internal demo, no users, no side effects | Single call | No constraint justifies the gates |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The seven gates: input, validation, context and
   retrieval, model and tools, ______, output, ______.
2. The trust boundary sits ______ context assembly.
3. State lives in the ______, not the model.
4. The toy pipeline costs $______ per month.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A clinic drafts discharge notes. A wrong dose harms a patient.
An auditor must replay any note from six months ago.
Name the gates. Name what the trace must carry.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D1.2 tests the full pipeline, trust boundaries, state, retries, telemetry | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Tier prices $1/$5 in/out per 1M (Fast) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy pipeline arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Seven-gate pipeline shape | General principle | Architecture practice | Long-standing |
| 30 seconds per human review | Not in source | -- | -- |

:::takeaway
Draw the pipeline before you defend it. Name every gate, its job, and
its latency slice. The exam tests whether each check sits at the right
stage.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | One wire has no address for failure | Prompt to model to user | Named gates | d12-f01 | SVG | Original |
| u02 | Reliability and boundary carry over | -- | Prerequisite table | d12-f02 | Table | §7.1, §7.2 |
| u03 | Seven gates, seven jobs | Prompt plus model | Input, valid, facts, draft, check, ship | d12-f03 | SVG | Original |
| u04 | Boundary sits before the model | Raw input straight in | Code checks at the boundary | d12-f04 | SVG | Original |
| u05 | Pipeline budget | Unknown model cost | $0.0072 per call, $10,800 per month | d12-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches diagnosis first | d12-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d12-f06 | Table | S03, S04 |
| u07 | Gates cost too | 7 gates, 0 measured | Each gate budgeted | d12-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d12-f08 | Table | Original |
| u09 | Constraints decide the gates | -- | Constraint verdict table | d12-f09 | Table | Original |
| u10 | Reviewer on all is valid but inferior | -- | 417 reviewer hours per day | d12-f10 | Table | Original |
| u11 | Demo favors the single call | -- | Counterfactual table | d12-f11 | Table | Original |
| u12 | Seven gates from memory | Blank recall card | Filled from memory | d12-f12 | ASCII | Original |
| u13 | Transfer to discharge notes | Unseen question | Key in Stage 8 | d12-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d12-f14 | Table | Mixed |
