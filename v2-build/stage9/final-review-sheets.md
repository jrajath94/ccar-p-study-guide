# Final review sheets

Last-mile sheets. Each sheet compresses one domain into the
highest-yield decisions and the canonical traps. No new topics.
Every term below was taught in the lessons. Read a sheet, then
solve. If a line feels new, go back to its lesson.

## Sheet 0: foundations (§7)

Highest-yield decisions:

1. The threshold chain: every adjective becomes a metric, a
   threshold, and an owner. "Fast" means nothing until it reads
   "p95 under 2 seconds, owned by the platform lead."
2. The sampler model: the model predicts the next token. It never
   verifies. Every model output needs a check outside the model.
3. Caller-side reliability: the retry lives in the caller, with an
   idempotency key. The model never retries a payment.
4. Enforcement before context: authorization runs in code before
   the model sees the data. A prompt that says "I am a manager"
   is a sign, not a lock.

Canonical traps: UI hiding is not authorization. A session id
proves nothing about the speaker. Token theft windows shrink
with short lifetimes.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 1: solution design (D1, 17%)

Highest-yield decisions:

1. The fork: fixed mapping goes deterministic. Open input with a
   verifiable output goes to Claude with a gate in code.
2. The pattern spectrum: augmented call, deterministic workflow,
   hybrid, agentic. Score on predictability, reversibility, error
   cost, latency, cost, observability, and dynamic-planning need.
3. Multi-agent needs handoff contracts: coordinator and worker
   roles, a disagree rule, checkpointing, trace propagation.
   Justify multi-agent over one agent plus tools, or do not
   build it.
4. Net value: (baseline cost minus new cost) times volume, plus
   avoided error cost, minus build and run cost. Measure the
   baseline first.

Canonical traps: Claude for everything. An agent loop on a fixed
task pays four calls where one would do. A build with no success
bar cannot prove it worked.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 2: models, prompting, context (D2, 13%)

Highest-yield decisions:

1. Tier pick: the cheapest tier that clears the quality floor
   wins. Cascade with a confidence check. Treat upgrades as
   production changes with regression tests.
2. Prompts are contracts, never authorization. Separate stable
   content from untrusted content. Structural enforcement gives
   hard guarantees. A prompt gives none.
3. Technique ladder: simplest technique that passes evals.
   Few-shot with rejection examples for near-miss shapes.
4. The prefix rule: stable first, variable last. Cache pricing is
   write 1.25x and read 0.1x with a 5-minute TTL. Break-even sat
   at a 4% hit rate on the toy. Recompute for your own numbers.

Canonical traps: prompts as enforcement. Caching the variable
tail breaks the prefix. A tier upgrade by default, with no
evidence the model layer is guilty.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 3: integration (D3, 19%)

Highest-yield decisions:

1. Capability bloat: removal revokes. Logging only watches. Least
   privilege on tools, data visibility, and write scope.
2. Identity: per-user delegation, audience-bound tokens, no token
   passthrough, source-system ACLs preserved. No shared
   credentials where the audit must name the human.
3. Latency: cut the worst ms-per-point stage when the SLA binds.
   Optimize to the SLA, not to zero. Tail latency decides.
4. RAG: ten stages, errors compound downstream. Fix upstream
   first. Chunk by document structure and query type. Live
   transactional state belongs behind a tool call, not a stale
   index.
5. Discovery: advertise lightly, fetch lazily, scope the list.
   Progressive discovery wins when tokens or selection confusion
   bind.

Canonical traps: shared credentials with audit needs. Faster
index rebuilds for live data, when the change rate beats any
cadence. Two hundred tools in one monolithic context.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 4: evaluation (D4, 16%)

Highest-yield decisions:

1. Metrics: the primary metric comes from the business goal.
   Guards stand as floors. When the budget binds, cost per
   successful task is the primary. Proxies stay diagnostic.
2. Datasets: five drawers (representative, edge, adversarial,
   malformed, regression), plus holdouts. Cheapest reliable
   evaluator per drawer: code, then judge, then human. Calibrate
   judges against human labels.
3. A/B tests: falsifiable hypothesis, primary metric first,
   consistent assignment, shadow before exposure. Statistical
   significance is not business significance.
4. Diagnosis: symptom to evidence to hypotheses to a
   discriminating test to the smallest correction to regression
   verification. Fix the failing layer, not a proxy.
5. Optimization: ordered levers (measure, context, cache, route,
   eliminate). Hold quality and safety floors on every cut.
   Streaming buys perception, not completion.

Canonical traps: accuracy as the eternal primary. A tier upgrade
for a template fault. A green proxy while the goal is red.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 5: governance (D5, 14%)

Highest-yield decisions:

1. Guardrails: the tool call is the enforcement point. Gates run
   in code before execution and fail closed. The model never
   enforces its own limits.
2. Human review: three shapes (pre-action, post-action, sampled)
   keyed to five stakes (consequence, reversibility, uncertainty,
   regulation, impact). Reviewers need full decision context.
   Model confidence is a phrase, not a score.
3. Compliance: one chain per requirement. Requirement, control,
   owner, evidence, cadence. Architectural implications only,
   never legal advice.
4. Responsible AI: per-group metrics and floors. The group score
   is the metric. The aggregate is the footnote.

Canonical traps: confidence as a calibrated score. Reviewing
everything at volume, which guarantees reviewer fatigue. Prompts
as money or confidentiality controls. The 90% aggregate hiding
the 68% group.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 6: stakeholders and lifecycle (D6, 14%)

Highest-yield decisions:

1. Discovery first: outcomes, capabilities, prohibited behaviors,
   workflows, cost limits, volume, quality and latency
   expectations, compliance, dependencies, owners, open
   assumptions. Turn adjectives into measurable requirements.
2. Trade-off communication: five fields per option (benefit, cost,
   risk, reversal cost, compliance impact), adapted per audience
   (exec, engineering, security, legal, product).
3. The return rule: never substitute later-phase work for
   unfinished discovery or design. A later-phase failure goes
   back to the skipped phase.
4. ADRs: decision, date, alternatives, rejections, assumptions,
   trade-offs, owner, evidence, open issues, review criteria.
   Successor-operable without the original meetings.

Canonical traps: "perfect," "never," and "zero" promises.
Best-effort promises with no triggers or consequences. Skipping
discovery under schedule pressure, then paying ten times
downstream.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.

## Sheet 7: developer productivity (D7, 7%)

Highest-yield decisions:

1. Team config: instructions vs enforceable permissions. CLAUDE.md
   guides. Deny rules enforce. Managed settings beat local ones.
   Scoped subagents carry least privilege.
2. AI workflows: four-part evidence before merge (tests ran,
   results inspected, no secrets in the diff, docs updated).
   Productivity is verified outcomes, not generated lines.
3. The symptom map: quality drift points to prompt, model, or
   retrieval. Latency points to context, dependencies, or cache.
   Tool failures point to credentials, permissions, throttling,
   or contracts. Cost points to tier picks, context, or cache.
   Lost agent work points to orchestration state and traces.

Canonical traps: lines of code, tokens, or hours as productivity.
Guidance treated as enforcement. A green test suite with no
failing test proving it catches bugs.

10-step checklist: ask type, stage, objective, constraints, layer.
Kill infeasible, kill constraint-breakers. Compare on objective,
check dependencies, verify the pick.
