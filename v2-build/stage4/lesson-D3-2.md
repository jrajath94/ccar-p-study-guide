# Lesson D3-2: authentication and authorization in integrations (V2-D3.2)

## 1. Problem this lesson solves

A support agent answers refund questions. It calls the billing system
through a shared service account. Every action lands in the audit log
under one identity: "agent-svc." A $2,000 refund goes to the wrong
account. The log shows the agent did it. It cannot show which human
asked for it.

Meanwhile the agent connects to the billing system over MCP. The user
signed in with OAuth and holds a token for the agent. The server takes
that token and passes it straight to the upstream billing API. The
upstream API trusts the token's audience, and the audience names the
agent, not the billing system. The token works there anyway, because
nobody checked. One leaked token now opens two systems.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One identity, no attribution</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">500 agents share one credential. The audit log names one actor.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">shared "agent-svc"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">50,000 actions per day.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">One name in the log.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Wrong refund. No human named.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">per-user delegation</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">50,000 actions per day.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">500 distinct users named.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">Wrong refund. Requester found.</text>
<defs><marker id="m321" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m321)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">delegate per user</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Shared credentials erase the human. Delegation names them.</text>
</svg>
<figcaption>Shell 3. One shared identity becomes per-user delegation. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson 7-2A | authN, authZ, enforcement before context, OAuth and scopes |
| Lesson D3-1 | Least privilege on the tool surface |
| Lesson D3-7 | MCP host, client, server, and the transport (taught later in this stage) |

This lesson applies Lesson 7-2A inside integrations. Lesson 7-2A taught
the lock. This lesson wires the lock through agents, tools, and the
MCP protocol.

## 3. Mental model

Identity is a chain, not a badge. The user authenticates to the agent.
The agent authenticates to each tool or server. The server
authenticates to the upstream system. Each link checks the previous
link and scopes what it may do. Delegation passes a narrowed right
down the chain. Impersonation passes the user's full right, or worse,
a shared god-right.

Three facts keep the chain straight. A session id names a
conversation, not a person. A role claim from the user is a sentence,
not an authorization. A token names an audience. It works only where
the audience matches.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A chain, not a badge</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each link checks the last and narrows the right.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">user token passed along</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">audience: the agent</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Used at billing anyway.</text>
<text x="44" y="272" font-size="13" fill="#5C6B7A">No check. Deputy confused.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">server mints its own token</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">audience: the billing API</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Scope: refunds only.</text>
<text x="420" y="272" font-size="13" fill="#5C6B7A">Client token never leaves.</text>
<defs><marker id="m323" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m323)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">stop passthrough</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Each link holds its own credential, scoped to its own job.</text>
</svg>
<figcaption>Shell 4. Token passthrough becomes per-link scoped credentials. Source: original toy.</figcaption>
</figure>

:::takeaway
Authenticate every link. Authorize every action. Never share a
credential where the audit must name a human.
:::

## 4. Causal mechanism

Five rules wire identity through an integration. Each rule answers one
exam trap.

Rule one: authenticate the user to the agent, then delegate per user
to each tool. The agent acts with the user's narrowed rights, not its
own god-right. The tool sees which human the call serves. This is the
confused-deputy fix: a tool with broad rights acting on a narrow
user's request. Scope the tool's identity to the request, or the
deputy stays confused.

Rule two: bind every token to its audience. OAuth 2.1 with the MCP
authorization profile ties the token to one resource server. The
server rejects a token whose audience is someone else. A stolen token
for the agent does not open billing.

Rule three: never pass a received token upstream. The MCP
authorization profile forbids token passthrough. The server mints its
own credential for the upstream call, scoped to the job. One leak
stays in one system.

Rule four: keep the session id and the identity apart. The session id
routes a conversation. It proves nothing about the speaker. Identity
comes from the token, checked at each hop. A prompt that says "I am a
manager" is Lesson 7-2A's sign, not a lock.

