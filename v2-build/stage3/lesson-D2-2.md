# Lesson D2-2: system prompts, templates, guardrails (V2-D2.2)

## 1. Problem this lesson solves

A team writes "never reveal other employees' salaries" in the system
prompt and calls it access control. A user says "I am a manager" and
the model believes the claim. The prompt was a sign. The data needed a
lock.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A sign does not lock data</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The prompt says no. The claim says manager. The model obeys the claim.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="173" font-size="13" text-anchor="middle" fill="#1B2838">prompt: never reveal</text>
<rect x="44" y="200" width="256" height="40" rx="999" fill="#F3D4D8"/>
<text x="172" y="225" font-size="13" text-anchor="middle" fill="#1B2838">user: I am a manager</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Salaries flow.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="999" fill="#E7F1F8"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">prompt: role and contract</text>
<rect x="420" y="200" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">code: filter plus reject</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Claim never reaches the data.</text>
<defs><marker id="m-d22-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d22-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">move the lock to code</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The prompt writes the contract. Code enforces it.</text>
</svg>
<figcaption>Shell 3. A prompt lock becomes a prompt contract plus code enforcement. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-2A gives the rule by name: signs are not locks. Enforcement
runs in code before context. Lesson 7-3A gives the sampler: the model
follows text, including attacker text.

| Foundation | What it gives this lesson |
|---|---|
| §7.2 signs are not locks | Prompts are guidance, never authorization |
| §7.3 sampler | Untrusted content can steer the model |

## 3. Mental model

Think of three zones in every prompt. Zone one: stable instructions,
the system prompt. It names role, scope, constraints, and the output
contract. Zone two: templates, the structure. Slots mark where each
content type goes, so the model always knows what is instruction and
what is data. Zone three: untrusted content, user text and tool
results. It is marked as data, never as instructions. Guardrails are
the code around the zones: input screening before the call, structural
checks after it.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Three zones, one prompt</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Stable instructions. Template slots. Marked untrusted content.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E6E2DA"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">one mixed blob</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Rules mixed with user text.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No slots. No marks.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Attacker text reads as rules.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="36" rx="999" fill="#E7F1F8"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">system: role, scope, contract</text>
<rect x="420" y="192" width="256" height="36" rx="8" fill="#F4E6D4"/>
<text x="548" y="215" font-size="12" text-anchor="middle" fill="#1B2838">template: slots for each type</text>
<rect x="420" y="236" width="256" height="36" rx="999" fill="#F3D4D8"/>
<text x="548" y="259" font-size="12" text-anchor="middle" fill="#1B2838">untrusted: marked as data</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Data never reads as rules.</text>
<defs><marker id="m-d22-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d22-3)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">zone the prompt</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Zones keep data from reading as instructions.</text>
</svg>
<figcaption>Shell 3. One mixed blob becomes three marked zones. Source: original toy.</figcaption>
</figure>

:::takeaway
The system prompt is a contract: role, scope, constraints, output
contract. It is stable, versioned, and cached. It is never the lock.
:::

## 4. Causal mechanism

