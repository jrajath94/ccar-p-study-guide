# Domain 3 Question Bank: Integration

25 original practice questions for objectives V2-D3.1 through V2-D3.8.
Baseline: Oct 6, 2026. Scope: blueprint v1.0 via secondary summaries (S03, S04), Sept 2026.
These are original practice items for study. They are not real exam items and do not predict exam content.
Format per question: scenario, one best answer or a marked multi-select, options, answer key, a §17 10-step method walk, and a 10-point explanation.

## Q-D3-01 (V2-D3.1)

**Scenario.** A support agent has 25 tools. One tool, `delete_account`, caused an incident: the model called it on a misread request. The proposed fix is: "Keep all 25 tools, but log every tool call for review."

**Question.** What is the best response to the proposal?

**Options.**
A) Approve, the audit trail shows exactly what fired, which helps forensics.
B) Reject, remove or tightly scope `delete_account` (confirm in code, cap its blast radius), and cut the tools the task never needs. Logging is not removal.
C) Approve, and add a second model to review each tool call.
D) Remove all 25 tools and make the agent answer from context only.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best response to a proposed fix.
2. Lifecycle stage: incident response.
3. Objective: the misread can never delete again.
4. Hard constraints: the tool can delete, the model misread once and can misread again.
5. System layer: tool configuration (capability bloat).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B removes the dangerous capability, the rest keep it armed.
9. Hidden dependencies: the scoped tool needs a confirm step and an allow-list of targets.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "log every tool call for review" after "the model called it on a misread request."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Dangerous permission removed or gated | No | Yes | No | Yes |
| Legitimate tasks keep their tools | Yes | Yes | Yes | No |
| Next misread cannot delete | No | Yes | No | Yes |

4. Why B satisfies all hard constraints: the delete capability is scoped, capped, or gated in code, unused tools leave the config.
5. Why B best meets the objective: V2-D3.1 says a tool that can write or delete gets scoped, capped, gated, or removed, and "logged for review" as the fix is rejected: logging is not removal.
6. Every rejected choice explained: A is the lesson's valid-but-inferior, the log records the next deletion beautifully but the permission stays armed. C adds a reviewer that reads the same misread request, the armed tool remains. D kills the agent's legitimate capabilities, deletion of everything is not least privilege, it is no privilege.
7. Exact limitation or tradeoff: B needs the scoping designed (who confirms, what targets are allowed), a too-tight scope can block legitimate deletes.
8. Relevant evidence (with date): "logged for review is the proposed fix: reject" from lesson-D3-1 (§9), Oct 6 2026, the 25-tool toy (12,500 vs 2,500 schema tokens) from the same lesson, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the incident were a forensics question (who did what), not a prevention question. C wins if the reviewer's inputs are trusted and the tool cannot be scoped. D wins if no legitimate task needs any tool (then the agent was the wrong pattern).
10. Misconception tested: visibility equals control. A log is forensics, only removing or gating the permission is control.

## Q-D3-02 (V2-D3.1)

**Scenario.** An agent's tool list includes `search_orders` ("look up orders by customer") and `find_orders` ("find customer orders"). It also includes `get_customer_profile`, which returns the full profile including payment details, though the task only needs the customer's name and tier.

**Question.** What is the best cleanup?

**Options.**
A) Keep both search tools for redundancy, rename the profile tool.
B) Merge the two overlapping order tools into one with a distinct description, and narrow `get_customer_profile` to return only name and tier (or split it).
C) Add logging to all three tools and review weekly.
D) Rewrite all descriptions to be longer and more detailed.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best cleanup action.
2. Lifecycle stage: operation (iteration).
3. Objective: least-privilege tool surface with no overlap.
4. Hard constraints: two tools overlap, one tool returns data the task never needs.
5. System layer: tool configuration.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the only option that both merges the overlap and narrows the data.
9. Hidden dependencies: the merged tool needs one clear description, the narrowed profile needs the tier field kept.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "look up orders by customer" vs "find customer orders", and "returns the full profile including payment details, though the task only needs the customer's name and tier."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Overlap merged | No | Yes | No | No |
| Data visibility narrowed | No | Yes | No | No |
| Selection confusion cut | No | Yes | No | Partial |

4. Why B satisfies all hard constraints: one order tool with a distinct description ends the overlap, the narrowed profile follows least privilege on data.
5. Why B best meets the objective: V2-D3.1 says overlapping descriptions merge to one, and a tool returning unneeded data gets removed or narrowed.
6. Every rejected choice explained: A keeps the overlap that causes wrong-tool picks, renaming the third tool fixes nothing. C logs the confusion instead of removing it. D writes longer descriptions for two tools that do the same job, better labels do not merge duplicates.
7. Exact limitation or tradeoff: the merge needs callers updated to the one tool, the narrowed profile needs a second tool if another task legitimately needs payment details.
8. Relevant evidence (with date): overlap and data-visibility verdicts from lesson-D3-1 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the two tools hit different backends with different SLAs (then they are not true duplicates). C wins if the question is forensics, not prevention. D wins if the descriptions are truly ambiguous but the tools are distinct.
10. Misconception tested: more description fixes tool confusion. It helps distinct tools, it cannot fix duplicates or over-wide data.

## Q-D3-03 (V2-D3.1), Select TWO

**Scenario.** A review of an agent's 40-tool config finds: (1) a `drop_table` tool unused in 6 months, (2) a `read_email` tool whose schema is 4,000 tokens, used once a day, (3) a `refund` tool used 500 times a day with proper gating, (4) a `list_users` tool returning full SSNs for a task that needs only names.

**Question.** Which TWO actions are correct? Select TWO.

**Options.**
A) Remove `drop_table`, an unused destructive tool is pure risk.
B) Keep `read_email` as is, it is used daily.
C) Narrow `list_users` to return only names.
D) Remove the `refund` tool because refunds are sensitive.
E) Keep everything and add a dashboard of tool-call counts.

**Answer.** A, C

**Method walk (Steps 1-10).**
1. Question type: config audit action (multi-select).
2. Lifecycle stage: operation (review).
3. Objective: least-privilege surface.
4. Hard constraints: unused destructive tool, over-wide data, token budget.
5. System layer: tool configuration.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A removes pure risk, C narrows over-wide data, B, D, E miss the point.
9. Hidden dependencies: removing `drop_table` needs a check that no hidden caller uses it.
10. Verify: A and C. Two selected.

**Explanation.**
1. Correct answer: A, C.
2. Decisive scenario phrase: "`drop_table` tool unused in 6 months" and "returning full SSNs for a task that needs only names."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Removes unneeded capability | Yes | No | Partial | Yes | No |
| Narrows data to the task | n/a | No | Yes | n/a | No |
| Keeps legitimate use | Yes | Yes | Yes | No | Yes |

4. Why A and C satisfy all hard constraints: A deletes a destructive tool with no users, C applies least privilege to the data.
5. Why A and C best meet the objective: V2-D3.1 says remove unneeded tools and limit data visibility, these are the two textbook applications.
6. Every rejected choice explained: B keeps a 4,000-token schema for one daily call, the token budget says count schema tokens per call and cut the unused, so the schema should shrink or the tool should narrow. D removes a gated, heavily used tool, sensitivity is handled by the gate, not by deletion. E is the dashboard version of "log everything": visibility without removal.
7. Exact limitation or tradeoff: A needs the unused claim verified (6 months of traces), C needs the names-only contract checked against future tasks.
8. Relevant evidence (with date): least-privilege and data-visibility verdicts from lesson-D3-1 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins if the 4,000-token schema is already minimal for the email task. D wins if the refund gate is found broken (then removal beats a bad gate). E wins if the question is forensics.
10. Misconception tested: used tools are fine as configured. Use does not bless scope, the data and the schema still get the least-privilege test.

## Q-D3-04 (V2-D3.2)

**Scenario.** A finance agent acts in the ERP as the employee who asked. The integration uses one shared service credential for the whole finance team. After a bad journal entry, the audit must name the human who ordered it. The log shows only the shared credential.

