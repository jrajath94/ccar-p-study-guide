# Domain 6 Question Bank: Stakeholder Communication and Lifecycle Management

25 original practice questions for objectives V2-D6.1 through V2-D6.5.
Baseline: Oct 6, 2026. Scope: blueprint v1.0 via secondary summaries (S03, S04), Sept 2026.
These are original practice items for study. They are not real exam items and do not predict exam content.
Format per question: scenario, one best answer or a marked multi-select, options, answer key, a §17 10-step method walk, and a 10-point explanation.
Toy numbers are original to this bank, computed inside each scenario.

## Q-D6-01 (V2-D6.1)

**Scenario.** A hospital asks for a discharge-summary agent. The clinical lead says accuracy "matters for patient safety." No numbers exist yet: no volume, no error budget, no named reviewer, no prohibited list.

**Question.** What is the best FIRST action?

**Options.**
A) Build a working prototype so the clinical lead sees progress this week.
B) Run structured discovery: outcomes, prohibited behaviors, error cost, volume, quality bar, latency, compliance, dependencies, owners, and open assumptions, then convert "accurate" into a measurable requirement.
C) Benchmark three model tiers on sample summaries.
D) Draft the system prompt with strict accuracy instructions.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: first action in a stakeholder request.
2. Lifecycle stage: discovery.
3. Objective: turn "accurate" into a measurable requirement before design.
4. Hard constraints: patient safety is in scope, no numbers exist, the safety constraints are unknown.
5. System layer: requirements discovery.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A builds before the safety constraints are known. C benchmarks before the bar exists. D writes prose before the requirement exists.
8. Compare on objective: B is the only action that finds the safety constraints first.
9. Hidden dependencies: the clinical lead must name who signs the quality bar, and the open assumptions must be written down.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "accuracy 'matters for patient safety.' No numbers exist yet."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Safety constraints found first | No | Yes | No | No |
| Adjective becomes a number | No | Yes | No | No |
| Owners and assumptions recorded | No | Yes | No | No |

4. Why B satisfies all hard constraints: the discovery grid asks the questions that find the safety bar, and the adjective-to-metric conversion makes "accurate" testable.
5. Why B best meets the objective: V2-D6.1 requires structured discovery across the dimensions plus adjective-to-metric conversion. B is that work.
6. Every rejected choice explained: A is the build-first trap. The prototype shows progress while the safety constraints stay unknown. C answers the wrong first question. Tier choice needs a bar to choose against. D is prose before requirements. A strict prompt with no measured bar is untestable.
7. Exact limitation or tradeoff: discovery takes calendar time. Stakeholders do not reply on demand. And it cannot find unknown unknowns.
8. Relevant evidence (with date): the discovery grid and adjective conversion from lesson-D6-1 (§§4-5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for a weekend demo with no real data, where the correct discovery is "what looks good on screen." C wins after the bar is signed and the question is which tier clears it. D wins never as the first action.
10. Misconception tested: building shows progress. Building before discovery shows motion. The safety bar comes first.

## Q-D6-02 (V2-D6.1)

**Scenario.** The AP lead says the new invoice agent must be "fast and accurate." The builder is about to start design. The contract will hold the builder to whatever is written down.

**Question.** What is the best next step?

**Options.**
A) Accept "fast and accurate" as the requirement and start building.
B) Convert the adjectives into measurable requirements: p95 latency under 60 seconds, match precision at least 98%, cost at most $0.20 per invoice, and record any open assumption.
C) Choose the fastest model tier available.
D) Promise the AP lead 100% accuracy.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: requirement-clarification action.
2. Lifecycle stage: discovery closing into design.
3. Objective: design starts from testable numbers, not adjectives.
4. Hard constraints: the contract binds the builder, adjectives are not testable, design is about to start.
5. System layer: requirement translation.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A hardens a guess into code. D promises what no measurement supports.
8. Compare on objective: B is the only option that makes the adjectives testable before design.
9. Hidden dependencies: the AP lead must sign the numbers, or the conversion is the builder's guess.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "must be 'fast and accurate.' The contract will hold the builder to whatever is written down."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Testable before design | No | Yes | No | No |
| Signed by the stakeholder | No | Yes | No | No |
| No unsupported promise | Yes | Yes | Yes | No |

4. Why B satisfies all hard constraints: each adjective becomes a number with a threshold, and the open-assumption record keeps guesses visible.
5. Why B best meets the objective: V2-D6.1 turns adjectives into measurable requirements. An unmeasured adjective in a contract is a dispute scheduled for demo day.
6. Every rejected choice explained: A lets design guess the meaning of "fast." Testing then checks the wrong bar. C picks a tier before the bar exists. Speed without a target is not a requirement. D is the banned promise. No measurement supports 100%.
7. Exact limitation or tradeoff: the numbers can be wrong. The AP lead's guess is still a guess until measured. The record makes it revisable.
8. Relevant evidence (with date): adjective-to-metric conversion from lesson-D6-1 (§4), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as stated. It wins when the adjectives are already defined in a signed standard the team cites. C wins after the latency bar is signed. D wins never.
10. Misconception tested: adjectives are requirements. They are not. A requirement the team cannot test is a wish.

## Q-D6-03 (V2-D6.1), Select TWO

**Scenario.** The invoice-agent discovery grid already holds outcomes, volume, cost limit, latency, and owners. Two cells are still blank, and design waits.

**Question.** Which TWO blank cells must be filled before design? Select TWO.

**Options.**
A) Prohibited behaviors: never auto-approve an invoice above $1,000.
B) The team's lunch preferences.
C) Compliance: invoices carry vendor bank details, so they are sensitive.
D) The model's parameter count.
E) The office floor plan.

**Answer.** A, C

**Method walk (Steps 1-10).**
1. Question type: discovery-completeness check.
2. Lifecycle stage: discovery gate before design.
3. Objective: no design decision rests on a blank cell.
4. Hard constraints: money moves, sensitive data is in scope, the grid gates design.
5. System layer: discovery artifacts.
6. Eliminate infeasible: all five are writable.
7. Eliminate constraint-violating: B, D, and E are not discovery dimensions. They answer no design question.
8. Compare on objective: A and C are the missing dimensions that change the design. The rest change nothing.
9. Hidden dependencies: the prohibited list needs the CFO's sign-off, and the compliance cell needs the data classification confirmed.
10. Verify: A and C together. No third option is a discovery dimension.

**Explanation.**
1. Correct answer: A, C.
2. Decisive scenario phrase: "Two cells are still blank, and design waits."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Discovery dimension | Yes | No | Yes | No | No |
| Changes the design | Yes | No | Yes | No | No |
| In scope: money or sensitive data | Yes | No | Yes | No | No |

