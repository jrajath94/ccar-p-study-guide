# Mixed-domain question bank: 50 original scenario questions

50 original practice questions across all seven domains, weighted to the
blueprint (D3 heaviest). IDs Q-M-01 through Q-M-50. None repeats any item
from qb-D1 through qb-D7. About a quarter are multiple-response.
Baseline: Oct 6, 2026. Scope: blueprint v1.0 via secondary summaries
(S03, S04), Sept 2026.
These are original practice items for study. They are not real exam items
and do not predict exam content.
Format per question: scenario, one best answer or a marked multi-select,
options, answer key, a compact §17 10-step method walk, and a 10-point
explanation per §19.2.
Tier names (Fast, Balanced, Capable, Most capable) are lesson toys from
stage3, priced per S10-S12 secondary sources, Oct 2026. Verify against
official docs before production use.

## Q-M-01 (V2-D1.1)

**Scenario.** A port handles 8,000 container damage claims per day. About
85% are standard: container ID, timestamp, one photo set. About 15% are
complex: multi-party liability narratives. One hard rule: no payout on an
unverified damage photo. The IT budget is fixed.

**Question.** Which design fits the scenario best?

**Options.**
A) One agent handles every claim end to end with no checks.
B) Deterministic rules validate the 85% standard claims. Claude drafts the
adjuster summary for the 15% complex claims. A code gate blocks any payout
until the damage photo check passes.
C) The most capable tier answers every claim with no checks.
D) Claude triages all claims and a human adjuster reviews every payout.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best architecture under constraints.
2. Lifecycle stage: design.
3. Objective: safe claim routing inside a fixed budget.
4. Hard constraints: no payout on an unverified photo, 8,000 claims per
day, budget fixed.
5. System layer: orchestration pattern plus verification gate.
6. Eliminate infeasible: all four are technically feasible.
7. Eliminate constraint-violating: A and C have no gate on payouts, D
needs 8,000 human reviews per day under a fixed budget.
8. Compare on objective: B forks by input shape and gates every payout in
code.
9. Hidden dependencies: the photo check needs the source photo set as
input.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "no payout on an unverified damage photo.
The IT budget is fixed."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Standard claims route cheap | No | Yes | No | No |
| Complex claims get language handling | Yes | Yes | Yes | Yes |
| Code gate on every payout | No | Yes | No | Yes |
| Fits fixed budget at 8k/day | No | Yes | No | No |

4. Why B satisfies all hard constraints: deterministic rules handle the
fixed 85% at parser cost, Claude handles the open 15%, and the code gate
enforces the no-unverified-payout rule on every claim.
5. Why B best meets the objective: V2-D1.1 maps task shape to lane (fixed
mapping goes deterministic, open input with a verifiable output goes to
Claude with a gate). B is the only option that applies the fork.
6. Every rejected choice explained: A is technically valid but violates
the payout rule (an agent with no checks on money movement). C is valid
quality-wise but violates the budget (most capable tier on every claim,
about 10x the Fast tier on the toy) and has no gate. D is valid as a
safety instinct but infeasible: 8,000 reviews per day cannot fit a fixed
budget, and triage errors stay in the system.
7. Exact limitation or tradeoff: B needs the rule set maintained as claim
forms change, and the photo check adds per-claim code.
8. Relevant evidence (with date): fork rule from lesson-D1-1 (§4), Oct 6
2026, tier pricing from S10-S12, Oct 2026, exam scope via S03/S04, Sept
2026.
9. Counterfactual where each plausible alternative wins: A wins for an
internal demo with no money movement. C wins when evals prove only the
top tier clears the quality floor. D wins at 40 claims per day where the
review labor fits the budget.
10. Misconception tested: "one agent for everything is simpler and safe."
It is neither here: no gate on payouts and no budget fit.

## Q-M-02 (V2-D1.2)

**Scenario.** A fire agency builds a detection pipeline: satellite feed to
validation to context assembly to model to verification to public alert to
feedback. The satellite feed is untrusted input. The perimeter database is
the system of record. A false public alert triggers panic evacuations.

**Question.** Where does human review sit in this pipeline?

**Options.**
A) Before validation, on the raw satellite feed.
B) After the model proposes a perimeter and before the public alert, with
the perimeter database as the check source.
C) After the public alert, as post-action review.
D) Nowhere. The model is accurate enough to skip review.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: control placement in a pipeline.
2. Lifecycle stage: design.
3. Objective: place review where it prevents the panic-evacuation harm.
4. Hard constraints: a false alert causes evacuations, the alert is
irreversible once broadcast.
5. System layer: verification stage plus trust boundaries.
6. Eliminate infeasible: all four are feasible placements.
7. Eliminate constraint-violating: A reviews raw pixels with no perimeter
to judge, C reviews after the harm, D ignores the error cost.
8. Compare on objective: B gates the irreversible action with the system
of record as context.
9. Hidden dependencies: the reviewer needs the proposed perimeter, the
satellite evidence, and the database state in one view.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "A false public alert triggers panic
evacuations."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Reviews the actual perimeter proposal | No | Yes | Yes | No |
| Acts before the irreversible alert | Yes | Yes | No | N/A |
| Reviewer sees the system of record | No | Yes | No | No |

4. Why B satisfies all hard constraints: the gate sits before the
irreversible broadcast, and the reviewer judges the proposal against the
perimeter database, the trusted source.
5. Why B best meets the objective: V2-D1.2 places verification after the
model and before the side effect, and V2-D5.3 keys review strength to
consequence and reversibility. The alert is high-consequence and
irreversible, so pre-action review with full context is the shape.
6. Every rejected choice explained: A reviews pixels before any perimeter
exists, so there is nothing to judge. C is post-action review on an
irreversible alert: the panic already happened. D treats accuracy as a
control. Accuracy is a metric, and no metric gates a side effect.
7. Exact limitation or tradeoff: B adds minutes to the alert path. The
agency must set a review SLA so the gate does not stall real fires.
8. Relevant evidence (with date): pipeline stage order from lesson-D1-2
(§4), Oct 6 2026, review strength keyed to consequence from lesson-D5-3,
Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins if the
feed itself is the attack surface (spoofed satellites) and validation
needs eyes. C wins for a low-stakes internal dashboard where the alert
is reversible. D wins never as a control, only as a cost note.
10. Misconception tested: "review anywhere counts as a control." Only
review before the irreversible action with decision context counts.

## Q-M-03 (V2-D1.3), Select TWO

**Scenario.** A ski resort publishes a daily avalanche bulletin. Inputs
are volatile: sensor data, weather models, and patrol observations that
change hourly. The bulletin format is fixed by the safety board. A wrong
bulletin risks lives.

**Question.** Which TWO patterns fit this task? Select TWO.

**Options.**
A) Augmented single call with no tools.
B) Deterministic workflow for the publish step.
C) Agentic research loop for the conditions assessment.
D) One fixed prompt with no tools and no checks.
E) Manual process with no model involvement.

**Answer.** B, C

**Method walk (Steps 1-10).**
1. Question type: pattern selection for a two-shape task.
2. Lifecycle stage: design.
3. Objective: match each sub-task to its pattern.
4. Hard constraints: volatile inputs, fixed bulletin format, life-safety
error cost.
5. System layer: architectural pattern choice (V2-D1.3).
6. Eliminate infeasible: all five are feasible to attempt.
7. Eliminate constraint-violating: A and D cannot gather volatile inputs,
E ignores the task.
8. Compare on objective: the task has two shapes: open assessment and
fixed publish. Each needs its own pattern.
9. Hidden dependencies: the loop's output must feed the workflow's fixed
schema.
10. Verify: B and C together cover both shapes. No third fits.

**Explanation.**
1. Correct answer: B, C.
2. Decisive scenario phrase: "Inputs are volatile... The bulletin format
is fixed by the safety board. A wrong bulletin risks lives."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Handles volatile inputs | No | No | Yes | No | Yes |
| Enforces the fixed format | No | Yes | No | No | Yes |
| Fits life-safety error cost | No | Yes | Partial | No | Partial |

4. Why B and C satisfy all hard constraints: the agentic loop plans the
assessment at runtime across changing sources (steps unknowable in
advance), and the deterministic workflow enforces the board's fixed
format plus a final check before publish.
5. Why B and C best meet the objective: V2-D1.3 evaluates patterns on
predictability and dynamic-planning need. Assessment scores high on
planning need (agent). Publish scores high on predictability need
(workflow). The hybrid of the two is the exam's standard answer for a
two-shape task.
6. Every rejected choice explained: A makes one judgment with no tools,
so it cannot read sensors or patrol notes. D is a prompt with no input
path and no check: a wrong bulletin ships. E is valid but answers a
different question. The scenario asks which patterns fit, and manual
process is not a pattern under test.
7. Exact limitation or tradeoff: the handoff between loop and workflow
needs a schema contract, and the loop needs a step cap so assessment
cost stays bounded.
8. Relevant evidence (with date): four-stop spectrum and seven axes from
lesson-D1-patterns (§4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when all
inputs arrive pre-assembled in one payload. D wins never for
life-safety output. E wins when the resort rejects automation entirely.
10. Misconception tested: "one pattern must win." Two-shape tasks take
two patterns, joined by a contract.

## Q-M-04 (V2-D1.4)

**Scenario.** A museum digitizes archives with three specialists: a
transcriber turns handwriting into text, a translator renders Latin into
English, and a cataloger writes metadata and the final record. The
translator and transcriber disagree on 12% of pages.

**Question.** What resolves the disagreement?

**Options.**
A) The coordinator re-runs both workers until they agree.
B) The handoff contract names the cataloger as arbiter with a documented
disagree rule. The coordinator applies it and logs the decision.
C) Majority vote across all three workers.
D) The translator wins because translation is the harder skill.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: multi-agent conflict resolution.
2. Lifecycle stage: design.
3. Objective: resolve worker disagreement deterministically.
4. Hard constraints: 12% disagreement rate, final record must be
consistent and auditable.
5. System layer: handoff contract (V2-D1.4).
6. Eliminate infeasible: all four are feasible to implement.
7. Eliminate constraint-violating: A may loop forever, C invents a rule
the contract never defined, D is arbitrary.
8. Compare on objective: only B uses the contract's disagree rule, which
V2-D1.4 requires.
9. Hidden dependencies: the arbiter needs both workers' outputs plus the
source page.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The translator and transcriber disagree on
12% of pages."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Terminates on every page | No | Yes | Yes | Yes |
| Rule defined before the dispute | No | Yes | No | No |
| Decision is logged | No | Yes | No | No |

4. Why B satisfies all hard constraints: the disagree rule is written
before any dispute, the cataloger arbitrates with full context, and the
logged decision makes the final record auditable.
5. Why B best meets the objective: V2-D1.4 requires the handoff contract
to name input schema, output schema, and the disagree rule. B is the
only option that uses all three.
6. Every rejected choice explained: A has no termination guarantee. Two
workers can disagree forever and burn budget. C invents majority vote,
but the transcriber and translator judge different things, so a vote is
meaningless. D picks a winner by prestige, not by contract. The next
dispute reopens the same fight.
7. Exact limitation or tradeoff: the cataloger becomes a bottleneck on
12% of pages, and its arbitration quality bounds the archive's quality.
8. Relevant evidence (with date): handoff contract and disagree rule from
lesson-D1-4 (§4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when
disagreement signals a fixable input (bad scan) and one re-run resolves
it. C wins when three independent judges score the same rubric. D wins
never as a design. It is a bias.
10. Misconception tested: "more agents means the truth emerges." Without
a disagree rule, more agents mean more disputes.

## Q-M-05 (V2-D1.5)

**Scenario.** An airport plans aircraft turnaround. Fueling, catering, and
cleaning are independent tasks. Pushback depends on all three plus tower
clearance. The turnaround SLA is 45 minutes.

**Question.** Which decomposition fits?

**Options.**
A) One sequential chain for all tasks including pushback.
B) Fan-out: fuel, catering, and cleaning run in parallel, then fan-in to a
readiness check, then pushback after tower clearance.
C) One agent improvises the order per flight.
D) Parallelize everything, including pushback with tower clearance.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: decomposition pattern selection.
2. Lifecycle stage: design.
3. Objective: meet the 45-minute SLA without breaking dependencies.
4. Hard constraints: pushback needs all three tasks plus tower clearance,
45-minute SLA.
5. System layer: decomposition patterns (V2-D1.5).
6. Eliminate infeasible: all four are feasible to attempt.
7. Eliminate constraint-violating: D breaks the pushback dependency, C
has no plan.
8. Compare on objective: B parallelizes the independent work and
serializes the dependent work.
9. Hidden dependencies: the fan-in needs a readiness signal from each of
the three tasks.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Fueling, catering, and cleaning are
independent tasks. Pushback depends on all three plus tower clearance."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Independent tasks in parallel | No | Yes | Maybe | Yes |
| Pushback waits for dependencies | Yes | Yes | Maybe | No |
| Plan is repeatable | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: the fan-out runs the three
independent tasks at once (max time, not sum), the fan-in checks
readiness, and pushback waits for tower clearance.
5. Why B best meets the objective: V2-D1.5 says parallelize independent
work and sequence dependent work. B is the only option that does both.
6. Every rejected choice explained: A is safe but slow: the sum of three
tasks risks the 45-minute SLA. C has no repeatable plan. Improvisation
is not a decomposition. D parallelizes pushback past its dependency,
which is a safety violation, not an optimization.
7. Exact limitation or tradeoff: B needs the readiness check to be fast
and the three tasks to truly share no resources (one fuel truck serving
two tasks breaks independence).
8. Relevant evidence (with date): decomposition patterns from
lesson-D1-patterns (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
three tasks share one crew and cannot overlap. C wins never as a
pattern. D wins when tower clearance is pre-approved and pushback needs
no readiness signal.
10. Misconception tested: "parallelize everything for speed."
Dependencies are not optional. Parallelizing past them is a defect.

## Q-M-06 (V2-D1.6)

**Scenario.** A dental supply distributor processes 2,000 orders per day
manually at $1.10 per order in labor. An automated design costs $0.18 per
order plus $400 per month in fixed cost. The error rate is unchanged.

**Question.** Which number decides ship or no-ship?

**Options.**
A) The per-order cost difference alone.
B) Net monthly value: (2,000 x 30 x ($1.10 - $0.18)) - $400.
C) The model's accuracy score on the order set.
D) The p95 latency of the new system.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: business value decision.
2. Lifecycle stage: design to build decision.
3. Objective: decide whether the automation is worth building.
4. Hard constraints: error rate unchanged, so quality is not the
decider.
5. System layer: value chain (V2-D1.6).
6. Eliminate infeasible: all four are computable.
7. Eliminate constraint-violating: none violate a hard rule. The test is
which number answers the question.
8. Compare on objective: only B runs the full baseline to net value
chain.
9. Hidden dependencies: the math assumes volume stays at 2,000 per day.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "manually at $1.10 per order in labor...
$0.18 per order plus $400 per month in fixed cost."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Counts the fixed cost | No | Yes | No | No |
| Compares against the baseline | Partial | Yes | No | No |
| Answers in net dollars | No | Yes | No | No |

