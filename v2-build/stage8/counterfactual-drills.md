# Counterfactual drills: §18 comparisons

Fifty-two drills, two per §18 comparison pair. Each drill gives a base
scenario, one changed requirement, the flipped answer, and one paragraph
that explains why the flip happens. The flip is the lesson: one line of
scenario changes the winner. Baseline: Oct 6, 2026. Practice items only.

## Pair 1: workflow vs agent

### CF-01

**Scenario.** A customs broker files import declarations. 95% of shipments
match a fixed tariff table. A deterministic workflow parses the manifest,
looks up the tariff, and files. Winner: workflow.

**Change.** The broker takes on art imports. Each piece needs provenance
research across auction records with no fixed source list.

**Flipped answer.** Agent loop for the art lane. The workflow keeps the
95% standard lane.

**Why the answer changes.** The workflow wins when code can list the
steps in advance. Provenance research has no fixed source list, so no
code can list the steps. The model must plan sources at runtime. The
constraint that changed is step listability, and it is the exact gate
from Pair 1. The standard lane keeps its workflow because its steps stay
fixed.

### CF-02

**Scenario.** An agent loop investigates supplier fraud. Sources vary per
case. No fixed checklist exists. Winner: agent loop.

**Change.** The regulator publishes a fixed 12-point fraud checklist and
demands the identical evidence order on every case.

**Flipped answer.** Deterministic workflow.

**Why the answer changes.** The identical-order demand kills runtime
planning. A workflow executes the same 12 steps in the same order every
run and produces the identical trace the regulator wants. The agent's
strength (adaptive planning) becomes a liability: its plan varies per
run. The new hard constraint is trace uniformity, which only fixed steps
satisfy.

## Pair 2: single agent vs multi-agent

### CF-03

**Scenario.** One agent drafts a product launch brief: market scan, pricing
check, and channel plan, run in one loop in 40 seconds. Winner: single
agent.

**Change.** A 15-second SLA arrives. The three pieces touch different
tools and share no state.

**Flipped answer.** Coordinator with three parallel workers.

**Why the answer changes.** One loop runs the pieces in sequence and
cannot beat 40 seconds. Parallel workers run the max piece, not the sum,
and the merge costs a few seconds. The SLA is the binding constraint and
only parallelism meets it. Independence of the pieces (no shared state)
keeps the merge cheap, so the parallel gain survives the handoff cost.

### CF-04

**Scenario.** Three parallel workers review contracts: legal, finance,
technical. They merge cleanly in 20 seconds. Winner: multi-agent.

**Change.** The merge rule turns ambiguous. Workers disagree on 40% of
contracts and each disagreement needs partner arbitration.

**Flipped answer.** Single agent, sequential.

**Why the answer changes.** The parallel gain was 20 seconds. The
arbitration cost now exceeds it: 40% of cases pay partner hours. The
handoff contract requires a disagree rule, and this one has none that
works. A single loop holds one consistent judgment and never pays the
merge tax. The binding cost moved from wall-clock time to disagreement
cost.

## Pair 3: augmented LLM vs autonomous loop

### CF-05

**Scenario.** A warranty bot checks one photo of a damaged part against
the warranty terms. One judgment, one tool. Winner: augmented single call.

**Change.** The bot must now verify the part serial in the ERP, then look
up the supplier batch from that result, then check the batch recall list.

**Flipped answer.** Autonomous loop with a step cap.

**Why the answer changes.** The augmented call makes one judgment with
tool results in context. The new task is data-dependent: step two needs
step one's result, and no code can precompute the chain. The loop
iterates call, act, observe until the recall check completes. The
constraint that changed is step dependence, which is the exact gate the
augmented call cannot cross.

### CF-06

**Scenario.** A research loop hunts supplier risk across news, filings, and
sanctions lists. Sources are unknown per case. Winner: autonomous loop.

**Change.** The task narrows to one known sanctions list with a fixed
schema. The question is always "is this name on the list."

**Flipped answer.** Augmented single call.

**Why the answer changes.** The loop's value was dynamic source planning.
One fixed list needs one lookup plus one judgment. Extra iterations burn
cost and add drift risk with no planning to do. A one-judgment task fits
the augmented call exactly. The plan became listable, so the loop's
machinery is pure overhead.

## Pair 4: sequential vs parallel execution

### CF-07

**Scenario.** Three analysts review a vendor: security, finance, legal.
Sequential, 48 seconds total, no SLA. Winner: sequential.