**Question.** What is the best fix?

**Options.**
A) Keep the shared credential but add the employee's name to the prompt.
B) Switch to per-user delegation: the agent acts with the requesting user's identity, no shared credentials where attribution matters, the ERP enforces each user's own permissions deterministically.
C) Create one credential per department instead of one for the team.
D) Log the employee's name alongside the shared credential in the application log.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best fix for an attribution failure.
2. Lifecycle stage: incident response.
3. Objective: the audit names the human.
4. Hard constraints: the ERP moves money, attribution must be per human, the current log collapses 50,000 actions a day to one name.
5. System layer: authentication and authorization.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A puts identity in the prompt, which is not authentication.
8. Compare on objective: only B gives the ERP a real per-user identity to enforce and log.
9. Hidden dependencies: delegation needs the identity provider to issue per-user tokens, the ERP must map them to permissions.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the audit must name the human who ordered it. The log shows only the shared credential."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| ERP sees the real user | No | Yes | No | No |
| Per-user permission enforced | No | Yes | Partial | No |
| Audit names the human | No | Yes | No | Partial |

4. Why B satisfies all hard constraints: per-user delegation gives each action a real identity, the ERP enforces that user's permissions, the audit trail names the human.
5. Why B best meets the objective: V2-D3.2 says no shared credentials when attribution matters, and user role claims in the prompt are not authorization.
6. Every rejected choice explained: A writes the name in the prompt, prompts are not identity, and the ERP still sees one credential. C is the lesson's valid-but-inferior: 50 shared credentials beat one, but departments are not humans and the audit still cannot name the person. D logs the name in the app log, but the ERP (the system of record) still authorized one identity, the two logs can disagree and the ERP's is the one that counts.
7. Exact limitation or tradeoff: B needs the identity plumbing (per-user tokens, ERP mapping), it is heavier than one shared secret.
8. Relevant evidence (with date): "audit must name the human: per-user delegation, no shared credentials" and "user role claims are not authZ" from lesson-D3-2 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never for identity. C wins if the audit only needs department-level attribution. D wins if the app log is the system of record for the audit (it is not here, the ERP is).
10. Misconception tested: naming the user somewhere equals authenticating the user. The enforcing system must see the identity, or the name is decoration.

## Q-D3-05 (V2-D3.2)

**Scenario.** An agent calls a partner API with a bearer token. The token crosses from the agent's network to the partner's network. Separately, the agent can trigger refunds in the company's own billing system.

**Question.** Which control pair is correct?

**Options.**
A) Trust the token because it came over TLS, let the model decide refunds from the prompt.
B) Bind the token to its audience and check the binding at receipt, enforce refund authorization deterministically at the billing system, failing closed.
C) Rotate the token weekly, add a second model to review refunds.
D) Put the token in the system prompt so it is always available, cache refund approvals for speed.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: control pair selection.
2. Lifecycle stage: design.
3. Objective: token safety across the boundary plus safe refunds.
4. Hard constraints: the token crosses a trust boundary, refunds are side effects in the owning system.
5. System layer: authentication and authorization.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: A trusts transport for identity and prose for money, D stores a secret in the prompt.
8. Compare on objective: B names both controls at the right places.
9. Hidden dependencies: audience binding needs the partner to check it, the billing check needs the approval record.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The token crosses from the agent's network to the partner's network" and "trigger refunds in the company's own billing system."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Token bound across the boundary | No | Yes | No | No |
| Refund enforced at the owning system | No | Yes | Partial | No |
| Fails closed | No | Yes | No | No |

4. Why B satisfies all hard constraints: audience binding checked at receipt stops token replay at the wrong service, deterministic enforcement at the billing system stops unauthorized refunds even if the model is fooled.
5. Why B best meets the objective: V2-D3.2 says tokens crossing a trust boundary get audience binding checked at receipt, and side effects get deterministic enforcement at the owning system.
6. Every rejected choice explained: A confuses TLS (transport privacy) with token binding (audience proof), and lets the prompt authorize money. C rotates the token but never binds it, the reviewer model reads the same untrusted inputs. D is two failures: secrets do not belong in prompts, and cached approvals are approvals the approver never gave.
7. Exact limitation or tradeoff: B needs the partner's cooperation on binding checks and the billing system's approval integration, both are real build work.
8. Relevant evidence (with date): token-boundary and side-effect verdicts from lesson-D3-2 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as a security design. C wins if the threat is token age, not token audience (rotation then helps, binding still needed). D wins never.
10. Misconception tested: TLS solves token trust. TLS protects the token in flight, binding proves where it may be used. Different threats, different controls.

## Q-D3-06 (V2-D3.2)

**Scenario.** A developer runs a local MCP server over stdio, spawned by their own agent, reading their own project files. The same agent also connects to a remote MCP server over the network that can query the company CRM.

**Question.** Which auth posture is correct?

**Options.**
A) OAuth for both servers, all MCP servers need it.
B) No auth on either, the agent is trusted.
C) Local stdio server: inherit the user's trust, OAuth adds nothing. Remote server over the network: OAuth is non-negotiable.
D) API key for the local server, nothing for the remote server since the CRM trusts the network.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: auth posture per integration type.
2. Lifecycle stage: design.
3. Objective: the right auth per trust boundary.
4. Hard constraints: local stdio is user-spawned on the user's machine, the remote server crosses the network to company data.
5. System layer: integration authentication.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: B leaves the CRM open to the network, D inverts the two (key where trust is inherited, nothing where the boundary is crossed).
8. Compare on objective: C matches the boundary to the control.
9. Hidden dependencies: the remote OAuth needs the identity provider and CRM scopes, the local server must stay stdio-local.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "local MCP server over stdio, spawned by their own agent" vs "remote MCP server over the network."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Local: no pointless auth | No | Yes | Yes | No |
| Remote: real auth to company data | Yes | No | Yes | No |

4. Why C satisfies all hard constraints: the local server runs as the user, so the user's identity is already the boundary, the remote server crosses the network, so OAuth proves who calls.
5. Why C best meets the objective: V2-D3.2 says local stdio user-spawned inherits trust (OAuth adds nothing) and remote over the network makes OAuth non-negotiable.
6. Every rejected choice explained: A applies OAuth where there is no boundary to cross, it is security theater with real config cost. B trusts the network for CRM data, the network is not a principal. D puts the key where trust is inherited and nothing where the boundary is crossed: exactly backwards.
7. Exact limitation or tradeoff: if the local server ever listens on a socket instead of stdio, the posture flips and it needs auth, the team must guard that change.
8. Relevant evidence (with date): local-vs-remote verdicts from lesson-D3-2 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the local server is shared across users on one machine (then it is not purely the user's). B wins never for company data. D wins never.
10. Misconception tested: one auth rule fits all servers. The trust boundary decides, stdio-local and network-remote are different boundaries.

## Q-D3-07 (V2-D3.3)

**Scenario.** A support pipeline has four stages: retrieval (400 ms, +6 accuracy points), rerank (700 ms, +1 point), deep reasoning (900 ms, +2 points), and verification (300 ms, +4 points). Accuracy is 93% against a 90% floor. The p95 SLA is 2 seconds, measured p95 is 2.9 seconds.

**Question.** What is the best next action?

**Options.**
A) Remove the rerank stage, it has the worst ms per accuracy point.
B) Add deeper reasoning to lift accuracy further.
C) Remove the verification stage, it is the easiest to cut.
D) Cache the retrieval results.

**Answer.** A

**Method walk (Steps 1-10).**
1. Question type: best next action under a latency SLA.
2. Lifecycle stage: operation (optimization).
3. Objective: p95 under 2 s with accuracy at or above 90%.
4. Hard constraints: measured 2.9 s vs 2 s SLA, accuracy 93% vs 90% floor (3 points of headroom).
5. System layer: per-stage latency vs accuracy.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: C removes verification, which guards correctness, the floor math must hold.
8. Compare on objective: rerank costs 700 ms per 1 point (worst ratio), removing it gives 2.2 s and 92%, still above the floor.
9. Hidden dependencies: the ms-per-point numbers must be measured, not guessed, removal needs a re-run of evals.
10. Verify: A alone. Single select.

