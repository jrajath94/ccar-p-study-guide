# Lesson D6-5: lifecycle phases (V2-D6.5)

## 1. Problem this lesson solves

A team finishes the agent. Nobody ran discovery. Nobody wrote
the design down. The handoff doc says "it works on my machine."
In production the error rate triples, so the team adds more
monitoring dashboards. The dashboards show the errors clearly.
Nobody can fix them, because the missing discovery never named
the true requirements.

Later-phase work cannot substitute for unfinished earlier
phases. Monitoring a wrong design produces beautiful charts of
the wrong behavior. The lifecycle runs in order: discovery,
design, handoff, monitoring, iteration. Each phase has an exit
gate. Skipping a gate moves the debt downstream, where it
costs more.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Dashboards cannot fix a skipped design</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">More monitoring on a wrong design measures the wrong thing well.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">5 dashboards added</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">errors still triple</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Monitoring substituted for design.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">go back: run discovery</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">design, then monitor</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Phases run in order. No substitution.</text>
<defs><marker id="m-d65-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d65-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">return to phase 1</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The fix is upstream, not on the dashboard.</text>
</svg>
<figcaption>Shell 3. Substituted monitoring becomes ordered phases. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lessons D6-1 through D6-4 each own one phase. This lesson owns
the order and the gates between them.

| Foundation | What it gives this lesson |
|---|---|
| V2-D6.1 discovery | Phase 1: questions and owners |
| V2-D6.2 trade-offs | Phase 2: priced design options |
| V2-D6.4 ADRs | Phase 3: handoff that survives people |
| V2-D6.3 feedback | Phase 4: triggers that feed phase 5 |

## 3. Mental model

Five phases, four gates. Discovery asks and records. Gate 1:
every requirement has a metric, a threshold, and an owner.
Design proposes and prices. Gate 2: options compared on the
five fields, ADRs written. Handoff transfers operations.
Gate 3: runbooks, alerts with owners, rollback path tested.
Monitoring watches. Gate 4: triggers fire, the loop closes.
Iteration improves. It feeds back to discovery when the world
changes.

:::takeaway
No phase does another phase's work. The gate is the exam's
answer when the stem skips a phase.
:::

<figure class="fig">
<svg viewBox="0 0 720 440" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="440" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five phases, four gates</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each gate names the artifact that lets the phase close.</text>
<rect x="24" y="96" width="672" height="72" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<rect x="40" y="112" width="112" height="40" rx="999" fill="#E7F4EF"/>
<text x="96" y="137" font-size="12" text-anchor="middle" fill="#1B2838">discovery</text>
<rect x="168" y="112" width="112" height="40" rx="999" fill="#E7F1F8"/>
<text x="224" y="137" font-size="12" text-anchor="middle" fill="#1B2838">design</text>
<rect x="296" y="112" width="112" height="40" rx="999" fill="#F4E6D4"/>
<text x="352" y="137" font-size="12" text-anchor="middle" fill="#1B2838">handoff</text>
<rect x="424" y="112" width="112" height="40" rx="999" fill="#F6E7A8"/>
<text x="480" y="137" font-size="12" text-anchor="middle" fill="#1B2838">monitoring</text>
<rect x="552" y="112" width="112" height="40" rx="999" fill="#D9E8D3"/>
<text x="608" y="137" font-size="12" text-anchor="middle" fill="#1B2838">iteration</text>
<rect x="24" y="192" width="672" height="160" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="224" font-size="13" font-weight="500" fill="#5C6B7A">GATES</text>
<text x="44" y="248" font-size="13" fill="#1B2838">G1: metric + threshold + owner per requirement</text>
<text x="44" y="272" font-size="13" fill="#1B2838">G2: priced options, ADRs written</text>
<text x="44" y="296" font-size="13" fill="#1B2838">G3: runbooks, alert owners, rollback tested</text>
<text x="44" y="320" font-size="13" fill="#1B2838">G4: triggers fire, loop closes, iteration feeds discovery</text>
<defs><marker id="m-d65-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="664" y1="132" x2="664" y2="172" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d65-3)"/>
<text x="664" y="192" font-size="12" text-anchor="middle" fill="#1B2838">feeds back</text>
<text x="24" y="396" font-size="15" fill="#1B2838">A gate holds the phase until the artifact exists.</text>
</svg>
<figcaption>Shell 4. Unordered work becomes gated phases. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Skipped gates compound. Discovery skipped: design guesses.
Design guessed: the handoff transfers a fragile system.
Handoff weak: monitoring alerts with no owner. Monitoring
noisy: iteration tunes the wrong layer. Each skipped gate
moves the cost downstream, where a fix costs ten times more.

