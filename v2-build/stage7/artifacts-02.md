# Artifacts 02: reliability, governance, and operations

Minimal implementation artifacts from §21, continued. Each artifact carries its contract. Status is ILLUSTRATIVE unless a local run verified it. No artifact here was deployed. Nothing here spends money or touches an external system.

:::takeaway
Reliability is caller-side. Governance is code-side. Operations is owner-side. Each artifact below names which side it lives on.
:::

## A12. Retry and idempotency example

Purpose: the caller-side reliability bundle from Lesson 7-1A: timeout, retry, idempotency key, backoff. The key makes repeats safe.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the backend honors idempotency keys: same key twice yields one charge. Failures are transient flakes, not outages.

Dependencies: a clock for the timeout. A sleep for backoff.

Permissions: the caller's payment scope. The key must be a real business key (the charge id), not a fresh random id per attempt.

Security boundary: the retry loop never logs the full card number. The key is safe to log. Amounts are logged in cents as integers.

Expected behavior: transient failures retry with growing waits. A duplicate delivery with the same key yields one charge. A persistent outage raises after the attempt cap.

Failure cases: correlated outage: every retry fails, the cap fires. Random key per attempt: dedupe breaks, double charge. Backoff without a cap: unbounded latency.

Verification: executed locally against a simulated flaky ledger. Real output:

```
run1: {'status': 'charged', 'charged_cents': 4599} attempts: 3 backend calls: 3
run2 duplicate: {'status': 'duplicate', 'charged_cents': 4599} total distinct charges: 1
run3: raised after 3 backend calls. Distinct charges: 0
```

Two flakes then success on run 1. The duplicate delivery on run 2 charged once. The outage on run 3 raised with zero charges. Test file: `tests/t_retry_idempotency.py`.

Status: TESTED-LOCAL. Ran Oct 6, 2026 on this machine. No network. The ledger is a simulation, not a payment provider.

## A13. Approval state machine

Purpose: the V2-D5.3 pre-action approval gate as code. States and legal transitions only. Illegal transitions raise.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: one approval per action id. Terminal states are denied, expired, and executed. Expiry is driven by a clock outside the machine.

Dependencies: an event source for approve, deny, expire, execute.

Permissions: the approver identity is recorded on the approve event. The executor may differ from the approver.

Security boundary: the machine is the enforcement point. The tool that performs the action checks the state. It never trusts a claim of approval.

Expected behavior: requested moves to approved, denied, or expired. Approved moves to executed or expired. Terminal states accept no events.

Failure cases: double approve. Execute without approve. Approve after expiry. Clock skew on expiry.

Verification: executed locally. Seven checks, all pass. Three illegal transitions rejected: execute from requested, approve from expired, double approve. Real output:

```
approval FSM checks: [True, True, True, True, True, True, True] -> ALL PASS
```

Test file: `tests/t_approval_fsm.py`.

Status: TESTED-LOCAL. Ran Oct 6, 2026 on this machine. No network.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Unguarded approvals leak</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Seven checks. Three illegal moves rejected. One rule.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: NO MACHINE</text>
<rect x="44" y="144" width="256" height="32" rx="999" fill="#F3D4D8"/>
<text x="172" y="165" font-size="13" text-anchor="middle" fill="#1B2838">approve, approve: allowed</text>
<rect x="44" y="184" width="256" height="32" rx="999" fill="#F3D4D8"/>
<text x="172" y="205" font-size="13" text-anchor="middle" fill="#1B2838">execute, no approve: allowed</text>
<rect x="44" y="224" width="256" height="32" rx="999" fill="#F3D4D8"/>
<text x="172" y="245" font-size="13" text-anchor="middle" fill="#1B2838">approve after expiry: allowed</text>
<text x="44" y="276" font-size="13" fill="#5C6B7A">Any event, any time.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: STATE MACHINE</text>
<rect x="420" y="144" width="80" height="32" rx="999" fill="#E7F1F8"/>
<text x="460" y="165" font-size="11" text-anchor="middle" fill="#1B2838">requested</text>
<rect x="508" y="144" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="548" y="165" font-size="11" text-anchor="middle" fill="#1B2838">approved</text>
<rect x="596" y="144" width="80" height="32" rx="999" fill="#D9E8D3"/>
<text x="636" y="165" font-size="11" text-anchor="middle" fill="#1B2838">executed</text>
<rect x="420" y="192" width="256" height="32" rx="8" fill="#F6E7A8"/>
<text x="548" y="213" font-size="13" text-anchor="middle" fill="#1B2838">denied, expired: terminal</text>
<text x="420" y="244" font-size="13" fill="#5C6B7A">Illegal moves raise. 7 of 7 checks pass.</text>
<defs><marker id="ma13" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#ma13)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">guard transitions</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The machine rejects what the policy forbids. The log names the approver.</text>
</svg>
<figcaption>Shell 4. A guarded state machine replaces unguarded approvals and rejects three illegal moves. Source: original toy.</figcaption>
</figure>