**Explanation.**
1. Correct answer: A.
2. Decisive scenario phrase: "measured p95 is 2.9 seconds" against "p95 SLA is 2 seconds", with "Accuracy is 93% against a 90% floor."
3. Requirement-to-option matrix:

| Stage | ms | Points | ms per point |
|---|---|---|---|
| Retrieval | 400 | 6 | 67 |
| Rerank | 700 | 1 | 700 |
| Reasoning | 900 | 2 | 450 |
| Verification | 300 | 4 | 75 |

4. Why A satisfies all hard constraints: cutting rerank removes 700 ms (2.9 to 2.2 s) and 1 point (93% to 92%), which stays above the 90% floor.
5. Why A best meets the objective: V2-D3.3 says when p95 breaks the SLA, cut the stage with the worst ms per accuracy point, the table names rerank.
6. Every rejected choice explained: B is the lesson's valid-but-inferior, deeper reasoning adds 900 ms to a p95 already at 2.9 s, moving the binding constraint the wrong way. C cuts verification, the cheapest points per ms and the correctness guard, the floor math (93 - 4 = 89%) then breaks. D may help retrieval latency but does not address the measured worst ratio, and the cache needs a stable prefix to pay.
7. Exact limitation or tradeoff: A spends 1 point of headroom, if accuracy later drifts down, the team has less buffer and must revisit.
8. Relevant evidence (with date): "p95 breaks the SLA: cut the stage with the worst ms per accuracy point" from lesson-D3-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins if the SLA were loose and accuracy sat below the floor. C wins never as a first cut, verification is the guard. D wins if retrieval's 400 ms were the binding stage and the prefix is stable.
10. Misconception tested: cut the biggest latency number. The ratio decides, not the raw ms, 900 ms for 2 points beats 700 ms for 1 point.

## Q-D3-08 (V2-D3.3)

**Scenario.** A pipeline includes a "tone check" stage added last year. No eval measures its effect on any metric. The p95 is 200 ms over the SLA. The team debates its value.

**Question.** What is the best action?

**Options.**
A) Keep it, it might help user satisfaction.
B) Remove it, a stage with no measured gain loses to the SLA.
C) Move it after the response is sent so it does not count toward p95.
D) Deepen it with a second model for better tone.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best action on an unmeasured stage.
2. Lifecycle stage: operation (optimization).
3. Objective: meet the SLA.
4. Hard constraints: p95 is 200 ms over, no eval measures the stage's gain.
5. System layer: per-stage latency accounting.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the only option that treats the unmeasured stage as the suspect.
9. Hidden dependencies: removal should be a tested change with evals confirming no metric moved.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "No eval measures its effect on any metric" and "p95 is 200 ms over the SLA."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| SLA addressed | No | Yes | Trick | No |
| Decided by measurement | No | Yes | No | No |

4. Why B satisfies all hard constraints: the stage has no measured gain, so removing it is the measured move, the SLA gets its 200 ms.
5. Why B best meets the objective: V2-D3.3 says a stage with no measured gain is removed, unmeasurable complexity loses.
6. Every rejected choice explained: A keeps cost for "might", hope is not a metric. C hides the stage from p95 instead of deciding its value, the cost and the question remain. D deepens an unmeasured stage, paying more for unknown gain.
7. Exact limitation or tradeoff: if users later report tone problems, the team re-adds the stage with an eval this time, removal is reversible.
8. Relevant evidence (with date): "stage has no measured gain: remove it" from lesson-D3-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if an eval shows the tone check moves satisfaction (then it is measured). C wins if the check is truly async-safe and its value is proven. D wins never without the measurement first.
10. Misconception tested: every stage earns its place by existing. Stages earn their place by measured gain, the unmeasured one is the first suspect.

## Q-D3-09 (V2-D3.3), Select TWO

**Scenario.** A team debates pipeline changes: (1) parallelize retrieval and the user-profile lookup, which are independent, (2) add a rerank stage with no accuracy measurement yet, (3) cut the verification stage to meet the SLA, (4) spend the latency budget on accuracy because the SLA is loose and errors are costly.

**Question.** Which TWO statements are correct? Select TWO.

**Options.**
A) Change 1 is correct: when latency binds but budget is open, parallelize before deepening.
B) Change 2 is correct: rerank usually helps, so add it now and measure later.
C) Change 3 is correct: the SLA outranks everything.
D) Change 4 is correct: with a loose SLA and costly errors, spend slices on accuracy.
E) Change 1 is wrong: parallel stages are harder to debug.

**Answer.** A, D

**Method walk (Steps 1-10).**
1. Question type: change-review judgment (multi-select).
2. Lifecycle stage: operation (optimization).
3. Objective: apply the accuracy-latency rules correctly.
4. Hard constraints: the lesson's per-change verdicts.
5. System layer: pipeline latency vs accuracy.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: B adds unmeasured complexity, C cuts the correctness guard.
8. Compare on objective: A and D match the decisive-constraint table.
9. Hidden dependencies: change 1 needs the independence verified, change 4 needs the error cost priced.
10. Verify: A and D. Two selected.

**Explanation.**
1. Correct answer: A, D.
2. Decisive scenario phrase: "independent", "no accuracy measurement yet", "cut the verification stage", "SLA is loose and errors are costly."
3. Requirement-to-option matrix:

| Change | A | B | C | D | E |
|---|---|---|---|---|---|
| 1: parallelize independent | Yes | n/a | n/a | n/a | No |
| 2: unmeasured rerank | n/a | No | n/a | n/a | n/a |
| 3: cut verification | n/a | n/a | No | n/a | n/a |
| 4: loose SLA, costly errors | n/a | n/a | n/a | Yes | n/a |

4. Why A and D satisfy all hard constraints: parallelizing independent stages cuts latency without touching accuracy, a loose SLA with costly errors means the budget buys accuracy.
5. Why A and D best meet the objective: V2-D3.3 says parallelize before deepening when latency binds, and spend slices on accuracy when the SLA is loose and errors are costly.
6. Every rejected choice explained: B adds a stage with no measured gain, the lesson says unmeasurable complexity loses, measure first. C treats the SLA as outranking correctness, verification is the guard that keeps the accuracy floor honest. E is a debugging preference, not a latency argument, independence is the test, not comfort.
7. Exact limitation or tradeoff: A needs the independence proven in traces, D needs the error price real, or the spend is hope.
8. Relevant evidence (with date): decisive-constraint table from lesson-D3-3 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins after an eval measures the rerank gain (then it is a priced stage). C wins if verification's own evals show zero catch rate (then it is the unmeasured stage). E wins never as a latency argument.
10. Misconception tested: latency work and accuracy work follow one rule. They follow opposite rules depending on which constraint binds.

## Q-D3-10 (V2-D3.4)

**Scenario.** A refund agent failed at 3 AM: a $2,000 refund went to the wrong account. The on-call engineer must find which hop authorized it. The system logs model prompts but not tool calls, retrieval results, or per-hop decisions.

**Question.** What is the best next action?

**Options.**
A) Raise log retention from 7 to 90 days.
B) Add per-hop tracing first: model calls, retrieval, tool calls, and decisions tied to one request id, with tokens and cost per hop. Then investigate with the new traces.
C) Read the prompt logs carefully, the answer is usually there.
D) Restart the agent, the failure was likely transient.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best next action on an observability gap.
2. Lifecycle stage: incident response.
3. Objective: name the authorizing hop.
4. Hard constraints: the current logs cannot name any hop, money moved.
5. System layer: observability.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: only B adds the missing hops, A extends what exists.
9. Hidden dependencies: the traces must cross no trust boundary unredacted, the id must be one per run.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "logs model prompts but not tool calls, retrieval results, or per-hop decisions."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Adds the missing hops | No | Yes | No | No |
| Names the authorizing hop | No | Yes | Luck | No |

