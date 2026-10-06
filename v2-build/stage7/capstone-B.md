# Capstone B: high-impact workflow with human approval and auditable tool execution

A design-and-defense exercise. The learner produces every section below as the deliverable. The scenario is fixed. The decisions are the learner's, defended against the alternatives.

Scenario: a finance team processes 2,000 vendor payouts per week through an agent workflow. Each payout moves real money and is irreversible after submission. Error cost: a wrong payout averages $4,000. The regulator requires a named human approver on every payout above $10,000. Volume grows 20% per quarter.

## Discovery brief

Outcomes: payouts complete in one business day. Zero unapproved payouts above $10,000. Every payout is auditable to the human, the evidence, and the decision.

Capabilities: intake, validation, fraud screen, approval routing, execution, reconciliation.

Prohibited behaviors: no payout without the required approval. No approval without the full decision context. No silent auto-approval above the threshold.

Workflows: intake, deterministic validation, fraud screen, amount-based approval routing, execution with idempotency, reconciliation.

Cost limits: operations budget $15,000 per month. Reviewer capacity: 400 reviews per week. Quality: wrong-payout rate below 0.1%. Latency: one business day end to end.

Compliance: named approver on payouts above $10,000. Immutable audit log. Retention: 7 years.

Dependencies: the payment provider. The fraud screen service. The identity provider for approver identity.

Owners: finance lead, security reviewer, on-call engineer.

Open assumptions: the payment provider honors idempotency keys. Approvers are reachable within 4 business hours.

## Architecture alternatives

Option 1: deterministic workflow with stakes-keyed approval. Fixed steps in code. Below $10,000: auto-approve with post-action sampled review. Above: pre-action approval with the A13 state machine.

Option 2: autonomous agent loop with approval hooks. The model plans the payout steps. Approval interrupts the loop.

Option 3: human review on everything. Every payout waits for a person.

Trade table:

| Dimension | Option 1: workflow plus stakes | Option 2: agent loop | Option 3: review all |
|---|---|---|---|
| Predictability | Fixed steps | Varies per run | Fixed, slow |
| Reviewer load | Only the high-stakes class | Interrupts per plan | 2,000 per week: infeasible |
| Audit | Step log plus approvals | Trajectory plus approvals | Full human record |
| Error cost | Gated where it matters | Loop can act between gates | Lowest, unaffordable |
| Ops | One pipeline | Loop monitoring | Reviewer farm |

Recommendation: Option 1. The steps are known, so the workflow wins (V2-D1.3). Approval is keyed to stakes (V2-D5.3), not applied blindly. Option 3 exceeds reviewer capacity by 5x. Option 2 adds planning variance to money movement.

## Requirements

Functional: process 2,000 payouts per week. Route by amount: auto below $10,000 with sampled review, pre-action approval above. Execute with idempotency keys. Reconcile daily.

Nonfunctional: wrong-payout rate below 0.1%. Approval decision latency under 4 business hours. Audit query under 30 seconds.

Hard constraints: no execution without the required approval state. No approver sees a request without the full context: amount, vendor, evidence, fraud score. Idempotency key on every payment call.

Success criteria: zero unapproved high-value payouts. Wrong-payout rate under 0.1%. Reconciliation clean daily.

## Decision records

ADR-B1: deterministic workflow over an agent loop. Steps are fixed. Money movement punishes plan variance.

ADR-B2: stakes-keyed approval. Pre-action above $10,000. Sampled post-action below. Reviewer capacity is the binding constraint.

ADR-B3: the A13 state machine as the enforcement point. The payment tool checks the state. It never trusts a claim of approval.

ADR-B4: idempotency key = payout id. Retries are safe by construction. The ledger dedupes.

## Security review

Threats: approval bypass via a direct tool call. Approver coercion via a thin context. Double payout on retry. Fraudulent vendor onboarding.

Controls: the state machine guards every transition. The approval screen shows the full context: amount, vendor history, fraud score, supporting documents. The payment tool requires the approved state. Idempotency keys on all payment calls. Vendor changes need a separate approval.

Fail-closed rules: approval service down means no high-value payout ships. Fraud screen down means hold, not pass. Audit write failure blocks execution.

Residual risks: a determined approver can still approve a bad payout. Accepted with sampled audits of approvals and a review date.

## Evaluation plan

Dataset: historical payouts with labels: correct, wrong amount, wrong vendor, fraud. Adversarial drawer: bypass attempts, thin-context approvals, duplicate submissions.

Grading: code checks for the state machine transitions and the idempotency behavior. Human review of sampled approvals against the rubric. Judge for the fraud screen calibration.

Gates: zero bypasses on the adversarial drawer. Wrong-payout rate under 0.1% on the historical set. Approval context completeness at 100%.