## A14. Prompt version record

Purpose: every shared prompt component carries a version. A silent edit is a silent production change (V2-D2.5).

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: prompts live in version control. Each version pins the model id and the cache prefix.

Dependencies: the prompt registry. The deployment pipeline reads the version.

Permissions: prompt authors propose. Reviewers approve. The registry is append-only.

Security boundary: the version record names the reviewer. Unreviewed versions never reach production.

Expected behavior: a new version starts a new cache. Rollback means pointing at the prior version, not editing in place.

Failure cases: ten live versions mean ten cold caches. An unversioned hotfix bypasses review.

Verification: deploy version N+1 to the staging environment. Assert the cache key changes. Roll back and assert the prior version serves.

Status: ILLUSTRATIVE. Not executed.

```yaml
prompt: refund-classifier
version: 14
model: claude-sonnet-5-5
author: billing-team
reviewer: s.chen
approved: 2026-10-01
cache_prefix_sha: 9f2c41aa
supersedes: 13
change: "added damaged-goods examples. Rejection cases kept"
```

## A15. Claude Code configuration

Purpose: the team-shared `.claude/settings.json`: permissions, hooks, MCP servers, and model guardrails in one committed file (V2-D7.1).

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the repo is shared. Secrets exist in the environment. Destructive commands exist in the workflow.

Dependencies: the settings schema of the installed Claude Code version.

Permissions: `permissions.deny` lists the forbidden tools. `permissions.ask` lists the gated ones. Everything else follows the default.

Security boundary: deny rules are locks. CLAUDE.md guidance is not. Personal overrides live in `settings.local.json`, never in the shared file.

Expected behavior: every clone gets identical permissions, hooks, and MCP servers. Destructive commands ask or block. Secret paths deny reads.

Failure cases: an over-tight deny blocks legitimate work and developers route around it. A stale hook path breaks every edit.

Verification: clone fresh. Attempt `Read(.env)` and assert the deny fires. Run an edit and assert the PostToolUse lint hook runs.

Status: ILLUSTRATIVE. Not executed.

```json
{
  "permissions": {
    "deny": ["Bash(rm -rf:*)", "Bash(sudo:*)", "Read(.env)", "Read(**/*.key)"],
    "ask": ["Bash(deploy:*)", "WebFetch(*prod*)"]
  },
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": "./scripts/lint.sh"}]
    }]
  },
  "mcpServers": {
    "doc-search": {"command": "python3", "args": ["./mcp/doc_server.py"]}
  }
}
```

## A16. Skill

Purpose: a governed reusable asset: named, versioned, reviewed procedure shared across teams (V2-D2.5).

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the skill is invoked by name. It carries its own prompt block and its own version.

Dependencies: the skill registry. The caller's tool envelope.

Permissions: the skill inherits the caller's envelope. A skill used by two teams needs the narrower team's envelope.

Security boundary: the skill's inputs are validated at invocation. Its outputs are untrusted text until checked.

Expected behavior: same name and version produce the same procedure everywhere. A new version is reviewed before it ships.

Failure cases: version drift across teams. A skill that quietly gains a tool its callers should not hold.

Verification: invoke version N in two teams. Assert identical behavior. Publish N+1 without review and assert the registry blocks it.

Status: ILLUSTRATIVE. Not executed.

```yaml
skill: refund-triage-procedure
version: 3
owner: billing-team
reviewer: s.chen
steps:
  - lookup_order
  - classify_reason
  - check_policy
  - propose_action
forbidden: [issue_refund]
note: "proposes only. The refund tool stays outside this skill"
```

## A17. Hook

Purpose: code that runs on a lifecycle event: before a tool runs, after a file edit, on session start (V2-D7.1).

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the host supports PreToolUse and PostToolUse hooks with matchers. Hooks run locally with a timeout.

Dependencies: the hook command and its runtime.

Permissions: the hook inherits the agent's environment. A PreToolUse hook can block the call.

