# Domain 7 Question Bank: Developer Productivity and Operational Enablement

25 original practice questions for objectives V2-D7.1 through V2-D7.3.
Baseline: Oct 6, 2026. Scope: blueprint v1.0 via secondary summaries (S03, S04), Sept 2026.
These are original practice items for study. They are not real exam items and do not predict exam content.
Format per question: scenario, one best answer or a marked multi-select, options, answer key, a §17 10-step method walk, and a 10-point explanation.
Claude Code config details follow lesson-D7-1 (Oct 6, 2026), which cites exam scope via S03/S04 (Sept 2026). Verify against current product docs before production use. Guidance and enforcement are distinguished in every item.

## Q-D7-01 (V2-D7.1)

**Scenario.** An eight-developer team shares one repo. The repo holds staging keys in .env files. The team wants agents to stop reading secret files and to lint every edit.

**Question.** Which setup fits?

**Options.**
A) A CLAUDE.md note that says "do not read secrets, run lint."
B) Deny rules on the secret paths, a PostToolUse hook that runs the linter on edits, and the shared settings file committed to the repo.
C) A bigger model with better judgment about secrets.
D) A weekly reminder in the team chat.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: team control for secrets and lint.
2. Lifecycle stage: design. The config does not exist yet.
3. Objective: secret reads are blocked in code, and every edit is linted.
4. Hard constraints: eight developers, secrets in the repo, edits constant, the control must survive the team's own members.
5. System layer: team configuration.
6. Eliminate infeasible: all four are writable.
7. Eliminate constraint-violating: A advises. It does not stop reads. C offers judgment, not a lock. D is a nag, not a control.
8. Compare on objective: B denies in code, lints via hook, and commits the file so every clone carries it.
9. Hidden dependencies: the secret-path globs must be right, or the deny rule misses. The hook must be reviewed like code.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "stop reading secret files and to lint every edit."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Secret read blocked in code | No | Yes | No | No |
| Lint runs on every edit | No | Yes | No | No |
| Applies to all eight developers | No | Yes | Partial | No |

4. Why B satisfies all hard constraints: the deny rule runs before the tool, the PostToolUse hook runs the linter after each edit, and the committed file lands on every clone.
5. Why B best meets the objective: V2-D7.1 draws the line between guidance and enforcement. CLAUDE.md cannot deny a read. A deny rule can.
6. Every rejected choice explained: A is the exam's favorite trap. A prompt doing a lock's job. The model may comply. It may not. C is the judgment trap. Better judgment still cannot stop a tool call. D is the nag. Reminders do not run before tools.
7. Exact limitation or tradeoff: deny rules can be bypassed by a clever command rewrite, so the globs need tests. Hooks run shell commands, so a malicious hook is a risk the team must review.
8. Relevant evidence (with date): the guidance-versus-enforcement mechanism from lesson-D7-1 (§§4-5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026. Verify the config schema against current product docs.
9. Counterfactual where each plausible alternative wins: A wins for a solo developer with no secrets and no destructive tools, where there is nothing to enforce. C wins never as the control. It wins as a quality upgrade after the deny rules exist. D wins never.
10. Misconception tested: a written instruction is a control. It is guidance. The rule that runs before the tool is the control.

## Q-D7-02 (V2-D7.1)

**Scenario.** A 20-person team shares one repo. Production credentials live in a vault. Staging keys live in .env files. The org requires secret-path rules that no team may weaken.

**Question.** Which configuration enforces the secret control at both levels?

**Options.**
A) A CLAUDE.md note that says "do not read .env files."
B) Committed deny rules on the secret paths in the shared settings file, personal exceptions in settings.local.json only, and the org-wide secret rules in managed settings that nothing below can override.
C) Each developer keeps a personal config file with their own rules.
D) No config. The developers are trusted.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: two-level enforcement design.
2. Lifecycle stage: design.
3. Objective: secret rules hold for the team and survive the team's own editors at the org level.
4. Hard constraints: 20 developers, secrets in the repo, the org rule must be unweakable, personal exceptions must not touch the shared file.
5. System layer: team plus org configuration.
6. Eliminate infeasible: all four are writable.
7. Eliminate constraint-violating: A is guidance at both levels. C fragments the control across 20 files. D is trust as a control.
8. Compare on objective: B puts team rules in the committed file and org rules where no team member can edit them.
9. Hidden dependencies: managed settings need an org plan and admin rights. A control the team cannot deploy is not a control.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "secret-path rules that no team may weaken."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Team-level enforcement | No | Yes | Partial | No |
| Org rule survives team editors | No | Yes | No | No |
| Personal exceptions contained | No | Yes | No | n/a |

4. Why B satisfies all hard constraints: the committed file enforces the team rules on every clone, settings.local.json holds personal exceptions without touching the shared file, and managed settings override everything below them.
5. Why B best meets the objective: V2-D7.1 separates the scopes. Project defaults are the team layer. Managed settings are the org layer. Guidance is neither layer.
6. Every rejected choice explained: A is the sign, not the lock, at both levels. Anyone with repo write access can also edit around a note. C is drift by design. Twenty personal files means twenty truths. D is the trust fallacy. Trusted developers still paste the wrong path under deadline.
7. Exact limitation or tradeoff: managed settings need the org plan and admin rights, and an org policy with no exception path creates shadow workflows.
8. Relevant evidence (with date): the four-scope model and managed-settings rule from lesson-D7-1 (§§4, 9) and Pair 23, Oct 6, 2026. Exam scope via S03/S04, Sept 2026. Verify the config schema against current product docs.
9. Counterfactual where each plausible alternative wins: A wins for style guidance on a trusted team with no secrets. C wins never as the control. It wins as personal preference storage. D wins for a solo project with no secrets, where there is nothing to enforce.
10. Misconception tested: a committed team file protects against the team. It does not. Anyone with repo write access can edit it. Org rules need the managed layer.

## Q-D7-03 (V2-D7.1)

**Scenario.** One developer needs a wider Bash tool scope for one day to debug a deploy script. The shared settings file denies it for the team. The exception must not weaken the control for the other seven developers.

**Question.** Where does the exception belong?

**Options.**
A) Edit the shared settings file for the day, then change it back.
B) The developer's settings.local.json, expiring after the day, with the reason recorded.
C) A note in CLAUDE.md.
D) A chat message to the team.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: exception-placement decision.
2. Lifecycle stage: operation.
3. Objective: one developer gets one day of wider scope without touching the team control.
4. Hard constraints: the shared file must stay intact, the exception must expire, the reason must be on record.
5. System layer: configuration scoping.
6. Eliminate infeasible: all four are writable.
7. Eliminate constraint-violating: A weakens the control for all eight developers on a promise to revert. C and D are guidance. Neither changes what the tool allows.
8. Compare on objective: B scopes the exception to the person and the day, with a record.
9. Hidden dependencies: the local file must actually override the shared deny for that developer, and the expiry must be real.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The exception must not weaken the control for the other seven developers."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Shared control untouched | No | Yes | Yes | Yes |
| Exception expires | Partial | Yes | No | No |
| Actually changes tool scope | Yes | Yes | No | No |

