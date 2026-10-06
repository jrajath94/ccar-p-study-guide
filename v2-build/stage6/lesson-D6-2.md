# Lesson D6-2: trade-off communication (V2-D6.2)

## 1. Problem this lesson solves

An architect tells the executives: "The agent hits 99% accuracy."
The executives approve. Three months later the bill lands: $80,000
per month. The engineers knew the cost. The security team never
heard the trade-off. Each audience got a different story, and none
got the whole truth.

A trade-off communicated to one audience is a rumor to the rest.
One option needs five messages, each tuned to what that audience
decides. And no message may promise what the numbers cannot prove:
no perfect accuracy, no zero risk.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One audience hears it all</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">99% accuracy to execs. $80,000 a month to no one.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">exec: "99% accuracy"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">$80,000 / month, unheard</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Surprise bill kills trust.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">exec: 99% at $80k / month</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">alt: 96% at $18k / month</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">The choice is theirs, priced.</text>
<defs><marker id="m-d62-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d62-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">price the trade</text>
<text x="24" y="312" font-size="15" fill="#1B2838">The decision belongs to the audience that pays.</text>
</svg>
<figcaption>Shell 3. A one-sided story becomes a priced choice. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D6-1 gives the measurable requirements that trade-offs
compare against. Lesson D5-1 gives the safety language for the
security audience.

| Foundation | What it gives this lesson |
|---|---|
| V2-D6.1 discovery | Numbers to compare options against |
| §7.2 enforcement | Security audience needs controls, not prose |

## 3. Mental model

Every option gets five fields: benefit, cost or concession, risk,
reversal cost, compliance impact. Then five audiences get five
versions of the same truth.

Executives decide on money and risk: net value, exposure, what
they sign. Engineers decide on build and run: latency, load,
failure behavior. Security decides on controls: data flows,
attack surface, enforcement. Legal and compliance decide on
evidence: retention, residency, audit trail. Product decides on
users: experience, error handling, support load.

:::takeaway
Five fields per option. Five audiences. Same truth, five
verdicts. A promise without a number is a rumor, not a message.
:::

<figure class="fig">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="420" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Five fields, five audiences</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One option. Each audience reads the field it owns.</text>
<rect x="24" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">"99% accuracy, great"</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">"ship it"</text>
<rect x="44" y="232" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">no risk named</text>
<rect x="44" y="292" font-size="13" fill="#5C6B7A">One slogan for everyone.</rect>
<rect x="400" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="124" height="36" rx="8" fill="#E7F4EF"/>
<text x="482" y="167" font-size="12" text-anchor="middle" fill="#1B2838">benefit: 99%</text>
<rect x="552" y="144" width="124" height="36" rx="8" fill="#F3D4D8"/>
<text x="614" y="167" font-size="12" text-anchor="middle" fill="#1B2838">cost: $80k / mo</text>
<rect x="420" y="188" width="124" height="36" rx="8" fill="#F6E7A8"/>
<text x="482" y="211" font-size="12" text-anchor="middle" fill="#1B2838">risk: 1% errors</text>
<rect x="552" y="188" width="124" height="36" rx="8" fill="#E7F1F8"/>
<text x="614" y="211" font-size="12" text-anchor="middle" fill="#1B2838">reverse: 2 weeks</text>
<rect x="420" y="232" width="256" height="36" rx="8" fill="#E6E2DA"/>
<text x="548" y="255" font-size="13" text-anchor="middle" fill="#1B2838">compliance: vendor data reviewed</text>
<text x="420" y="292" font-size="13" fill="#5C6B7A">Five fields. Each audience reads its own.</text>
<defs><marker id="m-d62-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="216" x2="384" y2="216" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d62-3)"/>
<text x="360" y="200" font-size="13" text-anchor="middle" fill="#1B2838">fill the five fields</text>
<text x="24" y="376" font-size="15" fill="#1B2838">Name the uncertainty. "99%" is a claim. "99% on eval set X" is a fact.</text>
</svg>
<figcaption>Shell 4. A slogan becomes five priced fields. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

