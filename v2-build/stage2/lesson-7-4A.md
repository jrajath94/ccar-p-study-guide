# Lesson 7-4A: architecture and business foundations

## 1. Problem this lesson solves

A stakeholder says "make it fast and accurate." The team nods. Three
engineers build three different things. None matches what the stakeholder
meant. The work gets redone.

Vague requirements are the most expensive bug in a project. They pass every
review because no one can prove them wrong. They detonate at handoff, when
guesses meet reality.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Vague words split the build</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One adjective. Three builders. Three different products.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">"fast and accurate"</text>
<rect x="48" y="196" width="72" height="56" rx="8" fill="#F3D4D8"/>
<text x="84" y="220" font-size="13" text-anchor="middle" fill="#1B2838">Build A</text>
<text x="84" y="238" font-size="13" text-anchor="middle" fill="#1B2838">1 s, sloppy</text>
<rect x="136" y="196" width="72" height="56" rx="8" fill="#F3D4D8"/>
<text x="172" y="220" font-size="13" text-anchor="middle" fill="#1B2838">Build B</text>
<text x="172" y="238" font-size="13" text-anchor="middle" fill="#1B2838">9 s, careful</text>
<rect x="224" y="196" width="72" height="56" rx="8" fill="#F3D4D8"/>
<text x="260" y="220" font-size="13" text-anchor="middle" fill="#1B2838">Build C</text>
<text x="260" y="238" font-size="13" text-anchor="middle" fill="#1B2838">5 s, medium</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="999" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">p95 at most 5 s, precision at least 95%</text>
<rect x="420" y="196" width="256" height="56" rx="8" fill="#E7F4EF"/>
<text x="548" y="220" font-size="13" text-anchor="middle" fill="#1B2838">One contract</text>
<text x="548" y="238" font-size="13" text-anchor="middle" fill="#1B2838">One build matches it</text>
<defs><marker id="m74a1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m74a1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">write the chain</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Adjectives permit three builds. Numbers permit one.</text>
</svg>
<figcaption>Shell 3. Vague adjectives become one numbered contract. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

None. This lesson opens the crash course. Later lessons reuse its chain.

| Foundation | What it gives the rest of the course |
|---|---|
| §7.4 chain | Every quality adjective becomes a metric, a threshold, and an owner |

## 3. Mental model

Think of a requirement as a contract, not a wish. A contract names the thing
to measure, the line it must cross, and the person who signs off. Four links:
requirement, metric, threshold, owner.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The four-link chain</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each adjective grows three links. The chain is the requirement.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="999" fill="#E6E2DA"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">"accurate triage"</text>
<text x="44" y="224" font-size="14" fill="#5C6B7A">No metric. No line. No owner.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="120" height="40" rx="999" fill="#E7F4EF"/>
<text x="480" y="169" font-size="13" text-anchor="middle" fill="#1B2838">requirement</text>
<rect x="420" y="192" width="120" height="40" rx="999" fill="#E7F1F8"/>
<text x="480" y="217" font-size="13" text-anchor="middle" fill="#1B2838">precision</text>
<rect x="556" y="144" width="120" height="40" rx="999" fill="#F6E7A8"/>
<text x="616" y="169" font-size="13" text-anchor="middle" fill="#1B2838">at least 95%</text>
<rect x="556" y="192" width="120" height="40" rx="999" fill="#F4E6D4"/>
<text x="616" y="217" font-size="13" text-anchor="middle" fill="#1B2838">support lead</text>
<defs><marker id="m74a3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m74a3)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">attach the chain</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Requirement, metric, threshold, owner. Miss one link and the chain holds nothing.</text>
</svg>
<figcaption>Shell 4. The adjective gains metric, threshold, and owner. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Ambiguity flows downhill. A vague requirement enters design. Each team
interprets it alone. Interpretations differ. Builds diverge. Integration
exposes the gap. Rework follows. One unclear adjective becomes three designs
and two rebuilds.

