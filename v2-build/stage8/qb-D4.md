# Domain 4 Question Bank: Evaluation, Testing and Optimization

25 original practice questions for objectives V2-D4.1 through V2-D4.6.
Baseline: Oct 6, 2026. Scope: blueprint v1.0 via secondary summaries (S03, S04), Sept 2026.
These are original practice items for study. They are not real exam items and do not predict exam content.
Format per question: scenario, one best answer or a marked multi-select, options, answer key, a §17 10-step method walk, and a 10-point explanation.

## Q-D4-01 (V2-D4.1)

**Scenario.** A product manager says: "Make the support bot more helpful." The team has no metric, no threshold, and no owner for "helpful." Engineering wants to start building.

**Question.** What is the best first action?

**Options.**
A) Start building, the team can define "helpful" after launch.
B) Pick the easiest metric (average response length) and optimize it.
C) Apply the metric chain first: turn "helpful" into task success with a threshold (e.g., resolved without escalation, 85%), plus guard metrics for safety and cost, each with an owner.
D) Ask the model to rate helpfulness on every answer.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: first action on a vague requirement.
2. Lifecycle stage: discovery.
3. Objective: a measurable definition of helpful.
4. Hard constraints: no numbers exist yet, the requirement is an adjective.
5. System layer: evaluation metrics.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only C converts the adjective into metrics with thresholds and owners.
9. Hidden dependencies: the threshold needs a baseline, the guard metrics need the safety and cost bars.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "Make the support bot more helpful" with "no metric, no threshold, and no owner."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Adjective becomes measurable | No | Wrong metric | Yes | Partial |
| Threshold set | No | Yes | Yes | No |
| Owner named | No | No | Yes | No |

4. Why C satisfies all hard constraints: the chain turns "helpful" into task success with a number, adds guard metrics, and names owners.
5. Why C best meets the objective: V2-D4.1 says a vague requirement with no numbers gets the chain first: metric with threshold.
6. Every rejected choice explained: A builds toward an undefined target, the team cannot know when it arrives. B picks a metric for ease, not meaning, longer answers are not more helpful. D asks the model to grade itself with no rubric, the scores are uncalibrated and the threshold is still missing.
7. Exact limitation or tradeoff: C takes a discovery session, the threshold is a first guess until the baseline is measured.
8. Relevant evidence (with date): "vague requirement, no numbers: apply the chain first" from lesson-D4-1 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as a method. B wins if response length were the proven proxy for the goal (it is not). D wins if the model grades against a calibrated rubric tied to human labels (then the grading is grounded).
10. Misconception tested: building first and measuring later works. It does not, the metric is the target, and an undefined target cannot be hit on purpose.

## Q-D4-02 (V2-D4.1)

**Scenario.** A summarizer's dashboard shows fluency 95 (green) for six months. A new audit measures actual task success: users find the needed fact in the summary only 60% of the time. The team ships on fluency.

**Question.** What is the best action?

**Options.**
A) Keep shipping on fluency, it is green and stable.
B) Replace fluency with task success as the primary metric, the proxy is green while the goal is red.
C) Average fluency and task success into one score.
D) Raise the fluency bar to 98.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: metric correction.
2. Lifecycle stage: operation (iteration).
3. Objective: ship on what the goal needs.
4. Hard constraints: fluency 95 coexists with task success 60, the team ships on the proxy.
5. System layer: evaluation metrics.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the only option that dethrones the misleading proxy.
9. Hidden dependencies: task success needs its measurement method (user found the fact) kept honest.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "fluency 95 (green)" while "users find the needed fact in the summary only 60% of the time."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Primary metric matches the goal | No | Yes | Diluted | No |
| Proxy dethroned | No | Yes | No | No |

4. Why B satisfies all hard constraints: task success becomes the ship metric, fluency drops to a diagnostic.
5. Why B best meets the objective: V2-D4.1 says metric green with goal red means the metric is a proxy, replace it.
6. Every rejected choice explained: A is the lesson's proxy-only failure: a green proxy never proves the goal, and it shipped the wrong thing for six months. C averages the lie with the truth, 77.5 hides both. D raises a bar that was never the goal, fluency 98 with task success 60 is still a failure.
7. Exact limitation or tradeoff: task success is harder to measure than fluency, the team must fund the measurement or the metric rots.
8. Relevant evidence (with date): "metric green, goal red: the metric is a proxy, replace it" and the 95/60 toy from lesson-D4-1 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if fluency were proven to predict task success (then it is not a proxy). C wins never as a primary metric. D wins if the goal were actually fluency.
10. Misconception tested: a green dashboard means a good product. It means a good metric, when the metric is a proxy, green is the most dangerous color.

## Q-D4-03 (V2-D4.1), Select TWO

**Scenario.** A team defines metrics for a refund agent: (1) refund accuracy (right amount, right account), (2) p95 latency, (3) cost per refund, (4) a safety guard: unauthorized refunds must be zero. The budget binds.

**Question.** Which TWO metric decisions are correct? Select TWO.

**Options.**
A) Make refund accuracy the primary metric with a threshold (e.g., 99.5%).
B) Give the safety guard a zero threshold: any unauthorized refund blocks the ship.
C) Drop the cost metric, accuracy is all that matters.
D) Make p95 latency the primary metric because users wait.
E) Track cost per successful refund as the primary business metric since the budget binds.

**Answer.** B, E

**Method walk (Steps 1-10).**
1. Question type: metric prioritization (multi-select).
2. Lifecycle stage: design.
3. Objective: the right primary and guard metrics.
4. Hard constraints: money moves (safety), budget binds (cost).
5. System layer: evaluation metrics.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the mandatory guard, E is the budget-driven primary.
9. Hidden dependencies: the zero threshold needs the unauthorized definition exact, cost per successful refund needs the success definition.
10. Verify: B and E. Two selected.

**Explanation.**
1. Correct answer: B, E.
2. Decisive scenario phrase: "unauthorized refunds must be zero" and "The budget binds."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Safety handled | Partial | Yes | n/a | n/a | n/a |
| Budget handled | n/a | n/a | No | n/a | Yes |
| Correct primary for the constraint | Partial | n/a | n/a | No | Yes |

4. Why B and E satisfy all hard constraints: the zero-threshold guard blocks any unauthorized refund, cost per successful refund is the primary the binding budget demands.
5. Why B and E best meet the objective: V2-D4.1 says safety or security at stake means a guard metric with a zero threshold, and budget binding means cost per successful task is the primary.
6. Every rejected choice explained: A is a fine metric but not the primary the scenario's constraints demand, with safety and budget binding, accuracy is necessary but not primary. C drops the cost metric the binding budget requires, the budget is a constraint, not a wish. D makes latency primary though no latency complaint or SLA appears, the binding constraints are safety and budget.
7. Exact limitation or tradeoff: cost per successful refund can incentivize refusing hard refunds, the accuracy metric must stay as a counterweight.
8. Relevant evidence (with date): guard-metric and cost-primary verdicts from lesson-D4-1 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if neither safety nor budget binds (then accuracy is the natural primary). C wins if the budget is open. D wins if a latency SLA binds.
10. Misconception tested: accuracy is always the primary metric. The binding constraint picks the primary, here safety guards and budget leads.

