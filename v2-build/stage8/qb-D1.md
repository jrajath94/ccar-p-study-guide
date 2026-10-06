# Domain 1 Question Bank: Solution Design and Architecture

25 original practice questions for objectives V2-D1.1 through V2-D1.6.
Baseline: Oct 6, 2026. Scope: blueprint v1.0 via secondary summaries (S03, S04), Sept 2026.
These are original practice items for study. They are not real exam items and do not predict exam content.
Format per question: scenario, one best answer or a marked multi-select, options, answer key, a §17 10-step method walk, and a 10-point explanation.
Tier names (Fast, Balanced, Capable, Most capable) are lesson toys from stage3, priced per S10-S12 secondary sources, Oct 2026. Verify against official docs before production use.

## Q-D1-01 (V2-D1.1)

**Scenario.** A hospital routes patient intake messages. The desk receives 12,000 messages per day. About 70% are standard forms: five checkboxes and a fixed symptom list. About 30% are free-text messages where the patient describes symptoms in their own words. A wrong route delays care. The IT budget is fixed.

**Question.** Which design fits the scenario best?

**Options.**
A) One agent handles every message end to end with no checks.
B) Deterministic rules route the 70% standard cases. Claude drafts replies for the 30% open cases. Code checks every draft against the source message before send.
C) The most capable tier answers every message with no checks.
D) Claude triages all messages, and a nurse reviews every draft before send.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best architecture under constraints.
2. Lifecycle stage: design.
3. Objective: safe routing inside a fixed budget.
4. Hard constraints: wrong route delays care, 12,000 messages per day, budget fixed, no unchecked draft reaches a patient.
5. System layer: orchestration pattern plus verification.
6. Eliminate infeasible: all four are technically feasible.
7. Eliminate constraint-violating: A has no check on care routing, C has no checks at all, D needs 12,000 x 30 s = 100 nurse-hours per day, which the fixed budget cannot carry.
8. Compare on objective: B pairs the fork (fixed cases deterministic, open cases Claude) with a gate on every draft.
9. Hidden dependencies: B needs the rule set maintained and the check must see the source message.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "A wrong route delays care. The IT budget is fixed."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixed cases route cheap | No | Yes | No | No |
| Open cases get language understanding | Yes | Yes | Yes | Yes |
| Gate on every draft | No | Yes | No | Yes |
| Fits fixed budget at 12k/day | No | Yes | No | No |

4. Why B satisfies all hard constraints: deterministic rules handle the fixed 70% at parser cost, Claude handles the open 30%, the code check enforces "no unchecked output reaches patients", and the fork keeps per-day cost far below the all-top-tier options.
5. Why B best meets the objective: the fork maps task shape to lane (fixed mapping goes deterministic, open input with a verifiable output goes to Claude with a gate), which is the V2-D1.1 decision rule.
6. Every rejected choice explained: A is technically valid but violates the error-cost constraint (an agent with no checks on care routing). C is valid quality-wise but violates the budget (most capable tier for every message, about 14x the Fast tier on the toy) and has no gate. D is valid as a safety instinct but infeasible at 12,000 x 30 s = 360,000 s = 100 nurse-hours per day under a fixed budget, and it fixes nothing: the triage failure stays in the system.
7. Exact limitation or tradeoff: B needs the rule set maintained as forms change, and the check must see the source message, which adds per-call code.
8. Relevant evidence (with date): fork rule and 80/20 split from lesson-D1-1 (§4), Oct 6 2026, tier pricing from S10-S12, Oct 2026, verify against official docs, reviewer math is an original toy for this question.
9. Counterfactual where each plausible alternative wins: A wins for an internal demo with no patients and no side effects (lesson-D1-2 counterfactual). C wins when the quality floor is unmet on every cheaper tier and evals prove the gain. D wins when volume is 50 per day and each draft carries legal risk, so the review labor fits.
10. Misconception tested: "more autonomy and more review always help." Here autonomy removes the gate and review removes the budget. The scenario, not a slogan, picks the design.

## Q-D1-02 (V2-D1.1)

**Scenario.** A retail CFO asks for an AI system that reads supplier invoices and "pays them automatically." About 80% of invoices arrive in one fixed layout. About 20% are open scans from new suppliers. Finance states one rule: money never moves on an unchecked total.

**Question.** What is the best FIRST action?

**Options.**
A) Start building the end-to-end payment agent so the CFO sees progress this week.
B) Benchmark the most capable tier against the fast tier on 1,000 invoices.
C) Write the hard constraint into the design: fork fixed layouts to a deterministic parser, route open scans to Claude, and place a code gate on every total before payment.
D) Draft the system prompt with strict instructions that forbid paying wrong totals.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: first action in a design discussion.
2. Lifecycle stage: discovery moving into design.
3. Objective: a payable-invoice design that honors the finance rule.
4. Hard constraints: money never moves on an unchecked total, 80/20 layout split.
5. System layer: requirements translation plus lane choice.
6. Eliminate infeasible: all are feasible as actions.
7. Eliminate constraint-violating: A builds before the constraint is in the design, D puts a money rule in a prompt, and prompts are not enforcement.
8. Compare on objective: C is the only action that turns the stated constraint into architecture before any build.
9. Hidden dependencies: the gate needs the parsed total and the source invoice as inputs.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "money never moves on an unchecked total."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Constraint enters the design first | No | No | Yes | No |
| Fork matches the 80/20 split | No | No | Yes | No |
| Enforcement in code, not prose | No | No | Yes | No |

4. Why C satisfies all hard constraints: it records the no-unchecked-payment rule as a code gate and picks lanes by input shape (fixed to parser, open to Claude), so no later step can drop the gate.
5. Why C best meets the objective: V2-D1.1 requires hard constraints to filter the design before build, C is the only option that does the filtering.
6. Every rejected choice explained: A is the classic skip-a-link failure: building before the five-link chain (outcome, function, numbers, limits, fit) is set. B is useful later but answers the wrong first question: tier choice before the constraint is recorded. D is the documented trap: a prompt is guidance, not a lock, the model may comply or not, and no audit can prove the gate ran.
7. Exact limitation or tradeoff: C produces no visible progress this week, which can frustrate the CFO, the cost is a short design pause.
8. Relevant evidence (with date): five-link translation chain from lesson-D1-1 (§4), Oct 6 2026, "prompts are contracts, never authorization" from lesson-D2-2, Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the ask is a throwaway prototype with no money movement. B wins after the gate is in the design and the question is which tier clears the quality floor. D wins for style guidance (tone, format), never for money rules.
10. Misconception tested: a strong instruction equals a control. It does not. The exam rewards the answer that puts the money rule in code.

## Q-D1-03 (V2-D1.1), Select TWO

**Scenario.** A bank scans paper cheques. Fields include payee name, amount in figures, amount in words, date, and signature presence. A fabricated payee name or an altered amount causes a direct loss. The scan volume is 40,000 cheques per day.

**Question.** Which TWO items are hard constraints for the design? Select TWO.

**Options.**
A) The system must support three languages by launch.
B) No payment on a cheque whose amount fields disagree.
C) No fabricated payee names may reach the payment step.
D) Cost per cheque must stay under $0.01.
E) The p95 latency must stay under 30 seconds.

**Answer.** B, C

**Method walk (Steps 1-10).**
1. Question type: constraint identification (multi-select).
2. Lifecycle stage: discovery.
3. Objective: separate hard constraints from goals.
4. Hard constraints: the scenario names direct loss from fabricated payees and altered amounts.
5. System layer: requirements translation.
6. Eliminate infeasible: all five are feasible requirements.
7. Eliminate constraint-violating: A, D, E are real goals but none is stated as must-never-happen.
8. Compare on objective: only B and C name conditions that must never occur.
9. Hidden dependencies: B needs both amount fields parsed, C needs a check against a trusted payee source.
10. Verify: B and C together, no third fits the "must never happen" test.

**Explanation.**
1. Correct answer: B, C.
2. Decisive scenario phrase: "A fabricated payee name or an altered amount causes a direct loss."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Violation causes direct loss | No | Yes | Yes | No | No |
| Stated as must-never-happen | No | Yes | Yes | No | No |