4. Why A and C satisfy all hard constraints: the prohibited list bounds the money movement, and the compliance cell triggers the data-handling rows. Design cannot proceed safely without either.
5. Why A and C best meet the objective: V2-D6.1 requires the full grid, including prohibited behaviors and compliance, before design. A blank cell is an open assumption, and open assumptions must be written, not skipped.
6. Every rejected choice explained: B is not a dimension. Lunch preferences answer no design question. D is trivia. The parameter count decides nothing about approvals or data handling. E is not a dimension. The floor plan never gated a design.
7. Exact limitation or tradeoff: filling the cells takes stakeholder time, and answers can conflict. The grid records the conflict instead of hiding it.
8. Relevant evidence (with date): the eleven-dimension grid from lesson-D6-1 (§5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins never. D wins when the parameter count drives a real constraint, such as on-device deployment. Then it belongs in the grid. E wins never.
10. Misconception tested: discovery is done when the easy cells are filled. It is done when the money, data, and prohibition cells are filled and signed.

## Q-D6-04 (V2-D6.1)

**Scenario.** During discovery, the AP lead says the auto-approval limit is $1,000. The CFO says it is $500. Both insist. Design waits on the number.

**Question.** What is the best action?

**Options.**
A) Use $1,000. The AP lead owns the workflow.
B) Split the difference at $750.
C) Record the conflict as an open assumption, escalate to the decision owner for sign-off on one number, and hold design until it is signed.
D) Build both limits and let users choose.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: conflicting-stakeholder resolution.
2. Lifecycle stage: discovery.
3. Objective: one signed number before design.
4. Hard constraints: two stakeholders disagree, the number gates design, the decision owner must sign.
5. System layer: stakeholder alignment.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A picks a side without authority. B invents a number neither stakeholder approved. D ships the conflict to users.
8. Compare on objective: C is the only option that produces a signed decision.
9. Hidden dependencies: the decision owner must actually be identified, and the hold must be communicated to the builder.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "The AP lead says the auto-approval limit is $1,000. The CFO says it is $500. Both insist."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| One signed number results | No | No | Yes | No |
| Decision owner decides | No | No | Yes | No |
| Design holds until signed | No | No | Yes | No |

4. Why C satisfies all hard constraints: the conflict is recorded instead of hidden, the owner signs one number, and design waits for the signature.
5. Why C best meets the objective: V2-D6.1 treats conflicting answers as a discovery limitation to be managed, not averaged. Answers can be wrong. The grid records and escalates.
6. Every rejected choice explained: A confuses workflow ownership with decision authority. The CFO owns the money rule. B is the averaging trap. $750 is a number no one approved. D is abdication. Users did not ask to resolve an internal conflict.
7. Exact limitation or tradeoff: escalation takes calendar time, and the builder idles. That idle time is cheaper than building the wrong limit.
8. Relevant evidence (with date): the conflicting-answers limitation from lesson-D6-1 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the AP lead is the documented decision owner for the limit. Then the choice follows authority instead of picking sides. B wins never as a decision method. D wins never.
10. Misconception tested: a compromise number resolves a conflict. It does not. Only the decision owner's signature resolves it.

## Q-D6-05 (V2-D6.1)

**Scenario.** Six months after sign-off, invoice volume doubles from 500 to 1,000 per day. The cost, latency, and owner cells still hold. The grid carries a review date, which arrives next week.

**Question.** What is the best action?

**Options.**
A) Re-run the full eleven-question discovery from scratch.
B) Update only the volume cell at the review date and re-sign it, then check which dependent cells the change touches.
C) Ignore the change. The design already shipped.
D) Rebuild the agent for the new volume without touching the grid.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: stale-discovery maintenance.
2. Lifecycle stage: operation, requirement review.
3. Objective: the grid reflects reality again with minimum rework.
4. Hard constraints: one cell changed, the rest hold, the review date exists for this purpose.
5. System layer: discovery lifecycle.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: C lets the design run on a false volume. D changes the system without updating the record.
8. Compare on objective: B uses the review date as designed. A re-runs ten good cells for no reason.
9. Hidden dependencies: the volume change may touch cost and latency cells, which then need their own re-sign.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "volume doubles from 500 to 1,000 per day" and "The grid carries a review date."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Grid reflects reality | Yes | Yes | No | No |
| Minimum rework | No | Yes | Yes | No |
| Uses the review date | No | Yes | No | No |

4. Why B satisfies all hard constraints: the changed cell is re-signed at its review date, and the dependent-cell check catches what the volume change breaks.
5. Why B best meets the objective: V2-D6.1 treats discovery as a living record. Date it and re-sign it. One changed cell means one re-signed cell, not a new discovery.
6. Every rejected choice explained: A is rework theater. Ten signed cells do not need new interviews. C is the rot option. The design keeps assuming 500 per day. D is the undocumented rebuild. The next engineer inherits a system the grid does not describe.
7. Exact limitation or tradeoff: the dependent-cell check can surface uncomfortable news, such as a broken cost cell. That news is the point of the review.
8. Relevant evidence (with date): the stale-grid figure and re-sign rule from lesson-D6-1 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when most cells changed or the business pivoted. Then the grid is stale throughout. C wins never. D wins for an emergency volume fix, with the grid updated in the post-incident window.
10. Misconception tested: signed requirements are permanent. They are not. Discovery is a living record with a review date.

## Q-D6-06 (V2-D6.2)

**Scenario.** The triage agent must cost at most $60,000 per month, and errors need human review. Option A costs $240,000 per month at 99% precision on the eval set. Option B costs $18,000 per month plus $30,000 per month in human correction labor at 96% precision, with 400 misrouted tickets per day needing 5 minutes of human fix each. Both keep ticket text in-region.

**Question.** Which recommendation fits?

**Options.**
A) Option A, described as near perfect.
B) Option B, presented with the $192,000 monthly saving, the 400 daily misroutes, the 33 human hours per day priced, the one-week reversal cost, and the same compliance posture.
C) Option B, described as perfect and risk free.
D) Option A, because higher precision always wins.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: architecture recommendation under a cost cap.
2. Lifecycle stage: design, decision.
3. Objective: recommend the option that fits the cap with its concessions priced.
4. Hard constraints: $60,000 per month cap, errors need human review, concessions must be stated.
5. System layer: trade-off communication.
6. Eliminate infeasible: both options are buildable.
7. Eliminate constraint-violating: A costs $240,000 per month, four times the cap. D ignores the cap entirely.
8. Compare on objective: B fits the cap at $48,000 per month and states every concession. C sells B with banned promises.
9. Hidden dependencies: the 33 human hours need staffing, and the eval-set precision must be labeled as eval-set, not production.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "must cost at most $60,000 per month."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fits the $60k cap | No | Yes | Yes | No |
| Concessions priced honestly | No | Yes | No | No |
| No banned promise | No | Yes | No | Yes |