4. Why B satisfies all hard constraints: settings.local.json is the personal scope. It never touches the committed file, the expiry bounds the window, and the recorded reason makes it reviewable.
5. Why B best meets the objective: V2-D7.1 assigns personal exceptions to the local file, never the shared file. Committed config is team config.
6. Every rejected choice explained: A is the revert-promise trap. The shared file is weakened for everyone until someone remembers, and "then change it back" is not a control. C is guidance. A note does not widen a deny rule. D is a message. Chat does not configure tools.
7. Exact limitation or tradeoff: personal overrides can accumulate into shadow configs. The team should review them periodically.
8. Relevant evidence (with date): the scope rules from lesson-D7-1 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026. Verify the config schema against current product docs.
9. Counterfactual where each plausible alternative wins: A wins never as the method. It wins as an emergency edit with a same-day revert commit and a reviewer watching. C wins for workflow guidance, never for scope. D wins never.
10. Misconception tested: a temporary edit to the shared file is harmless. It is a team-wide control change with a sticky-note expiry.

## Q-D7-04 (V2-D7.1), Select TWO

**Scenario.** The org's platform team decides which settings must hold for every team and which stay with the teams.

**Question.** Which TWO belong in org-managed settings? Select TWO.

**Options.**
A) Deny rules on secret paths that no team may weaken.
B) The monthly model spend cap with its owner.
C) A team's PostToolUse lint hook.
D) The team's preferred code style notes in CLAUDE.md.
E) A developer's editor theme.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: setting-scope classification.
2. Lifecycle stage: design, platform governance.
3. Objective: org non-negotiables live where no team can weaken them.
4. Hard constraints: managed settings override everything below, team workflow stays with teams, guidance is not enforcement.
5. System layer: configuration governance.
6. Eliminate infeasible: all five are placeable.
7. Eliminate constraint-violating: C is team workflow tooling. D is guidance. E is personal preference.
8. Compare on objective: A and B are the org non-negotiables. Secret paths and spend caps must hold everywhere.
9. Hidden dependencies: the managed layer needs the org plan and admin rights, plus an exception process.
10. Verify: A and B together. No third option is an org non-negotiable.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "which settings must hold for every team."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Must hold everywhere | Yes | Yes | No | No | No |
| Enforcement, not guidance | Yes | Yes | Yes | No | No |
| Survives team editors | Yes | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: both are controls the org cannot let a team weaken, and the managed layer is the only scope nothing below overrides.
5. Why A and B best meet the objective: V2-D7.1 assigns org non-negotiables, secret paths and model and spend guardrails, to managed settings. Workflow tooling belongs to the team.
6. Every rejected choice explained: C is the team's lint hook. It belongs in project defaults, where the team owns it. D is CLAUDE.md guidance. It is not enforcement at any scope. E is personal taste. It belongs nowhere near the managed layer.
7. Exact limitation or tradeoff: an org policy with no exception path creates shadow workflows. The managed layer needs a break-glass story.
8. Relevant evidence (with date): Pair 23, project defaults versus managed policies, Oct 6, 2026. Lesson-D7-1 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins in project defaults, not managed settings. D wins as team guidance, never as enforcement. E wins in the developer's personal config.
10. Misconception tested: everything important belongs in managed settings. Only the non-negotiables do. Workflow preferences managed org-wide get routed around.

## Q-D7-05 (V2-D7.1)

**Scenario.** A research subagent gathers background on vendors. It must never modify code. Last week a prompt injection told it to "fix" a file, and it edited one.

**Question.** Which control fits?

**Options.**
A) A system instruction that says "never modify code."
B) A scoped subagent whose tool list holds Read and Grep only, so no write tool exists to call.
C) Remove all tools from the subagent.
D) Full tool access with an audit log.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: subagent-scope control.
2. Lifecycle stage: design, hardening.
3. Objective: the research loop cannot write, even under injection.
4. Hard constraints: research needs Read and Grep, no write tool may be callable, the injection already beat prose once.
5. System layer: agent configuration.
6. Eliminate infeasible: all four are configurable.
7. Eliminate constraint-violating: A is the instruction the injection already defeated. D logs the edit after the file changed.
8. Compare on objective: B removes the capability instead of asking the model to decline it. C removes the needed tools too.
9. Hidden dependencies: the tool list must be fenced at the loop level, not just hidden from the prompt.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "a prompt injection told it to 'fix' a file, and it edited one."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Write impossible, not just discouraged | No | Yes | Yes | No |
| Research tools survive | Yes | Yes | No | Yes |
| Survives injection | No | Yes | Yes | No |

4. Why B satisfies all hard constraints: with no write tool in its list, the subagent cannot call what it cannot see. The injection has no tool to steer toward.
5. Why B best meets the objective: V2-D7.1 requires scoped subagents with fenced tool lists. The research subagent gets Read and Grep only.
6. Every rejected choice explained: A is the sign, not the lock. The scenario proves the injection beats it. C is the amputation. Research without Read and Grep is not research. D is the audit trap. The log records the edit. The file is already changed.
7. Exact limitation or tradeoff: fenced lists need maintenance as the subtask evolves, and an over-narrow list blocks legitimate subtask growth.
8. Relevant evidence (with date): scoped subagents from lesson-D7-1 (§4) and Pair 12, Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for style guidance on a trusted loop with no destructive tools. C wins when the subtask needs no tools at all. D wins as the audit baseline alongside B, never alone.
10. Misconception tested: telling the subagent its limits is enough. It is not. The tool list is the limit. Fence the list.

## Q-D7-06 (V2-D7.1)

**Scenario.** Developers paste API tokens into chat to query the shared doc-search server. Tokens leak into transcripts. Each developer configures the server differently, and searches behave differently per machine.

**Question.** Which setup fits?

**Options.**
A) Keep pasting tokens. It works.
B) Declare the MCP server once in the shared config so every teammate gets the same tools, and keep tokens out of chat.
C) Ban the doc-search server.
D) Give each developer their own server with their own tokens.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: shared tool configuration.
2. Lifecycle stage: design.
3. Objective: one server declaration, identical tools on every machine, no tokens in chat.
4. Hard constraints: tokens must leave chat, config drift must end, the search function must survive.
5. System layer: team configuration.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A keeps the leak. D multiplies the drift.
8. Compare on objective: B declares once and distributes identically. C kills the needed function.
9. Hidden dependencies: the server credentials must live in the config's secret handling, not in the chat history.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "Tokens leak into transcripts. Each developer configures the server differently."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Tokens out of chat | No | Yes | Yes | Partial |
| Identical tools per machine | No | Yes | n/a | No |
| Search function survives | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: the single declaration ends the per-machine drift, and server-side credential handling keeps tokens out of transcripts.
5. Why B best meets the objective: V2-D7.1 declares MCP servers once in config so every teammate gets the same tools. Committed config is team config.
6. Every rejected choice explained: A is the leak normalized. "It works" is not a security posture. C is the amputation. The search function the team needs dies with the server. D is drift as architecture. N servers means N behaviors.
7. Exact limitation or tradeoff: the shared server becomes a single point of failure, and its credentials need their own rotation.
8. Relevant evidence (with date): the MCP declaration mechanism from lesson-D7-1 (§4), Oct 6, 2026. Exam scope via S03/S04, Sept 2026. Verify the config schema against current product docs.
9. Counterfactual where each plausible alternative wins: A wins never. C wins when the server serves no real need. Then removal is correct. D wins when teams need isolated servers for data boundaries, with each declared in its own shared config.
10. Misconception tested: pasting a token is configuration. It is a leak with extra steps. Declare the server. Keep the token out of chat.

