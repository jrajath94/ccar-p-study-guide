# Prerequisite diagnostic: answer key

Sixteen expected answers for `stage2/diagnostic.md`. Baseline: Oct 6, 2026.
Each item gives the expected answer, the reason it holds, the principle it
tests, and the lesson section to re-read on a miss. These are study answers,
not exam items.

## Area 1: architecture and business foundations (lesson-7-4A)

### Q1: the missing acceptance criteria

**Expected answer.** The gap: "fast, accurate, and safe" are adjectives with
no acceptance criteria. No one can tell when the scribe is good enough.
First question to the clinic: "What does an acceptable note look like, and
how do we measure accuracy on real visits?"

**Why.** Latency work optimizes a number no one agreed to. Accuracy and
safety have no test. The team tunes a metric while the real goal stays
vague. Work without a target wastes the sprint.

**Principle.** Functional vs nonfunctional requirements, adjectives turned
into acceptance criteria before optimization (V2-D1.1, V2-D4.1).

**Re-read.** `lesson-7-4A.md` §4 (Causal mechanism) and §9 (Decisive
scenario constraints): the adjectives-to-numbers ladder.

### Q2: adjectives to numbers, cap check

**Expected answer.** Convert the adjectives: "a few seconds" becomes p95
response time at or under 5 seconds. "Almost nothing" becomes cost per chat
at or under $0.04. Cap check: $2,000 / 50,000 chats = $0.04 per chat.
The cap allows $0.04 per chat. Whether the adjectives fit depends on the
numbers chosen, so the conversion comes first.

**Why.** $2,000 divided by 50,000 equals $0.04 per chat. That is arithmetic,
not judgment. Until "a few seconds" and "almost nothing" become numbers,
no one can say if the pilot cap allows them. The conversion is the work.

**Principle.** SLOs and cost models at arithmetic level. Measurable
requirements before feasibility claims (V2-D1.1, V2-D6.1).

**Re-read.** `lesson-7-4A.md` §4 (Causal mechanism): SLO and unit-cost
arithmetic, and §5 (Minimal worked example) for the per-unit math.

### Q3: review strength ranking

**Expected answer.** Feature A (auto-sent refund emails) needs the stronger
review. Money moves with no human in the loop. Feature B (drafts for agent
approval) keeps a human gate. The two risk axes: impact (financial loss)
times reversibility (a sent refund is hard to reverse).

**Why.** Impact times reversibility sets review strength. A wrong refund
costs money and resists reversal. A wrong draft costs an agent's time and
never reaches the customer. Same code size, different risk class.

**Principle.** Risk classification by impact and reversibility. Review
strength keyed to consequence (V2-D5.3).

**Re-read.** `lesson-7-4A.md` §9 (Decisive scenario constraints): the
stakes ladder for human review.

### Q4: the decision record

**Expected answer.** The artifact: an architecture decision record (ADR).
Three fields it must contain: the decision and its date, the alternatives
considered and why each lost, and the owner who stands behind it.

**Why.** Six months later the only reliable witness is the written record.
The decision plus date fixes what was chosen and when. Rejected
alternatives stop the next engineer from re-litigating them. The owner
names who answers questions. Without these three, the choice evaporates.

**Principle.** ADRs make decisions successor-operable. Ownership is a
field, not a hope (V2-D6.4).

**Re-read.** `lesson-7-4A.md` §6 (Product and protocol mapping) and §9
(Decisive scenario constraints): ADR fields and ownership.

## Area 2: LLM foundations (lesson-7-3A)

### Q5: token arithmetic

**Expected answer.** Per-report token total: 40,000 input + 1,000 output =
41,000 tokens. Cut the input side first. The 40,000-token report dwarfs
the 1,000-token summary, and input tokens dominate the bill.

**Why.** Cost follows tokens, and input tokens are 40x the output here.
Any cut to the summary saves at most 1,000 tokens. A cut to the report
context (retrieval of relevant sections, compaction, truncation) saves
tens of thousands. Cut where the tokens are.

**Principle.** Tokens as the cost unit. Input vs output cost split
(V2-D2.4, V2-D4.5).

**Re-read.** `lesson-7-3A.md` §4 (Causal mechanism): token accounting, and
§9 (Decisive scenario constraints): where to cut first.

### Q6: the sampling model

**Expected answer.** Corrected mental model: the model samples from a
probability distribution, so one prompt can yield different outputs across
runs. The control that belongs outside the model: a grounding check of
each claimed date against the source document, in code.

**Why.** "Liar" implies intent. The mechanism is random draws from a distribution, not intent.
No prompt fixes sampling variance. Only an outside check (the date read
back from the source and compared in code) turns an unverifiable claim
into a verified one.

