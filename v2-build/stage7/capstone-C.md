# Capstone C: organization-wide Claude Code enablement

A design-and-defense exercise. The learner produces every section below as the deliverable. The scenario is fixed. The decisions are the learner's, defended against the alternatives.

Scenario: a 300-developer organization rolls out Claude Code. Goals: faster delivery, consistent quality, no secret leaks, no surprise bills. Constraints: production credentials exist in the environment. Destructive commands exist in the workflow. Three teams need different tool sets. The security team holds veto on the rollout.

## Discovery brief

Outcomes: developers ship faster with AI assistance. Every repo carries the same safety baseline. Spend stays under budget. Zero secret leaks in 90 days.

Capabilities: repo exploration, implementation, refactoring, testing, review, debugging, docs, incident investigation.

Prohibited behaviors: no secret reads. No destructive commands without a gate. No unreviewed config changes to the shared baseline.

Workflows: per-repo project config. Team-level shared skills. Org-level managed policies. Exception process for legitimate needs.

Cost limits: $25,000 per month for model spend. Per-team dashboards. Monthly cap with an owner.

Quality: reverts attributable to AI assistance tracked. Evidence gates on completion claims: tests ran, results inspected, secrets protected.

Compliance: the security baseline is non-negotiable and org-managed. Audit of config changes.

Dependencies: the identity provider for developer identity. The model provider for spend data. The repo hosting for config distribution.

Owners: platform lead, security reviewer, per-team config owners.

Open assumptions: the org can deploy managed settings to all machines. Developers accept a shared baseline with a documented exception path.

## Architecture alternatives

Option 1: layered config. Org-managed policies for the non-negotiables. Committed project configs per repo for team workflow. Personal overrides outside git.

Option 2: guidance only. One org CLAUDE.md with best practices. No enforced permissions.

Option 3: locked-down uniform config. One org config, no per-team variation, no overrides.

Trade table:

| Dimension | Option 1: layered | Option 2: guidance only | Option 3: locked down |
|---|---|---|---|
| Secret protection | Deny rules enforced | Wishes | Enforced |
| Team fit | Per-repo config | Full freedom | One size, poor fit |
| Bypass risk | Exception process | No control to bypass | Shadow workflows |
| Rollout friction | Medium | Low, then incidents | High |
| Audit | Config as code | None | Config as code |

Recommendation: Option 1. Enforcement where the security team needs it. Flexibility where teams need it. Option 2 fails the first secret leak. Option 3 breeds shadow workflows that the security team cannot see.

## Requirements

Functional: identical safety baseline on every machine. Per-repo workflow config. Shared skills for common procedures. Scoped subagents for research tasks.

Nonfunctional: config rollout under 24 hours. Spend dashboard per team. Secret scan on every commit.

Hard constraints: deny rules on secret paths are org-managed and cannot be weakened by teams. No plugin installs without version pinning and review.

Success criteria: zero secret leaks in 90 days. Spend under budget. Developer satisfaction above the pre-rollout baseline. Revert rate flat or down.

## Decision records

ADR-C1: layered config over guidance-only or locked-down. Enforcement for the baseline, flexibility for the workflow.

ADR-C2: instructions vs permissions split. CLAUDE.md carries guidance. Deny rules and hooks carry controls. Never one doing the other's job.

ADR-C3: scoped subagents for research. Read and Grep only. No write access. The research loop cannot modify code.

ADR-C4: shared skills as governed assets. Named, versioned, reviewed. A skill update is a reviewed change, not a silent edit.

ADR-C5: spend guardrails per team. Model selection per task class. Monthly cap with a named owner per team.

## Security review

Threats: secret exfiltration through the model. Destructive command execution. Malicious or careless plugin. Prompt injection via repo content.

Controls: org-managed deny rules on secret paths and destructive commands. PreToolUse hooks on risky commands. Secret scan in CI, fail closed. Plugin review before install, version pinned. Scoped subagents with fenced tool lists.

Fail-closed rules: a missing managed policy means the old policy stands, never no policy. A failed secret scan blocks the merge.

Residual risks: a developer can still paste a secret into chat. Accepted with training, the scan, and a review date. The control reduces, not eliminates.

## Evaluation plan

Metrics: secret-leak incidents (target zero). Spend per team per month. Revert rate on AI-assisted changes. Developer self-reported time saved. Evidence-gate compliance: the share of completion claims with all four evidence parts.

Method: baseline month before rollout. Monthly review after. Per-team dashboards. Quarterly security audit of the config and the plugin list.

Regression: any secret-leak incident triggers a full config review and a new adversarial test in the rollout checklist.

## Cost and latency budget

Volume: 300 developers, estimated 50 assisted sessions per developer per month: 15,000 sessions.

Per-session budget: mixed model routing. Cheap model for exploration, balanced for implementation. Toy estimate: $1.20 per session average. Per month: 15,000 times $1.20 = $18,000, under the $25,000 ceiling with headroom.