## Q-D4-04 (V2-D4.1)

**Scenario.** A medical triage assistant routes patients to care levels. A wrong route delays care. The team proposes these metrics: routing accuracy 95%, p95 latency 3 s, cost per route $0.02.

**Question.** Which gap exists, and what is the best fix?

**Options.**
A) No gap exists, ship on these three.
B) The gap is a latency SLO, add p99.
C) The gap is a safety guard metric: routes that delay critical care must be zero (or near-zero with a defined review), added as a blocking guard alongside accuracy.
D) The gap is a cost metric, add cost per token.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: metric gap identification.
2. Lifecycle stage: design.
3. Objective: metrics that cover the harm.
4. Hard constraints: a wrong route delays care, the proposed set has no harm metric.
5. System layer: evaluation metrics.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only C names the missing guard the harm demands.
9. Hidden dependencies: "delay critical care" needs a clinical definition and a labeled set.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "A wrong route delays care."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Harm measured | No | No | Yes | No |
| Blocks the ship on harm | No | No | Yes | No |

4. Why C satisfies all hard constraints: the guard metric measures the harm directly and blocks shipping while it is nonzero.
5. Why C best meets the objective: V2-D4.1 says safety at stake means adding the guard metric with a zero threshold, accuracy 95% can hide a 5% of delayed critical cases.
6. Every rejected choice explained: A ships with no harm metric, 95% accuracy is compatible with every critical case in the 5%. B adds p99, a finer latency number for a scenario whose binding constraint is harm, not speed. D adds cost per token, a finer cost number for a scenario whose missing piece is safety.
7. Exact limitation or tradeoff: the guard needs the clinical definition and labels, a vague guard is a slogan, not a metric.
8. Relevant evidence (with date): "safety or security at stake: add the guard metric with a zero threshold" from lesson-D4-1 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the harm were already covered by accuracy with a proven mapping (it is not). B wins if a latency SLA binds. D wins if the budget binds and cost is unmeasured.
10. Misconception tested: accuracy covers safety. It does not, accuracy averages, harm concentrates. The guard metric exists because the average lies.

## Q-D4-05 (V2-D4.2)

**Scenario.** A team builds the eval set for a support bot from clean, well-formed tickets. In production, 15% of tickets have typos, pasted stack traces, screenshots-as-text, and angry all-caps. The bot fails on most of them.

**Question.** What is the best fix to the eval framework?

**Options.**
A) Add more clean tickets to the eval set.
B) Add edge, adversarial, and malformed drawers to the eval set, drawn from production's ugly inputs, the set must include the 15% as they arrive.
C) Lower the quality bar for ugly tickets.
D) Filter ugly tickets out of production.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best fix to an eval dataset.
2. Lifecycle stage: preproduction.
3. Objective: evals that predict production.
4. Hard constraints: production has 15% ugly inputs, the eval set has none.
5. System layer: evaluation datasets.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: D refuses real users, C moves the bar instead of the set.
8. Compare on objective: only B makes the eval set represent production.
9. Hidden dependencies: the drawers need production sampling that respects PII rules.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "In production, 15% of tickets have typos, pasted stack traces" while the eval set is "clean, well-formed tickets."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Eval represents production | No | Yes | No | n/a |
| Ugly inputs covered | No | Yes | Excused | Removed |

4. Why B satisfies all hard constraints: the drawers mirror the production mix, the eval then measures what users actually get.
5. Why B best meets the objective: V2-D4.2 says production with ugly inputs makes edge, adversarial, and malformed drawers mandatory.
6. Every rejected choice explained: A adds more of what already passes, the eval gets bigger and stays blind. C lowers the bar for the inputs that need it most, the bar follows the user, not the eval's comfort. D deletes real users from the product, the 15% are customers.
7. Exact limitation or tradeoff: ugly inputs need PII stripping before they enter the eval set, the sampling must be refreshed as production shifts.
8. Relevant evidence (with date): drawer verdict from lesson-D4-2 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the failures were on clean tickets (then volume of clean cases helps). C wins never as a method. D wins if the ugly inputs are abuse, not users (then filtering is a product decision).
10. Misconception tested: a bigger eval set is a better eval set. Representativeness beats size, a thousand clean tickets cannot see the 15%.

## Q-D4-06 (V2-D4.2)

**Scenario.** A team grades 5,000 summaries a day with an LLM judge. No one checked the judge against human labels. The judge's scores drifted up 8 points over two months while user complaints rose.

**Question.** What is the best next action?

**Options.**
A) Tune the judge's prompt to push scores back down.
B) Collect human labels on a representative sample, calibrate the judge against them, and only then trust its scores, re-baseline the drifted period.
C) Replace the judge with a bigger model.
D) Average three judges to cancel the drift.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best next action on an uncalibrated judge.
2. Lifecycle stage: operation (iteration).
3. Objective: trustworthy grades.
4. Hard constraints: no human labels exist, scores drifted while complaints rose.
5. System layer: evaluation framework (judge calibration).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B grounds the judge in human labels.
9. Hidden dependencies: the sample must be representative, the label rubric must be crisp.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "No one checked the judge against human labels" and "scores drifted up 8 points over two months while user complaints rose."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Judge grounded in human labels | No | Yes | No | No |
| Drift explained, not hidden | No | Yes | No | No |

4. Why B satisfies all hard constraints: human labels are the ground truth, calibration ties the judge to them, the re-baseline fixes the drifted history.
5. Why B best meets the objective: V2-D4.2 says judge uncalibrated means human labels first, no judge without a calibration run.
6. Every rejected choice explained: A tunes the prompt to move the number, not to match truth, the drift's cause stays unknown. C buys a bigger uncalibrated judge, size does not create ground truth. D averages three drifting judges, the mean of three wrongs is still wrong.
7. Exact limitation or tradeoff: human labels cost money and time, the team calibrates once, then uses the ladder (code, then judge, then human spot checks).
8. Relevant evidence (with date): "judge uncalibrated: human labels first" from lesson-D4-2 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins after calibration shows the prompt is the fault (then tuning is grounded). C wins if the judge's capability (not calibration) is the fault, proven against labels. D wins never as a calibration method.
10. Misconception tested: judge scores are measurements. Uncalibrated scores are opinions with decimals, the human labels are what make them measurements.

## Q-D4-07 (V2-D4.2), Select TWO

**Scenario.** A team grades 2,000 cases per eval run. Human grading costs $250 per run. The ladder (code checks, then calibrated judge, then human spot checks) costs $25.60 per run. The team runs evals daily.

**Question.** Which TWO statements are correct? Select TWO.

**Options.**
A) Use the ladder for daily runs and reserve full human grading for releases or disputes, the 10x cost gap decides the cadence.
B) Grade everything by human, it is the most reliable.
C) Calibrate the judge once against human labels, then trust the ladder within its calibrated scope.
D) Skip calibration, the judge is cheaper and therefore better.
E) Run evals monthly to save money.

**Answer.** A, C