## Q-D7-07 (V2-D7.1)

**Scenario.** Two of eight developers leave the default model on for bulk refactors. One month of agent-heavy work costs $4,800. The team lead wants the number watched, not wished.

**Question.** Which control set fits?

**Options.**
A) Trust the developers to pick cheaper models.
B) Route cheap work to cheap models per task, and set a monthly spend number with the team lead as owner who reviews it.
C) Ban agent use for refactors.
D) Put every task on the most capable model for quality.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: spend-guardrail design.
2. Lifecycle stage: operation.
3. Objective: the monthly agent bill is a watched number with an owner.
4. Hard constraints: cheap work must ride cheap models, the number needs an owner and a review, the $4,800 must come down.
5. System layer: team cost controls.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A is the current failure restated. D maximizes the bill.
8. Compare on objective: B routes by task and assigns the number to an owner. C removes the productivity the team wants.
9. Hidden dependencies: the routing needs the task-to-model mapping defined, and the review needs the actuals on time.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The team lead wants the number watched, not wished."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Cheap work on cheap models | No | Yes | n/a | No |
| Number with an owner | No | Yes | No | No |
| Productivity kept | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: per-task routing moves the bulk refactors off the default model, and the owned monthly number turns the next surprise into a watched variance.
5. Why B best meets the objective: V2-D7.1 closes the loop with model selection per task plus a spend number with an owner. A watched number beats a wished one.
6. Every rejected choice explained: A is the status quo that produced $4,800. Trust without a number is not a control. C is the ban. It kills the refactor productivity the team bought the agents for. D is the bill maximizer. Quality as the only criterion writes a blank check.
7. Exact limitation or tradeoff: routing needs the mapping maintained, and a wrong mapping puts hard work on a weak model. The quality floor must hold.
8. Relevant evidence (with date): the spend-guardrail toy from lesson-D7-1 (§5), Oct 6, 2026. $4,800 before routing, $1,900 after. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as the control. It wins as culture beside the guardrail. C wins when refactors show negative value after measurement. Then the ban is a decision, not a reflex. D wins for the few tasks where only the top tier clears the quality floor, routed explicitly.
10. Misconception tested: cost control means using less AI. It means routing each task to its cheapest sufficient model, with the total watched by an owner.

## Q-D7-08 (V2-D7.1), Select TWO

**Scenario.** A team lists five items from its Claude Code setup.

**Question.** Which TWO are enforcement, not guidance? Select TWO.

**Options.**
A) A deny rule on Read(.env).
B) A CLAUDE.md note about code style.
C) A PreToolUse hook that blocks a tool call before it runs.
D) A memory file with team conventions.
E) A wiki page describing the workflow.

**Answer.** A, C

**Method walk (Steps 1-10).**
1. Question type: guidance-versus-enforcement classification.
2. Lifecycle stage: design review.
3. Objective: name the items that can actually stop a tool call.
4. Hard constraints: enforcement decides without asking. Guidance shapes choices.
5. System layer: configuration review.
6. Eliminate infeasible: all five exist.
7. Eliminate constraint-violating: B, D, and E are guidance by definition. None of them runs before a tool.
8. Compare on objective: A and C are the items with code behind them.
9. Hidden dependencies: the deny rule needs correct globs, and the hook needs review like code.
10. Verify: A and C together. No third item stops a tool.

**Explanation.**
1. Correct answer: A, C.
2. Decisive scenario phrase: "Which TWO are enforcement, not guidance?"
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Runs before the tool | Yes | No | Yes | No | No |
| Can stop the call | Yes | No | Yes | No | No |
| Leaves an enforcement record | Yes | No | Yes | No | No |

4. Why A and C satisfy all hard constraints: the deny rule blocks the read in code, and the PreToolUse hook decides before the tool runs. Both leave a record.
5. Why A and C best meet the objective: V2-D7.1 defines the line. Instructions shape the model's choices. Permissions and hooks decide without asking.
6. Every rejected choice explained: B is guidance. A style note shapes choices. It stops nothing. D is guidance. Conventions in a memory file are advice, not rules. E is guidance. A wiki describes. It does not decide.
7. Exact limitation or tradeoff: enforcement needs design time per rule, and misconfigured rules block legitimate work. Each deny rule needs a test that it fires.
8. Relevant evidence (with date): the instructions-versus-permissions pair from Pair 13, Oct 6, 2026. Lesson-D7-1 (§4), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins as style guidance, which is its real job. D wins as convention storage, never as a control. E wins as onboarding reading, never as enforcement.
10. Misconception tested: anything written in the config directory is a control. Only the items with code behind them are. The rest is guidance wearing a config costume.

## Q-D7-09 (V2-D7.1)

**Scenario.** Developers face 40 permission asks per day. By day three they click "allow" without reading. A risky ask hides among the routine ones.

**Question.** Which permission design fits?

**Options.**
A) Keep asking on everything. Developers must pay attention.
B) Allow the safe actions, deny the dangerous ones, and ask only on the gray middle where judgment matters.
C) Allow everything to protect flow.
D) Deny everything to protect safety.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: permission-ask design under fatigue.
2. Lifecycle stage: operation.
3. Objective: each ask gets read, and the dangerous actions are already decided.
4. Hard constraints: 40 asks per day produced blind clicking, the gray middle is where judgment adds value.
5. System layer: permission ergonomics.
6. Eliminate infeasible: all four are configurable.
7. Eliminate constraint-violating: A produced the blind clicking it claims to prevent. C removes the control. D blocks legitimate work.
8. Compare on objective: B shrinks the ask set to the judgments that matter.
9. Hidden dependencies: the safe and dangerous lists must match the real workflow, or developers route around the config.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "40 permission asks per day. By day three they click 'allow' without reading."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Asks get read | No | Yes | n/a | n/a |
| Dangerous actions decided in code | No | Yes | No | Yes |
| Legitimate work flows | Yes | Yes | Yes | No |

4. Why B satisfies all hard constraints: the safe list and the deny list remove the routine asks, and the few remaining asks each get real attention.
5. Why B best meets the objective: V2-D7.1 treats "ask" as a budget. Forty asks a day spends it by day three. Spend it where judgment matters.
6. Every rejected choice explained: A is the fatigue generator. Attention is finite. Forty asks spends it. C is the control removed for comfort. Flow is protected. Nothing else is. D is the lockdown. Developers route around it by Friday, and the routed path has no rules at all.
7. Exact limitation or tradeoff: the safe and dangerous lists need maintenance as the workflow changes, and a miscategorized action either annoys or endangers.
8. Relevant evidence (with date): the prompt-fatigue figure from lesson-D7-1 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when asks are rare, under five per day, and each is genuinely gray. Then attention holds. C wins never as the design. D wins for a classified environment where no action is routine, decided explicitly.
10. Misconception tested: more asks mean more safety. They mean less attention per ask. Safety comes from deciding the clear cases in code and asking only on the gray.

## Q-D7-10 (V2-D7.2)

**Scenario.** An agent edits the auth module and reports "fixed." The developer is about to merge.