<figure class="fig">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="380" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">How vagueness multiplies</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each handoff copies the ambiguity. The count of wrong builds grows.</text>
<rect x="24" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="200" height="40" rx="999" fill="#E6E2DA"/>
<text x="144" y="169" font-size="14" text-anchor="middle" fill="#1B2838">1 vague requirement</text>
<rect x="44" y="200" width="80" height="56" rx="8" fill="#F3D4D8"/>
<text x="84" y="224" font-size="13" text-anchor="middle" fill="#1B2838">team 1</text>
<text x="84" y="242" font-size="13" text-anchor="middle" fill="#1B2838">guesses</text>
<rect x="136" y="200" width="80" height="56" rx="8" fill="#F3D4D8"/>
<text x="176" y="224" font-size="13" text-anchor="middle" fill="#1B2838">team 2</text>
<text x="176" y="242" font-size="13" text-anchor="middle" fill="#1B2838">guesses</text>
<rect x="228" y="200" width="80" height="56" rx="8" fill="#F3D4D8"/>
<text x="268" y="224" font-size="13" text-anchor="middle" fill="#1B2838">team 3</text>
<text x="268" y="242" font-size="13" text-anchor="middle" fill="#1B2838">guesses</text>
<rect x="400" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">3 interpretations, 1 correct</text>
<rect x="420" y="200" width="256" height="56" rx="8" fill="#F3D4D8"/>
<text x="548" y="224" font-size="14" text-anchor="middle" fill="#1B2838">3 - 1 = 2 rebuilds</text>
<text x="548" y="244" font-size="13" text-anchor="middle" fill="#5C6B7A">count from the toy</text>
<defs><marker id="m74a4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="194" x2="384" y2="194" stroke="#1B2838" stroke-width="2" marker-end="url(#m74a4)"/>
<text x="360" y="178" font-size="13" text-anchor="middle" fill="#1B2838">interpret alone</text>
<text x="24" y="332" font-size="15" fill="#1B2838">Vagueness does not stay put. It copies itself at every handoff.</text>
</svg>
<figcaption>Shell 3. Separate interpretation turns one vague requirement into two rebuilds. Source: original toy.</figcaption>
</figure>

:::takeaway
Every adjective in a requirement needs a number, a threshold, and an owner.
Write the chain before the build, not after the rework.
:::

## 5. Minimal worked example

Toy: ticket triage. "Triage must be fast and accurate."

The chain: requirement "every ticket reaches the right queue." Metric
"precision on a 500-ticket holdout." Threshold "at least 95%." Owner
"support lead." Fast: metric "p95 classification latency." Threshold "at
most 5 seconds."

Cost math (toy assumptions, stated): manual triage costs 100 tickets per
week times 10 minutes = 1,000 minutes = 16.7 hours, times $30 per hour =
$500 per week. Automated triage costs $0.01 per ticket times 100 = $1 per
week, plus human review of the 20% flagged = 20 tickets times 5 minutes =
100 minutes = 1.7 hours times $30 = $50 per week. Total $51 per week.
Savings: $500 - $51 = $449 per week, times 52 = $23,348 per year.

<figure class="fig">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="380" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The chain prices the decision</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Manual triage vs triage with thresholds. Toy assumptions, full arithmetic.</text>
<rect x="24" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">manual: $500 / week</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">100 x 10 min = 1,000 min</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">1,000 / 60 = 16.7 h</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">16.7 x $30 = $500</text>
<rect x="400" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">with chain: $51 / week</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">$1 API + $50 review = $51</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">$500 - $51 = $449 saved / week</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">$449 x 52 = $23,348 / year</text>
<defs><marker id="m74a5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="194" x2="384" y2="194" stroke="#1B2838" stroke-width="2" marker-end="url(#m74a5)"/>
<text x="360" y="178" font-size="13" text-anchor="middle" fill="#1B2838">automate to thresholds</text>
<text x="24" y="332" font-size="15" fill="#1B2838">The threshold decides what to automate and what a human still reviews.</text>
</svg>
<figcaption>Shell 4. Thresholds turn the triage cost into arithmetic. Source: original toy.</figcaption>
</figure>

### The 10-step best-answer method in action

The canonical 10-step best-answer method, applied to this question:

Mini question: "A 200-person support org wants ticket triage. Wrong routing
delays refunds, so error cost is high. Budget is fixed. Which approach fits?
A) Build on adjectives, tune later. B) Write the requirement, metric,
threshold, and owner chain, then build. C) Ship a prototype with no
thresholds, then set them from its behavior."

| Step | Action on this question |
|---|---|
| 1. Question type | Best architecture under constraints |
| 2. Lifecycle stage | Design |
| 3. Objective | Route tickets with bounded error cost inside a fixed budget |
| 4. Hard constraints | Wrong routing delays refunds. Budget is fixed |
| 5. System layer | Requirements and acceptance, not the model |
| 6. Infeasible options | None: all three could run |
| 7. Constraint violators | A sets no bar on error cost. C sets thresholds after damage |
| 8. Compare survivors | Only B remains |
| 9. Hidden consequences | C lets real refund damage happen before it measures. A tunes with no stop rule |
| 10. Verify | B is the complete single answer |

Verdict: B. The decisive constraint is error cost, and only B puts a