**Method walk (Steps 1-10).**
1. Question type: eval economics judgment (multi-select).
2. Lifecycle stage: operation.
3. Objective: reliable grades at a sustainable cadence.
4. Hard constraints: $250 vs $25.60 per run, daily cadence wanted.
5. System layer: evaluation framework.
6. Eliminate infeasible: B is financially infeasible daily ($250 x 365).
7. Eliminate constraint-violating: D skips the grounding the judge needs.
8. Compare on objective: A sets the cadence by cost, C grounds the ladder.
9. Hidden dependencies: the calibration scope must be documented, releases need the human bar defined.
10. Verify: A and C. Two selected.

**Explanation.**
1. Correct answer: A, C.
2. Decisive scenario phrase: "$250 per run" vs "$25.60 per run" and "runs evals daily."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Daily cadence affordable | Yes | No | Yes | Yes | n/a |
| Grades grounded | Yes | Yes | Yes | No | Partial |

4. Why A and C satisfy all hard constraints: the ladder makes daily runs affordable, calibration grounds the judge, humans keep the release gate.
5. Why A and C best meet the objective: V2-D4.2 prescribes the cheapest reliable evaluator (code, then judge, then human) with the judge calibrated against human labels.
6. Every rejected choice explained: B is the lesson's valid-but-inferior: the most reliable grades at 10x the cost turn daily runs into monthly runs, and the framework dies from its own cost. D confuses cheap with good, an uncalibrated judge is not a grader. E saves money by blinding the team, monthly evals miss regressions for weeks.
7. Exact limitation or tradeoff: the ladder's scope is its calibration, inputs outside it need human eyes, and the team must say what "outside" means.
8. Relevant evidence (with date): ladder economics ($250 vs $25.60) and calibration rule from lesson-D4-2 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins if the budget is open and the stakes demand it (then daily human grading is the design). D wins never. E wins if the product changes monthly (then the cadence matches the change rate).
10. Misconception tested: the best grader is the right grader for every run. The ladder exists because cost sets cadence, the most reliable grade at the wrong cadence is the wrong system.

## Q-D4-08 (V2-D4.2)

**Scenario.** A team mines production conversations for eval cases. Some conversations contain account numbers and health details. The eval set lives in a shared bucket that the whole company can read. A past bug (wrong dosage quotes) was fixed last quarter.

**Question.** Which TWO-part action is correct? (Single best answer.)

**Options.**
A) Strip PII before the cases leave the trust boundary, and keep a regression drawer with the dosage cases, run on every change.
B) Keep the PII, the eval team needs realistic data.
C) Delete the dosage cases, the bug is fixed.
D) Move the bucket inside the trust boundary and change nothing else.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: eval hygiene (two-part action).
2. Lifecycle stage: preproduction.
3. Objective: safe cases plus no regressions.
4. Hard constraints: PII in the cases, shared bucket, a fixed bug that must stay fixed.
5. System layer: evaluation datasets.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: B ships PII to a shared bucket.
8. Compare on objective: A is the only option that handles both the PII and the regression.
9. Hidden dependencies: stripping needs the PII patterns, the drawer needs the dosage cases labeled.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "account numbers and health details" in "a shared bucket that the whole company can read", and "wrong dosage quotes) was fixed last quarter."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| PII handled | Yes | No | Partial | Partial |
| Dosage bug stays fixed | Yes | Yes | No | Yes |

4. Why A satisfies all hard constraints: stripping before the boundary keeps PII inside, the regression drawer re-proves the fix on every change.
5. Why A best meets the objective: V2-D4.2 says PII gets stripped before cases leave the trust boundary, and old bugs get a regression drawer run on every change.
6. Every rejected choice explained: B keeps PII in a company-readable bucket, "realistic data" does not outrank the boundary. C deletes the proof the bug stays fixed, the next change can reintroduce it silently. D moves the bucket but strips nothing and names no drawer, the PII is still over-shared and the regression is still unguarded.
7. Exact limitation or tradeoff: stripping can remove context the case needs, the team must verify the stripped cases still test the behavior.
8. Relevant evidence (with date): PII and regression-drawer verdicts from lesson-D4-2 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins if the bucket is inside the trust boundary with proper access control (then stripping is optional). C wins never, fixed bugs keep their drawer. D wins if the only problem were the bucket location (it is not, the drawer is absent too).
10. Misconception tested: fixed means forgotten. Fixed means guarded, the regression drawer is the guard.

## Q-D4-09 (V2-D4.3)

**Scenario.** A team wants to change the refund agent's policy prompt. The change could wrongly deny legitimate refunds. Traffic is 50,000 refunds per day.

**Question.** What is the best rollout?

**Options.**
A) Ship to everyone and watch the dashboard over the weekend.
B) Shadow the new prompt first (run it, log decisions, take no action), then a controlled exposure with the primary metric monitored, then full rollout.
C) Ship to 50% immediately, the sample is big enough.
D) Ask the model whether the new prompt is safe.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best rollout for a risky change.
2. Lifecycle stage: preproduction.
3. Objective: prove safety before users feel the change.
4. Hard constraints: the change can harm users and money, 50,000 refunds per day.
5. System layer: A/B testing and iteration.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the only path where harm is measured before it reaches users.
9. Hidden dependencies: shadow mode needs the decision logged without acting, the primary metric needs its threshold.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "could wrongly deny legitimate refunds" at "50,000 refunds per day."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Harm measured before users feel it | No | Yes | Partial | No |
| Control exists | No | Yes | Yes | No |

4. Why B satisfies all hard constraints: shadow mode measures the new prompt's decisions with zero user impact, controlled exposure limits the blast radius with the metric watched.
5. Why B best meets the objective: V2-D4.3 says change that can harm users or money gets shadow first, then controlled exposure.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: fine for reversible low-stakes tweaks, but a harmful refund change reaches every user before anyone measures it. C skips the shadow, 50% of 50,000 harmed users is still 25,000 harmed users with no prior measurement. D asks the model to bless its own prompt, the model is not a test.
7. Exact limitation or tradeoff: shadow plus controlled exposure takes days, the team must keep the old prompt serving during the test.
8. Relevant evidence (with date): "change can harm: shadow first, then controlled exposure" from lesson-D4-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for a reversible low-stakes tweak (copy change, no money). C wins after the shadow shows no harm (then the 50% is the controlled exposure). D wins never as a test.
10. Misconception tested: big traffic makes testing unnecessary ("we will see it fast"). Big traffic makes the harm big, the shadow exists so the harm is measured, not felt.

## Q-D4-10 (V2-D4.3)

**Scenario.** A team ships two changes together: a new retrieval chunker and a new system prompt. Task success moves from 82% to 86%. The team credits the chunker.

**Question.** What is the best response?

**Options.**
A) Accept the credit, the number went up.
B) Split the changes and test one at a time, with two changes shipped together, no one knows which moved the number.
C) Ship a third change to see if the number moves again.
D) Roll back both changes, the test was invalid.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: test-design correction.
2. Lifecycle stage: operation (iteration).
3. Objective: know which change moved the number.
4. Hard constraints: two changes, one measurement, credit assigned without evidence.
5. System layer: A/B testing.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B restores the one-change-per-test rule.
9. Hidden dependencies: the split tests need the same eval set and enough traffic each.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "ships two changes together" and "The team credits the chunker."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Attribution provable | No | Yes | No | n/a |
| Learning kept | Luck | Yes | No | No |