Security boundary: hooks are code, so they are reviewed like code. A hook that shells out to an unpinned script is a supply-chain risk.

Expected behavior: a PreToolUse hook blocks forbidden calls before they run. A PostToolUse hook lints after edits. A slow hook fails open with a warning, never silently.

Failure cases: hook timeout stalls every tool call. A crashing hook blocks all work. A hook that mutates files creates loops.

Verification: register a PreToolUse hook that denies one test command. Assert the denial fires and the audit records it. Time the hook under load.

Status: ILLUSTRATIVE. Not executed.

```json
{
  "PreToolUse": [{
    "matcher": "Bash",
    "hooks": [{"type": "command", "command": "./scripts/guard_bash.sh"}]
  }]
}
```

`guard_bash.sh` exits 1 on `rm -rf /`, on `sudo`, and on credential exfiltration patterns, else exits 0.

## A18. Plugin packaging example

Purpose: a distributable bundle: one skill, its hooks, its MCP server config, and its permission fragment, versioned together.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the plugin manager installs into the project config. The bundle declares its permission needs up front.

Dependencies: A15 config schema, A16 skill format, A17 hook format.

Permissions: the bundle requests the minimum set. Installation shows the requested permissions for review.

Security boundary: a plugin is third-party code. Review the bundle before install. Pin the version. Never auto-update a plugin with tool permissions.

Expected behavior: install adds the skill, hooks, and MCP server in one step. Uninstall removes all three. No residue.

Failure cases: a plugin update widens permissions silently. Two plugins register conflicting hooks. A malicious plugin exfiltrates via its MCP server.

Verification: install in a sandbox project. Assert the permission prompt lists the exact set. Uninstall and assert no hooks or servers remain.

Status: ILLUSTRATIVE. Not executed.

```
refund-plugin/
  plugin.json        # name, version, permission requests
  skills/refund-triage-procedure.yaml
  hooks/guard_bash.sh
  mcp/doc_server.py
  permissions.fragment.json
```

## A19. CI quality gate

Purpose: the merge gate from V2-D7.2: tests ran, results inspected, secrets protected. No claim of completion without the four evidence parts.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: CI runs on every pull request. The gate blocks the merge on failure.

Dependencies: the eval runner (A11), the secret scanner, the test suite.

Permissions: CI may read the repo and write check results. It holds no production credentials.

Security boundary: the secret scanner fails closed: a suspected secret blocks the merge until a human clears it.

Expected behavior: the regression drawer runs on every change. The secret scan runs on every diff. A red gate blocks the merge with a named reason.

Failure cases: a flaky test trains the team to re-run until green. The gate becomes advisory and then decorative.

Verification: open a PR with a known-bad change. Assert the gate blocks with the right reason. Open a PR with a fake secret and assert the scan blocks.

Status: ILLUSTRATIVE. Not executed.

```yaml
quality_gate:
  steps:
    - tests: "pytest -q"
    - regression: "eval-runner --dataset v2026-10-06 --block-on-regression-fail"
    - secrets: "scan --fail-closed"
    - evidence: "require: tests_ran, results_inspected, secrets_clear"
  on_fail: block_merge
```

## A20. Architecture decision record

Purpose: the nine-field ADR from V2-D6.4: decision, date, alternatives, rejections, assumptions, trade-offs, owner, evidence, open issues, review criteria. Successor-operable without the original meetings.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: one ADR per decision. Append-only. Light ADRs for reversible decisions.

Dependencies: none.

Permissions: authors propose. The owner signs.

Security boundary: the ADR records the security trade-off explicitly. "Accepted risk" needs a named acceptor and a review date.

Expected behavior: a new team member reconstructs the why from the ADR alone. Reversal cost is stated before it is needed.

Failure cases: ADRs written after the fact as justification. Stale ADRs that no longer describe the system.

Verification: hand the ADR to an engineer outside the team. Ask for the decision, the rejected alternatives, and the reversal cost. All three must come back correct.

Status: ILLUSTRATIVE. Not executed.

```markdown
# ADR-014: hybrid refund triage
Date: 2026-10-06. Owner: billing-team.
Decision: deterministic workflow for the fixed 80%, augmented call for the 20%.
Alternatives: all-agent (rejected: $480 vs $55.40 per day, unstable on fixed cases),
  all-workflow (rejected: cannot judge scanned receipts).
Assumptions: the 80/20 split holds. Receipt images stay legible.
Trade-offs: two code paths to maintain. Model cost on the 20%.
Evidence: eval drawer scores v2026-10-06. Cost toy in Lesson D1-patterns.
Open: receipt OCR quality below 90% triggers re-review.
Review: 2027-01-06 or on split drift.
```

