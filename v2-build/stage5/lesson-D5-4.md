# Lesson D5-4: regulatory compliance (V2-D5.4)

This lesson describes architectural implications only. It is not
legal advice. Regulations are interpreted by lawyers, not by this
page. The exam tests how a requirement changes the architecture:
handling, access, logging, retention, deployment route, residency,
and evidence.

## 1. Problem this lesson solves

A health triage agent stores chat transcripts with symptoms. The
team keeps them forever for training. An audit asks: where does
EU data live, who can read it, how long is it kept, and where is
the proof. The team has no answers. The architecture never heard
the regulation.

Compliance is not a document written after the build. It is a set
of requirements that shapes the build: where data may live, who
may touch it, how long it stays, and what evidence proves it.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The architecture never heard it</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The audit asks four questions. The build answers none.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">one region, forever logs</text>
<rect x="44" y="208" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="233" font-size="13" text-anchor="middle" fill="#1B2838">access: everyone</text>
<text x="44" y="264" font-size="13" fill="#5C6B7A">Audit: four blanks.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="40" rx="8" fill="#E7F4EF"/>
<text x="480" y="173" font-size="12" text-anchor="middle" fill="#1B2838">EU region</text>
<rect x="556" y="148" width="120" height="40" rx="8" fill="#F6E7A8"/>
<text x="616" y="173" font-size="12" text-anchor="middle" fill="#1B2838">30-day logs</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">role-scoped access</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Audit: four answers.</text>
<defs><marker id="m-d54-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d54-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">build the answers</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The requirement enters the architecture. The audit reads the architecture.</text>
</svg>
<figcaption>Shell 3. An unaware architecture becomes an auditable architecture. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-2A gives access control and auditability. Lesson 7-4A
gives the owner rule. This lesson chains them into a compliance
row.

| Foundation | What it gives this lesson |
|---|---|
| §7.2 security | Access control, audit logs, retention basics |
| §7.4 business | Every control gets an owner and a review date |

## 3. Mental model

One chain per requirement. Requirement: the rule in plain words.
Control: what the architecture does about it. Owner: the person
who answers for it. Evidence: the artifact that proves it.
Cadence: how often the evidence is produced and reviewed.

Three regulation families shape the chain. GDPR: EU personal
data. Handling limits, access limits, deletion rights, residency
questions. HIPAA: US health data. Access controls, audit trails,
retention rules. FedRAMP: US federal systems. Deployment route
restrictions, control baselines, continuous monitoring evidence.
The names matter less than the shape: each family turns into
rows in the chain.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One chain per requirement</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Requirement, control, owner, evidence, cadence. Every row.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="13" text-anchor="middle" fill="#1B2838">"we comply"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No control named.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No evidence exists.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">No owner signed.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="32" rx="999" fill="#E7F1F8"/>
<text x="460" y="169" font-size="11" text-anchor="middle" fill="#1B2838">control</text>
<rect x="508" y="148" width="80" height="32" rx="999" fill="#F6E7A8"/>
<text x="548" y="169" font-size="11" text-anchor="middle" fill="#1B2838">owner</text>
<rect x="596" y="148" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="636" y="169" font-size="11" text-anchor="middle" fill="#1B2838">evidence</text>
<rect x="464" y="188" width="128" height="32" rx="999" fill="#F4E6D4"/>
<text x="528" y="209" font-size="11" text-anchor="middle" fill="#1B2838">cadence: monthly</text>
<text x="420" y="244" font-size="13" fill="#5C6B7A">Each row is auditable.</text>
<defs><marker id="m-d54-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d54-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">write the rows</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A claim without a row is a wish. A row without evidence is a rumor.</text>
</svg>
<figcaption>Shell 3. A bare claim becomes a five-link compliance row. Source: original toy.</figcaption>
</figure>

:::takeaway
Every compliance requirement becomes a row: requirement, control,
owner, evidence, cadence. The exam tests the architecture, not
the law.
:::

## 4. Causal mechanism

