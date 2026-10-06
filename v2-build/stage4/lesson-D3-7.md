# Lesson D3-7: integration mechanisms (V2-D3.7)

## 1. Problem this lesson solves

A team needs their agent to call one internal billing API. The team
picks MCP because it is the standard. They write a server, wire a
client, negotiate versions, and handle the protocol lifecycle. Three
weeks later the integration works. A direct HTTPS call would have
taken one day.

In the next building, a team builds the same billing API for five
different hosts in three languages. They hand-roll five bespoke
clients. Each host invents its own tool schema. Bugs multiply. MCP
would have meant one server, five clients, one schema.

Both teams chose by fashion. The mechanism must match the reuse, not
the trend.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Fashion picks the mechanism</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One API, one host: 3 weeks of protocol. Five hosts: 5 bespoke clients.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">MCP for one API, one host</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">15 days vs 1 day</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Protocol with no reuse.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">direct API for one host</text>
<rect x="420" y="196" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">MCP for five hosts</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">Reuse decides. Not fashion.</text>
<defs><marker id="m371" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m371)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">match reuse</text>
<text x="24" y="312" font-size="15" fill="#1B2838">MCP is not automatically better than a direct API.</text>
</svg>
<figcaption>Shell 3. The mechanism follows the reuse pattern. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

| Foundation | What it gives this lesson |
|---|---|
| Lesson 7-1A | HTTP, processes, trust boundaries between hops |
| Lesson 7-2A | Security boundaries live between components |

## 3. Mental model

Five mechanisms connect an agent to the world. Direct API or SDK: a
function call over HTTPS, your code, your schema. CLI: a subprocess
call, text in and text out. MCP: a standard protocol between a host,
its clients, and servers that expose tools, resources, and prompts.
Agent to agent: one agent delegates to another, each with its own
loop. Managed runtime: a platform hosts the agent loop and the
integrations for you.

Six axes score the pick. Reuse: how many consumers share the work.
Security boundaries: where trust changes hands. Ownership: who
builds and maintains it. Operational complexity: what runs in
production. Compatibility: languages, platforms, versions. Interaction
pattern: call and return, stream, or delegate a goal.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Six axes, five mechanisms</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Reuse decides most picks. The rest break ties.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">"we use MCP"</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">No axes. No scoring.</text>
<text x="44" y="240" font-size="13" fill="#5C6B7A">One answer for all cases.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="120" height="36" rx="999" fill="#E7F1F8"/>
<text x="480" y="171" font-size="12" text-anchor="middle" fill="#1B2838">reuse</text>
<rect x="548" y="148" width="120" height="36" rx="999" fill="#F6E7A8"/>
<text x="608" y="171" font-size="12" text-anchor="middle" fill="#1B2838">boundary</text>
<rect x="420" y="192" width="120" height="36" rx="999" fill="#E7F4EF"/>
<text x="480" y="215" font-size="12" text-anchor="middle" fill="#1B2838">owner</text>
<rect x="548" y="192" width="120" height="36" rx="999" fill="#E6E2DA"/>
<text x="608" y="215" font-size="12" text-anchor="middle" fill="#1B2838">ops cost</text>
<text x="420" y="244" font-size="13" fill="#5C6B7A">Plus compatibility, pattern.</text>
<text x="420" y="268" font-size="13" fill="#5C6B7A">Score each candidate.</text>
<defs><marker id="m373" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m373)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">score the pick</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Six axes beat one slogan.</text>
</svg>
<figcaption>Shell 3. One default mechanism becomes a six-axis comparison. Source: original toy.</figcaption>
</figure>

:::takeaway
Direct API for one consumer. MCP for many consumers. CLI for
legacy tools. Agent to agent for delegated goals. Managed runtime
when the platform owns the loop.
:::

## 4. Causal mechanism

Each mechanism moves work across a boundary differently.

Direct API or SDK: your code calls HTTPS. You own the schema, the
retries, the auth. Lowest ceremony for one consumer. Cost grows with
consumers: N hosts times M tools means N x M bespoke integrations.

CLI: your code spawns a process and parses text. It wraps tools that
already exist as commands. Text parsing is brittle. It wins when the
capability exists only as a CLI and rewriting it costs more.