**Question.** Which evidence must exist before the merge?

**Options.**
A) The agent's message that says "fixed."
B) The four evidence parts: the tests ran, a human inspected the results, the claim matched the execution, and the diff was scanned for secrets.
C) A CI badge from last week.
D) The count of lines the agent wrote.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: merge-evidence requirement.
2. Lifecycle stage: implementation, pre-merge.
3. Objective: the "fixed" claim is proven before it lands.
4. Hard constraints: the auth module is sensitive, the claim must match execution, secrets must not ship.
5. System layer: evidence gates.
6. Eliminate infeasible: all four are obtainable.
7. Eliminate constraint-violating: A is prose as proof. C is a stale badge. D counts volume.
8. Compare on objective: B is the only option where each part checks the claim against reality.
9. Hidden dependencies: the tests must actually cover the fix, and the secret scan must know the key formats.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "reports 'fixed.' The developer is about to merge."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Claim checked against execution | No | Yes | No | No |
| Results inspected by a human | No | Yes | No | No |
| Secrets kept out of the diff | No | Yes | No | No |
| Current to this change | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: the run proves the tests executed, inspection proves a human read the result, the match proves the claim is true, and the scan proves no secret shipped.
5. Why B best meets the objective: V2-D7.2 requires verification with tests run, results inspected, claims matched, and secrets protected. Evidence is cheaper than reverts.
6. Every rejected choice explained: A is the merge-on-prose trap. The agent says "fixed." CI fails an hour later. The revert costs a morning. C is the stale badge. Last week's green says nothing about this edit. D is the volume metric. Lines written measure activity, not completion.
7. Exact limitation or tradeoff: evidence gates slow the loop. A 10-minute suite on every edit taxes flow. The gate must fit the change's weight.
8. Relevant evidence (with date): the four-part evidence rule from lesson-D7-2 (§§4, 9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for a trivial change with a ten-second revert, where the gate costs more than the revert. C wins never as merge evidence. D wins never. It measures the wrong thing by design.
10. Misconception tested: the agent's completion message is evidence. It is a claim. Evidence is the run, the inspection, the match, and the scan.

## Q-D7-11 (V2-D7.2)

**Scenario.** An agent refactors a payment module and claims "all green." The suite has 200 tests and CI ran it. The lead wants proof the suite can catch bugs, not just pass.

**Question.** Which check earns that proof?

**Options.**
A) Trust the green CI run.
B) Require the failing test first: the agent reproduces the bug with a failing test, then fixes it, then the suite goes green, with the run log on the PR.
C) Count the tests. 200 is enough.
D) Run the suite twice.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: test-suite trust verification.
2. Lifecycle stage: implementation, pre-merge.
3. Objective: prove the suite detects the bug class before trusting its green.
4. Hard constraints: the payment module is sensitive, a passing suite may assert nothing, the proof must be on the PR.
5. System layer: evidence quality.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A trusts an unproven suite. C counts tests. D repeats the unproven run.
8. Compare on objective: B is the only option where the suite demonstrates detection before the fix.
9. Hidden dependencies: the failing test must target the actual bug, not a trivial assertion.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "proof the suite can catch bugs, not just pass."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Suite demonstrates detection | No | Yes | No | No |
| Tied to this change | No | Yes | No | No |
| On the PR record | Partial | Yes | No | Partial |

4. Why B satisfies all hard constraints: the red run proves the test sees the bug, the green run proves the fix, and the log on the PR makes both reviewable.
5. Why B best meets the objective: V2-D7.2 states the rule. A test that never failed proves nothing. Red before green is what earns trust.
6. Every rejected choice explained: A is the green-trust trap. The suite passes. The test asserts nothing. The bug is still present. C is the count fallacy. Two hundred empty assertions are two hundred zeros. D is the double-zero. Running an empty suite twice proves nothing twice.
7. Exact limitation or tradeoff: reproducing first costs the agent an extra loop, and some bugs resist clean reproduction. The reproduction is still the price of trust.
8. Relevant evidence (with date): the red-before-green rule from lesson-D7-2 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the suite already carries red-before-green history on record. Then the trust is earned, not assumed. C wins never as proof. D wins never.
10. Misconception tested: a green suite is a good suite. Greenness without a failing-first proof is unproven. Demand the red.

## Q-D7-12 (V2-D7.2)

**Scenario.** A team merges 30 agent PRs per month and reverts 9. Each revert costs 4 hours at $150 per hour: $5,400 per month. The revert rate keeps climbing.

**Question.** Which change fits?

**Options.**
A) A bigger model that writes more lines per PR.
B) Evidence gates on the merge: tests run on every edit via hook, run logs required on the PR, claims checked against execution, secrets scanned.
C) A dashboard that counts tokens per developer.
D) Merge faster to clear the queue.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: revert-rate intervention.
2. Lifecycle stage: operation.
3. Objective: reverts fall because claims are proven before merge.
4. Hard constraints: 9 reverts per month at $600 each, the cause is unverified claims, the fix must gate the merge.
5. System layer: workflow gates.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A increases the volume that caused the reverts. D accelerates the failure.
8. Compare on objective: B gates the merge on evidence. C measures adoption, not completion.
9. Hidden dependencies: the hook must run the real suite, and reviewers must actually read the logs.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "merges 30 agent PRs per month and reverts 9" at "$5,400 per month."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Gates the merge | No | Yes | No | No |
| Checks claims against execution | No | Yes | No | No |
| Addresses the cause | No | Yes | No | No |

4. Why B satisfies all hard constraints: the hook runs the suite on every edit, the log requirement makes the run reviewable, and the claim check plus secret scan close the two failure modes.
5. Why B best meets the objective: V2-D7.2 prices the alternative. After gates, 30 PRs and 1 revert cost $600 per month. Savings: $4,800 per month. Evidence is cheaper than reverts.
6. Every rejected choice explained: A is the volume trap. More lines per PR with no evidence is more reverts per month. C is the adoption dashboard. It shows who uses the tools. It says nothing about whether the PRs survive. D is the speed trap. Faster merges of unproven claims clear the queue into the revert pile.
7. Exact limitation or tradeoff: agents can game the gate with tests that assert nothing, so the red-before-green proof stays mandatory.
8. Relevant evidence (with date): the revert-pricing toy from lesson-D7-2 (§4), Oct 6, 2026. $5,400 before gates, $600 after. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when evals prove the bigger model clears the quality bar the reverts measure. Then it is a quality fix, not a volume fix. C wins never as the intervention. D wins never.
10. Misconception tested: the fix for bad agent output is a better model. The fix is a gate on the merge. Gate the merge, not the model.

## Q-D7-13 (V2-D7.2)

**Scenario.** An agent's edits twice committed API keys to the repo. The keys were found during a later audit, months after the commits.

**Question.** Which control fits?