4. Why B satisfies all hard constraints: $18,000 plus $30,000 equals $48,000 per month, inside the cap. The 400 daily misroutes price as 400 x 5 = 2,000 minutes = 33.3 hours per day. The saving versus A is $240,000 minus $48,000 = $192,000 per month.
5. Why B best meets the objective: V2-D6.2 requires benefit, cost, risk, reversal cost, and compliance impact per option. B is the only option that presents all five fields honestly.
6. Every rejected choice explained: A violates the stated cap and hides the 1% error rate behind "near perfect." 1% of 10,000 tickets is 100 misroutes per day, unstated. C sells the right option with the two banned promises. "Perfect" and "risk free" have no measurement behind them. D is precision absolutism. Precision without a budget is not a recommendation.
7. Exact limitation or tradeoff: B's 3 extra points of error need 33 human hours per day, every day. That labor is a permanent cost line.
8. Relevant evidence (with date): the two-option toy with full five-field pricing from lesson-D6-2 (§5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the cap is lifted and the 1% error difference carries regulatory weight. Then the price buys something. C wins never. D wins never as stated. It wins when precision is the only scored dimension.
10. Misconception tested: the best option is the highest-precision option. The best option is the one that fits the cap with its concessions priced and signed.

## Q-D6-07 (V2-D6.2)

**Scenario.** The team chose option B. Three audiences must sign: the executive who holds the budget, the security lead, and the engineering lead.

**Question.** Which message fits the security lead?

**Options.**
A) "B saves $192,000 per month."
B) "B keeps ticket text in-region, cuts tool hops versus A, shrinks the attack surface, and holds the same compliance posture."
C) "B runs at p95 3 seconds."
D) "B uses fewer tokens."

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: audience-tailored communication.
2. Lifecycle stage: design, decision.
3. Objective: the security lead can sign on security grounds.
4. Hard constraints: same truth for all audiences, each audience gets the fields it decides on.
5. System layer: stakeholder communication.
6. Eliminate infeasible: all four messages are sendable.
7. Eliminate constraint-violating: none are infeasible, but A, C, and D give the security lead no security field.
8. Compare on objective: B is the only message with the fields a security lead signs: data residency, attack surface, compliance.
9. Hidden dependencies: the in-region claim needs the region config as evidence.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the security lead" must sign.
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Security-decidable fields | No | Yes | No | No |
| Same truth as other audiences | Yes | Yes | Yes | Yes |
| Answers the sign-off question | No | Yes | No | No |

4. Why B satisfies all hard constraints: residency, tool-hop count, attack surface, and compliance posture are the fields the security sign-off rests on.
5. Why B best meets the objective: V2-D6.2 requires the message adapted to the audience with the same truth. Executives cannot act on tool-hop counts, and security cannot act on dollar savings.
6. Every rejected choice explained: A is the executive's field. It answers no security question. C is the engineering field. Latency says nothing about data or attack surface. D is an engineering cost field. Token counts do not sign a security review.
7. Exact limitation or tradeoff: tailoring takes work per audience, and the numbers must stay consistent across the versions. One truth, five framings.
8. Relevant evidence (with date): the per-audience message fields from lesson-D6-2 (§5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for the executive audience. C wins for the engineering audience. D wins for the engineering cost discussion. Each field has its audience.
10. Misconception tested: one message serves all audiences. It does not. The same truth needs different fields per signer.

## Q-D6-08 (V2-D6.2), Select TWO

**Scenario.** A team pitches an agent that "eliminates all review work and never makes a mistake." The eval set holds 500 cases. The agent scores 99%. The run rate is 10,000 tickets per day.

**Question.** Which TWO are the honest versions of the pitch? Select TWO.

**Options.**
A) "99% precision on the 500-case eval set. The 1% error rate means about 100 tickets per day still need review."
B) "The agent eliminates all review work."
C) "Measured runs cut review labor from 40 to 4 hours per day. Residual errors route to a human queue."
D) "The agent never makes a mistake."
E) "Risk is zero."

**Answer.** A, C

**Method walk (Steps 1-10).**
1. Question type: honest restatement of vendor claims.
2. Lifecycle stage: design, evaluation of a pitch.
3. Objective: replace slogans with measured claims.
4. Hard constraints: every claim needs a number and a scope, banned promises are out.
5. System layer: trade-off communication.
6. Eliminate infeasible: all five are sayable.
7. Eliminate constraint-violating: B, D, and E are the banned promises. No measurement supports "all," "never," or "zero."
8. Compare on objective: A and C attach numbers, scopes, and residuals to the claims.
9. Hidden dependencies: the 500-case eval must be representative, or the 99% does not transfer.
10. Verify: A and C together. No third option carries a number.

**Explanation.**
1. Correct answer: A, C.
2. Decisive scenario phrase: "eliminates all review work and never makes a mistake."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Number attached | Yes | No | Yes | No | No |
| Scope stated | Yes | No | Yes | No | No |
| Residual owned | Yes | No | Yes | No | No |

4. Why A and C satisfy all hard constraints: A converts 99% on 500 cases into 100 tickets per day at the run rate. C states the measured labor cut and names where the residual goes.
5. Why A and C best meet the objective: V2-D6.2 requires quantified trade-offs with explicit uncertainties. Uncertainty stated beats perfection promised.
6. Every rejected choice explained: B is the banned "eliminates all" promise. The 1% error rate alone refutes it. D is the banned "never" promise. 99% on 500 cases is not never. E is the banned "zero risk" promise. No measurement supports it.
7. Exact limitation or tradeoff: honest numbers can lose the pitch to a competitor's slogans. The signature must still rest on the numbers.
8. Relevant evidence (with date): the promise price check from lesson-D6-2 (§4), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins never. D wins never. E wins never. The honest versions A and C are the only shippable claims.
10. Misconception tested: a strong pitch needs strong adjectives. It needs strong numbers. The exam marks "perfect" and "zero risk" as distractors every time.

## Q-D6-09 (V2-D6.2)

**Scenario.** The signed trade-off picked option B at $18,000 per month. The provider then doubled token prices. Option B now costs $40,000 per month. Option A now costs $480,000 per month. The numbers on the signed page are stale.

**Question.** What is the best action?

**Options.**
A) Keep the signed recommendation. A signature is a signature.
B) Recompute every field with the new prices, re-sign the trade-off, and date every number.
C) Switch to option A quietly and tell no one.
D) Blame the provider and pause the project.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: stale trade-off maintenance.
2. Lifecycle stage: operation.
3. Objective: the decision rests on current numbers again.
4. Hard constraints: prices changed, the signature bound the old numbers, the decision must be re-made on the new ones.
5. System layer: decision currency.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A treats a signature as permanent. C changes the decision without a signature. D abandons the decision.
8. Compare on objective: B re-runs the decision process on the new prices.
9. Hidden dependencies: the recompute needs the current price sheet, and the re-sign needs the same signers.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The provider then doubled token prices. The numbers on the signed page are stale."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Numbers current | No | Yes | No | No |
| Decision re-signed | No | Yes | No | No |
| Dates on the numbers | No | Yes | No | No |

4. Why B satisfies all hard constraints: every field is recomputed at the new prices, the signers sign the new page, and the dates make the next staleness visible.
5. Why B best meets the objective: V2-D6.2 treats trade-offs as dated artifacts. A trade-off has an expiry date. Put it on the page.
6. Every rejected choice explained: A confuses a signature with permanence. The signature bound numbers that no longer exist. C is the silent switch. The team operates a decision no one signed. D is abdication. The provider changed prices. The decision still belongs to the team.
7. Exact limitation or tradeoff: recompute and re-sign take the signers' time again, and frequent repricing can churn the decision. Date the numbers so the churn is visible.
8. Relevant evidence (with date): the repriced trade-off figure from lesson-D6-2 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the price change is immaterial to the decision. Then the signature still binds the same winner. C wins never. D wins when the new prices kill both options' value cases. Then pausing is a decision, signed.
10. Misconception tested: a signed decision is done forever. It is done until its numbers expire. Date every number.

## Q-D6-10 (V2-D6.2)

**Scenario.** The executive asks: "If we pick B and we are wrong, what does it cost to switch?" Option A takes two weeks to rebuild the pipeline. Option B takes one week. Both need a compliance re-check after a switch.

**Question.** Which answer fits?

