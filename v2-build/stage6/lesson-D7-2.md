# Lesson D7-2: AI-assisted workflows (V2-D7.2)

## 1. Problem this lesson solves

A developer asks the agent to fix a bug. The agent writes 400
lines, declares victory, and the developer merges. The bug is
still there. The tests never ran. The agent's claim of success
was a sentence, not evidence.

Generated code is not completed work. A workflow is complete
when evidence exists: tests ran, results were inspected, claims
match execution, and secrets stayed protected. Teams that
measure productivity by generated lines or token volume reward
the appearance of work. The exam tests the evidence bar.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A claim is not evidence</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">400 lines. Zero tests run. The bug survives the merge.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">"fixed, 400 lines"</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">bug still present</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">No test ran. The claim was prose.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">tests ran: 142 pass</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">claim matches the run</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Evidence gates the merge.</text>
<defs><marker id="m-d72-1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d72-1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">demand evidence</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Work is done when the run proves it, not when the model says it.</text>
</svg>
<figcaption>Shell 3. An unproven claim becomes a tested claim. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson D7-1 owns the hooks that enforce the evidence gates.
Lesson D5-1 owns the fail-closed law for secrets in agent
workflows.

| Foundation | What it gives this lesson |
|---|---|
| V2-D7.1 config | Hooks that run tests and lint |
| §7.2 secrets | Secrets never enter prompts or logs |

## 3. Mental model

Eight workflows, one evidence rule. Repo exploration: the
agent maps the codebase, and the evidence is a cited file
list. Implementation: code plus tests. Refactoring: tests
pass before and after. Testing: the run log, not the plan.
Review: findings tied to line numbers. Debugging: the failing
case reproduced, then fixed. Docs: examples that execute.
Incident investigation: the timeline cites logs.

The evidence rule has four parts. Tests ran: the command
executed, with output. Results inspected: a human or a
checker read the output, not just the exit code. Claims
match execution: "fixed" means the failing test now passes.
Secrets protected: no key, token, or credential in prompts,
logs, or commits.

:::takeaway
Four evidence parts: ran, inspected, matched, protected.
Productivity is verified outcomes, not generated lines.
:::

<figure class="fig">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="420" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The four-part evidence rule</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Each part answers one question a reviewer will ask.</text>
<rect x="24" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="167" font-size="13" text-anchor="middle" fill="#1B2838">"it works"</text>
<rect x="44" y="188" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="211" font-size="13" text-anchor="middle" fill="#1B2838">"trust me"</text>
<rect x="44" y="232" width="256" height="36" rx="999" fill="#E6E2DA"/>
<text x="172" y="255" font-size="13" text-anchor="middle" fill="#1B2838">log has the API key</text>
<text x="44" y="292" font-size="13" fill="#5C6B7A">Prose, not proof.</text>
<rect x="400" y="96" width="296" height="240" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="124" height="36" rx="8" fill="#E7F4EF"/>
<text x="482" y="167" font-size="12" text-anchor="middle" fill="#1B2838">ran: 142 pass</text>
<rect x="552" y="144" width="124" height="36" rx="8" fill="#E7F1F8"/>
<text x="614" y="167" font-size="12" text-anchor="middle" fill="#1B2838">inspected</text>
<rect x="420" y="188" width="124" height="36" rx="8" fill="#F6E7A8"/>
<text x="482" y="211" font-size="12" text-anchor="middle" fill="#1B2838">matched</text>
<rect x="552" y="188" width="124" height="36" rx="8" fill="#F4E6D4"/>
<text x="614" y="211" font-size="12" text-anchor="middle" fill="#1B2838">protected</text>
<rect x="420" y="232" width="256" height="36" rx="8" fill="#D9E8D3"/>
<text x="548" y="255" font-size="13" text-anchor="middle" fill="#1B2838">hook gates the merge</text>
<text x="420" y="292" font-size="13" fill="#5C6B7A">Proof, not prose.</text>
<defs><marker id="m-d72-3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="216" x2="384" y2="216" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d72-3)"/>
<text x="360" y="200" font-size="13" text-anchor="middle" fill="#1B2838">check all four</text>
<text x="24" y="376" font-size="15" fill="#1B2838">Missing one part means the work is not done.</text>
</svg>
<figcaption>Shell 4. Prose claims become four evidence parts. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

An unverified claim travels like a verified one. The agent
says "fixed." The developer merges. CI runs an hour later
and fails. The revert costs a morning. The team learns to
distrust the agent, and the distrust is correct: the
workflow had no gate.