The return rule: when a later phase fails, go back to the
phase whose gate was skipped. Production errors with no
named requirements mean discovery never closed. Fixing the
monitoring config is a proxy fix. The exam asks for the
first action, and the answer is the skipped phase, not more
tooling on the current one.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Debt moves downstream</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One skipped gate. Cost multiplies at every phase.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">G1 skipped: $82.50</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">design guesses: $825</text>
<rect x="44" y="232" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">rebuild: $8,250</text>
<text x="44" y="284" font-size="13" fill="#5C6B7A">Each phase multiplies by ten.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="167" font-size="13" text-anchor="middle" fill="#1B2838">G1 passed: $82.50</text>
<rect x="420" y="188" width="256" height="36" rx="8" fill="#E7F1F8"/>
<text x="548" y="211" font-size="13" text-anchor="middle" fill="#1B2838">design priced: included</text>
<rect x="420" y="232" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="255" font-size="13" text-anchor="middle" fill="#1B2838">no rebuild: $0</text>
<text x="420" y="284" font-size="13" fill="#5C6B7A">The gate stops the multiply.</text>
<defs><marker id="m-d65-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d65-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">hold the gate</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The cheapest phase is the one that holds its gate.</text>
</svg>
<figcaption>Shell 4. A skipped gate becomes a held gate, priced per phase. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: triage agent again. Timeline A skips gates. Discovery
skipped, cost avoided: $82.50. Design guesses the threshold.
Handoff has no runbook. Production errors triple. The team
adds dashboards for two weeks: 2 engineers x 80 hours x $150 =
$24,000. Then they rebuild the threshold logic: 4 weeks =
$48,000. Total: $72,000 to fix what $82.50 of discovery
would have caught.

Timeline B holds the gates. Discovery costs $82.50. Design
prices two options. Handoff ships runbooks. Monitoring fires
one trigger in month two, tuned in a day. Same system, two
histories. The difference is four held gates.

Mini question: "An agent is live. Error rate tripled. There
was no discovery: requirements were never written with
thresholds. The team proposes more dashboards and a bigger
model. What is the correct first action? A) Add dashboards
and upgrade the model. B) Return to discovery: write the
requirements with metrics, thresholds, and owners, then
re-design. C) Add a human reviewer on every task."

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
| STEP 1 | First action on a live failure with skipped discovery |
| STEP 2 | Operation failure, but the skipped phase is discovery |
| STEP 3 | Name the true requirements, then fix the right layer |
| STEP 4 | No thresholds exist. Dashboards cannot invent them |
| STEP 5 | Lifecycle layer: the return rule |
| STEP 6 | All three are feasible |
| STEP 7 | A substitutes later-phase work for missing discovery. C adds review everywhere, a proxy fix |
| STEP 8 | B returns to the skipped phase per the return rule |
| STEP 9 | B needs stakeholder time to write the requirements |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the skipped gate. More
dashboards measure the wrong design well. The correct first
action is the phase that was skipped.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Phase gates | Lifecycle plan | V2-D6.5 no substitution |
| Runbooks | Handoff artifacts | V2-D6.5, V2-D7.3 operations |
| Rollback path | Deployment practice | V2-D6.5 gate 3 |
| Iteration loop | Feedback contract | V2-D6.5, V2-D6.3 feedback to discovery |

## 7. Current limitations