4. Why B satisfies all hard constraints: per-hop traces with one id make the run replayable, tokens and cost per hop add the attribution the incident needs.
5. Why B best meets the objective: V2-D3.4 requires end-to-end reconstructability, the lesson says retention extends what you have, it does not add what you lack.
6. Every rejected choice explained: A is the lesson's valid-but-inferior, 90 days of prompt logs still cannot name the refunding hop. C hopes the prompt log contains the tool decision, it does not by construction. D restarts the system and destroys nothing but learns nothing, the next 3 AM looks the same.
7. Exact limitation or tradeoff: B takes build time before the investigation can proceed, the team should also preserve what evidence exists now.
8. Relevant evidence (with date): "raise retention" valid-but-inferior and the full-trajectory verdict from lesson-D3-4 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the traces exist but aged out before the investigation (then retention is the gap). C wins if the fault is prompt-shaped and the prompt log is complete. D wins if the traces show a transient downstream error (evidence first, restart second).
10. Misconception tested: more retention equals more observability. Retention is time, traces are content. The gap here is content.

## Q-D3-11 (V2-D3.4)

**Scenario.** A team runs 10 million agent calls per day. Full per-hop traces would cost more than the model calls. The team must still catch failures and attribute cost per task.

**Question.** What is the best tracing design?

**Options.**
A) Trace nothing, rely on user complaints.
B) Full traces on every call, observability is worth any cost.
C) Sample deep traces, keep skeleton traces for the rest, keep all errors in full, and record tokens and dollars per hop on every call.
D) Keep full traces for 90 days and delete the rest.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: best tracing design at scale.
2. Lifecycle stage: design.
3. Objective: catch failures and attribute cost without outspending the models.
4. Hard constraints: 10M calls per day, full traces cost more than the calls.
5. System layer: observability at scale.
6. Eliminate infeasible: B is financially infeasible at this volume.
7. Eliminate constraint-violating: A abandons failure detection entirely.
8. Compare on objective: C keeps the failure signal (all errors full) and the cost signal (per-hop tokens and dollars) at a fraction of full-trace cost.
9. Hidden dependencies: the sample must be representative, the skeleton must carry the request id and the outcome.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "10 million agent calls per day" and "Full per-hop traces would cost more than the model calls."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Failures catchable | No | Yes | Yes | Partial |
| Cost per task attributable | No | Yes | Yes | No |
| Cost fits the volume | Yes | No | Yes | Partial |

4. Why C satisfies all hard constraints: sampling bounds the trace bill, full error traces keep the failure signal, per-hop tokens and dollars give cost attribution on every call.
5. Why C best meets the objective: V2-D3.4 says when volume forbids full traces, sample deep, skeleton the rest, and keep all errors.
6. Every rejected choice explained: A saves the trace bill and loses the product, user complaints are not monitoring. B is correct in principle and bankrupt in practice at 10M calls a day. D keeps 90 days of whatever exists, if the traces are skeletons, 90 days of skeletons still cannot replay a failure.
7. Exact limitation or tradeoff: sampled traces can miss a rare failure mode, the team must watch the error stream (kept in full) for the sampling gaps.
8. Relevant evidence (with date): volume verdict from lesson-D3-4 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as a design. B wins at 1,000 calls a day where full traces are cheap. D wins if the gap is retention, not trace depth.
10. Misconception tested: observability is all or nothing. At scale it is tiered: deep samples, skeletons, full errors, and cost on every hop.

## Q-D3-12 (V2-D3.4)

**Scenario.** An agent's traces include full user messages, which sometimes contain account numbers and passwords. The traces ship to a third-party analytics service. The security team flags the pipeline.

**Question.** What is the best fix?

**Options.**
A) Stop tracing user messages entirely.
B) Redact secrets and PII from traces before they cross the trust boundary to the analytics service, keep the redaction in code and tested.
C) Ask the analytics vendor to promise not to look at the data.
D) Encrypt the traces, the vendor can decrypt as needed.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best fix for a trace-data leak.
2. Lifecycle stage: incident response.
3. Objective: analytics continue without secrets leaving.
4. Hard constraints: traces cross a trust boundary to a third party, secrets are in the messages.
5. System layer: observability plus data handling.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: C trusts a promise for secrets, D gives the vendor the keys to the secrets.
8. Compare on objective: B keeps the traces useful and the secrets home.
9. Hidden dependencies: the redaction patterns must cover account numbers and passwords, tests must prove they fire.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "traces ship to a third-party analytics service" with "account numbers and passwords" inside.
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Secrets stay inside | Yes | Yes | No | No |
| Traces stay useful | No | Yes | Yes | Yes |

4. Why B satisfies all hard constraints: redaction in code before the boundary means the third party never receives the secrets, the traces keep their diagnostic value.
5. Why B best meets the objective: V2-D3.4 says traces crossing a trust boundary get secrets and PII redacted first.
6. Every rejected choice explained: A protects the secrets by destroying the traces, the team loses the failure signal. C is a promise, not a control, the data still leaves. D encrypts in flight but the vendor decrypts, the secrets still arrive.
7. Exact limitation or tradeoff: redaction patterns need maintenance, a new secret format slips through until the patterns learn it.
8. Relevant evidence (with date): trust-boundary verdict from lesson-D3-4 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the messages have no diagnostic value beyond the secrets (rare). C wins never for secrets. D wins if the vendor is inside the trust boundary (then it is not third-party).
10. Misconception tested: encryption solves data sharing. Encryption protects the pipe, redaction decides what may travel. The boundary question is what leaves, not how.

## Q-D3-13 (V2-D3.5)

**Scenario.** A finance RAG bot answers from annual reports. Users report wrong numbers from tables: the chunker splits tables mid-row, so "revenue 2024" and its value land in different chunks. The team proposes swapping to a larger embedding model.

**Question.** What is the best response?

**Options.**
A) Approve the embedding swap, better vectors lift recall.
B) Reject the swap, re-chunk at structure boundaries so tables stay whole, then re-run evals. Better vectors over broken chunks still retrieve broken chunks.
C) Increase the chunk count per query from 5 to 15.
D) Fine-tune the embedding model on finance text.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best response to a proposed fix (diagnosis).
2. Lifecycle stage: operation (iteration).
3. Objective: correct table numbers.
4. Hard constraints: the trace names split tables, an upstream chunking fault.
5. System layer: RAG pipeline (chunking stage).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B fixes the indicted stage, the rest polish other stages.
9. Hidden dependencies: structure-aware chunking needs the document structure parsed, evals must include table questions.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "the chunker splits tables mid-row, so 'revenue 2024' and its value land in different chunks."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixes the split tables | No | Yes | No | No |
| Fixes upstream first | No | Yes | No | No |

4. Why B satisfies all hard constraints: structure-boundary chunking keeps rows whole, the eval re-run proves the fix.
5. Why B best meets the objective: V2-D3.5 says chunk by document structure and query type, and wrong answer with right pipeline shape means diagnose per stage, fix upstream first.
6. Every rejected choice explained: A is the lesson's valid-but-inferior, better embeddings can lift recall on paraphrases, but better vectors over broken chunks still retrieve broken chunks. C retrieves more broken pieces, fifteen split rows do not make a whole table. D trains vectors for a chunking fault, the fault is where the cuts fall, not what the vectors mean.
7. Exact limitation or tradeoff: structure-aware chunking costs parser work per document type, a new layout needs its rules.
8. Relevant evidence (with date): "tables split: re-chunk at structure boundaries" and "fix the failing component, not a proxy" from lesson-D3-5 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the chunks are whole but paraphrased queries miss (then recall is the fault). C wins if the fault is too few chunks, not broken ones. D wins if finance jargon truly defeats the base embeddings on whole chunks.
10. Misconception tested: retrieval quality is an embedding problem. The pipeline has ten stages, the trace names the guilty one, and here the guilty stage is the chunker.