**Principle.** Generation as sampling. Hallucination as unverifiable
generation. Verification outside the model (V2-D4.1, V2-D5.2).

**Re-read.** `lesson-7-3A.md` §4 (Causal mechanism): sampling and
uncertainty, and §9 (Decisive scenario constraints): the outside check.

### Q7: retrieval over fine-tuning

**Expected answer.** Choose retrieval. The deciding fact: the handbook
updates every month. Fine-tuning bakes the current version into weights
that go stale on the next update. Retrieval reads the current version at
query time.

**Why.** The update cadence decides. Monthly changes make trained weights
a treadmill: retrain or serve stale policy. Retrieval re-ingests the
changed pages and cites them. Changing facts belong outside the model.

**Principle.** Retrieval for changing knowledge, fine-tuning for stable
behavior. Citation needs a source (V2-D3.5).

**Re-read.** `lesson-7-3A.md` §9 (Decisive scenario constraints) and §11
(Counterfactual where the alternative wins): when fine-tuning is wrong.

### Q8: indirect injection, fix layer

**Expected answer.** Attack class: indirect prompt injection (instructions
arrive inside untrusted content, the email, not from the user). The fix
lives in the enforcement layer and the tool layer: treat email text as
data, never as instructions, and gate the refund tool with a code check.
The prompt alone cannot carry this.

**Why.** The model cannot reliably separate "user instruction" from
"email content that looks like instruction" by prompt wording. The
boundary must be structural: untrusted text stays data, and the money
tool demands authorization in code. A prompt is guidance. The gate is a
lock.

**Principle.** Trust boundaries. Direct vs indirect injection.
Deterministic enforcement for side effects (V2-D5.1, V2-D5.2).

**Re-read.** `lesson-7-3A.md` §4 (Causal mechanism): trust boundaries, and
§9 (Decisive scenario constraints): structural separation.

## Area 3: software and distributed systems (lesson-7-1A)

### Q9: idempotent retries

**Expected answer.** The retry must live in the caller (client side), with
a per-charge idempotency key sent on every attempt. The mechanism that
makes a retried charge safe: the server dedupes on the key, so a repeated
request charges once.

**Why.** A blind retry re-sends "charge $50" as a new request. The server
sees two charges. An idempotency key turns the second send into a replay
of the first. The retry stays in the caller, where the timeout and the
key live. The safety lives in the server dedupe.

**Principle.** Retries with backoff. Idempotency keys for non-idempotent
operations (V2-D1.2).

**Re-read.** `lesson-7-1A.md` §4 (Causal mechanism): retry placement and
idempotency, and §5 (Minimal worked example).

### Q10: timeouts and backpressure

**Expected answer.** Two controls: a timeout (deadline) on the model call,
and backpressure on the request queue (bound the queue, shed or reject
excess load). The caller owns the timeout. The service owns the queue
bound.

**Why.** The 90-second hang holds a request slot. Slots fill, the site
slows. A caller-owned timeout caps how long one call can hold a slot.
Backpressure caps how many requests can pile up behind slow calls. One
without the other leaves a hole: no timeout means slots leak, no
backpressure means the queue grows without bound.

**Principle.** Timeouts at the caller, backpressure at the service.
Failures must not cascade (V2-D1.2).

**Re-read.** `lesson-7-1A.md` §4 (Causal mechanism): timeouts, backpressure,
and bulkheads.

### Q11: the three telemetry signals

**Expected answer.** Three signals: logs (discrete events per call),
metrics (counts, latencies, error rates over time), and traces (the 14
tool calls linked by one run id). The trace shows the cause: it links the
final error back through each hop to the step that first failed.

**Why.** The final error message names the symptom. Logs show what each
call did. Metrics show whether the failure is new or chronic. Only the
trace reconstructs the run end to end: call 7 of 14 returned the bad
value that call 14 choked on. Without the run id, the 14 calls are
strangers.

**Principle.** Observability as logs plus metrics plus traces. Trace
propagation across hops (V2-D3.4).

**Re-read.** `lesson-7-1A.md` §4 (Causal mechanism): the three signals, and
§9 (Decisive scenario constraints): reconstructability.

### Q12: consistency vs availability, blast radius

**Expected answer.** Trade-off in one sentence: stronger consistency costs
availability or latency, so a system that stays up during deploys accepts
brief staleness. Isolation principle: blast radius, limit the damage of
one bad deploy (canary, staged rollout, fast rollback).

**Why.** "Strong consistency everywhere, always" demands coordination on
every write. Coordination fails or slows under partitions and deploys.
The 60-second stale window is the price of staying available. Blast
radius keeps one bad flag push to a slice of traffic instead of the
fleet.

**Principle.** Availability vs consistency as a priced trade-off. Blast
radius for deploys (V2-D1.2).