**Change.** The sales team needs the verdict in 25 seconds for live deal
calls.

**Flipped answer.** Parallel with a merge step.

**Why the answer changes.** Sequential costs the sum (48 s). Parallel
costs the max piece plus merge (about 24 s). The 25-second SLA binds and
only the max-piece math meets it. The pieces are independent reviews of
the same vendor file, so the merge is a simple combine. Time was not a
constraint before. Now it is the only one that matters.

### CF-08

**Scenario.** Three workers draft sections of one incident report in
parallel and merge. Winner: parallel.

**Change.** The sections must now be written into one shared live
document, and two workers keep overwriting each other's paragraphs.

**Flipped answer.** Sequential.

**Why the answer changes.** Parallelism demands independent pieces. A
shared live document is shared mutable state: the independence gate
fails. The overwrites are a race, not a merge. Sequential passes the
document forward, and each writer sees the previous sections. The state
shape changed, so the execution shape must follow.

## Pair 5: MCP vs direct API vs CLI

### CF-09

**Scenario.** One Python service calls one internal pricing API. Winner:
direct API.

**Change.** Four more teams in three languages need the same pricing
capability.

**Flipped answer.** MCP server.

**Why the answer changes.** Direct API wins on one consumer and one
language: no protocol tax. Five consumers in three languages flip the
math: one MCP server with declared tools serves all of them, while
direct API means five bespoke integrations. Reuse crossed the threshold
where the protocol tax pays for itself. The constraint that changed is
consumer count, the exact V2-D3.7 axis.

### CF-10

**Scenario.** A vendor capability is used through a CLI wrapper. The CLI
output format changes quarterly and breaks the parser. Winner: CLI (only
option available).

**Change.** The vendor ships a stable typed API with versioned schemas.

**Flipped answer.** Direct API.

**Why the answer changes.** The CLI won by default: the capability
existed nowhere else. A stable typed API removes the parse risk and the
contract becomes typed. The subprocess babysitting and the quarterly
parser incidents disappear. The constraint that changed is capability
availability, and the typed contract dominates text parsing on every
axis.

## Pair 6: shared tools vs independent agents

### CF-11

**Scenario.** One support assistant uses 8 tools under one owner. Winner:
shared tools.

**Change.** The catalog grows to 40 tools with overlapping descriptions.
Wrong-tool picks triple.

**Flipped answer.** Split into independent agents (or progressive
discovery).

**Why the answer changes.** One loop with a flat 40-tool list collapses
pick accuracy: overlapping descriptions confuse the model and every
schema burns context tokens per call. Independent agents fence a small
tool set per loop, so each decision sees a clean namespace. The binding
cost moved from coordination (zero before) to pick accuracy. Past the
bloat threshold, the flat list is the failure.

### CF-12

**Scenario.** Two agents own billing and support with clean contracts.
Winner: independent agents.

**Change.** Every ticket now needs both agents to agree before any reply
ships.

**Flipped answer.** One agent with shared tools.

**Why the answer changes.** Independent agents win when tasks have
different owners and clean handoffs. Agreement on every case makes
coordination the whole job: contracts, merge, and conflict rules run on
100% of tickets. One loop with both tool sets never pays the handoff
tax. The handoff frequency changed from occasional to every case, and
coordination cost now exceeds specialization gain.

## Pair 7: prompt caching vs response caching

### CF-13

**Scenario.** 10,000 calls per day share an 8,000-token system prompt.
Questions vary. Winner: prompt caching.

**Change.** Traffic shifts: the same five FAQ prompts now make up all
10,000 calls.

**Flipped answer.** Response caching.

**Why the answer changes.** Prompt caching reuses the prefix while the
model still runs per call. Exact-duplicate prompts let the system serve a
stored answer at near-zero cost on hits. The variable that changed is
prompt duplication: varied questions keep the model running, identical
questions make the run redundant. At 80%+ exact hits, the stored answer
wins on cost with no quality change, provided answers stay valid.

### CF-14

**Scenario.** A FAQ bot serves 95% of answers from a response cache.
Winner: response caching.

**Change.** Answers must now include each user's live account balance.

**Flipped answer.** Prompt caching plus a balance tool call.

**Why the answer changes.** A cached answer is per-prompt, not per-user.
The live balance differs per user, so the stored answer is wrong for
everyone except the user it was cached for. Serving it is a correctness
incident, not a saving. Prompt caching still cuts the stable prefix cost,
and the tool call fetches fresh state. The data freshness constraint
killed the whole-answer cache.