## Q-D3-14 (V2-D3.5), Select TWO

**Scenario.** A legal assistant must cite the exact clause for every claim in its answers. The corpus is 50,000 contracts, updated weekly.

**Question.** Which TWO pipeline choices are required? Select TWO.

**Options.**
A) The full pipeline with grounding and citation checks: retrieval, rerank, assembly, generation, then a code check that each claim maps to a cited chunk.
B) Chunking by document structure (clauses stay whole) with metadata (contract id, date, parties).
C) A weekly full fine-tune on the new contracts.
D) The smallest embedding model to save cost.
E) Generation without retrieval, relying on the model's training data.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: pipeline design for cited answers (multi-select).
2. Lifecycle stage: design.
3. Objective: every claim cited to its clause.
4. Hard constraints: 50,000 contracts, weekly updates, citations mandatory.
5. System layer: RAG pipeline.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: E cannot cite sources it never retrieved, C trains weekly for a retrieval problem.
8. Compare on objective: A is the pipeline the citation requirement demands, B makes the chunks citable.
9. Hidden dependencies: the citation check needs the chunk ids in the trace, the metadata needs the contract fields parsed.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "must cite the exact clause for every claim" and "updated weekly."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Claims checkable vs source | Yes | n/a | No | n/a | No |
| Clauses retrievable whole | n/a | Yes | n/a | n/a | n/a |
| Weekly updates handled | Yes | Yes | Slow | n/a | No |

4. Why A and B satisfy all hard constraints: the full pipeline with the grounding check enforces the citation rule, structure chunking plus metadata makes each clause addressable.
5. Why A and B best meet the objective: V2-D3.5 says answers needing citations get the full pipeline with grounding checks, and chunking follows document structure.
6. Every rejected choice explained: C fine-tunes weekly for a knowledge-cutoff problem, re-ingestion cadence beats fine-tuning and the tuned model still cannot cite. D picks the embedding by price alone, the choice needs an eval, and cheap vectors that miss clauses fail the citation bar. E is the anti-RAG: no retrieval means no source, so no citation is possible.
7. Exact limitation or tradeoff: the full pipeline is the expensive option, the citation requirement is what justifies it.
8. Relevant evidence (with date): "answers need citations: full pipeline with grounding checks" and "knowledge changes weekly: re-ingestion cadence beats fine-tuning" from lesson-D3-5 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the task is style or judgment rather than knowledge (then retrieval is not the answer). D wins if evals show the small embeddings clear the recall bar. E wins never for cited answers.
10. Misconception tested: fine-tuning replaces the RAG pipeline. It replaces knowledge the model must memorize, citations need retrieval, and weekly change needs re-ingestion.

## Q-D3-15 (V2-D3.5)

**Scenario.** A RAG bot's answers got worse after a re-ingestion. The pipeline shape is unchanged. Traces show the new chunks are twice as long and split sections mid-paragraph. Retrieval recall on the eval set fell from 88% to 71%.

**Question.** What is the best next action?

**Options.**
A) Swap to a larger embedding model.
B) Add a rerank stage.
C) Roll back the chunking change (or fix the chunker to restore structure boundaries), since the trace indicts the chunking stage.
D) Increase the number of retrieved chunks.

**Answer.** C

**Method walk (Steps 1-10).**
1. Question type: best next action from a diagnosed regression.
2. Lifecycle stage: incident response.
3. Objective: restore recall to 88%.
4. Hard constraints: the failure starts on the re-ingestion date, the trace indicts chunking.
5. System layer: RAG pipeline (ingestion/chunking).
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: C fixes the indicted stage, the rest compensate around it.
9. Hidden dependencies: the rollback needs the old chunker config versioned, the fix needs structure rules.
10. Verify: C alone. Single select.

**Explanation.**
1. Correct answer: C.
2. Decisive scenario phrase: "got worse after a re-ingestion" and "the new chunks are twice as long and split sections mid-paragraph."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixes the indicted stage | No | No | Yes | No |
| Restores the known-good state | No | No | Yes | No |

4. Why C satisfies all hard constraints: the failure starts on the change date, so the change is the first suspect, restoring the chunker restores the 88%.
5. Why C best meets the objective: V2-D4.4 says failure starting on a change date means suspect that layer first, and V2-D3.5 says fix upstream first.
6. Every rejected choice explained: A is the proxy fix again, better vectors over mid-paragraph splits still retrieve splits. B adds a stage to compensate for broken chunks, rerank cannot unsplit a paragraph. D retrieves more broken chunks, volume does not repair cuts.
7. Exact limitation or tradeoff: the rollback needs the old config, if the old chunker is gone, the team re-implements structure boundaries and re-ingests.
8. Relevant evidence (with date): change-date diagnosis from lesson-D4-4 (§9) and upstream-first from lesson-D3-5 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the chunks are unchanged and only the embeddings changed (then the embedding stage is the suspect). B wins if recall is fine but precision is low (rerank is the precision stage). D wins if the eval shows too few chunks retrieved, not broken ones.
10. Misconception tested: regressions need new capabilities. They need the change log, the newest change is the first suspect, and the trace confirms it.

## Q-D3-16 (V2-D3.6)

**Scenario.** A parts assistant gets two query shapes: "bearing 6204-ZZ dimensions" (exact part code) and "which bearing fits a humid conveyor" (paraphrase, no code). The current semantic-only index misses the exact-code queries.

**Question.** What is the best retrieval change?

**Options.**
A) Bigger embedding model.
B) Hybrid retrieval: keyword for the code-bearing queries, semantic for the paraphrases, with rank fusion, metadata filters for the part family.
C) Keyword-only for all queries.
D) Rebuild the index every 5 minutes.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best retrieval strategy for mixed queries.
2. Lifecycle stage: operation (iteration).
3. Objective: both query shapes answered.
4. Hard constraints: exact codes need keyword, paraphrases need semantic.
5. System layer: retrieval strategy.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B gives each shape its mechanism and fuses the ranks.
9. Hidden dependencies: the fusion weights need tuning on the eval set, the metadata needs the part family parsed.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "exact part code" vs "paraphrase, no code", and "semantic-only index misses the exact-code queries."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Exact codes found | No | Yes | Yes | No |
| Paraphrases found | Yes | Yes | No | Partial |
| Mixed shapes handled | No | Yes | No | No |

4. Why B satisfies all hard constraints: keyword catches the code, semantic catches the paraphrase, rank fusion merges, metadata filters narrow by family.
5. Why B best meets the objective: V2-D3.6 says a code or name in the query means keyword must be in the mix, a paraphrase means semantic must be in the mix, and mixed shapes mean hybrid with rank fusion.
6. Every rejected choice explained: A improves vectors but semantic search still misses exact codes, the mechanism is the gap, not the model. C flips the failure: keyword-only misses the paraphrases. D rebuilds the same semantic-only index faster, freshness is not the fault.
7. Exact limitation or tradeoff: hybrid needs the fusion tuned, bad weights let one signal drown the other.
8. Relevant evidence (with date): keyword/semantic/hybrid verdicts from lesson-D3-6 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the miss is paraphrase recall on whole chunks (then vectors are the fault). C wins if all queries carry codes (then keyword alone suffices). D wins if the fault is stale data, not query shape.
10. Misconception tested: one retrieval mode fits all queries. The query shape picks the mode, mixed shapes need the hybrid.

## Q-D3-17 (V2-D3.6)

**Scenario.** A shopper asks the assistant: "Where is my order right now?" The order index rebuilds every 60 minutes. The team proposes rebuilding every 5 minutes.

**Question.** What is the best response?