4. Why B and C satisfy all hard constraints: a hard constraint is a condition that must never occur, B and C are the only options stated that way, each tied to direct loss.
5. Why B and C best meet the objective: V2-D1.1 requires naming hard constraints before lane choice, the design forks around exactly these two gates.
6. Every rejected choice explained: A is a launch goal, not a never-event, missing a language delays launch but causes no loss. D is a budget target, exceeding it is a business decision, not a loss event. E is a nonfunctional requirement, a slow cheque causes delay, not loss.
7. Exact limitation or tradeoff: treating only B and C as hard means A, D, E can slip, the team must still track them as goals with owners.
8. Relevant evidence (with date): hard-constraint definition from lesson-D1-1 (§4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins as the hard constraint if a regulator fines the bank per unsupported language. D wins if the business case goes negative above $0.01 (then it is a build/no-build gate). E wins if a clearing window closes at 30 s and late cheques are rejected with fees.
10. Misconception tested: every numbered requirement is a hard constraint. It is not. Goals have thresholds and owners, hard constraints have gates.

## Q-D1-04 (V2-D1.1)

**Scenario.** A logistics firm routes all 10,000 daily invoices through Claude on the Fast tier. 80% have a fixed layout. Monthly model cost is $540. The CFO asks for the single change that cuts cost most while keeping field precision at or above 98%.

**Question.** Which change best meets the goal?

**Options.**
A) Switch all traffic to the most capable tier for better precision.
B) Fork the 80% fixed-layout invoices to a deterministic parser, keep Claude on the 20% open scans, keep the total-check gate.
C) Add explicit reasoning to every call to raise precision.
D) Cache the full conversation including the variable invoice tail.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best optimization action under a quality floor.
2. Lifecycle stage: operation (iteration).
3. Objective: cut cost with precision at or above 98%.
4. Hard constraints: precision floor 98%, gate on totals stays.
5. System layer: lane assignment.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright, but A raises cost (wrong direction).
8. Compare on objective: only B cuts cost, the lesson toy prices it at $132/month vs $540.
9. Hidden dependencies: the parser needs the fixed layout spec, the gate still sees every total.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "80% have a fixed layout" plus "precision at or above 98%".
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Cuts monthly cost | No | Yes | No | No |
| Keeps precision floor | Yes | Yes | Yes | Yes |
| Keeps the total gate | Yes | Yes | Yes | Yes |

4. Why B satisfies all hard constraints: the parser handles fixed layouts deterministically (precision risk falls, not rises), Claude keeps the open 20%, and the gate stays on every total.
5. Why B best meets the objective: on the lesson toy, hybrid costs $4.40/day ($132/month) against $18/day ($540/month) all-Claude, a 4x cut with the quality floor held by the fork and the gate.
6. Every rejected choice explained: A moves cost the wrong way ($72/day on the Capable toy) with no eval showing the gain. C adds output tokens and latency to 10,000 calls a day while the bar is already met. D caches a variable tail, so the prefix never stabilizes and the hit rate sits near zero while writes keep billing.
7. Exact limitation or tradeoff: B needs the parser maintained as layouts drift, a new supplier layout must route to Claude until the parser learns it.
8. Relevant evidence (with date): fork arithmetic from lesson-D1-1 (§5), Oct 6 2026, tier pricing S10-S12, Oct 2026, verify against official docs, cache prefix rule from lesson-D2-5, Oct 6 2026.
9. Counterfactual where each plausible alternative wins: A wins if evals show the Fast tier below the 98% floor and the capable tier above it. C wins if errors concentrate on hard scans where steps are checkable. D wins if the tail were stable (it is not here).
10. Misconception tested: cost cutting means a cheaper model. Here the cut comes from lane choice, not tier choice.

## Q-D1-05 (V2-D1.2)

**Scenario.** A clinic drafts discharge notes with Claude. A wrong dose harms a patient. An auditor must replay any note from six months ago and see exactly what the model saw and checked.

**Question.** Which architecture best fits?

**Options.**
A) A single Claude call with a careful system prompt, prompts are logged.
B) Seven gates: input, validation, context and retrieval, model and tools, verification, output, feedback. Validation and authorization run in code before context assembly. Every hop emits a trace with one request id, the trace carries input hash, chunk ids, the draft, and the check result.
C) A Claude call plus a nurse who reads every draft, the nurse's approval is the trace.
D) Two Claude calls: one drafts, one reviews. The review call is the verification gate.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: architecture interpretation.
2. Lifecycle stage: design.
3. Objective: safe notes with full replay six months later.
4. Hard constraints: wrong dose harms, replay must show what the model saw and checked, state and checks in code.
5. System layer: end-to-end pipeline plus observability.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A cannot show what the model saw (no retrieval record, no check record), C makes the nurse the trace, so the model context is unrecorded, D has the reviewer see only the draft, not the retrieved source chunks.
8. Compare on objective: only B records the full chain the auditor needs.
9. Hidden dependencies: B needs a system of record for the dose facts and retention for the traces.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "replay any note from six months ago and see exactly what the model saw and checked."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Gate before the model in code | No | Yes | No | No |
| Verification against source | No | Yes | Partial | Partial |
| Replay shows retrieved facts | No | Yes | No | No |
| Trace survives six months | No | Yes | No | No |

4. Why B satisfies all hard constraints: validation and authorization run in code at the trust boundary, verification checks the draft against retrieved chunks, per-stage traces with one request id make any run replayable.
5. Why B best meets the objective: V2-D1.2 names the seven gates and the trace content (input hash, chunk ids, draft, check result) as the mechanism for exactly this audit demand.
6. Every rejected choice explained: A hopes the prompt validates input and verifies output, hope is not a gate, and prompt logs do not record retrieved chunks. C puts the human in the loop but leaves the model context unrecorded, the auditor cannot see what the draft was checked against. D improves the draft but the reviewer call sees only the draft text, so a dose error with no source comparison can still pass.
7. Exact limitation or tradeoff: B is the heaviest build of the four, trace storage for every note has a real retention cost.
8. Relevant evidence (with date): seven gates and trace content from lesson-D1-2 (§3-§5), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for an internal demo with no patients and no audit (lesson-D1-2 counterfactual). C wins at 50 notes a day where each note carries legal risk and the nurse sees the retrieved sources too. D wins when the check is stylistic (tone, format), not factual.
10. Misconception tested: a second model call equals verification. It does not unless the check compares the draft against the source in a recorded way.

## Q-D1-06 (V2-D1.2), Select TWO

**Scenario.** A payment support bot issues refunds through a tool. After an incident where a refund went to the wrong account, the team must be able to replay any refund decision and name the exact hop that authorized it.

**Question.** Which TWO trace contents are mandatory for the replay? Select TWO.

**Options.**
A) The model temperature and top-p used at generation time.
B) The retrieved account record the amount was checked against, with its id.
C) The per-hop record showing which gate authorized the refund, tied to one request id.
D) The full prompt text with all few-shot examples.
E) The GPU cluster region that served the call.

**Answer.** B, C

**Method walk (Steps 1-10).**
1. Question type: control placement for audit replay (multi-select).
2. Lifecycle stage: design (observability design).
3. Objective: replay any refund and name the authorizing hop.
4. Hard constraints: money moved, audit must name the hop, end-to-end reconstructability.
5. System layer: observability (V2-D3.4) inside the seven gates.
6. Eliminate infeasible: all are recordable.
7. Eliminate constraint-violating: A, D, E record facts that cannot name the authorizing hop or the checked record.
8. Compare on objective: only B gives the source of truth for the amount, only C names the authorizing gate.
9. Hidden dependencies: the account record id must come from the system of record, not the draft.
10. Verify: B and C together, adding D is nice but not mandatory for the stated objective.

**Explanation.**
1. Correct answer: B, C.
2. Decisive scenario phrase: "name the exact hop that authorized it."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Names the checked record | No | Yes | No | No | No |
| Names the authorizing hop | No | No | Yes | No | No |
| Tied to one request id | No | Yes | Yes | No | No |