The architecture bends in six places. Data handling: minimize
what is collected, mask what the model does not need, strip PII
from traces. Access: role-scoped reads, per-user identity, no
shared credentials. Logging: record who, what, and the decision,
and protect the logs themselves. Retention: keep data only as
long as the requirement allows, then delete on schedule.
Deployment route: regulated data may force a specific cloud,
region, or on-premise route. Residency: EU data stays in the EU
region. Evidence: the audit trail, the access review, the
deletion log.

Retention is the quiet killer. "Keep everything for training" is
a compliance position. The compliant position is a number: logs
kept 30 days, transcripts kept 90 days, then deleted. The deletion
itself is logged. The log of the deletion is the evidence.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Retention is a number</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">"Forever" is a position. "30 days" is a control.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">kept: forever</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No deletion job.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No evidence.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Breach surface grows daily.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">logs: 30 days</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">transcripts: 90 days</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Deletion logged monthly.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Surface stops growing.</text>
<defs><marker id="m-d54-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d54-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">number the days</text>
<text x="24" y="352" font-size="15" fill="#1B2838">A retention number plus a deletion log is the evidence.</text>
</svg>
<figcaption>Shell 3. Forever retention becomes numbered retention with deletion logs. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: health triage agent. EU users, symptom transcripts, 100,000
chats per month. The compliance row for one requirement.

Requirement: EU personal data stays in the EU and is deleted on
schedule. Control: deploy the EU traffic to the EU region. Mask
symptom details in traces. Delete transcripts after 90 days,
logs after 30 days. Owner: data protection lead. Evidence: the
region config, the monthly deletion log, the quarterly access
review. Cadence: deletion monthly, access review quarterly.

Storage math (toy assumptions, stated): 100,000 chats per month,
2 KB per transcript. One month: 100,000 x 2 KB = 200 MB. 90-day
retention: 600 MB live. Forever retention after 3 years:
200 MB x 36 = 7,200 MB = 7.2 GB of stale health data. Deletion
on schedule removes 6.6 GB of breach surface: 7.2 - 0.6 = 6.6 GB.

Second row. Requirement: only care-team roles read transcripts.
Control: role-scoped access on the transcript store, per-user
identity, audit log on every read. Owner: security lead.
Evidence: the quarterly access review plus the read audit log.
Cadence: quarterly.

Mini question: "A health agent stores EU symptom transcripts in
one US region, kept forever, readable by all engineers. Which
change addresses the root cause? A) Encrypt the transcripts. B)
Deploy EU traffic to an EU region, scope access by role, set
retention with deletion logs, and name an owner. C) Add a privacy
notice to the app."

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
| STEP 1 | Architecture for a regulated data flow |
| STEP 2 | Design: the data plane ignores the regulation |
| STEP 3 | Make the architecture answer the audit |
| STEP 4 | EU health data. US region. Forever retention. Open access |
| STEP 5 | Data plane: residency, access, retention |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the root cause: encryption does not fix region or access. C is a notice, not a control |
| STEP 8 | B builds the full row: region, access, retention, owner |
| STEP 9 | B needs the EU deployment route and the deletion job owned |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive requirement is the full compliance row,
and only B builds it. The scenario names region, access, and
retention, and the answer is architecture, not a notice.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Deletion shrinks the surface</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">7.2 GB forever. 0.6 GB on schedule. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">7.2 GB forever</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">200 MB x 36 = 7,200 MB.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">3 years of stale data.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Breach surface grows.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">0.6 GB live</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">90 days: 600 MB.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Deletion logged monthly.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">7.2 - 0.6 = 6.6 GB gone.</text>
<defs><marker id="m-d54-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d54-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">delete on schedule</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Scheduled deletion is a control. The deletion log is the evidence.</text>
</svg>
<figcaption>Shell 4. Forever retention becomes scheduled deletion with arithmetic. Source: original toy.</figcaption>
</figure>

:::takeaway
Residency, access, retention, evidence: the audit asks these
four. The architecture must answer all four before the audit.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Regional deployment | Cloud region config | V2-D5.4 residency, deployment route |
| Role-scoped data access | Store ACLs, Lesson 7-2A | V2-D5.4 access |
| Deletion job plus log | Scheduled job, audit store | V2-D5.4 retention, evidence |
| Quarterly access review | Security process | V2-D5.4 cadence |