**Options.**
A) Scan for key patterns after the merge.
B) A pre-commit hook that scans the diff for key patterns and blocks the commit on a hit, failing closed.
C) A CLAUDE.md reminder to be careful with keys.
D) A manual grep for keys each quarter.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: secret-spill prevention.
2. Lifecycle stage: implementation.
3. Objective: no key reaches the repo history.
4. Hard constraints: two spills already happened, the check must run before the commit lands, a hit must block.
5. System layer: workflow hooks.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A finds the leak after it ships. C is guidance against a spill fault. D samples quarterly.
8. Compare on objective: B is the only option that blocks the commit before the key lands in history.
9. Hidden dependencies: the pattern list must cover the key formats in use, and the hook must fail closed on scanner errors.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "twice committed API keys to the repo" and "found during a later audit, months after the commits."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Blocks before history | No | Yes | No | No |
| Fails closed on a hit | n/a | Yes | No | No |
| Catches the known formats | Partial | Yes | No | Partial |

4. Why B satisfies all hard constraints: the hook sees the diff before the commit, a hit blocks the landing, and fail-closed means a broken scanner blocks rather than waves through.
5. Why B best meets the objective: V2-D7.2 requires secrets protected in the workflow, with the scan before commit failing closed. B is that control.
6. Every rejected choice explained: A is the after-the-fact scan. The key sits in history for months before the audit finds it. C is the reminder trap. Carefulness is not a gate. Two spills prove it. D is the quarterly glance. The key ships on day one and is found on day ninety.
7. Exact limitation or tradeoff: secret scanning misses novel key formats, so the pattern list needs ownership and the team still needs rotation on spill.
8. Relevant evidence (with date): the pre-commit scan rule from lesson-D7-2 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins as the backstop sweep alongside B, never alone. C wins never as the control. D wins never as the control. It wins as the periodic hygiene check beside the hook.
10. Misconception tested: finding leaked keys is the control. Blocking the commit is the control. Detection after the merge is forensics.

## Q-D7-14 (V2-D7.2)

**Scenario.** An agent explores a new repo and summarizes its architecture. No test suite can verify a summary. The developer must decide whether to trust it.

**Question.** Which evidence fits the claim?

**Options.**
A) No evidence. Exploration cannot be checked.
B) Cited file paths for every claim plus executed examples where behavior is described.
C) A longer summary.
D) The agent's confidence statement.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: evidence selection for unverifiable-by-test work.
2. Lifecycle stage: implementation.
3. Objective: the summary's claims are checkable by the developer.
4. Hard constraints: no suite exists, each claim needs a pointer, behavior claims need a run.
5. System layer: evidence adaptation.
6. Eliminate infeasible: all four are producible.
7. Eliminate constraint-violating: A surrenders checkability. C lengthens the unchecked text. D is a phrase.
8. Compare on objective: B gives the developer the pointers and runs to verify each claim.
9. Hidden dependencies: the cited paths must be the files actually read, and the examples must run in the real repo.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "No test suite can verify a summary."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Claims are checkable | No | Yes | No | No |
| Behavior claims are run | No | Yes | No | No |
| Fits work with no tests | n/a | Yes | No | No |

4. Why B satisfies all hard constraints: the file paths let the developer open each source, and the executed examples prove the behavior claims.
5. Why B best meets the objective: V2-D7.2 adapts the evidence to the work. Docs and exploration need different evidence: cited files, executed examples.
6. Every rejected choice explained: A is the surrender. "Cannot be checked" becomes "need not be checked." C is the length fallacy. A longer unchecked summary is a longer risk. D is the confidence trap. A phrase is not a pointer.
7. Exact limitation or tradeoff: citations take agent effort per claim, and examples can rot as the repo changes. The evidence is still cheaper than a wrong architecture map.
8. Relevant evidence (with date): the no-tests evidence rule from lesson-D7-2 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never. C wins never as evidence. D wins never.
10. Misconception tested: no tests means no evidence. It means different evidence. Cite the files. Run the examples.

## Q-D7-15 (V2-D7.2), Select TWO

**Scenario.** A team debates how to measure agent productivity across its developers.

**Question.** Which TWO measures are valid? Select TWO.

**Options.**
A) The revert rate on agent PRs after evidence gates.
B) Lines of code generated per week.
C) Tokens consumed per developer.
D) The share of PRs that carry run logs with inspected results.
E) Hours the agent process ran.

**Answer.** A, D

**Method walk (Steps 1-10).**
1. Question type: productivity-metric selection.
2. Lifecycle stage: operation.
3. Objective: measure completed, surviving work, not activity.
4. Hard constraints: the measure must reflect outcomes, volume metrics are documented traps.
5. System layer: productivity measurement.
6. Eliminate infeasible: all five are computable.
7. Eliminate constraint-violating: B, C, and E measure activity. Activity without evidence is reverts.
8. Compare on objective: A measures survival. D measures evidence discipline. The rest measure motion.
9. Hidden dependencies: the revert rate needs the revert cause labeled, or it mixes agent faults with human ones.
10. Verify: A and D together. No third option measures outcomes.

**Explanation.**
1. Correct answer: A, D.
2. Decisive scenario phrase: "how to measure agent productivity."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Measures outcomes | Yes | No | No | Yes | No |
| Rewards evidence | Partial | No | No | Yes | No |
| Not gameable by volume | Yes | No | No | Yes | No |

4. Why A and D satisfy all hard constraints: the revert rate shows whether merged work survives, and the log share shows whether the evidence discipline holds.
5. Why A and D best meet the objective: V2-D7.2 measures completion, not volume. Productivity means work that survives, with evidence, not activity.
6. Every rejected choice explained: B is the documented trap. It rewards volume, and volume without evidence is reverts. C is the adoption metric. Tokens per developer show spend, not shipped work. E is the runtime metric. Hours running measure patience, not productivity.
7. Exact limitation or tradeoff: revert rates lag, and log share can be gamed with empty logs. The red-before-green proof stays mandatory.
8. Relevant evidence (with date): the volume-metric rejection from lesson-D7-2 (§8), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: B wins never as the productivity measure. C wins as the cost-attribution metric, never as productivity. E wins never.
10. Misconception tested: activity equals productivity. It does not. Lines, tokens, and hours are motion. Reverts and evidence are the measure.

## Q-D7-16 (V2-D7.2)

**Scenario.** An agent fixes a typo in a code comment. A revert takes ten seconds. The evidence-gate pipeline takes twenty minutes.

**Question.** Which action fits?

**Options.**
A) Run the full evidence-gate pipeline.
B) Merge on prose. The gate costs more than the revert.
C) Skip the fix. It is only a comment.
D) Hold a review meeting.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: gate-proportionality decision.
2. Lifecycle stage: implementation.
3. Objective: the cheapest correct path for a trivial change.
4. Hard constraints: ten-second revert, twenty-minute gate, zero blast radius.
5. System layer: workflow pragmatics.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A spends twenty minutes to protect ten seconds. D spends more.
8. Compare on objective: B matches the control cost to the failure cost.
9. Hidden dependencies: the change must truly be trivial. A "typo" that touches logic is not this case.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "A revert takes ten seconds. The evidence-gate pipeline takes twenty minutes."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Control cost fits failure cost | No | Yes | Yes | No |
| Change still ships | Yes | Yes | No | Yes |
| No process theater | No | Yes | n/a | No |