## Pair 8: progressive discovery vs monolithic context

### CF-15

**Scenario.** A travel agent uses 8 tools under a 2-second chat SLA.
Winner: monolithic context.

**Change.** The catalog grows to 60 tools with overlapping names. Wrong
picks spike.

**Flipped answer.** Progressive discovery.

**Why the answer changes.** Monolithic context loads every schema every
call. At 60 tools the token cost is heavy and the wrong-tool risk grows
with the visible choice set. Discovery shows names first and fetches the
chosen schema on demand, which shrinks both the token bill and the pick
surface. The latency cost of one discovery round trip is now smaller than
the accuracy cost of the flat list. Surface size crossed the threshold.

### CF-16

**Scenario.** 60 tools behind progressive discovery, each call uses two
tools. Winner: discovery.

**Change.** The task becomes a batch job where every call invokes all 60
tools.

**Flipped answer.** Monolithic context.

**Why the answer changes.** Discovery saves tokens by fetching only the
schemas the call needs. When the call needs all 60 schemas, the fetch
saves nothing and adds a round trip of pure latency. Monolithic loads
everything up front, which is exactly what the batch needs. The usage
pattern changed from sparse to dense, and the optimization must match
the pattern.

## Pair 9: RAG vs large-context prompting

### CF-17

**Scenario.** A contract assistant serves 12 standard contracts that never
change. Winner: large-context prompting.

**Change.** The library grows to 4,000 contracts with weekly updates.

**Flipped answer.** RAG pipeline.

**Why the answer changes.** Twelve fixed contracts fit the window at low
per-call cost with zero pipeline. Four thousand changing contracts
exceed any window and go stale weekly. RAG retrieves a few chunks per
query and re-ingests only changed documents. The variables that changed
are corpus size and update cadence, the two axes where large context
fails and retrieval wins.

### CF-18

**Scenario.** RAG over a changing policy library with citation checks.
Winner: RAG.

**Change.** The regulator drops the citation requirement and the library
freezes at 20 pages.

**Flipped answer.** Large-context prompting.

**Why the answer changes.** RAG earned its pipeline cost three ways:
unbounded corpus, changing facts, and per-chunk citations. The freeze
kills the first two and the dropped requirement kills the third. Twenty
static pages fit the window cheaply. The pipeline's stages (ingestion,
chunking, indexing, grounding checks) no longer buy anything, and each
stage is a failure point with no payoff.

## Pair 10: RAG vs customization (fine-tuning)

### CF-19

**Scenario.** Support answers over a weekly-changing policy library, with
citations. Winner: RAG.

**Change.** The task becomes classifying tickets into 40 fixed categories
with stable definitions. No citations needed.

**Flipped answer.** Fine-tuning.

**Why the answer changes.** The need changed from facts to behavior.
RAG retrieves documents, but classification needs a decision boundary,
not a paragraph. Fine-tuning bakes the category definitions into the
model and runs with no retrieval cost. Weekly retraining is unnecessary
because the categories are stable. The knowledge-vs-behavior axis is the
decisive one, and it flipped.

### CF-20

**Scenario.** A fine-tuned classifier tags tickets into stable
categories. Winner: fine-tuning.

**Change.** Categories gain new members weekly, and auditors demand the
source rule behind each decision.

**Flipped answer.** RAG over the rule documents.

**Why the answer changes.** Weekly category changes turn fine-tuning into
a retraining treadmill. Worse, weights cannot cite: no source rule can
be shown per decision. RAG retrieves the current rule text and grounds
each decision in a citable chunk. The audit requirement is the binding
constraint, and only retrieval produces evidence. The update cadence
alone would weaken fine-tuning. The citation demand kills it.

## Pair 11: retrieval failure vs model limitation

### CF-21

**Scenario.** A policy bot gives a wrong answer. The trace shows the
retrieved set lacks the relevant policy chunk. Diagnosis: retrieval
failure.

**Change.** The team fixes retrieval. The trace now shows the right chunk
present, and the answer is still wrong.

**Flipped answer.** Model limitation.

**Why the answer changes.** Diagnosis follows the evidence, not the
history. The chunk's absence named retrieval as the failing layer. Its
presence with a still-wrong answer moves the failure downstream: the
model had the facts and failed to use them. The fix moves from chunking
and indexing to the prompt, the model choice, or a verification gate.
Same symptom, different layer, because the trace moved.