**Options.**
A) "We will not be wrong. The evals are clear."
B) "Reversal costs two weeks from A and one week from B, plus the compliance re-check on the new pipeline. That cost is part of the decision."
C) A dump of the full technical specification.
D) "B is cheaper, so reversal does not matter."

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: reversal-cost communication.
2. Lifecycle stage: design, decision.
3. Objective: the executive signs with the exit price known.
4. Hard constraints: the question asks for the cost of being wrong, the answer must be a number, the compliance re-check is real.
5. System layer: trade-off communication.
6. Eliminate infeasible: all four are sayable.
7. Eliminate constraint-violating: A refuses the question. D declares the question irrelevant.
8. Compare on objective: B answers the asked question with numbers. C answers a different question with a document.
9. Hidden dependencies: the week estimates need the team's planning basis behind them.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "If we pick B and we are wrong, what does it cost to switch?"
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Answers the asked question | No | Yes | No | No |
| Priced per option | No | Yes | No | No |
| Includes the compliance re-check | No | Yes | No | No |

4. Why B satisfies all hard constraints: it gives the two-week and one-week figures, adds the re-check, and frames the cost as a decision input.
5. Why B best meets the objective: V2-D6.2 lists reversal cost as a required field per option. The executive signs the risk, not the rumor.
6. Every rejected choice explained: A is the infallibility dodge. Evals are clear until production disagrees. C is the spec dump. The executive asked for an exit price, not a document. D is the cheapness dodge. A cheap option with an expensive reversal can be the worse bet.
7. Exact limitation or tradeoff: week estimates are estimates. They need the planning basis cited, or they are new slogans.
8. Relevant evidence (with date): the five-field trade-off from lesson-D6-2 (§5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as an answer. C wins for the engineering audience that asked for the spec. D wins never as stated. It wins when the reversal cost is measured and trivial, and the number is shown.
10. Misconception tested: the decision is about picking the winner. It is also about pricing the exit. The executive signs both.

## Q-D6-11 (V2-D6.3), Select TWO

**Scenario.** A hospital pilot shows 94% precision against a 96% contract target. The contract sets the review trigger at 450 errors per day for two consecutive days and the iterate rule at drops under 10 points. The current run rate is 420 errors per day.

**Question.** Which TWO statements belong in the update to the clinical lead? Select TWO.

**Options.**
A) "The review trigger has not fired: 420 per day is below the 450-per-day, two-day rule."
B) "The 2-point miss is under the 10-point iterate threshold, so we tune prompts and retrieval instead of rebuilding."
C) "We paused the pilot immediately."
D) "The contract target is met."
E) "We will rebuild the pipeline this week."

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: contract-status communication.
2. Lifecycle stage: operation, pilot review.
3. Objective: the clinical lead hears the true trigger status and the rule-based next step.
4. Hard constraints: the trigger rule is 450 per day for two days, the iterate rule is under 10 points, the target is 96%.
5. System layer: expectation management.
6. Eliminate infeasible: all five are sayable.
7. Eliminate constraint-violating: C invents a breach that did not happen. D is false. 94% is below 96%. E skips the contract's own iterate rule.
8. Compare on objective: A states the trigger truth. B states the rule-based verdict. The rest misstate the contract.
9. Hidden dependencies: the 420-per-day rate must be measured on the same metric the contract names.
10. Verify: A and B together. No third option states the contract truthfully.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "94% precision against a 96% contract target" and "450 errors per day for two consecutive days."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Trigger status true | Yes | n/a | No | n/a | n/a |
| Follows the iterate rule | n/a | Yes | No | n/a | No |
| Target status true | n/a | n/a | n/a | No | n/a |

4. Why A and B satisfy all hard constraints: 420 is below 450, so the trigger has not fired. The 2-point miss is under 10 points, so the contract orders iteration, not a rebuild.
5. Why A and B best meet the objective: V2-D6.3 requires review triggers with breach consequences and an iterate-versus-re-architect rule, all signed before the crisis. A and B apply the signed rules.
6. Every rejected choice explained: C is panic as procedure. Pausing on an unfired trigger spends the breach consequence for nothing. D is false comfort. The target is 96%. The pilot shows 94%. E skips the contract. The rule says iterate under 10 points. The drop is 2.
7. Exact limitation or tradeoff: the honest update admits a miss against the target. That admission is the price of trust.
8. Relevant evidence (with date): the trigger and iterate-rule mechanism from lesson-D6-3 (§§4-5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins when the trigger actually fires. Then the consequence runs. D wins when the pilot hits 96%. Then it is true. E wins on a drop of 10 points or more, or after three failed iterations. Then the contract itself orders the rebuild.
10. Misconception tested: a miss against the target means rebuild. It does not. The contract's own rule decides: under 10 points, iterate.

## Q-D6-12 (V2-D6.3)

**Scenario.** After a vendor model change, triage precision drops 18 points. Two tuning rounds fail to recover it. The contract says: iterate on drops under 10 points, re-architect on drops of 10 or more, or after three failed iterations.

**Question.** What is the best next step?

**Options.**
A) Run a third tuning round with a bigger prompt.
B) Re-architect, per the contract's own rule: the drop exceeds 10 points and iterations failed.
C) Wait a month and hope the vendor reverts the change.
D) Lower the contract target to match the new score.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: iterate-versus-re-architect decision.
2. Lifecycle stage: operation.
3. Objective: follow the signed rule for a large, unrecoverable drop.
4. Hard constraints: the drop is 18 points, two iterations failed, the rule names 10 points as the line.
5. System layer: expectation contract enforcement.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A runs a third round the rule already priced as wasteful. C waits on hope. D rewrites the target to flatter the system.
8. Compare on objective: B is the only option that applies the signed rule.
9. Hidden dependencies: the re-architecture needs the same contract rewritten for the new design.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "drops 18 points. Two tuning rounds fail."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Follows the 10-point rule | No | Yes | No | No |
| Accounts for failed iterations | No | Yes | No | No |
| Honest about the drop | Yes | Yes | No | No |

4. Why B satisfies all hard constraints: 18 exceeds the 10-point line, and two failed iterations confirm tuning will not recover it. The contract orders the rebuild.
5. Why B best meets the objective: V2-D6.3 requires the iterate-versus-re-architect rule signed before the crisis, so the response is a procedure, not a panic. B runs the procedure.
6. Every rejected choice explained: A is the stall. The contract priced three failed iterations as a quarter burned. The drop already exceeds the line. C is hope as a plan. The vendor's roadmap is not a recovery strategy. D is target-shopping. The target measures the business need. The system missed it.
7. Exact limitation or tradeoff: re-architecture resets every tuned threshold and costs the rebuild. The contract priced that too.
8. Relevant evidence (with date): the iterate-versus-re-architect rule from lesson-D6-3 (§§4, 11), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins on a 4-point drop with zero failed iterations. Then the contract orders tuning. C wins never as the plan. D wins when the business need genuinely changed and the target is re-signed with the stakeholder.
10. Misconception tested: more tuning eventually fixes a structural drop. It does not. The contract's own line decides, and the line is 10 points.

## Q-D6-13 (V2-D6.3), Select TWO

**Scenario.** A team writes the production expectation contract for the triage agent. Five candidate parts are on the table.

**Question.** Which TWO are required parts of the contract? Select TWO.