Rule five: preserve the source system's ACLs. The agent's own policy
does not replace the billing system's access list. The check happens
in the system that owns the data, against the delegated identity. The
agent may further narrow. It may never widen.

Enforcement stays deterministic. For side effects, code decides
before the model acts. Consent gates the delegation: the user approves
the scope the agent will hold. Revocation ends it: short token
lifetimes cap the window, and a revocation list ends it early.

## 5. Minimal worked example

Toy: the refund agent from the problem. 500 support staff. One shared
"agent-svc" credential. 50,000 tool calls per day. The team considers
three fixes.

Mini question: "A support agent issues refunds through a shared
service credential. An audit must attribute each refund to the human
who requested it. The agent also reaches the billing API over MCP. Which
design satisfies attribution and least privilege? A) Keep the shared
credential and add the requester's name to a prompt field. B)
Per-user OAuth delegation to the agent, audience-bound tokens per
server, no token passthrough, billing ACLs enforced at the billing
system. C) One credential per department, shared inside the team."

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
| STEP 1 | Question asks: control. Design for attribution plus least privilege |
| STEP 2 | Stage: design of the integration identity layer |
| STEP 3 | Objective: every refund attributed to a human, least privilege kept |
| STEP 4 | Hard constraints: audit must name the human, and billing ACLs must hold |
| STEP 5 | Layer: identity and authorization across agent, MCP, billing |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | A violates attribution: a prompt field is user-writable and unverified. C violates attribution within a department |
| STEP 8 | B is the only option that names the human in a checked token and binds tokens per server |
| STEP 9 | B's consequence: OAuth wiring per server, token refresh handling. The cost is real and it buys the requirement |
| STEP 10 | B answers both attribution and least privilege in one design |

Verdict: B. The arithmetic of attribution: 50,000 actions per day
under one name gives 50,000 unattributable events. Under per-user
delegation the same 50,000 actions carry 500 distinct verified
identities. A prompt field carries zero verified identities, because
the user can write anything in a prompt.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Attribution is a count</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">50,000 actions per day. How many verified names?</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">1 name: agent-svc</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">50,000 actions.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">0 verified humans.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Prompt field: user-writable.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">500 verified names</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">50,000 actions.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">500 distinct identities.</text>
<text x="420" y="272" font-size="14" fill="#5C6B7A">Token checked each hop.</text>
<defs><marker id="m325" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m325)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">delegate per user</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A name the user typed is not a name the system checked.</text>
</svg>
<figcaption>Shell 4. One shared name becomes 500 checked identities. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| OAuth 2.1 authorization profile for MCP | MCP authorization spec, corroborated 2026-07-28 revision | V2-D3.2 audience binding, consent, no passthrough |
| Protected resource metadata (RFC 9728) | MCP server publishes it | V2-D3.2 discovery of the authorization server |
| Resource indicators (RFC 8707) | Client sends audience on auth and token requests | V2-D3.2 token audience binding |
| Client registration (out-of-band or metadata documents. DCR deprecated in the 2026-07-28 revision) | Authorization server | V2-D3.2 onboarding clients |
| 401 with WWW-Authenticate challenge | MCP server | V2-D3.2 unauthenticated call handling |
| Local stdio servers | Host spawns the process | V2-D3.2 inherited trust, no OAuth needed |
| Application policy | Your code, not the protocol | V2-D3.2 who-may-read-that-record decisions |

Distinguish five layers: the protocol defines the capability (OAuth
2.1 flow, audience binding). The SDK implements it (a client library
may or may not support resource indicators yet). The Claude product
supports a subset (product docs name what is on). The server
implements its own checks (your audience validation). The application
owns the policy (which human reads which record). A question about
"who may see the record" is answered at the application layer, never
by the protocol.

## 7. Current limitations