An unsupported claim flows through the organization. The builder
says "perfect accuracy." The executive hears zero risk. Legal
hears no liability. Product ships on the assumption. The first
real error hits a customer. Blame flows backward to the person
who promised.

Quantified trade-offs with explicit uncertainties stop the
chain. Each audience sees the concession it must own. The
executive signs the risk, not the rumor. The exam tests this
directly: any option that promises perfect accuracy or zero risk
is the distractor, because no measurement supports it.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The promise price check</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">From "perfect" to priced: each claim pays in numbers or dies.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">"perfect accuracy"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">exec hears: zero risk</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">First error: blame, not a plan.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">99% on eval set, n = 500</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">1% errors: 100 per day</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Exec signs the 1%, not the slogan.</text>
<defs><marker id="m-d62-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d62-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">attach the numbers</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Uncertainty stated beats perfection promised.</text>
</svg>
<figcaption>Shell 3. An unpriced promise becomes a priced claim. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: 10,000 support tickets per day. Two options for the triage
agent.

Option A, agentic deep search: benefit, 99% precision on the
500-ticket eval set. Cost, $0.80 per ticket = $8,000 per day =
$240,000 per month. Concession, p95 latency 12 seconds. Risk,
1% errors = 100 misrouted tickets per day. Reversal cost, two
weeks to rebuild the pipeline. Compliance impact, vendor ticket
text stays in-region, reviewed.

Option B, hybrid retrieval plus rules: benefit, 96% precision.
Cost, $0.06 per ticket = $600 per day = $18,000 per month.
Concession, 3 extra points of error. Risk, 4% errors = 400
misrouted tickets per day, each needing 5 minutes of human fix =
400 x 5 = 2,000 minutes = 33.3 hours per day at $30 per hour =
$1,000 per day = $30,000 per month. Reversal cost, one week.
Compliance impact, same as A.

Net comparison: A costs $240,000 per month. B costs $18,000 +
$30,000 = $48,000 per month. B saves $192,000 per month at the
price of 300 extra misroutes per day. The executive message:
"B costs $192k less per month and needs 33 human hours a day
for corrections." The engineering message: "B runs at p95
3 seconds, holds no long tool loops, fails to a human queue."
The security message: "Both keep data in-region. B has fewer
tool hops and a smaller attack surface."

Mini question: "The triage agent must cost at most $60,000 per
month. Errors need human review. Which option do you recommend,
and how do you present it? A) Option A, described as near
perfect. B) Option B, with the $192,000 saving, the 400 daily
misroutes, and the 33 human hours priced. C) Option B,
described as perfect and risk free."

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
| STEP 1 | Recommendation plus its communication |
| STEP 2 | Design: options on the table |
| STEP 3 | Fit the $60,000 budget with honest review load |
| STEP 4 | Hard budget $60,000 per month. Errors need review |
| STEP 5 | Architecture selection with stakeholder message |
| STEP 6 | All three are feasible to say |
| STEP 7 | A breaks the budget: $240,000 per month. C breaks the honesty rule: perfect and risk free are unsupported |
| STEP 8 | B fits at $48,000 and states its own cost |
| STEP 9 | B needs 33 human hours per day staffed, or the misroutes pile up |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive facts are the budget and the honesty
rule. Option A breaks the budget. Option C breaks the truth.
Only B is both affordable and honest.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| Cost per task | Lesson D4-1, Lesson D1-2 | V2-D6.2 quantified benefit and cost |
| p95 latency | SLO practice | V2-D6.2 concession field |
| Reversal cost | ADR, V2-D6.4 | V2-D6.2 reversal field |
| Review triggers | Lesson D5-3 | V2-D6.2 risk field, human load |
| Compliance impact | Lesson D5-4 | V2-D6.2 compliance field |

## 7. Current limitations