## A21. Risk register

Purpose: the V2-D5.2 risk list with prevention, detection, and recovery per risk. Living document, reviewed on cadence.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: risks are named before they are managed. Each risk has an owner.

Dependencies: the threat model. Incident history.

Permissions: risk owners may accept, mitigate, or escalate. Acceptance needs a review date.

Security boundary: the register itself is internal. It names weaknesses, so access is limited.

Expected behavior: every known risk carries the three responses and an owner. New incidents add rows.

Failure cases: a register written once and never reviewed. Risks without owners.

Verification: pick three rows. Ask each owner for the current prevention and detection state. All three answer from the register, not from memory.

Status: ILLUSTRATIVE. Not executed.

| Risk | Prevention | Detection | Recovery | Owner |
|---|---|---|---|---|
| Prompt injection via tool output | Quarantine tool results as data | Adversarial drawer case adv-014 | Block call, alert, rotate | sec-team |
| Double charge on retry | Idempotency key = charge id | Duplicate-key metric | Reconcile ledger | billing-team |
| Stale RAG index | Re-ingest cadence | Freshness probe | Roll back index version | data-team |
| Reviewer rubber stamp | Sampled audits of approvals | Approval latency metric | Re-train, narrow scope | ops-lead |

## A22. Handoff checklist

Purpose: the V2-D6.5 handoff from builders to owners: everything the next team needs to operate the system.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the receiving team is named. The handoff is a meeting plus artifacts, not a document dump.

Dependencies: A20 ADRs, A21 risk register, A23 runbook.

Permissions: the receiving team gets the minimum access to operate, not the builder's full access.

Security boundary: credentials are rotated at handoff. Builder access is revoked.

Expected behavior: the receiving team runs the first incident drill before the handoff closes. Open items have owners and dates.

Failure cases: a handoff with no drill. Tribal knowledge that never made the checklist.

Verification: the receiving team answers five questions cold: the rollback step, the on-call rotation, the cost dashboard, the kill switch, the data retention rule.

Status: ILLUSTRATIVE. Not executed.

```markdown
## Handoff: refund triage v3
Receiving team: billing-ops. Date: 2026-10-06.
- [ ] ADRs 011-014 read and signed
- [ ] Risk register reviewed. Owners confirmed
- [ ] Runbook drill completed (incident: stale index)
- [ ] Dashboards: cost, latency, error rate, approval queue
- [ ] Credentials rotated. Builder access revoked
- [ ] Kill switch tested in staging
- [ ] Open items: receipt OCR review (owner: data-team, due 2026-11-01)
```

## A23. Incident runbook

Purpose: the V2-D7.3 ordered response: symptom to investigation mapping, owner, escalation. Written before the incident.

Version: 1.0. Baseline Oct 6, 2026.

Assumptions: the symptom map from V2-D7.3. Quality maps to prompt, model, or retrieval drift. Latency maps to context, dependencies, or cache. Tool issues map to credentials, permissions, or throttling. Cost maps to model choice, context, or cache use.

Dependencies: dashboards, traces, the eval runner.

Permissions: the on-call role may read logs and traces, restart services, and roll back versions. It may not change permissions.

Security boundary: the runbook never contains credentials. It names where to get them under break-glass.

Expected behavior: the on-call engineer follows the map, finds the layer, and acts. Every incident updates the map.

Failure cases: a runbook that describes the system instead of the response. Steps that assume tools the on-call role cannot reach.

Verification: run a game day on a staging incident. Time to the right layer. Every step must be executable by the on-call role.

Status: ILLUSTRATIVE. Not executed.

```markdown
## Runbook: wrong answers spike
Symptom: groundedness score drops below floor.
1. Check the eval dashboard: which drawer dropped.
2. Drawer = retrieval: check index freshness probe and chunk diff.
3. Drawer = adversarial: check for a new injection pattern. Add a case.
4. Else: check model version pin and prompt version (A14).
5. Mitigate: roll back the last change (prompt, index, or model).
6. Escalate to the data-team owner if the index is stale past 1 hour.
```

:::takeaway
Twenty-three artifacts, three executed locally with real output. The rest are complete, bounded designs. Nothing here claims a run that never happened.
:::
