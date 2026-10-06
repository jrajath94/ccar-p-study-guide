# Comparisons 04: verification and evaluation

Five high-confusion pairs from §18. Tight matrices. Prior-stage concepts appear by name only.

:::takeaway
A check that cannot fail is not a check. Every verification here must name what fails it.
:::

## Pair 17: schema validity vs factual correctness

Shared: both validate model output. Both live under V2-D2.2 and V2-D4.1. Both belong in the pipeline before the output ships.

Decisive difference: schema validity checks shape: fields present, types right, enum values legal. Factual correctness checks content: the values are true against a source. A valid schema can carry a lie.

| Dimension | Schema validity | Factual correctness |
|---|---|---|
| Checks | Shape of the output | Truth of the values |
| Mechanism | Deterministic code | Grounding check against a source |
| Cost | Microseconds | A retrieval or lookup per claim |
| Fails on | Malformed JSON | Invented invoice total |
| Best fit | Every structured output | Every fact the business depends on |

Winning constraints: this pair is not either-or. Schema validation is mandatory for every structured output (V2-D2.2: schema validation in code, not hope in the prompt). Factual checks are mandatory for every consequential claim (Lesson 7-3A: every fact gets a check outside the model).

Losing constraints: schema-only validation loses when the numbers matter: valid JSON with an invented total ships the error in a pretty envelope. Fact-checking without schema loses when downstream code parses the output: a true claim in broken JSON crashes the consumer.

Costs: schema checks are nearly free. Fact checks cost a lookup per claim. Check the claims that carry error cost, not every adjective.

Security: schema validation is also an injection control: strict enums and length caps bound what injected content can smuggle through. Fact checks need trusted sources: checking against the same poisoned document proves nothing.

Operational burden: schemas need versioning with the output contract. Fact checks need the source of truth named and monitored for drift.

Counterexample: an internal draft summary for a human editor. Schema matters little. The human is the fact check. Both automated checks can stay light.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Output contract plus code enforcement | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Model never verifies | General principle | Lesson 7-3A | Long-standing |

Minimal pairs:

- MP1. Base: invoice extraction to JSON. Winner: both, schema in code plus total checked against the source image. Change: the output becomes a free-text draft for a human. Schema drops out. The human parses prose, not JSON.
- MP2. Base: schema-validated output, totals unchecked, one invented total ships. The postmortem adds the factual check. The layer that failed was content, not shape.
- MP3. Base: every claim fact-checked against a source, output schema loose. Change: a downstream service starts parsing the output. Schema validation becomes mandatory. The consumer changed the contract.

## Pair 18: citation presence vs citation support

Shared: both involve citations in answers. Both live under V2-D3.5. Both matter when answers need citations (V2-D3.5 decisive constraint).

Decisive difference: citation presence means the answer carries a reference marker. Citation support means the referenced text actually backs the claim. Presence is a format choice. Support is verification.

| Dimension | Citation presence | Citation support |
|---|---|---|
| What it proves | The answer looks sourced | The claim matches the source |
| Check | Marker exists | Entailment: source implies claim |
| Failure mode | Decorative citations | Quote mined out of context |
| Cost | Free: the model adds markers | A check per cited claim |
| Best fit | Never alone | Every cited answer |

Winning constraints: support wins always. Presence alone never wins: it is the check that cannot fail, and the model is fluent at producing it.

Losing constraints: support checks lose on cost when applied to every trivial claim. Scope them to consequential claims. Presence loses everywhere as a quality signal.

Costs: on the toy: 100 cited answers per day. Presence check: free, catches 0 of 40 unsupported claims. Support check: one entailment check per claim, catches the 40. The 40 blocked claims are the whole value.

Security: decorative citations are a trust attack surface. A user who sees citations assumes verification. Unsupported citations manufacture false confidence, which is worse than no citations.

Operational burden: support needs the grounding stage in the RAG pipeline (V2-D3.5: ingestion through grounding and citation checks). It needs a cited-span store so the checker can re-read the source.