4. Why B satisfies all hard constraints: the ten-second revert bounds the failure, and skipping the twenty-minute gate saves the larger cost.
5. Why B best meets the objective: V2-D7.2 scales evidence to the change. Evidence gates win nothing where the gate costs more than the revert.
6. Every rejected choice explained: A is the gate absolutism the lesson warns against. Twenty minutes to protect ten seconds is waste. C is the skip. The typo stays because the process is heavy. Fix the process weight, not the typo. D is the meeting for a comment. The review costs more than the gate it replaces.
7. Exact limitation or tradeoff: "trivial" must be judged honestly. A mislabeled trivial change skips the gate it needed.
8. Relevant evidence (with date): the trivial-change counterfactual from lesson-D7-2 (§11), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins for any change with a non-trivial blast radius, where the gate is the cheaper path. C wins never. A correct trivial fix still ships. D wins never for a comment.
10. Misconception tested: gates apply uniformly. They apply proportionately. Match the control to the failure cost.

## Q-D7-17 (V2-D7.2), Select TWO

**Scenario.** An agent maps an unfamiliar repo and claims the payment flow has no retry logic.

**Question.** Which TWO evidence items support the claim? Select TWO.

**Options.**
A) Cited file paths for the payment flow files it read.
B) Executed examples showing the flow's behavior without retries.
C) The agent's statement that it is confident.
D) The number of files it opened.
E) A screenshot of the prompt.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: exploration-evidence selection.
2. Lifecycle stage: implementation.
3. Objective: the "no retry logic" claim is checkable.
4. Hard constraints: the claim is a negative, the files must be cited, the behavior must be shown.
5. System layer: evidence for exploration work.
6. Eliminate infeasible: all five are producible.
7. Eliminate constraint-violating: C is a phrase. D counts activity. E shows the ask.
8. Compare on objective: A lets the developer verify the sources. B demonstrates the behavior.
9. Hidden dependencies: the file set must be complete for the negative claim, or the retry hides in an uncited file.
10. Verify: A and B together. No third item evidences the claim.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "claims the payment flow has no retry logic."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Sources checkable | Yes | Partial | No | No | No |
| Behavior demonstrated | No | Yes | No | No | No |
| Supports a negative claim | Partial | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: the cited paths let the developer confirm the file set, and the executed examples show the flow running without retries.
5. Why A and B best meet the objective: V2-D7.2 requires cited files and executed examples for exploration claims. A negative claim needs both.
6. Every rejected choice explained: C is the confidence trap. A phrase is not a pointer. D is the activity count. Files opened measure effort, not findings. E is the prompt screenshot. It shows the ask, not the answer.
7. Exact limitation or tradeoff: a negative claim is only as complete as the file set. One uncited file can hide the retry.
8. Relevant evidence (with date): the exploration-evidence rule from lesson-D7-2 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins never as evidence. D wins never. E wins never.
10. Misconception tested: the agent's thoroughness is evidence. It is not. Cited sources and executed runs are the evidence.

## Q-D7-18 (V2-D7.3)

**Scenario.** A triage agent's p95 latency rises from 3 seconds to 14 seconds in one week. The runbook orders checks: context size, then dependency latency, then cache hit rate. The trace shows average context grew from 12,000 to 90,000 tokens after a prompt change added full ticket histories.

**Question.** What is the best FIRST action?

**Options.**
A) Upgrade to a larger model.
B) Trim the context: the first check matched, so fix it before running check two.
C) Add more logging to the agent.
D) Add a human reviewer on every task.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: incident first action from the runbook map.
2. Lifecycle stage: operation, incident response.
3. Objective: restore latency by fixing the matched suspect.
4. Hard constraints: the runbook orders the checks, check one matched, the fix must precede check two.
5. System layer: operational debugging.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A upgrades an innocent model. C adds noise. D cuts throughput.
8. Compare on objective: B follows the map. The first check matched, so the fix lands there.
9. Hidden dependencies: the trim must keep the tickets the task needs, and the runbook gains an alert line for context size.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "average context grew from 12,000 to 90,000 tokens after a prompt change."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Follows the runbook order | No | Yes | No | No |
| Fixes the matched suspect | No | Yes | No | No |
| Addresses the root cause | No | Yes | No | No |

4. Why B satisfies all hard constraints: the map says context first, the trace confirms the growth, and the trim restores the 12,000-token baseline.
5. Why B best meets the objective: V2-D7.3 maps latency to context, then dependencies, then cache. Check the context before the model.
6. Every rejected choice explained: A is the fashionable proxy. The model is innocent. Cost rises, latency stays. C is the noise option. More logs never shortened a context window. D is the throughput cut. Reviewers slow tasks. They do not shrink tokens. Three proxy fixes. Zero root causes.
7. Exact limitation or tradeoff: trimming can drop tickets a later step needs. The trim keeps the last 5, and the runbook gains the alert at 30,000 tokens.
8. Relevant evidence (with date): the latency map and the trim fix from lesson-D7-3 (§5), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when evals prove the model misses a signed latency-adjacent quality bar. Then it is a quality fix. C wins never as the fix. It wins as the detection baseline. D wins never for latency.
10. Misconception tested: latency means the model is slow. The map says context first. The trace agreed. Fix the context.

## Q-D7-19 (V2-D7.3)

**Scenario.** An agent's tool calls fail at 10% per day. Nothing in the code changed. The team debates the first check.

**Question.** Which order fits the map?

**Options.**
A) Rewrite the tool with a larger model.
B) Check credentials and token expiry, then permissions, then throttling, then the tool contract.
C) Add more retries with no backoff.
D) Increase the timeout to ten minutes.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: tool-failure investigation order.
2. Lifecycle stage: operation.
3. Objective: find the external cause in map order.
4. Hard constraints: nothing changed in code, so the cause is external. Credentials, permissions, throttling, and contract are the ordered suspects.
5. System layer: operational debugging.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A rebuilds an innocent tool. C amplifies a throttled dependency. D waits longer on a credentials fault.
8. Compare on objective: B is the map's order for tool failures.
9. Hidden dependencies: each check needs its own signal. Token expiry needs the auth logs, throttling needs the provider headers.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "fail at 10% per day. Nothing in the code changed."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Checks external causes first | No | Yes | No | No |
| Follows the map order | No | Yes | No | No |
| Cannot amplify the fault | Yes | Yes | No | Yes |

4. Why B satisfies all hard constraints: "nothing changed in code" points outside the code, and the map orders the outside suspects: credentials, permissions, throttling, contract.
5. Why B best meets the objective: V2-D7.3 maps tool failures to credentials, then permissions, then throttling, then the contract. The order is the procedure.
6. Every rejected choice explained: A is the rebuild reflex. The tool did not change. Rewriting it fixes nothing. C is the documented trap. Retries without backoff amplify a throttled dependency and hide the cause. The map beats the mask. D is the wait-longer option. A ten-minute timeout on an expired token fails slowly.
7. Exact limitation or tradeoff: ordered checks can be slow when two causes combine. The map still beats hunting by fashion.
8. Relevant evidence (with date): the tool-failure map from lesson-D7-3 (§§4, 9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the contract changed and the tool must be rewritten to it, decided after the map clears the earlier suspects. C wins never without backoff. With backoff it is a valid retry policy, not the diagnosis. D wins when the cause is proven to be slow responses, not failures.
10. Misconception tested: failing tools need better tools. They need the map. Nothing changed in code means the cause is outside the code.

## Q-D7-20 (V2-D7.3)

**Scenario.** The agent's monthly bill triples. Quality and latency are unchanged. The runbook orders cost checks: routing, then context, then caching.

**Question.** What is the best FIRST check?

**Options.**
A) Drop the grounding check to halve the per-call cost.
B) Check the routing: confirm cheap work still rides cheap models before touching context or cache.
C) Delete old logs to save money.
D) Switch every call to the smallest model.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: cost-spike investigation order.
2. Lifecycle stage: operation.
3. Objective: find the cost cause in map order without breaking the quality floor.
4. Hard constraints: the bill tripled, quality is unchanged and must stay so, the safety floor is not negotiable for savings.
5. System layer: operational debugging.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A cuts the control that holds the quality floor. D changes quality blindly.
8. Compare on objective: B is the map's first check for cost.
9. Hidden dependencies: the routing check needs per-task cost attribution, or the leak hides in the aggregate.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "monthly bill triples. Quality and latency are unchanged."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Follows the cost map | No | Yes | No | No |
| Holds the quality floor | No | Yes | Yes | No |
| Finds the cause before cutting | No | Yes | No | No |