**Options.**
A) Approve, 5-minute rebuilds cut the staleness window from 60 minutes to 5.
B) Reject, put a live order-status tool call behind the assistant instead. The answer changes faster than any refresh, so it belongs behind a tool call, not a stale index.
C) Approve, and also rebuild every minute for even fresher data.
D) Cache the last answer per user for speed.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best response to a freshness proposal.
2. Lifecycle stage: operation (iteration).
3. Objective: the present order status, not a snapshot.
4. Hard constraints: the status changes continuously, any snapshot lags.
5. System layer: retrieval vs tool data.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B gives the present with one call, A gives a 5-minute-old past at 288 rebuilds a day.
9. Hidden dependencies: the tool needs the order system's live API and the user's order id.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Where is my order right now?" and "The order index rebuilds every 60 minutes."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Answer is the present | No | Yes | No | No |
| Cost sane | 288 rebuilds/day | One call | 1,440 rebuilds/day | Cheap but stale |

4. Why B satisfies all hard constraints: the tool reads the live system, the answer is the present, not a snapshot.
5. Why B best meets the objective: V2-D3.6 says live transactional state belongs behind a tool call, not a stale index, a faster snapshot is still a snapshot.
6. Every rejected choice explained: A is the lesson's valid-but-inferior, 288 rebuilds a day of 1,000 documents, and the answer can still lag a shipment by 5 minutes. C multiplies the cost to 1,440 rebuilds for a 1-minute lag, the curve never reaches the present. D serves the last answer fast, "fast" and "wrong" is not a tradeoff the shopper wants.
7. Exact limitation or tradeoff: B depends on the order API being up, the design needs a fallback message when the tool fails.
8. Relevant evidence (with date): live-data verdict from lesson-D3-6 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the data changes hourly and the question tolerates the lag (then the index fits). C wins never as a principled answer. D wins if the question asks for the last known status explicitly.
10. Misconception tested: fresher snapshots solve freshness. Snapshots solve slowness of snapshots, only the live call solves freshness.

## Q-D3-18 (V2-D3.6), Select THREE

**Scenario.** A company assistant serves 10,000 employees. Documents carry department ACLs. Queries mix exact project names and paraphrased questions. Some answers (headcount, salaries) change daily.

**Question.** Which THREE retrieval rules are correct? Select THREE.

**Options.**
A) Apply the metadata ACL filter before scoring, so users never see documents they cannot open.
B) Use hybrid retrieval with rank fusion for the mixed query shapes.
C) Index the daily headcount numbers and rebuild nightly.
D) Put headcount and salary lookups behind a tool call to the HR system.
E) Drop the ACL filter for speed, the model will keep secrets.

**Answer.** A, B, D

**Method walk (Steps 1-10).**
1. Question type: retrieval rule selection (multi-select).
2. Lifecycle stage: design.
3. Objective: correct answers with access control and fresh numbers.
4. Hard constraints: ACLs vary by user, query shapes mix, some facts change daily.
5. System layer: retrieval strategy.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: E trusts the model with access control, the model is not an ACL. C serves day-old numbers for daily-changing facts.
8. Compare on objective: A enforces access before scoring, B handles the mixed shapes, D keeps live facts live.
9. Hidden dependencies: the ACL metadata must be current, the fusion needs tuning, the HR tool needs the requester's identity.
10. Verify: A, B, and D. Three selected.

**Explanation.**
1. Correct answer: A, B, D.
2. Decisive scenario phrase: "Documents carry department ACLs", "mix exact project names and paraphrased questions", and "change daily."
3. Requirement-to-option matrix:

| Test | A | B | C | D | E |
|---|---|---|---|---|---|
| Access enforced | Yes | n/a | n/a | n/a | No |
| Mixed shapes handled | n/a | Yes | n/a | n/a | n/a |
| Daily facts fresh | n/a | n/a | No | Yes | n/a |

4. Why A, B, and D satisfy all hard constraints: the ACL filter before scoring means unauthorized documents never reach the model, hybrid covers both query shapes, the tool call gives the present headcount.
5. Why A, B, and D best meet the objective: V2-D3.6 says access varying by user means metadata ACL filter before scoring, mixed shapes mean hybrid with rank fusion, and fast-changing answers belong behind a tool call.
6. Every rejected choice explained: C indexes daily-changing numbers with a nightly rebuild, the numbers can lag a full day. E is the documented trap: the model does not enforce ACLs, and retrieved-then-filtered leaks through the context.
7. Exact limitation or tradeoff: the ACL filter needs the metadata fresh, stale ACLs either leak or over-block. The HR tool needs per-user auth so one employee cannot pull another's salary.
8. Relevant evidence (with date): ACL, hybrid, and live-data verdicts from lesson-D3-6 (§9), Oct 6 2026, "preserve source-system ACLs" from V2-D3.2, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the numbers change weekly and the question tolerates the lag. E wins never as a design.
10. Misconception tested: the model can keep secrets it retrieved. It cannot be trusted to, the filter must run before scoring, in code.

## Q-D3-19 (V2-D3.7)

**Scenario.** A platform team needs one "search tickets" capability available to agents written in Python, TypeScript, and Go, running on laptops, CI runners, and a hosted agent service. Three teams will consume it.

**Question.** Which integration mechanism fits best?

**Options.**
A) A direct API client written separately in each language.
B) One MCP server exposing the ticket search with one schema, consumed by all hosts and languages.
C) A CLI wrapper around the existing ticket CLI, parsed per language.
D) An agent-to-agent handoff: each team runs its own search agent.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best integration mechanism.
2. Lifecycle stage: design.
3. Objective: one capability, many hosts and languages, three consumers.
4. Hard constraints: three languages, three runtimes, reuse across teams.
5. System layer: integration mechanism.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B gives one server and one schema for all consumers, A triples the client work.
9. Hidden dependencies: the server needs versioning and auth for the three teams.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "agents written in Python, TypeScript, and Go" and "Three teams will consume it."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| One schema for all | No | Yes | Partial | No |
| Reuse across teams | No | Yes | Partial | No |
| No per-language client work | No | Yes | No | n/a |

4. Why B satisfies all hard constraints: one MCP server, one schema, every host and language connects the same way.
5. Why B best meets the objective: V2-D3.7 says many hosts or languages means MCP: one server, one schema.
6. Every rejected choice explained: A writes and maintains three clients for one capability, the reuse the scenario demands is exactly what MCP sells. C wraps a CLI and parses per language, fragile parsing times three languages. D runs three search agents, the subtask needs no planning, so the agents add coordination for nothing.
7. Exact limitation or tradeoff: B needs the server operated, versioned, and secured, the protocol cost pays off only because reuse is real here.
8. Relevant evidence (with date): "many hosts or languages: MCP, one server, one schema" from lesson-D3-7 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for one host and one language (direct API, skip the protocol). C wins if the capability exists only as a CLI and the team is one (wrapper, parse carefully). D wins if the subtask needs its own plan and tools (agent to agent with a handoff contract).
10. Misconception tested: MCP is the default for every integration. It is the answer when reuse across hosts or languages is real, otherwise the scenario decides.

## Q-D3-20 (V2-D3.7)

**Scenario.** One team, one Python service, needs to call the company's internal pricing API (8 endpoints) from its agent. A teammate proposes building an MCP server for the pricing API "for future reuse."

**Question.** What is the best response?

**Options.**
A) Approve, MCP is the modern standard and reuse may come.
B) Reject the server, use the direct API client. One host, one language, 8 tools, 1 consumer: the direct call ships in a day and the exam rewards the present scenario, not the imagined future.
C) Build the MCP server but skip auth for speed.
D) Wrap the API in a CLI first, then put MCP on the CLI.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best response to a mechanism proposal.
2. Lifecycle stage: design.
3. Objective: the pricing capability live with minimum sound cost.
4. Hard constraints: one host, one language, one consumer, no reuse named.
5. System layer: integration mechanism.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: C ships an unauthenticated server, the scenario names company pricing data.
8. Compare on objective: B ships in a day, A builds a server, a client, lifecycle handling, and version negotiation for no named consumer.
9. Hidden dependencies: the direct client still needs the API's auth.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "One team, one Python service" and "for future reuse" with no consumer named.
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Ships fast | No | Yes | No | No |
| Reuse real, not imagined | No | n/a | No | No |
| Auth handled | Yes | Yes | No | Partial |