Numbers go stale: costs change when the provider reprices.
Audiences rotate: the signed executive leaves and the new one
never saw the trade-off. Uncertainty hides in evals: 99% on a
500-ticket set may not hold on real traffic. And too many
options paralyze: six priced options can be worse than two.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The repriced trade-off</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Provider reprices. Option A no longer wins.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">B wins: $192k / mo saved</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Provider doubles token price.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">A now $480k / mo</text>
<rect x="420" y="208" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="233" font-size="14" text-anchor="middle" fill="#1B2838">recompute, re-sign</text>
<text x="420" y="260" font-size="13" fill="#5C6B7A">Date every number.</text>
<defs><marker id="m-d62-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d62-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">recompute the fields</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A trade-off has an expiry date. Put it on the page.</text>
</svg>
<figcaption>Shell 3. A static trade-off becomes a dated trade-off. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| One message for all | Same slide deck to everyone | Tiny team, one room, shared context |
| Five tailored messages (this lesson) | Benefit, cost, risk, reversal, compliance per audience | Execs, security, legal decide |
| Raw data dump | Numbers with no framing | Technical audience that wants the sheet |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Audience holds budget or sign-off | Quantified trade-off, priced concessions |
| Option promises perfect accuracy or zero risk | Distractor. No measurement supports it |
| Multiple audiences decide | Tailor per audience, same truth |
| One engineer decides alone | One message suffices |

## 10. Valid-but-inferior option

One message for all. Valid: it is fast and consistent. Inferior
here: executives cannot act on tool-hop counts, and security
cannot act on dollar savings. Each audience starves on the wrong
fields.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| One message for all | Fast, consistent | Wrong fields for three audiences |

## 11. Counterfactual where the alternative wins

Two-person startup. Builder and founder share a desk. The
founder holds budget, tech, and risk in one head. One message
wins: the five-audience split costs a day for zero gain.

| Situation | Winner | Why |
|---|---|---|
| Two people, one room | One message | All five audiences fit in one head |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Five fields: benefit, ______, risk,
   reversal ______, ______ impact.
2. Five audiences: exec, engineering, ______,
   ______, product.
3. Never promise ______ accuracy or ______ risk.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A team pitches an agent that "eliminates all
review work and never makes a mistake."
Name the two promises the exam marks as
distractors, and write the honest version
of each with its number.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D6.2 tests five-field trade-offs, audience adaptation, quantified options, no unsupported promises | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D6.2 | Sept 2026 |
| Toy arithmetic: $240k vs $48k per month, 400 misroutes, 33.3 human hours | Original toy, computed above | This lesson | Oct 6, 2026 |

:::takeaway
Price every option on the five fields. Adapt the message to
the audience. State the uncertainty. Any option that promises
perfection is the distractor.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | One audience hears it all | 99% to execs, $80k unheard | Priced choice per audience | d62-f01 | SVG | Original |
| u02 | Requirements and safety carry over | -- | Prerequisite table | d62-f02 | Table | V2-D6.1, §7.2 |
| u03 | Five fields, five audiences | Slogan for all | Priced fields per audience | d62-f03 | SVG | Original |
| u04 | The promise price check | "perfect" unpriced | 99% on eval, 100/day errors | d62-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B fits budget, honest | d62-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d62-f06 | Table | S03, S04 |
| u07 | The repriced trade-off | Static fields | Dated, recomputed fields | d62-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d62-f08 | Table | Original |
| u09 | Constraints decide the message | -- | Constraint verdict table | d62-f09 | Table | Original |
| u10 | One message valid but inferior | -- | Validity vs inferiority table | d62-f10 | Table | Original |
| u11 | Two-person team favors one message | -- | Counterfactual table | d62-f11 | Table | Original |
| u12 | Five fields from memory | Blank recall card | Filled from memory | d62-f12 | ASCII | Original |
| u13 | Transfer to agent pitch | Unseen question | Key in Stage 8 | d62-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d62-f14 | Table | Mixed |