4. Why B and C satisfy all hard constraints: B carries the system-of-record facts the amount was checked against, C carries per-hop authorization under one id, so the replay names the gate.
5. Why B and C best meet the objective: V2-D1.2 and V2-D3.4 require per-stage traces with one request id and the source facts, which is exactly B plus C.
6. Every rejected choice explained: A records sampler settings, they cannot name a hop or a record. D is bulky context that shows what the model saw but not which gate authorized the money move. E is infrastructure trivia with no audit value.
7. Exact limitation or tradeoff: B and C do not record why the model chose the draft, they record what was checked and who authorized, which is what the auditor asked for.
8. Relevant evidence (with date): trace content list from lesson-D1-2 (§5), Oct 6 2026, "sample deep, skeleton the rest, keep all errors" from lesson-D3-4, Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when debugging a quality regression across a sampler change. D wins when the dispute is about prompt content (e.g., a stale instruction). E wins for a latency or residency incident, not an authorization replay.
10. Misconception tested: more logged data equals better audit. It does not. The audit needs the record and the hop, not the sampler.

## Q-D1-07 (V2-D1.2)

**Scenario.** A support bot quotes prices from a product catalog. Users report wrong prices on 3% of answers. The traces show: validation passed, retrieval returned the 2024 price list, the model quoted those prices faithfully, and the verification check compared each claim against the retrieved chunks and passed.

**Question.** Which gate is the root cause, and what is the best fix?

**Options.**
A) The verification gate, make the model check prices twice.
B) The context and retrieval gate, the index holds a stale 2024 price list, so re-ingest the current catalog.
C) The model, move to a more capable tier.
D) The output gate, add a regex for price formats.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: root cause from traces.
2. Lifecycle stage: incident response.
3. Objective: correct prices.
4. Hard constraints: the fix must address the failing layer, verification passed, so the draft matched its source.
5. System layer: context and retrieval.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: the trace indicts retrieval (stale list), the check passed because the draft matched stale facts. Fix the failing component, not a proxy.
9. Hidden dependencies: re-ingestion needs the current catalog as the system of record and a freshness check.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "retrieval returned the 2024 price list" while "the verification check ... passed."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixes the indicted layer | No | Yes | No | No |
| Addresses stale facts | No | Yes | No | No |
| Keeps the passing gates intact | Yes | Yes | Yes | Yes |

4. Why B satisfies all hard constraints: the trace shows verification did its job (draft matched source), the fault is upstream, so the fix re-ingests the current catalog into the index.
5. Why B best meets the objective: V2-D1.2 and V2-D4.4 require fixing the failing component, not a proxy, every other option polishes a gate that already passed.
6. Every rejected choice explained: A doubles a check that already passed, it cannot see that the source is stale. C is the classic proxy fix: a bigger tier quoting the same stale list gives the same wrong prices at higher cost. D validates price format, but the prices were well-formed and wrong.
7. Exact limitation or tradeoff: re-ingestion fixes staleness but not retrieval ranking, if wrong-chunk errors appear next, the fix moves to chunk size and boundaries.
8. Relevant evidence (with date): "fix the failing component, not a proxy" from lesson-D3-5 (§9) and lesson-D4-4 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the draft contradicted the chunks and the check missed it (verification fault). C wins if traces show the model misread fresh chunks (model fault). D wins if wrong prices came from malformed model output, not stale facts.
10. Misconception tested: a passing verification proves the answer is right. It proves only that the draft matches its source. A stale source passes every check.

## Q-D1-08 (V2-D1.2)

**Scenario.** A team ships a Claude support bot handling 50,000 answers per day. The verification gate catches 2% of drafts with unsupported claims, and those drafts ship anyway because "the reviewers will catch them." The proposal on the table: put a human reviewer on every answer.

**Question.** What is the best next action?

**Options.**
A) Approve the reviewer plan, human review is the strongest safety control.
B) Block the 2% failed drafts from shipping in code, then fix the retrieval or prompt cause of the failures, do not add universal review.
C) Hire a review vendor and sample 10% of answers for review.
D) Remove the verification gate since its failures ship anyway.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: next action on a broken control.
2. Lifecycle stage: operation (incident response).
3. Objective: stop unsupported claims from shipping.
4. Hard constraints: 50,000 answers per day, failed checks currently ship, the gate exists but has no teeth.
5. System layer: verification gate plus feedback.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: D removes a working detector, A needs 50,000 x 30 s = 417 reviewer-hours per day.
8. Compare on objective: B enforces the existing gate in code and attacks the cause, C samples but lets 90% of failures through.
9. Hidden dependencies: blocking needs the check result wired to the ship decision, the cause fix needs the failure traces.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "those drafts ship anyway because 'the reviewers will catch them.'"
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Failed drafts stop shipping | Partial | Yes | Partial | No |
| Feasible at 50k/day | No | Yes | Yes | Yes |
| Fixes the cause | No | Yes | No | No |

4. Why B satisfies all hard constraints: the gate's verdict becomes the ship decision in code (fail closed), and the team fixes the layer the failure traces indict.
5. Why B best meets the objective: V2-D1.2 says each gate has one job and a gate never borrows another's, verification that does not block is decoration, and universal review is 417 reviewer-hours per day that fixes nothing.
6. Every rejected choice explained: A is valid as an instinct but infeasible at this volume and leaves the failing stage failing. C is cheaper than A but still lets most failures ship and never fixes the cause. D destroys the detector instead of giving it teeth, the team would then ship blind.
7. Exact limitation or tradeoff: blocking on the check can raise false-positive blocks, the cause fix must follow quickly or the block rate becomes a product problem.
8. Relevant evidence (with date): "gate is mandatory... reviewer on every answer" valid-but-inferior from lesson-D1-2 (§10), Oct 6 2026, "controls must fail closed" from V2-D5.1 scope, exam via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins at 100 answers a day with legal exposure per answer. C wins when failures are rare and the sample feeds a labeled set for eval. D wins if the gate's false-positive rate exceeds its catch rate and a better check replaces it.
10. Misconception tested: a detector plus a hope equals a control. Without the block wired in code, the gate is a dashboard, not a guardrail.

## Q-D1-09 (V2-D1.3)

**Scenario.** A warehouse handles returns. 90% are unopened boxes with a barcode: scan, check the order, refund. 10% are damaged goods needing a judgment call on restocking vs write-off. A wrong refund costs the item margin. The error cost is high and refunds are hard to reverse.

**Question.** Which pattern fits best?

**Options.**
A) One agent handles every return end to end.
B) A deterministic workflow handles the 90% barcode cases. Claude handles the 10% judgment cases with a gate on every refund. Code verifies the order and the amount before money moves.
C) An augmented single call: Claude sees the barcode scan and decides every case with tools.
D) A multi-agent team: one agent per return, coordinated by a supervisor agent.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best architecture under constraints.
2. Lifecycle stage: design.
3. Objective: correct refunds with bounded cost.
4. Hard constraints: wrong refund costs margin, refunds hard to reverse, 90/10 split.
5. System layer: orchestration pattern.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A and D give an agent unsupervised money moves (high error cost, low reversibility pushes left on the spectrum), C uses the model for fixed barcode steps at model price with no gate named.
8. Compare on objective: B matches the 90/10 split and puts the gate where the money moves.
9. Hidden dependencies: the barcode lookup must hit the order system of record, the gate needs the amount and the policy.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "A wrong refund costs the item margin" plus "90% are unopened boxes with a barcode."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixed cases deterministic | No | Yes | No | No |
| Judgment cases get the model | Yes | Yes | Yes | Yes |
| Gate on every refund | No | Yes | No | No |
| Cost fits the 90/10 split | No | Yes | Partial | No |

