# Lesson D7-3: debugging and operational resolution (V2-D7.3)

## 1. Problem this lesson solves

The triage agent's p95 latency jumps from 3 seconds to 14.
The team upgrades the model. Latency stays at 14. They add
more logging. Latency stays at 14. Three weeks pass. The real
cause: a context window that grew to 90,000 tokens per call
after a prompt change. Nobody looked at the context size,
because nobody had a map from symptom to investigation.

Every symptom points at a short list of suspects. Quality
decline: prompt drift, model drift, retrieval drift. Latency
rise: context growth, dependency slowdown, cache misses.
Tool failures: credentials, permissions, throttling,
contracts. Cost rise: routing, context, caching. Lost agent
work: orchestration state, traces. The map turns a hunt into
a checklist.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The symptom has a short suspect list</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">p95 at 14 seconds. Three weeks of wrong fixes.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">bigger model: still 14 s</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">more logging: still 14 s</text>
<rect x="44" y="232" width="256" height="36" rx="8" fill="#F3D4D8"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">cause: 90k context</text>
<text x="44" y="288" font-size="13" fill="#5C6B7A">Nobody checked the suspect list.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="36" rx="8" fill="#E7F4EF"/>
<text x="548" y="167" font-size="13" text-anchor="middle" fill="#1B2838">latency map: check context</text>
<rect x="420" y="188" width="256" height="36" rx="8" fill="#E7F1F8"/>
<text x="548" y="211" font-size="13" text-anchor="middle" fill="#1B2838">found in 1 hour</text>
<rect x="420" y="232" width="256" height="36" rx="8" fill="#D9E8D3"/>
<text x="548" y="255" font-size="13" text-anchor="middle" fill="#1B2838">fix: trim to 12k</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Checklist beats a hunt.</text>
<defs><marker id="m-d73-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d73-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">use the map</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Three weeks of hunts vs one hour with the map.</text>
</svg>
<figcaption>Shell 3. A model upgrade becomes a context check. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D4-4 owns fix-at-the-right-layer diagnosis. Lesson
D3-4 owns the traces the map reads. Lesson D6-5 owns the
handoff runbooks this lesson extends.

| Foundation | What it gives this lesson |
|---|---|
| V2-D4.4 diagnosis | Layer-first fault isolation |
| V2-D3.4 observability | Traces, costs, and error ids |
| V2-D6.5 handoff | Runbooks and alert owners |

## 3. Mental model

The map pairs each symptom with its suspects, in check
order.

Quality decline: check prompt drift first (did the prompt
change), then model drift (did the version change), then
retrieval drift (did the corpus change). Latency rise:
check context growth, then dependency slowdown, then cache
misses. Tool failures: check credentials, then permissions,
then throttling, then the tool contract. Cost rise: check
routing (is the cheap model still used), then context size,
then caching. Lost agent work: check orchestration state,
then traces.

:::takeaway
Symptom first, suspects in order. The map is a runbook, not
a guess. The exam asks which suspect to check first.
:::

<figure class="fig">
<svg viewBox="0 0 720 460" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="460" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The symptom-to-suspect map</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Five symptoms. Ordered suspects. The order is the runbook.</text>
<rect x="24" y="96" width="672" height="280" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<rect x="44" y="116" width="200" height="36" rx="8" fill="#F3D4D8"/>
<text x="144" y="139" font-size="12" text-anchor="middle" fill="#1B2838">quality decline</text>
<text x="264" y="139" font-size="12" fill="#5C6B7A">prompt then model then retrieval</text>
<rect x="44" y="160" width="200" height="36" rx="8" fill="#F6E7A8"/>
<text x="144" y="183" font-size="12" text-anchor="middle" fill="#1B2838">latency rise</text>
<text x="264" y="183" font-size="12" fill="#5C6B7A">context then deps then cache</text>
<rect x="44" y="204" width="200" height="36" rx="8" fill="#E7F1F8"/>
<text x="144" y="227" font-size="12" text-anchor="middle" fill="#1B2838">tool failures</text>
<text x="264" y="227" font-size="12" fill="#5C6B7A">creds then perms then throttle then contract</text>
<rect x="44" y="248" width="200" height="36" rx="8" fill="#F4E6D4"/>
<text x="144" y="271" font-size="12" text-anchor="middle" fill="#1B2838">cost rise</text>
<text x="264" y="271" font-size="12" fill="#5C6B7A">routing then context then caching</text>
<rect x="44" y="292" width="200" height="36" rx="8" fill="#E6E2DA"/>
<text x="144" y="315" font-size="12" text-anchor="middle" fill="#1B2838">lost agent work</text>
<text x="264" y="315" font-size="12" fill="#5C6B7A">orchestration state then traces</text>
<text x="44" y="348" font-size="13" fill="#5C6B7A">Check in order. Stop at the first suspect that matches.</text>
<text x="24" y="416" font-size="15" fill="#1B2838">The order is the runbook. A guess is not.</text>
</svg>
<figcaption>Shell 2. Five symptoms become five ordered suspect lists. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