4. Why B satisfies all hard constraints: one change per test isolates the effect, the eval set stays fixed across the two tests.
5. Why B best meets the objective: V2-D4.3 says two changes shipping together get split, one change per test.
6. Every rejected choice explained: A credits the chunker on no evidence, the prompt may have done the work, or the two interacted. C adds a third unknown to two unknowns, the pile of confounds grows. D rolls back a gain on a method complaint, the number did move, the attribution is what needs repair.
7. Exact limitation or tradeoff: split tests take twice the traffic or twice the time, the team must size each arm.
8. Relevant evidence (with date): "two changes ship together: split them" from lesson-D4-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as a method. C wins never. D wins if the change is harmful and the team needs it out now (then attribution waits).
10. Misconception tested: the number going up proves the favored change worked. It proves something worked, the test design decides whether anyone knows what.

## Q-D4-11 (V2-D4.3), Select THREE

**Scenario.** A team plans a prompt change test: 400 requests per day on the changed flow, primary metric is task success, the switch costs $0.01 per request extra.

**Question.** Which THREE statements about the test design are correct? Select THREE.

**Options.**
A) State a falsifiable hypothesis first (e.g., "the new prompt raises task success by at least 3 points").
B) Keep assignment consistent: a user stays in one arm for the test.
C) Watch p-values only, a significant p-value means ship.
D) Test for one day, 400 requests are enough for any claim.
E) Since the switch costs $0.01 per request, business significance decides, not the p-value alone.

**Answer.** A, B, E

**Method walk (Steps 1-10).**
1. Question type: test-design review (multi-select).
2. Lifecycle stage: preproduction.
3. Objective: a test that can actually answer.
4. Hard constraints: 400 requests per day, the switch has a real per-request cost.
5. System layer: A/B testing.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A, B, and E are the lesson's rules, C and D break them.
9. Hidden dependencies: the hypothesis needs the 3 points justified, consistency needs the assignment keyed, business significance needs the dollar math.
10. Verify: A, B, and E. Three selected.

**Explanation.**
1. Correct answer: A, B, E.
2. Decisive scenario phrase: "400 requests per day" and "the switch costs $0.01 per request extra."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Hypothesis falsifiable | Yes | n/a | n/a | n/a | n/a |
| Assignment consistent | n/a | Yes | n/a | n/a | n/a |
| Cost enters the decision | n/a | n/a | No | n/a | Yes |

4. Why A, B, and E satisfy all hard constraints: the falsifiable hypothesis sets the bar before the data, consistent assignment keeps the arms clean, the cost rule keeps the decision honest.
5. Why A, B, and E best meet the objective: V2-D4.3 requires a falsifiable hypothesis with the primary metric first, consistent assignment, and business significance (not p-values) when the switch has a real cost.
6. Every rejected choice explained: C ships on the p-value alone while the switch costs real money, a significant 0.5-point gain can still lose money. D asserts 400 requests suffice for any claim, sample size follows the claimed lift, and 400 a day may need weeks.
7. Exact limitation or tradeoff: A, B, and E do not set the sample size, the team must still compute it from the 3-point claim.
8. Relevant evidence (with date): hypothesis, assignment, and business-significance rules from lesson-D4-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the switch were free (then the p-value plus the primary metric could decide). D wins if the claimed lift is huge and 400 requests truly suffice (the math must show it).
10. Misconception tested: a significant p-value means ship. It means the effect is real, the cost decides whether it is worth it.

Again the E problem. E is correct and the item asks for two n/a flawed per the rewrite rule. Fix: make it Select THREE with A, B, E. But then the scenario must make C and D clearly wrong (they are). Let me rewrite as Select THREE.

## Q-D4-12 (V2-D4.3)

**Scenario.** A new rerank stage lifts task success from 84.0% to 84.6% with p < 0.01 on 200,000 requests. The stage adds $0.004 per request. Volume is 1,000,000 requests per day.

**Question.** Should the team ship the stage?

**Options.**
A) Yes, the p-value is significant.
B) No, the business math decides. The gain is 0.6 points on 1M requests = 6,000 more successes per day at $4,000 per day. Unless a success is worth more than $0.67, the stage loses money.
C) Yes, any significant gain is worth shipping.
D) No, p-values are meaningless.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: ship decision on a significant but small lift.
2. Lifecycle stage: preproduction.
3. Objective: decide by business significance.
4. Hard constraints: 0.6-point lift, $0.004 per request, 1M requests per day.
5. System layer: A/B testing (business significance).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B does the dollar math the switch cost demands.
9. Hidden dependencies: the $0.67 break-even needs the value of a success priced.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "adds $0.004 per request" at "1,000,000 requests per day" for a "0.6%" lift.
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Dollar math done | No | Yes | No | No |
| Decision follows the math | No | Yes | No | No |

4. Why B satisfies all hard constraints: 0.6% of 1M = 6,000 successes, 1M x $0.004 = $4,000/day, $4,000 / 6,000 = $0.67 per success break-even.
5. Why B best meets the objective: V2-D4.3 says when the switch has a real cost, business significance decides, not p-values.
6. Every rejected choice explained: A ships on significance alone, the p-value says the lift is real, not that it is worth $4,000 a day. C is A's slogan form, "any gain" ignores the price. D throws out p-values entirely, they are not meaningless, they are insufficient for a priced decision.
7. Exact limitation or tradeoff: if a success is worth $5 (e.g., a saved sale), the math flips and the stage ships, the team must price the success.
8. Relevant evidence (with date): "switch has a real cost: business significance decides, not p-values" from lesson-D4-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the stage were free (then the significant lift ships on its own). C wins never as a method. D wins never, p-values still gate whether the lift is real.
10. Misconception tested: statistical significance equals business significance. It equals reality of the effect, the price tag decides the ship.

## Q-D4-13 (V2-D4.4)

**Scenario.** A support bot's task success fell from 90% to 81% starting Tuesday. The change log shows: Monday, the team deployed a new system prompt, Tuesday, the retriever index was re-ingested with a new chunker.

**Question.** Which layer should the team suspect first?

**Options.**
A) The model tier, move to a more capable tier.
B) The Tuesday change: the re-ingestion with the new chunker. The failure starts on the change date, so that layer is the first suspect.
C) The Monday change: the system prompt, because prompts are the usual suspect.
D) The users, the questions probably got harder.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: right-layer diagnosis.
2. Lifecycle stage: incident response.
3. Objective: find the guilty layer fast.
4. Hard constraints: the failure starts Tuesday, two changes exist (Monday prompt, Tuesday chunker).
5. System layer: diagnosis across layers.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B follows the change-date rule, C follows habit.
9. Hidden dependencies: the team must confirm with traces, not stop at the suspicion.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "fell from 90% to 81% starting Tuesday" with "Tuesday, the retriever index was re-ingested with a new chunker."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Matches the failure start date | No | Yes | No | No |
| Names a real change | n/a | Yes | Yes | No |