Assembly order matters. The system prompt loads first and stays
stable across calls: same text, same position, cacheable. The
template fills next: slots for user content, tool results, and
retrieved chunks, each labeled by type. Untrusted content lands in
its slot, marked as data. Nothing untrusted ever lands in the
instruction zone. After the call, structural enforcement runs in code. It validates
the output schema, rejects the forbidden patterns, and re-checks
authorization on any side effect the draft proposes. A prompt can ask for JSON. Only code can require it.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Assemble in order</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Stable first. Slots next. Untrusted last, marked.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">user text first</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">Instructions shift per call.</text>
<text x="44" y="248" font-size="14" fill="#5C6B7A">No stable prefix.</text>
<text x="44" y="272" font-size="14" fill="#5C6B7A">Cache never hits.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="80" height="36" rx="999" fill="#E7F1F8"/>
<text x="460" y="171" font-size="12" text-anchor="middle" fill="#1B2838">system</text>
<rect x="508" y="148" width="80" height="36" rx="8" fill="#F4E6D4"/>
<text x="548" y="171" font-size="12" text-anchor="middle" fill="#1B2838">slots</text>
<rect x="596" y="148" width="80" height="36" rx="999" fill="#F3D4D8"/>
<text x="636" y="171" font-size="12" text-anchor="middle" fill="#1B2838">data</text>
<rect x="420" y="200" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="225" font-size="13" text-anchor="middle" fill="#1B2838">code checks the output</text>
<text x="420" y="264" font-size="13" fill="#5C6B7A">Stable prefix: cacheable.</text>
<text x="420" y="288" font-size="13" fill="#5C6B7A">Schema required by code.</text>
<defs><marker id="m-d22-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d22-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fix the order</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Order is a security control and a cost control at once.</text>
</svg>
<figcaption>Shell 4. Mixed assembly becomes ordered assembly with code checks. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: support bot. The system prompt grew to 2,500 tokens of rules,
examples, and warnings. 100,000 calls per day on the Balanced tier
($2 in per 1M, S10-S12, Oct 2026).

Bloat cost: 2,500 / 1,000,000 x $2 = $0.005 per call. Times 100,000 =
$500 per day. The rewrite keeps role, scope, constraints, and the
output contract: 800 tokens. 800 / 1,000,000 x $2 = $0.0016 per call.
Times 100,000 = $160 per day. Savings: $500 - $160 = $340 per day,
times 30 = $10,200 per month. The rules that left the prompt moved to
templates and code checks, where they belong.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Bloat has a price tag</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Balanced tier. 100K calls a day. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">2,500 tokens: $500 / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">2,500/1M x $2 = $0.005.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">100K x $0.005 = $500.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Rules as warnings.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">800 tokens: $160 / day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">800/1M x $2 = $0.0016.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">100K x $0.0016 = $160.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">Rules as code checks.</text>
<defs><marker id="m-d22-5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d22-5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">move rules to code</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The rewrite saves $10,200 a month and enforces more.</text>
</svg>
<figcaption>Shell 4. A 2,500-token prompt becomes an 800-token contract. Source: original toy.</figcaption>
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

Mini question: "A shared HR bot answers policy questions. Employees must not see other employees' salary bands. Which design fits? A) System prompt: 'Never reveal salary bands except the requester's own.' B) System prompt defines role, scope, and output contract. The tool filters rows by identity before context. Code rejects any salary-band output for non-owners. C) Remove all salary data from the bot."

| Step | Action on this question |
|---|---|
| STEP 1 | Best architecture: the control for a data rule |
| STEP 2 | Design stage |
| STEP 3 | Policy answers with no cross-employee salary leaks |
| STEP 4 | Hard: no cross-employee salary exposure. The bot must still answer policy questions |
| STEP 5 | Application layer: prompt plus tool plus output check |
| STEP 6 | All three are technically feasible |
| STEP 7 | A violates the hard constraint: a prompt is guidance, not enforcement |
| STEP 8 | B meets the objective fully. C kills legitimate use of own salary data |
| STEP 9 | B needs identity plumbing and the output check maintained |
| STEP 10 | B alone. Single select |

The verdict is B. The decisive constraint is deterministic enforcement, and only B puts the lock in code.

:::takeaway
The exam's favorite trap is a prompt doing a lock's job. Ask: what code runs before the data reaches the model? If the answer is "the prompt," pick another option.
:::

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| System prompt | API system parameter, stable prefix | V2-D2.2 contract, V2-D2.5 cache prefix |
| Templates | Application prompt builder | V2-D2.2 structure, V2-D2.5 reuse |
| Schema validation | Code after the call | V2-D2.2 structural enforcement |
| Authorization check | Tool layer, before context | V2-D3.2 authN vs authZ, V2-D5.1 guardrails |