Latency: no user-facing SLA. Developer tools. Hook overhead budget: under 200 ms per tool call. Slower hooks fail open with a warning.

## Implementation contracts

Config contract: input, the layered settings. Output, the effective permission set per machine. Failure: managed policy missing means last-known-good stands, alert the platform lead.

Skill contract: input, the skill name and version. Output, the procedure with the caller's tool envelope. Failure: unreviewed version never installs.

Spend contract: input, per-team usage. Output, the dashboard and the cap alert. Failure: cap breach pages the team owner, throttles to the cheap model.

## Deployment gates

Gate 1: security review signed on the managed policy set.

Gate 2: pilot with 30 developers for one month. Zero leaks. Spend within the prorated budget.

Gate 3: matcher tests green on every deny rule: each rule proven to fire.

Gate 4: exception process documented and tested with one real request.

Gate 5: rollback plan: managed policy revert under 1 hour.

## Ownership

Platform lead: the managed policies, the rollout, the spend dashboards. Security reviewer: the baseline, the plugin reviews, the audits. Per-team config owners: the repo configs, the team skills. Developers: their personal overrides, kept out of git.

## Runbook

Symptom: secret-leak alert. Revoke the exposed credential at once. Find the leak path: chat, log, or commit. If the deny rule should have caught it, fix the pattern and add a matcher test. Postmortem within 48 hours.

Symptom: spend cap breach. Throttle the team to the cheap model. Review the usage: which task class drove it. Adjust routing or raise the cap with the owner's sign-off.

Symptom: developers report the baseline blocks legitimate work. Route through the exception process. Allow-list the narrow path with audit. Never weaken the org rule for one workflow.

## Stakeholder presentation

Executives: the productivity case, the spend ceiling, the risk posture. Security: the enforced baseline, the audit trail, the incident record. Engineering managers: the per-team flexibility, the skills library, the evidence gates. Developers: the workflow wins, the exception path, the override rules.

## Failure injection

Inject 1: attempt `Read(.env)` on a fresh clone. Expect: the deny rule fires. The attempt is logged.

Inject 2: install a plugin update that widens permissions. Expect: the review gate blocks it. The version stays pinned.

Inject 3: remove the managed policy from a test machine. Expect: last-known-good stands. The platform lead is alerted.

Inject 4: a scoped research subagent attempts a file write. Expect: the tool list denies it. The attempt is logged.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Layers beat wishes</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">300 developers. One shared baseline. Three teams, three workflows.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: EVERY DEV ALONE</text>
<rect x="44" y="144" width="256" height="32" rx="999" fill="#F3D4D8"/>
<text x="172" y="165" font-size="13" text-anchor="middle" fill="#1B2838">300 different setups</text>
<rect x="44" y="184" width="256" height="32" rx="999" fill="#F3D4D8"/>
<text x="172" y="205" font-size="13" text-anchor="middle" fill="#1B2838">secrets in chat: uncounted</text>
<rect x="44" y="224" width="256" height="32" rx="999" fill="#F3D4D8"/>
<text x="172" y="245" font-size="13" text-anchor="middle" fill="#1B2838">spend: nobody's number</text>
<text x="44" y="276" font-size="13" fill="#5C6B7A">No baseline. No owner.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: LAYERED CONFIG</text>
<rect x="420" y="144" width="80" height="32" rx="999" fill="#F6E7A8"/>
<text x="460" y="165" font-size="11" text-anchor="middle" fill="#1B2838">org policy</text>
<rect x="508" y="144" width="80" height="32" rx="999" fill="#E7F1F8"/>
<text x="548" y="165" font-size="11" text-anchor="middle" fill="#1B2838">repo cfg</text>
<rect x="596" y="144" width="80" height="32" rx="999" fill="#E7F4EF"/>
<text x="636" y="165" font-size="11" text-anchor="middle" fill="#1B2838">personal</text>
<text x="420" y="200" font-size="13" fill="#5C6B7A">Deny rules tested. Hooks live.</text>
<text x="420" y="220" font-size="13" fill="#5C6B7A">Spend per team, capped.</text>
<text x="420" y="240" font-size="13" fill="#5C6B7A">Exceptions documented.</text>
<defs><marker id="mcc" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#mcc)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">layer the config</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The org owns the baseline. Teams own the workflow. Nobody owns secrets in chat.</text>
</svg>
<figcaption>Shell 3. A layered config replaces 300 solo setups with one enforced baseline and per-team workflow. Source: original toy.</figcaption>
</figure>

## Related exam scenarios

V2-D7.1: team configuration, permissions vs guidance, hooks, scoped subagents, managed policies. V2-D7.2: evidence gates on AI-assisted work. V2-D2.5: skills as governed assets. V2-D3.1: least privilege on the tool surface.

:::takeaway
One enforced baseline. Per-team workflow freedom. Tested deny rules. Spend with an owner. Exceptions through a process, never around it.
:::