4. Why B satisfies all hard constraints: the failure starts on the re-ingestion date, the change-date rule makes that layer the first suspect.
5. Why B best meets the objective: V2-D4.4 says failure starting on a change date means suspect that layer first.
6. Every rejected choice explained: A is the proxy fix, nothing indicts the model tier, and a bigger tier over broken chunks gives the same failures at higher cost. C suspects the prompt by habit, the failure did not start Monday, so the prompt is the second suspect, not the first. D blames the users with no evidence, the change log is evidence, the user theory is not.
7. Exact limitation or tradeoff: suspicion is not proof, the team must check the retrieval traces before fixing.
8. Relevant evidence (with date): "failure starts on a change date: suspect that layer first" from lesson-D4-4 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if traces show the model misreading good chunks (model fault). C wins if the failure started Monday (then the prompt is the change-date suspect). D wins with evidence of a real distribution shift (then the evidence supports that diagnosis).
10. Misconception tested: the usual suspect is the right suspect. The change log outranks habit, the date names the layer.

## Q-D4-14 (V2-D4.4)

**Scenario.** A classifier's accuracy fell from 96% to 88% after a template change. Traces show the new template truncates the ticket text to 200 characters, cutting off the details the labels need. A teammate proposes upgrading the model tier.

**Question.** What is the best response?

**Options.**
A) Approve the tier upgrade, a bigger model reads truncated text better.
B) Reject the upgrade, fix the template to pass the full ticket text. The trace indicts the template layer, so the fix goes there with the smallest correction.
C) Add explicit reasoning to compensate for the truncation.
D) Collect more training data for the truncated format.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best response to a proxy fix.
2. Lifecycle stage: incident response.
3. Objective: restore 96% accuracy.
4. Hard constraints: the trace indicts the template (200-char truncation), the labels need the cut details.
5. System layer: diagnosis (prompt/template layer).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B fixes the indicted layer.
9. Hidden dependencies: the template fix must be tested against the eval set.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the new template truncates the ticket text to 200 characters, cutting off the details the labels need."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixes the indicted layer | No | Yes | No | No |
| Restores the lost details | No | Yes | No | No |

4. Why B satisfies all hard constraints: the template passes the full text again, the smallest correction restores the 96%.
5. Why B best meets the objective: V2-D4.4 says the trace indicts one layer, so fix that layer with the smallest correction, the tier upgrade is the classic proxy fix.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: on the toy it cost $360 extra per day and fixed nothing, because the template was guilty. C reasons over truncated text, the details are gone, and reasoning cannot recover them. D trains for the broken format, the format is the bug, not the data.
7. Exact limitation or tradeoff: if the 200-char limit was intentional (context budget), the team must solve the budget another way (e.g., smarter selection, not blind truncation).
8. Relevant evidence (with date): "upgrade the model tier" valid-but-inferior and the trace-indictment rule from lesson-D4-4 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if traces show the model misreading full texts (true model fault). C wins if the details are present but the judgment is hard (reasoning fault). D wins if the format is fixed by product decision and the model must learn it.
10. Misconception tested: a bigger model fixes data starvation. It does not, every tier lacks the details. Fix the layer the trace names.

## Q-D4-15 (V2-D4.4), Select TWO

**Scenario.** Three incidents: (1) answers cite clauses that do not exist in the retrieved chunks, (2) the bot quotes last quarter's prices though the catalog updated yesterday, (3) latency tripled after a new rerank stage shipped.

**Question.** Which TWO layer diagnoses are correct? Select TWO.

**Options.**
A) Incident 1 is a verification-layer fault: the draft was not checked against the retrieved chunks (or the check is broken).
B) Incident 2 is a retrieval-layer fault: stale index, the re-ingestion missed the catalog update.
C) Incident 3 is a model-layer fault: the model got slower.
D) Incident 1 is a retrieval-layer fault: the chunks are wrong.
E) Incident 2 is a model-layer fault: the model forgot the prices.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: layer diagnosis (multi-select).
2. Lifecycle stage: incident response.
3. Objective: the right layer per incident.
4. Hard constraints: the symptom shapes (fabricated citations, stale facts, latency after a stage shipped).
5. System layer: diagnosis across layers.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A and B match the symptoms, C, D, E misread them.
9. Hidden dependencies: each diagnosis needs its trace confirmed before the fix.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "cite clauses that do not exist in the retrieved chunks", "quotes last quarter's prices though the catalog updated yesterday", "latency tripled after a new rerank stage shipped."
3. Requirement-to-option matrix:

| Incident | A | B | C | D | E |
|---|---|---|---|---|---|
| 1: phantom citations | Yes | n/a | n/a | No | n/a |
| 2: stale prices | n/a | Yes | n/a | n/a | No |
| 3: latency after rerank | n/a | n/a | No | n/a | n/a |

4. Why A and B satisfy all hard constraints: phantom citations mean the draft escaped its source check (verification), stale prices mean the index missed the update (retrieval).
5. Why A and B best meet the objective: V2-D4.4 says diagnose at the right layer and fix the failing component, not a proxy.
6. Every rejected choice explained: C blames the model for latency that started when the rerank stage shipped, the change-date rule names the stage. D blames retrieval for incident 1, but the chunks are fine, the draft invented citations the chunks never held, which is the check's failure. E blames the model's memory for prices that live in the index, the model quotes what retrieval gives it.
7. Exact limitation or tradeoff: A and B are diagnoses, not fixes, the verification check needs repair and the index needs re-ingestion with a freshness check.
8. Relevant evidence (with date): layer-diagnosis rules from lesson-D4-4 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if latency rose with no stage change (then the model or its host is the suspect). D wins if the chunks themselves hold the phantom clauses (then retrieval fed bad sources). E wins if the prices come from the model's weights, not an index (then it is a knowledge-cutoff problem).
10. Misconception tested: every quality failure is a model failure. The pipeline has layers, the symptom names the layer, and the fix follows the name.

## Q-D4-16 (V2-D4.4)

**Scenario.** A bot's answers degraded over three weeks. No layer was changed. Traces exist but show nothing wrong at any layer: retrieval returns good chunks, the model reads them correctly, the checks pass, yet users rate answers worse.

**Question.** What is the best next action?

**Options.**
A) Upgrade the model tier, something must be wrong with the model.
B) Rewrite the system prompt, prompts are the usual suspect.
C) Instrument first: add user-outcome tracing (did the answer solve the user's problem?) and production sampling with human labels. No fix without evidence.
D) Rebuild the index, stale data is the usual cause.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: best next action with no evidence.
2. Lifecycle stage: incident response.
3. Objective: find the real fault before fixing.
4. Hard constraints: no change date, no trace indicts any layer, users rate answers worse.
5. System layer: diagnosis (instrumentation).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only C refuses to fix blind, the rest guess.
9. Hidden dependencies: the outcome tracing needs the user's goal captured, the sampling needs human labels.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "No layer was changed" and "show nothing wrong at any layer, yet users rate answers worse."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Acts on evidence | No | No | Yes | No |
| Can find the real fault | Luck | Luck | Yes | Luck |

