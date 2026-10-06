# Lesson D4-6: production monitoring (V2-D4.6)

## 1. Problem this lesson solves

A refund agent runs fine for three months. Then task success slides
from 92% to 84%. Nobody notices for six weeks. The eval set still
scores 91%, because the eval set is last quarter's traffic. By the
time a human spots the slide, 40,000 bad refunds are out.

The system had logs. It had no monitoring. Logs record. Monitoring
watches, compares, and pages a named owner when the line breaks.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Logs recorded, nobody watched</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Six weeks of drift. The eval set smiled the whole time.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">logs: everything</text>
<rect x="44" y="200" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">alerts: none</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">Drift: 6 weeks, unseen.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">alert line: 88%</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">owner: on-call lead</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Drift: caught at day 2.</text>
<defs><marker id="m-d46-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d46-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">watch the line</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Monitoring is a watched line with a named owner, not a pile of logs.</text>
</svg>
<figcaption>Shell 3. Unwatched logs become a watched alert line. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D3-4 gives the traces that feed monitoring: per-hop inputs,
decisions, outputs, cost. Lesson 7-1A gives the reliability numbers.
Lesson 7-4A gives the owner rule: every line has a signer.

| Foundation | What it gives this lesson |
|---|---|
| §7.1 systems | Retry, timeout, breaker signals |
| V2-D3.4 observability | Traces with one id, per-hop cost |

## 3. Mental model

Five watches, always on. Operational metrics: task success, latency
p95, error rate, cost per task, tool failure rate. Instrumentation:
the traces from Lesson D3-4, aggregated into dashboards per stage.
Drift detection: the live numbers compared against the baseline on
a schedule. Regression suites: the eval set from Lesson D4-2, run
on a cadence against production samples. Alerts: a line, a window,
and a named owner who acts.

The eval data must mirror production. An eval set frozen last
quarter cannot catch this quarter's drift. Refresh the production
sample on a cadence. Compare like with like.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five watches, always on</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Metrics, traces, drift, regression, alerts. Each watch owns one job.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E6E2DA"/>
<text x="172" y="177" font-size="13" text-anchor="middle" fill="#1B2838">dashboard: traffic only</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No baseline.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No owner.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Drift: invisible.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="32" rx="999" fill="#E7F1F8"/>
<text x="460" y="169" font-size="11" text-anchor="middle" fill="#1B2838">metrics</text>
<rect x="508" y="148" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="11" text-anchor="middle" fill="#1B2838">drift</text>
<rect x="596" y="148" width="80" height="32" rx="999" fill="#F6E7A8"/>
<text x="636" y="169" font-size="11" text-anchor="middle" fill="#1B2838">alerts</text>
<rect x="464" y="188" width="80" height="32" rx="999" fill="#F4E6D4"/>
<text x="504" y="209" font-size="11" text-anchor="middle" fill="#1B2838">regress</text>
<rect x="552" y="188" width="80" height="32" rx="999" fill="#E6E2DA"/>
<text x="592" y="209" font-size="11" text-anchor="middle" fill="#1B2838">owner</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Baseline: 92%. Line: 88%.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Eval mirrors production.</text>
<defs><marker id="m-d46-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d46-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">set the watches</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Five watches turn drift from a surprise into a page.</text>
</svg>
<figcaption>Shell 3. One traffic dashboard becomes five named watches. Source: original toy.</figcaption>
</figure>

:::takeaway
Watch the line, not the pile. Baseline, alert line, window, and
named owner on every metric that matters.
:::

## 4. Causal mechanism

Drift has four parents. Input drift: the ticket mix changes, new
intents arrive. Model drift: the provider updates the model,
behavior shifts. Data drift: the source documents change, retrieval
returns different chunks. Prompt drift: someone edits the template
without a version note. The monitor cannot name the parent. It can
only page the owner. Diagnosis from Lesson D4-4 names the parent.

The alert rule has three parts. The line: task success below 88%.
The window: the 7-day mean, so one bad hour does not page anyone.
The owner: the on-call lead, named in the runbook, with a
diagnosis checklist. An alert without an owner is a notification.
A notification is a hope.

