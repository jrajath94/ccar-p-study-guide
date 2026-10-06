# Lesson 7-3A: LLM foundations

## 1. Problem this lesson solves

Teams treat the model as a database that returns facts, or as a calculator
that computes. It is neither. It samples the next token from learned
patterns. Designs built on the database model skip verification. Designs
built on the calculator model trust arithmetic the model never did.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Two wrong machines</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Database and calculator both promise certainty. The model promises neither.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="120" height="48" rx="8" fill="#E7F1F8"/>
<text x="104" y="173" font-size="13" text-anchor="middle" fill="#1B2838">database</text>
<rect x="176" y="144" width="120" height="48" rx="8" fill="#E7F1F8"/>
<text x="236" y="173" font-size="13" text-anchor="middle" fill="#1B2838">calculator</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Returns facts. Computes sums.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">No verification designed in.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="999" fill="#E7F4EF"/>
<text x="548" y="173" font-size="13" text-anchor="middle" fill="#1B2838">next-token sampler</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Predicts. Samples. Never verifies.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Verification lives outside.</text>
<defs><marker id="m73a1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m73a1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">replace the machine</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Pick the right machine and the design follows: verify outside the model.</text>
</svg>
<figcaption>Shell 3. The database and calculator models become one sampler. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A: the threshold habit. Quality claims about model output need
the same chain: metric, threshold, owner.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 chain | "Accurate" becomes precision at least 95% on a holdout set |

## 3. Mental model

The model is autocomplete with a universe of text. It predicts the most
likely next token, then the next. It does not look up facts. It does not
run code. Two identical prompts can give two different answers because
sampling is random by design.

<figure class="fig">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="380" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Database out, sampler in</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The same question can yield two answers. That is the design, not a bug.</text>
<rect x="24" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">question</text>
<rect x="44" y="200" width="256" height="56" rx="8" fill="#E7F1F8"/>
<text x="172" y="224" font-size="14" text-anchor="middle" fill="#1B2838">"database"</text>
<text x="172" y="244" font-size="13" text-anchor="middle" fill="#5C6B7A">one true answer, always</text>
<rect x="400" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">question</text>
<rect x="420" y="200" width="120" height="56" rx="8" fill="#E7F4EF"/>
<text x="480" y="224" font-size="13" text-anchor="middle" fill="#1B2838">answer A</text>
<text x="480" y="242" font-size="13" text-anchor="middle" fill="#5C6B7A">run 1</text>
<rect x="556" y="200" width="120" height="56" rx="8" fill="#E7F4EF"/>
<text x="616" y="224" font-size="13" text-anchor="middle" fill="#1B2838">answer B</text>
<text x="616" y="242" font-size="13" text-anchor="middle" fill="#5C6B7A">run 2</text>
<defs><marker id="m73a3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="194" x2="384" y2="194" stroke="#1B2838" stroke-width="2" marker-end="url(#m73a3)"/>
<text x="360" y="178" font-size="13" text-anchor="middle" fill="#1B2838">replace with sampling</text>
<text x="24" y="332" font-size="15" fill="#1B2838">Sampling explains different answers, hallucinations, and why verification sits outside.</text>
</svg>
<figcaption>Shell 3. The database model becomes a sampling model. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Text becomes tokens. Tokens become probabilities for the next token.
Sampling picks one. The pick joins the context. The loop repeats.
Uncertainty enters at the sampling step and never leaves.

Hallucination is fluent text with no check behind it. The model did not
lie. It never verified.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Where randomness enters</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Open the loop. Randomness has one address: the sampling step.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="112" height="48" rx="999" fill="#E6E2DA"/>
<text x="100" y="177" font-size="14" text-anchor="middle" fill="#1B2838">prompt</text>
<rect x="188" y="148" width="112" height="48" rx="8" fill="#E7F1F8"/>
<text x="244" y="177" font-size="14" text-anchor="middle" fill="#1B2838">"magic"</text>
<text x="44" y="232" font-size="14" fill="#5C6B7A">No named steps.</text>
<text x="44" y="256" font-size="14" fill="#5C6B7A">No address for error.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="412" y="148" width="88" height="40" rx="999" fill="#E6E2DA"/>
<text x="456" y="173" font-size="13" text-anchor="middle" fill="#1B2838">tokens</text>
<rect x="508" y="148" width="88" height="40" rx="999" fill="#E6E2DA"/>
<text x="552" y="173" font-size="13" text-anchor="middle" fill="#1B2838">probs</text>
<rect x="604" y="148" width="80" height="40" rx="999" fill="#F4E6D4"/>
<text x="644" y="173" font-size="13" text-anchor="middle" fill="#1B2838">sample</text>
<rect x="412" y="204" width="184" height="40" rx="999" fill="#E6E2DA"/>
<text x="504" y="229" font-size="13" text-anchor="middle" fill="#1B2838">text, loop repeats</text>
<text x="412" y="268" font-size="13" fill="#C46B2C">Randomness enters here.</text>
<defs><marker id="m73a4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m73a4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">open the loop</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Fix the step you can see. Verification lives outside the loop, in code.</text>
</svg>
<figcaption>Shell 4. The loop opens and randomness gets one address. Source: original toy.</figcaption>
</figure>