4. Why B satisfies all hard constraints: fixed steps go left on the spectrum (deterministic workflow), the judgment 10% gets Claude, the code gate enforces the high-error-cost rule before money moves.
5. Why B best meets the objective: the pattern spectrum scores on predictability, reversibility, error cost, latency, and cost, high error cost with low reversibility pushes left, while the open 10% needs the model. B is the hybrid the spectrum prescribes.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: it handles the open 10% but pays agent cost on the fixed 90% and varies run to run on fixed cases ($480/day vs $55.40 on the lesson toy). C pays model price for barcode parsing and names no gate on the refund. D adds coordination overhead (supervisor plus workers) for work that needs no planning, traces would show a plan the team never wrote.
7. Exact limitation or tradeoff: B needs the barcode rule set and the refund policy maintained, damaged-goods edge cases outside the 10% still need a fallback route.
8. Relevant evidence (with date): pattern spectrum and hybrid verdict from lesson-D1-patterns (§9, V2-D1.3), Oct 6 2026, refund toy ($480 vs $55.40/day) from the same lesson, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for open-ended research where steps are unknown until runtime. C wins when every case needs one judgment plus tools and steps are few. D wins when returns split into independent specialist tracks with a deadline (V2-D1.4 territory).
10. Misconception tested: one agent for everything is the modern default. The spectrum says the task shape decides, fixed bones go deterministic.

## Q-D1-10 (V2-D1.3)

**Scenario.** A document pipeline chains 12 Claude calls in fixed order: extract, classify, summarize, check, format, and seven more steps. Traces show each step rewrites the draft, errors compound across steps, and total latency is the sum of all 12 calls. The steps are fixed and known in advance.

**Question.** What is the best next action?

**Options.**
A) Move to a more capable tier so each step makes fewer errors.
B) Replace the chain with fan-out and fan-in: run the independent extractions in parallel, merge with a validation gate, and move the certain sub-tasks (format checks, totals) into deterministic code.
C) Add a 13th call where a second model reviews the final draft.
D) Add prompt caching on the full conversation to cut latency.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best next action on a diagnosed architecture fault.
2. Lifecycle stage: operation (optimization).
3. Objective: cut compounded errors and summed latency.
4. Hard constraints: steps fixed and known, errors compound across rewrites, latency sums.
5. System layer: orchestration pattern.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B attacks both failure modes (parallelism cuts summed latency, no rewrites cut compounding, deterministic code removes model variance on certain tasks).
9. Hidden dependencies: fan-out needs independence verified per piece, the merge needs a validation gate with a citation or totals check.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "each step rewrites the draft, errors compound" and "total latency is the sum of all 12 calls."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Stops error compounding | No | Yes | Partial | No |
| Cuts summed latency | No | Yes | No | Partial |
| Certain tasks deterministic | No | Yes | No | No |

4. Why B satisfies all hard constraints: parallel independent work removes the latency sum, the merge gate checks the combined result, deterministic code does the certain sub-tasks with zero model variance.
5. Why B best meets the objective: V2-D1.5 names fan-out/fan-in for independent pieces and the deterministic split for certain sub-tasks, V2-D1.3 pushes fixed known steps left on the spectrum.
6. Every rejected choice explained: A is the proxy fix, a bigger tier still rewrites the draft 12 times and still sums latency, at higher cost. C adds a 13th rewrite to a pipeline whose disease is rewrites. D helps only if the prefix is stable, a 12-step chain with a changing draft defeats the prefix rule, and caching does not fix compounding errors.
7. Exact limitation or tradeoff: B needs the independence of pieces proven and a merge contract written, misjudged independence creates merge conflicts.
8. Relevant evidence (with date): "chain everything" valid-but-inferior and fan-out verdict from lesson-D1-patterns (§10, V2-D1.5), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if traces show one step's errors dominate and that step is genuinely hard (model fault). C wins as a cheap critique pass when the chain is short and the check is checkable. D wins when the chain shares a large stable prefix and latency, not errors, is the complaint.
10. Misconception tested: chaining is the safe default because failures point at one step. Clear failure attribution does not fix compounding, the pattern must match the independence of the work.

## Q-D1-11 (V2-D1.3)

**Scenario.** An analyst asks the system: "Find everything about this new supplier: ownership, financial health, sanctions exposure, and news from the last year." No one can list the research steps in advance, each finding decides the next search.

**Question.** Which pattern fits best?

**Options.**
A) A deterministic workflow with the ten research steps fixed in order.
B) An agentic loop: the model plans, searches with tools, reads results, and replans until the brief is covered or a step budget is hit.
C) An augmented single call with all ten searches in one prompt.
D) A hybrid: deterministic steps for the fixed lookups, and no model involvement.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best architecture under constraints.
2. Lifecycle stage: design.
3. Objective: complete open-ended research.
4. Hard constraints: steps unknown until runtime, each finding decides the next search.
5. System layer: orchestration pattern.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A requires steps known in advance (they are not), D excludes the model from work that needs language judgment.
8. Compare on objective: only B plans dynamically, which is the task itself here.
9. Hidden dependencies: B needs a step budget, tool result limits, and a coverage checklist so the loop terminates.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "No one can list the research steps in advance, each finding decides the next search."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Handles unknown steps | No | Yes | No | No |
| Replans on findings | No | Yes | No | No |
| Terminates | Yes | With budget | Yes | Yes |

4. Why B satisfies all hard constraints: the agent loop is the pattern for unknown steps, the step budget and coverage checklist keep it terminating.
5. Why B best meets the objective: V2-D1.3 says steps unknown and task open means agentic, dynamic planning is the task, not overhead.
6. Every rejected choice explained: A is infeasible in the strong sense: a workflow cannot list steps that do not exist until the search runs. C stuffs ten searches into one call with no replanning, the first surprising finding has nowhere to go. D removes the judgment the task needs.
7. Exact limitation or tradeoff: B costs more per task and its path varies run to run, the step budget caps the cost but can cut a deep trail short.
8. Relevant evidence (with date): open-research counterfactual from lesson-D1-patterns (§11, V2-D1.3), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the research is a fixed checklist (same ten sources every time). C wins for one lookup with one judgment plus tools. D wins when the "research" is a fixed database query with no judgment.
10. Misconception tested: agents are always the answer for research. They are the answer only when the steps are unknowable in advance.

## Q-D1-12 (V2-D1.3), Select THREE

**Scenario.** A team must match four work types to patterns. The work types: (1) parse fixed-format EDI orders, (2) draft a custom reply to an angry customer email, (3) run a fixed 6-step nightly reconciliation, (4) investigate a novel production incident with unknown cause.

**Question.** Which THREE pattern matches are correct? Select THREE.

**Options.**
A) EDI orders: deterministic workflow or parser code, no model needed.
B) Angry customer email: augmented single call (one judgment plus tools), with a tone and facts check before send.
C) Nightly reconciliation: agentic loop so the system can discover new steps each night.
D) Novel incident: agentic loop with a step budget, since the steps are unknown until the investigation runs.
E) EDI orders: most capable tier with explicit reasoning for maximum accuracy.

**Answer.** A, B, D

**Method walk (Steps 1-10).**
1. Question type: pattern matching (multi-select).
2. Lifecycle stage: design.
3. Objective: one correct pattern per work type.
4. Hard constraints: fixed mapping goes deterministic, open judgment gets the model with a gate, unknown steps need dynamic planning.
5. System layer: orchestration pattern.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: C gives an agent fixed known steps (planning overhead with nothing to plan), E pays model price for a fixed mapping.
8. Compare on objective: A, B, D each match task shape to pattern.
9. Hidden dependencies: B needs the facts check against the order record, D needs the step budget.
10. Verify: A, B, D. Three selected, C and E rejected.

**Explanation.**
1. Correct answer: A, B, D.
2. Decisive scenario phrase: "fixed-format", "custom reply", "fixed 6-step", "unknown cause."
3. Requirement-to-option matrix:

| Work type | A | B | C | D | E |
|---|---|---|---|---|---|
| EDI: fixed mapping | Yes | n/a | n/a | n/a | No |
| Email: one judgment plus tools | n/a | Yes | n/a | n/a | n/a |
| Reconciliation: steps fixed | n/a | n/a | No | n/a | n/a |
| Incident: steps unknown | n/a | n/a | n/a | Yes | n/a |