**Re-read.** `lesson-7-1A.md` §9 (Decisive scenario constraints): the
consistency price tag, and §4 (Causal mechanism): blast radius.

## Area 4: security and identity (lesson-7-2A)

### Q13: hiding is not authorizing

**Expected answer.** The confusion: the team treats UI hiding as access
control. The absent check: server-side authorization on every request for
the admin resource. It must run at the enforcement point (the API or
server), never in the browser.

**Why.** The browser is the attacker's machine. A hidden link is one
"view source" away. The server answers the request, so the server must
check the caller's rights on each request. Hiding changes what honest
users see. Authorization changes what the server allows.

**Principle.** Authentication vs authorization. Enforcement at the server
boundary (V2-D3.2).

**Re-read.** `lesson-7-2A.md` §4 (Causal mechanism): authN vs authZ and the
enforcement point.

### Q14: the confused deputy

**Expected answer.** Identity problem: confused deputy, the bot acts with
ambient authority while "being" the customer. Safe delegation in one
sentence: the bot acts under a per-user delegated token with narrow
scopes, so each order-history read carries the real user's identity and
the least privilege it needs.

**Why.** "Act as the customer" hands the bot the customer's full rights
with no audit of whose authority it used. A scoped delegation token says:
this request runs for user X, may read orders, may not refund. The
service checks the token, not the bot's claim. Identity travels with the
call.

**Principle.** User identity vs service identity. Delegation with scopes.
No ambient authority (V2-D3.2).

**Re-read.** `lesson-7-2A.md` §4 (Causal mechanism): delegation and the
confused deputy, and §9 (Decisive scenario constraints).

### Q15: secrets in prompts

**Expected answer.** Two violations: the API key lives in the prompt
(secrets do not belong in model input), and the log exporter ships
prompts to an outside vendor (the secret leaves the trust boundary).
The key must live in a secrets manager (or the server-side credential
store), injected at the tool call, never in the prompt.

**Why.** Prompts get logged, cached, exported, and shown to vendors.
Any secret in a prompt is a secret shared with every system that touches
prompts. The model never needs the raw key: the tool layer holds the
credential and calls billing on the model's behalf, with the model's
request authorized in code.

**Principle.** Secrets management. Least privilege. Prompts are not a
credential store (V2-D5.1, V2-D3.1).

**Re-read.** `lesson-7-2A.md` §4 (Causal mechanism): secrets handling, and
§9 (Decisive scenario constraints): least privilege.

### Q16: tenant isolation and the audit record

**Expected answer.** Isolation failure: missing tenant isolation, one
tenant's configuration bleeds into another's answers. Minimum audit
record for one tool call: who (tenant and user id), what (tool name and
arguments), when (timestamp), and the decision or result.

**Why.** A shared prompt tweak with no tenant fence is a shared brain.
Clinic B's answers change because nothing separates the tenants'
configurations. The audit record must name the tenant on every call, or
a cross-tenant leak is invisible after the fact. Isolation is a design
property. The audit record is how it gets proven.

**Principle.** Tenant isolation. Auditability per call (V2-D3.2, V2-D5.4).

**Re-read.** `lesson-7-2A.md` §4 (Causal mechanism): tenant isolation and
audit records, and §9 (Decisive scenario constraints).

## Coverage

| Diagnostic | Area | Lesson section to re-read |
|---|---|---|
| Q1 | 7.4 requirements | lesson-7-4A §4, §9 |
| Q2 | 7.4 SLO and cost math | lesson-7-4A §4, §5 |
| Q3 | 7.4 risk classification | lesson-7-4A §9 |
| Q4 | 7.4 ADRs | lesson-7-4A §6, §9 |
| Q5 | 7.3 token accounting | lesson-7-3A §4, §9 |
| Q6 | 7.3 sampling and verification | lesson-7-3A §4, §9 |
| Q7 | 7.3 retrieval vs fine-tuning | lesson-7-3A §9, §11 |
| Q8 | 7.3 injection and trust boundaries | lesson-7-3A §4, §9 |
| Q9 | 7.1 retries and idempotency | lesson-7-1A §4, §5 |
| Q10 | 7.1 timeouts and backpressure | lesson-7-1A §4 |
| Q11 | 7.1 logs, metrics, traces | lesson-7-1A §4, §9 |
| Q12 | 7.1 consistency and blast radius | lesson-7-1A §4, §9 |
| Q13 | 7.2 authN vs authZ | lesson-7-2A §4 |
| Q14 | 7.2 delegation | lesson-7-2A §4, §9 |
| Q15 | 7.2 secrets and least privilege | lesson-7-2A §4, §9 |
| Q16 | 7.2 tenant isolation and audit | lesson-7-2A §4, §9 |