### CF-22

**Scenario.** A model limitation is diagnosed: the chunk is present, the
model still fails. The team upgrades to a stronger model. Winner so far:
model fix.

**Change.** The stronger model gives the same wrong answer on the same
query class, and a fresh trace shows the chunk absent all along.

**Flipped answer.** Retrieval failure.

**Why the answer changes.** The upgrade was an experiment, and it failed:
same wrong answer on the same class. The fresh trace reveals the chunk
never arrived, so the stronger model never saw the facts either. The
first diagnosis trusted a stale trace. The new evidence names retrieval.
The expensive upgrade bought nothing because it fixed a proxy, not the
layer. The lesson is the V2-D4.4 habit: trace the retrieved set first.

## Pair 12: skills vs tools vs subagents

### CF-23

**Scenario.** One refund lookup action, called from one prompt. Winner:
tool.

**Change.** Five teams repeat the same 15-step refund procedure, each with
a pasted copy of the prompt. The copies drift.

**Flipped answer.** Skill.

**Why the answer changes.** One action needs no governance: a tool fits.
Five drifting copies of a 15-step procedure are a version-control
failure: fixes land in some copies and not others. A skill names,
versions, and reviews the procedure once, and all teams share it. The
variable that changed is reuse count across teams. Past one team, the
governed asset beats the copy.

### CF-24

**Scenario.** A skill runs a research procedure: search, read, summarize.
Winner: skill.

**Change.** The procedure now needs web search plus file writes, with
different permissions than the calling agent holds.

**Flipped answer.** Subagent with a scoped tool list.

**Why the answer changes.** A skill inherits the caller's permission
envelope. The new procedure needs a different envelope: search allowed,
writes fenced to one directory. Only a separate loop with its own tool
list can carry different permissions. The procedure outgrew the asset
class. The permission boundary is the gate between skill and subagent.

## Pair 13: instructions vs enforceable permissions

### CF-25

**Scenario.** A solo developer's scratch project. No secrets, no
destructive tools. CLAUDE.md carries style guidance. Winner: instructions.

**Change.** The repo gains production credentials and a deploy script.

**Flipped answer.** Enforceable permissions: deny rules on secret paths
and the deploy command.

**Why the answer changes.** Guidance shapes choices on a trusted team
with nothing to protect. Production credentials create a control need:
a secret read must be blocked, not discouraged. A deny rule runs before
the tool and logs the attempt. A CLAUDE.md note is a sign the model may
ignore under pressure. The threat model changed, so the mechanism must
change from guidance to enforcement.

### CF-26

**Scenario.** Deny rules block `Bash(sudo:*)` for the whole team. Winner:
enforceable permissions.

**Change.** The on-call workflow legitimately needs sudo for one restart
script, and engineers start bypassing the rule with personal overrides.

**Flipped answer.** Keep the rule, add an allow-listed exception for the
one script with audit logging.

**Why the answer changes.** The rule is still the right control: blanket
sudo stays denied. But a control the team routes around is theater with
extra steps. The narrow exception names the legitimate path and logs it,
so the workflow works inside the control instead of around it. The
principle holds (enforce in code), while the rule matches the real
workflow. This drill flips the shape of the answer, not the mechanism.

## Pair 14: authentication vs authorization

### CF-27

**Scenario.** A support bot filters tickets by the agent's region. The
design checks the agent's identity against the HR policy table in code.
Winner: proper authN plus authZ.

**Change.** A refactor reads the region from the agent's self-declared
chat profile instead of the HR table.

**Flipped answer.** The design now fails. Fix: restore the check against
the HR policy table.

**Why the answer changes.** The region moved from a verified identity
attribute to a user claim. A user saying "I am in EMEA" convinces the
model and convinces no lock. Authorization must decide on verified
identity, never on self-declaration. The code path looks the same. The
trust source changed. That one-line change converts a control into a
suggestion.

### CF-28

**Scenario.** A shared service credential fronts a read-only internal
dashboard. Winner: shared credential (attribution not needed).

**Change.** The dashboard gains a refund button. Money moves on click.

**Flipped answer.** Per-user authentication plus deterministic
authorization on the refund action.

**Why the answer changes.** Read-only access needed no attribution, so a
shared credential was proportionate. Money movement needs to know who
acted and whether they may act: per-user authN plus a code-enforced
authZ check. Side effects changed the verdict. The V2-D3.2 rule is
explicit: no shared credentials when attribution matters, deterministic
enforcement for side effects.