4. Why A, B, D satisfy all hard constraints: A puts fixed mapping in code, B gives the judgment case one model call plus a check, D gives the unknown-step case dynamic planning with a budget.
5. Why A, B, D best meet the objective: each matches the V2-D1.3 spectrum rule (steps fixed and known go deterministic, one judgment plus tools is the augmented call, steps unknown is agentic).
6. Every rejected choice explained: C is the "agent for everything" slogan applied to a fixed checklist, the steps never change, so planning is pure overhead and the path varies for no reason. E pays the most capable tier with reasoning for a fixed-format parse that a parser does deterministically, no eval can justify the cost.
7. Exact limitation or tradeoff: B still needs the facts check (the model must not invent order details), D's budget can cut a deep investigation short.
8. Relevant evidence (with date): spectrum verdicts from lesson-D1-patterns (§9, V2-D1.3), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the reconciliation steps genuinely change nightly based on findings. E wins if the EDI format breaks often and the layout is no longer fixed.
10. Misconception tested: the fanciest pattern fits every work type. The spectrum matches shape to pattern, one work type at a time.

## Q-D1-13 (V2-D1.4)

**Scenario.** A proposal team must produce a bid in 6 hours. Three independent specialist reviews run in parallel: technical, pricing, and legal. Each review needs deep focus on its own documents. The three reviews merge into one bid with a single consistent voice.

**Question.** Which orchestration fits best?

**Options.**
A) A single agent with all tools does the three reviews in sequence.
B) A coordinator with three specialist workers: each worker owns one review under a handoff contract (input documents, output format, merge rule), the coordinator merges, checkpoints save each handoff.
C) Three independent agents with no coordinator and no merge step, the bid team stitches the outputs by hand.
D) A deterministic workflow that runs the three reviews in sequence with no model.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best architecture under constraints.
2. Lifecycle stage: design.
3. Objective: three deep reviews merged in 6 hours.
4. Hard constraints: reviews independent, deadline 6 hours, one consistent merged bid, work must survive worker failure.
5. System layer: multi-agent orchestration.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: C has no merge and no contract, so coherence fails, D removes the judgment the reviews need.
8. Compare on objective: B parallelizes with contracts, A is valid but sequential (48 s vs 24 s on the lesson toy) and dilutes focus in one long context.
9. Hidden dependencies: the handoff contract needs the merge rule and the output format, checkpointing covers worker failure.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Three independent specialist reviews" plus "merge into one bid."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Parallel independent work | No | Yes | Yes | No |
| Handoff contract and merge | N/A | Yes | No | N/A |
| Survives worker failure | Yes | Yes | No | Yes |
| Meets the deadline | Risky | Yes | Risky | No |

4. Why B satisfies all hard constraints: workers run in parallel (the deadline), contracts name input, output, and merge rule (coherence), and checkpointing saves each handoff (resume on failure).
5. Why B best meets the objective: V2-D1.4 prescribes coordinator/worker with handoff contracts exactly when work splits into independent specialist tracks with a merge.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: simpler and 30% cheaper on the toy, but sequential latency on parallelizable work and one long context dilutes focus across three reviews. C has no merge, no contract, and no single report, coherence is hoped for. D drops the model from reviews that need judgment.
7. Exact limitation or tradeoff: B costs more (coordination plus contracts) and needs the merge rule designed up front, a bad merge rule produces a consistent but wrong bid.
8. Relevant evidence (with date): coordinator/worker verdict and the 48 s vs 24 s toy from lesson-D1-patterns (§9-§10, V2-D1.4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the three reviews share one evolving context (entangled work, splitting shreds context). C wins never as a design, it is a hope. D wins when the reviews are checklist verifications with no judgment.
10. Misconception tested: multi-agent is always better for parallel work. It wins only with contracts, a merge, and checkpointing, otherwise it is three agents and a prayer.

## Q-D1-14 (V2-D1.4)

**Scenario.** A procurement lead negotiates with one supplier over five rounds. Each round depends on the last: the supplier's concession shapes the next ask. The full history must stay in view. The team proposes splitting the negotiation across three worker agents coordinated by a supervisor.

**Question.** What is the best response to the proposal?

**Options.**
A) Approve, more agents mean faster rounds.
B) Reject the split, use a single agent with tools. The work is entangled, and handoffs would carry the whole history anyway.
C) Approve but add a fourth agent to check the other three.
D) Replace the agents with a deterministic workflow of five fixed rounds.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: architecture judgment (accept or reject a proposal).
2. Lifecycle stage: design.
3. Objective: effective negotiation support.
4. Hard constraints: each round depends on the last, full history must stay in view.
5. System layer: orchestration (single vs multi-agent).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright, but A/C/D mismatch the work shape.
8. Compare on objective: B keeps the shared evolving context in one loop, splitting shreds it.
9. Hidden dependencies: the single agent needs the full history in context and a round log.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Each round depends on the last" and "The full history must stay in view."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Shared evolving context kept | No | Yes | No | No |
| No history-shredding handoffs | No | Yes | No | No |
| Handles adaptive rounds | Yes | Yes | Yes | No |

4. Why B satisfies all hard constraints: one loop holds the whole history, no handoff needs to re-carry it, the agent adapts each round.
5. Why B best meets the objective: V2-D1.4 says one entangled task with shared evolving context goes to a single agent plus tools, contracts would rot because handoffs shift every round.
6. Every rejected choice explained: A splits entangled work, each handoff must carry the full history, so the split buys coordination cost with no parallelism gain. C adds a checker to a broken split, the disease is the split, not the lack of checking. D fixes five rounds in advance, but the rounds adapt to concessions, fixed steps cannot adapt.
7. Exact limitation or tradeoff: the single agent's context grows over five rounds, the team must watch for dilution and compact between rounds if needed.
8. Relevant evidence (with date): negotiation counterfactual from lesson-D1-patterns (§11, V2-D1.4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the work splits into independent tracks (e.g., three suppliers negotiated in parallel). C wins when the task needs a critic pass on a finished draft (V2-D1.5 critique). D wins when the rounds are a fixed script with no adaptation.
10. Misconception tested: splitting work across agents is always parallelization. For entangled work it is fragmentation, the handoffs cost more than they save.

## Q-D1-15 (V2-D1.4), Select TWO

**Scenario.** A coordinator agent fans out document reviews to worker agents. The team writes the handoff contract between coordinator and workers.

**Question.** Which TWO elements must the handoff contract name? Select TWO.

**Options.**
A) The input documents and the required output format for each worker.
B) The merge rule the coordinator uses to combine worker outputs.
C) The preferred writing style and personality of each worker.
D) The model tier each worker must use.
E) The office hours during which workers may run.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: contract content (multi-select).
2. Lifecycle stage: design.
3. Objective: a handoff contract that prevents incoherence.
4. Hard constraints: workers need bounded inputs and a defined output, the coordinator needs a merge rule.
5. System layer: multi-agent orchestration.
6. Eliminate infeasible: all are writable.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A bounds the work, B defines the merge, C, D, E are style or ops details that do not prevent incoherence.
9. Hidden dependencies: the merge rule needs the output format to merge against.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "handoff contract between coordinator and workers."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Prevents incoherent handoffs | Yes | Yes | No | No | No |
| Needed for the merge | Yes | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: A names what each worker gets and must return, B names how the pieces combine into one report.
5. Why A and B best meet the objective: V2-D1.4 defines the handoff contract as input, output, and the merge rule, without B, three good reviews never become one bid.
6. Every rejected choice explained: C is style guidance, it does not bound the work or define the merge. D is an ops choice the coordinator can set per worker, not a contract term that prevents incoherence. E is a calendar detail.
7. Exact limitation or tradeoff: A and B do not cover failure handling, the design still needs the disagreement rule and checkpointing named elsewhere.
8. Relevant evidence (with date): handoff contract definition from lesson-D1-patterns (V2-D1.4), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the deliverable is customer-facing prose with a brand voice requirement (then tone is a contract term). D wins if tier choice affects the quality floor per worker and evals prove it. E wins never as a contract term.
10. Misconception tested: a contract is a long document. It is three things: input, output, merge rule. Everything else is appendix.

## Q-D1-16 (V2-D1.4)

**Scenario.** Two worker agents review the same vendor contract. Worker 1 rates the liability clause "acceptable." Worker 2 rates it "high risk." The coordinator must produce one rating. The contract has no disagreement rule.

**Question.** What is the best design fix?