4. Why B satisfies all hard constraints: it runs the V2-D1.6 chain end to
end. Gross monthly saving: 60,000 orders x $0.92 = $55,200. Net: $55,200
- $400 = $54,800 per month. Positive by a wide margin.
5. Why B best meets the objective: ship or no-ship is a net value
question. Only B computes net value. The rest measure parts of the
system.
6. Every rejected choice explained: A ignores the $400 fixed cost and the
volume math. A per-unit delta is not a decision. C measures quality,
which the scenario holds constant. D measures speed, which no
requirement names.
7. Exact limitation or tradeoff: the math assumes steady volume and no
transition cost. A volume drop or a painful cutover changes the answer.
8. Relevant evidence (with date): baseline to improvement to cost to net
value from lesson-7-4A (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
fixed cost is zero and volume is fixed. C wins when the error rate
differs between options. D wins when an SLA names latency with a
penalty.
10. Misconception tested: "cheaper per unit means ship it." Net value
decides, and net includes fixed cost and volume.

## Q-M-07 (V2-D1.2)

**Scenario.** A food truck fleet tracks stock. Vendors self-report
inventory by text message. The POS records every sale. Stockouts lose
sales. Overstock spoils by evening.

**Question.** What is the system of record for stock levels?

**Options.**
A) The vendor's texted inventory.
B) The POS sales ledger minus deliveries, reconciled in code. Vendor
texts are untrusted input.
C) The model's estimate blended from both sources.
D) Whichever source reported most recently.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: system-of-record identification.
2. Lifecycle stage: design.
3. Objective: name the trustworthy source for stock truth.
4. Hard constraints: stockouts lose sales, overstock spoils. The number
must be right.
5. System layer: trust boundaries and state (V2-D1.2).
6. Eliminate infeasible: all four are feasible to build.
7. Eliminate constraint-violating: A trusts self-reports, C lets the
model invent stock, D is recency without trust.
8. Compare on objective: only B derives stock from the verified ledger.
9. Hidden dependencies: deliveries must be recorded as reliably as
sales.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Vendors self-report inventory by text
message. The POS records every sale."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Source is verified | No | Yes | No | No |
| Crosses no trust boundary unchecked | No | Yes | No | No |
| Reproducible in code | No | Yes | No | No |

4. Why B satisfies all hard constraints: the POS ledger is machine
recorded and auditable. Deliveries minus sales reconciled in code gives
a computed stock with a provenance chain. Vendor texts stay outside the
trust boundary as untrusted input.
5. Why B best meets the objective: V2-D1.2 requires naming the system of
record and the trust boundaries. The ledger is the record. The texts are
the boundary crossing.
6. Every rejected choice explained: A makes self-reports the truth. A
vendor's typo becomes the stock. C asks the model to blend sources, and
the blend is unverifiable. D picks by recency. A fresh lie beats an old
truth.
7. Exact limitation or tradeoff: B needs delivery records as reliable as
POS data. Theft, waste, and comps need their own entries or the ledger
drifts.
8. Relevant evidence (with date): trust boundaries and system of record
from lesson-D1-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
vendors scan barcodes into a verified app (then the report is trusted
input). C wins never for a system of record. D wins for a "latest news"
feed, not for stock.
10. Misconception tested: "newest data is truest data." Trust decides
truth, not recency.

## Q-M-08 (V2-D1.5), Select TWO

**Scenario.** A wind farm inspects 120 turbines per quarter. Each turbine
gets an independent inspection report. Report quality varies widely by
inspector.

**Question.** Which TWO decomposition patterns fit? Select TWO.

**Options.**
A) Fan-out/fan-in: one inspection task per turbine, merged into a fleet
report.
B) Critique pattern: a reviewer agent checks each report against the
inspection checklist.
C) Single sequential pass with no review.
D) Chaining where each turbine's report depends on the previous one.
E) One augmented call covering all 120 turbines.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: decomposition pattern selection (multi).
2. Lifecycle stage: design.
3. Objective: cover 120 independent inspections with consistent quality.
4. Hard constraints: turbines are independent, quality varies by
inspector.
5. System layer: decomposition patterns (V2-D1.5).
6. Eliminate infeasible: all five are feasible to attempt.
7. Eliminate constraint-violating: D invents a false dependency, E
exceeds any context window.
8. Compare on objective: independence calls for fan-out, quality
variance calls for critique.
9. Hidden dependencies: the merge needs a common report schema. The
critique needs the checklist.
10. Verify: A and B together. C covers neither constraint.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "Each turbine gets an independent inspection
report. Report quality varies widely by inspector."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Uses independence | Yes | No | No | No | No |
| Fixes quality variance | No | Yes | No | No | No |
| Scales to 120 turbines | Yes | Yes | Slow | No | No |

4. Why A and B satisfy all hard constraints: fan-out/fan-in runs the 120
independent inspections in parallel and merges them. The critique
pattern checks each report against the checklist before merge.
5. Why A and B best meet the objective: V2-D1.5 maps independence to
fan-out and quality variance to a validation pattern. The two patterns
compose: critique inside each fan-out branch, merge at the fan-in.
6. Every rejected choice explained: C is slow (120 sequential reports)
and has no quality gate. D chains independent tasks, which adds delay
for zero benefit. E stuffs 120 reports into one call: context overflow
and no per-report check.
7. Exact limitation or tradeoff: the critique step doubles per-report
cost, and the merge needs a strict schema or the fleet report is mush.
8. Relevant evidence (with date): decomposition patterns from
lesson-D1-patterns (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins when one
inspector does all 120 and quality is uniform. D wins when turbines
share a fault that propagates down the row. E wins never at this scale.
10. Misconception tested: "one pattern per design." Independent scale
and quality variance are two problems. They take two patterns.

## Q-M-09 (V2-D2.1)

**Scenario.** A microbrewery chatbot handles 3,000 chats per day. About
90% are FAQs: hours, location, tour booking. About 10% are recipe
troubleshooting: stuck fermentation, off flavors. A wrong recipe answer
ruins a customer's batch.

**Question.** Which tier strategy fits best?

**Options.**
A) Most capable tier for every chat.
B) Fast tier for FAQs, stronger tier for recipe troubleshooting, with a
quality floor: recipe answers must cite the brewing guide.
C) Fast tier for everything.
D) Stronger tier for FAQs, Fast tier for troubleshooting.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: model tier routing.
2. Lifecycle stage: design.
3. Objective: cut cost without risking ruined batches.
4. Hard constraints: wrong recipe advice ruins a batch, 3,000 chats per
day.
5. System layer: model selection and routing (V2-D2.1).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: C risks batch-ruining answers on the
hard 10%, D routes backwards.
8. Compare on objective: B matches tier strength to error cost per
class.
9. Hidden dependencies: the router must classify FAQ vs troubleshooting
reliably.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "90% are FAQs... 10% are recipe
troubleshooting. A wrong recipe answer ruins a customer's batch."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| FAQs stay cheap | No | Yes | Yes | No |
| Hard cases get strength | Yes | Yes | No | No |
| Quality floor on risky answers | No | Yes | No | No |

4. Why B satisfies all hard constraints: FAQs ride the cheap tier,
troubleshooting gets the stronger tier, and the citation floor grounds
the risky answers.
5. Why B best meets the objective: V2-D2.1 routes on the
capability-cost-latency trade-off with quality floors. Error cost, not
volume, sets the tier per class.
6. Every rejected choice explained: A is safe but wasteful: top tier on
3,000 chats with 90% FAQs. C saves money and risks ruined batches on
the hard 10%. D is backwards: it spends strength where the task is
trivial and starves the risky class.
7. Exact limitation or tradeoff: the router is a new failure point. A
misclassified troubleshooting chat lands on the cheap tier.
8. Relevant evidence (with date): tier routing and quality floors from
lesson-D2-1 (§4), Oct 6 2026, tier pricing from S10-S12, Oct 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
FAQ answers also carry high error cost. C wins when evals prove the
Fast tier clears the recipe floor. D wins never. It is backwards.
10. Misconception tested: "one tier for the whole product." The exam
rewards routing by error cost per class.

## Q-M-10 (V2-D2.2)

**Scenario.** An aquarium kiosk answers visitor questions. The animal
medical records must never reach visitors. A vendor proposes a system
prompt line: "Never reveal animal medical records."

**Question.** What is the correct control?

**Options.**
A) The system prompt line is enough. The model will comply.
B) A code filter: medical records stay out of the retrieval set, and an
output check blocks any medical content before display.
C) A longer system prompt with the rule repeated three times.
D) Fine-tune the model to dislike medical topics.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: control placement for a confidentiality rule.
2. Lifecycle stage: design.
3. Objective: guarantee medical records never reach visitors.
4. Hard constraints: the records must never be disclosed, visitors are
untrusted.
5. System layer: guardrails and enforcement (V2-D2.2, V2-D5.1).
6. Eliminate infeasible: all four are feasible to attempt.
7. Eliminate constraint-violating: A, C, and D rely on model behavior,
which is not a guarantee.
8. Compare on objective: only B enforces in code at two points.
9. Hidden dependencies: the retrieval index must tag medical records so
the filter can find them.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "must never reach visitors."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Guarantee, not guidance | No | Yes | No | No |
| Blocks at retrieval | No | Yes | No | No |
| Blocks at output | No | Yes | No | No |

4. Why B satisfies all hard constraints: the filter removes medical
records before the model ever sees them, and the output check catches
anything the filter missed. Two code gates, zero reliance on model
obedience.
5. Why B best meets the objective: V2-D2.2 is explicit: prompts are not
authorization, and structural enforcement gives the hard guarantee. A
"never" rule is a control, and controls live in code.
6. Every rejected choice explained: A is the exam's favorite trap: a
prompt is guidance the model may ignore under pressure or injection.
C is the same trap with repetition. Three signs are still signs. D
changes model tendencies but proves nothing per request and cannot be
audited.
7. Exact limitation or tradeoff: B needs the medical tag maintained on
every record. An untagged record slips past the filter to the output
check.
8. Relevant evidence (with date): "prompts are not authorization" from
lesson-D2-2 (§4), Oct 6 2026, structural enforcement from lesson-D5-1,
Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins for tone
guidance ("be friendly"), never for confidentiality. C wins never as a
control. D wins for stable style needs, not for data protection.
10. Misconception tested: "a strong instruction equals a control." It
does not. The exam rewards the answer that puts the rule in code.

## Q-M-11 (V2-D2.3), Select TWO

**Scenario.** A piano restoration shop builds a cost estimator. Customers
describe damage in free text. The shop wants fixed-format estimates and
wants the model to refuse jobs outside its craft (e.g., car repair).

**Question.** Which TWO prompt techniques fit? Select TWO.

**Options.**
A) Few-shot examples including rejection examples (car repair refused).
B) Structured output schema for the estimate.
C) Zero-shot with no examples and no schema.
D) Asking the model to "try its best" on any topic.
E) A longer model with no technique changes.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: prompt technique selection (multi).
2. Lifecycle stage: design.
3. Objective: fixed-format estimates plus reliable refusals.
4. Hard constraints: estimates need a fixed format, out-of-craft jobs
must be refused.
5. System layer: prompt techniques (V2-D2.3).
6. Eliminate infeasible: all five are feasible to attempt.
7. Eliminate constraint-violating: C and D leave format and refusal to
chance, E changes no technique.
8. Compare on objective: A teaches the refusal boundary, B enforces the
format.
9. Hidden dependencies: the rejection examples must cover near-miss
cases (furniture repair vs piano repair).
10. Verify: A and B together. No third fits.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "fixed-format estimates... refuse jobs
outside its craft."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Teaches the refusal boundary | Yes | No | No | No | No |
| Enforces the output format | No | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: rejection examples show the
model exactly where the craft boundary lies, and the structured schema
makes the format a contract, not a hope.
5. Why A and B best meet the objective: V2-D2.3 prescribes the simplest
technique that passes evals: few-shot with rejection examples for the
boundary, structured outputs for the format. Each technique answers one
requirement.
6. Every rejected choice explained: C leaves both format and refusal to
chance. D is an anti-technique: "try its best" invites out-of-craft
answers. E spends money on a bigger model while the missing pieces are
technique, not capacity.
7. Exact limitation or tradeoff: the example set needs maintenance as
new edge cases arrive, and the schema needs versioning with the
estimate format.
8. Relevant evidence (with date): few-shot with rejection examples and
structured outputs from lesson-D2-3 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins for a
low-stakes internal draft with no format needs. D wins never. E wins
when evals show the task exceeds the current tier's capacity.
10. Misconception tested: "a bigger model replaces technique." Format
and refusal boundaries are technique problems first.

## Q-M-12 (V2-D2.4)

**Scenario.** An elevator maintenance assistant keeps six months of
service history in context on every call. Token bills tripled. Techs
report the model now confuses last month's fix with this month's fault.
Duplicate sensor readings appear three times per call.

**Question.** What is the first fix?

**Options.**
A) Move to a larger context window.
B) Just-in-time retrieval of relevant history plus compaction of the
conversation, with dedupe of sensor readings.
C) A stronger model tier.
D) Longer system prompt explaining the timeline.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: context diagnosis and fix.
2. Lifecycle stage: operate and optimize.
3. Objective: cut tokens and fix the confusion.
4. Hard constraints: bills tripled, confusion between months, duplicate
readings.
5. System layer: context management (V2-D2.4).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A feeds the growth, C buys strength
for a context problem, D adds tokens to a token problem.
8. Compare on objective: B attacks growth, duplication, and dilution at
once.
9. Hidden dependencies: retrieval needs the history indexed by elevator
and date.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "six months of service history in context
on every call... confuses last month's fix with this month's fault...
Duplicate sensor readings appear three times."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Cuts token growth | No | Yes | No | No |
| Removes duplication | No | Yes | No | No |
| Fixes dilution/confusion | No | Yes | No | No |

