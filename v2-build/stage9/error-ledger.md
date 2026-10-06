# The learner error ledger

Use this ledger after every practice set. One row per missed or
shaky question. The ledger converts a wrong answer into a named
mental-model repair. A row is closed only when the corrected
principle survives a new scenario.

## The 12 error classes

| # | Class | What went wrong |
|---|---|---|
| 1 | Missing fact | The answer needed a taught fact the learner never stored. |
| 2 | Wrong mechanism | The learner named the wrong cause for the effect. |
| 3 | Missed constraint | A hard constraint in the stem was skipped or softened. |
| 4 | Wrong objective | The learner answered a different objective than the item asked. |
| 5 | Wrong lifecycle stage | Discovery work was done in design, or an operations fix was offered for a design gap. |
| 6 | Wrong enforcement layer | The control was placed in a prompt, a log, or a monitor instead of code. |
| 7 | Service or protocol confusion | Two tools, APIs, or protocols were mixed up. |
| 8 | Stale knowledge | The answer used a retired model, price, or spec revision. |
| 9 | Unsupported assumption | The learner assumed a fact the stem never gave. |
| 10 | Multi-select mistake | The right count was missed, or a weak option was added, or a valid one was dropped. |
| 11 | Time-pressure mistake | The learner knew the principle and still rushed past a constraint. |
| 12 | High-confidence misconception | The learner was sure and wrong. The mental model itself needs repair. |

## Row format

Copy this block once per missed question. Fill every field. A row
with a blank field is not done.

```
Question: <question id, e.g. Q-D3-04>
My answer: <the option or options picked>
Confidence (1-5): <1 = guessed, 5 = sure>
Error class: <one of the 12 above>
Missed phrase: <the exact stem phrase that decided the item>
Mistaken model: <the rule the learner actually used>
Corrected principle: <the taught principle, in one sentence>
Counterexample: <a new mini-scenario where the old model fails>
Review date: <YYYY-MM-DD, 3 days out, then 7 days out>
```

## Worked example row 1: prompts as a money gate

```
Question: Q-D2-06
My answer: A (the system prompt refuses the $9,000 refund)
Confidence (1-5): 5
Error class: 6, wrong enforcement layer
Missed phrase: "the refund executes when the model approves it"
Mistaken model: A prompt instruction can stop a tool call.
Corrected principle: Prompts are contracts, never authorization.
The gate lives in code before the tool runs.
Counterexample: A payroll agent with "never pay twice" in the
system prompt pays a duplicate invoice when the model samples a
confident yes. A code gate on idempotency keys blocks the second
call. The prompt watches. The gate decides.
Review date: 2026-10-09, then 2026-10-16
```

## Worked example row 2: logging as removal

```
Question: Q-D3-01
My answer: C (log every call of delete_account)
Confidence (1-5): 4
Error class: 9, unsupported assumption
Missed phrase: "remove unneeded tools"
Mistaken model: Watching a tool is the same as removing it.
Corrected principle: Removal revokes. Logging only watches. A
logged tool the model can still call is still in the attack
surface.
Counterexample: An audit log records every call of a
drop_table tool. The model calls it on a confused parse of a
user request. The log proves the disaster happened. It did not
stop it. Removing the tool from the config stops
it.
Review date: 2026-10-09, then 2026-10-16
```

## Worked example row 3: tier upgrade for a template fault

```
Question: Q-D4-14
My answer: D (move to the Capable tier)
Confidence (1-5): 3
Error class: 2, wrong mechanism
Missed phrase: "the trace indicts the template"
Mistaken model: A bigger model fixes every quality fault.
Corrected principle: Fix the failing layer, not a proxy. The
trace names the layer. A tier upgrade fixes only a model-layer
fault.
Counterexample: A support bot gives wrong refund amounts. The
trace shows the template strips the currency field before the
model ever sees it. The Capable tier costs four times more and
returns the same wrong number, because the number was already
gone. Fix the template.
Review date: 2026-10-09, then 2026-10-16
```

## The remediation rule

Never re-answer the same question to prove a repair. The old
question now cues the old answer. Instead, test the corrected
principle in a new scenario. Write one fresh mini-scenario where
the mistaken model fails and the corrected principle picks the
right move. If the new scenario is solved cleanly, close the row.
If not, the row stays open and the class gets a second row.

Prioritize confident errors. A class 12 row outranks a class 11
row. A class 11 row outranks a lucky guess. Sort the weekly review
by confidence first, then by class frequency.

## Readiness thresholds: study heuristics

These bands describe study behavior. They are not exam
guarantees. No official raw-percentage pass mapping is published,
so no practice score predicts the scaled result.

| Band | Ledger signal | Meaning | Action |
|---|---|---|---|
| Red | 5 or more open rows, or 3 or more class 12 rows | Mental models are still wrong, not just facts | Stop new questions. Re-read the linked lesson sections. Close every class 12 row with a fresh scenario before the next bank. |
| Amber | 2 to 4 open rows, no class 12 | Models are mostly right, traps still bite | Work the counterfactual drills for the weak objectives. Add one new scenario per open row. |
| Green | 0 to 1 open rows | Models hold under fresh scenarios | Keep warm with the mixed bank. Add new rows for any fresh miss. |

A learner is ready to sit a full mock when two conditions
hold. The ledger holds zero open class 12 rows. Every open row
has a counterexample that passed a fresh scenario. This is a
study heuristic. It does not promise a pass.