**Options.**
A) Average the two ratings and ship "medium risk."
B) Add a named disagreement rule: route conflicts to a critic pass with the clause text and both rationales, then escalate to a human reviewer if the critic cannot resolve with evidence.
C) Let the coordinator pick whichever rating arrived first.
D) Add a third worker and take the majority vote.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: control design for disagreement.
2. Lifecycle stage: design (fix).
3. Objective: one defensible rating from conflicting workers.
4. Hard constraints: the rating must rest on evidence, liability risk is high-stakes.
5. System layer: multi-agent orchestration (disagreement handling).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A invents a rating neither worker gave, C is arbitrary.
8. Compare on objective: B resolves on evidence and escalates on genuine uncertainty.
9. Hidden dependencies: the critic needs the clause text and both rationales, the human needs real decision context.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The contract has no disagreement rule."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Rating rests on evidence | No | Yes | No | Partial |
| Handles genuine uncertainty | No | Yes | No | No |
| Deterministic rule, not luck | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: the critic re-examines with both rationales and the source text, escalation puts true uncertainty before a human with context.
5. Why B best meets the objective: V2-D1.4 requires disagreement handling in the design, a named rule beats hoping the coordinator guesses right.
6. Every rejected choice explained: A averages two judgments into a third judgment no one made, "medium risk" is a number without a reason. C is nondeterminism dressed as a rule, arrival order is not evidence. D is better than C but majority vote on two voters plus one more is still a vote, not a reason, it can also entrench a shared blind spot.
7. Exact limitation or tradeoff: B adds a critic call and possible human latency, the team must define "cannot resolve" crisply or everything escalates.
8. Relevant evidence (with date): disagreement handling requirement from V2-D1.4 scope, exam via S03/S04, Sept 2026, critique pattern from lesson-D1-patterns (V2-D1.5), Oct 6 2026, "reviewers need real decision context" from V2-D5.3 scope.
9. Counterfactual where each plausible alternative wins: A wins for low-stakes numeric estimates where the mean is the estimator (e.g., story points). C wins never as a design. D wins when voters are independent and numerous and the task is a classification with a clear label set.
10. Misconception tested: any aggregation rule resolves disagreement. Aggregation without evidence produces a confident-sounding fiction.

## Q-D1-17 (V2-D1.5)

**Scenario.** An analyst firm produces earnings briefs. Every number in the brief must carry a citation to the source filing. The brief has 12 independent sections. A deterministic script can verify that the totals match the cited tables.

**Question.** Which decomposition fits best?

**Options.**
A) Chain all 12 sections in order through one long agent run.
B) Fan out the 12 independent sections to parallel workers, each attaching citations per number, fan in with a merge, run the deterministic totals check on the merged brief.
C) One augmented call writes the whole brief, then a second call adds citations from memory.
D) Twelve sequential calls, each rewriting the full draft so far.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best decomposition under constraints.
2. Lifecycle stage: design.
3. Objective: 12 cited sections with verified totals.
4. Hard constraints: every number cited, sections independent, totals must check.
5. System layer: decomposition.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A and D let one running draft carry unattributed numbers (traceability fails), C invents citations from memory.
8. Compare on objective: B gives each number a source at creation and checks totals in code.
9. Hidden dependencies: the citation format contract must be shared, the totals script needs the cited tables.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Every number in the brief must carry a citation" plus "12 independent sections."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Per-number citation at creation | No | Yes | No | No |
| Parallel independent work | No | Yes | No | No |
| Deterministic totals check | No | Yes | No | No |

4. Why B satisfies all hard constraints: fan-out matches independence, per-number citations satisfy traceability, the code check verifies totals against cited tables.
5. Why B best meets the objective: V2-D1.5 names fan-out/fan-in for independent pieces, the validation gate on the merge, and the deterministic split for certain sub-tasks (totals).
6. Every rejected choice explained: A is the lesson's valid-but-inferior chain: 12 sequential calls sum latency and each rewrite risks unattributed numbers. C asks the model to recall citations, recalled citations are the exact failure the requirement forbids. D is A's slower cousin: each step rewrites the draft, so errors compound and citations drift.
7. Exact limitation or tradeoff: B needs the merge to preserve every citation, a sloppy merge drops sources and the check passes on a thinner brief.
8. Relevant evidence (with date): fan-out/fan-in and validation-gate verdicts from lesson-D1-patterns (§9, V2-D1.5), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when section order matters and each section's output feeds the next (true chain). C wins never for cited work. D wins never, it is the anti-pattern the lesson names.
10. Misconception tested: citations can be added after the draft. They cannot be trusted then, the citation must attach at the moment the number is written.

## Q-D1-18 (V2-D1.5)

**Scenario.** A team routes incoming support tickets. The router must first decide the ticket type (billing, technical, account), then handle each type differently. Billing tickets need a deterministic balance lookup before any reply. Technical tickets need a judgment call with tools. The team built one chain that runs every ticket through all steps in order.

**Question.** What is the best first change?

**Options.**
A) Add a route step at the front: classify the ticket, then send billing tickets to the deterministic lookup path and technical tickets to the agent path.
B) Add explicit reasoning to every step of the existing chain.
C) Move the whole chain to the most capable tier.
D) Cache the chain's full conversation to cut latency.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: best first action (decomposition fix).
2. Lifecycle stage: operation (redesign).
3. Objective: right handling per ticket type without wasted steps.
4. Hard constraints: billing needs a deterministic lookup first, technical needs judgment, the current chain runs all steps for all tickets.
5. System layer: decomposition (routing pattern).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A sends each ticket down its own path, B, C, D polish a chain whose shape is the problem.
9. Hidden dependencies: the classifier needs the ticket-type taxonomy, the billing path needs the balance system.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "runs every ticket through all steps in order" though "each type" needs different handling.
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Billing gets deterministic lookup | Yes | Partial | Partial | Partial |
| Technical gets judgment | Yes | Yes | Yes | Yes |
| No wasted steps per ticket | Yes | No | No | No |

4. Why A satisfies all hard constraints: the route step classifies first, each type then follows its own path with the right tool or lane.
5. Why A best meets the objective: V2-D1.5 names routing as the decomposition move for mixed work, the chain is the wrong shape for typed work.
6. Every rejected choice explained: B adds reasoning tokens to steps that should not run at all for a given ticket. C pays the top tier for a shape problem, the wasted steps still run. D caches a chain whose prefix changes per ticket type, the hit rate will disappoint and the shape stays wrong.
7. Exact limitation or tradeoff: A needs the classifier to be right, a misrouted ticket gets the wrong path, so the router needs its own eval and a fallback.
8. Relevant evidence (with date): routing pattern from lesson-D1-patterns (V2-D1.5), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins when one path's steps are checkable and hard (reasoning helps). C wins when evals show the current tier below the quality floor on the judgment path. D wins when one path dominates volume with a stable prefix.
10. Misconception tested: one pipeline can serve mixed work if it is long enough. Length is not routing, typed work needs a fork.

## Q-D1-19 (V2-D1.5), Select TWO

**Scenario.** A research assistant handles two query shapes: (1) "What is the current price of stock X?" (2) "Summarize the bull and bear cases for stock X from the last ten filings."

**Question.** Which TWO statements about decomposition are correct? Select TWO.

**Options.**
A) Query 1 needs a tool call for the live price, the index cannot hold the present.
B) Query 2 fits fan-out: pull the ten filings in parallel, summarize each, then merge with a validation gate.
C) Both queries should run through one fixed 8-step chain for consistency.
D) Query 2 should use a single call with all ten filings in context to avoid merge complexity.
E) Query 1 should be answered from the cached index for speed.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: decomposition judgment (multi-select).
2. Lifecycle stage: design.
3. Objective: right shape per query.
4. Hard constraints: price changes faster than any refresh, ten filings are independent.
5. System layer: decomposition.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: C forces one shape on two shapes, E serves a stale price.
8. Compare on objective: A names the live-data rule, B matches independence to fan-out.
9. Hidden dependencies: the tool needs the market data source, the merge needs the validation gate.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "current price" and "ten filings."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Live data handled live | Yes | n/a | No | n/a | No |
| Independence matched to pattern | n/a | Yes | No | No | n/a |