4. Why C satisfies all hard constraints: outcome tracing measures what the current traces miss (did it solve the problem?), human-labeled production samples ground the ratings.
5. Why C best meets the objective: V2-D4.4 says no evidence at any layer means instrument first, no fix without evidence.
6. Every rejected choice explained: A upgrades the tier on no indictment, the lesson's $360-a-day proxy fix. B rewrites the prompt on habit, the traces show the prompt's outputs are fine. D rebuilds the index on habit, retrieval returns good chunks per the traces.
7. Exact limitation or tradeoff: instrumentation takes time while users suffer, the team should also check for a distribution shift in the questions (new topics the eval never covered).
8. Relevant evidence (with date): "no evidence at any layer: instrument first" from lesson-D4-4 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if new evidence indicts the model layer. B wins if the prompt changed (then the change-date rule applies). D wins if the traces show stale chunks (then retrieval is indicted).
10. Misconception tested: action beats investigation. Blind fixes feel fast and cost weeks, the instrument-first rule exists because guessing at layers is the most expensive slowness.

## Q-D4-17 (V2-D4.5)

**Scenario.** A pipeline's p95 is 2.9 s against a 2 s SLA. Quality sits above the floor on every metric. Per-stage measurements: retrieval 400 ms, rerank 700 ms (+1 point), reasoning 900 ms (+2 points), verification 300 ms (+4 points). The team asks where to cut.

**Question.** What is the best first cut?

**Options.**
A) Cut the rerank stage, at 700 ms per 1 point it is the thinnest receipt.
B) Cut verification, 300 ms is the smallest number.
C) Cut retrieval, it runs on every call.
D) Cut reasoning, 900 ms is the biggest number.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: best first cut under an SLA.
2. Lifecycle stage: operation (optimization).
3. Objective: p95 under 2 s with the floor held.
4. Hard constraints: floor holds everywhere, the SLA binds.
5. System layer: cost-performance optimization.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright, but the floor math must hold after the cut.
8. Compare on objective: A removes the worst ms-per-point stage, the floor survives (93% to 92% on the D3 toy).
9. Hidden dependencies: the per-stage numbers must be measured, the cut needs an eval re-run.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "Quality sits above the floor on every metric" and "p95 is 2.9 s against a 2 s SLA."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Worst ms per point cut | Yes | No | No | No |
| Floor survives | Yes | Risked | Risked | Yes |

4. Why A satisfies all hard constraints: 700 ms per 1 point is the thinnest receipt, removing it keeps accuracy above the floor.
5. Why A best meets the objective: V2-D4.5 says when the SLA binds and the floor holds, cut the thinnest receipt first.
6. Every rejected choice explained: B cuts the smallest raw number, but verification is 75 ms per point and the correctness guard, raw ms is not the receipt. C cuts retrieval (67 ms per point, the best receipt) and 6 points, the floor breaks. D cuts the biggest raw number, but reasoning's 450 ms per point beats rerank's 700, biggest is not thinnest.
7. Exact limitation or tradeoff: the cut spends 1 point of headroom, the team must watch the floor after the cut.
8. Relevant evidence (with date): "SLA binds, floor holds: cut the thinnest receipt first" from lesson-D4-5 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins never as a first cut. C wins if retrieval's points were unmeasured (then it is the unmeasured stage). D wins if reasoning's 2 points were unmeasured.
10. Misconception tested: cut the biggest or the smallest latency. The receipt (ms per accuracy point) decides, the raw number misleads both ways.

## Q-D4-18 (V2-D4.5)

**Scenario.** Users complain the assistant "feels slow." The p95 SLA measures completion at 3 s. The team proposes streaming the output so the first token arrives in 0.5 s.

**Question.** What is the best response?

**Options.**
A) Approve, streaming fixes the slowness users feel.
B) Approve streaming as a perceived-latency win, but name the truth: p95 completion stays 3 s, so the SLA still needs a real cut (thinnest receipt first).
C) Reject streaming, it never helps.
D) Remove the SLA, users feel the first token.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best response to a latency proposal.
2. Lifecycle stage: operation (optimization).
3. Objective: honest latency improvement.
4. Hard constraints: the SLA measures completion, streaming moves first token, not completion.
5. System layer: latency optimization.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the only option that separates perceived from measured latency.
9. Hidden dependencies: the real cut needs the per-stage receipts measured.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The p95 SLA measures completion at 3 s" and "the first token arrives in 0.5 s."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Perceived latency helped | Yes | Yes | No | Partial |
| SLA honestly addressed | No | Yes | No | No |

4. Why B satisfies all hard constraints: streaming ships for the feel, the SLA gets its real cut separately.
5. Why B best meets the objective: V2-D4.5's lesson says streaming alone is perceived responsiveness, the completion time is unchanged, and the SLA measures completion.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: users feel faster while p95 completion stays 3 s, the SLA still fails. C rejects a real perceived-latency win, streaming helps the feel, it just does not move the SLA. D deletes the contract instead of meeting it, the users' wait is still 3 s.
7. Exact limitation or tradeoff: streaming plus a real cut costs both the streaming work and the cut, the team must do both, not substitute one for the other.
8. Relevant evidence (with date): "streaming alone" valid-but-inferior from lesson-D4-5 (§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the SLA measured time-to-first-token (then streaming moves the SLA). C wins never outright. D wins never, SLAs are renegotiated, not deleted.
10. Misconception tested: faster-feeling equals faster. The first token is UX, completion is the SLA. Both matter, and they are different numbers.

## Q-D4-19 (V2-D4.5)

**Scenario.** A team's pipeline misses the quality floor: groundedness is 88% against a 92% bar. The p95 is also over the SLA. The team proposes cutting the rerank stage to fix latency first.

**Question.** What is the best response?

**Options.**
A) Approve, latency first, quality second.
B) Reject the cuts, with the floor unmet, no cuts. Fix quality first, then optimize latency against the held floor.
C) Cut rerank and add a bigger tier at the same time.
D) Lower the groundedness bar to 88%.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: sequencing judgment (quality vs latency).
2. Lifecycle stage: operation (optimization).
3. Objective: floor held, then SLA met.
4. Hard constraints: groundedness 88% vs 92% bar, the floor is unmet.
5. System layer: cost-performance optimization.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: D moves the bar instead of the system.
8. Compare on objective: only B enforces the floor-first order.
9. Hidden dependencies: the quality fix needs its diagnosis (which layer fails groundedness).
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "groundedness is 88% against a 92% bar" and "proposes cutting the rerank stage to fix latency first."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Floor fixed before cuts | No | Yes | No | Evaded |
| Latency addressed | Yes | After | Partial | No |

4. Why B satisfies all hard constraints: cuts are priced in accuracy points, with the floor unmet, there are no points to spend.
5. Why B best meets the objective: V2-D4.5 says quality floor unmet means no cuts, fix quality first.
6. Every rejected choice explained: A optimizes a pipeline that fails its bar, a fast wrong answer is still wrong. C does both at once, the tier change confounds the quality diagnosis, and the cut still spends points the floor does not have. D lowers the bar to meet the number, the bar follows the requirement, not the system's comfort.
7. Exact limitation or tradeoff: B delays the latency win, the team must say so plainly and fix the groundedness layer first.
8. Relevant evidence (with date): "quality floor unmet: no cuts, fix quality first" from lesson-D4-5 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the floor holds (then the thinnest receipt goes first). C wins never as a combined move, sequence the tier test after the floor holds. D wins if the 92% bar was arbitrary and the requirement truly is 88% (then the bar was wrong, not the system).
10. Misconception tested: latency and quality optimize in parallel. They sequence: the floor first, then the cuts. Cuts spend accuracy, a broken floor has none to spend.