A hunt without a map tries fixes by fashion. The team
upgrades the model because upgrades are fashionable. The
model is innocent. Each wrong fix costs engineering weeks
and teaches nothing. The incident repeats, because the
runbook was never written.

A runbook with the map, an owner, and an escalation path
ends the cycle. The on-call engineer opens the latency
runbook: check context size, then dependency latency, then
cache hit rate. The first check matches. The fix is a
prompt trim. The incident review updates the runbook. The
next incident with the same symptom resolves without the
original architect. The team, not the hero, owns the
system.

Escalation arithmetic: without the runbook, the incident
takes 3 weeks of senior time: 2 engineers x 60 hours x
$200 = $24,000, and it repeats twice a year = $48,000.
With the runbook, one on-call engineer resolves it in
4 hours: $800, and the recurrence drops to zero after the
fix ships. The numbers are a toy. The mechanism is real.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The hero tax</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Two incidents a year. One needs the architect. One does not.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">no runbook: 3 weeks</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">2 x 60 h x $200 = $24,000</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Twice a year: $48,000. Repeats.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">runbook: 4 hours</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">4 h x $200 = $800</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Fix ships. No repeat.</text>
<defs><marker id="m-d73-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d73-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">write the runbook</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A runbook is the architect's knowledge, available at 3 a.m.</text>
</svg>
<figcaption>Shell 4. A hero-dependent incident becomes a runbook incident. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: triage agent, p95 latency 3 s to 14 s in one week.
Runbook path: check 1, context size. The trace shows
average context grew from 12,000 to 90,000 tokens after a
prompt change added full ticket histories. Check 1 matches.
Stop. Fix: trim to the last 5 tickets, 12,000 tokens.
Latency returns to 3 s. The runbook gains a line: "alert
when average context passes 30,000 tokens."

The wrong path: upgrade the model (cost up, latency same),
add logging (noise up, latency same), add a human reviewer
on every task (throughput down, latency same). Three proxy
fixes. Zero root causes.

Mini question: "An agent's tool calls start failing at 10%
per day. Nothing in the code changed. Which is the correct
first check? A) Rewrite the tool with a larger model. B)
Check credentials and token expiry, then permissions, then
throttling, then the tool contract. C) Add more retries
with no backoff."

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
| STEP 1 | First check on failing tool calls |
| STEP 2 | Incident response: live failures, no code change |
| STEP 3 | Find the root cause in check order |
| STEP 4 | Nothing changed in code. The cause is external |
| STEP 5 | Tool integration layer |
| STEP 6 | All three are feasible |
| STEP 7 | A violates the map: nothing points at the model. C violates the retry law: retries without backoff amplify the failure |
| STEP 8 | B follows the map in order: creds, perms, throttle, contract |
| STEP 9 | B needs the credential rotation log and the throttle dashboard |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive fact is the unchanged code. An
external cause is on the suspect list first: credentials
expire, permissions change, throttles bite, contracts
drift. The map orders them.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Symptom map | Runbook | V2-D7.3 ordered investigation |
| Traces and ids | Lesson D3-4 | V2-D7.3 lost work investigation |
| Retry with backoff | Lesson 7-1A | V2-D7.3 safe recovery |
| Alert owners | Handoff runbook | V2-D7.3 ownership and escalation |
| Post-incident review | Team practice | V2-D7.3 runbook updates |