4. Why A and B satisfy all hard constraints: A keeps the fast-changing answer behind a tool call, B parallelizes the independent filings and gates the merge.
5. Why A and B best meet the objective: V2-D3.6 says live transactional state belongs behind a tool call, and V2-D1.5 says independent pieces fan out.
6. Every rejected choice explained: C is one chain for two shapes, the price query would wait through eight steps and still get a stale answer. D stuffs ten filings into one context, the middle filings get lost and the merge complexity becomes attention dilution. E is the staleness trap: a cached price is a snapshot, and the question asks for the present.
7. Exact limitation or tradeoff: A depends on the market data tool being up, B needs the merge gate to catch a worker that summarized the wrong filing.
8. Relevant evidence (with date): live-data rule from lesson-D3-6 (§9), Oct 6 2026, fan-out verdict from lesson-D1-patterns (V2-D1.5), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if both queries truly share eight ordered steps (they do not here). D wins if the corpus is tiny and fits comfortably with headroom. E wins if the question asks for the closing price, a fixed historical fact.
10. Misconception tested: one decomposition serves all queries. Shape decides: live goes to tools, independent goes to fan-out.

## Q-D1-20 (V2-D1.5)

**Scenario.** A marketing team uses Claude to draft campaign briefs. Inside each brief, the budget table must sum correctly and the dates must fall on weekdays. The team currently asks Claude to compute the sums and check the calendars in prose.

**Question.** What is the best change?

**Options.**
A) Add few-shot examples of correct budget tables to the prompt.
B) Move the certain sub-tasks into deterministic code: a script sums the table and validates the dates, Claude drafts the prose around the checked numbers.
C) Switch to the most capable tier for better arithmetic.
D) Add a second Claude call to double-check the first call's arithmetic.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best decomposition fix.
2. Lifecycle stage: operation (iteration).
3. Objective: correct sums and valid dates.
4. Hard constraints: arithmetic must be exact, weekday checks are rule-based.
5. System layer: decomposition (deterministic split).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B removes model variance from certain tasks entirely, the rest reduce it.
9. Hidden dependencies: the script needs the table format contract, the prose must reference the checked numbers, not recompute them.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the budget table must sum correctly and the dates must fall on weekdays."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Exact arithmetic guaranteed | No | Yes | No | No |
| Rule-based date check guaranteed | No | Yes | No | No |
| Prose keeps the model | Yes | Yes | Yes | Yes |

4. Why B satisfies all hard constraints: code sums exactly and checks weekdays by rule, Claude keeps the open prose work.
5. Why B best meets the objective: V2-D1.5's deterministic split says certain sub-tasks inside the work go to code, arithmetic and calendar rules are certain.
6. Every rejected choice explained: A improves the odds with examples but the model still samples, "usually right" is not a guarantee for money tables. C is the proxy fix: a bigger tier still samples arithmetic. D doubles the sampling, two guesses do not make a proof.
7. Exact limitation or tradeoff: B needs the table format contract maintained, a format change breaks the script until it is updated.
8. Relevant evidence (with date): deterministic split from lesson-D1-patterns (§9, V2-D1.5), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the task is stylistic (tone, structure) rather than exact. C wins when the failing part is genuinely hard judgment, not arithmetic. D wins as a critique pass on prose quality, not on sums.
10. Misconception tested: the model should do everything in one pass because it is capable. Capability is not certainty, certain sub-tasks belong in code.

## Q-D1-21 (V2-D1.6)

**Scenario.** A support team considers auto-drafting replies. Agents handle 2,000 tickets per week at 6 minutes each. Drafts cut handle time to 4 minutes each. The agent hour costs $45 (toy). Wrong drafts that ship cost $500 per incident (not in source): 10 per year now, 4 per year with drafts plus review. Drafts cost $0.01 each to run. Build cost is $20,000 one time.

**Question.** What is the first-year net value, and what is the build decision?

**Options.**
A) Net about $138,000, build.
B) Net about $135,000, build.
C) Net negative, do not build.
D) Net about $158,000, build.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: business-value computation and decision.
2. Lifecycle stage: discovery (build or no-build).
3. Objective: first-year net value.
4. Hard constraints: all four terms need numbers: baseline, new cost, avoided errors, build cost.
5. System layer: business-value alignment.
6. Eliminate infeasible: all are computable.
7. Eliminate constraint-violating: none violate outright, the arithmetic decides.
8. Compare on objective: compute each term fully, only A counts all four.
9. Hidden dependencies: incident prices are toy assumptions, labeled not in source.
10. Verify: A. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "Drafts cut handle time to 4 minutes each" and "10 per year now, 4 per year with drafts plus review."
3. Requirement-to-option matrix:

| Term | Arithmetic |
|---|---|
| Baseline | 2,000 x 6 min = 12,000 min = 200 h, 200 x $45 = $9,000/week, x 52 = $468,000/year |
| New world | 2,000 x 4 min = 133.3 h, x $45 = $6,000/week, x 52 = $312,000/year, run 2,000 x $0.01 x 52 = $1,040/year |
| Labor savings | $468,000 - $312,000 = $156,000/year |
| Avoided errors | (10 - 4) x $500 = $3,000/year |
| Net | $156,000 + $3,000 - $20,000 - $1,040 = $137,960, about $138,000 |

4. Why A satisfies all hard constraints: every term has a number and the equation uses all four, the net is positive, so the build decision is yes.
5. Why A best meets the objective: V2-D1.6 defines net value as (baseline - new) x volume + avoided error cost - build and run cost, A is the only option that computes it whole.
6. Every rejected choice explained: B drops the avoided-error term ($3,000), the error term is small here but the method requires it, and on other toys it dominates. C is the "do not build" reflex with no arithmetic behind it. D forgets the $20,000 build cost, the most common business-case lie.
7. Exact limitation or tradeoff: incident prices and the 6-to-4 minute cut are toy assumptions, a pilot must measure the real handle-time cut before the full build.
8. Relevant evidence (with date): net-value equation from lesson-D1-6 (§3-§4), Oct 6 2026, contract toy ($689K/year) from the same lesson, "not in source" labels follow the lesson's honesty rule.
9. Counterfactual where each plausible alternative wins: B wins if the error term is truly zero (no incidents at stake). C wins if the equation comes back negative (then not building is the best answer). D wins never, forgetting build cost is not a method.
10. Misconception tested: labor savings alone make the case. The case needs all four terms, here the build cost is 13% of the gross savings, and forgetting it is the classic error.

## Q-D1-22 (V2-D1.6)

**Scenario.** A team prices an AI triage tool for the support desk. Run cost is $40,000 per year. Measured labor savings are $25,000 per year. There is no error term: triage mistakes cost nothing measurable. The sponsor asks whether to build.

**Question.** What is the best answer?

**Options.**
A) Build, the tool is strategically important.
B) Build a smaller pilot, the numbers may improve.
C) Do not build, the net value is negative and building destroys value.
D) Build, run cost always falls over time.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: build or no-build decision.
2. Lifecycle stage: discovery.
3. Objective: avoid value destruction.
4. Hard constraints: net = $25,000 - $40,000 = -$15,000 per year, no error term to rescue it.
5. System layer: business-value alignment.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only C follows the equation to its verdict.
9. Hidden dependencies: "strategically important" and "costs fall" are hopes, not terms.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "Run cost is $40,000 per year. Measured labor savings are $25,000 per year."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Follows the equation | No | Partial | Yes | No |
| Names the negative net | No | No | Yes | No |

4. Why C satisfies all hard constraints: the equation is complete (no error term exists), the net is -$15,000/year, and V2-D1.6 says a negative net means do not build.
5. Why C best meets the objective: the best answer is sometimes no, C is the only option that says it.
6. Every rejected choice explained: A substitutes "strategic importance" for arithmetic, strategy without a priced term is a slogan. B is reasonable when the baseline is unknown, but here the numbers are measured, a pilot to "hope for better" is delay, not method. D asserts a future cost fall with no evidence, the decision uses today's numbers.
7. Exact limitation or tradeoff: C kills the project, if the sponsor can narrow the scope until the equation turns, that narrower case gets its own computation.
8. Relevant evidence (with date): negative-net counterfactual from lesson-D1-6 (§11), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if a priced error term or revenue term turns the net positive. B wins when the baseline is unknown (pilot first, then decide). D wins with a signed vendor quote showing the lower run cost.
10. Misconception tested: every AI proposal deserves a build. It does not. The equation can say no, and no is a complete answer.