MCP: the host creates one client per server. The client and server
speak JSON-RPC. The lifecycle runs in order: initialize with protocol
version and capabilities, discover with tools/list, resources/list,
and prompts/list, invoke with tools/call, resources/read, and
prompts/get, handle errors as structured responses, and negotiate
versions when they differ. Transport is stdio for local servers or
Streamable HTTP for remote ones. The server exposes three
primitives. Tools are callable actions, often side-effecting.
Resources are readable data addressed by URI. Prompts are reusable
templates. One server serves many hosts. The N x M problem becomes
N plus M.

Agent to agent: one agent hands a goal to another. Each keeps its
own loop, context, and tools. It wins when the subtask needs its own
planning and its own tools. It costs coordination: handoff contracts
and result verification (Lesson D1-patterns covers multi-agent
coordination).

Managed runtime: the platform runs the loop, the tools, and the
scaling. You configure. It wins when undifferentiated operations
dominate. It costs control: the platform's limits become your
limits.

Five layers keep MCP questions straight. The protocol defines the
capability: the messages, the lifecycle, the primitives. The SDK
implements a subset: a client library may lag the spec. The Claude
product supports a subset: product docs name what is actually on.
The server implements its own behavior: your code decides what each
tool does. The application owns the policy: who may call what.
"Can the model call this tool" is a protocol question. "Should this
user reach that record" is an application question (Lesson D3-2).

## 5. Minimal worked example

Toy: the billing API. Scenario X: one team, one host, one language.
Scenario Y: five hosts, three languages, one billing API. Options:
A) MCP server in both scenarios. B) Direct API in X, MCP server in
Y. C) CLI wrapper in both.

Integration arithmetic. Bespoke cost: N hosts x M tools. With M = 8
billing tools and N = 5 hosts, bespoke costs 40 integrations. MCP
costs 1 server plus 5 client wirings = 6 integration points. For N =
1, bespoke costs 8, MCP costs 1 server plus 1 client wiring plus
protocol handling. The direct call wins on simplicity.

Mini question: "One team, one host, one internal API with 8 tools.
Which integration mechanism fits best? A) Build an MCP server. B)
Call the API directly with an SDK. C) Wrap the API in a CLI."

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
| STEP 1 | Question asks: best architecture. Integration mechanism |
| STEP 2 | Stage: design of the integration |
| STEP 3 | Objective: call 8 tools with least total cost |
| STEP 4 | Hard constraints: one team, one host, one language |
| STEP 5 | Layer: integration mechanism |
| STEP 6 | All options are technically feasible. None eliminated here |
| STEP 7 | None violate stated constraints. All survive to comparison |
| STEP 8 | B has the lowest ceremony: no server, no protocol, no client wiring. A adds a server and lifecycle for zero reuse. C adds text parsing for no reason |
| STEP 9 | B's consequence: if a second host appears later, revisit. That is a future decision, not a present cost |
| STEP 10 | B alone minimizes present cost. A optimizes for reuse that does not exist |

Verdict: B. The reuse arithmetic: 1 host x 8 tools = 8 bespoke
calls vs 1 server + 1 client + protocol handling. The scenario has
no second consumer, so the protocol buys nothing. The exam's
verbatim warning applies directly: the scenario, not a slogan,
determines the answer. "MCP is standard" is a slogan.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">N x M vs N + M</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">5 hosts, 8 tools. Bespoke: 40 integrations. MCP: 6 points.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">5 x 8 = 40 bespoke</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Each host reinvents.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">Schemas drift.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">1 + 5 = 6 MCP points</text>
<text x="420" y="224" font-size="14" fill="#5C6B7A">One server, one schema.</text>
<text x="420" y="248" font-size="14" fill="#5C6B7A">Five thin clients.</text>
<defs><marker id="m375" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m375)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">share one server</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Reuse is the only reason a protocol earns its keep.</text>
</svg>
<figcaption>Shell 4. Forty bespoke integrations become six MCP points. Source: original toy.</figcaption>
</figure>

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Host, client, server plus tools, resources, prompts | MCP spec concepts | V2-D3.7 mechanism identity |
| initialize, */list, */call, */read, */get, errors, versioning | MCP lifecycle | V2-D3.7 discovery and invocation |
| stdio, Streamable HTTP | MCP transports | V2-D3.7 local vs remote |
| OAuth 2.1 authorization profile | MCP authorization spec | V2-D3.2, Lesson D3-2 |
| Direct SDK calls, CLI subprocess, managed runtimes | Your stack | V2-D3.7 alternatives to MCP |