## 7. Current limitations

Regulations change: the row written this year may miss next
year's rule. Lawyers, not engineers, interpret the requirement:
the chain carries the interpretation, not the law. Multi-region
adds cost and complexity: two regions mean two of everything.
Deletion conflicts with debugging: the engineer wants the old
trace, the rule wants it gone. The rule wins.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Two regions, two of everything</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Residency has a price. Pay it with eyes open.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">one region, one bill</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Simple.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Non-compliant.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">two regions, two bills</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Compliant.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Priced and owned.</text>
<defs><marker id="m-d54-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d54-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">pay for residency</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Compliance is a cost line. Budget it like one.</text>
</svg>
<figcaption>Shell 3. One region becomes two priced regions. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Notice-only compliance | Words in the app | No regulated data |
| Legal review of every row | Lawyer per decision | Extreme regulatory exposure |
| Architecture rows (this lesson) | Requirement to evidence | Regulated production systems |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| EU personal data | Residency row: region, access, retention, evidence |
| Health data | Access row plus audit trail on every read |
| Federal deployment | Deployment route row, control baseline evidence |
| No regulated data | Skip the machinery. Notice suffices |

## 10. Valid-but-inferior option

Encryption alone. Valid: encryption protects data at rest and in
transit, and it is required anyway. Inferior for the audit: it
fixes neither the region, nor the access list, nor the retention
schedule. On the toy, encrypted transcripts still sat in the US
forever, readable by all.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Encryption alone | Protects data in place | Region, access, retention unanswered |

## 11. Counterfactual where the alternative wins

Public documentation bot. No personal data, no health data, no
federal customer. Notice-only compliance wins: there is no
regulated data to govern, and rows would protect nothing.

| Situation | Winner | Why |
|---|---|---|
| No regulated data | Notice-only | No data to govern |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The five links: requirement, control, ______,
   evidence, ______.
2. The audit asks: residency, ______, retention, ______.
3. Forever retention: 7.2 GB. Scheduled: ______ GB.
4. This lesson is ______ implications, not legal advice.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A finance agent stores EU transaction records. The
deployment is one US region. Retention is unset. Access
is by shared service account.
Name the four architecture changes and the evidence
for each.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D5.4 tests GDPR, HIPAA, FedRAMP effects on handling, access, logging, retention, deployment route, residency, evidence, and the requirement to control to owner to evidence to cadence chain | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D5.4 | Sept 2026 |
| Toy storage arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Regulation interpretations | Not legal advice. Architectural implications only | This lesson | Oct 6, 2026 |

:::takeaway
The exam's D5.4 trap offers a notice or encryption. The scenario
asks for architecture. Build the row: control, owner, evidence,
cadence.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Architecture never heard it | One region, forever | EU region, numbered retention | d54-f01 | SVG | Original |
| u02 | Access and owners carry over | -- | Prerequisite table | d54-f02 | Table | §7.2, §7.4 |
| u03 | One chain per requirement | Bare claim | Five-link row | d54-f03 | SVG | Original |
| u04 | Retention is a number | Forever | 30 and 90 days, deletion logged | d54-f04 | SVG | Original |
| u05 | Deletion shrinks the surface | 7.2 GB forever | 0.6 GB live, 6.6 GB gone | d54-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B builds the row | d54-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d54-f06 | Table | S03, S04 |
| u07 | Two regions, two bills | One region | Two priced regions | d54-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d54-f08 | Table | Original |
| u09 | Constraints decide the row | -- | Constraint verdict table | d54-f09 | Table | Original |
| u10 | Encryption alone valid but inferior | -- | Validity vs inferiority table | d54-f10 | Table | Original |
| u11 | Public bot favors notice-only | -- | Counterfactual table | d54-f11 | Table | Original |
| u12 | Chain facts from memory | Blank recall card | Filled from memory | d54-f12 | ASCII | Original |
| u13 | Transfer to finance agent | Unseen question | Key in Stage 8 | d54-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d54-f14 | Table | Mixed |