Do not assume the exam always wants more autonomy, a larger model, more tools, more logging, a human reviewer everywhere, a new framework, or a complete redesign. Sometimes the best answer is: clarify the requirement, remove an unnecessary capability, fix retrieval, add a deterministic validation gate, narrow permissions, or preserve an existing sufficient workflow. The scenario, not a slogan, determines the answer.
number on it before the build.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| SLO | Service contract, SRE practice | V2-D1.6 latency and reliability targets, V2-D3.3 tuning to SLAs |
| ADR | Architecture decision record | V2-D6.4 documentation that a successor can run |
| Acceptance threshold | Evaluation plan | V2-D4.1 turning vague goals into metric thresholds |
| Owner | Team charter, RACI | V2-D6.1 discovery, V2-D5.3 review ownership |

## 7. Current limitations

A number on paper can miss the goal. The metric can be green while users
suffer. Thresholds expire when volume doubles. Owners leave and no one
re-signs the contract.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Green metric, missed goal</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The number holds. The world moves. The chain needs a review date.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">precision 96% at least 95%</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Metric green. Users quiet.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Goal met, for now.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">precision 96% at least 95%</text>
<text x="420" y="220" font-size="14" fill="#1F7A72">Metric still green.</text>
<text x="420" y="244" font-size="14" fill="#C46B2C">New ticket types arrive. Users complain.</text>
<defs><marker id="m74a7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m74a7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">goal shifts</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A threshold is a snapshot. Date it, and re-sign it when the world moves.</text>
</svg>
<figcaption>Shell 3. A stale threshold stays green while the goal moves. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Build first, measure later | Prototype with no thresholds | One-person spike, reversible demo |
| Adjectives plus sign-off | Stakeholder approves words, not numbers | Tiny team, shared context, low stakes |
| Full chain (this lesson) | Numbers before the build | Handoffs, high error cost, fixed budget |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Error cost high or irreversible | Use the chain |
| Two or more teams hand off | Use the chain |
| Trade-offs collide (latency vs accuracy) | Use the chain. Numbers settle the fight |
| Reversible demo, one builder | Skip the chain. Adjectives suffice |

## 10. Valid-but-inferior option

Build first, measure later. Valid: prototypes teach fast. Inferior here:
measurement starts after wrong routing already cost refunds. On the toy,
one week of unmeasured errors at 80% precision misroutes 20 tickets
(100 x 0.20 = 20). The dollar cost of each delayed refund: not in source.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Build first, measure later | Fast learning, no upfront debate | Errors hit customers before any bar exists |

## 11. Counterfactual where the alternative wins

Weekend hackathon. Two builders. Demo on Monday. No customers, no money
moves. The chain costs half a day of meetings. Adjectives win: "fast enough
for the demo" is the correct bar.

| Situation | Winner | Why |
|---|---|---|
| Hackathon demo, no customers | Adjectives | Chain overhead exceeds the stakes |

## 12. Recall prompt

```
Cover the answers. Say each link aloud.
1. Requirement: _________________________
2. Metric:      _________________________
3. Threshold:   _________________________
4. Owner:       _________________________
Uncover. Fix what you missed. Repeat once.
```

## 13. Unseen transfer question

```
A recruiter wants "strong communicators" on the team.
The hiring bar must survive an audit.
Write the four chain links for this requirement.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Chain maps to V2-D1.1, V2-D4.1, V2-D6.4 objectives | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Toy cost arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Numbers-before-build practice | General principle | Industry practice | Long-standing |
| Dollar cost of a delayed refund | Not in source | -- | -- |

:::takeaway
The exam tests the chain. When a stem says "fast," "accurate," or "high
quality," the right answer converts the adjective to a metric with a
threshold. Options that skip the numbers are usually the distractors.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Vague words split the build | Adjective, three builds | One numbered contract | f01 | SVG | Original |
| u02 | Chain is this lesson's foundation | -- | Foundation table | f02 | Table | Original |
| u03 | Four-link chain | Bare adjective | Requirement, metric, threshold, owner | f03 | SVG | Original |
| u04 | Vagueness multiplies at handoffs | 1 requirement, 3 guesses | 3 - 1 = 2 rebuilds | f04 | SVG | Original |
| u05 | Chain prices the triage decision | $500/week manual | $51/week with thresholds | f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches error cost | f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | f06 | Table | S03, S04 |
| u07 | Green metric can miss the goal | Metric green, goal met | Metric green, goal moved | f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide the method | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Build-first is valid but inferior | -- | Validity vs inferiority table | f10 | Table | Original |
| u11 | Adjectives win the hackathon | -- | Counterfactual table | f11 | Table | Original |
| u12 | Four links from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer: interview bar | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