4. Why B satisfies all hard constraints: just-in-time retrieval loads
only the relevant history, compaction keeps the active context small,
and dedupe removes the triple readings. All three diagnosed faults
(growth, duplication, dilution) get a fix.
5. Why B best meets the objective: V2-D2.4 diagnoses context faults as
growth, duplication, loss, exhaustion, and dilution, then matches each
to active context vs retrieval vs compaction. B is the only option that
follows the diagnosis.
6. Every rejected choice explained: A is the classic error: a bigger
window holds more duplicates and more dilution. C upgrades the reader
while the text stays bloated. D adds prompt tokens to a bill driven by
history tokens.
7. Exact limitation or tradeoff: retrieval can miss a relevant old fix.
The index quality bounds the answer quality.
8. Relevant evidence (with date): context fault taxonomy from
lesson-D2-4 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
task genuinely needs the full six months every call and the budget
allows it. C wins when the trace shows the chunk present and the answer
still wrong (model layer). D wins never for a token problem.
10. Misconception tested: "bigger window fixes context problems." It
feeds them. Diagnose first: growth, duplication, dilution.

## Q-M-13 (V2-D2.5)

**Scenario.** A sports league rulebook assistant serves 20,000 calls per
day. Every call starts with the same 8,000-token rulebook prefix.
Questions vary. The team considers prompt caching.

**Question.** What decides whether caching pays?

**Options.**
A) The total daily call count alone.
B) Whether the 8,000-token prefix is stable across calls and the hit
rate clears the break-even point.
C) The model tier chosen.
D) The length of the user questions.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: caching economics.
2. Lifecycle stage: design to optimize.
3. Objective: decide if prompt caching pays.
4. Hard constraints: 8,000-token stable prefix, varied questions.
5. System layer: prompt reuse (V2-D2.5).
6. Eliminate infeasible: all four are answerable.
7. Eliminate constraint-violating: none violate. The test is which factor
decides.
8. Compare on objective: caching economics rest on prefix stability and
hit rate vs break-even.
9. Hidden dependencies: prefix edits reset the cache. The TTL bounds the
write cost.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the same 8,000-token rulebook prefix.
Questions vary."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Names the reuse unit | No | Yes | No | No |
| Names the break-even test | No | Yes | No | No |

4. Why B satisfies all hard constraints: prompt caching reuses the
stable input prefix across calls with different suffixes. The scenario
matches exactly: stable prefix, varied questions. The break-even test
(on the lesson toy, about 4% hit rate) decides the money.
5. Why B best meets the objective: V2-D2.5 defines the mechanism
(prefix rules, TTL, costs, break-even). B is the only option that names
both the mechanism's precondition and its economic test.
6. Every rejected choice explained: A counts calls but not reuse: 20,000
calls with a shifting prefix cache nothing. C sets the per-token price
but not whether caching applies. D is irrelevant: the suffix varies by
design under prompt caching.
7. Exact limitation or tradeoff: prefix edits (rulebook updates) reset
the cache and re-pay the write cost. Measure the real hit rate before
claiming savings.
8. Relevant evidence (with date): prompt caching prefix rules and
break-even toy from lesson-D2-5 (§4), Oct 6 2026, pricing from S10-S12,
Oct 2026.
9. Counterfactual where each plausible alternative wins: A wins never
alone. C wins when comparing tiers, not caching. D wins for response
caching, where identical whole prompts are the precondition.
10. Misconception tested: "high volume means caching always pays."
Stability plus hit rate decide, not volume.

## Q-M-14 (V2-D2.1)

**Scenario.** A library catalog agent runs on the Balanced tier. The
provider releases a new version of the same tier. The team wants the
new version live by Friday.

**Question.** What is the required first step?

**Options.**
A) Swap the model ID on Friday. Same tier means same behavior.
B) Run the regression suite against the new version and compare with the
pinned baseline before any traffic moves.
C) Ask the model if it feels ready for the new version.
D) Route 100% of traffic on Friday and watch the dashboards.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: model change management.
2. Lifecycle stage: operate.
3. Objective: ship the upgrade without silent behavior change.
4. Hard constraints: catalog answers must stay correct. No untested
change reaches users.
5. System layer: model selection lifecycle (V2-D2.1).
6. Eliminate infeasible: all four are feasible actions.
7. Eliminate constraint-violating: A assumes sameness, C is nonsense, D
tests in production.
8. Compare on objective: only B measures the new version before exposure.
9. Hidden dependencies: the regression suite must cover the catalog's
edge cases, not only happy paths.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The provider releases a new version of the
same tier."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Treats the upgrade as a production change | No | Yes | No | No |
| Measures before exposure | No | Yes | No | No |

4. Why B satisfies all hard constraints: V2-D2.1 treats every model
change as a production change. The regression suite compares the new
version against the pinned baseline on representative, edge, and
adversarial cases before any user sees it.
5. Why B best meets the objective: behavior drifts between versions even
inside a tier. Only measurement catches the drift. B is the only option
that measures first.
6. Every rejected choice explained: A assumes the tier name guarantees
behavior. It does not. C anthropomorphizes the model. The model has no
say in the change process. D is production testing: users become the
regression suite.
7. Exact limitation or tradeoff: the suite takes time to run, so Friday
may slip. A rushed swap is worse than a late swap.
8. Relevant evidence (with date): "upgrades are production changes" from
lesson-D2-1 (§4), Oct 6 2026, regression suites from lesson-D4-2, Oct 6
2026.
9. Counterfactual where each plausible alternative wins: A wins never
for a version change. C wins never. D wins for a shadow deploy where
the new version gets copied traffic with no user impact.
10. Misconception tested: "same tier means same model." Version changes
behavior. Test the version, not the name.

## Q-M-15 (V2-D2.4), Select THREE

**Scenario.** A vineyard sensor assistant answers irrigation questions.
Each call loads the full season of sensor readings: 60,000 tokens.
Duplicate readings from overlapping sensors appear twice. The model
sometimes answers from March data for a July question.

**Question.** Which THREE context faults are present? Select THREE.

**Options.**
A) Context growth: the full season loads on every call.
B) Duplication: overlapping sensors repeat readings.
C) Dilution: March data answers July questions.
D) Context exhaustion: the window overflows.
E) Conversation loss: old turns vanish.

**Answer.** A, B, C

**Method walk (Steps 1-10).**
1. Question type: context fault diagnosis (multi).
2. Lifecycle stage: operate and optimize.
3. Objective: name the faults the evidence shows.
4. Hard constraints: 60,000 tokens per call, duplicates, wrong-month
answers.
5. System layer: context fault taxonomy (V2-D2.4).
6. Eliminate infeasible: all five are real fault names.
7. Eliminate constraint-violating: D needs an overflow (none stated), E
needs lost turns (none stated).
8. Compare on objective: the evidence names growth and duplication
directly, and the March-for-July answers show dilution: the model
attends to the wrong span of the bloated context.
9. Hidden dependencies: each fault needs its own fix (retrieval for
growth, dedupe for duplication, fewer better-placed chunks for
dilution).
10. Verify: A, B, and C. D and E lack evidence. Select THREE.

**Explanation.**
1. Correct answer: A, B, C.
2. Decisive scenario phrase: "the full season of sensor readings:
60,000 tokens. Duplicate readings from overlapping sensors appear
twice. The model sometimes answers from March data for a July
question."
3. Requirement-to-option matrix:

| Evidence | A | B | C | D | E |
|---|---|---|---|---|---|
| 60,000 tokens per call | Yes | No | No | No | No |
| Readings appear twice | No | Yes | No | No | No |
| Wrong-month answers from a bloated context | No | No | Yes | No | No |
| Window overflow stated | No | No | No | No | No |

4. Why A, B, and C satisfy the diagnosis: the full-season load on every
call is textbook context growth. The doubled readings are textbook
duplication. The March-for-July answers are textbook dilution: the
model attends to the wrong span of an oversized context. All three are
named faults in the V2-D2.4 taxonomy.
5. Why A, B, and C best meet the objective: V2-D2.4 names growth,
duplication, and dilution as distinct faults with distinct fixes
(retrieval for growth, dedupe for duplication, fewer better-placed
chunks for dilution). Naming all three points at all three fixes.
6. Every rejected choice explained: D needs an overflow error, which
the scenario never states. E needs vanishing turns, which never
appear.
7. Exact limitation or tradeoff: fixing all three still leaves index
quality as the bound for the retrieval that replaces the full-season
load.
8. Relevant evidence (with date): context fault taxonomy (growth,
duplication, loss, exhaustion, dilution) from lesson-D2-4 (§4), Oct 6
2026.
9. Counterfactual where each plausible alternative wins: D wins when
the call errors on window size. E wins when old turns vanish after
compaction.
10. Misconception tested: "growth alone explains every context
failure." Each named fault needs its own fix. Name every fault the
evidence shows.

## Q-M-16 (V2-D3.1)

**Scenario.** A shipping broker agent carries 24 tools. Three tools
overlap: `quote_rate`, `get_rate_quote`, and `rate_lookup` do the same
thing. A `delete_shipment` tool exists though no task deletes shipments.
The team proposes logging all tool calls for review.

**Question.** What is the correct bloat response?

**Options.**
A) Keep all 24 tools and rely on the logs.
B) Remove the two overlapping quote tools and the delete tool. Keep the
logs as observability, not as the fix.
C) Add three more quote tools for redundancy.
D) Log the delete tool's calls and keep it.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: capability bloat evaluation.
2. Lifecycle stage: design review.
3. Objective: shrink the tool surface to least privilege.
4. Hard constraints: overlapping descriptions confuse the model, the
delete tool serves no task.
5. System layer: tool config evaluation (V2-D3.1).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A, C, and D keep unneeded or
dangerous tools.
8. Compare on objective: only B removes what the tasks do not need.
9. Hidden dependencies: removal needs a check that no hidden workflow
calls the delete tool.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Three tools overlap... A `delete_shipment`
tool exists though no task deletes shipments."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Removes overlapping tools | No | Yes | No | No |
| Removes the unneeded delete tool | No | Yes | No | No |
| Treats logging as observability | No | Yes | No | No |

4. Why B satisfies all hard constraints: one quote tool stays, two
redundant descriptions leave (wrong-tool risk falls), and the delete
tool leaves the config entirely (attack surface shrinks).
5. Why B best meets the objective: V2-D3.1 demands least privilege:
remove unneeded tools, limit data visibility and writes, and treat
overlapping descriptions as a bloat signal. B executes all three.
6. Every rejected choice explained: A keeps the bloat and mistakes logs
for a fix. C adds redundancy, which is more bloat. D is the exam's
named trap: logging a dangerous unneeded tool is negligence with a
dashboard.
7. Exact limitation or tradeoff: removal needs the bloat review repeated
periodically. Tools creep back without an owner.
8. Relevant evidence (with date): "logging is not removal" from
lesson-D3-1 (§4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never
as a bloat fix. C wins never. D wins when the delete tool is needed
for incident response. Then it stays watched and gated.
10. Misconception tested: "monitoring a tool equals securing it." Only
removal shrinks the surface. Logs watch the surface that remains.

## Q-M-17 (V2-D3.2)

**Scenario.** A lab-results bot serves three clinics. Each clinic's
patients must see only their own clinic's results. The design filters by
the clinic name the user types in chat.

**Question.** What is wrong with this design?

**Options.**
A) Nothing. The filter uses the clinic name.
B) The clinic name is a user claim, not an authorization decision. The
filter must check the authenticated identity against the clinic roster in
code before any data is read.
C) The bot needs a bigger model to understand clinic names.
D) The filter should run after the model answers.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: authorization design flaw.
2. Lifecycle stage: design review.
3. Objective: enforce tenant isolation on lab results.
4. Hard constraints: patients see only their own clinic's results.
5. System layer: authN and authZ (V2-D3.2).
6. Eliminate infeasible: all four are feasible to build.
7. Eliminate constraint-violating: A accepts the flaw, C buys strength
for a trust problem, D filters after exposure.
8. Compare on objective: only B replaces the claim with a verified
check.
9. Hidden dependencies: the roster must map authenticated users to
clinics.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The design filters by the clinic name the
user types in chat."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Identity is verified | No | Yes | No | No |
| Check runs before data access | Yes | Yes | N/A | No |
| Claim rejected as proof | No | Yes | No | No |

4. Why B satisfies all hard constraints: the authenticated identity is
checked against the clinic roster in code. A user who types another
clinic's name gets nothing. The check runs before any read.
5. Why B best meets the objective: V2-D3.2 is explicit: user role claims
are not authZ, and source-system ACLs must be preserved. B enforces the
roster. The scenario's design enforces a chat message.
6. Every rejected choice explained: A blesses the flaw. C treats a trust
boundary as a capability problem. D filters after the model answers,
which is after the data was read: the leak already happened.
7. Exact limitation or tradeoff: B needs the roster kept current. A
stale roster locks out real patients or admits former ones.
8. Relevant evidence (with date): "user role claims are not authZ" from
lesson-D3-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins never
for patient data. C wins when the failure is name ambiguity across
clinics with verified identity. D wins never. Post-answer filtering is
not a control.
10. Misconception tested: "the user said so, so it is true." Claims are
not identity. The roster is.

## Q-M-18 (V2-D3.3), Select TWO

**Scenario.** A support answer pipeline has four stages with measured p95
latencies: parse 0.1 s, retrieval 0.9 s, rerank 1.8 s, model reasoning
2.2 s. Total p95 is 5.0 s. The SLA demands p95 under 3.0 s.

**Question.** Which TWO stages should the team optimize first? Select
TWO.

**Options.**
A) Parse.
B) Retrieval.
C) Rerank.
D) Model reasoning.
E) Add a fifth stage for safety checks.

**Answer.** C, D

**Method walk (Steps 1-10).**
1. Question type: latency optimization priority (multi).
2. Lifecycle stage: operate and optimize.
3. Objective: bring p95 from 5.0 s under 3.0 s.
4. Hard constraints: 2.0 s must come out of the pipeline, SLA is p95.
5. System layer: per-stage latency analysis (V2-D3.3).
6. Eliminate infeasible: all five are feasible actions.
7. Eliminate constraint-violating: A saves 0.1 s at most, E adds
latency.
8. Compare on objective: C and D hold 4.0 s of the 5.0 s total.
9. Hidden dependencies: cutting reasoning must not drop the quality
floor.
10. Verify: C and D. B's 0.9 s cannot close the gap alone.

**Explanation.**
1. Correct answer: C, D.
2. Decisive scenario phrase: "rerank 1.8 s, model reasoning 2.2 s...
SLA demands p95 under 3.0 s."
3. Requirement-to-option matrix:

| Stage | p95 | Share of 5.0 s | Closes the 2.0 s gap |
|---|---|---|---|
| Parse | 0.1 s | 2% | No |
| Retrieval | 0.9 s | 18% | No |
| Rerank | 1.8 s | 36% | With D, yes |
| Reasoning | 2.2 s | 44% | With C, yes |