Representative eval data is the fifth watch's fuel. Sample
production weekly. Label a slice. Run the regression suite nightly.
Compare the suite score against the live score. When they diverge,
the set is stale, not the system.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The alert rule has three parts</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Line, window, owner. Miss one and the page never fires.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">alert: "success low"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No line.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No window.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No owner.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">line: below 88%</text>
<rect x="420" y="192" width="256" height="36" rx="8" fill="#E7F1F8"/>
<text x="548" y="215" font-size="12" text-anchor="middle" fill="#1B2838">window: 7-day mean</text>
<rect x="420" y="236" width="256" height="36" rx="8" fill="#F6E7A8"/>
<text x="548" y="259" font-size="12" text-anchor="middle" fill="#1B2838">owner: on-call lead</text>
<defs><marker id="m-d46-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d46-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">name all three</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A complete alert rule pages a person, not a channel.</text>
</svg>
<figcaption>Shell 3. A vague alert becomes a line, a window, and an owner. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: refund agent. Baseline task success 92%. Alert line 88% on
the 7-day mean. Owner: on-call lead. Regression suite: 500 cases,
nightly, from Lesson D4-2's set.

Week 12: new refund policy ships. Tickets about the new policy
fail. Live success slides to 85%. The 7-day mean crosses 88% on
day 2 of the slide. The owner gets paged. Diagnosis from Lesson
D4-4: data drift, the retrieval index lacks the new policy.
Fix: re-index. Live success returns to 91%.

Cost of the miss without monitoring: 10,000 tickets per day x
42 days x (92% - 84%) extra failures. Extra failures per day:
10,000 x 0.08 = 800. Over 42 days: 800 x 42 = 33,600 bad
outcomes. Each costs $2 in rework: 33,600 x $2 = $67,200.

Cost of the alert path: one false page per quarter. Each false
page costs 2 engineer hours at $150: $300. The monitor pays for
itself 224 times over on one catch: $67,200 / $300 = 224.

Mini question: "Live task success slides for two days. The
regression suite still scores 91%. Which action fits? A) Trust
the suite and wait. B) Page the owner and diagnose for drift,
since the suite mirrors last quarter. C) Roll back the model
tier."

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
| STEP 1 | First action on live drift with a clean suite |
| STEP 2 | Operation: the system is live and sliding |
| STEP 3 | Catch the drift and name its parent |
| STEP 4 | Live slides. Suite is stale. Alert line crossed |
| STEP 5 | Monitoring and eval-data layer |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the drift evidence: the suite is stale. C is a proxy fix before diagnosis |
| STEP 8 | B pages the owner and refreshes the eval mirror |
| STEP 9 | B needs the alert rule and the production sample pipeline owned |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the stale suite: live data moved,
the set did not. Only B acts on the live signal and fixes the
mirror.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The monitor prices itself</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One catch saves $67,200. One false page costs $300.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">miss: $67,200</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">800 x 42 = 33,600 bad.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">33,600 x $2 = $67,200.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Caught at week 6.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">catch: $300</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Paged at day 2.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">False page: $300.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">$67,200 / $300 = 224x.</text>
<defs><marker id="m-d46-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d46-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">price the watch</text>
<text x="24" y="352" font-size="15" fill="#1B2838">One honest catch pays for decades of false pages.</text>
</svg>
<figcaption>Shell 4. A six-week miss becomes a day-2 catch with arithmetic. Source: original toy.</figcaption>
</figure>

:::takeaway
The eval set is a mirror. Polish the mirror on a cadence, or it
shows last quarter while this quarter breaks.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Trace aggregation | Metrics backend, dashboards per stage | V2-D4.6 instrumentation |
| Alert rule with owner | Paging system, runbook | V2-D4.6 alerts with owners |
| Nightly regression run | CI or scheduled eval job | V2-D4.6 regression suites |
| Production sample pipeline | Sampling plus labeling job | V2-D4.6 representative eval data |

## 7. Current limitations