The hook from V2-D7.1 closes the loop. A PostToolUse hook
runs the test suite after every edit. The merge requires
the run log. Claims match execution because the execution
is on the record. Secrets stay protected because the hook
scans the diff for key patterns before commit. The workflow
is: explore, implement, test, inspect, commit. Each step
leaves evidence.

Productivity math: before evidence gates, the team merged
30 agent PRs per month and reverted 9. Revert cost: 9 x 4
hours x $150 = $5,400 per month, plus the distrust tax.
After gates, 30 PRs, 1 revert: $600 per month. Savings:
$4,800 per month, $57,600 per year. The numbers are a toy.
The direction is real.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Reverts priced per month</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">30 agent PRs. 9 reverts vs 1 revert.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="13" text-anchor="middle" fill="#1B2838">9 reverts x 4 h x $150</text>
<rect x="44" y="196" width="256" height="40" rx="999" fill="#E6E2DA"/>
<text x="172" y="221" font-size="13" text-anchor="middle" fill="#1B2838">= $5,400 / month</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Claims merged without proof.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="13" text-anchor="middle" fill="#1B2838">1 revert x 4 h x $150</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="13" text-anchor="middle" fill="#1B2838">= $600 / month</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">$5,400 - $600 = $4,800 saved.</text>
<defs><marker id="m-d72-4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d72-4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">gate the merge</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Evidence is cheaper than reverts.</text>
</svg>
<figcaption>Shell 4. Ungated merges become gated merges, priced. Source: original toy.</figcaption>
</figure>

## 5. Minimal worked example

Toy: debugging workflow. The agent reproduces the bug with a
failing test: `npm test -- auth.test.js`, 1 fail, 141 pass.
It fixes the token refresh path. The hook reruns the suite:
142 pass. The developer inspects the diff: 40 lines, no
secrets. The claim "fixed" matches the run. The PR merges.

The wrong workflow: the agent edits, says "done," and the
developer merges on prose. CI fails an hour later. Revert.
Morning lost.

Mini question: "A team measures agent productivity by lines
generated per week. Reverts rise. Which change fits?
A) A bigger model that writes more lines. B) Evidence gates:
tests run on every edit via hook, run logs required on the
PR, claims checked against execution, secrets scanned. C) A
dashboard that counts tokens per developer."

### The 10-step best-answer method in action

STEP 1: Identify what the question asks: best architecture, first action, next action, root cause, control, metric, or optimization.
STEP 2: Identify lifecycle stage: discovery, design, implementation, preproduction, operation, or incident response.
STEP 3: Extract the objective.
STEP 4: Extract hard constraints.
STEP 5: Identify the system layer.
STEP 6: Eliminate technically infeasible options.
STEP 7: Eliminate options violating hard constraints.
STEP 8: Compare remaining options against the objective.
STEP 9: Check hidden dependencies and consequences.
STEP 10: Verify the complete answer or multi-select combination.

Do not assume the exam always wants more autonomy, a larger model, more tools, more logging, a human reviewer everywhere, a new framework, or a complete redesign. Sometimes the best answer is: clarify the requirement, remove an unnecessary capability, fix retrieval, add a deterministic validation gate, narrow permissions, or preserve an existing sufficient workflow. The scenario, not a slogan, determines the answer.

| Step | Action on this question |
|---|---|
| STEP 1 | Productivity metric and its fix |
| STEP 2 | Operation: the team ships with agents daily |
| STEP 3 | Raise real throughput, cut reverts |
| STEP 4 | Reverts rising. Lines metric rewards volume |
| STEP 5 | Workflow and measurement layer |
| STEP 6 | All three are feasible |
| STEP 7 | A violates the evidence rule: more lines, same reverts. C violates it too: tokens are volume, not outcomes |
| STEP 8 | B gates on evidence: ran, inspected, matched, protected |
| STEP 9 | B needs the hook maintained and the test suite fast |
| STEP 10 | B alone. Single select |

Verdict: B. The decisive error is the metric. Lines and
tokens measure volume. Evidence measures completion.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| PostToolUse hook | V2-D7.1 config | V2-D7.2 test and lint gates |
| Scoped subagents | `.claude/agents/` | V2-D7.2 review and explore roles |
| Run logs | CI, PR | V2-D7.2 "tests ran" evidence |
| Secret scan | Pre-commit hook | V2-D7.2 "secrets protected" |
| Skills | `.claude/skills/` | V2-D7.2 reusable workflow assets |