4. Why B satisfies all hard constraints: routing is the map's first cost suspect, and the check finds the leak without touching any control.
5. Why B best meets the objective: V2-D7.3 maps cost rises to the route check, then context, then caching. Check the route before the model.
6. Every rejected choice explained: A is the floor violation. Dropping the grounding check halves the cost and breaks the precision the contract guarantees. Floors outrank speed. C is the penny hunt. Storage pennies against a tripled model bill. D is the blind downgrade. The quality floor was not consulted.
7. Exact limitation or tradeoff: routing fixes need the task-to-model mapping current, or the leak returns next month.
8. Relevant evidence (with date): the cost map from lesson-D7-3 (§9) and the floor-outranks-speed rule from Pair 25, Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never while the floor stands. It wins when the floor is re-signed lower with the stakeholder. C wins never as the cost fix. D wins when the map clears routing and context and evals prove the small model holds the floor.
10. Misconception tested: a tripled bill needs immediate cuts. It needs the map. Cut after the cause is named, never before, and never below the floor.

## Q-D7-21 (V2-D7.3)

**Scenario.** A RAG agent's answer quality drops 8 points in a week. No prompt changed. The corpus team shipped a reindex last week.

**Question.** Which investigation fits the map?

**Options.**
A) Retrain the model on new data.
B) Check the retrieval layer first: the reindex is the prime suspect, then the prompt, then the model.
C) Upgrade to the most capable tier.
D) Add more few-shot examples to the prompt.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: quality-drop investigation order.
2. Lifecycle stage: operation.
3. Objective: find the quality cause in map order.
4. Hard constraints: the prompt did not change, the reindex is the known change, the map orders the suspects.
5. System layer: operational debugging.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A treats a retrieval shift as a model fault. C is the fashionable proxy. D tunes the prompt before the map clears retrieval.
8. Compare on objective: B starts where the change happened.
9. Hidden dependencies: the retrieval check needs the pre- and post-reindex eval split to confirm the suspect.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "No prompt changed. The corpus team shipped a reindex last week."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Starts at the known change | No | Yes | No | No |
| Follows the quality map | No | Yes | No | No |
| Avoids the proxy fix | No | Yes | No | No |

4. Why B satisfies all hard constraints: the reindex is the week's only known change, and the map orders quality suspects as prompt, model, and retrieval drift, with the change pointing at retrieval first.
5. Why B best meets the objective: V2-D7.3 maps quality drops to prompt, model, and retrieval drift. The team checks the changed layer first.
6. Every rejected choice explained: A is the retrain reflex. Retraining on a retrieval problem burns a quarter and fixes nothing. C is the tier-upgrade proxy. A bigger model over a broken index is a bigger bill over a broken index. D is the prompt tune. The prompt did not change. Tuning it is motion.
7. Exact limitation or tradeoff: the reindex may be innocent, and then the map continues to the prompt and the model. The order still starts at retrieval.
8. Relevant evidence (with date): the quality map from lesson-D7-3 (§9) and the reindex transfer case from lesson-D7-3 (§13), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when the map clears retrieval and the prompt and evals prove model drift. Then retraining is the fix. C wins never as the diagnosis. D wins when the prompt is the proven suspect after retrieval is cleared.
10. Misconception tested: quality drops mean the model degraded. The map says check what changed. The reindex changed. Start there.

## Q-D7-22 (V2-D7.3), Select TWO

**Scenario.** An agent's 40-step run vanishes midway: no output, no error, no resume point. The team must recover the work, not restart it.

**Question.** Which TWO artifacts make recovery possible? Select TWO.

**Options.**
A) The plan checkpoint written at each handoff.
B) The run trace showing completed tool calls and their outputs.
C) The model's apology message.
D) A fresh run from step one.
E) A larger context window.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: lost-work recovery.
2. Lifecycle stage: operation, incident response.
3. Objective: resume the run from its last good state.
4. Hard constraints: no resume point exists in the run itself, the work must not run twice, the state must come from artifacts.
5. System layer: orchestration state.
6. Eliminate infeasible: all five exist or are producible.
7. Eliminate constraint-violating: C explains nothing. E adds capacity, not state.
8. Compare on objective: A gives the resume point. B gives the completed work. D restarts instead of resuming.
9. Hidden dependencies: the checkpoint must capture the plan state, and the trace must be end-to-end reconstructable.
10. Verify: A and B together. No third artifact holds the lost state.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "no output, no error, no resume point" and "recover the work, not restart it."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Holds the last good state | Yes | Partial | No | No | No |
| Shows completed work | No | Yes | No | No | No |
| Enables resume, not restart | Yes | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: the checkpoint is the resume point the run lacked, and the trace shows which steps already completed with their outputs.
5. Why A and B best meet the objective: V2-D7.3 maps lost agent work to orchestration state and traces. Resume from the checkpoint. The trace is the state.
6. Every rejected choice explained: C is the apology. It explains nothing and recovers nothing. D is the restart. The 40 steps run twice, and the side effects may double. E is the capacity trap. A larger window holds no record of the lost run.
7. Exact limitation or tradeoff: checkpoints add per-handoff cost, and traces need retention. Both are the price of resumability.
8. Relevant evidence (with date): the lost-work map entry from lesson-D7-3 (§9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins never. D wins when the run is idempotent and cheap, and no checkpoint exists. Then restart is rational. E wins never as the recovery.
10. Misconception tested: a lost run must be rerun. It must be resumed. The checkpoint and the trace are what make resume possible.

## Q-D7-23 (V2-D7.3), Select TWO

**Scenario.** The team writes the on-call runbook for the triage agent.

**Question.** Which TWO belong in the runbook? Select TWO.

**Options.**
A) The ordered symptom-to-suspect checks from the map.
B) The named owner and the escalation path.
C) "Try upgrading the model first."
D) A blank page titled "vibes."
E) Only the vendor's status page URL.

**Answer.** A, B

**Method walk (Steps 1-10).**
1. Question type: runbook-content selection.
2. Lifecycle stage: operation.
3. Objective: the on-call engineer resolves the incident without the original architect.
4. Hard constraints: the checks must be ordered, the owner must be named, the escalation must exist.
5. System layer: operational readiness.
6. Eliminate infeasible: all five are writable.
7. Eliminate constraint-violating: C is the fashion hunt. D is not a procedure. E covers one external suspect.
8. Compare on objective: A is the map. B is the accountability. The rest are not a runbook.
9. Hidden dependencies: the map must be updated after every incident, or it rots.
10. Verify: A and B together. No third option belongs in a runbook.