## Cost and latency budget

Volume: 2,000 payouts per week, about 400 per business day.

Reviewer load: 15% of payouts exceed $10,000: 300 pre-action approvals per week, under the 400 capacity. Below threshold: 5% sampled post-action review: 85 per week.

Latency: intake and validation 10 minutes. Fraud screen 5 minutes. Approval queue p95 3 business hours. Execution 5 minutes. Total under one business day.

Cost: workflow compute trivial. Reviewer time: 385 reviews per week at 5 minutes each = 32 hours. The budget covers it with the current team.

## Implementation contracts

Intake contract: input, a payout request. Output, a validated request with a payout id. Failure: reject with reasons.

Approval contract: input, the payout plus full context. Output, an approved, denied, or expired state with the approver identity. Failure: expire on timeout, alert the requester.

Execution contract: input, an approved payout. Output, a provider confirmation with the idempotency key. Failure: retry with backoff, then hold for human.

Reconciliation contract: input, the day's payouts. Output, a matched ledger or an exception list. Failure: page the finance lead on any unmatched payout.

## Deployment gates

Gate 1: adversarial drawer green, including bypass attempts.

Gate 2: approval drill: the finance team approves, denies, and lets expire 20 test payouts.

Gate 3: idempotency proven in staging: duplicate deliveries yield one payout.

Gate 4: audit log queryable with sub-30-second response on a week of data.

Gate 5: runbook drill completed by the on-call engineer.

## Ownership

Finance lead: the approval policy and the reviewer roster. Security reviewer: the state machine, the audit log, the fail-closed rules. On-call engineer: the watches and the runbook. Data-team: the fraud screen calibration.

## Runbook

Symptom: unapproved payout alert. Freeze the payout queue. Check the state machine log for the bypass path. If the tool executed without the approved state, revoke its credentials and roll back the deploy. Page the security reviewer.

Symptom: approval queue backlog past 4 hours. Check approver availability. Escalate to the backup roster. Never auto-approve the backlog: the threshold is regulatory.

Symptom: duplicate payout detected. Check the idempotency key on both calls. If the keys differ, find the key-generation bug. Reconcile and recover from the vendor.

## Stakeholder presentation

Executives: the risk posture, the throughput, the cost. Finance: the approval policy, the reconciliation record, the audit trail. Engineering: the workflow, the state machine, the contracts. Regulators: the named approver per high-value payout, the immutable log, the fail-closed rules.

## Failure injection

Inject 1: call the payment tool directly with forged approval metadata. Expect: the tool checks the state machine and refuses. The attempt is logged.

Inject 2: approve a payout, then expire the approval before execution. Expect: execution refuses. The requester is notified.

Inject 3: submit the same payout twice within one second. Expect: one payout. The idempotency key dedupes.

Inject 4: take the fraud screen offline during a payout run. Expect: payouts hold. None pass silently.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Stakes key the review</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">2,000 payouts per week. 300 above $10,000. Reviewer capacity 400.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: REVIEW EVERYTHING</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">2,000 reviews needed</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">Capacity 400. Backlog 1,600.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">Rubber stamp by Friday.</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">The gate becomes theater.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: STAKES-KEYED</text>
<rect x="420" y="144" width="124" height="36" rx="999" fill="#F6E7A8"/>
<text x="482" y="167" font-size="12" text-anchor="middle" fill="#1B2838">300 pre-action</text>
<rect x="552" y="144" width="124" height="36" rx="999" fill="#E7F4EF"/>
<text x="614" y="167" font-size="12" text-anchor="middle" fill="#1B2838">85 sampled</text>
<text x="420" y="200" font-size="13" fill="#5C6B7A">385 reviews. Under capacity.</text>
<text x="420" y="220" font-size="13" fill="#5C6B7A">Full context per approval.</text>
<text x="420" y="240" font-size="13" fill="#5C6B7A">State machine enforces.</text>
<defs><marker id="mcb" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mcb)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">key by stakes</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Review where the money is irreversible. Sample where it is not.</text>
</svg>
<figcaption>Shell 4. Stakes-keyed review moves 2,000 reviews to 385 and keeps the gate real. Source: original toy.</figcaption>
</figure>

## Related exam scenarios

V2-D5.3: review strength keyed to consequence and reversibility. V2-D5.1: deterministic tool authorization, fail closed. V2-D1.3: the workflow pattern for fixed steps with high error cost. V2-D3.4: tracing the payout run end to end. V2-D6.4: ADRs for the approval policy.

:::takeaway
Fixed steps in code. Approval keyed to stakes. The state machine as the lock. The idempotency key as the safety net. Every payout auditable.
:::