**Options.**
A) Measured quality: the primary metric, the floor, and the eval set it was measured on.
B) Review triggers with breach consequences, signed before any crisis.
C) A promise of 100% precision and zero downtime.
D) A cost forecast: free to run at any volume, forever.
E) "The team will fix issues as they arise."

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: contract-completeness check.
2. Lifecycle stage: preproduction.
3. Objective: the contract holds measurable quality and enforceable triggers.
4. Hard constraints: probabilistic systems need ranges and triggers, promises need measurements, consequences need signatures.
5. System layer: expectation contracts.
6. Eliminate infeasible: all five are writable.
7. Eliminate constraint-violating: C is the banned promise. D invents free compute. E is ad hoc firefighting.
8. Compare on objective: A and B are the measurable, enforceable parts. The rest are slogans.
9. Hidden dependencies: the trigger needs the metric pipeline behind it, or it never fires.
10. Verify: A and B together. No third option is measurable or enforceable.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "production expectation contract."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Measurable | Yes | Yes | No | No | No |
| Enforceable | Partial | Yes | No | No | No |
| Probabilistic-system honest | Yes | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: A names the metric, the floor, and the set, so quality is checkable. B names the trigger and the consequence, signed before the crisis, so the response is a procedure.
5. Why A and B best meet the objective: V2-D6.3 requires measurable quality, realistic SLAs, review triggers, and breach consequences. A and B are those parts.
6. Every rejected choice explained: C is the banned promise. No measurement supports 100% or zero. D is fantasy accounting. Compute is never free at volume. E is the no-contract option. "As they arise" means after the customer finds them.
7. Exact limitation or tradeoff: triggers misfire, and consequences can be too harsh. The contract needs the diagnosis step before the consequence.
8. Relevant evidence (with date): the six-part contract from lesson-D6-3 (§§4-5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins never. D wins never. E wins for a tiny team with one user and low stakes, where ad hoc response is proportionate.
10. Misconception tested: a contract is a promise of good outcomes. It is a set of measurable bars with triggers and consequences, signed in advance.

## Q-D6-14 (V2-D6.3)

**Scenario.** The error trigger fires one week after the ticket team adds three new ticket types. The model version did not change. The retrieval config did not change.

**Question.** What is the best first step?

**Options.**
A) Pause auto-routing immediately per the breach consequence.
B) Segment the drift first: check whether the errors concentrate in the new ticket types, then decide.
C) Retrain the model on the new tickets.
D) Disable the trigger so it stops firing.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: trigger-diagnosis action.
2. Lifecycle stage: operation.
3. Objective: find whether the trigger fired on a real model drop or a data shift.
4. Hard constraints: new ticket types arrived, the model did not change, the consequence is expensive.
5. System layer: drift diagnosis.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A fires the expensive consequence on an undiagnosed signal. D blinds the team.
8. Compare on objective: B distinguishes a data shift from a model drop before any consequence. C treats a data shift as a model fault.
9. Hidden dependencies: the error logs must carry the ticket-type label for the segmentation to work.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "three new ticket types. The model version did not change."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Diagnoses before acting | No | Yes | No | No |
| Distinguishes data shift from model drop | No | Yes | No | No |
| Avoids a false-alarm consequence | No | Yes | Partial | No |

4. Why B satisfies all hard constraints: the segmentation shows whether the new types carry the errors, and the consequence waits for the diagnosis.
5. Why B best meets the objective: V2-D6.3 warns that triggers misfire and requires the data cut checked first. A trigger starts a diagnosis, not a punishment.
6. Every rejected choice explained: A is the $25,000-a-day pause on a false alarm. New ticket types, same model. C is the retrain reflex. The model is innocent. The data changed. D is the blindfold. The next real drop fires into silence.
7. Exact limitation or tradeoff: segmentation takes analyst time while the trigger stays open. That delay is cheaper than the false consequence.
8. Relevant evidence (with date): the trigger-misfire figure from lesson-D6-3 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the segmentation confirms a real model drop past the trigger. Then the consequence runs. C wins when the data shift is permanent and the model must learn the new types, decided after diagnosis. D wins never.
10. Misconception tested: a fired trigger means the model broke. It means something changed. The data cut decides what.

## Q-D6-15 (V2-D6.3)

**Scenario.** The triage agent costs $0.06 per ticket at 10,000 tickets per day: $18,000 per month. The business plan triples volume next quarter. Review labor is priced separately from the per-ticket cost.

**Question.** Which forecast is honest?

**Options.**
A) "$18,000 per month, flat."
B) "$54,000 per month at triple volume, plus the priced review labor, with the per-ticket cost and the date on the page."
C) "Costs scale linearly. Trust the trend."
D) "The first tier of growth is free."

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: production cost forecast.
2. Lifecycle stage: design, planning.
3. Objective: the business plans on the true cost at triple volume.
4. Hard constraints: $0.06 per ticket is measured, volume triples, review labor is separate, the forecast needs a date.
5. System layer: cost forecasting.
6. Eliminate infeasible: all four are sayable.
7. Eliminate constraint-violating: A ignores the tripling. C is a slogan without numbers. D invents a free tier.
8. Compare on objective: B is the only forecast with the arithmetic, the separate labor line, and the date.
9. Hidden dependencies: the per-ticket cost must be re-measured if the mix changes at higher volume.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "triples volume next quarter" and "$0.06 per ticket at 10,000 tickets per day."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Arithmetic shown | No | Yes | No | No |
| Review labor separated | No | Yes | No | No |
| Dated | No | Yes | No | No |

4. Why B satisfies all hard constraints: $0.06 x 10,000 x 30 = $18,000 per month today, times 3 = $54,000 per month, plus the labor line, with the date on the page.
5. Why B best meets the objective: V2-D6.3 requires production cost forecasting as a contract part. A forecast without arithmetic and a date is a wish.
6. Every rejected choice explained: A is the flat-line fantasy. Volume triples and the bill does not. C is the trend slogan. "Scales linearly" without the per-ticket number is unverifiable. D is the free-tier invention. No provider donates the growth tier.
7. Exact limitation or tradeoff: the per-ticket cost can shift with the volume mix, so the forecast needs re-measurement each quarter.
8. Relevant evidence (with date): cost-forecast toy arithmetic from lesson-D6-3 (§5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when volume is contractually capped at today's level. Then flat is honest. C wins never as the forecast. D wins when a real contract includes a free tier, cited with its limits.
10. Misconception tested: today's bill predicts tomorrow's bill. It does not. Multiply by the planned volume, price the labor, date the page.

## Q-D6-16 (V2-D6.4)

**Scenario.** The engineer who chose the cross-encoder reranker leaves the team. A successor must operate the choice: why it was picked, what was rejected, and when to revisit it.

**Question.** Which artifact serves the successor?

**Options.**
A) A link to the chat thread where the team discussed rerankers.
B) ADR-014 with the decision, date, alternatives, rejections, assumptions, trade-offs, owner, evidence, open issues, and review criteria.
C) Code comments that say "we use a reranker."
D) A 20-page design document written after the decision.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: knowledge-transfer artifact selection.
2. Lifecycle stage: handoff.
3. Objective: the successor operates the decision without the original meetings.
4. Hard constraints: the why, the rejected options, and the revisit conditions must all be on the page.
5. System layer: architecture documentation.
6. Eliminate infeasible: all four exist or are writable.
7. Eliminate constraint-violating: A is a thread, not a record. C states the what, not the why. D is prose written after the evidence cooled.
8. Compare on objective: B is the only artifact with the decision, the rejections, the evidence, and the review criteria together.
9. Hidden dependencies: the ADR must be written at decision time, while the evidence is fresh.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "why it was picked, what was rejected, and when to revisit it."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Decision and date recorded | Partial | Yes | No | Partial |
| Rejected options with reasons | No | Yes | No | Partial |
| Revisit conditions stated | No | Yes | No | No |