## Pair 15: approval vs audit logging

### CF-29

**Scenario.** An agent drafts refunds. All refunds stay reversible for 24
hours. Audit logging plus post-action sampled review. Winner: audit.

**Change.** Refunds become instant and irreversible at send.

**Flipped answer.** Pre-action approval by a human with full decision
context.

**Why the answer changes.** Reversibility was the gate. A reversible
refund can be undone, so after-the-fact review plus logs sufficed. An
irreversible refund cannot. The control must move before the action:
a human sees the exact amount, payee, and reason, then approves. Audit
logging stays as the record, but it is no longer the control. Timing
relative to irreversibility decides.

### CF-30

**Scenario.** Pre-action approval gates every database read. Volume hits
50,000 reads per day. Reviewers rubber-stamp. Winner so far: approval.

**Change.** Same volume, same rubber-stamping, one misuse ships.

**Flipped answer.** Sampled human review plus audit logging. Reserve
pre-action approval for writes.

**Why the answer changes.** The gate degraded into theater: reviewers
cannot meaningfully judge 50,000 reads a day, so the approval proves
nothing. Reads are low-stakes and reversible. The control cost exceeds
the risk. Sampled review plus complete audit logs give real detection at
a fraction of the reviewer load. The stakes, not the habit, set the
control. Approval stays where it belongs: on writes.

## Pair 16: removing capability vs monitoring capability

### CF-31

**Scenario.** An agent carries a delete tool it never uses. The proposal
is to log its calls. Winner so far: monitoring.

**Change.** A security review asks what task needs the delete tool. The
answer: none.

**Flipped answer.** Remove the tool from the config.

**Why the answer changes.** Monitoring watches a risk. Removal deletes
it. An unneeded delete tool is pure attack surface: prompt injection can
steer the model to a tool no task requires. The exam rule is blunt:
logging is not removal. The review's question (what task needs this)
is the V2-D3.1 bloat test, and the answer "none" ends the debate. The
config change costs one line.

### CF-32

**Scenario.** The delete tool was removed from the agent. Winner:
removal.

**Change.** The on-call workflow now needs the delete tool for incident
response, with a 10-minute SLA.

**Flipped answer.** Restore the tool with monitoring plus pre-action
approval gates.

**Why the answer changes.** Removal won while the tool was unneeded.
Need returned, so the capability must return. But it returns watched
and gated: monitoring for the audit trail, pre-action approval because
deletion is irreversible. The principle is stable (remove the unneeded,
gate the dangerous), and the tool moved from the first bucket to the
second. Necessity is the variable that flipped.

## Pair 17: schema validity vs factual correctness

### CF-33

**Scenario.** An invoice extractor outputs JSON. Schema validation runs in
code. Totals are unchecked. One invented total ships. Winner so far:
schema only.

**Change.** The postmortem names the invented total as the loss event.

**Flipped answer.** Add factual correctness checks: each total verified
against the source image in code.

**Why the answer changes.** Schema validation checks shape, not truth.
Valid JSON carried the lie in a pretty envelope. The loss event proves
the content layer was the failing one. A grounding check (parsed total
vs source image, compared in code) fails the run that schema validation
passed. Shape and truth are different layers, and the incident names
which one failed.

### CF-34

**Scenario.** Every claim in the output is fact-checked against a source.
The output schema is loose. Winner: factual checks.

**Change.** A downstream service starts parsing the output as JSON.

**Flipped answer.** Add schema validation in code.

**Why the answer changes.** Truth without shape was fine while a human
read the output. A parsing consumer needs a contract: fields present,
types right, enums legal. A true claim in broken JSON crashes the
consumer. The consumer changed the contract, so the check set must grow.
Both layers are now mandatory: schema for the machine, facts for the
business.

## Pair 18: citation presence vs citation support

### CF-35

**Scenario.** Policy answers carry citation markers. No support check
runs. A wrong answer cites a real page that says the opposite. Winner so
far: presence.

**Change.** The incident report names the decorative citation as the
trust failure.

**Flipped answer.** Citation support checks: the source must imply the
claim.

**Why the answer changes.** Presence is a format choice the model makes
fluently. It cannot fail. The incident proves the failure mode: a real
marker on a contradicting page manufactures false confidence, which is
worse than no citation. An entailment check per cited claim has teeth:
40 unsupported claims get blocked instead of shipped. The check must be
able to fail, or it is not a check.