4. Why C and D satisfy the objective: they hold 4.0 s of the 5.0 s
total. The 2.0 s cut must come mostly from them. Optimizing parse saves
0.1 s at best, which is noise.
5. Why C and D best meet the objective: V2-D3.3 says measure per stage
and optimize the stages that dominate. Measurement names rerank and
reasoning. Opinion does not enter.
6. Every rejected choice explained: A optimizes 2% of the budget. Even
perfect parse saves 0.1 s. B is real latency but only 18%. It cannot
carry the 2.0 s cut. E adds a stage, which moves p95 the wrong way.
7. Exact limitation or tradeoff: cutting reasoning risks the quality
floor. Every latency cut must hold quality and safety floors.
8. Relevant evidence (with date): per-stage measurement and SLA
optimization from lesson-D3-3 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
parse is 2.5 s of the total. B wins when retrieval dominates. E wins
when a missing safety check is the actual requirement, not latency.
10. Misconception tested: "optimize the stage you understand best."
Optimize the stage the measurement names.

## Q-M-19 (V2-D3.4)

**Scenario.** A food delivery dispatch agent fails an order: the driver
assignment never happened. The logs show per-hop events: model call ok,
retrieval ok, tool call timed out, queue event missing. The team cannot
tell which hop dropped the assignment.

**Question.** What gap exists?

**Options.**
A) More log lines per hop.
B) One run id propagated across the model call, retrieval, tools, and
the queue, so the run reconstructs end to end.
C) A bigger model.
D) A second queue.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: observability gap diagnosis.
2. Lifecycle stage: operate.
3. Objective: reconstruct the failed run across hops.
4. Hard constraints: the assignment vanished between hops. Per-hop logs
exist.
5. System layer: observability at scale (V2-D3.4).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A adds volume without linkage, C buys
strength for a tracing problem, D adds hops.
8. Compare on objective: only B links the existing events into one run.
9. Hidden dependencies: every hop (including the queue) must accept and
forward the run id.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The team cannot tell which hop dropped
the assignment."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Links events across hops | No | Yes | No | No |
| Covers the queue hop | No | Yes | No | No |
| Uses existing logs | No | Yes | No | No |

4. Why B satisfies all hard constraints: the run id turns scattered
per-hop events into one reconstructable run. The missing queue event
becomes visible as the gap in the chain.
5. Why B best meets the objective: V2-D3.4 requires tracing model calls,
retrieval, tools, queues, and dependencies with end-to-end
reconstructability. The run id is the mechanism.
6. Every rejected choice explained: A adds log volume. Unlinked events
stay unlinked. C upgrades the model while the failure is in the hops.
D adds a second queue, which is a second place to lose the assignment.
7. Exact limitation or tradeoff: the run id needs propagation discipline
and clock discipline across hops, plus a trace store.
8. Relevant evidence (with date): trace across model, retrieval, tools,
and queues from lesson-D3-4 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when a
hop logs nothing at all. C wins when the trace shows the model chose
wrong with full context. D wins never for observability.
10. Misconception tested: "more logs equal observability." Linked logs
equal observability. Unlinked logs are noise.

## Q-M-20 (V2-D3.5)

**Scenario.** A city archive builds RAG over two collections: council
meeting minutes and zoning maps. Minutes are long prose with agenda
items. Maps are large images with district labels.

**Question.** Which chunking fits?

**Options.**
A) Fixed 500-token chunks for both collections.
B) Minutes chunked by agenda item, maps chunked by district tile. Each
chunk carries its structure metadata.
C) One chunk per entire document for both.
D) Random chunks for variety.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: chunking strategy.
2. Lifecycle stage: design.
3. Objective: chunk by document structure and query type.
4. Hard constraints: two different document shapes, queries target
agenda items and districts.
5. System layer: RAG pipeline chunking (V2-D3.5).
6. Eliminate infeasible: all four are feasible to implement.
7. Eliminate constraint-violating: A splits agenda items mid-item, C
exceeds useful chunk size, D is nonsense.
8. Compare on objective: only B matches chunk boundaries to query
boundaries.
9. Hidden dependencies: the tile boundaries must align with the district
labels.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Minutes are long prose with agenda items.
Maps are large images with district labels."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Chunk boundary matches query unit | No | Yes | No | No |
| Respects document structure | No | Yes | No | No |
| Metadata supports filtering | No | Yes | No | No |

4. Why B satisfies all hard constraints: agenda-item chunks answer
agenda-item queries. District tiles answer district queries. Structure
metadata lets retrieval filter before scoring.
5. Why B best meets the objective: V2-D3.5 chunks by document structure
and query type. B is the only option that does both per collection.
6. Every rejected choice explained: A cuts agenda items in half and
slices maps on arbitrary token lines. C makes each chunk a whole
document: retrieval returns the haystack. D is not a strategy.
7. Exact limitation or tradeoff: structure-aware chunking needs a
parser per document type. The parsing stage becomes a failure point to
monitor.
8. Relevant evidence (with date): chunking by document structure and
query type from lesson-D3-5 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
collection is uniform prose with no structure. C wins when documents
are tiny. D wins never.
10. Misconception tested: "one chunk size fits all." Structure decides
chunking, not a fixed token count.

## Q-M-21 (V2-D3.6)

**Scenario.** An airline disruption bot rebooks passengers during
storms. Seat inventory changes every minute. The design embeds yesterday's
seat map in the RAG index.

**Question.** What is the correct retrieval design?

**Options.**
A) Keep the seat map in the index. Refresh it nightly.
B) Put live seat inventory behind a tool call at rebooking time. Use the
index only for stable policy text.
C) Drop retrieval entirely and guess seat availability.
D) Cache one seat map per week for consistency.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: retrieval strategy for live state.
2. Lifecycle stage: design.
3. Objective: rebook against true seat inventory.
4. Hard constraints: inventory changes every minute. A wrong rebooking
strands a passenger.
5. System layer: retrieval strategy (V2-D3.6).
6. Eliminate infeasible: all four are feasible to build.
7. Eliminate constraint-violating: A, C, and D serve stale or invented
inventory.
8. Compare on objective: only B reads live state at decision time.
9. Hidden dependencies: the tool needs the airline's inventory API with
per-request auth.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Seat inventory changes every minute."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Reads current inventory | No | Yes | No | No |
| Stable policy stays retrievable | Yes | Yes | No | Yes |
| No stranded passengers from stale data | No | Yes | No | No |

4. Why B satisfies all hard constraints: the tool call reads the live
inventory at the moment of rebooking. The index keeps the slow-moving
policy text, which is what indexes are for.
5. Why B best meets the objective: V2-D3.6 is explicit: live
transactional state belongs behind a tool call, not a stale index. B is
the only option that follows the rule.
6. Every rejected choice explained: A serves yesterday's seats during
today's storm. C invents inventory. D is worse than A: a week-old map
during irregular operations.
7. Exact limitation or tradeoff: the tool call adds latency and needs
the inventory API's uptime. A cache of seconds (not hours) is the
compromise.
8. Relevant evidence (with date): live state behind a tool call from
lesson-D3-6 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
inventory changes daily, not minutely. C wins never. D wins never for
live state.
10. Misconception tested: "the index holds all knowledge." Indexes hold
slow knowledge. Live state needs a live call.

## Q-M-22 (V2-D3.7), Select TWO

**Scenario.** A farm co-op builds two integrations. (1) A shared soil
sensor capability needed by five teams in three languages. (2) A billing
pair: one Python service calling one internal invoicing API.

**Question.** Which TWO mechanisms fit? Select TWO.

**Options.**
A) MCP server for the shared soil sensor capability.
B) Direct API for the single billing pair.
C) MCP server for the single billing pair.
D) CLI wrapper for the soil sensors.
E) Direct API reimplemented five times for the sensors.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: integration mechanism selection (multi).
2. Lifecycle stage: design.
3. Objective: pick the mechanism per integration.
4. Hard constraints: five teams and three languages for sensors. One
consumer and one language for billing.
5. System layer: integration mechanism choice (V2-D3.7).
6. Eliminate infeasible: all five are feasible.
7. Eliminate constraint-violating: D adds parse risk with no need, E
duplicates work five times, C pays protocol tax for one pair.
8. Compare on objective: reuse decides the sensor side, simplicity
decides the billing side.
9. Hidden dependencies: the MCP server needs versioning and uptime. The
direct API needs per-client updates only.
10. Verify: A and B. Each answers one integration.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "five teams in three languages... one
Python service calling one internal invoicing API."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Serves five teams, three languages | Yes | No | Yes | No | No |
| Cheapest for one pair | No | Yes | No | No | No |
| Avoids duplicate implementations | Yes | N/A | Yes | No | No |

4. Why A and B satisfy all hard constraints: one MCP server with
declared tools serves all five sensor teams. The direct API is the
cheapest correct choice for one consumer in one language.
5. Why A and B best meet the objective: V2-D3.7 compares mechanisms on
reuse, security boundaries, ownership, and operational complexity. Reuse
is real on the sensor side (MCP wins) and absent on the billing side
(direct API wins).
6. Every rejected choice explained: C pays MCP's protocol tax (server
lifecycle, versioning) for a single pair with zero reuse gain. D wraps
a capability in text parsing with no need. E reimplements the same
integration five times, which is the cost MCP exists to kill.
7. Exact limitation or tradeoff: the MCP server is a new service to own.
The direct API needs per-client updates if the billing pair grows.
8. Relevant evidence (with date): five-option mechanism table from
lesson-D3-7 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins when the
billing pair grows to five consumers. D wins when the sensors exist
only as a CLI. E wins never. It is the anti-pattern.
10. Misconception tested: "newest protocol wins everywhere." Reuse
decides. One pair takes the direct API.

## Q-M-23 (V2-D3.8)

**Scenario.** A real-estate listing agent carries 45 tools with
overlapping names. Token budget is tight. The chat latency SLA is loose
(10 seconds). Wrong-tool picks climb.

**Question.** Which context strategy fits?

**Options.**
A) Monolithic context: load all 45 schemas on every call.
B) Progressive discovery: show tool names first, fetch full schemas on
demand.
C) Remove all tools and guess.
D) Load 45 schemas plus full documentation on every call.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: discovery vs monolithic context.
2. Lifecycle stage: design to optimize.
3. Objective: cut tokens and wrong-tool picks within the loose SLA.
4. Hard constraints: 45 tools, overlapping names, tight token budget,
10-second SLA.
5. System layer: progressive discovery (V2-D3.8).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A keeps the bloat, C removes
capability, D adds tokens.
8. Compare on objective: only B shrinks both the token bill and the pick
surface.
9. Hidden dependencies: the discovery protocol must return the right
schema on first fetch.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "45 tools with overlapping names. Token
budget is tight... Wrong-tool picks climb."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Cuts schema tokens per call | No | Yes | Yes | No |
| Shrinks the visible pick set | No | Yes | N/A | No |
| Fits the 10 s SLA | Yes | Yes | Yes | Maybe |

4. Why B satisfies all hard constraints: names-only first view cuts the
per-call schema tokens. Fetching the chosen schema on demand keeps the
visible choice set small, which cuts wrong-tool picks. The discovery
round trip fits inside the loose 10-second SLA.
5. Why B best meets the objective: V2-D3.8 prescribes discovery when the
tool surface is large and tasks vary. 45 overlapping tools is past the
threshold, and the SLA has room for the round trip.
6. Every rejected choice explained: A keeps 45 schemas in context every
call: tokens burn and picks stay confused. C deletes the capability the
product needs. D is A with documentation: more tokens, same confusion.
7. Exact limitation or tradeoff: discovery adds one round trip per call.
Under a tight SLA it would lose.
8. Relevant evidence (with date): discovery vs monolithic constraints
from lesson-D3-8 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins with 8
tools and a 2-second SLA. C wins never as a strategy. D wins never.
10. Misconception tested: "load everything so the model can choose."
Past the bloat threshold, everything to choose from means nothing
chosen well.

## Q-M-24 (V2-D3.2)

**Scenario.** A school district chatbot lets parents ask about grades. A
grade change moves through the student information system. The design
lets the model call the grade-change tool when the chat sounds
convincing.

**Question.** Where must the authorization check run?

**Options.**
A) In the system prompt: "only change grades for verified parents."
B) In code before the tool runs: verify the caller's identity and their
right to change that student's grade, then allow or deny.
C) After the tool runs, in the audit log.
D) In the model's judgment of the conversation.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: authorization enforcement placement.
2. Lifecycle stage: design.
3. Objective: gate grade changes on real authority.
4. Hard constraints: grade changes are high-stakes and regulated.
"Sounds convincing" is not authority.
5. System layer: authZ enforcement (V2-D3.2).
6. Eliminate infeasible: all four are feasible to build.
7. Eliminate constraint-violating: A and D trust the model, C checks
after the change.
8. Compare on objective: only B decides before the side effect in code.
9. Hidden dependencies: the identity system must link callers to
students.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "lets the model call the grade-change tool
when the chat sounds convincing."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Decides before the side effect | No | Yes | No | Maybe |
| Uses verified identity | No | Yes | No | No |
| Deterministic, auditable | No | Yes | Partial | No |

4. Why B satisfies all hard constraints: the code check verifies who
calls and whether they may change that student's grade. The tool never
runs on a convincing tone.
5. Why B best meets the objective: V2-D3.2 demands deterministic
enforcement for side effects, before context, with the model as none of
the three (not the identity, not the policy, not the lock). B is the
only option that puts the lock in code.
6. Every rejected choice explained: A is the prompt-as-control trap. C
logs the change after it happened. The grade is already wrong. D makes
the model the authorization authority, which V2-D3.2 forbids.
7. Exact limitation or tradeoff: B needs the parent-student mapping
maintained. A stale mapping blocks legitimate changes.
8. Relevant evidence (with date): deterministic enforcement for side
effects from lesson-D3-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins for
tone guidance, never for grade changes. C wins as a complement to B,
never alone. D wins never as authorization.
10. Misconception tested: "the model can tell who is authorized." It
cannot. Code checks identity against policy.

## Q-M-25 (V2-D3.5)

**Scenario.** A legal contract RAG pipeline runs: ingestion, parsing,
chunking, metadata, indexing, retrieval, rerank, assembly, generation.
Answers cite clause numbers. A cited clause once supported the opposite
of the claim.

**Question.** Which pipeline stage is absent?

**Options.**
A) A bigger chunk size.
B) Grounding and citation checks: each cited claim verified against its
source chunk before the answer ships.
C) A stronger reranker.
D) More documents in the index.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: pipeline gap diagnosis.
2. Lifecycle stage: design review.
3. Objective: stop unsupported citations.
4. Hard constraints: cited clauses must support their claims. One
inversion already shipped.
5. System layer: RAG pipeline stages (V2-D3.5).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A, C, and D improve retrieval, not
verification.
8. Compare on objective: only B checks the claim against the source.
9. Hidden dependencies: the checker needs the cited chunk text, not just
the clause number.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "A cited clause once supported the opposite
of the claim."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Verifies claim against source | No | Yes | No | No |
| Blocks before ship | No | Yes | No | No |

