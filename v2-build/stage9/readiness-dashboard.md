# Readiness dashboard

A domain-by-domain checklist keyed to the blueprint weights. Work
the domains in weight order, not in comfort order. D3 first, then
D1, D4, D5, D6, D2, D7.

## The one rule of this dashboard

Every band below is a study heuristic. No official raw-percentage
pass mapping is published. A practice score cannot predict the
scaled result of 720 on the 100 to 1000 scale. Use the bands to
decide what to study next, never to decide that you will pass.

## Domain checklist

For each domain: study the lessons, close the error-ledger rows,
then test. Mark a domain ready only when all three checks hold.

| Domain | Weight | Objectives | Study | Practice | Ready when |
|---|---|---|---|---|---|
| D1 Solution Design | 17% | 6 | Lessons D1-1, D1-2, D1-patterns, D1-6 | qb-D1 (25) | The fork, the pattern spectrum, and net-value math are automatic. |
| D2 Models and Context | 13% | 5 | Lessons D2-1 to D2-5 | qb-D2 (25) | Tier picks clear the quality floor at the lowest cost. The prefix rule is automatic. |
| D3 Integration | 19% | 8 | Lessons D3-1 to D3-8 | qb-D3 (25) | Controls sit at enforceable boundaries. Removal beats logging. |
| D4 Evaluation | 16% | 6 | Lessons D4-1 to D4-6 | qb-D4 (25) | The primary metric comes from the business goal. The failing layer is fixed, not a proxy. |
| D5 Governance | 14% | 5 | Lessons D5-1 to D5-5 | qb-D5 (25) | Gates fail closed. Review strength matches consequence. |
| D6 Stakeholders | 14% | 5 | Lessons D6-1 to D6-5 | qb-D6 (25) | Adjectives become numbers before design. ADRs answer the why. |
| D7 Productivity | 7% | 3 | Lessons D7-1 to D7-3 | qb-D7 (25) | Guidance and enforcement are never confused. The runbook map is automatic. |

After the domain banks: the mixed bank (50 items), then the
counterfactual drills (52), then one mock at a time (4 mocks of 63).

## Accuracy bands

Score each domain bank separately. Bands are study heuristics, not
exam guarantees.

| Band | Domain-bank accuracy | Study meaning |
|---|---|---|
| Red | Below about two-thirds | The domain is not learned yet. |
| Amber | About two-thirds to four-fifths | The domain is learned but traps still bite. |
| Green | Above about four-fifths | The domain holds under fresh scenarios. |

The mock score note applies here too: do not convert a mock
percentage into a pass prediction. Use a weak mock domain as a
pointer back to its lessons.

## What to do at each band

Red: stop new questions in that domain. Re-read the linked
lesson sections. Re-do the section 12 recall prompts from memory.
Work the counterfactual drills for the weak objectives. Log every
miss in the error ledger with its class.

Amber: work the mixed-bank items for the weak objectives only.
Review the open error-ledger rows for that domain. For each row,
write one fresh mini-scenario and solve it. Close the row only
when the new scenario is solved cleanly.

Green: keep the domain warm. Rotate mixed-bank items across
domains. Add new ledger rows for any fresh miss, however small.
Sit a full mock only when every domain is green or amber with
zero open class 12 rows.

## Exam-day protocol: the 10-step method

Run these ten steps on every item. No step is optional. About two
minutes per item across 63 items in 120 minutes leaves no time for
a second method.

```
STEP 1: Identify what the question asks: best architecture, first
action, next action, root cause, control, metric, or optimization.
STEP 2: Identify lifecycle stage: discovery, design,
implementation, preproduction, operation, or incident response.
STEP 3: Extract the objective.
STEP 4: Extract hard constraints.
STEP 5: Identify the system layer.
STEP 6: Eliminate technically infeasible options.
STEP 7: Eliminate options violating hard constraints.
STEP 8: Compare remaining options against the objective.
STEP 9: Check hidden dependencies and consequences.
STEP 10: Verify the complete answer or multi-select combination.
```

Do not assume the exam always wants more autonomy, a larger model,
more tools, more logging, a human reviewer everywhere, a new
framework, or a complete redesign. Sometimes the best answer is:
clarify the requirement, remove an unnecessary capability, fix
retrieval, add a deterministic validation gate, narrow
permissions, or preserve an existing sufficient workflow. The
scenario, not a slogan, determines the answer.

Three-pass time plan for the 120 minutes. Pass one: answer the
items you can solve in under a minute and mark the rest. Pass two:
work the marked items with the full ten steps. Pass three: check
every multi-select count and every flagged item once. Never leave
an item blank.