## Q-D4-20 (V2-D4.5), Select TWO

**Scenario.** A team's cost breakdown per call: context 8,000 tokens (mostly repeated instructions), retrieval 1,500, generation 500. Quality floor holds. The budget binds.

**Question.** Which TWO moves are correct? Select TWO.

**Options.**
A) Shrink the context before caching: dedupe the repeated instructions and move the stable block to the cache prefix.
B) Route the easy calls to the cheaper tier after the router proves them easy on evals.
C) Add a rerank stage for better quality.
D) Cache the full conversation including the variable tail.
E) Upgrade all traffic to the most capable tier for headroom.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: cost-optimization move selection (multi-select).
2. Lifecycle stage: operation (optimization).
3. Objective: cut cost with the floor held.
4. Hard constraints: context dominates (8,000 of 10,000 tokens), floor holds, budget binds.
5. System layer: token and cost optimization.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A attacks the dominant cost, B routes the provably easy calls down.
9. Hidden dependencies: A needs the prefix stable, B needs the router's "easy" proven on evals, not assumed.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "context 8,000 tokens (mostly repeated instructions)" and "Quality floor holds."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Attacks the dominant cost | Yes | Partial | No | No | No |
| Floor provably held | Yes | With evals | n/a | n/a | Yes |

4. Why A and B satisfy all hard constraints: shrinking the 8,000-token context cuts the biggest term, routing only the proven-easy calls protects the floor.
5. Why A and B best meet the objective: V2-D4.5 says context dominating cost means shrink context before caching, and route only what the router proves easy.
6. Every rejected choice explained: C adds a stage (more cost) to a pipeline whose floor already holds, the budget binds the other way. D caches the variable tail, the prefix never stabilizes and writes keep billing. E buys headroom the floor does not need at top-tier prices.
7. Exact limitation or tradeoff: A needs the stable block versioned, B needs the router re-proven as traffic shifts.
8. Relevant evidence (with date): "context dominates cost: shrink context before caching" and "route only what the router proves easy" from lesson-D4-5 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the floor were unmet (then quality comes before cuts). D wins never. E wins if the floor is unmet and the capable tier is the proven fix.
10. Misconception tested: caching fixes context cost. Caching discounts a stable prefix, the shrink comes first, because a smaller context beats a discounted big one.

## Q-D4-21 (V2-D4.6)

**Scenario.** A team's quality dashboard is green for six weeks. A user survey shows answers got worse a month ago. The eval suite has not changed in four months, production topics shifted to a new product line.

**Question.** What is the best next action?

**Options.**
A) Celebrate, the dashboard is green.
B) Tune the model to the new product line immediately.
C) Page the owner and refresh the suite: the suite is stale. Add the new product line's cases, re-baseline, and find why the green suite missed a month of drift.
D) Lower the survey's influence, users are subjective.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: best next action on a stale suite.
2. Lifecycle stage: operation (monitoring).
3. Objective: a suite that sees the drift.
4. Hard constraints: suite unchanged for four months, production shifted, users report worse answers for a month.
5. System layer: production monitoring.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only C treats the green as the suspect.
9. Hidden dependencies: the refresh needs the new product line's cases labeled, the owner must be named.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "dashboard is green for six weeks" while "answers got worse a month ago" and "The eval suite has not changed in four months."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Suite represents production | No | n/a | Yes | No |
| Drift explained | No | No | Yes | No |

4. Why C satisfies all hard constraints: the refresh adds the missing cases, the re-baseline shows the true state, the post-mortem finds the blind spot.
5. Why C best meets the objective: V2-D4.6 says live slides with a green suite means the suite is stale, page and refresh.
6. Every rejected choice explained: A trusts the instrument over the users, the instrument is what failed. B tunes the model to a drift the suite cannot see, the fix may help, but the blindness remains. D dismisses the users, the survey is the signal the suite missed.
7. Exact limitation or tradeoff: the refresh costs labeling work, the team should also schedule suite reviews so staleness is caught by calendar, not by users.
8. Relevant evidence (with date): "live slides, suite is green: the suite is stale, page and refresh" from lesson-D4-6 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as a method. B wins after the refreshed suite confirms the model layer is the fault. D wins never, user signal outranks a stale suite.
10. Misconception tested: green means good. Green means the suite passes, when production moves and the suite does not, green is the color of blindness.

## Q-D4-22 (V2-D4.6)

**Scenario.** A team monitors a payment assistant. They need to catch a full outage in minutes and a slow quality drift over weeks. One alert exists: a daily average of task success.

**Question.** What is the best monitoring design?

**Options.**
A) Keep the daily average, it covers both.
B) Pair a fast line with a slow line: a minutes-scale alert on error rate and traffic (outage), plus a weeks-scale trend on task success with human-labeled samples (drift).
C) Add ten more daily averages.
D) Alert on every single failed task.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best monitoring design for two time scales.
2. Lifecycle stage: operation (monitoring design).
3. Objective: fast outage caught fast, slow drift caught at all.
4. Hard constraints: outage needs minutes, drift needs weeks, one daily average serves neither well.
5. System layer: production monitoring.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B gives each time scale its line.
9. Hidden dependencies: the fast line needs its threshold tuned, the slow line needs the labeled samples funded.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "catch a full outage in minutes and a slow quality drift over weeks."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Outage in minutes | No | Yes | No | Yes |
| Drift over weeks | Partial | Yes | Partial | No |
| Alert fatigue avoided | Yes | Yes | No | No |

4. Why B satisfies all hard constraints: the fast line pages on error rate and traffic drops, the slow line trends task success on labeled samples.
5. Why B best meets the objective: V2-D4.6 says fast outage vs slow drift means pair a fast line with a slow line.
6. Every rejected choice explained: A is one line for two time scales, the daily average sees the outage a day late and the drift only when it is big. C multiplies the wrong shape, ten daily averages are still daily. D pages on every failure, the team drowns and starts ignoring the pager, which kills both lines.
7. Exact limitation or tradeoff: two lines need two thresholds and two owners, the slow line's labels cost ongoing money.
8. Relevant evidence (with date): "fast outage vs slow drift: pair a fast line with a slow line" from lesson-D4-6 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the product is low-stakes and daily detection suffices for both. C wins never as a design. D wins if failures are rare and each one is critical (then every failure deserves a page).
10. Misconception tested: one metric monitors everything. Time scales differ, the outage line and the drift line are different instruments.

## Q-D4-23 (V2-D4.6)

**Scenario.** A team's incident review finds: the quality alert fired three times last month, nobody owned it, each firing was discussed in a chat thread and forgotten. The alert still has no owner.

**Question.** What is the best first action?