:::takeaway
The model predicts the next token. It does not verify. Every fact the
business depends on gets a check outside the model, in deterministic code.
:::

## 5. Minimal worked example

Toy: summarize a 10,000-token contract. Cap the output at 500 tokens.
Words are roughly tokens times 0.75, so about 7,500 words. That ratio is
a rough industry rule, not a source value.

Cost on the Balanced tier (claude-sonnet-5-5, $2 in and $10 out per 1M
tokens, secondary sources S10-S12, Oct 2026): input 10,000 / 1,000,000 x
$2 = $0.02. Output 500 / 1,000,000 x $10 = $0.005. Total $0.025 per
contract. Scale: 1,000 contracts per day x $0.025 = $25 per day, times 30
= $750 per month.

Context check: a 1M-token window holds 1,000,000 / 10,000 = 100 such
contracts in one call. The 128K output cap covers the 500 tokens needed.
It fits, but stuffing 100 contracts in one call dilutes focus.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Count tokens before the bill</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Balanced tier, $2 in / $10 out per 1M tokens. Full arithmetic shown.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">$750 / month surprise</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">No token math.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">No per-contract cost.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">No scale check.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">$0.025 / contract</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">in: 10,000/1M x $2 = $0.02</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">out: 500/1M x $10 = $0.005</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">1,000 x $0.025 x 30 = $750</text>
<defs><marker id="m73a5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m73a5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">count tokens first</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The same $750 hurts less when the arithmetic predicted it.</text>
</svg>
<figcaption>Shell 4. Token arithmetic turns the bill into a plan. Source: original toy.</figcaption>
</figure>

### The 10-step best-answer method in action

Note: the canonical §17 text was not in this builder's context. The steps
below reconstruct the standard exam method. The coordinator should align
them with §17.

Mini question: "A law firm summarizes 1,000 contracts per day. A wrong
date in a summary can void a filing. Which design fits? A) Trust the model
with monthly spot-checks. B) Model summary plus a citation check against the
source text. C) Fine-tune on 10,000 past summaries, then spot-check."

| Step | Action on this question |
|---|---|
| 1. Read the stem once | Type: design choice under consequence |
| 2. Mark the hard constraints | Wrong date voids a filing. 1,000 per day |
| 3. Predict before reading options | Every output needs a check outside the model |
| 4. Read every option | Do not stop at the first plausible one |
| 5. Delete constraint breakers | A breaks the error-cost constraint: monthly checks miss daily damage |
| 6. Delete different-problem solvers | C solves style, not factuality |
| 7. Compare survivors on cost, risk, reversibility | B checks every output. C still trusts every output |
| 8. Hunt the traps | "Fine-tune" sounds like it fixes facts. It tunes style, not truth |
| 9. Match the decisive constraint | B is the only option with per-output verification |
| 10. Stress-test the pick | B survives production: the citation check is deterministic code |

Verdict: B. The decisive constraint is the voided filing, and only B
checks every output against the source.

## 6. Product and protocol mapping

Key separation from the prereq graph: a mechanism is how models work. A
feature is what one product exposes. The exam tests mechanisms. Products
change.

| Mechanism or feature | Product surface, Oct 6, 2026 | Exam use |
|---|---|---|
| Context window (mechanism) | Haiku 4.5: 200K in, 64K out. Sonnet, Opus, Fable: 1M in, 128K out | V2-D2.4 window management, V2-D2.1 tier choice |
| Structured outputs (feature) | API output contract | V2-D2.3 structural enforcement |
| Tool calling (mechanism) | Model requests a tool. Code runs it | V2-D3.7 integration |
| Prompt caching (feature) | Prefix cache with TTL | V2-D2.5 cost control |