**Explanation.**
1. Correct answer: A, B.
2. Decisive scenario phrase: "the on-call runbook for the triage agent."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D | E |
|---|---|---|---|---|---|
| Ordered procedure | Yes | Partial | No | No | No |
| Owner named | No | Yes | No | No | No |
| Ends hero dependence | Yes | Yes | No | No | No |

4. Why A and B satisfy all hard constraints: the ordered checks turn the hunt into a procedure, and the named owner with the escalation path ends the 3 a.m. guess about who to call.
5. Why A and B best meet the objective: V2-D7.3 requires runbooks with the symptom map, an owner, and an escalation path. The team, not the hero, owns the system.
6. Every rejected choice explained: C is the hunt by fashion the runbook exists to end. "Upgrade first" is the proxy-fix list. D is the blank page. Vibes page no one at 3 a.m. E is the single-URL runbook. The vendor's status page covers one suspect and names no owner.
7. Exact limitation or tradeoff: maps go stale and runbooks rot like ADRs. The incident review is the runbook's maintenance contract.
8. Relevant evidence (with date): the runbook requirements from lesson-D7-3 (§§4, 9), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: C wins never as the first line. It wins as a last resort after the map is exhausted, decided explicitly. D wins never. E wins as one appendix line, never as the runbook.
10. Misconception tested: a runbook is a document. It is a procedure with an owner. The document without the owner is a wiki page.

## Q-D7-24 (V2-D7.3)

**Scenario.** The triage agent fails in a way the team never saw before: outputs loop on a new input shape. The runbook has no matching entry. The on-call engineer must act now.

**Question.** What is the best action?

**Options.**
A) Follow the closest runbook entry even though it does not match.
B) Page the architect to investigate, then update the runbook with the new entry in the post-incident review.
C) Ignore the failure. It is new, so no procedure covers it.
D) Reboot the agent every hour.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: novel-failure response.
2. Lifecycle stage: operation, incident response.
3. Objective: resolve the new failure and teach the runbook about it.
4. Hard constraints: no map entry matches, a human detective is needed, the runbook must learn.
5. System layer: incident escalation.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A follows a non-matching checklist off a cliff. C ignores a live failure. D treats the symptom hourly.
8. Compare on objective: B brings the detective now and the procedure later.
9. Hidden dependencies: the architect must be reachable, and the post-incident review must actually update the runbook.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "fails in a way the team never saw before" and "The runbook has no matching entry."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Matches the novelty | No | Yes | No | No |
| Resolves now | Partial | Yes | No | Partial |
| Runbook learns | No | Yes | No | No |

4. Why B satisfies all hard constraints: the architect is the human detective the novel failure needs, and the post-incident update gives the runbook its new entry.
5. Why B best meets the objective: V2-D7.3 is explicit. The first incident of a new kind still needs a human detective. Then every incident edits the map.
6. Every rejected choice explained: A is the cliff walk. A non-matching checklist applied anyway misleads with confidence. C is the shrug. New failures still page. D is the hourly reboot. It masks the loop and teaches nothing.
7. Exact limitation or tradeoff: paging the architect reintroduces hero dependence for one incident. The runbook update is what ends it.
8. Relevant evidence (with date): the novel-failure rule from lesson-D7-3 (§11), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins when an entry partially matches and the engineer adapts it explicitly, noting the gap. C wins never. D wins as a stopgap while the detective works, never as the response.
10. Misconception tested: the runbook covers everything. It covers the known. The novel failure needs the detective, then the runbook grows.

## Q-D7-25 (V2-D7.3)

**Scenario.** The team added a new payment dependency last month. The runbook still lists the old suspects. Last night's on-call followed the runbook and missed the new dependency for two hours.

**Question.** What is the best fix?

**Options.**
A) Freeze the runbook so it stays stable.
B) Update the runbook after every incident, with the incident review as its maintenance contract.
C) Delete the runbook. It misled the on-call.
D) Trust senior memory instead of the runbook.

**Answer.** B

**Method walk (Steps 1-10).**
1. Question type: runbook-maintenance fix.
2. Lifecycle stage: operation.
3. Objective: the runbook tracks the system it describes.
4. Hard constraints: the system changed, the runbook did not, the on-call followed it off the map.
5. System layer: operational documentation.
6. Eliminate infeasible: all four are executable.
7. Eliminate constraint-violating: A freezes the rot in place. C deletes the procedure. D replaces the procedure with memory.
8. Compare on objective: B makes every incident maintain the map.
9. Hidden dependencies: the incident review must be a real meeting with the runbook edit as its output.
10. Verify: B alone. Single select.

**Explanation.**
1. Correct answer: B.
2. Decisive scenario phrase: "The runbook still lists the old suspects" and "missed the new dependency for two hours."
3. Requirement-to-option matrix:

| Requirement | A | B | C | D |
|---|---|---|---|---|
| Runbook tracks the system | No | Yes | n/a | No |
| Maintenance is owned | No | Yes | No | No |
| On-call protected next time | No | Yes | No | No |

4. Why B satisfies all hard constraints: the post-incident update adds the new suspect, and the review-as-contract makes the update recur.
5. Why B best meets the objective: V2-D7.3 states the rule. Runbooks rot like ADRs. The incident review is the runbook's maintenance contract.
6. Every rejected choice explained: A is the stability fallacy. A frozen runbook describing last month's system is confidently wrong. C is the deletion reflex. The runbook misled because it was stale, not because runbooks mislead. D is the memory bank. Senior memory leaves with the senior.
7. Exact limitation or tradeoff: the update discipline costs review time per incident, and rushed updates can add wrong entries. The review must be honest.
8. Relevant evidence (with date): the runbook-rot figure from lesson-D7-3 (§7), Oct 6, 2026. Exam scope via S03/S04, Sept 2026.
9. Counterfactual where each plausible alternative wins: A wins never as the fix. It wins as a version freeze with a dated successor, which is B with a label. C wins never. D wins never as the system. It wins as the detective for the novel failure, per Q-D7-24.
10. Misconception tested: the runbook is written once. It is written after every incident. The map is maintained, not made.

## Coverage: D7 questions to objectives

| Objective | Questions | Count |
|---|---|---|
| V2-D7.1 | Q-D7-01, Q-D7-02, Q-D7-03, Q-D7-04, Q-D7-05, Q-D7-06, Q-D7-07, Q-D7-08, Q-D7-09 | 9 |
| V2-D7.2 | Q-D7-10, Q-D7-11, Q-D7-12, Q-D7-13, Q-D7-14, Q-D7-15, Q-D7-16, Q-D7-17 | 8 |
| V2-D7.3 | Q-D7-18, Q-D7-19, Q-D7-20, Q-D7-21, Q-D7-22, Q-D7-23, Q-D7-24, Q-D7-25 | 8 |
| Total | | 25 |

Multi-response items: Q-D7-04, Q-D7-08, Q-D7-15, Q-D7-17, Q-D7-22, Q-D7-23 (6 of 25).