Gates can become bureaucracy: a two-person team does not
need four formal reviews. Emergencies skip phases on
purpose: an outage fix goes straight to production. The
return rule costs time: going back to discovery mid-crisis
feels slow. And phases overlap in practice: design starts
while discovery closes, and that is fine if the gate holds.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The outage shortcut</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Production is down. The gate waits. Then the record is written.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">gate blocks the hotfix</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Downtime grows. Bureaucracy wins.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">hotfix now, ADR after</text>
<rect x="420" y="208" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="233" font-size="14" text-anchor="middle" fill="#1B2838">post-incident record</text>
<text x="420" y="260" font-size="13" fill="#5C6B7A">Emergency path, then the gate catches up.</text>
<defs><marker id="m-d65-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d65-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">allow the shortcut</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Gates serve the system. The outage gets the shortcut, then the record.</text>
</svg>
<figcaption>Shell 3. A blocking gate becomes an emergency path with a record. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Skip phases, ship fast | No gates | Prototype, hackathon, reversible demo |
| Gated lifecycle (this lesson) | Five phases, four gates, return rule | Production, handoffs, real money |
| Agile sprints without gates | Iterations, no artifacts | Product team with embedded users |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Stem skips discovery or design | First action is the skipped phase |
| Later-phase fix proposed for an early-phase gap | Distractor. Proxy fix |
| Live outage | Hotfix now, record after |
| Reversible demo | Skip the gates |

## 10. Valid-but-inferior option

Add a human reviewer on every task. Valid: review catches
errors. Inferior here: review on everything costs a fortune
and never names the requirements. It treats the symptom of
skipped discovery, not the cause.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Review everywhere | Catches errors | Symptom treatment, no requirements |

## 11. Counterfactual where the alternative wins

Production outage, customers down. The hotfix cannot wait for
discovery. Skipping phases wins: fix now, write the ADR in
the post-incident review. The gate catches up after.

| Situation | Winner | Why |
|---|---|---|
| Live outage | Skip to the fix | Downtime beats process |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Five phases: discovery, ______, handoff,
   ______, iteration.
2. G1 artifact: metric + ______ + ______.
3. Return rule: go back to the ______ phase.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A team ships a RAG agent with no discovery
and no ADRs. Six months later the retriever
vendor doubles prices. The team must decide
rebuild vs renegotiate in one week.
Name the skipped phases and the first
three artifacts they must write now.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D6.5 tests five phases, gates, no substitution of later-phase work | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D6.5 | Sept 2026 |
| Toy arithmetic: $72,000 fix vs $82.50 discovery, ten times per phase | Original toy, computed above | This lesson | Oct 6, 2026 |

:::takeaway
Hold the gates in order. When a later phase fails, return to
the phase whose gate was skipped. The exam's first-action
questions are won by the return rule.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Dashboards cannot fix a skipped design | 5 dashboards, errors triple | Return to discovery | d65-f01 | SVG | Original |
| u02 | Phases own their lessons | -- | Prerequisite table | d65-f02 | Table | V2-D6.1 to V2-D6.4 |
| u03 | Five phases, four gates | Unordered work | Gated phase chain | d65-f03 | SVG | Original |
| u04 | Debt moves downstream | $82.50 to $72,000 | Gate stops the multiply | d65-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B is the skipped phase | d65-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d65-f06 | Table | S03, S04 |
| u07 | The outage shortcut | Gate blocks hotfix | Emergency path, record after | d65-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d65-f08 | Table | Original |
| u09 | Constraints decide the phase | -- | Constraint verdict table | d65-f09 | Table | Original |
| u10 | Review-everywhere valid but inferior | -- | Validity vs inferiority table | d65-f10 | Table | Original |
| u11 | Outage favors the shortcut | -- | Counterfactual table | d65-f11 | Table | Original |
| u12 | Five phases from memory | Blank recall card | Filled from memory | d65-f12 | ASCII | Original |
| u13 | Transfer to RAG repricing | Unseen question | Key in Stage 8 | d65-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d65-f14 | Table | Mixed |