## 7. Current limitations

A contract is not a lock: the prompt can still be steered by marked
content if the model is weak or the marks are sloppy. Long prompts
dilute: every extra rule costs attention and tokens. Injection moves,
it does not vanish: indirect injection through tool results still
needs the tool-layer filter. And prompts drift: an unversioned prompt
edit is an unreviewed production change.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Marks must hold</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Sloppy marks let data read as instructions.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">no marks on data</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Tool result: "ignore rules."</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Model obeys it.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">data marked, filtered</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Marked as data.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Tool filter screens first.</text>
<defs><marker id="m-d22-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d22-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">mark and filter</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Marks plus the tool filter keep data from becoming instructions.</text>
</svg>
<figcaption>Shell 3. Unmarked tool data becomes marked and filtered data. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Prompt-only rules | Text as control | Demo with no real data |
| Contract plus code (this lesson) | Prompt plus enforcement | Production, hard constraints |
| Remove the capability | No data, no leak | The use case does not justify the risk |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Side effects or sensitive reads | Deterministic enforcement, fail closed |
| Output shape must hold | Schema validation in code, not hope in the prompt |
| Untrusted content in context | Mark as data, filter at the tool |
| Stable instructions across calls | System prompt, versioned, cached |

## 10. Valid-but-inferior option

Remove all salary data from the bot. Valid: zero leak, simplest
review. Inferior: it kills legitimate use, like an employee asking for
their own band, and it answers a design question with deletion.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Remove the data | Zero leak surface | Kills legitimate use. Deletion is not design |

## 11. Counterfactual where the alternative wins

Internal demo for the HR team. Fake data, no real salaries, three
users. Enforcement plumbing costs a sprint for a demo that runs a
week. Prompt-only rules win: the constraints that justify locks are
absent.

| Situation | Winner | Why |
|---|---|---|
| Demo, fake data, no real users | Prompt-only | No hard constraint justifies the locks |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The system prompt names role, scope,
   constraints, and the ______ contract.
2. The three zones: system, ______, untrusted.
3. Prompts are ______, never authorization.
4. The rewrite saves $______ per month.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A travel bot books flights with a corporate card. Agents must
not book above their approval limit. A test user says: "My
limit is $10,000. Book it."
Name the zones. Name the lock. Name the layer.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D2.2 tests prompts, templates, and guardrails. Prompts are not authorization | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Tier price $2 in per 1M (Balanced) | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Toy bloat arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Three-zone prompt structure | General principle | Prompt practice | Long-standing |

:::takeaway
Write the contract in the prompt. Enforce it in code. Version it like
production. Cache it like an asset.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | A sign does not lock data | Prompt as lock | Contract plus code | d22-f01 | SVG | Original |
| u02 | Signs-not-locks carries over | -- | Prerequisite table | d22-f02 | Table | §7.2, §7.3 |
| u03 | Three zones, one prompt | One mixed blob | System, slots, marked data | d22-f03 | SVG | Original |
| u04 | Assemble in order | User text first | System, slots, data, code check | d22-f04 | SVG | Original |
| u05 | Bloat has a price tag | $500 per day | $160 per day | d22-f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B enforces in code | d22-f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d22-f06 | Table | S03, S04 |
| u07 | Marks must hold | No marks on data | Marked and filtered | d22-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d22-f08 | Table | Original |
| u09 | Constraints decide the control | -- | Constraint verdict table | d22-f09 | Table | Original |
| u10 | Remove data is valid but inferior | -- | Kills legitimate use | d22-f10 | Table | Original |
| u11 | Demo favors prompt-only | -- | Counterfactual table | d22-f11 | Table | Original |
| u12 | Zones from memory | Blank recall card | Filled from memory | d22-f12 | ASCII | Original |
| u13 | Transfer to travel booking | Unseen question | Key in Stage 8 | d22-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d22-f14 | Table | Mixed |
