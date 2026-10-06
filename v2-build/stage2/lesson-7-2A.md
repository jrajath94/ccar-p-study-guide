# Lesson 7-2A: security and identity

## 1. Problem this lesson solves

The model reads everything in its context window. A poisoned document, a
clever user, or a sloppy tool can place secrets or other tenants' data in
front of it. Once data is in context, the model cannot unsee it. Prevention
must happen before context assembly.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The model cannot unsee</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Filter before context. After is too late.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">tool returns all rows</text>
<rect x="44" y="200" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">model sees salaries of all</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Leak already happened.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">tool returns 8 rows</text>
<rect x="420" y="200" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">model sees only the team</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Nothing to leak.</text>
<defs><marker id="m72a1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m72a1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">filter before context</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The check runs before assembly. The model never receives what it must not see.</text>
</svg>
<figcaption>Shell 3. Filtering moves before context assembly. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-1A: requests cross trust boundaries, and every hop is a chance to
check. Lesson 7-3A: injection is real, so untrusted text must not become
instructions. Lesson 7-4A: compliance names the owner of each control.

| Foundation | What it gives this lesson |
|---|---|
| §7.1 systems | Trust boundaries sit between hops |
| §7.3 LLM | Prompt text is untrusted input, not a lock |
| §7.4 business | Each control gets an owner and a review date |

## 3. Mental model

Three questions, three different answers. Authentication: who knocks?
Authorization: which rooms may they enter? Enforcement: is the door locked,
or is there only a sign? The model reads signs. It is not a lock. Locks
are code that runs before data reaches the model.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Signs are not locks</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">A user claim convinces the model. Only code convinces the data.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">"I am a manager"</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">model believes the claim</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Payroll rows flow.</text>
<text x="44" y="276" font-size="13" fill="#5C6B7A">A sign, not a lock.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="120" height="36" rx="999" fill="#E7F1F8"/>
<text x="480" y="167" font-size="13" text-anchor="middle" fill="#1B2838">authN</text>
<rect x="548" y="144" width="120" height="36" rx="999" fill="#F6E7A8"/>
<text x="608" y="167" font-size="13" text-anchor="middle" fill="#1B2838">authZ</text>
<rect x="420" y="192" width="248" height="40" rx="8" fill="#E7F4EF"/>
<text x="544" y="217" font-size="13" text-anchor="middle" fill="#1B2838">8 rows pass the gate</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Code decides. Model formats.</text>
<defs><marker id="m72a3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m72a3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">check before context</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Who knocks, which rooms open, and a real lock: three separate answers.</text>
</svg>
<figcaption>Shell 4. Claims move from the model to code before context. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

A request arrives with an identity token. Authentication verifies the
token: signature, expiry, audience. Authorization consults policy: this
identity, this action, this resource. The enforcement point permits or
denies. Only permitted data enters the context. The audit log records who,
what, and the decision.

Prompt text never decides access. A sentence in the system prompt is
guidance, not a lock.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The gate before the model</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">5,000 rows in the table. 8 rows reach the model. The gate decides.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">tool returns all rows</text>
<rect x="44" y="200" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="229" font-size="14" text-anchor="middle" fill="#1B2838">5,000 rows in context</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">Model filters by user claim.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="460" y="171" font-size="12" text-anchor="middle" fill="#1B2838">authN</text>
<rect x="508" y="148" width="80" height="36" rx="999" fill="#F6E7A8"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">authZ</text>
<rect x="596" y="148" width="80" height="36" rx="999" fill="#E7F4EF"/>
<text x="636" y="171" font-size="12" text-anchor="middle" fill="#1B2838">audit</text>
<rect x="420" y="200" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="229" font-size="14" text-anchor="middle" fill="#1B2838">8 rows in context</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">5,000 - 4,992 denied = 8.</text>
<defs><marker id="m72a4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m72a4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">enforce at the tool</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The tool is the enforcement point. Denied rows never enter context.</text>
</svg>
<figcaption>Shell 4. The tool gate cuts 5,000 rows to 8 before the model sees them. Source: original toy.</figcaption>
</figure>

:::takeaway
Authentication says who knocks. Authorization says which rooms open.
Enforcement is code before context. The model is none of the three.
:::

## 5. Minimal worked example

Toy: payroll lookup. 5,000 employees, 200 managers. Request: "show my
team's salaries."

Before: the tool runs the query as a service account and returns every
row the SQL matched. The model is told "only show this user's team." A
user who claims a bigger team sees bigger salaries.

After: the tool takes the caller's identity, checks the HR policy table,
and returns only the 8 direct reports. The model formats 8 rows. It
cannot leak what it never received.

Audit math (toy assumption: 200 bytes per event): 1,000,000 tool calls
per day times 200 bytes = 200,000,000 bytes per day = 200 MB per day,
times 30 = 6,000 MB = 6 GB per month.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Eight rows, not five thousand</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The filter runs in the tool. The model formats what survives.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">5,000 rows to the model</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">Service account query.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">Prompt says "own team only."</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Claim decides. Sign, not lock.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">8 rows to the model</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">Caller identity checked.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">HR policy consulted.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Audit: 200 MB / day.</text>
<defs><marker id="m72a5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m72a5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">authZ filter at tool</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The model cannot leak rows it never received. That is the whole defense.</text>
</svg>
<figcaption>Shell 4. The tool filter shrinks the context from 5,000 rows to 8. Source: original toy.</figcaption>
</figure>

### The 10-step best-answer method in action