Alert fatigue kills the watch: too many lines, the owner mutes
them all. The window hides fast breaks: a 7-day mean misses a
2-hour outage, so pair slow drift lines with fast break lines.
The monitor watches the system, not the world: a policy change
upstream breaks the task without touching any metric until users
complain. Sampling lies at small volumes: the weekly sample is
too thin to see a rare segment.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Two lines, two speeds</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The slow line misses the fast break. Pair them.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">one line: 7-day mean</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">2-hour outage: unseen.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Mean barely moves.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">slow: 7-day mean</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">fast: 1-hour error rate</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Drift and outage both page.</text>
<defs><marker id="m-d46-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d46-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">pair the lines</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Slow lines catch drift. Fast lines catch outages. Run both.</text>
</svg>
<figcaption>Shell 3. One slow line becomes a paired slow and fast line. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Logs only | Records, no watches | Tiny tool, one user |
| Manual weekly review | Human reads dashboards | Low volume, expert owner |
| Five watches (this lesson) | Lines, windows, owners | Production agent fleet |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Live slides, suite is green | The suite is stale. Page and refresh |
| Fast outage vs slow drift | Pair a fast line with a slow line |
| No named owner | No monitoring exists yet. Name one first |
| Alert fires weekly with no action | The line is wrong. Retune or retire it |

## 10. Valid-but-inferior option

Manual weekly dashboard review. Valid: a careful owner catches
most drift, and it needs no paging machinery. Inferior at scale:
the toy's slide ran 42 days before a human looked. Reviewers miss
weeks, owners change, and the review is the first chore dropped
under pressure.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Weekly manual review | Catches drift, cheap | 42-day lag. Dropped under pressure |

## 11. Counterfactual where the alternative wins

Internal tool, five users, the author sits next to them. Logs plus
a glance at the dashboard win: drift is a hallway conversation,
and paging machinery is theater.

| Situation | Winner | Why |
|---|---|---|
| Five users, one hallway | Logs plus a glance | Drift is a conversation |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The five watches: metrics, instrumentation,
   ______, regression, alerts.
2. An alert rule needs a ______, a ______, and an ______.
3. The toy catch saves $______ vs a $______ false page.
4. Pair the slow line with a ______ line.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A triage agent's live success holds at 90% but the
nightly regression suite drops to 82%. The suite has
not been refreshed in four months.
Name the diagnosis and the two fixes.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D4.6 tests operational metrics, instrumentation, drift detection, regression suites, alerts with owners, representative eval data | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D4.6 | Sept 2026 |
| Toy miss and catch arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Engineer hour rate $150 | Toy assumption, stated | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D4.6 trap offers more logs or longer retention. The
scenario asks for drift. The answer is a watched line with an
owner.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Logs recorded, nobody watched | Logs, no alerts | Watched line, owner | d46-f01 | SVG | Original |
| u02 | Traces and owners carry over | -- | Prerequisite table | d46-f02 | Table | §7.1, V2-D3.4 |
| u03 | Five watches, always on | Traffic dashboard | Five named watches | d46-f03 | SVG | Original |
| u04 | Alert rule has three parts | Vague alert | Line, window, owner | d46-f04 | SVG | Original |
| u05 | Monitor prices itself | $67,200 miss | $300 catch, 224x | d46-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B pages and refreshes | d46-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d46-f06 | Table | S03, S04 |
| u07 | Two lines, two speeds | One slow line | Paired slow and fast | d46-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d46-f08 | Table | Original |
| u09 | Constraints decide the watch | -- | Constraint verdict table | d46-f09 | Table | Original |
| u10 | Manual review valid but inferior | -- | Validity vs inferiority table | d46-f10 | Table | Original |
| u11 | Hallway favors logs plus glance | -- | Counterfactual table | d46-f11 | Table | Original |
| u12 | Watch facts from memory | Blank recall card | Filled from memory | d46-f12 | ASCII | Original |
| u13 | Transfer to triage agent | Unseen question | Key in Stage 8 | d46-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d46-f14 | Table | Mixed |