4. Why B satisfies all hard constraints: the nine fields carry the decision, the alternatives and rejections, the evidence, and the review criteria that tell the successor when to reopen it.
5. Why B best meets the objective: V2-D6.4 requires ADRs that let a successor operate the system without the original meetings. B is that artifact.
6. Every rejected choice explained: A is archaeology. The thread buries the decision among jokes and dead ends. C is a label. "We use a reranker" explains nothing about why. D is the long prose doc. Twenty pages written after the fact, with the evidence already cold.
7. Exact limitation or tradeoff: ADRs rot when code changes without a new record, and they cannot capture tacit knowledge. The review criteria field is the antidote to rot.
8. Relevant evidence (with date): the ADR mechanism and the successor test from lesson-D6-4 (§§4, 9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as the record. It wins as color beside the ADR. C wins for a config flag with no trade-off, where a commit message suffices. D wins for a greenfield design review, not a decided point.
10. Misconception tested: the code is the documentation. The code shows the what. The ADR shows the why, the rejected, and the when-to-revisit.

## Q-D6-17 (V2-D6.4)

**Scenario.** ADR-014 says the team keeps the reranker. Last month the team removed the reranker from code for cost reasons. The ADR still says "kept." A new engineer reads ADR-014 and re-adds the reranker.

**Question.** What is the best fix?

**Options.**
A) Edit ADR-014 in place to say "removed."
B) Write ADR-015 that records the removal and supersedes ADR-014, chaining the records.
C) Delete ADR-014 so no one reads a stale record.
D) Do nothing. The code is the truth.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: stale-record remediation.
2. Lifecycle stage: operation.
3. Objective: the record tells the truth again without rewriting history.
4. Hard constraints: the original decision and its evidence must survive, the removal must be recorded, the chain must be followable.
5. System layer: documentation integrity.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A rewrites history. C deletes the audit trail. D leaves the trap set.
8. Compare on objective: B records the new decision and preserves the old one in a chain.
9. Hidden dependencies: ADR-015 must link back to ADR-014 explicitly, or the chain breaks.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The ADR still says 'kept.' A new engineer reads ADR-014 and re-adds the reranker."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Current truth recorded | Yes | Yes | No | No |
| History preserved | No | Yes | No | No |
| Chain followable | No | Yes | No | No |

4. Why B satisfies all hard constraints: ADR-015 records the removal with its date and reasons, supersedes ADR-014, and leaves the original evidence intact.
5. Why B best meets the objective: V2-D6.4 treats ADRs as append-only. A change is a new ADR that supersedes. Records chain. Never edited in place.
6. Every rejected choice explained: A is the rewrite. The evidence for the original decision vanishes, and the audit trail now lies about the past. C is deletion as hygiene. The next auditor finds a gap where the decision was. D is neglect. The next reader falls into the same trap.
7. Exact limitation or tradeoff: chaining adds record count, and readers must follow the supersede links. The links are the price of an honest history.
8. Relevant evidence (with date): the append-only rule and the rotting-ADR figure from lesson-D6-4 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never for a decided ADR. C wins when the ADR was never true, a draft recorded by mistake, with the correction noted. D wins never.
10. Misconception tested: fixing a stale record means editing it. It means superseding it. Edit the past and the evidence dies with it.

## Q-D6-18 (V2-D6.4), Select TWO

**Scenario.** A successor reads ADR-014 two years later. Rerank costs doubled since the decision. She must decide whether the decision still holds.

**Question.** Which TWO fields answer that question? Select TWO.

**Options.**
A) Review criteria: "reopen if rerank cost doubles or precision drops 5 points."
B) The original eval numbers and their links.
C) The author's favorite lunch spot.
D) Assumptions that could break, including the cost assumption.
E) A summary poem about reranking.

**Answer.** A, D

**Method walk (Steps 1-10).**
1. Question type: record-field selection for a revisit decision.
2. Lifecycle stage: operation, decision review.
3. Objective: decide whether the old decision still holds under new costs.
4. Hard constraints: the question is "does it still hold," not "why was it made." The fields must name the trip conditions.
5. System layer: decision maintenance.
6. Eliminate infeasible: all five are readable.
7. Eliminate constraint-violating: C and E are not ADR fields. B shows the past, not the trip condition.
8. Compare on objective: A states the explicit reopen rule. D names the assumptions whose breakage reopens the decision.
9. Hidden dependencies: the review criteria must be written at decision time to be trustworthy now.
10. Verify: A and D together. No third field answers "still holds."

**Explanation.**
1. Correct answer: A, D.
2. Decisive scenario phrase: "She must decide whether the decision still holds."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| States the trip condition | Yes | No | No | Yes | No |
| Written at decision time | Yes | Yes | No | Yes | No |
| Answers "still holds" | Yes | Partial | No | Yes | No |

4. Why A and D satisfy all hard constraints: the review criteria fired, rerank cost doubled, which is the named trip condition. The assumptions field confirms the cost assumption was load-bearing.
5. Why A and D best meet the objective: V2-D6.4 requires review criteria on every ADR precisely so a successor can check them and run. A and D are the check.
6. Every rejected choice explained: B shows why the decision was made, not whether its conditions still hold. Past numbers do not trip. C is not a field. Lunch spots never gated a decision. E is not a field. Poems do not trip either.
7. Exact limitation or tradeoff: review criteria can fire on noise, so the successor still re-measures before reversing the decision.
8. Relevant evidence (with date): the review-criteria field and the successor test from lesson-D6-4 (§§4, 9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins when the question is "was this decision sound," not "does it still hold." C wins never. E wins never.
10. Misconception tested: the evidence field tells you when to revisit. It does not. The review criteria and the assumptions do.

## Q-D6-19 (V2-D6.4)

**Scenario.** A startup acquihires a three-person ML team. Their repo has 40 config flags and no ADRs. Time allows three ADRs this week.

**Question.** Which flags deserve ADRs first?

**Options.**
A) The three flags with the largest cost, safety, or reversibility consequences, each with a review criterion that says when to revisit it.
B) All 40 flags, each as a 20-page ADR.
C) None. Commit messages are enough.
D) Only the flags the founding engineer remembers choosing.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: documentation prioritization.
2. Lifecycle stage: handoff.
3. Objective: the highest-consequence decisions are recorded first.
4. Hard constraints: three ADRs fit the week, the flags with consequences matter most, each needs a revisit rule.
5. System layer: architecture documentation.
6. Eliminate infeasible: B does not fit the week.
7. Eliminate constraint-violating: C leaves the consequential flags undocumented. D documents by memory, not by consequence.
8. Compare on objective: A rations the three ADRs to the flags where a wrong guess costs the most.
9. Hidden dependencies: the team must agree on what counts as a consequence, or the ranking is one person's taste.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "40 config flags and no ADRs. Time allows three ADRs this week."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fits the week | Yes | No | Yes | Yes |
| Covers the consequential flags | Yes | Yes | No | Partial |
| Revisit rule included | Yes | n/a | No | No |