Counterexample: a brainstorming draft with explicitly marked "unverified ideas." Citations would imply a rigor the document disclaims. Neither check applies until the draft hardens.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Grounding and citation checks in the pipeline | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Markers are not proof</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">100 cited answers. 40 citations do not support their claims.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: PRESENCE CHECK</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F6E7A8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">100 pass, 0 blocked</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Marker exists on all 100.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">40 unsupported claims ship.</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">The check cannot fail.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: SUPPORT CHECK</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">60 pass, 40 blocked</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">Source must imply the claim.</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">40 claims fail and route to fix.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">The check has teeth.</text>
<defs><marker id="mc4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mc4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">check entailment</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Presence checks formatting. Support checks truth. Only one blocks errors.</text>
</svg>
<figcaption>Shell 4. An entailment check moves 40 unsupported claims from shipped to blocked. Source: original toy.</figcaption>
</figure>

Minimal pairs:

- MP1. Base: policy answers with citation markers, no support check. A wrong answer cites a real page that says the opposite. Winner flips to support checks. The incident names the missing layer.
- MP2. Base: support checks on every cited claim, costs high. Change: the answers become low-stakes internal drafts. Winner flips to presence plus sampled support checks. The stakes no longer pay for full verification.
- MP3. Base: support check passes against the retrieved chunk. Change: the chunk itself is later found poisoned. The check was correct and the source was wrong. The fix moves upstream to ingestion screening (V2-D5.2).

## Pair 19: confidence vs calibrated risk

Shared: both quantify uncertainty. Both inform the V2-D5.3 review decision. Both need the metric-threshold-owner chain from Lesson 7-4A.

Decisive difference: confidence is the model's self-reported certainty, often uncalibrated. Calibrated risk is a measured probability tied to outcomes: when the system says 90%, it is right 90% of the time on a labeled set.

| Dimension | Model confidence | Calibrated risk |
|---|---|---|
| Source | The model's own words | Measurement on labeled data |
| Calibration | Usually overconfident | Tested: predicted vs actual |
| Drives | A feeling | The review threshold |
| Failure mode | Fluent certainty, wrong answer | Stale calibration after drift |
| Best fit | Never as a control | Gating and routing decisions |

Winning constraints: calibrated risk wins wherever a threshold drives action: route to human review, escalate the model, or block the answer. Confidence alone never wins as a control.

Losing constraints: calibration loses when no labeled data exists: unmeasured risk is a guess with a number on it. Confidence loses everywhere it is used as a gate: the model does not know what it does not know.

Costs: calibration costs the labeled set and the recalibration cadence. Using raw confidence costs nothing and buys nothing: it is a number without a contract.

Security: an attacker can prompt the model to state high confidence. Confidence as a control is prompt-injectable. Calibrated risk lives in code and measurement, outside the model's reach.

Operational burden: calibration needs the eval set from V2-D4.2, a recalibration trigger on drift (V2-D4.6), and an owner. Confidence needs nothing, which is exactly its danger.

Counterexample: a creative writing assistant. No threshold, no gate, no stakes. Neither measure matters. The user is the judge.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Review strength keyed to uncertainty | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

Minimal pairs:

- MP1. Base: triage bot routes "low confidence" answers to humans. The model marks 95% of answers high confidence and errors persist. Winner flips to calibrated risk thresholds from a labeled set. The gate needs measurement, not self-report.
- MP2. Base: calibrated risk gates review at a measured 90% precision line. Change: the data drifts and the calibration goes stale. The fix is recalibration, not gate removal. The mechanism is right. The measurement aged.
- MP3. Base: no labeled data, new domain. Winner: neither as a gate. Ship with human review on consequential actions and build the labeled set. Calibration without labels is fiction.

## Pair 20: human review vs deterministic validation

Shared: both verify output before it ships. Both live under V2-D5.1 and V2-D5.3. Both need to name what they catch.

Decisive difference: human review applies judgment to open-ended quality. Deterministic validation applies code to checkable rules. Judgment catches what rules cannot name. Rules catch what humans miss at scale.

| Dimension | Human review | Deterministic validation |
|---|---|---|
| Catches | Nuance, tone, novel errors | Format, ranges, known bad patterns |
| Scales | Linearly with reviewer hours | Near zero marginal cost |
| Consistency | Varies by reviewer and hour | Identical every run |
| Failure mode | Fatigue, rubber stamp | Rule gap: unlisted error passes |
| Best fit | Open quality, high stakes | Checkable invariants |

Winning constraints: human review wins on open-ended quality with real stakes. Deterministic validation wins on checkable invariants at any volume. Most production systems need both: rules first, humans on what rules cannot check.