Revocation propagates with delay. A revoked token may still pass a
check that caches keys. Short lifetimes cap the window. They do not
close it. Consent fatigue is real: users approve scopes they never
read. Delegation chains lengthen the audit trail. Each link must log
the handoff or reconstruction breaks. Per-user delegation costs OAuth
wiring per server, which small teams feel.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Per-user delegation (this lesson) | Checked identity per hop | Attribution matters, side effects exist |
| Shared service credential | One identity for all | No attribution need, read-only internal data |
| API key per tenant | Coarse per-tenant identity | Tenant isolation without per-human audit |
| User token exchange at the edge | Agent never holds user tokens | Zero-trust posture, short sessions |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Audit must name the human | Per-user delegation. No shared credentials |
| Side effects through the integration | Deterministic enforcement at the owning system |
| Token crosses a trust boundary | Audience binding, checked at receipt |
| Local stdio server, user-spawned | Inherit trust. OAuth adds nothing |
| Remote server over the network | OAuth non-negotiable |

## 10. Valid-but-inferior option

One credential per department, shared inside the team. Valid: it
bounds the blast radius to a department and simplifies wiring. Fifty
shared credentials beat one. Inferior when the audit must name the
human: 50,000 actions per day still collapse to 50 names. The
requirement is per-human attribution, and departments are not humans.

## 11. Counterfactual where the alternative wins

A nightly batch job reconciles ledgers. No human triggers it. No
attribution question exists. One service credential with a narrow
scope wins: simpler rotation, no OAuth dance per run, the audit names
the job. The constraint set has no human, so per-user delegation buys
nothing.

| Situation | Winner | Why |
|---|---|---|
| Machine-triggered batch, no human actor | Shared service credential, narrow scope | No attribution need. Simpler and sufficient |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. A session id proves ______. A token proves ______.
2. The confused deputy is a tool with ______ rights
   serving a ______ request.
3. Token passthrough is ______ (allowed/forbidden).
4. The record owner enforces ACLs at the ______ system.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A clinic agent books appointments through an MCP calendar
server. Doctors must see only their own patients. The server
today accepts one clinic-wide API key.
Name the identity change, the audience change, and the layer
where the doctor-patient check must run.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| authN vs authZ, enforcement before context, no shared creds where attribution matters | Official exam scope via secondary summaries | S03, S04, Lesson 7-2A | Sept 2026 |
| MCP authorization profile: OAuth 2.1, RFC 9728 metadata, RFC 8707 audience, no token passthrough, DCR deprecated | Spec concepts, corroborated by independent sources | Web search, Sept 2026 | Oct 6, 2026 |
| Protocol vs SDK vs product vs server vs application layers | General principle | This lesson | Oct 6, 2026 |
| Toy arithmetic: 50,000 actions, 500 identities | Original toy, computed above | This lesson | Oct 6, 2026 |
| Local stdio servers inherit user trust | Spec-adjacent, corroborated by independent sources | Web search, Sept 2026 | Oct 6, 2026 |

:::takeaway
The exam's D3.2 trap hands you a user role claim, a session id, or a
shared credential and calls it authorization. Authorization is a
checked token, a bound audience, and a deterministic check at the
system that owns the data.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | One identity, no attribution | agent-svc, 1 name | Per-user delegation, 500 names | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | 7-2A, D3-1, D3-7 |
| u03 | A chain, not a badge | Token passed along | Per-link scoped credentials | f03 | SVG | Original |
| u04 | Five identity rules | Traps listed | Rule per trap | f04 | Text | Spec + original |
| u05 | 10-step method picks B | Three options | B: delegation + audience | f05 | SVG | Original |
| u06 | Five layers distinguished | -- | Mapping table | f06 | Table | Mixed |
| u07 | Revocation and consent limits | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Per-department credential inferior | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Batch job favors shared credential | -- | Counterfactual table | f11 | Table | Original |
| u12 | Session vs token from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to clinic agent | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