## 7. Current limitations

Evidence gates slow the loop: a 10-minute suite on every
edit taxes flow. Agents can game the gate: a test that
asserts nothing passes. Inspected results need a human, and
humans rubber-stamp. Secrets scanning misses novel key
formats. And some work has no test: docs and exploration
need different evidence, like cited files.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The gate that proves nothing</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">The suite passes. The test asserts nothing.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">142 pass, 0 fail</text>
<rect x="44" y="196" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="221" font-size="14" text-anchor="middle" fill="#1B2838">bug still present</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">The test asserted nothing.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">failing test first</text>
<rect x="420" y="196" width="256" height="40" rx="8" fill="#E7F1F8"/>
<text x="548" y="221" font-size="14" text-anchor="middle" fill="#1B2838">then the fix</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Red before green. The test earns trust.</text>
<defs><marker id="m-d72-7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m-d72-7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">reproduce first</text>
<text x="24" y="312" font-size="15" fill="#1B2838">A test that never failed proves nothing.</text>
</svg>
<figcaption>Shell 3. An empty-passing suite becomes a red-then-green suite. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Trust the claim | Merge on prose | Trivial change, instant revert |
| Volume metrics | Lines, tokens per week | Nobody measures this seriously |
| Evidence gates (this lesson) | Ran, inspected, matched, protected | Team, production, real cost of reverts |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Claim of completion | Demand the four evidence parts |
| Reverts rising | Gate the merge, not the model |
| Secrets in the workflow | Scan before commit, fail closed |
| No tests possible | Different evidence: cited files, executed examples |

## 10. Valid-but-inferior option

A dashboard that counts tokens per developer. Valid: it shows
who uses the tools. Inferior as the productivity measure: it
rewards volume, and volume without evidence is reverts.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Token dashboard | Shows adoption | Measures volume, not completion |

## 11. Counterfactual where the alternative wins

Trivial typo fix in a comment. Revert takes ten seconds.
Evidence gates win nothing: the run costs more than the
revert. Merge on prose, correctly.

| Situation | Winner | Why |
|---|---|---|
| Ten-second revert | Merge on prose | Gate cost exceeds revert cost |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. Four parts: ran, ______, matched,
   ______.
2. Productivity measures ______, not
   ______ or tokens.
3. A test that never ______ proves nothing.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
An agent refactors a payment module and
claims "all green." The suite has 200 tests
and ran in CI. List the four evidence checks
you run before merge, and the one check
that catches a test that asserts nothing.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| V2-D7.2 tests AI-assisted workflows with verification requirements: tests ran, results inspected, claims match execution, secrets protected | Official exam scope via secondary summaries | S03, S04, blueprint ledger V2-D7.2 | Sept 2026 |
| Toy arithmetic: 9 vs 1 revert per month, $5,400 vs $600, $57,600 per year | Original toy, computed above | This lesson | Oct 6, 2026 |
| Evidence over volume as productivity measure | General principle | Industry practice | Long-standing |

:::takeaway
Never merge a claim. Merge evidence. The four parts gate
every agent workflow, and the exam's productivity questions
are won by the team that checks them.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | A claim is not evidence | "fixed, 400 lines" | Tests ran, claim matched | d72-f01 | SVG | Original |
| u02 | Hooks and secrets carry over | -- | Prerequisite table | d72-f02 | Table | V2-D7.1, §7.2 |
| u03 | Four-part evidence rule | Prose claims | Four evidence parts | d72-f03 | SVG | Original |
| u04 | Reverts priced per month | $5,400 per month | $600 per month | d72-f04 | SVG | Original |
| u05 | 10-step method picks B | Three options | B gates on evidence | d72-f05 | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | d72-f06 | Table | S03, S04 |
| u07 | The gate that proves nothing | Empty pass | Red-then-green test | d72-f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | d72-f08 | Table | Original |
| u09 | Constraints decide the gate | -- | Constraint verdict table | d72-f09 | Table | Original |
| u10 | Token dashboard valid but inferior | -- | Validity vs inferiority table | d72-f10 | Table | Original |
| u11 | Trivial fix favors prose merge | -- | Counterfactual table | d72-f11 | Table | Original |
| u12 | Four parts from memory | Blank recall card | Filled from memory | d72-f12 | ASCII | Original |
| u13 | Transfer to payment refactor | Unseen question | Key in Stage 8 | d72-f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | d72-f14 | Table | Mixed |