4. Why B satisfies all hard constraints: the grounding stage checks that
the source chunk implies the claim. The inverted citation fails the
check and routes to fix instead of shipping.
5. Why B best meets the objective: V2-D3.5 lists grounding and citation
checks as pipeline stages. The scenario's pipeline ends at generation.
The missing stage is the one that would have caught the inversion.
6. Every rejected choice explained: A changes chunk size. A bigger
chunk can still contradict the claim. C improves ranking. The top chunk
was already retrieved. D adds documents. More sources do not verify
claims.
7. Exact limitation or tradeoff: the check costs one verification per
cited claim. Scope it to consequential claims.
8. Relevant evidence (with date): grounding and citation checks in the
RAG pipeline from lesson-D3-5 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
chunks split clauses mid-sentence. C wins when the wrong chunk ranks
first. D wins when the clause is absent from the index.
10. Misconception tested: "retrieval quality equals answer truth."
Retrieval finds candidates. Grounding verifies them.

## Q-M-26 (V2-D4.1), Select TWO

**Scenario.** A hiring-screening assistant ranks applicants from resumes.
The company faces hiring-bias regulation. A wrong rank costs a good
candidate the job.

**Question.** Which TWO metrics belong in the evaluation? Select TWO.

**Options.**
A) Groundedness: each claimed resume fact traces to the source resume.
B) Subgroup fairness: rank quality measured per demographic group, not
as one aggregate.
C) Tokens per resume.
D) P95 latency.
E) Model confidence score.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: metric selection (multi).
2. Lifecycle stage: design of evaluation.
3. Objective: measure what the hiring decision risks.
4. Hard constraints: bias regulation, wrong ranks cost candidates jobs.
5. System layer: evaluation metrics (V2-D4.1).
6. Eliminate infeasible: all five are measurable.
7. Eliminate constraint-violating: C and D measure cost and speed, not
the decision risk. E is uncalibrated.
8. Compare on objective: A guards truth, B guards fairness across
groups.
9. Hidden dependencies: subgroup measurement needs the group labels and
a fairness floor.
10. Verify: A and B. No third measures the decision risk.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "faces hiring-bias regulation. A wrong
rank costs a good candidate the job."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Measures decision truth | Yes | No | No | No | No |
| Measures fairness per group | No | Yes | No | No | No |
| Required by the risk | Yes | Yes | No | No | No |

4. Why A and B satisfy the objective: groundedness catches invented
resume facts (the direct harm), and subgroup measurement catches bias
hiding inside a good aggregate (the regulated harm).
5. Why A and B best meet the objective: V2-D4.1 turns vague requirements
into acceptance thresholds on task success, groundedness, safety, and
business outcome. Hiring's vague "fair and accurate" becomes these two
measured thresholds.
6. Every rejected choice explained: C and D are real metrics for cost
and latency budgets, but neither measures rank quality or fairness.
E is the model's self-report: uncalibrated and prompt-injectable, never
a metric.
7. Exact limitation or tradeoff: subgroup labels raise privacy handling
needs. Groundedness checks cost a verification per claim.
8. Relevant evidence (with date): metric definition from lesson-D4-1
(§4), Oct 6 2026, subgroup evaluation from lesson-D5-5, Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins when the
budget binds. D wins when an SLA names latency. E wins never as a
metric.
10. Misconception tested: "one aggregate score proves fairness." It
hides subgroup harm. Measure per group.

## Q-M-27 (V2-D4.2)

**Scenario.** A fraud detector flags suspicious transactions. The team
built the eval set from last quarter's confirmed frauds. The model
scores 99% on it. A teammate asks how they know the judge's grades are
right.

**Question.** What is the missing eval practice?

**Options.**
A) A bigger model.
B) A held-out set the team never trains on, plus calibration of the
judge against human labels.
C) More confirmed frauds in the training set.
D) A faster grading script.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: eval framework gap.
2. Lifecycle stage: evaluation design.
3. Objective: trust the 99% score.
4. Hard constraints: the eval set may overlap training. The judge's
grades are unverified.
5. System layer: eval datasets and frameworks (V2-D4.2).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A buys strength for a measurement
problem, C feeds training not eval, D speeds grading without fixing
it.
8. Compare on objective: only B separates eval from training and checks
the grader.
9. Hidden dependencies: the holdout must mirror production, including
edge and adversarial cases.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "built the eval set from last quarter's
confirmed frauds... how they know the judge's grades are right."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Separates eval from training | No | Yes | No | No |
| Verifies the grader | No | Yes | No | No |

4. Why B satisfies the objective: the holdout the team never trains on
measures generalization, not memorization. Calibrating the judge
against human labels verifies the grades the 99% rests on.
5. Why B best meets the objective: V2-D4.2 requires representative,
edge, adversarial, and regression cases with holdouts, and the grading
ladder (code, then judge, then human) with judges calibrated against
human labels. B is the only option that follows it.
6. Every rejected choice explained: A upgrades the model while the
measurement is broken. C improves training. The question is about eval
trust. D makes bad grading faster.
7. Exact limitation or tradeoff: holdouts shrink the training pool, and
judge calibration needs human-labeled cases, which cost reviewer time.
8. Relevant evidence (with date): holdouts and judge calibration from
lesson-D4-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
the trace shows the model failing with full context. C wins when the
model underfits known fraud. D wins never as an eval fix.
10. Misconception tested: "a high score on our data proves quality."
Only a held-out set with a calibrated grader proves it.

## Q-M-28 (V2-D4.3)

**Scenario.** A team plans an A/B test of a new reranker. Claim: 1% lift
in booking conversion. Traffic: 400 sessions per day. The test plan
runs for one week.

**Question.** What is wrong with this plan?

**Options.**
A) Nothing. One week is standard.
B) The traffic cannot resolve a 1% lift in one week. Use offline
evaluation on the five drawers instead.
C) The reranker needs a bigger model first.
D) A/B tests never work for rerankers.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: experiment design flaw.
2. Lifecycle stage: evaluation.
3. Objective: test the 1% lift claim honestly.
4. Hard constraints: 400 sessions per day, 1% claimed lift, one-week
window.
5. System layer: A/B testing (V2-D4.3).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A ignores sample size, C answers the
wrong question, D is false.
8. Compare on objective: only B names the sample-size veto.
9. Hidden dependencies: the offline drawers must include the booking
conversion proxy metric.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "1% lift... 400 sessions per day... one
week."
3. Requirement-to-option matrix:

| Check | A | B | C | D |
|---|---|---|---|---|
| Computes sample adequacy | No | Yes | No | No |
| Offers a valid alternative | No | Yes | No | No |

4. Why B is right: 2,800 sessions cannot resolve a 1% lift. The test
would run for months and still wobble. V2-D4.3 demands sample size
before the test starts. The offline suite on representative, edge,
adversarial, malformed, and regression drawers still gates quality.
5. Why B best meets the objective: a test that cannot answer is theater.
B kills the theater and keeps the gate that works.
6. Every rejected choice explained: A treats one week as magic. Sample
math does not care about the calendar. C buys model strength for a
statistics problem. D is false: A/B tests work for rerankers with
enough traffic.
7. Exact limitation or tradeoff: offline eval cannot measure the true
business outcome. If the lift claim matters, the team needs more
traffic or a longer window, honestly priced.
8. Relevant evidence (with date): sample size and significance from
lesson-D4-3 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins with
40,000 sessions per day. C wins when the trace shows ranking failures
with full context. D wins never.
10. Misconception tested: "running the test is always informative." A
test without power informs no one.

## Q-M-29 (V2-D4.4)

**Scenario.** A contract Q&A bot gives wrong answers on paraphrased
questions. The trace shows the right clause chunk present in the
retrieved set. The answer still misstates the clause.

**Question.** Which layer failed, and what is the fix?

**Options.**
A) Retrieval failed. Rebuild the index.
B) The model layer failed. Fix the prompt or the model choice, or add a
verification gate. The chunk arrived and the model still failed.
C) The chunking failed. Make chunks bigger.
D) The evaluation failed. The answers are actually fine.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: layer diagnosis.
2. Lifecycle stage: operate and debug.
3. Objective: fix the failing component, not a proxy.
4. Hard constraints: the chunk is present, the answer is still wrong.
5. System layer: issue diagnosis (V2-D4.4).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A and C fix retrieval that the trace
clears, D denies the evidence.
8. Compare on objective: the evidence names the model layer.
9. Hidden dependencies: the verification gate needs the source chunk as
its check input.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the right clause chunk present in the
retrieved set. The answer still misstates the clause."
3. Requirement-to-option matrix:

| Evidence | A | B | C | D |
|---|---|---|---|---|
| Chunk present | Contradicts | Matches | Contradicts | Ignores |
| Answer wrong | Matches | Matches | Matches | Denies |

4. Why B is right: the trace clears retrieval (the chunk arrived) and
convicts the model (it had the facts and failed). The fix belongs at
the convicted layer: prompt, model choice, or a verification gate.
5. Why B best meets the objective: V2-D4.4 says fix the failing
component, not a proxy. Rebuilding the index is the classic proxy fix:
it costs a pipeline rebuild and changes nothing.
6. Every rejected choice explained: A rebuilds a working index. C
changes chunk size for a reasoning failure. D denies the user's
evidence. The answers are wrong.
7. Exact limitation or tradeoff: a verification gate adds per-answer
cost. A model upgrade adds per-call cost. Measure which holds the
floor cheaper.
8. Relevant evidence (with date): diagnose at the right layer from
lesson-D4-4 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
trace shows the chunk absent. C wins when chunks split the clause
mid-sentence. D wins never against evidence.
10. Misconception tested: "wrong answer means bad retrieval." The trace
decides the layer, not the symptom.

## Q-M-30 (V2-D4.5), Select TWO

**Scenario.** A document Q&A service costs $3,000 per month. The CFO
wants $1,800. Quality floor: 95% precision on cited answers, measured
weekly. Current precision: 97%.

**Question.** Which TWO levers cut cost while holding the floor? Select
TWO.

**Options.**
A) Prompt caching on the stable 6,000-token instruction prefix.
B) Tier routing: simple lookups to the Fast tier, hard reasoning stays
on the current tier.
C) Drop the grounding check to halve verification cost.
D) Halve the eval sample to save grading cost.
E) Remove the quality floor to open cheaper options.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: cost optimization under a floor (multi).
2. Lifecycle stage: operate and optimize.
3. Objective: cut $1,200 per month with precision at or above 95%.
4. Hard constraints: the 95% floor is measured weekly and must hold.
5. System layer: token and cost optimization (V2-D4.5).
6. Eliminate infeasible: all five are feasible.
7. Eliminate constraint-violating: C, D, and E attack the floor or its
measurement.
8. Compare on objective: A and B cut cost inputs, not quality inputs.
9. Hidden dependencies: routing needs a reliable difficulty classifier.
Caching needs prefix stability.
10. Verify: A and B. The rest break the floor.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "Quality floor: 95% precision on cited
answers, measured weekly."
3. Requirement-to-option matrix:

| Lever | A | B | C | D | E |
|---|---|---|---|---|---|
| Cuts real cost | Yes | Yes | Yes | No | Maybe |
| Holds the 95% floor | Yes | Yes | No | Hides drops | No |

4. Why A and B satisfy the objective: caching cuts the prefix token
bill. Routing cuts the per-call tier cost on easy questions. Neither
touches the grounding check or the measurement, so the floor holds.
5. Why A and B best meet the objective: V2-D4.5 says measure per stage,
then cut oversized context, caching, routing, and call elimination,
while holding quality and safety floors. A and B are the textbook
levers.
6. Every rejected choice explained: C drops the check that holds the
floor. Floors outrank speed and savings. D shrinks the sample so drops
go undetected: measurement theater. E removes the floor itself, which
is surrender, not optimization.
7. Exact limitation or tradeoff: the router can misclassify, and the
cache needs prefix hygiene. Both need monitoring.
8. Relevant evidence (with date): per-stage measurement and floor
discipline from lesson-D4-5 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins never
while the floor stands. D wins never. E wins when the business
drops the floor explicitly and owns the risk.
10. Misconception tested: "any cost cut is an optimization." Only cuts
that hold the floor count. The rest are quality cuts in disguise.

## Q-M-31 (V2-D4.6)

**Scenario.** A loan-approval assistant runs in production. Approval
rates drift upward over two months. No alert fires. The team learns about
it from a customer complaint.

**Question.** What gap exists in production monitoring?

**Options.**
A) A bigger model.
B) Drift detection on the approval rate with an alert routed to a named
owner, plus a regression suite on representative eval data.
C) More logs.
D) A second assistant for redundancy.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: production monitoring gap.
2. Lifecycle stage: operate.
3. Objective: catch drift before customers do.
4. Hard constraints: two months of drift, no alert, complaint-driven
discovery.
5. System layer: production monitoring (V2-D4.6).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A buys strength for a monitoring gap,
C adds volume without detection, D doubles the unmonitored system.
8. Compare on objective: only B names detection, alerting, and
ownership.
9. Hidden dependencies: the drift metric needs a baseline window and a
threshold.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Approval rates drift upward over two
months. No alert fires."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Detects the drift | No | Yes | No | No |
| Alerts a named owner | No | Yes | No | No |
| Checks against representative data | No | Yes | No | No |

4. Why B satisfies the objective: drift detection watches the approval
rate against its baseline. The alert with a named owner turns detection
into response. The regression suite on representative data says whether
the drift is a quality change or a population change.
5. Why B best meets the objective: V2-D4.6 requires operational metrics,
drift detection, regression suites, and alerts with owners. The
scenario's system has none of the four.
6. Every rejected choice explained: A upgrades the model while the gap
is the lack of watches. C adds logs nobody watches. The complaint already proved
that. D runs two assistants with the same blind spot.
7. Exact limitation or tradeoff: thresholds need tuning to avoid alert
fatigue. The owner needs runbook authority to act.
8. Relevant evidence (with date): drift detection and alert ownership
from lesson-D4-6 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
trace shows model failures. C wins when a hop logs nothing. D wins
never for monitoring.
10. Misconception tested: "the dashboard is the monitoring." Detection
plus alert plus owner is the monitoring. A dashboard nobody watches is
furniture.

## Q-M-32 (V2-D4.2)

**Scenario.** A phishing-triage bot classifies employee-reported emails.
The eval set has 500 real phishing emails and 500 clean emails. It
scores 98%. In production, an attacker submits a crafted email that
looks clean to the classifier but carries a malicious link. The bot
passes it.

**Question.** Which eval drawer is absent?