### CF-36

**Scenario.** Support checks run on every cited claim. Costs are high.
Winner: full support checks.

**Change.** The answers become low-stakes internal drafts for one team.

**Flipped answer.** Citation presence plus sampled support checks.

**Why the answer changes.** Full entailment checks price per claim.
Low-stakes drafts do not carry the error cost that paid for them. The
stakes dropped, so the verification spend must drop with it: presence
keeps the format habit, sampled checks keep a detection signal. The
principle is proportional verification: check the claims that carry
error cost, not every adjective. Stakes set the budget.

## Pair 19: confidence vs calibrated risk

### CF-37

**Scenario.** A triage bot routes "low confidence" answers to humans. The
model marks 95% of answers high confidence. Errors persist. Winner so
far: confidence gating.

**Change.** The team builds a labeled set and measures: at the model's
"90% confident" line, actual accuracy is 61%.

**Flipped answer.** Calibrated risk thresholds from the labeled set.

**Why the answer changes.** The measurement exposes the gap: the model's
self-report is uncalibrated and overconfident. A gate built on it routes
by feeling. Calibrated risk ties the threshold to outcomes: when the
system says 90%, it is right 90% of the time. The review threshold now
rests on measurement, outside the model's reach and outside an
attacker's prompt. The labeled set is what made the flip possible.

### CF-38

**Scenario.** Calibrated risk gates review at a measured 90% precision
line. Winner: calibrated risk.

**Change.** The data drifts. Recalibration shows the 90% line now holds
71% precision. The team proposes dropping the gate.

**Flipped answer.** Keep the gate, recalibrate the threshold. Do not drop
it.

**Why the answer changes.** The mechanism is right. The measurement aged.
Drift moved the line, so the fix is a new measurement, not gate removal.
Dropping the gate returns to unmeasured risk, which is worse than a
stale number. The V2-D4.6 habit applies: detect drift, recalibrate on
fresh labels, keep the owner. This drill flips the proposed action, not
the principle.

## Pair 20: human review vs deterministic validation

### CF-39

**Scenario.** Humans review every refund payout. Volume is 200 per day.
Winner: human review.

**Change.** Volume grows to 20,000 payouts per day. Reviewers rubber-stamp
within a week.

**Flipped answer.** Deterministic rules for the checkable cases, sampled
human review for the rest.

**Why the answer changes.** Human review scales linearly with reviewer
hours. At 20,000 per day the gate becomes theater: the stamp lands but
the judgment left. Deterministic rules (amount caps, payee lists, fraud
patterns) run at near-zero marginal cost and never fatigue. Humans stay
where they add value: the sampled cases and the novel patterns rules
cannot name. Volume broke the human gate. Rules plus sampling replace
it.

### CF-40

**Scenario.** Deterministic rules validate all outputs. A novel fraud
pattern passes every rule for a month. Winner so far: rules.

**Change.** The fraud team characterizes the new pattern.

**Flipped answer.** Add human review on the flagged class, then encode
the pattern as a new rule.

**Why the answer changes.** Rules catch only the errors someone listed.
The novel pattern was unlisted, so it passed. Human judgment catches
what rules cannot name: the reviewer sees the new shape and flags it.
Once characterized, the pattern becomes a rule and the humans move on.
The pair is a loop, not a choice: rules first, humans on the gap, then
the gap becomes a rule. The incident names the missing step.

## Pair 21: offline evaluation vs A/B testing

### CF-41

**Scenario.** A new reranker passes the offline suite. The goal is rank
quality on the labeled set. Winner: ship after the offline gate.

**Change.** The product goal becomes revenue per session, not rank
quality.

**Flipped answer.** Add an A/B test on revenue per session.

**Why the answer changes.** The offline suite measures dataset scores.
Revenue per session is a business outcome that only real users produce.
Better ranks may or may not move revenue. The dataset cannot answer.
The A/B test exposes a controlled sample and measures the outcome that
matters. The goal changed from a model metric to a business metric, and
only the test measures the new one. The offline gate stays as the
pre-ship check.

### CF-42

**Scenario.** An A/B test is planned for a claimed 1% lift on 500
sessions per day. Winner so far: A/B test.

**Change.** The statistician computes the required sample: 60 days to
detect the 1% lift.

**Flipped answer.** Offline evaluation only. Skip the A/B test.