4. Why A satisfies all hard constraints: the three ADRs land on cost, safety, and reversibility, and each review criterion dates the decision.
5. Why A best meets the objective: V2-D6.4 rations ADRs to decisions with trade-offs. A config flag with no trade-off needs a commit message, not an ADR.
6. Every rejected choice explained: B is bureaucracy as diligence. Forty 20-page ADRs is a month of writing for flags that needed a sentence. C is the amnesia option. The consequential flags stay tribal knowledge. D is the memory lottery. Forgotten flags with real consequences stay undocumented.
7. Exact limitation or tradeoff: the ranking itself can be wrong, so the review criteria must let a successor promote a flag later.
8. Relevant evidence (with date): the ADR prioritization rule from lesson-D6-4 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins with a quarter to spend and an audit demanding full coverage. Then completeness is the requirement. C wins when no flag carries a trade-off. Then commit messages suffice. D wins never as the method.
10. Misconception tested: documentation means documenting everything. It means documenting the consequential first, with revisit rules.

## Q-D6-20 (V2-D6.4)

**Scenario.** A team flips a feature flag that changes a button label. The change is reversible in one deploy. No trade-off was debated. No compliance or cost consequence exists.

**Question.** Which record fits?

**Options.**
A) A full nine-field ADR with a formal review meeting.
B) A light ADR with the decision, date, owner, and review criterion, or a commit message if the team agrees that suffices.
C) A 20-page design document.
D) No record of any kind.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: record-weight selection.
2. Lifecycle stage: implementation.
3. Objective: the record matches the decision's weight.
4. Hard constraints: reversible in one deploy, no trade-off, no consequence.
5. System layer: documentation proportionality.
6. Eliminate infeasible: all four are producible.
7. Eliminate constraint-violating: A and C spend more than the decision is worth. D leaves even the date unknown.
8. Compare on objective: B records the decision at its true weight.
9. Hidden dependencies: the team must agree the flag is truly consequence-free, or the light record hides a real trade-off.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "reversible in one deploy. No trade-off was debated."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Weight matches the decision | No | Yes | No | No |
| Decision, date, owner known | Yes | Yes | Yes | No |
| No bureaucracy | No | Yes | No | Yes |

4. Why B satisfies all hard constraints: the light record names the decision, date, owner, and revisit rule, and the commit-message option is proportionate to a debated-nothing flag.
5. Why B best meets the objective: V2-D6.4 scales the record to the decision. A config flag with no trade-off needs a commit message, not a nine-field ADR.
6. Every rejected choice explained: A is the meeting for a label. The review costs more than the deploy it governs. C is heavier than A. Twenty pages for a button label is process satire. D is the amnesia option. Even a light decision deserves its date and owner on record.
7. Exact limitation or tradeoff: light records can hide a trade-off the team did not see. The review criterion is the safety net.
8. Relevant evidence (with date): the proportionality rule from lesson-D6-4 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the flag flips a safety or cost consequence. Then the full record is proportionate. C wins never for a flag. D wins never. Some record always beats none.
10. Misconception tested: every decision deserves the full ADR. It does not. The record matches the weight. A label gets a line.

## Q-D6-21 (V2-D6.5)

**Scenario.** A production triage agent misroutes tickets daily. There are no written requirements: no precision target, no prohibited list, no owner for the threshold. The team proposes better monitoring dashboards.

**Question.** What is the best FIRST action?

**Options.**
A) Build the monitoring dashboards.
B) Return to discovery: write the requirements, the prohibited behaviors, and the owner, then fix against them.
C) Upgrade to a larger model.
D) Add a human reviewer on every ticket.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: first action on a skipped-phase failure.
2. Lifecycle stage: operation, with a discovery gap underneath.
3. Objective: fix the missing phase, not the symptom.
4. Hard constraints: no requirements exist, the threshold has no owner, dashboards cannot invent a target.
5. System layer: lifecycle phase discipline.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A monitors against no target. C upgrades past the missing requirements. D reviews against no bar.
8. Compare on objective: B is the only option that returns to the skipped phase.
9. Hidden dependencies: the requirements need a signer, or the return trip produces another unsigned page.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "There are no written requirements: no precision target, no prohibited list, no owner for the threshold."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Returns to the skipped phase | No | Yes | No | No |
| Produces a target to fix against | No | Yes | No | No |
| Names the owner | No | Yes | No | No |

4. Why B satisfies all hard constraints: discovery writes the target, the prohibitions, and the owner, and every later fix then has a bar to hit.
5. Why B best meets the objective: V2-D6.5 states the return rule. When a later phase fails, go back to the phase whose gate was skipped. Fixing the monitoring config is a proxy fix.
6. Every rejected choice explained: A is the proxy fix the lesson names. Dashboards watch the misroutes continue against no target. C is the tier-upgrade proxy. A larger model with no requirements still has no target. D is review against no bar. Reviewers cannot enforce a threshold that was never written.
7. Exact limitation or tradeoff: returning to discovery mid-operation feels slow. That slowness is cheaper than another quarter of misroutes.
8. Relevant evidence (with date): the return rule from lesson-D6-5 (§4), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when requirements exist and the gap is truly observability. Then dashboards are the fix. C wins when evals prove the model misses a signed target. Then the tier is the fix. D wins for extreme-stakes classes with a signed bar, as the review shape, not the requirements.
10. Misconception tested: a production problem needs a production-phase fix. It needs the skipped phase. The exam asks for the first action, and the answer is the skipped phase.

## Q-D6-22 (V2-D6.5)

**Scenario.** Production is down. Customers cannot file tickets. The on-call engineer has a hotfix ready. The change process requires a design review and an ADR before any deploy.

**Question.** What is the best action?

**Options.**
A) Block the hotfix until the design review and ADR are done.
B) Ship the hotfix now, then write the ADR and hold the review in the post-incident window.
C) Run full discovery before the fix.
D) Wait for the architecture board's next meeting.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: emergency-path decision.
2. Lifecycle stage: operation, live outage.
3. Objective: restore service fast without losing the record.
4. Hard constraints: customers are down, the fix is ready, the record must still be written.
5. System layer: lifecycle pragmatics.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A lets downtime grow while process runs. C runs discovery during an outage. D schedules the fix for later.
8. Compare on objective: B restores service now and catches the record up after.
9. Hidden dependencies: the post-incident window must be real and scheduled, or the record never gets written.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Production is down. Customers cannot file tickets."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Service restored fast | No | Yes | No | No |
| Record still written | Yes | Yes | Yes | Yes |
| Proportionate to the outage | No | Yes | No | No |

4. Why B satisfies all hard constraints: the hotfix ends the downtime now, and the post-incident ADR and review preserve the decision trail.
5. Why B best meets the objective: V2-D6.5 allows the emergency path. The outage gets the shortcut, then the gate catches up. Gates serve the system.
6. Every rejected choice explained: A is bureaucracy winning over customers. The review can wait. The downtime cannot. C is the full-process reflex in the wrong moment. Discovery during an outage is process theater. D is the calendar as an excuse. The board meets later. The customers wait now.
7. Exact limitation or tradeoff: the hotfix may carry a design the review would have caught. The post-incident review must be honest enough to find it.
8. Relevant evidence (with date): the outage-shortcut figure from lesson-D6-5 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for a non-urgent change, where the gate properly precedes the deploy. C wins never during an outage. D wins never. The board does not outrank the outage.
10. Misconception tested: process first, always. Process first, except when customers are down. Then fix first, record after.

## Q-D6-23 (V2-D6.5), Select TWO