4. Why B satisfies all hard constraints: the direct client covers one host and one language with the API's own auth.
5. Why B best meets the objective: V2-D3.7 says one host and one language means direct API, skip the protocol, and "use MCP" with no reuse named is rejected: the scenario decides.
6. Every rejected choice explained: A is the lesson's valid-but-inferior: the protocol works and a second host later would reuse it, but now it is a server plus a client plus versioning for 8 tools and 1 consumer. C keeps the server cost and drops auth, the worst of both. D stacks two mechanisms (CLI then MCP) for a direct-call problem, each layer adds parsing and failure modes.
7. Exact limitation or tradeoff: if a second team or language appears, the team re-evaluates, the direct client is then the thing to wrap.
8. Relevant evidence (with date): "one host, one language: direct API, skip the protocol" and the valid-but-inferior MCP server from lesson-D3-7 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when three teams in three languages are named (then reuse is real). C wins never. D wins if the API exists only as a CLI (then the wrapper is the honest answer, without MCP on top).
10. Misconception tested: building for imagined reuse is free. The protocol has a price, the scenario must name the reuse that pays it.

## Q-D3-21 (V2-D3.7)

**Scenario.** Two integration needs: (1) a 20-year-old mainframe capability exposed only through a terminal CLI, needed by one agent, (2) a fraud-review subtask that needs its own plan, its own tools, and its own context, separate from the main agent.

**Question.** Which mechanism pair is correct?

**Options.**
A) MCP server for the mainframe, direct API for the fraud review.
B) CLI wrapper for the mainframe (parse carefully), agent-to-agent with a handoff contract for the fraud review.
C) Direct API for both.
D) Managed runtime for both, accept the platform limits.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: mechanism pair selection.
2. Lifecycle stage: design.
3. Objective: the right mechanism per need.
4. Hard constraints: the mainframe speaks only CLI, the fraud subtask needs its own plan, tools, and context.
5. System layer: integration mechanism.
6. Eliminate infeasible: C is infeasible for the mainframe (no API exists).
7. Eliminate constraint-violating: none violate outright beyond C's infeasibility.
8. Compare on objective: B matches each need to its mechanism.
9. Hidden dependencies: the CLI parse needs tests for format changes, the handoff needs the contract (input, output, merge rule).
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "exposed only through a terminal CLI" and "needs its own plan, its own tools, and its own context."
3. Requirement-to-option matrix:

| Need | A | B | C | D |
|---|---|---|---|---|
| 1: CLI-only capability | Partial | Yes | No | Partial |
| 2: own plan, tools, context | No | Yes | No | No |

4. Why B satisfies all hard constraints: the wrapper meets the mainframe where it is, the agent-to-agent handoff gives the subtask its own loop and envelope.
5. Why B best meets the objective: V2-D3.7 says legacy capability with CLI only gets a CLI wrapper (parse carefully), and a subtask needing its own plan and tools gets agent-to-agent with a handoff contract.
6. Every rejected choice explained: A builds an MCP server for a CLI-only mainframe (a server around a screen-scrape) and gives the fraud subtask a direct API, which cannot carry a plan. C is infeasible on need 1: no API exists. D rents a platform for two needs neither of which wants platform limits, the mainframe still needs its wrapper underneath.
7. Exact limitation or tradeoff: CLI parsing is brittle, the wrapper needs format-change tests. The subagent needs an owner and a contract, or it becomes a second unsupervised loop.
8. Relevant evidence (with date): CLI-wrapper and agent-to-agent verdicts from lesson-D3-7 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the mainframe capability must serve many hosts (then the MCP server earns its keep). C wins if the mainframe gains a real API. D wins if the team wants zero ops and accepts the limits.
10. Misconception tested: one mechanism covers all integrations. The capability's shape (CLI-only) and the subtask's shape (own plan) pick different mechanisms.

## Q-D3-22 (V2-D3.7), Select TWO

**Scenario.** A team must choose mechanisms for: (1) a shared vector-search capability used by 6 agent services in 2 languages, (2) a single Python agent calling the team's own billing API, (3) a prototype the team wants to run with zero ops effort.

**Question.** Which TWO mechanism matches are correct? Select TWO.

**Options.**
A) Need 1: MCP server, one schema for the 6 services and 2 languages.
B) Need 2: direct API client, one host and one language.
C) Need 3: a hand-rolled Kubernetes operator for full control.
D) Need 1: six separate direct clients, one per service.
E) Need 2: agent-to-agent handoff with a supervisor.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: mechanism matching (multi-select).
2. Lifecycle stage: design.
3. Objective: the right mechanism per need.
4. Hard constraints: reuse across services and languages for need 1, single host and language for need 2.
5. System layer: integration mechanism.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A matches many-hosts reuse to MCP, B matches single-host to direct API.
9. Hidden dependencies: the MCP server needs versioning, the direct client needs the billing API's auth.
10. Verify: A and B. Two selected.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "6 agent services in 2 languages" and "a single Python agent calling the team's own billing API."
3. Requirement-to-option matrix:

| Need | A | B | C | D | E |
|---|---|---|---|---|---|
| 1: 6 services, 2 languages | Yes | n/a | n/a | No | n/a |
| 2: one host, one language | n/a | Yes | n/a | n/a | No |
| 3: zero ops | n/a | n/a | No | n/a | n/a |

4. Why A and B satisfy all hard constraints: the MCP server gives one schema to all consumers, the direct client ships in a day for the single host.
5. Why A and B best meet the objective: V2-D3.7 maps many hosts or languages to MCP and one host plus one language to direct API.
6. Every rejected choice explained: C answers "zero ops" with a hand-rolled operator, the highest-ops choice on the list, a managed runtime is the zero-ops mechanism. D writes six clients for one capability, the exact duplication MCP exists to prevent. E gives a single API call a supervisor and a handoff contract, the call needs no plan.
7. Exact limitation or tradeoff: the MCP server's ops cost is justified by the 6 services, with one service it would not be.
8. Relevant evidence (with date): mechanism verdicts from lesson-D3-7 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins if the team wants full control and accepts the ops (then it is not the zero-ops need). D wins if the services cannot share a schema for regulatory reasons. E wins if the billing call grows into a subtask with its own plan and tools.
10. Misconception tested: mechanism choice is about taste. It is about reuse, boundaries, ownership, and ops, the scenario's counts decide.

## Q-D3-23 (V2-D3.8)

**Scenario.** A research agent has 200 tools. Each call carries about 100,000 schema tokens. Wrong-tool picks grow with the surface size. The token budget binds.

**Question.** What is the best change?