MCP spec concepts above are corroborated by independent sources
against the 2026-07-28 spec revision (see evidence). Product support
for any single primitive must be checked in current product docs.
the protocol defines it, the product decides what ships.

## 7. Current limitations

Version skew: client and server negotiate, and old meets new.
Server quality varies: a bad server behind a standard protocol is
still a bad server. Debugging crosses a boundary: the host sees
structured errors, not the server's internals. The protocol does not
authorize data access. The application does (Lesson D3-2). SDK
support lags the spec. Check before you depend on a new primitive.

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Direct API or SDK | Bespoke HTTPS, your schema | One consumer, one language |
| MCP | Standard host-client-server | Many consumers or languages |
| CLI | Subprocess plus text parsing | Capability exists only as a CLI |
| Agent to agent | Delegated goal, own loop | Subtask needs its own planning |
| Managed runtime | Platform runs the loop | Ops dominate, control secondary |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| One host, one language | Direct API. Skip the protocol |
| Many hosts or languages | MCP. One server, one schema |
| Legacy capability, CLI only | CLI wrapper. Parse carefully |
| Subtask needs its own plan and tools | Agent to agent with handoff contract |
| Team wants zero ops | Managed runtime. Accept platform limits |
| "Use MCP" with no reuse named | Reject. The scenario decides |

## 10. Valid-but-inferior option

Build an MCP server for the single-host case. Valid: the protocol
works, the integration functions, and a second host later would
reuse it. Inferior now: a server, a client, lifecycle handling, and
version negotiation for 8 tools and 1 consumer. The direct call
ships in a day. The exam rewards the present scenario, not the
imagined future.

## 11. Counterfactual where the alternative wins

Five hosts in three languages share the billing API. The MCP server
wins outright: 6 integration points instead of 40, one schema, one
place to fix bugs. The direct API would mean 40 bespoke clients.
Reuse flips the winner.

| Situation | Winner | Why |
|---|---|---|
| Five hosts, three languages | MCP server | 6 points vs 40. One schema |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The three MCP primitives: ______, ______, ______.
2. The lifecycle order: ______, ______, ______.
3. One host creates ______ client(s) per server.
4. 5 hosts x 8 tools bespoke = ______. MCP = ______.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A data team exposes 12 warehouse tools to 4 different agent
hosts in 2 languages. Today each host has hand-rolled clients.
Bugs repeat in all four.
Name the mechanism, the primitive type for the tools, and
the integration-point count before and after.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Compare mechanisms on reuse, security boundaries, ownership, operational complexity, compatibility, interaction pattern. MCP not automatically better | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D3.7 | Sept 2026 |
| MCP architecture: host, client 1:1 per server, tools, resources, prompts, JSON-RPC, initialize, */list, */call, */read, */get, stdio and Streamable HTTP | Spec concepts, corroborated by independent sources against the 2026-07-28 revision | Web search, Sept 2026 | Oct 6, 2026 |
| MCP authorization profile: OAuth 2.1, audience binding, no passthrough | Spec concepts, corroborated by independent sources | Lesson D3-2, web search | Oct 6, 2026 |
| Toy arithmetic: 40 bespoke vs 6 MCP points | Original toy, computed above | This lesson | Oct 6, 2026 |
| Exact product support per primitive | Unverified | Check current product docs | Oct 6, 2026 |

:::takeaway
The exam's D3.7 trap is the slogan "MCP is the standard, so use
MCP." The six axes decide. No reuse, no protocol.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Fashion picks the mechanism | MCP for one host | Direct API. MCP for five | f01 | SVG | Original |
| u02 | Prior lessons carry over | -- | Prerequisite table | f02 | Table | 7-1A, 7-2A |
| u03 | Six axes, five mechanisms | One default | Scored comparison | f03 | SVG | Original |
| u04 | Mechanism and layer model | Slogan | Five mechanisms, five layers | f04 | Text | Spec + original |
| u05 | 10-step method picks B | Three options | B: direct API | f05 | SVG | Original |
| u06 | Concepts map to products | -- | Mapping table | f06 | Table | Mixed |
| u07 | Version skew and boundary limits | -- | Limitation list | f07 | Text | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide | -- | Constraint verdict table | f09 | Table | Original |
| u10 | MCP for one host inferior | -- | Validity vs inferiority | f10 | Text | Original |
| u11 | Five hosts flip the winner | -- | Counterfactual table | f11 | Table | Original |
| u12 | Primitives from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to data team | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