**Scenario.** The triage agent moves from the build team to the platform team. The handoff must let the new team operate it without the original meetings.

**Question.** Which TWO artifacts must the handoff include? Select TWO.

**Options.**
A) The ADR set with decisions, owners, and review criteria.
B) The runbook with the symptom map, the owner, and the escalation path.
C) A 200-slide deck with no named owner.
D) The vendor's marketing one-pager.
E) A recording of the farewell party.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: handoff-package selection.
2. Lifecycle stage: handoff.
3. Objective: the new team operates the system without the old team's meetings.
4. Hard constraints: decisions need their whys, incidents need their procedures, both need owners.
5. System layer: lifecycle handoff.
6. Eliminate infeasible: all five exist or are producible.
7. Eliminate constraint-violating: C names no owner. D is a vendor pitch, not operations. E is sentiment, not procedure.
8. Compare on objective: A carries the decisions. B carries the operations. The rest carry neither.
9. Hidden dependencies: the runbook must be current, or the new team follows a stale map.
10. Verify: A and B together. No third option passes the successor test.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "operate it without the original meetings."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Decisions with whys | Yes | No | No | No | No |
| Incident procedures | No | Yes | No | No | No |
| Owner named | Yes | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: the ADR set answers why each decision was made and when to revisit it. The runbook answers what to do when symptoms appear and who owns the call.
5. Why A and B best meet the objective: V2-D6.5 requires the handoff to carry the ADR, the risk register, and the runbook. A and B are the core of that package.
6. Every rejected choice explained: C is volume without ownership. Two hundred slides and no one to call is not a handoff. D is the vendor's story, not the system's truth. E is a lovely recording. It pages no one at 3 a.m.
7. Exact limitation or tradeoff: both artifacts rot without maintenance. The handoff must include their review cadence, not just their current text.
8. Relevant evidence (with date): the handoff requirements from lesson-D6-5 (§4) and Pair 26, Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins never as the handoff. It wins as background reading beside A and B. D wins never. E wins never.
10. Misconception tested: a handoff is a meeting. It is a package. The successor test is simple: run the system without the original meetings.

## Q-D6-24 (V2-D6.5)

**Scenario.** The agent's approval threshold was guessed during a skipped design phase. Errors cluster at the threshold. The team proposes more alerting on threshold crossings.

**Question.** What is the best action?

**Options.**
A) Add the alerts on threshold crossings.
B) Return to design: set the threshold from measured data, record it in an ADR, and then set alerts on the real number.
C) Add a real-time dashboard for the threshold.
D) Raise the threshold until complaints stop.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: proxy-fix rejection.
2. Lifecycle stage: operation, with a design gap underneath.
3. Objective: the threshold rests on measurement, then monitoring watches the real number.
4. Hard constraints: the threshold was guessed, errors cluster at it, alerts on a guessed number fire on fiction.
5. System layer: lifecycle phase discipline.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A monitors a guess. C charts a guess. D tunes by complaint volume.
8. Compare on objective: B fixes the design gap first, then monitors the measured number.
9. Hidden dependencies: the measurement needs representative data, and the ADR needs its review criterion.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The agent's approval threshold was guessed during a skipped design phase."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Threshold from measurement | No | Yes | No | No |
| Design gap closed | No | Yes | No | No |
| Monitoring on a real number | No | Yes | No | No |

4. Why B satisfies all hard constraints: the measured threshold replaces the guess, the ADR records it with a revisit rule, and the alerts then watch a number that means something.
5. Why B best meets the objective: V2-D6.5 forbids substituting later-phase work for unfinished design. Alerting is later-phase work. The design was never finished.
6. Every rejected choice explained: A is the proxy fix. Alerts on a guessed threshold fire on fiction and train the team to ignore them. C is the same proxy with charts. A dashboard does not measure the threshold. D is complaint-driven tuning. Complaints measure loudness, not the right number.
7. Exact limitation or tradeoff: measuring the threshold takes a proper eval, and the design return feels slow. The slow trip beats a fast proxy.
8. Relevant evidence (with date): the no-phase-substitution rule from lesson-D6-5 (§4), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the threshold is measured and the gap is truly observability. Then alerts are the fix. C wins alongside B as the visualization, never instead of it. D wins never as the method.
10. Misconception tested: monitoring fixes a bad threshold. It watches a bad threshold. Measurement fixes it. Monitoring follows.

## Q-D6-25 (V2-D6.5)

**Scenario.** A two-person team ships an internal tool. The process demands four formal gate reviews per change. The reviews take longer than the changes themselves.

**Question.** What is the best action?

**Options.**
A) Keep all four reviews. Process is process.
B) Right-size the gates to the team: light checks that fit two people, with the full gates reserved for production or handoff changes.
C) Drop all gates permanently.
D) Add a fifth review for safety.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: gate-proportionality decision.
2. Lifecycle stage: implementation, team process.
3. Objective: gates cost less than the risk they cover, at this team's scale.
4. Hard constraints: two people, internal tool, reviews cost more than changes.
5. System layer: lifecycle pragmatics.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A keeps a cost larger than the risk. D grows it. C removes even the cheap checks.
8. Compare on objective: B scales the gates to the stakes and keeps the full gates where they matter.
9. Hidden dependencies: the team must define which changes count as production or handoff, or the reservation is vague.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "two-person team" and "The reviews take longer than the changes themselves."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Cost below the risk covered | No | Yes | Yes | No |
| Some check remains | Yes | Yes | No | Yes |
| Full gates where stakes live | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: light checks fit a two-person flow, and the full gates still guard production and handoff changes.
5. Why B best meets the objective: V2-D6.5 warns that gates can become bureaucracy. A two-person team does not need four formal reviews. Right-size them.
6. Every rejected choice explained: A is the process absolutism the lesson warns against. The reviews cost more than the risk they cover. C is the pendulum swing. Zero gates means zero checks even where stakes appear. D is the safety theater. A fifth review multiplies the same disproportion.
7. Exact limitation or tradeoff: light gates can miss what formal gates catch. The reservation for production changes is the backstop.
8. Relevant evidence (with date): the bureaucracy limitation from lesson-D6-5 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for a regulated production system with handoffs, where four gates are proportionate. C wins for a throwaway experiment with a fixed end date and no users. D wins never.
10. Misconception tested: more gates mean more safety. Gates mean safety when their cost fits their risk. Past that, they are bureaucracy.

## Coverage: D6 questions to objectives

| Objective | Questions | Count |
|---|---|---|
| V2-D6.1 | Q-D6-01, Q-D6-02, Q-D6-03, Q-D6-04, Q-D6-05 | 5 |
| V2-D6.2 | Q-D6-06, Q-D6-07, Q-D6-08, Q-D6-09, Q-D6-10 | 5 |
| V2-D6.3 | Q-D6-11, Q-D6-12, Q-D6-13, Q-D6-14, Q-D6-15 | 5 |
| V2-D6.4 | Q-D6-16, Q-D6-17, Q-D6-18, Q-D6-19, Q-D6-20 | 5 |
| V2-D6.5 | Q-D6-21, Q-D6-22, Q-D6-23, Q-D6-24, Q-D6-25 | 5 |
| Total | | 25 |

Multi-response items: Q-D6-03, Q-D6-08, Q-D6-11, Q-D6-13, Q-D6-18, Q-D6-23 (6 of 25).