Window and price facts are current product behavior from secondary sources
(S10-S12). Do not present them as exam scope. The exam tests tier-level
trade-off judgment, not memorized model IDs.

## 7. Current limitations

Hallucination has no complete fix. Long contexts dilute attention: content
in the middle gets lost more often. Prices and windows change. The Oct 2026
matrix is a snapshot, not a constant. Fine-tuning adjusts style and format.
It does not install new facts reliably.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Fits is not the same as works</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One hundred contracts fit the window. Focus does not scale with fit.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">100 contracts, one call</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">1M / 10,000 = 100. It fits.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Key clause sits at #50.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">clause #50 missed</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Middle content gets lost.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Trade-off, not a measured rate.</text>
<defs><marker id="m73a7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m73a7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">attention dilutes</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Window size is capacity. Retrieval is focus. The exam tests the difference.</text>
</svg>
<figcaption>Shell 3. A full window does not guarantee full attention. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Fine-tune a model | Train on examples | Stable task, fixed labels, style consistency at scale |
| Rules engine, no model | Code decides | Deterministic mapping, zero tolerance for surprise |
| Retrieval plus model (this lesson) | Model reads fresh documents | Changing knowledge, need citations |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Facts change monthly | Retrieval beats fine-tuning |
| Every output needs proof | Citation check outside the model |
| Wrong answer costs money or safety | Verification is mandatory, not optional |
| Closed task, fixed labels | Fine-tune or rules can win |

## 10. Valid-but-inferior option

Stuff everything into one giant prompt. Valid: it works, and short-term it
is simple. Inferior: cost grows with every token on every call, and focus
dilutes. Toy: 100 contracts at 10,000 tokens = 1M input tokens per call,
which is $2 per call on the Balanced tier. Ten calls per day = $20 per day.
Retrieval sends 3 chunks of 500 tokens = 1,500 tokens, which is 1,500 /
1,000,000 x $2 = $0.003 per query.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Giant prompt | Works today, no pipeline to build | $2 per call vs $0.003 per retrieval query |

## 11. Counterfactual where the alternative wins

Closed world: 50 fixed support macros, text never changes, answers must
match word for word. Retrieval adds moving parts for no gain. A fine-tuned
classifier, or even keyword rules, wins on cost and determinism.

| Situation | Winner | Why |
|---|---|---|
| 50 fixed macros, frozen text | Fine-tune or rules | Retrieval machinery exceeds the need |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The model predicts the next ______.
2. Randomness enters at the ______ step.
3. Hallucination means text with no ______ behind it.
4. One contract summary costs $______ on the toy math.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A clinic summarizes visit notes into dosage instructions.
A wrong dose harms a patient.
List everything that must sit OUTSIDE the model.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Tier windows and prices | Current product behavior, secondary | S10, S11, S12 | Oct 1, ~Sep 25, ~Sep 29, 2026 |
| Token to word ratio 0.75 | General principle, rough rule | Industry practice | Long-standing |
| Sampling and hallucination mechanism | General principle | ML canon | Long-standing |
| Cost arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Exam tests tier trade-offs, not model IDs | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

:::takeaway
Tier reasoning beats model memorization. The exam tests trade-off
judgment: cost, latency, capability. The Oct 2026 matrix is enrichment,
not scope.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Model is a sampler, not a database | Database mental model | Sampler mental model | f01 | SVG | Original |
| u02 | Threshold habit carries over | -- | Prerequisite table | f02 | Table | §7.4 |
| u03 | Autocomplete with a universe of text | One true answer | Two runs, two answers | f03 | SVG | Original |
| u04 | Randomness has one address | "Magic" box | Tokens, probs, sample, text | f04 | SVG | Original |
| u05 | Token arithmetic predicts the bill | $750 surprise | $0.025 per contract | f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches voided-filing risk | f05b | Table | Original |
| u06 | Mechanism vs feature separation | -- | Mapping table | f06 | Table | S10-S12 |
| u07 | Fit is not focus | 100 contracts fit | Clause 50 missed | f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide the design | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Giant prompt is valid but inferior | -- | Cost comparison table | f10 | Table | Original |
| u11 | Frozen macros favor fine-tune | -- | Counterfactual table | f11 | Table | Original |
| u12 | Sampler facts from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to dosage instructions | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