## 7. Current limitations

Maps go stale: a new dependency adds a suspect. Ordered
checks can be slow when two causes combine. Runbooks rot
like ADRs: a fix that changed the system but not the
runbook misleads the next on-call. And the map cannot
cover novel failures: the first incident of a new kind
still needs a human detective.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The runbook rots too</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The system changed. The runbook did not. The on-call follows it off a cliff.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">runbook: check context</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">new dep added, unlisted</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">On-call misses the real suspect.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">post-incident updates it</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">new suspect listed</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Every incident edits the map.</text>
<defs><marker id="m-d73-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d73-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">update after every incident</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The incident review is the runbook's maintenance contract.</text>
</svg>
<figcaption>Shell 3. A stale runbook becomes a maintained runbook. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Hunt by fashion | Upgrade, log, hope | Never, but teams do it |
| Page the architect | Hero-driven | First incident of a new kind |
| Map plus runbook (this lesson) | Ordered suspects, owner, escalation | Recurring operations, real on-call |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Symptom named in the stem | First suspect on the map's list |
| Nothing changed in code | External suspects first: creds, perms, versions |
| Latency rose | Check context before the model |
| Cost rose | Check routing before the model |
| Recurring incident | Runbook and owner must exist |

## 10. Valid-but-inferior option

Add more retries with no backoff. Valid: retries mask
flaky calls. Inferior here: retries without backoff
amplify a throttled dependency, and they never find the
cause. The map beats the mask.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Retries without backoff | Masks flakiness | Amplifies throttling, hides cause |

## 11. Counterfactual where the alternative wins

First incident of a brand-new failure mode. The map has
no entry. Paging the architect wins: a human detective
beats a checklist with no matching row.

| Situation | Winner | Why |
|---|---|---|
| Novel failure, no map entry | The architect | No checklist covers it yet |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Latency rise: ______ -> deps -> ______.
2. Tool failures: creds -> ______ -> ______
   -> contract.
3. Cost rise: ______ -> context -> ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A RAG agent's answer quality drops 8 points
in a week. No prompt changed. The corpus
team shipped a reindex. Name the ordered
checks from the map and the one the team
skipped last time.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D7.3 tests symptom-to-investigation mapping, runbooks, escalation, ownership, team resolution without the architect | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D7.3 | Sept 2026 |
| Toy arithmetic: $24,000 per incident without runbook, $800 with, no repeat | Original toy, computed above | This lesson | Oct 6, 2026 |
| Retry law: backoff on retries, from Lesson 7-1A | General principle | Lesson 7-1A | Oct 6, 2026 |

:::takeaway
Check the map before the model. Ordered suspects beat
fashionable fixes. The runbook lets the team resolve the
incident without the person who built the system.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Symptom has a short suspect list | Model upgrade, still 14 s | Context check in 1 hour | d73-f01 | SVG | Original |
| u02 | Layer diagnosis carries over | -- | Prerequisite table | d73-f02 | Table | V2-D4.4, V2-D3.4, V2-D6.5 |
| u03 | Symptom-to-suspect map | Hunt by guess | Five ordered lists | d73-f03 | SVG | Original |
| u04 | The hero tax | $24,000 per incident | $800 with runbook | d73-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B follows the map | d73-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d73-f06 | Table | S03, S04 |
| u07 | The runbook rots too | Stale runbook | Post-incident updates | d73-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d73-f08 | Table | Original |
| u09 | Constraints decide the check | -- | Constraint verdict table | d73-f09 | Table | Original |
| u10 | Retries valid but inferior | -- | Validity vs inferiority table | d73-f10 | Table | Original |
| u11 | Novel failure favors the architect | -- | Counterfactual table | d73-f11 | Table | Original |
| u12 | Suspect order from memory | Blank recall card | Filled from memory | d73-f12 | ASCII | Original |
| u13 | Transfer to RAG quality drop | Unseen question | Key in Stage 8 | d73-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d73-f14 | Table | Mixed |