**Why the answer changes.** A test that cannot answer is theater. 500
sessions a day cannot resolve a 1% lift in any sane window. The test
would run 60 days and still wobble. The V2-D4.3 rule applies: no
traffic, no test. Offline evaluation on the five drawers still gates
quality. The sample-size math is the binding constraint, and it vetoes
the test.

## Pair 22: logging vs tracing vs compliance evidence

### CF-43

**Scenario.** A single model call per request. One log line per call.
Winner: logging.

**Change.** The design grows into an agent: retrieval, three tools, and
a queue between hops.

**Flipped answer.** Add tracing with one run id across all hops.

**Why the answer changes.** One hop needs one log line. Five hops need
the run id: per-hop events without it cannot reconstruct the run. The
2 a.m. question ("which hop failed") is unanswerable from scattered
logs. Tracing links the events end to end. The architecture changed
from one hop to many, and the observability must match the hop count.

### CF-44

**Scenario.** Full tracing on every run. A healthcare customer asks for
HIPAA evidence. Winner so far: tracing.

**Change.** The auditor asks: "Prove the access control works. Show me
the control, the owner, and the review cadence."

**Flipped answer.** Add the compliance evidence mapping: requirement to
control to owner to evidence to cadence.

**Why the answer changes.** Traces record what happened. The auditor
asks for proof that a control works, which is a different artifact: the
requirement named, the control described, the owner assigned, the
evidence attached, the cadence set. A trace is not a control mapping.
Each artifact serves its audience: traces serve the on-call engineer,
evidence serves the auditor. The new audience demands the new artifact.

## Pair 23: project defaults vs managed policies

### CF-45

**Scenario.** A team commits `.claude/settings.json` with deny rules on
secret paths. Winner: project defaults.

**Change.** The org mandates secret-path deny rules that no team may
weaken, after one team deleted theirs.

**Flipped answer.** Managed policies for the secret-path rules.

**Why the answer changes.** The committed file cannot protect against
its own editors: anyone with repo write access can weaken it. The org
mandate needs a layer nothing below overrides. Managed policies deploy
from the admin and hold across every repo. The control moved from team
workflow to org non-negotiable. Scope of authority is the gate between
the two mechanisms.

### CF-46

**Scenario.** An org-managed policy pins one model for all teams.
Winner: managed policies.

**Change.** One team needs a cheaper tier for a batch job. The policy
has no exception path. The team routes around it with personal configs.

**Flipped answer.** Add an exception process to the policy. Keep the
pin as the default.

**Why the answer changes.** The pin is still right as the default: it
holds spend and quality floors org-wide. But a policy with no exception
path creates shadow workflows, which are worse than exceptions: they
are invisible. The exception process names the legitimate path (batch
job, cheaper tier, spend owner) and keeps it visible. Enforcement
without a pressure valve breeds evasion. This drill flips the policy
shape, not the layer.

## Pair 24: prototype success vs production readiness

### CF-47

**Scenario.** A prototype scores 96% on 50 clean cases. The team ships to
real users. Winner so far: prototype.

**Change.** Real traffic arrives with typos and attacks. The score drops
to 70%. The adversarial drawer scores 12 of 100.

**Flipped answer.** Run the readiness loop: five eval drawers, five
watches, runbook, hardening.

**Why the answer changes.** The 96% proved the idea on clean data. Clean
data flatters: it never contains the typos and attacks that real
traffic brings. The 70% prices the hardening work, and the adversarial
drawer names the biggest gap. Production readiness is a different
product from the prototype, with owners, evidence, and gates. The
audience changed from the funder to the user, and the proof must change
with it.

### CF-48

**Scenario.** Full readiness hardening is underway on a new idea.
Winner so far: readiness work.

**Change.** The prototype test shows the model cannot do the core task
at all: 20% on the happy path.

**Flipped answer.** Kill the project. Stop the hardening.

**Why the answer changes.** Readiness hardens an idea that works. The
prototype answers "can this work," and the answer is no. Hardening a
dead idea is waste: eval drawers and runbooks cannot fix a missing
capability. The prototype gate comes before the readiness gate, and it
just failed. The correct move is the kill decision, made fast and
without sunk-cost grief.

## Pair 25: technical optimization vs business value

### CF-49

**Scenario.** The team cuts tokens 40% on a triage bot. Winner so far:
optimization.

**Change.** Finance asks for the net value. The bot saves $23,348 per
year in labor. The token cut saves $12 per month.

**Flipped answer.** The value case was already won. The optimization is
garnish.