**Options.**
A) Rewrite all 200 descriptions to be more distinct.
B) Move to progressive discovery: show tool names first, load full schemas on demand, shrink the visible choice set per task.
C) Remove 100 tools at random to halve the surface.
D) Move to the most capable tier for better tool selection.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: best change for tool-surface overload.
2. Lifecycle stage: operation (iteration).
3. Objective: cut token overhead and wrong-tool picks.
4. Hard constraints: 200 tools, 100,000 schema tokens per call, both tokens and wrong picks named.
5. System layer: capability discovery.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B attacks both named problems, A attacks only one.
9. Hidden dependencies: discovery needs the name list to be searchable and the schema load to be cheap.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "200 tools", "100,000 schema tokens", and "Wrong-tool picks grow with the surface size."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Cuts token overhead | No | Yes | Yes | No |
| Cuts wrong-tool picks | Partial | Yes | Partial | Partial |
| Principled, not random | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: names-first cuts the per-call schema tokens, on-demand schemas keep capability, the smaller visible set cuts selection confusion.
5. Why B best meets the objective: V2-D3.8 says tool surface above about 20 tools with binding tokens means progressive discovery.
6. Every rejected choice explained: A is the lesson's valid-but-inferior, clearer descriptions cut confusion but keep 100,000 schema tokens per call and 200 open doors, better labels answer only one of the two named problems. C halves the surface by luck, the removed 100 may include the tools the task needs. D buys better selection at top-tier prices while the 100,000 tokens still bill every call.
7. Exact limitation or tradeoff: discovery adds a lookup hop, the name index must stay accurate or the agent cannot find the right tool.
8. Relevant evidence (with date): progressive-discovery verdict from lesson-D3-8 (§9-§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the surface is small (20 tools) and the problem is labels only. C wins if half the tools are provably unused (then it is a prune, not randomness). D wins if the tier cannot do tool selection at all (capability fault).
10. Misconception tested: better descriptions fix tool overload. They fix confusion, not tokens and not attack surface, the surface size is its own problem.

## Q-D3-24 (V2-D3.8)

**Scenario.** A team with 150 tools debates two fixes: rewrite every description (3 weeks of work) or build progressive discovery (2 weeks of work). The complaints are both slow calls (token-heavy schemas) and wrong-tool picks.

**Question.** Which fix should the team choose, and why?

**Options.**
A) Rewrite descriptions, it is the simpler change.
B) Progressive discovery, it answers both complaints, while rewritten descriptions answer only the wrong picks and keep the token cost.
C) Do both, more fixes are better.
D) Neither, 150 tools are fine as is.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: fix selection under two complaints.
2. Lifecycle stage: operation (iteration).
3. Objective: fix tokens and wrong picks with one change.
4. Hard constraints: both complaints named, 150 tools.
5. System layer: capability discovery.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: B is the only single fix that answers both complaints.
9. Hidden dependencies: the discovery index needs the tool names and purposes accurate.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "both slow calls (token-heavy schemas) and wrong-tool picks."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Fixes token overhead | No | Yes | Yes | No |
| Fixes wrong picks | Yes | Yes | Yes | No |
| One change, not two | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: names-first removes the schema tokens from the hot path, the smaller visible set cuts the picks.
5. Why B best meets the objective: V2-D3.8's decisive rule names both tokens and wrong picks as the discovery triggers, the rewrite answers one.
6. Every rejected choice explained: A is real work that answers half the complaint, the token bill survives. C does both at 5 weeks, the rewrite's marginal gain over discovery alone does not justify 3 weeks. D denies the measured complaints.
7. Exact limitation or tradeoff: discovery's lookup hop adds latency, the team should measure it against the saved schema tokens.
8. Relevant evidence (with date): "rewrite descriptions" valid-but-inferior from lesson-D3-8 (§10), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins if the token budget is open and only wrong picks hurt. C wins if the descriptions are also dangerously ambiguous (then the rewrite has its own justification). D wins if the complaints are anecdotal with no measurements.
10. Misconception tested: doing both is always safer. Sequencing matters, the fix that answers both complaints comes first, and the second fix must earn its weeks.

## Q-D3-25 (V2-D3.8), Select THREE

**Scenario.** A team compares discovery designs: (1) a 12-tool agent where latency binds harder than tokens, (2) a 200-tool agent where tasks are known in advance per team, (3) a 200-tool agent with ad-hoc tasks and a binding token budget.

**Question.** Which THREE statements are correct? Select THREE.

**Options.**
A) Case 1: monolithic context is fine, with 12 tools and latency binding harder than tokens, the discovery hop costs more than it saves.
B) Case 2: static per-task subsets beat discovery, the tasks are known, so each team gets its narrowed tool list.
C) Case 3: progressive discovery wins, ad-hoc tasks plus a binding token budget are its triggers.
D) Case 1: progressive discovery is mandatory above 10 tools.
E) Case 2: keep all 200 tools visible for flexibility.

**Answer.** A, B, C

**Method walk (Steps 1-10).**
1. Question type: discovery-design judgment (multi-select).
2. Lifecycle stage: design.
3. Objective: the right discovery per case.
4. Hard constraints: the lesson's per-case verdicts (surface size, latency vs tokens, task known or ad-hoc).
5. System layer: capability discovery.
6. Eliminate infeasible: all are feasible.
7. Eliminate constraint-violating: none violate outright.
8. Compare on objective: A, B, and C each match the decisive table.
9. Hidden dependencies: case 2's subsets need the task taxonomy maintained, case 3's discovery needs the name index accurate.
10. Verify: A, B, and C. Three selected.

**Explanation.**
1. Correct answer: A, B, C.
2. Decisive scenario phrase: "12-tool agent where latency binds harder than tokens", "tasks are known in advance per team", "ad-hoc tasks and a binding token budget."
3. Requirement-to-option matrix:

| Case | A | B | C | D | E |
|---|---|---|---|---|---|
| 1: 12 tools, latency binds | Yes | n/a | n/a | No | n/a |
| 2: tasks known | n/a | Yes | n/a | n/a | No |
| 3: ad-hoc, tokens bind | n/a | n/a | Yes | n/a | n/a |

4. Why A, B, and C satisfy all hard constraints: the monolithic 12-tool context avoids a discovery hop that costs more than it saves, static subsets give known tasks their narrowed lists with zero lookup, discovery answers the ad-hoc plus binding-tokens case.
5. Why A, B, and C best meet the objective: V2-D3.8 says latency binding harder than tokens with a small set means monolithic, tasks known in advance mean static per-task subsets, and surface above about 20 tools with binding tokens means progressive discovery.
6. Every rejected choice explained: D invents a "mandatory above 10 tools" rule, the lesson's triggers are surface size plus binding tokens plus wrong picks, and case 1 fails the latency test. E keeps 200 doors open for known tasks, flexibility the tasks never use is attack surface.
7. Exact limitation or tradeoff: static subsets need the taxonomy maintained, a new task type needs its subset designed. Discovery's lookup hop needs measuring against the saved schema tokens.
8. Relevant evidence (with date): per-case verdicts from lesson-D3-8 (§9), Oct 6 2026, exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: D wins never, no single tool-count rule exists. E wins if the tasks are truly ad-hoc per team (then case 2 becomes case 3).
10. Misconception tested: progressive discovery is always the answer. It is the answer for its triggers, small sets, known tasks, and latency-bound designs have their own answers.

## Coverage: D3 questions to objectives

| Objective | Questions | Count |
|---|---|---|
| V2-D3.1 | Q-D3-01, Q-D3-02, Q-D3-03 | 3 |
| V2-D3.2 | Q-D3-04, Q-D3-05, Q-D3-06 | 3 |
| V2-D3.3 | Q-D3-07, Q-D3-08, Q-D3-09 | 3 |
| V2-D3.4 | Q-D3-10, Q-D3-11, Q-D3-12 | 3 |
| V2-D3.5 | Q-D3-13, Q-D3-14, Q-D3-15 | 3 |
| V2-D3.6 | Q-D3-16, Q-D3-17, Q-D3-18 | 3 |
| V2-D3.7 | Q-D3-19, Q-D3-20, Q-D3-21, Q-D3-22 | 4 |
| V2-D3.8 | Q-D3-23, Q-D3-24, Q-D3-25 | 3 |
| Total | | 25 |

Multi-response items: Q-D3-03, Q-D3-09, Q-D3-14, Q-D3-18, Q-D3-22, Q-D3-25 (6 of 25).

Hmm, point 6 and 9 again dance around the "equally defensible" problem. C is correct, and with Select TWO the item is flawed per the task's rewrite rule. Let me fix properly: change the scenario so C is wrong, or make it Select THREE with A, B, C. Cleanest: make it Select THREE, answer A, B, C, and adjust distractors so only D and E are wrong. That is uniquely defensible. Rewrite the question.

Actually wait n/a D says "progressive discovery is mandatory above 10 tools" n/a wrong (invented rule). E says keep all 200 visible for known tasks n/a wrong. So Select THREE with A, B, C works cleanly. Let me rewrite.