## Q-D1-23 (V2-D1.6), Select TWO

**Scenario.** A team lists four outcomes from an AI project: (1) the same invoices processed with half the staff hours, (2) analysts now answer questions they could never answer before, (3) fewer compliance fines, (4) answers arrive in 2 seconds instead of 20.

**Question.** Which TWO value-type matches are correct? Select TWO.

**Options.**
A) Outcome 1 is efficiency: the same work, cheaper.
B) Outcome 2 is transformation: the previously impossible.
C) Outcome 3 is productivity: more work with the same people.
D) Outcome 4 is quality: fewer errors.
E) Outcome 2 is efficiency: faster answers.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: value-type classification (multi-select).
2. Lifecycle stage: discovery.
3. Objective: name the value type per outcome.
4. Hard constraints: the four types are efficiency, productivity, transformation, quality.
5. System layer: business-value alignment.
6. Eliminate infeasible: all are classifiable.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A and B match the lesson definitions exactly.
9. Hidden dependencies: none, this is definitional.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "the same invoices processed with half the staff hours" and "questions they could never answer before."
3. Requirement-to-option matrix:

| Outcome | A | B | C | D | E |
|---|---|---|---|---|---|
| 1: same work, cheaper | Yes | n/a | n/a | n/a | n/a |
| 2: previously impossible | n/a | Yes | n/a | n/a | No |
| 3: fewer fines | n/a | n/a | No | n/a | n/a |
| 4: faster answers | n/a | n/a | n/a | No | n/a |

4. Why A and B satisfy all hard constraints: A matches the efficiency definition (same work cheaper), B matches transformation (the impossible, now done).
5. Why A and B best meet the objective: V2-D1.6 defines the four types, correct naming drives which metric proves the value.
6. Every rejected choice explained: C mislabels fewer fines, fines avoided are the quality term (error cost), not productivity (more output per person). D mislabels speed, faster answers are latency, an SLO guard on the equation, not the quality term. E mislabels new capability as efficiency, doing the previously impossible is transformation by definition.
7. Exact limitation or tradeoff: naming the type is step one, each still needs its metric, threshold, and owner before it enters the equation.
8. Relevant evidence (with date): four value types from lesson-D1-6 (§3), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if outcome 3 were "analysts handle twice the cases" (more with the same people). D wins if outcome 4 were "fewer wrong answers" (error cut). E wins never, new capability is not efficiency.
10. Misconception tested: all good outcomes are "efficiency." They are not, the type decides the metric, and the metric decides whether the value is real.

## Q-D1-24 (V2-D1.6)

**Scenario.** A claims assistant has two proposed improvements. Improvement X cuts p95 latency 20% (from 5 s to 4 s). Improvement Y cuts the error rate from 3% to 2%, each error costs $500 (not in source). Volume is 100,000 claims per year. The budget funds one improvement.

**Question.** Which improvement should the team fund first?

**Options.**
A) Improvement X, latency is what users feel.
B) Improvement Y, the error term dominates the value equation.
C) Split the budget evenly between X and Y.
D) Neither, latency and errors are both fine.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: prioritization under a fixed budget.
2. Lifecycle stage: discovery (roadmap).
3. Objective: fund the improvement with the bigger net value.
4. Hard constraints: budget funds one, error price $500, volume 100,000/year.
5. System layer: business-value alignment.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: Y avoids 1% x 100,000 = 1,000 errors x $500 = $500,000/year, X's latency cut has no priced term.
9. Hidden dependencies: the error price is a toy assumption, the latency cut needs a priced term to compete.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "each error costs $500" and "Volume is 100,000 claims per year."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Priced value term | No | Yes | Partial | No |
| Fits one-improvement budget | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: 1,000 avoided errors x $500 = $500,000/year of priced value, the budget funds one improvement and Y is the one with a number.
5. Why B best meets the objective: V2-D1.6 says the value driver decides, here error cost dominates and latency has no priced term.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: latency is real value when users wait, but here no one priced the wait, while the error bill is $500,000. C splits the budget so neither improvement ships whole, half a latency cut and half an error cut is two unfinished projects. D ignores a priced $500,000 term.
7. Exact limitation or tradeoff: if users abandon at 5 s, latency gets a priced churn term and the math can flip, the scenario gives no such term.
8. Relevant evidence (with date): "optimize the easiest metric" valid-but-inferior from lesson-D1-6 (§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if a priced churn term ties abandonment to the 5 s latency. C wins if both improvements are cheap enough to ship whole (then the budget is not really one-improvement). D wins if the error price were $5, not $500.
10. Misconception tested: the easiest metric to move is the best investment. The priced term decides, not the ease.

## Q-D1-25 (V2-D1.6)

**Scenario.** A retailer wants an AI demand forecast. No one knows the current forecast accuracy: the baseline was never measured. The vendor quotes $120,000 per year. The sponsor wants a build decision this week.

**Question.** What is the best recommendation?

**Options.**
A) Build now, the vendor's reference customers show good results.
B) Run a priced pilot first: measure the baseline on a fixed SKU set, then compute the net value before the full build.
C) Decline, forecasting is too hard for AI.
D) Build now and measure the baseline during rollout.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: stakeholder decision under unknown baseline.
2. Lifecycle stage: discovery.
3. Objective: a build decision grounded in numbers.
4. Hard constraints: baseline unknown, vendor price known, the equation needs a baseline.
5. System layer: business-value alignment.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B produces the missing term before committing $120,000/year.
9. Hidden dependencies: the pilot needs a fixed SKU set and a measurement method agreed in advance.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "No one knows the current forecast accuracy: the baseline was never measured."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Produces the baseline term | No | Yes | No | Late |
| Commits spend before numbers | Yes | No | No | Yes |
| Decidable this quarter | Yes | Yes | Yes | Yes |

4. Why B satisfies all hard constraints: the pilot measures the baseline, which the equation requires, the full build waits for the net.
5. Why B best meets the objective: V2-D1.6 says baseline unknown means pilot first, then decide, you cannot subtract from a number you do not have.
6. Every rejected choice explained: A outsources the baseline to reference customers whose data, SKUs, and costs differ. C declines on a vibe ("too hard") instead of a number, the equation might have said yes. D commits the spend and measures later, which is building before the filter the lesson forbids.
7. Exact limitation or tradeoff: the pilot costs time and money, its scope must be fixed (SKU set, weeks, success bar) or it becomes a slow build by another name.
8. Relevant evidence (with date): "baseline unknown: pilot first, then decide" from lesson-D1-6 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the vendor contract ties price to measured accuracy gains (then the baseline is the vendor's problem). C wins if the equation with a measured baseline comes back negative. D wins never as a decision method.
10. Misconception tested: a decision this week needs a yes or no this week. It needs the missing term first, "pilot, then decide" is a complete answer.

## Coverage: D1 questions to objectives

| Objective | Questions | Count |
|---|---|---|
| V2-D1.1 | Q-D1-01, Q-D1-02, Q-D1-03, Q-D1-04 | 4 |
| V2-D1.2 | Q-D1-05, Q-D1-06, Q-D1-07, Q-D1-08 | 4 |
| V2-D1.3 | Q-D1-09, Q-D1-10, Q-D1-11, Q-D1-12 | 4 |
| V2-D1.4 | Q-D1-13, Q-D1-14, Q-D1-15, Q-D1-16 | 4 |
| V2-D1.5 | Q-D1-17, Q-D1-18, Q-D1-19, Q-D1-20 | 4 |
| V2-D1.6 | Q-D1-21, Q-D1-22, Q-D1-23, Q-D1-24, Q-D1-25 | 5 |
| Total | | 25 |

Multi-response items: Q-D1-03, Q-D1-06, Q-D1-12, Q-D1-15, Q-D1-19, Q-D1-23 (6 of 25).