**Why the answer changes.** The V2-D1.6 chain runs baseline, improvement,
cost, net value. The bot's net value comes from labor saved, not tokens
cut. The 40% cut is real engineering and nearly irrelevant money. The
priority question ("what is worth doing") outranks the implementation
question ("what is faster"). Optimization without the value lens is the
fastest route to a system nobody needed, and here the lens shows the
work was already done by the labor math.

### CF-50

**Scenario.** A support bot proved its value at $0.50 per ticket.
Winner: value case closed.

**Change.** Volume grows 100x. Unit cost breaks the budget. The CFO
freezes the rollout.

**Flipped answer.** Technical optimization: routing, caching, smaller
tiers, call elimination.

**Why the answer changes.** The value case held at the old volume. At
100x, the unit economics are the value case: a valuable task at a
broken unit cost is a prototype, not a product. Routing simple tickets
to cheaper tiers, caching the stable prefix, and killing redundant calls
restore the margin. The V2-D4.5 rule holds the floors: quality and
safety stay while cost falls. Scale changed the binding constraint from
"does it work" to "does the unit math work."

## Pair 26: implementation completion vs lifecycle ownership

### CF-51

**Scenario.** A feature merges with green tests. The team moves on.
Winner so far: implementation complete.

**Change.** The first incident pages nobody. There is no runbook, no
owner, no rollback plan.

**Flipped answer.** Lifecycle ownership: runbook, escalation, named
owner, watches.

**Why the answer changes.** Merge is a milestone, not a state. The
incident exposes the gap: code done, ownership missing. The V2-D6.5
chain runs discovery, design, handoff, monitoring, iteration. The team
stopped at handoff. Ownership assigns the watches, the runbook, and the
escalation path, so the next incident pages someone with a plan. "Done"
means owned, or it means nothing at 2 a.m.

### CF-52

**Scenario.** Full ownership rituals run on a prototype: on-call rota,
watch tuning, iteration budget. Winner so far: ownership.

**Change.** The prototype's end date passes. No users ever arrived.

**Flipped answer.** Implementation completion was the right finish line.
Drop the rituals.

**Why the answer changes.** Ownership serves users and incidents. A
throwaway experiment with a fixed end date and no users has neither.
The rota, the tuning, and the budget were waste: process without a
system to protect. The lifecycle chain applies to systems that live.
For the experiment, merged code and a short note were done. The scope
of the artifact decides the scope of the ownership, and here the
artifact expired.

## Coverage

| Pair | Topic | Drills |
|---|---|---|
| 1 | workflow vs agent | CF-01, CF-02 |
| 2 | single agent vs multi-agent | CF-03, CF-04 |
| 3 | augmented LLM vs autonomous loop | CF-05, CF-06 |
| 4 | sequential vs parallel execution | CF-07, CF-08 |
| 5 | MCP vs direct API vs CLI | CF-09, CF-10 |
| 6 | shared tools vs independent agents | CF-11, CF-12 |
| 7 | prompt caching vs response caching | CF-13, CF-14 |
| 8 | progressive discovery vs monolithic context | CF-15, CF-16 |
| 9 | RAG vs large-context prompting | CF-17, CF-18 |
| 10 | RAG vs customization | CF-19, CF-20 |
| 11 | retrieval failure vs model limitation | CF-21, CF-22 |
| 12 | skills vs tools vs subagents | CF-23, CF-24 |
| 13 | instructions vs enforceable permissions | CF-25, CF-26 |
| 14 | authentication vs authorization | CF-27, CF-28 |
| 15 | approval vs audit logging | CF-29, CF-30 |
| 16 | removing capability vs monitoring capability | CF-31, CF-32 |
| 17 | schema validity vs factual correctness | CF-33, CF-34 |
| 18 | citation presence vs citation support | CF-35, CF-36 |
| 19 | confidence vs calibrated risk | CF-37, CF-38 |
| 20 | human review vs deterministic validation | CF-39, CF-40 |
| 21 | offline evaluation vs A/B testing | CF-41, CF-42 |
| 22 | logging vs tracing vs compliance evidence | CF-43, CF-44 |
| 23 | project defaults vs managed policies | CF-45, CF-46 |
| 24 | prototype success vs production readiness | CF-47, CF-48 |
| 25 | technical optimization vs business value | CF-49, CF-50 |
| 26 | implementation completion vs lifecycle ownership | CF-51, CF-52 |