The canonical 10-step best-answer method, applied to this question:

Mini question: "A shared support bot reads order history. Agents must see
only their region's orders. Which design fits? A) System prompt: 'only show
your region.' B) The tool checks the agent's identity and filters by region
before returning rows. C) One deployment per region."

| Step | Action on this question |
|---|---|
| 1. Question type | Best architecture under data isolation |
| 2. Lifecycle stage | Design |
| 3. Objective | One shared bot where agents see only their region |
| 4. Hard constraints | Cross-region reads are forbidden. One shared deployment |
| 5. System layer | Authorization before context, not instructions |
| 6. Infeasible options | None: all three could run |
| 7. Constraint violators | A is guidance, not enforcement. C breaks the shared-bot constraint |
| 8. Compare survivors | Only B remains |
| 9. Hidden consequences | C multiplies deployments and cost. A fails audit |
| 10. Verify | B is the complete single answer |

Verdict: B. The decisive constraint is deterministic isolation, and only B

Do not assume the exam always wants more autonomy, a larger model, more tools, more logging, a human reviewer everywhere, a new framework, or a complete redesign. Sometimes the best answer is: clarify the requirement, remove an unnecessary capability, fix retrieval, add a deterministic validation gate, narrow permissions, or preserve an existing sufficient workflow. The scenario, not a slogan, determines the answer.
enforces it in code before the model sees the data.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| OAuth2 and OIDC | Delegated login. ID token vs access token | V2-D3.2 authentication vs authorization |
| Scopes, audience, lifetime | Token fields | V2-D3.2 least privilege, no shared creds |
| MCP tool server | Tool boundary | V2-D3.7 integration, V2-D3.1 tool config |
| Vault for secrets | Secrets manager, general practice | V2-D3.2 secrets never in prompts |

## 7. Current limitations

Authorization cannot fix bad data: permitted rows can still be wrong.
Tokens can be stolen. Short lifetimes limit the damage. The confused
deputy: a tool with broad rights acts on a narrow user's request, so scope
the tool's identity too. Audit logs need their own protection.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Shrink the theft window</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">A stolen token lives until expiry. Short life means short damage.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">token lives 24 hours</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Stolen at hour 1.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Abused for 23 hours.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">token lives 15 minutes</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">24 x 60 / 15 = 96.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Damage window shrinks 96x.</text>
<defs><marker id="m72a7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m72a7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">cut the lifetime</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Short lifetimes do not stop theft. They cap its blast radius.</text>
</svg>
<figcaption>Shell 3. A 15-minute token shrinks the theft window 96-fold. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Instruction-only control | Prompt tells the model the rule | Demo with no real data |
| Separate deployment per tenant | Physical isolation | Two tenants, extreme regulatory split |
| Deterministic enforcement (this lesson) | Code checks before context | Any real data, any scale |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Side effects or sensitive reads | Deterministic enforcement, fail closed |
| Attribution matters (who did what) | No shared credentials. Per-user identity |
| Regulation names the control | Enforcement plus audit log, owner assigned |
| Local single-user tool, no secrets | Skip the machinery |

## 10. Valid-but-inferior option

Separate deployment per tenant. Valid: real isolation, simple mental
model. Inferior at scale: N tenants means N deploys, N configs, N bills.
Toy: 50 clinics times a full stack versus one stack with tenant_id on
every query. Ops cost grows with tenants instead of staying flat.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Per-tenant deployment | True physical isolation | Cost and ops grow with every tenant |

## 11. Counterfactual where the alternative wins

Two hospitals. Regulators require physical data separation. No shared
anything. Two deployments win: the requirement is separation itself, not
efficiency.

| Situation | Winner | Why |
|---|---|---|
| Mandated physical separation | Per-tenant deployment | Separation is the requirement |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Authentication answers ______.
2. Authorization answers ______.
3. The ______ runs before data enters context.
4. One million audit events per day is ______ MB.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A support inbox bot reads customer emails with PII.
Agents handle three brands. Brand A's agents must never
see Brand B's customers.
Name the check, the layer, and the audit record.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| authN, authZ, OAuth mechanics | General principle | Security canon | Long-standing |
| Toy payroll and audit arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Exam: prompts are not authorization. Deterministic enforcement for side effects | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| MCP as an integration surface | Current product behavior, secondary | S04 prep-path list | Sept 2026 |

:::takeaway
The exam's favorite trap is a prompt doing a lock's job. Ask: what code
runs before the data reaches the model? If the answer is "the prompt,"
pick another option.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Model cannot unsee context | All rows reach the model | 8 rows reach the model | f01 | SVG | Original |
| u02 | Boundaries and owners carry over | -- | Prerequisite table | f02 | Table | §7.1, §7.3, §7.4 |
| u03 | Signs are not locks | Claim convinces the model | Code gate: authN, authZ | f03 | SVG | Original |
| u04 | Gate before the model | 5,000 rows in context | 8 rows in context | f04 | SVG | Original |
| u05 | Tool filter shrinks context | 5,000 rows to model | 8 rows. Audit 200 MB/day | f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches isolation need | f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | f06 | Table | S03, S04 |
| u07 | Short token life caps theft | 24-hour token | 15-minute token, 96x smaller window | f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide the control | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Per-tenant deploy is valid but inferior | -- | Validity vs inferiority table | f10 | Table | Original |
| u11 | Mandated separation favors two deploys | -- | Counterfactual table | f11 | Table | Original |
| u12 | Three answers from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to inbox PII | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