Losing constraints: human review loses at high volume: the rubber stamp arrives and the gate becomes theater. Deterministic validation loses on novel errors: the rule list never names the new failure.

Costs: human review costs reviewer time per item. Deterministic checks cost build time once. On the V2-D5.3 toy: review everything fits tiny volume with extreme stakes. Sampled review fits high volume with low stakes.

Security: reviewers need real decision context: the exact action and its consequences. Rules need fail-closed defaults: a rule that cannot decide must block, not pass (V2-D5.1).

Operational burden: human review needs reviewer training, calibration, and a queue. Deterministic validation needs the rule set owned and the gap list reviewed: every incident that passed the rules adds a rule or a documented exception.

Counterexample: a deterministic format check on a creative story. The rules cannot name quality. Human review is the only check that means anything.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Stakes-keyed review shapes | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Controls must fail closed | General principle | V2-D5.1 | Long-standing |

Minimal pairs:

- MP1. Base: refund agent, humans review every payout, volume 200 per day. Change: volume grows to 20,000 per day. Winner flips to deterministic rules for the checkable cases plus sampled human review. The human gate cannot scale.
- MP2. Base: deterministic rules validate all outputs. A novel fraud pattern passes every rule for a month. Winner flips to add human review on the flagged class. The rule gap needed judgment.
- MP3. Base: human review on loan decisions with per-group fairness floors (V2-D5.5). Change: the fairness check becomes a computed metric with a threshold. The fairness gate flips to deterministic validation. The rule is now checkable, but human review stays for the open-ended credit narrative.

## Pair 21: offline evaluation vs A/B testing

Shared: both measure change quality. Both live under V2-D4.2 and V2-D4.3. Both need a primary metric first.

Decisive difference: offline evaluation grades a fixed dataset with no users exposed. A/B testing exposes a sample of real users to the change and measures the outcome. One is safe and static. The other is real and risky.

| Dimension | Offline evaluation | A/B testing |
|---|---|---|
| Users exposed | None | A controlled sample |
| Measures | Dataset score | Business outcome |
| Risk | Zero user harm | Real exposure, needs a guard |
| Blind spot | Dataset drift from reality | Needs traffic and time |
| Best fit | Every change, before ship | Production changes with measurable goals |

Winning constraints: offline evaluation wins as the gate before any ship: the regression drawer runs on every change (V2-D4.2). A/B testing wins when the question is the business outcome: only real users answer it.

Losing constraints: offline-only loses when the dataset goes stale: green suite, live slides (V2-D4.6). A/B loses when traffic is too small for the claimed lift: the test cannot answer, so do not test (V2-D4.3).

Costs: offline costs the dataset and grading. A/B costs experiment time and the risk budget. A falsifiable hypothesis with a primary metric keeps both honest.

Security: A/B assignment must be consistent per user: flip-flopping exposure corrupts the measurement and the user experience. Offline sets with PII need stripping before the cases leave the trust boundary (V2-D4.2).

Operational burden: offline needs the five drawers (representative, edge, adversarial, malformed, regression) plus the grading ladder: code, then judge, then human, with judges calibrated against human labels. A/B needs the hypothesis, consistent assignment, sample size, and the shadow-first rule for risky changes.

Counterexample: a prompt wording tweak with no behavior change and no measurable goal. Neither applies. Ship it with the regression suite green and move on.

Evidence:

| Claim | Class | Source | Date |
|---|---|---|---|
| Five drawers, grading ladder, judge calibration | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |
| Shadow first for risky changes | General principle | V2-D4.3 | Long-standing |

Minimal pairs:

- MP1. Base: new reranker, offline suite green. Winner: ship after the gate. Change: the goal is revenue per session, not rank quality. Winner flips to add an A/B test. The dataset cannot measure the business outcome.
- MP2. Base: A/B test planned for a 1% lift claim on 500 sessions per day. Winner flips to offline evaluation only. The traffic cannot answer the claim, so the test is theater.
- MP3. Base: A/B test on a risky auto-refund change. Change: the change can harm users directly. Winner flips to shadow first, then controlled exposure. The risk demands the safer lane before the real one.

:::takeaway
Verify shape in code, truth against sources, risk by measurement, quality by the right judge, and business impact on real users. Each check has one job.
:::