**Options.**
A) Representative cases.
B) Adversarial cases: inputs crafted to fool the classifier.
C) Malformed cases.
D) Regression cases.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: eval drawer gap.
2. Lifecycle stage: evaluation design.
3. Objective: name the drawer that would have caught the attack.
4. Hard constraints: the attack email was crafted to fool the
classifier.
5. System layer: eval datasets (V2-D4.2).
6. Eliminate infeasible: all four are real drawer names.
7. Eliminate constraint-violating: A, C, and D describe cases the set
already covers or that miss the attack shape.
8. Compare on objective: only B names crafted-to-fool inputs.
9. Hidden dependencies: the adversarial drawer needs red-team-crafted
cases, refreshed as attacks evolve.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "a crafted email that looks clean to the
classifier but carries a malicious link."
3. Requirement-to-option matrix:

| Drawer | Covers crafted-to-fool inputs |
|---|---|
| Representative | No |
| Adversarial | Yes |
| Malformed | No |
| Regression | No |

4. Why B is right: the five drawers are representative, edge,
adversarial, malformed, and regression. The attack is the textbook
adversarial case: an input designed to beat the classifier. The eval
set's 1,000 honest emails never contained one.
5. Why B best meets the objective: V2-D4.2 requires the adversarial
drawer for any classifier facing attackers. The 98% measured the wrong
threat.
6. Every rejected choice explained: A covers normal traffic, which the
set has. C covers broken inputs, not crafted ones. D covers past bugs,
not new attacks.
7. Exact limitation or tradeoff: adversarial cases need red-team effort
and refresh. Attackers adapt.
8. Relevant evidence (with date): the five eval drawers from
lesson-D4-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
set misses a whole traffic class. C wins when crashes come from broken
MIME. D wins when an old bug returns.
10. Misconception tested: "high accuracy means attacker-proof." Accuracy
on honest data says nothing about crafted data.

## Q-M-33 (V2-D4.4)

**Scenario.** A research assistant's p95 latency jumps from 4 s to 11 s
over three weeks. Nothing in the code changed. Per-stage measurement
shows: retrieval 1 s (unchanged), model reasoning 2.5 s (unchanged),
context assembly 7 s (was 0.5 s).

**Question.** Which layer failed, and what is the fix?

**Options.**
A) The model slowed. Upgrade the tier.
B) The context layer failed: assembly now loads far more tokens per
call. Fix the context growth (retrieval scoping, compaction, dedupe).
C) Retrieval failed. Rebuild the index.
D) The network failed. Add retries.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: latency layer diagnosis.
2. Lifecycle stage: operate and debug.
3. Objective: name the layer the measurement convicts.
4. Hard constraints: no code changed, assembly went 0.5 s to 7 s,
others flat.
5. System layer: issue diagnosis (V2-D4.4, V2-D4.5).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A, C, and D contradict the flat
measurements.
8. Compare on objective: the measurement names context assembly.
9. Hidden dependencies: the growth source (which data now loads) must
be found before scoping.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "context assembly 7 s (was 0.5 s)...
retrieval 1 s (unchanged), model reasoning 2.5 s (unchanged)."
3. Requirement-to-option matrix:

| Layer | Changed | Fix matches |
|---|---|---|
| Model | No | A fixes the wrong layer |
| Context | Yes, 0.5 to 7 s | B |
| Retrieval | No | C fixes the wrong layer |
| Network | No evidence | D invents a cause |

4. Why B is right: per-stage measurement is the V2-D4.4 habit. Assembly
is the only stage that moved. Context growth (more tokens assembled per
call) is the convicted cause. Retrieval scoping, compaction, and dedupe
are its fixes.
5. Why B best meets the objective: fix the failing component, not a
proxy. A model upgrade would cost more per call forever and leave the
7-second assembly untouched.
6. Every rejected choice explained: A upgrades a flat stage. C rebuilds
a flat index. D invents a network cause with no evidence.
7. Exact limitation or tradeoff: scoping retrieval can drop a useful
old document. The index quality bounds the fix.
8. Relevant evidence (with date): per-stage measurement and diagnose at
the right layer from lesson-D4-4 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
reasoning time jumps with context flat. C wins when retrieval time
jumps. D wins when timeouts cluster on one dependency.
10. Misconception tested: "latency spike means the model got slow." The
stages decide. Measure first.

## Q-M-34 (V2-D5.1)

**Scenario.** A pharmacy refill bot approves repeat prescriptions. A
dosage ambiguity appears: the label says "take as directed" with no
number. The bot must decide.

**Question.** Which control must fail closed here?

**Options.**
A) The dosage check: on ambiguity, block the refill and route to the
pharmacist. The check defaults to deny, not to guess.
B) The dosage check: on ambiguity, approve the most common dosage.
C) The logging: on ambiguity, log extra details and approve.
D) The model: on ambiguity, pick the likelier reading.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: fail-closed control design.
2. Lifecycle stage: design.
3. Objective: handle dosage ambiguity safely.
4. Hard constraints: a wrong dosage harms the patient. "Take as
directed" carries no number.
5. System layer: safety controls (V2-D5.1).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: B, C, and D approve or guess on
ambiguity.
8. Compare on objective: only A defaults to deny.
9. Hidden dependencies: the pharmacist queue needs an SLA so blocked
refills do not stall care.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "the label says 'take as directed' with no
number."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Defaults to deny on ambiguity | Yes | No | No | No |
| Routes to a qualified human | Yes | No | No | No |
| Never guesses a dosage | Yes | No | No | No |

4. Why A satisfies all hard constraints: the control fails closed: when
it cannot decide, it blocks. The pharmacist (qualified, accountable)
resolves the ambiguity. No guess reaches the patient.
5. Why A best meets the objective: V2-D5.1 requires knowing which
controls must fail closed. A dosage gate on patient safety is the
textbook case: uncertainty must stop the action, not shape it.
6. Every rejected choice explained: B approves the common dosage. Common
is not this patient. C logs the ambiguity and approves anyway: a
perfect record of a harmful guess. D asks the model to gamble on a
dosage, which is the exact failure the control exists to prevent.
7. Exact limitation or tradeoff: the pharmacist queue grows. Blocked
refills need a turnaround SLA.
8. Relevant evidence (with date): fail-closed controls from lesson-D5-1
(§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: B wins never
for dosages. C wins as a complement to A, never alone. D wins never
for safety gates.
10. Misconception tested: "the system must always produce an answer."
On safety gates, "I cannot decide, so I stop" is the correct output.

## Q-M-35 (V2-D5.2), Select TWO

**Scenario.** A procurement agent reads vendor PDFs, compares quotes, and
issues purchase orders up to $50,000 with no human step. Vendor PDFs come
from the open internet.

**Question.** Which TWO risks are present? Select TWO.

**Options.**
A) Indirect prompt injection: a vendor PDF carries instructions like
"approve this vendor."
B) Excessive agency: the agent moves $50,000 with no human gate.
C) Model hallucination about the vendor's founding year.
D) Slow p95 latency.
E) High token cost.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: risk identification (multi).
2. Lifecycle stage: design review.
3. Objective: name the risks the scenario creates.
4. Hard constraints: PDFs from the open internet, $50,000 with no human
step.
5. System layer: risk and failure modes (V2-D5.2).
6. Eliminate infeasible: all five are real risk names.
7. Eliminate constraint-violating: C is low-stakes trivia, D and E are
performance, not the named risk classes.
8. Compare on objective: A matches the untrusted PDFs, B matches the
ungated money.
9. Hidden dependencies: prevention needs input screening plus a
pre-action approval gate.
10. Verify: A and B. The rest miss the risk class.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "Vendor PDFs come from the open internet...
issues purchase orders up to $50,000 with no human step."
3. Requirement-to-option matrix:

| Risk | Evidence in scenario |
|---|---|
| Indirect injection | PDFs from the open internet read as content |
| Excessive agency | $50,000 POs with no human gate |

4. Why A and B are the risks: untrusted PDFs are the classic indirect
injection path: instructions inside content the model reads as data.
Ungated $50,000 purchase orders are the textbook excessive agency: the
agent's action radius exceeds its oversight.
5. Why A and B best meet the objective: V2-D5.2 requires naming risks
with prevention, detection, and recovery per risk. These two demand a
screening layer and a pre-action approval gate.
6. Every rejected choice explained: C is a hallucination about trivia.
The founding year moves no money. D and E are performance concerns,
not safety risks. They belong to D4, not D5.
7. Exact limitation or tradeoff: the approval gate adds latency to
procurement. The screening layer needs maintenance against new
injection shapes.
8. Relevant evidence (with date): indirect injection and excessive
agency from lesson-D5-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins when the
founding year appears in a filed report. D wins when an SLA binds. E
wins when the budget binds.
10. Misconception tested: "reading a PDF is passive." For an agent with
tools, reading is an instruction channel.

## Q-M-36 (V2-D5.3)

**Scenario.** A city permit bot processes demolition permits. A wrong
approval lets a crew demolish a protected historic building. The
demolition is irreversible.

**Question.** Which human-in-the-loop shape fits?

**Options.**
A) Post-action sampled review of issued permits.
B) Pre-action approval: a qualified reviewer sees the full application,
the historic registry check, and the exact demolition order, then
approves or denies before anything issues.
C) No review. The bot is fast and usually right.
D) Annual review of the permit statistics.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: review shape selection.
2. Lifecycle stage: design.
3. Objective: prevent irreversible wrongful demolition.
4. Hard constraints: a wrong approval destroys a historic building.
Demolition is irreversible.
5. System layer: human-in-the-loop validation (V2-D5.3).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A reviews after the building falls,
C and D are not controls.
8. Compare on objective: only B gates before the irreversible action.
9. Hidden dependencies: the reviewer needs real decision context, not a
yes button.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "A wrong approval lets a crew demolish a
protected historic building. The demolition is irreversible."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Acts before the irreversible step | No | Yes | No | No |
| Reviewer sees full context | Maybe | Yes | No | No |
| Can stop the harm | No | Yes | No | No |

4. Why B satisfies all hard constraints: the gate sits before the
irreversible action, and the reviewer sees the application, the
registry check, and the order: real decision context.
5. Why B best meets the objective: V2-D5.3 keys review strength to
consequence, reversibility, and regulation. Irreversible plus historic
protection equals pre-action approval with full context.
6. Every rejected choice explained: A is post-action review on an
irreversible act: the building is already gone. C is speed over safety
with no control. D reviews statistics yearly. No single demolition is
stopped.
7. Exact limitation or tradeoff: the reviewer queue needs staffing and
an SLA. Permits slow down.
8. Relevant evidence (with date): review strength keyed to consequence
and reversibility from lesson-D5-3 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins for
reversible permits (paint colors). C wins never as a control. D wins
as a complement to B, never alone.
10. Misconception tested: "review is review." Timing relative to
irreversibility is the whole decision.

## Q-M-37 (V2-D5.4)

**Scenario.** A support bot serves EU customers. Tickets contain names,
order histories, and payment references. EU data must stay in the EU.
A regulator may ask for proof.

**Question.** What does the compliance design need?

**Options.**
A) A note in the README that data stays in the EU.
B) The full chain per requirement: requirement to control to owner to
evidence to cadence. EU residency gets a control (EU-region storage and
processing), an owner, stored evidence, and a review cadence.
C) A bigger model hosted anywhere.
D) Deleting all tickets after one day.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: compliance design.
2. Lifecycle stage: design.
3. Objective: meet GDPR residency with proof.
4. Hard constraints: EU data stays in the EU. The regulator may ask for
proof.
5. System layer: regulatory compliance (V2-D5.4).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A is a note, not a control. C ignores
residency. D deletes evidence the business needs.
8. Compare on objective: only B builds the provable chain.
9. Hidden dependencies: the evidence must show actual storage locations,
not intentions.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "EU data must stay in the EU. A regulator
may ask for proof."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Names the control | No | Yes | No | No |
| Names the owner | No | Yes | No | No |
| Produces evidence | No | Yes | No | No |
| Sets a review cadence | No | Yes | No | No |

4. Why B satisfies all hard constraints: the residency requirement maps
to an EU-region control, a named owner, stored evidence of actual
storage locations, and a cadence that re-checks. The regulator gets
proof, not promises.
5. Why B best meets the objective: V2-D5.4 runs requirement to control
to owner to evidence to cadence. B is the chain. The rest are fragments.
6. Every rejected choice explained: A documents an intention. Auditors
do not accept intentions. C hosts anywhere, which violates residency
by design. D deletes tickets the business and the regulator both need.
Retention policy is not "delete everything fast."
7. Exact limitation or tradeoff: the chain needs maintenance: region
configs drift, owners change, evidence goes stale without the cadence.
8. Relevant evidence (with date): the five-link compliance chain from
lesson-D5-4 (§4), Oct 6 2026. Architectural implications only, not legal
advice.
9. Counterfactual where each plausible alternative wins: A wins never
for a regulator. C wins when no residency rule applies. D wins when a
retention rule truly demands one-day deletion and the business agrees.
10. Misconception tested: "we comply because we intend to." Compliance
is the chain with evidence. Intent is not a link.

## Q-M-38 (V2-D5.5), Select TWO

**Scenario.** A resume-screening assistant advances candidates to
interviews. The aggregate advance rate looks balanced. A subgroup audit
shows one group advances at half the rate of the others.

**Question.** Which TWO actions address this? Select TWO.

**Options.**
A) Evaluate and report metrics per subgroup, with a fairness floor per
group, not one aggregate.
B) Audit the training and eval data for the bias source, then fix the
data or the decision rule.
C) Publish the aggregate rate as proof of fairness.
D) Remove the subgroup labels so no one can measure the gap.
E) Trust the model's confidence scores.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: fairness response (multi).
2. Lifecycle stage: operate and remediate.
3. Objective: close the subgroup gap with evidence.
4. Hard constraints: one group advances at half the rate. The aggregate
hides it.
5. System layer: responsible AI (V2-D5.5).
6. Eliminate infeasible: all five are feasible actions.
7. Eliminate constraint-violating: C defends the hiding aggregate, D
destroys the measurement, E trusts an uncalibrated signal.
8. Compare on objective: A measures per group, B finds and fixes the
cause.
9. Hidden dependencies: the fairness floor needs a business and legal
sign-off.
10. Verify: A and B. The rest hide or ignore the gap.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "The aggregate advance rate looks balanced.
A subgroup audit shows one group advances at half the rate."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Measures per group | Yes | No | No | No | No |
| Finds the cause | No | Yes | No | No | No |
| Hides the gap | No | No | Yes | Yes | Yes |