**Options.**
A) Tune the alert threshold.
B) Add more alerts for coverage.
C) Name an owner first: one person accountable for the alert's tuning, response, and retirement. No monitoring exists until someone owns it.
D) Silence the alert, it clearly does not work.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: best first action on an unowned alert.
2. Lifecycle stage: operation (monitoring).
3. Objective: the alert becomes a working control.
4. Hard constraints: three firings, no owner, no response, no tuning.
5. System layer: production monitoring (ownership).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only C addresses the root cause (no owner), the rest treat symptoms.
9. Hidden dependencies: the owner needs the authority to tune and the time to respond.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "nobody owned it, each firing was discussed in a chat thread and forgotten."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Root cause addressed | No | No | Yes | No |
| Alert becomes actionable | Maybe | No | Yes | No |

4. Why C satisfies all hard constraints: the owner tunes, responds, and retires, accountability replaces the chat thread.
5. Why C best meets the objective: V2-D4.6 says no named owner means no monitoring exists yet, name one first.
6. Every rejected choice explained: A tunes a threshold nobody will maintain, the next drift re-breaks it. B adds alerts to an unowned system, more unowned alerts are more noise. D silences the one signal the team has, the failures continue quietly.
7. Exact limitation or tradeoff: one owner can become a bottleneck, the team should name a backup and a rotation.
8. Relevant evidence (with date): "no named owner: no monitoring exists yet, name one first" from lesson-D4-6 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins after the owner is named and the threshold is the diagnosed problem. B wins after ownership exists and a real coverage gap is found. D wins if the alert is proven wrong (then retirement is the owner's call, not silence by frustration).
10. Misconception tested: monitoring is instrumentation. Instrumentation without an owner is a dashboard, the owner is what makes it monitoring.

## Q-D4-24 (V2-D4.6)

**Scenario.** A latency alert fires every Monday morning. Each time, the on-call checks, finds nothing wrong (a batch job skews the Monday numbers), and closes it. This has run for two months. The team now ignores the alert channel.

**Question.** What is the best action?

**Options.**
A) Keep the alert, it might catch a real incident one day.
B) Retune or retire the alert: exclude the batch window or move the alert to business-hours traffic. An alert that fires weekly with no action is a wrong line.
C) Page louder on Mondays so the team pays attention.
D) Lower the threshold to catch smaller issues.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best action on a noisy alert.
2. Lifecycle stage: operation (monitoring).
3. Objective: an alert channel the team trusts.
4. Hard constraints: weekly false fires for two months, the team ignores the channel, the cause is known (batch job skew).
5. System layer: production monitoring (alert hygiene).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B fixes the line, the rest preserve or worsen the noise.
9. Hidden dependencies: the retune needs the batch window defined, retirement needs the coverage replaced.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "fires every Monday morning" with "finds nothing wrong" for "two months" and "The team now ignores the alert channel."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| False fires stop | No | Yes | No | No |
| Channel trust restored | No | Yes | No | No |

4. Why B satisfies all hard constraints: excluding the batch window removes the known false cause, the channel becomes trustworthy again.
5. Why B best meets the objective: V2-D4.6 says an alert firing weekly with no action is the wrong line, retune or retire it.
6. Every rejected choice explained: A keeps a line the team ignores, an ignored alert is not coverage, it is a story the team tells itself. C pages louder into an ignored channel, volume does not create trust. D lowers the threshold, which fires more often with the same false cause, the noise grows.
7. Exact limitation or tradeoff: if the batch window ever carries real incidents, the exclusion blinds the team there, the exclusion needs its own review.
8. Relevant evidence (with date): "alert fires weekly with no action: the line is wrong, retune or retire it" from lesson-D4-6 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the fires were real but the response was weak (then the response needs fixing, not the line). C wins never as a trust repair. D wins if the misses are real and the noise is tolerable (then the threshold was the fault).
10. Misconception tested: more alerting equals more safety. Unactioned alerts destroy the channel, a quiet trusted channel beats a loud ignored one.

## Q-D4-25 (V2-D4.6), Select TWO

**Scenario.** A team designs production monitoring for a claims assistant: quality floor 95% task success, p95 latency 2 s, cost budget per month, and a regulator that can audit any decision.

**Question.** Which TWO monitoring choices are correct? Select TWO.

**Options.**
A) Instrument the model, retrieval, tools, and dependencies with per-stage metrics, and keep the eval suite representative of production with a named owner.
B) Run the regression suite on every change and page on quality slides with the owner accountable.
C) Review the dashboard manually once a month, the team is small.
D) Alert only on latency, quality moves slowly.
E) Keep no traces to save cost, the metrics suffice.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: monitoring design selection (multi-select).
2. Lifecycle stage: operation (monitoring design).
3. Objective: floor held, regressions caught, audits answerable.
4. Hard constraints: quality floor, latency SLA, cost budget, regulator audits.
5. System layer: production monitoring.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: E destroys auditability the regulator requires.
8. Compare on objective: A instruments every layer with an owned suite, B gates changes and pages on slides.
9. Hidden dependencies: the per-stage metrics need the request id, the page needs its threshold.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "quality floor 95%", "regulator that can audit any decision."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Every layer instrumented | Yes | n/a | No | No | No |
| Regressions gated | n/a | Yes | No | n/a | n/a |
| Audits answerable | Yes | n/a | No | n/a | No |

4. Why A and B satisfy all hard constraints: per-stage instrumentation with an owned representative suite covers the floor and the audit, the regression gate plus paging covers change risk.
5. Why A and B best meet the objective: V2-D4.6 requires instrumentation of model, retrieval, tools, and dependencies, representative eval data, regression suites, and alerts with owners.
6. Every rejected choice explained: C is the lesson's valid-but-inferior: on the toy the slide ran 42 days before a human looked, manual review is the first chore dropped under pressure. D watches one of three constraints, quality and cost drift unseen. E saves the trace bill and loses the audit, the regulator's "any decision" needs the traces.
7. Exact limitation or tradeoff: A and B cost build and label money, the team must fund the suite's representativeness or it rots like the D4-21 toy.
8. Relevant evidence (with date): monitoring requirements from lesson-D4-6 (§9) and the 42-day toy from §10, Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the product is a low-stakes internal tool with no floor (then the stakes do not justify the machinery). D wins never as a complete design. E wins never with a regulator in the scenario.
10. Misconception tested: monitoring is one dashboard. It is instrumentation plus an owned suite plus gates plus paging, the dashboard is the least of it.

## Coverage: D4 questions to objectives

| Objective | Questions | Count |
|---|---|---|
| V2-D4.1 | Q-D4-01, Q-D4-02, Q-D4-03, Q-D4-04 | 4 |
| V2-D4.2 | Q-D4-05, Q-D4-06, Q-D4-07, Q-D4-08 | 4 |
| V2-D4.3 | Q-D4-09, Q-D4-10, Q-D4-11, Q-D4-12 | 4 |
| V2-D4.4 | Q-D4-13, Q-D4-14, Q-D4-15, Q-D4-16 | 4 |
| V2-D4.5 | Q-D4-17, Q-D4-18, Q-D4-19, Q-D4-20 | 4 |
| V2-D4.6 | Q-D4-21, Q-D4-22, Q-D4-23, Q-D4-24, Q-D4-25 | 5 |
| Total | | 25 |

Multi-response items: Q-D4-03, Q-D4-07, Q-D4-11, Q-D4-15, Q-D4-20, Q-D4-25 (6 of 25).