4. Why A and B satisfy the objective: per-group metrics with a floor
make the gap visible and blockable. The data audit finds whether the
bias lives in the training data, the labels, or the rule, so the fix
lands at the cause.
5. Why A and B best meet the objective: V2-D5.5 requires evaluation
across subgroups, not aggregate only, plus accountability and
traceability. A is the measurement. B is the accountability.
6. Every rejected choice explained: C uses the aggregate as proof. The
scenario proves the aggregate lies. D deletes the labels: the gap
persists, now unmeasurable, which is worse. E trusts confidence, which
is uncalibrated and irrelevant to fairness.
7. Exact limitation or tradeoff: subgroup labels need privacy handling.
The data fix may require relabeling effort.
8. Relevant evidence (with date): subgroup evaluation from lesson-D5-5
(§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins never
as proof. D wins never. Measurement is the duty. E wins never as a
fairness signal.
10. Misconception tested: "balanced overall means fair." Aggregates hide
subgroup harm. The audit proved it here.

## Q-M-39 (V2-D5.1)

**Scenario.** A tutoring bot serves children aged 8 to 12. Children type
free text. Risks: children share personal details, and some messages
hint at self-harm.

**Question.** Which guardrail design fits?

**Options.**
A) Input screening in code: detect personal details and self-harm
signals, redact or block before the model sees them, and route
self-harm signals to the safety protocol.
B) A system prompt asking children not to share personal details.
C) Log the chats for later review.
D) A longer context window.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: guardrail design for a vulnerable population.
2. Lifecycle stage: design.
3. Objective: protect children in free-text chat.
4. Hard constraints: ages 8 to 12, personal details and self-harm
signals in input.
5. System layer: guardrails and safety controls (V2-D5.1).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: B trusts children to self-censor, C
reviews after exposure, D is irrelevant.
8. Compare on objective: only A screens before the model sees the text.
9. Hidden dependencies: the self-harm protocol needs a qualified human
path, not just a block.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "children aged 8 to 12... share personal
details... hint at self-harm."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Screens before model exposure | Yes | No | No | No |
| Handles self-harm with a protocol | Yes | No | No | No |
| Does not rely on child behavior | Yes | No | Yes | Yes |

4. Why A satisfies all hard constraints: the code screen runs before the
model, so personal details never enter the context and self-harm
signals trigger the safety protocol immediately.
5. Why B best meets the objective: V2-D5.1 layers model safeguards,
input and output screening, and deterministic controls, with fail-closed
defaults. A is the input-screening layer done in code.
6. Every rejected choice explained: B asks 8-year-olds to self-censor.
That is not a control. C reviews after the model already saw the
details. D adds context window to a safety problem.
7. Exact limitation or tradeoff: screening can over-block innocent
messages. The block list needs tuning and a human appeal path.
8. Relevant evidence (with date): input and output screening from
lesson-D5-1 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: B wins as a
complement to A, never alone. C wins for low-stakes adult chat. D wins
never for safety.
10. Misconception tested: "a polite prompt protects children." Code
screens. Prompts suggest.

## Q-M-40 (V2-D5.2)

**Scenario.** A team adopts a third-party MCP server for document search.
The server is closed source. It requests broad file-system read access.
The vendor updates it silently every week.

**Question.** What is the primary risk, and what is the first mitigation?

**Options.**
A) Cost. Negotiate the price.
B) Supply-chain risk: unreviewed code with broad access updating
silently. First mitigation: pin the version, scope its file access to
the document directory, and review each update before deploy.
C) Latency. Add caching.
D) Model quality. Upgrade the tier.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: supply-chain risk response.
2. Lifecycle stage: design to operate.
3. Objective: bound the third-party server's risk.
4. Hard constraints: closed source, broad file access, silent weekly
updates.
5. System layer: risk management (V2-D5.2).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A, C, and D answer non-risks.
8. Compare on objective: only B names the risk and bounds it.
9. Hidden dependencies: the review needs someone who can read the
update diff or a sandbox to test it.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "closed source... broad file-system read
access... updates it silently every week."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Names the supply-chain risk | No | Yes | No | No |
| Bounds file access | No | Yes | No | No |
| Stops silent updates | No | Yes | No | No |

4. Why B satisfies the objective: version pinning stops silent changes.
Scoped file access applies least privilege. Per-update review makes
each change a decision. The three together convert an open pipe into a
governed dependency.
5. Why B best meets the objective: V2-D5.2 lists supply-chain risk with
prevention, detection, and recovery. B is prevention (pin, scope) plus
detection (review).
6. Every rejected choice explained: A negotiates price on a security
risk. C caches a risk. D upgrades the model while the server reads the
whole file system.
7. Exact limitation or tradeoff: review slows updates. The team accepts
slower features for a bounded dependency.
8. Relevant evidence (with date): supply-chain risk from lesson-D5-2
(§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
server is first-party and reviewed. C wins when the server is trusted
and slow. D wins when search quality is the gap.
10. Misconception tested: "a vendor tool is our tool." Third-party code
is supply chain. Govern it like one.

## Q-M-41 (V2-D6.1)

**Scenario.** A port customs broker wants a bot that clears shipments
"fast and cheap." Daily volume is 600 shipments. The compliance team
requires every clearance decision logged with the rule cited.

**Question.** What is the first discovery output?

**Options.**
A) A vendor shortlist.
B) Measurable requirements: "fast" becomes clearance p95 under 10
minutes, "cheap" becomes cost per clearance under $0.40, plus the
logging requirement with its fields, owner, and volume of 600 per day.
C) A system prompt draft.
D) A model tier choice.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: discovery output.
2. Lifecycle stage: discovery.
3. Objective: turn adjectives into measurable requirements.
4. Hard constraints: compliance logging with cited rules, 600 per day.
5. System layer: structured discovery (V2-D6.1).
6. Eliminate infeasible: all four are producible.
7. Eliminate constraint-violating: A, C, and D skip discovery and build
on adjectives.
8. Compare on objective: only B converts the adjectives and records the
compliance shape.
9. Hidden dependencies: the p95 and cost numbers need stakeholder
sign-off, not invention.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "'fast and cheap'... every clearance
decision logged with the rule cited."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Converts adjectives to numbers | No | Yes | No | No |
| Captures the logging requirement | No | Yes | No | No |
| Records volume and owner | No | Yes | No | No |

4. Why B satisfies the objective: discovery ends when outcomes,
constraints, volume, and compliance needs are measurable and owned.
B lists all four. The numbers are explicit and therefore arguable.
5. Why B best meets the objective: V2-D6.1 turns adjectives into
measurable requirements and records prohibited behaviors, workflows,
cost limits, and owners. B is that record.
6. Every rejected choice explained: A shops for vendors before knowing
what to buy. C drafts a prompt before the requirements exist. D picks
a tier before the cost limit is a number.
7. Exact limitation or tradeoff: the numbers in B are draft targets.
Stakeholders must ratify them or they are fiction.
8. Relevant evidence (with date): structured discovery from lesson-D6-1
(§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins after
requirements are signed. C wins after the design is set. D wins after
the cost limit is numeric.
10. Misconception tested: "discovery means stakeholder chats."
Discovery outputs measurable, owned requirements.

## Q-M-42 (V2-D6.2)

**Scenario.** An architect must present two options to two audiences:
the CFO and the security team. Option X is cheaper but stores data with
a new vendor. Option Y costs more and keeps data in-house.

**Question.** How should the message differ?

**Options.**
A) Same slide deck for both audiences.
B) CFO: cost, risk in dollars, reversal cost, and compliance impact per
option. Security: threat model, vendor trust boundary, data controls,
and audit evidence per option.
C) Tell the CFO only the price and the security team only the vendor
name.
D) Recommend X to the CFO and Y to security.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: stakeholder communication.
2. Lifecycle stage: design communication.
3. Objective: give each audience what it decides on.
4. Hard constraints: one decision, two audiences with different duties.
5. System layer: architecture communication (V2-D6.2).
6. Eliminate infeasible: all four are deliverable.
7. Eliminate constraint-violating: A ignores audience duties, C
withholds material facts, D splits the recommendation.
8. Compare on objective: only B adapts benefit, cost, risk, and
compliance per audience.
9. Hidden dependencies: the numbers behind both messages must match.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the CFO and the security team... cheaper
but stores data with a new vendor."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Adapts to audience duty | No | Yes | No | No |
| Covers cost, risk, reversal, compliance | Maybe | Yes | No | No |
| One consistent recommendation base | Yes | Yes | No | No |

4. Why B satisfies the objective: the CFO decides on money and risk in
dollars. Security decides on threat model and controls. B gives each
the axes of its duty with the same underlying facts.
5. Why B best meets the objective: V2-D6.2 communicates benefit, cost,
risk, reversal cost, and compliance impact per option, adapted to exec,
engineering, security, legal, and product. B executes the rule.
6. Every rejected choice explained: A gives security dollar slides and
the CFO threat-model slides. Neither decides well. C withholds material
facts from fiduciaries. D tells two stories. The first joint meeting
exposes the split.
7. Exact limitation or tradeoff: two messages need one fact base, or
the audiences decide on different realities.
8. Relevant evidence (with date): audience-adapted trade-off
communication from lesson-D6-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins for one
audience. C wins never for fiduciaries. D wins never. One
recommendation, honestly held.
10. Misconception tested: "good news for everyone." Different duties
need different axes, same facts.

## Q-M-43 (V2-D6.3), Select TWO

**Scenario.** A triage bot routes IT tickets. The vendor promises "99%
accuracy." The CIO asks what SLA the team can honestly sign.

**Question.** Which TWO statements set honest expectations? Select TWO.

**Options.**
A) No fixed accuracy promise. Report measured precision and recall per
ticket class with the eval date, and re-measure monthly.
B) Named review triggers: new ticket classes, drift beyond the
threshold, or precision drops route to human review and re-evaluation.
C) "99% accuracy guaranteed on all tickets, forever."
D) "The bot is AI, so occasional errors are magic, not our problem."
E) A latency SLA only, with no quality terms.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: expectation alignment (multi).
2. Lifecycle stage: handoff to production.
3. Objective: sign an SLA the team can honestly keep.
4. Hard constraints: probabilistic system, vendor overpromises, CIO
needs a signature.
5. System layer: feedback and expectation alignment (V2-D6.3).
6. Eliminate infeasible: all five are statable.
7. Eliminate constraint-violating: C promises the unpromisable, D
abdicates, E ignores quality.
8. Compare on objective: A makes quality measurable and dated, B makes
breaches actionable.
9. Hidden dependencies: the monthly re-measurement needs the eval
pipeline to stay live.
10. Verify: A and B. The rest are dishonest or empty.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "The vendor promises '99% accuracy.'...
what SLA the team can honestly sign."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Measurable quality | Yes | No | Claims | No | No |
| Dated and re-measured | Yes | No | No | No | No |
| Breach has a consequence | No | Yes | No | No | No |

4. Why A and B satisfy the objective: measured per-class precision with
a date replaces the vendor's slogan. Review triggers with consequences
say what happens when reality moves. Together they are a realistic SLA
for a probabilistic system.
5. Why A and B best meet the objective: V2-D6.3 demands measurable
quality, realistic SLAs for probabilistic systems, review triggers, and
breach consequences. A and B are those four, split across two options.
6. Every rejected choice explained: C signs a forever-guarantee on a
probabilistic system. The first drift breaks it. D is abdication dressed
as honesty. E signs latency while quality (the actual risk) goes
unmentioned.
7. Exact limitation or tradeoff: monthly re-measurement costs eval
effort. The triggers need thresholds that avoid false alarms.
8. Relevant evidence (with date): realistic SLAs and review triggers
from lesson-D6-3 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins never
for probabilistic systems. D wins never. E wins when quality is
contractually out of scope and latency is the product.
10. Misconception tested: "the vendor's number is our SLA." Only
measured, dated, re-measured numbers are signable.

## Q-M-44 (V2-D6.4)

**Scenario.** A team pins the model version for the catalog agent after
the regression suite passes. Six months later a new engineer asks why
this version and not the newer one.

**Question.** Which record answers her?

**Options.**
A) The chat log where the team discussed it.
B) An ADR: the decision and date, the alternatives considered and why
each lost, key assumptions, trade-offs, the owner, and the evidence
(the regression results).
C) The model ID in the config file.
D) A Slack thread from the release week.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: architecture documentation.
2. Lifecycle stage: handoff and maintenance.
3. Objective: make the decision answerable without the original
meeting.
4. Hard constraints: six months later, original team may be gone.
5. System layer: ADRs (V2-D6.4).
6. Eliminate infeasible: all four exist as artifacts.
7. Eliminate constraint-violating: A, C, and D lack the decision
rationale.
8. Compare on objective: only B records decision, alternatives, and
evidence.
9. Hidden dependencies: the ADR needs the regression results attached,
not referenced vaguely.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Six months later a new engineer asks why
this version and not the newer one."
3. Requirement-to-option matrix:

| Field | A | B | C | D |
|---|---|---|---|---|
| Decision and date | Maybe | Yes | Partial | Maybe |
| Alternatives and rejections | No | Yes | No | Maybe |
| Owner and evidence | No | Yes | No | No |

4. Why B satisfies the objective: the ADR holds the decision, its date,
the rejected alternatives with reasons, assumptions, trade-offs,
owner, and the regression evidence. The engineer gets the full answer
without the meeting.
5. Why B best meets the objective: V2-D6.4 requires ADRs that make the
architecture successor-operable. B is the ADR. The rest are fragments.
6. Every rejected choice explained: A is a chat log: searchable, not
structured, and it rots. C shows what was pinned, never why. D is a
thread: it scrolls away and names no owner.
7. Exact limitation or tradeoff: ADRs need writing discipline. A stale
ADR (never updated when the decision changes) misleads.
8. Relevant evidence (with date): ADR fields from lesson-D6-4 (§4), Oct
6 2026.
9. Counterfactual where each plausible alternative wins: A wins never
as the record. C wins as a pointer to the ADR, never alone. D wins
never.
10. Misconception tested: "the config is the documentation." Config
says what. The ADR says why.

## Q-M-45 (V2-D6.5)

**Scenario.** A team builds monitoring dashboards and alert rules for a
support bot while discovery is still open: no measurable requirements,
no named owner, no compliance review.

**Question.** What is wrong?

**Options.**
A) Nothing. Monitoring early is good practice.
B) The team substitutes later-phase work for unfinished discovery.
Monitoring needs requirements and owners to watch. Without them the
dashboards watch nothing meaningful.
C) The dashboards need more colors.
D) Discovery should be skipped to save time.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: lifecycle phase judgment.
2. Lifecycle stage: across phases.
3. Objective: name the phase error.
4. Hard constraints: discovery is open: no requirements, no owner, no
compliance review.
5. System layer: lifecycle phases (V2-D6.5).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A blesses the error, C is cosmetic,
D inverts the fix.
8. Compare on objective: only B names the substitution.
9. Hidden dependencies: none. The phase order is the point.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "while discovery is still open: no
measurable requirements, no named owner, no compliance review."
3. Requirement-to-option matrix:

| Check | A | B | C | D |
|---|---|---|---|---|
| Names the phase error | No | Yes | No | No |
| Explains why monitoring fails here | No | Yes | No | No |

4. Why B is right: V2-D6.5 runs discovery, design, handoff, monitoring,
iteration, and forbids substituting later-phase work for unfinished
earlier phases. Alerts need thresholds (requirements) and responders
(owners). Without them the dashboards are decoration.
5. Why B best meets the objective: the phase error is the whole story.
Monitoring without requirements cannot alert. Without owners, alerts
page nobody.
6. Every rejected choice explained: A mistakes motion for progress. C
is cosmetic. D proposes skipping the phase whose absence caused the
problem.
7. Exact limitation or tradeoff: none. The fix is to finish discovery
first, which takes calendar time the team wanted to skip.
8. Relevant evidence (with date): lifecycle phases and no phase
substitution from lesson-D6-5 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins when
discovery is closed and requirements are signed. C wins never. D wins
never.
10. Misconception tested: "any progress is good progress." Progress in
the wrong phase is rework with a dashboard.

## Q-M-46 (V2-D6.2)

**Scenario.** An architect compares RAG and fine-tuning for a policy
assistant. The policies update monthly. Stakeholders ask which choice is
easier to reverse.

**Question.** What is the correct reversal-cost comparison?

**Options.**
A) Fine-tuning is easier to reverse: just retrain.
B) RAG is easier to reverse: swap or re-ingest documents without
retraining. Fine-tuning reversal means retraining or rollback of model
weights with new evals.
C) Both reverse with one config flag.
D) Reversal cost does not matter.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: trade-off communication (reversal cost).
2. Lifecycle stage: design communication.
3. Objective: compare reversal cost honestly.
4. Hard constraints: policies update monthly. Stakeholders decide on
the comparison.
5. System layer: architecture decisions and trade-offs (V2-D6.2).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A inverts the costs, C is false, D
ignores a decision axis.
8. Compare on objective: only B prices both reversals.
9. Hidden dependencies: the RAG reversal still needs re-ingest and a
regression check.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The policies update monthly... which
choice is easier to reverse."
3. Requirement-to-option matrix:

| Comparison | A | B | C | D |
|---|---|---|---|---|
| RAG reversal priced | No | Yes | No | No |
| Fine-tune reversal priced | Wrong | Yes | No | No |

4. Why B is right: reversing RAG means re-ingesting or swapping
documents: minutes to hours, no training. Reversing fine-tuning means
retraining or rolling back weights plus re-running evals: hours to days
with new risk. Monthly policy updates make this gap recur monthly.
5. Why B best meets the objective: V2-D6.2 requires benefit, cost, risk,
and reversal cost per option. B is the only option that states both
reversal costs.
6. Every rejected choice explained: A calls retraining easy. It is the
expensive path. C invents a flag that does not exist. D drops a
required axis: stakeholders cannot decide without it.
7. Exact limitation or tradeoff: RAG reversal still needs the re-ingest
pipeline and a regression gate. "Easier" is not "free."
8. Relevant evidence (with date): reversal cost as a trade-off axis from
lesson-D6-2 (§4), Oct 6 2026, RAG vs fine-tuning from lesson-D3-5, Oct
6 2026.
9. Counterfactual where each plausible alternative wins: A wins when the
training pipeline is one click and the document set is huge. C wins
never. D wins never for stakeholders.
10. Misconception tested: "the better option has no reversal cost."
Every option has one. Name it.

## Q-M-47 (V2-D7.1)

**Scenario.** A 30-person consultancy uses Claude Code on client repos.
Client secrets live in `.env` files. The team lead proposes a CLAUDE.md
note: "Never read client secrets."

**Question.** What is the correct team configuration?

**Options.**
A) The CLAUDE.md note is enough for 30 people.
B) Enforceable permissions in the committed settings: deny rules on
secret paths (`.env`, key files), plus hooks that block secret exfil,
with CLAUDE.md kept for workflow guidance only.
C) No configuration. Trust the team.
D) A longer CLAUDE.md note with the rule in bold.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: team tool configuration.
2. Lifecycle stage: enablement.
3. Objective: protect client secrets across 30 people.
4. Hard constraints: client secrets in repos, 30 users, secrets must
never be read or exfiltrated.
5. System layer: Claude Code team config (V2-D7.1).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A, C, and D rely on guidance or
trust.
8. Compare on objective: only B enforces in code.
9. Hidden dependencies: the deny rules need tests proving they fire,
and a legitimate path for approved secret use.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Client secrets live in `.env` files...
'Never read client secrets.'"
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Blocks the read in code | No | Yes | No | No |
| Blocks exfiltration | No | Yes | No | No |
| Auditable enforcement | No | Yes | No | No |

4. Why B satisfies all hard constraints: deny rules run before the tool
and block the read. Hooks catch exfil paths. The committed settings
apply to all 30 clones. Guidance stays in CLAUDE.md where it belongs.
5. Why B best meets the objective: V2-D7.1 is explicit: instructions vs
enforceable permissions, and never CLAUDE.md alone for controls. B is
the only option that separates the two.
6. Every rejected choice explained: A is the sign-not-lock trap at team
scale: 30 people times model non-obedience. C is no control at all. D
is A with formatting. Bold does not enforce.
7. Exact limitation or tradeoff: deny rules need design time and an
exception path, or developers route around them.
8. Relevant evidence (with date): instructions vs enforceable
permissions from lesson-D7-1 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins for a
solo dev with no secrets. C wins never for client secrets. D wins
never as a control.
10. Misconception tested: "a written rule is a control." Only the rule
the code enforces is a control.

## Q-M-48 (V2-D7.2), Select TWO

**Scenario.** An engineer uses an AI assistant to write an incident
postmortem. The draft cites a root cause and a fix. The team will act
on the fix this week.

**Question.** Which TWO verifications are required before the team acts?
Select TWO.

**Options.**
A) The engineer ran the cited tests and inspected the results herself.
B) The engineer confirmed no secrets appear in the draft or the pasted
logs.
C) The draft has no typos.
D) The draft uses the team's font.
E) The assistant's confidence is high.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: AI-assisted work verification (multi).
2. Lifecycle stage: operations.
3. Objective: verify the postmortem before acting on it.
4. Hard constraints: the team acts on the fix this week. A wrong fix
wastes the week or harms the system.
5. System layer: developer workflow verification (V2-D7.2).
6. Eliminate infeasible: all five are doable.
7. Eliminate constraint-violating: C and D are cosmetic, E is
uncalibrated.
8. Compare on objective: A verifies the technical claim, B verifies
secret safety.
9. Hidden dependencies: the test results must be re-runnable by a
second engineer.
10. Verify: A and B. The rest are cosmetic or empty.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "The team will act on the fix this week."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Verifies the technical claim | Yes | No | No | No | No |
| Protects secrets | No | Yes | No | No | No |

4. Why A and B are required: acting on the fix makes the draft's claims
load-bearing, so the engineer must verify the tests ran and the results
hold. Pasted logs are a classic secret leak path, so the draft needs a
secret check.
5. Why A and B best meet the objective: V2-D7.2 requires verification
of AI-assisted work: tests ran, results inspected, secrets protected.
A and B are those three, split across two options.
6. Every rejected choice explained: C polishes prose while the fix may
be wrong. D is about format. E trusts the model's self-report, which is
not verification.
7. Exact limitation or tradeoff: verification takes engineer time. That
is the price of acting on AI-drafted claims.
8. Relevant evidence (with date): verification requirements from
lesson-D7-2 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: C wins for a
published report after the fix is verified. D wins never as
verification. E wins never.
10. Misconception tested: "the AI wrote it, so it is checked." The
human checks. That is the whole rule.

## Q-M-49 (V2-D7.3)

**Scenario.** The monthly model bill jumps 3x. Nothing shipped this
month. The on-call engineer opens the runbook.

**Question.** What does the runbook's cost branch check first?

**Options.**
A) The model's mood.
B) Routing (are cheap queries hitting the expensive tier), context
(oversized or duplicated context per call), and caching (cache hit rate
drops): the symptom-to-investigation map for cost.
C) The office Wi-Fi.
D) The vendor's stock price.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: operational debugging.
2. Lifecycle stage: operate.
3. Objective: find the cost spike's cause fast.
4. Hard constraints: 3x bill, no shipments, on-call needs a fast path.
5. System layer: debugging and operational resolution (V2-D7.3).
6. Eliminate infeasible: all four are statable.
7. Eliminate constraint-violating: A, C, and D are not causes.
8. Compare on objective: only B follows the cost investigation map.
9. Hidden dependencies: the runbook needs per-tier and per-stage cost
breakdowns to check the branches.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The monthly model bill jumps 3x. Nothing
shipped this month."
3. Requirement-to-option matrix:

| Check | A | B | C | D |
|---|---|---|---|---|
| Follows the cost map | No | Yes | No | No |
| Names real cost drivers | No | Yes | No | No |

4. Why B is right: V2-D7.3 maps cost symptoms to route choice, context, and
caching investigations. A router misconfiguration, a context blowup, or
a cache outage each explain a 3x bill with no shipments.
5. Why B best meets the objective: the runbook exists so the on-call
engineer checks causes in probability order instead of guessing. B is
that order.
6. Every rejected choice explained: A is nonsense. C is the local
network. The bill is server-side. D is the vendor's equity. It does
not set the bill.
7. Exact limitation or tradeoff: the map needs the cost breakdowns
instrumented in advance. A bill with no per-stage data cannot be
debugged.
8. Relevant evidence (with date): symptom-to-investigation mapping from
lesson-D7-3 (§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins never.
C wins when the symptom is local latency. D wins never.
10. Misconception tested: "debug by intuition." Debug by the map. The
map is the runbook's job.

## Q-M-50 (V2-D7.1)

**Scenario.** A data-science team wants a research subagent: web search
and file reads for literature review. The team's main agent holds write
access to production data pipelines.

**Question.** How should the subagent be scoped?

**Options.**
A) Give the subagent the same tools as the main agent for simplicity.
B) Scope the subagent to read-only tools (search, read) with no write
access and no production credentials. It returns findings, and the main
agent acts on them.
C) No subagent. Do research in the main agent.
D) Give the subagent write access but ask it nicely to read only.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: subagent scoping.
2. Lifecycle stage: enablement.
3. Objective: bound the research subagent's blast radius.
4. Hard constraints: main agent holds production write access. Research
needs only search and read.
5. System layer: scoped subagents (V2-D7.1).
6. Eliminate infeasible: all four are feasible.
7. Eliminate constraint-violating: A copies production writes, D trusts
a request.
8. Compare on objective: only B gives the subagent exactly what the
subtask needs.
9. Hidden dependencies: the handoff back to the main agent needs a
findings schema.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "web search and file reads for literature
review... main agent holds write access to production data pipelines."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Least privilege per subagent | No | Yes | N/A | No |
| Production writes fenced off | No | Yes | N/A | No |
| Subtask still doable | Yes | Yes | Yes | Yes |

4. Why B satisfies all hard constraints: the subagent gets search and
read only. No write tool means no write path, whatever the model
decides. Production credentials never enter its context.
5. Why B best meets the objective: V2-D7.1 scopes subagents with their
own tool lists under least privilege. B is the pattern: the research
loop cannot touch what it cannot see.
6. Every rejected choice explained: A hands production writes to a loop
that never needs them: maximum blast radius. C avoids the scoping
question but keeps research inside the privileged loop, which is worse.
D is the prompt-as-permission trap: "ask nicely" is not scoping.
7. Exact limitation or tradeoff: the findings handoff needs a schema,
or the main agent misreads the research.
8. Relevant evidence (with date): scoped subagents from lesson-D7-1
(§4), Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins never
for least privilege. C wins when the research needs the main agent's
tools. D wins never as scoping.
10. Misconception tested: "one tool list for the whole team is simpler."
Simpler to configure, wider to breach. Scope per loop.

## Coverage

| Domain | Objective | Questions |
|---|---|---|
| D1 | V2-D1.1 | Q-M-01 |
| D1 | V2-D1.2 | Q-M-02, Q-M-07 |
| D1 | V2-D1.3 | Q-M-03 |
| D1 | V2-D1.4 | Q-M-04 |
| D1 | V2-D1.5 | Q-M-05, Q-M-08 |
| D1 | V2-D1.6 | Q-M-06 |
| D2 | V2-D2.1 | Q-M-09, Q-M-14 |
| D2 | V2-D2.2 | Q-M-10 |
| D2 | V2-D2.3 | Q-M-11 |
| D2 | V2-D2.4 | Q-M-12, Q-M-15 |
| D2 | V2-D2.5 | Q-M-13 |
| D3 | V2-D3.1 | Q-M-16 |
| D3 | V2-D3.2 | Q-M-17, Q-M-24 |
| D3 | V2-D3.3 | Q-M-18 |
| D3 | V2-D3.4 | Q-M-19 |
| D3 | V2-D3.5 | Q-M-20, Q-M-25 |
| D3 | V2-D3.6 | Q-M-21 |
| D3 | V2-D3.7 | Q-M-22 |
| D3 | V2-D3.8 | Q-M-23 |
| D4 | V2-D4.1 | Q-M-26 |
| D4 | V2-D4.2 | Q-M-27, Q-M-32 |
| D4 | V2-D4.3 | Q-M-28 |
| D4 | V2-D4.4 | Q-M-29, Q-M-33 |
| D4 | V2-D4.5 | Q-M-30 |
| D4 | V2-D4.6 | Q-M-31 |
| D5 | V2-D5.1 | Q-M-34, Q-M-39 |
| D5 | V2-D5.2 | Q-M-35, Q-M-40 |
| D5 | V2-D5.3 | Q-M-36 |
| D5 | V2-D5.4 | Q-M-37 |
| D5 | V2-D5.5 | Q-M-38 |
| D6 | V2-D6.1 | Q-M-41 |
| D6 | V2-D6.2 | Q-M-42, Q-M-46 |
| D6 | V2-D6.3 | Q-M-43 |
| D6 | V2-D6.4 | Q-M-44 |
| D6 | V2-D6.5 | Q-M-45 |
| D7 | V2-D7.1 | Q-M-47, Q-M-50 |
| D7 | V2-D7.2 | Q-M-48 |
| D7 | V2-D7.3 | Q-M-49 |

Domain counts: D1 x8, D2 x7, D3 x10, D4 x8, D5 x7, D6 x6, D7 x4 = 50.
Multiple-response items: Q-M-03, Q-M-08, Q-M-11, Q-M-15, Q-M-18, Q-M-22,
Q-M-26, Q-M-30, Q-M-35, Q-M-38, Q-M-43, Q-M-48 = 12 of 50 (24%).
