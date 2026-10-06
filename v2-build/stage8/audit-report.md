# Stage 8d audit report: independent adversarial audit of the CCAR-P v2 question bank

Auditor: Stage 8d (independent adversarial auditor). Baseline: Oct 6, 2026.
Scope: 477 questions (qb-D1..D7: 175, qb-mixed: 50, mocks: 252) + 16
diagnostic keys. Method per item: attempt to defeat the key per the
§19.3 attack list (ambiguity, stale facts, unsupported capabilities,
missing permission layers, wrong lifecycle stage, cost/latency
assumptions, multi-select uniqueness, incomplete enforcement,
model/platform incompatibility, counterfactual soundness).
Rule: two equally defensible answers = FAIL. Fix loop max 3, then
REJECTED.

## Priority flags (builder-marked, audited first)

| ID | Verdict | Summary |
|---|---|---|
| Q-M-15 | FIXED (loop 1) | Select TWO had THREE defensible answers (A growth, B duplication, C dilution, lesson-D2-4 names dilution as a fault). Rebuilt as Select THREE, key A, B, C. |
| M2-Q13 | PASS | Key B unique. Distractors absurd but none valid. Weak-distractor note only. |
| M3-Q33 | FIXED (loop 1) | Key B demanded "measurement conditions," a requirement the Lesson 7-4A / lesson-D4-1 chain (requirement, metric, threshold, owner) does not teach, the lesson's own worked example treats "p95 under 5 seconds" as a complete guard. Old key contradicted the lesson. Rebuilt around the genuinely missing taught link: the owner. Key now B. |
| M4-Q47 | PASS | Key A unique: pre-action approval is the right shape (review before the publish action) and proportionate (public but reversible, drafts usually fine, editor has context). No other option defensible. |

## Per-question status

Legend: PASS = key survived. FIXED = key/scenario/distractor edited (loop count).
REJECTED = removed to rejected-items.md. PENDING = not yet audited.

### qb-D1.md (Q-D1-01 .. Q-D1-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D1-01 | PASS | B fork (deterministic 70%, Claude 30%) + code gate, D infeasible at 12k/day |
| Q-D1-02 | PASS | C constraint into design first, D prompt-is-not-enforcement trap |
| Q-D1-03 | PASS | Select TWO B,C: must-never-happen test, A/D/E are goals not hard constraints |
| Q-D1-04 | PASS | Cost/latency toy labeled, B unique, D's prefix argument sound |
| Q-D1-05 | PASS | B is the lesson's seven-gate architecture, A/C/D each fail replay |
| Q-D1-06 | PASS | Select TWO unique: B names record, C names hop, D nice-but-not-mandatory addressed |
| Q-D1-07 | PASS | Trace indicts retrieval, B fixes failing layer, not a proxy |
| Q-D1-08 | PASS | B gives gate teeth in code + cause fix, A infeasible at 50k/day (417 h math checks) |
| Q-D1-09 | PASS | 90/10 split + irreversible refunds: B unique hybrid |
| Q-D1-10 | PASS | B attacks both failure modes (parallelism + no rewrites + deterministic split) |
| Q-D1-11 | PASS | Unknown steps: B agentic unique |
| Q-D1-12 | PASS | Select THREE A,B,D unique, C contradicts fixed steps, E pays model price for fixed parse |
| Q-D1-13 | PASS | B best (contracts + merge + checkpoint), A valid-but-inferior, not equal |
| Q-D1-14 | PASS | Entangled work: B single agent unique |
| Q-D1-15 | PASS | Select TWO A,B per taught contract definition, C's counterfactual correctly scoped out |
| Q-D1-16 | PASS | B evidence-based resolution, D majority vote addressed as weaker for high stakes |
| Q-D1-17 | PASS | B fan-out + per-number citations + code totals check unique |
| Q-D1-18 | PASS | Routing is the shape fix, A unique |
| Q-D1-19 | PASS | Select TWO A,B unique, D's counterfactual (tiny corpus) correctly scoped out |
| Q-D1-20 | PASS | Deterministic split B unique, two samples do not make a proof |
| Q-D1-21 | PASS | Arithmetic verified: $137,960 net, B/C/D each drop exactly one term as claimed |
| Q-D1-22 | PASS | Measured negative net: C unique, pilot-when-measured-is-delay argument sound |
| Q-D1-23 | PASS | Select TWO A,B per lesson definitions, C/D/E mislabels each addressed |
| Q-D1-24 | PASS | $500k error term dominates, B unique |
| Q-D1-25 | PASS | Unknown baseline: B pilot-first unique per lesson |

### qb-D2.md (Q-D2-01 .. Q-D2-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D2-01 | PASS | B unique, D adds cost for unneeded margin, floor already met |
| Q-D2-02 | PASS | B cascade+escalation, 8s budget fits, counterfactual covers latency-bound case |
| Q-D2-03 | PASS | Select TWO A,C: regression suite + canary per production-change rule |
| Q-D2-04 | PASS | C fewest rungs, hidden dependency (single tier must clear floor) acknowledged in walk, D mechanism backwards |
| Q-D2-05 | PASS | B climb one rung, spread-even errors undercut few-shot (C) |
| Q-D2-06 | PASS | B code gate fail-closed, classic enforcement item |
| Q-D2-07 | PASS | B untrusted-data marking + tool filter, C kills feature |
| Q-D2-08 | PASS | Select TWO B,C: hard guarantee needs schema+validator, prompt (A) gives none |
| Q-D2-09 | PASS | B versioned modules, standard |
| Q-D2-10 | PASS | B instructions vs enforcement, standard |
| Q-D2-11 | PASS | B rejection examples for near-miss shape |
| Q-D2-12 | PASS | B decline: bar met, reasoning adds tokens for no gain |
| Q-D2-13 | PASS | Select TWO A,B, D wrong (evals pass), E wrong (task 2 hard) |
| Q-D2-14 | PASS | A checkable reasoning steps for regulator |
| Q-D2-15 | PASS | B fine-tune/reframe after techniques exhausted, C is proxy fix |
| Q-D2-16 | PASS | B JIT + compaction trigger, A/C/D each lose or delay |
| Q-D2-17 | PASS | B fewer shorter better-placed chunks, A worsens dilution |
| Q-D2-18 | PASS | Select TWO A,B, C mislabels retention need as growth, correctly rejected |
| Q-D2-19 | PASS | B bounded storage outside active context, 7-yr retention vs context |
| Q-D2-20 | PASS | C fix compaction contract, trigger value kept |
| Q-D2-21 | PASS | B stable-first reorder, prefix rule |
| Q-D2-22 | PASS | Select TWO A,C, 4% break-even verified against lesson derivation (0.000576/0.0144=0.04) |
| Q-D2-23 | PASS | B reorder then re-measure, TTL does not fix broken prefix |
| Q-D2-24 | PASS | B governed Skill, drift failure |
| Q-D2-25 | PASS | Select THREE A,B,E, C prose cannot scope permissions |

### qb-D3.md (Q-D3-01 .. Q-D3-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D3-01 | PASS | B remove/scope delete_account, logging is not removal |
| Q-D3-02 | PASS | B merge overlapping tools, narrow profile, least privilege |
| Q-D3-03 | PASS | Select TWO A,C: drop_table removed, list_users narrowed, refund kept (task needs it) |
| Q-D3-04 | PASS | B per-user delegation, shared credential kills attribution |
| Q-D3-05 | PASS | B token audience binding + deterministic refund auth fail-closed |
| Q-D3-06 | PASS | C local stdio inherits trust, remote needs OAuth, matches MCP guidance |
| Q-D3-07 | FIXED | FIXED expl: key A survives (best first cut) but 2.9-0.7=2.2s still exceeds 2s SLA, explanation now states residual 200ms gap and next cuts |
| Q-D3-08 | PASS | B remove unmeasured stage, no-measured-gain loses to SLA |
| Q-D3-09 | PASS | Select TWO A,D: parallelize independent, spend on accuracy when SLA loose+errors costly |
| Q-D3-10 | PASS | B per-hop tracing first, then investigate |
| Q-D3-11 | PASS | C sample deep + skeleton + all errors, cost-bounded observability |
| Q-D3-12 | PASS | B redact PII before trust boundary, in code |
| Q-D3-13 | PASS | B re-chunk at structure boundaries, vectors do not fix broken chunks |
| Q-D3-14 | PASS | Select TWO A,B: full pipeline with citation checks + structure chunking |
| Q-D3-15 | PASS | C roll back chunking change, trace indicts chunker |
| Q-D3-16 | PASS | B hybrid + rank fusion for mixed query shapes |
| Q-D3-17 | PASS | B live tool call for live state, refresh cadence cannot beat change rate |
| Q-D3-18 | PASS | Select THREE A,B,D: ACL-first, hybrid, tool for daily numbers |
| Q-D3-19 | PASS | B one MCP server, one schema, all hosts |
| Q-D3-20 | PASS | B direct API, one host one language, exam rewards present scenario |
| Q-D3-21 | PASS | B CLI wrapper for mainframe + agent-to-agent for subtask |
| Q-D3-22 | PASS | Select TWO A,B: MCP for shared multi-lang, direct for single |
| Q-D3-23 | PASS | B progressive discovery, token budget binds |
| Q-D3-24 | PASS | B discovery answers both complaints, rewrite answers one |
| Q-D3-25 | PASS | Select THREE A,B,C: per-case discovery verdicts |

### qb-D4.md (Q-D4-01 .. Q-D4-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D4-01 | PASS | C metric chain first, standard |
| Q-D4-02 | PASS | B replace proxy with task success, proxy green goal red |
| Q-D4-03 | PASS | ATTACKED: A looked defensible, but lesson-D4-1 §9 table says "Budget binds → Cost per successful task is the primary", key B,E lesson-grounded. PASS |
| Q-D4-04 | PASS | C safety guard metric gap, medical triage |
| Q-D4-05 | PASS | B add edge/adversarial/malformed drawers from production |
| Q-D4-06 | PASS | B calibrate judge against human labels, drift |
| Q-D4-07 | PASS | Select TWO A,C: ladder daily, human for releases, calibrate within scope |
| Q-D4-08 | PASS | A strip PII + regression drawer, single best answer |
| Q-D4-09 | PASS | B shadow then controlled exposure, risky refund change |
| Q-D4-10 | PASS | B split changes, test one at a time, attribution |
| Q-D4-11 | PASS | Select THREE A,B,E: falsifiable hypothesis, consistent assignment, business significance |
| Q-D4-12 | PASS | B business math: 6000 successes at $4000/day needs success >$0.67, arithmetic verified |
| Q-D4-13 | PASS | B Tuesday change first suspect, change-date rule |
| Q-D4-14 | PASS | B fix template layer, trace indicts template |
| Q-D4-15 | PASS | Select TWO A,B: verification fault + retrieval fault, incident 3 not model |
| Q-D4-16 | PASS | C instrument first, no fix without evidence |
| Q-D4-17 | PASS | A cut thinnest receipt, question says "first cut" so framing honest |
| Q-D4-18 | PASS | B streaming is perceived-latency win, p95 truth named |
| Q-D4-19 | PASS | B floor unmet means no cuts, fix quality first |
| Q-D4-20 | PASS | Select TWO A,B: shrink context then cache, route easy calls |
| Q-D4-21 | PASS | C refresh stale suite, green dashboard vs drift |
| Q-D4-22 | PASS | B fast line + slow line, outage vs drift |
| Q-D4-23 | PASS | C name an owner first, unowned alert is not monitoring |
| Q-D4-24 | PASS | B retune or retire, weekly no-action firing is a wrong line |
| Q-D4-25 | PASS | Select TWO A,B: instrument all layers + regression on change |

### qb-D5.md (Q-D5-01 .. Q-D5-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D5-01 | PASS | B deterministic gate fail-closed + screening + sandbox, D infeasible at 8k/day |
| Q-D5-02 | PASS | B untrusted-data screening + deterministic gate, first control |
| Q-D5-03 | PASS | Select TWO A,B: payout gate and screener fail closed, C/E fail open, D not safety |
| Q-D5-04 | PASS | B confine to /reports, deny network, time limit, least privilege |
| Q-D5-05 | PASS | B code-level output screening + pin version + regression, model update shifted refusal |
| Q-D5-06 | PASS | A indirect injection: sandbox + screen + quarantine + alert |
| Q-D5-07 | PASS | A cap + alert + call-count from measured runs, B breaks legit 24-call tasks |
| Q-D5-08 | PASS | Select TWO A,B: kill run + quarantine, incident response pair |
| Q-D5-09 | PASS | B pin version + regression + rollback, version-behavior control |
| Q-D5-10 | PASS | B checkpoint + verify handoffs + resume + alert, silent skip |
| Q-D5-11 | PASS | B pre-action on 8% + sampled 2%, math: 480x3min=24h/day feasible vs 300h full |
| Q-D5-12 | PASS | A full decision context for reviewers, 98% approval hid 40% bad |
| Q-D5-13 | PASS | Select TWO A,B: post-action sampled on reversible, pre-action on legal-risk |
| Q-D5-14 | PASS | B licensed pre-action approval, logged, regulator requires it |
| Q-D5-15 | PASS | B rotate + cap sessions + stakes-keyed shape, fatigue is the fault |
| Q-D5-16 | PASS | B EU region + role-scoped access + retention + owner/evidence/cadence |
| Q-D5-17 | PASS | B deletion log + access review as evidence |
| Q-D5-18 | PASS | Select TWO A,B: requirement-control-owner-evidence-cadence chains |
| Q-D5-19 | PASS | B hold 90-day schedule, debug on masked data |
| Q-D5-20 | PASS | B deployment-route row first, FedRAMP |
| Q-D5-21 | FIXED | FIXED numbers: 800x96%+200x68%=90.4%, scenario said 94%, corrected to 90% in scenario, option A, explanation. Key B unaffected |
| Q-D5-22 | PASS | B split by group + per-group floor, 12-point gap |
| Q-D5-23 | PASS | Select TWO A,C: applicant notice + trace for replay |
| Q-D5-24 | PASS | Select TWO A,B: uncertainty interval + grow sample, n=20 too noisy to bind (1 miss=5pts) |
| Q-D5-25 | PASS | B trace-backed explanations only, fabricated citations blocked |

### qb-D6.md (Q-D6-01 .. Q-D6-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D6-01 | PASS | B structured discovery first, adjectives to requirements |
| Q-D6-02 | PASS | B adjectives to numbers before design, contract binds |
| Q-D6-03 | PASS | Select TWO A,C: prohibited behaviors + compliance cells |
| Q-D6-04 | PASS | C record conflict, escalate to owner, hold design |
| Q-D6-05 | PASS | B update volume cell at review date, check dependents |
| Q-D6-06 | PASS | B honest trade-off presentation, numbers verified: $192k saving, 33.3h/day, A violates $60k budget |
| Q-D6-07 | PASS | B security-lead message: in-region, fewer hops, attack surface |
| Q-D6-08 | PASS | Select TWO A,C: 1% of 10k = 100/day math verified, honest restatements |
| Q-D6-09 | PASS | B recompute + re-sign with new prices, dated numbers |
| Q-D6-10 | PASS | B reversal cost named as part of decision |
| Q-D6-11 | PASS | Select TWO A,B: 420<450 trigger not fired, 2pt miss < 10pt iterate rule |
| Q-D6-12 | PASS | B re-architect per contract rule, 18pt drop, iterations failed |
| Q-D6-13 | PASS | Select TWO A,B: measured quality + review triggers with consequences |
| Q-D6-14 | PASS | B segment drift first, new ticket types |
| Q-D6-15 | PASS | B honest forecast: $0.06x10kx30=$18k, triple=$54k, math verified |
| Q-D6-16 | PASS | B full ADR serves successor |
| Q-D6-17 | PASS | B ADR-015 supersedes, chain the records |
| Q-D6-18 | PASS | Select TWO A,D: review criteria + breakable assumptions |
| Q-D6-19 | PASS | A three highest-consequence flags first |
| Q-D6-20 | PASS | B light ADR or commit message, right-sized |
| Q-D6-21 | PASS | B return to discovery, no substituting later-phase work |
| Q-D6-22 | PASS | B ship hotfix, ADR in post-incident window |
| Q-D6-23 | PASS | Select TWO A,B: ADR set + runbook for handoff |
| Q-D6-24 | PASS | B return to design: threshold from measured data |
| Q-D6-25 | PASS | B right-size gates to team |

### qb-D7.md (Q-D7-01 .. Q-D7-25)

| ID | Verdict | Note |
|---|---|---|
| Q-D7-01 | PASS | B deny rules + PostToolUse lint hook + shared settings, instructions are not enforcement |
| Q-D7-02 | PASS | B layered settings: org-managed non-overridable + local exceptions |
| Q-D7-03 | PASS | B settings.local.json expiring, shared file untouched |
| Q-D7-04 | PASS | Select TWO A,B: org-managed = non-weakenable secrets + spend cap |
| Q-D7-05 | PASS | B scoped subagent Read/Grep only, no write tool exists |
| Q-D7-06 | PASS | B one MCP server in shared config, tokens out of chat |
| Q-D7-07 | PASS | B route cheap to cheap + spend number with owner |
| Q-D7-08 | PASS | Select TWO A,C: deny rule + PreToolUse block are enforcement |
| Q-D7-09 | PASS | B allow safe, deny dangerous, ask on gray middle |
| Q-D7-10 | PASS | B four evidence parts before merge |
| Q-D7-11 | PASS | B failing test first proves suite catches bugs |
| Q-D7-12 | PASS | B evidence gates, math verified: 9x4hx$150=$5,400/mo |
| Q-D7-13 | PASS | B pre-commit hook fail-closed on key patterns |
| Q-D7-14 | PASS | B cited paths + executed examples for unverifiable summary |
| Q-D7-15 | PASS | Select TWO A,D: revert rate + run-log share, LoC/tokens/hours are vanity |
| Q-D7-16 | PASS | B merge on prose, gate cost vs revert cost proportionality |
| Q-D7-17 | PASS | Select TWO A,B: negative claim needs paths + observed behavior |
| Q-D7-18 | PASS | B runbook order: fix matched check first |
| Q-D7-19 | PASS | B creds, perms, throttling, contract order |
| Q-D7-20 | PASS | B routing first per runbook cost order |
| Q-D7-21 | PASS | B retrieval first, reindex is prime suspect |
| Q-D7-22 | PASS | Select TWO A,B: plan checkpoint + run trace for recovery |
| Q-D7-23 | PASS | Select TWO A,B: symptom map + owner/escalation in runbook |
| Q-D7-24 | PASS | B page architect, update runbook post-incident |
| Q-D7-25 | PASS | B runbook updated after every incident |

### qb-mixed.md (Q-M-01 .. Q-M-50)

| ID | Verdict | Note |
|---|---|---|
| Q-M-01 | PASS | B fork + gate, hospital-claims variant of D1 pattern |
| Q-M-02 | PASS | B human review after model, before public alert, perimeter DB as check source |
| Q-M-03 | PASS | Select TWO B,C: agentic assessment + deterministic publish |
| Q-M-04 | PASS | B contract names arbiter with disagree rule |
| Q-M-05 | PASS | B fan-out independent, fan-in, pushback after clearance, D parallelizes a dependency (wrong) |
| Q-M-06 | PASS | B net monthly value, error rate unchanged so no error term, math: 60kx$0.92-$400 |
| Q-M-07 | PASS | B POS ledger minus deliveries in code, vendor texts untrusted |
| Q-M-08 | PASS | Select TWO A,B: fan-out per turbine + critique pattern |
| Q-M-09 | PASS | B Fast for FAQ, stronger for troubleshooting + citation floor |
| Q-M-10 | PASS | B code filter + output check, prompt line insufficient |
| Q-M-11 | PASS | Select TWO A,B: rejection examples + schema |
| Q-M-12 | PASS | B JIT retrieval + compaction + dedupe |
| Q-M-13 | PASS | B prefix stability + break-even decides caching |
| Q-M-14 | PASS | B regression suite before traffic moves, version change |
| Q-M-15 | FIXED | FIXED: Select THREE A,B,C (was Select TWO A,B), dilution is a named fault per lesson-D2-4 |
| Q-M-16 | PASS | B remove overlapping + delete tool, logs are observability |
| Q-M-17 | PASS | B user claim is not authZ, check identity in code |
| Q-M-18 | PASS | Select TWO C,D: rerank 1.8s + reasoning 2.2s are the two biggest stages |
| Q-M-19 | PASS | B one run id across hops, reconstructability |
| Q-M-20 | PASS | B chunk by structure (agenda item / district tile) + metadata |
| Q-M-21 | PASS | B live inventory behind tool call, index for stable policy |
| Q-M-22 | PASS | Select TWO A,B: MCP for shared multi-lang, direct for single pair |
| Q-M-23 | PASS | B progressive discovery, tokens bind, SLA loose |
| Q-M-24 | PASS | B authZ in code before tool runs |
| Q-M-25 | PASS | B grounding/citation checks stage absent |
| Q-M-26 | PASS | Select TWO A,B: groundedness + subgroup fairness for regulated hiring |
| Q-M-27 | PASS | B held-out set + judge calibration |
| Q-M-28 | PASS | B 2800 sessions cannot resolve 1% lift, offline eval instead |
| Q-M-29 | PASS | B model layer failed (chunk arrived, model misstated), fix prompt/model/verify |
| Q-M-30 | PASS | Select TWO A,B: cache prefix + tier routing, C drops the grounding the floor needs |
| Q-M-31 | PASS | B drift detection + owner + regression suite |
| Q-M-32 | PASS | B adversarial drawer absent |
| Q-M-33 | PASS | B context growth, fix scoping/compaction/dedupe |
| Q-M-34 | PASS | A dosage check fails closed on ambiguity |
| Q-M-35 | PASS | Select TWO A,B: indirect injection + excessive agency ($50k no gate) |
| Q-M-36 | PASS | B pre-action approval, irreversible demolition |
| Q-M-37 | PASS | B requirement-control-owner-evidence-cadence chain |
| Q-M-38 | PASS | Select TWO A,B: per-subgroup metrics + audit data source |
| Q-M-39 | PASS | A code screening for PII/self-harm before model |
| Q-M-40 | PASS | B supply-chain risk, pin + scope + review updates |
| Q-M-41 | PASS | B adjectives to measurable requirements first |
| Q-M-42 | PASS | B audience-adapted messages (CFO vs security) |
| Q-M-43 | PASS | Select TWO A,B: no fixed promise + triggers, D/E dishonest |
| Q-M-44 | PASS | B ADR answers the why |
| Q-M-45 | PASS | B no substituting later-phase work for discovery |
| Q-M-46 | PASS | B RAG easier to reverse than fine-tuning |
| Q-M-47 | PASS | B enforceable permissions, CLAUDE.md is guidance |
| Q-M-48 | PASS | Select TWO A,B: ran tests + inspected, no secrets |
| Q-M-49 | PASS | B runbook cost branch: routing, context, caching |
| Q-M-50 | PASS | B scope subagent read-only, main agent keeps writes |

### mocks.md Mock 1 (M1-Q01 .. M1-Q63)

| ID | Verdict | Note |
|---|---|---|
| M1-Q01 | PASS | B fork + gate, quota filing |
| M1-Q02 | PASS | C constraint into design first |
| M1-Q03 | PASS | A,C trust boundaries: untrusted input + EHR write |
| M1-Q04 | PASS | B verification after scoring, before letter |
| M1-Q05 | PASS | C hybrid: deterministic + routed agent for 8% |
| M1-Q06 | PASS | B agentic loop, step cap, no source list |
| M1-Q07 | PASS | B disagree rule in contract |
| M1-Q08 | PASS | A,D parallel tasks, B/C/E violate dependencies |
| M1-Q09 | PASS | B critique pattern vs brand guide |
| M1-Q10 | PASS | B net $49,000, math verified, errors unchanged |
| M1-Q11 | PASS | B net value answers finance |
| M1-Q12 | PASS | B Fast logistics + stronger merit + floor |
| M1-Q13 | PASS | B regression before cutover, deprecation |
| M1-Q14 | PASS | B,C retrieval filter + output check |
| M1-Q15 | PASS | B discount cap in code |
| M1-Q16 | PASS | A few-shot edge cases + schema |
| M1-Q17 | PASS | A,C growth + dilution (no duplication evidence, Q-M-15 done right) |
| M1-Q18 | PASS | B compaction + JIT |
| M1-Q19 | PASS | B caching iff stable prefix + break-even |
| M1-Q20 | PASS | B remove delete_booking, logging is not removal |
| M1-Q21 | PASS | A,B remove overlap + mass_email |
| M1-Q22 | PASS | B tenant claim is not authZ |
| M1-Q23 | PASS | B approval in code before export |
| M1-Q24 | PASS | C,D rerank 2.1s + model 2.4s dominate |
| M1-Q25 | PASS | B one run id across hops |
| M1-Q26 | PASS | B rerank then assembly then generation |
| M1-Q27 | PASS | B grounding/citation checks absent |
| M1-Q28 | PASS | ATTACKED: A (keyword) weaker than B given synonym hint, B strictly dominates. PASS |
| M1-Q29 | PASS | B MCP server for 3 teams 2 langs |
| M1-Q30 | PASS | B move to stable typed API |
| M1-Q31 | PASS | A,B 50 tools + loose SLA favor discovery |
| M1-Q32 | PASS | B groundedness primary for trust |
| M1-Q33 | PASS | B adjectives to numbers: $0.04/chat verified |
| M1-Q34 | PASS | B red regression drawer blocks ship |
| M1-Q35 | PASS | A,B adversarial + edge drawers |
| M1-Q36 | PASS | B falsifiable hypothesis + metric + assignment |
| M1-Q37 | PASS | B prompt layer: schema removal |
| M1-Q38 | PASS | B,C unvetted mirror + timing point at data |
| M1-Q39 | PASS | B cache stable 4k prefix |
| M1-Q40 | PASS | B SLA on p95 not p50 |
| M1-Q41 | PASS | B alert + owner + runbook |
| M1-Q42 | PASS | A,B purchase gate + email scope fail closed |
| M1-Q43 | PASS | B sandbox for generated scripts |
| M1-Q44 | PASS | B indirect injection, structural fix |
| M1-Q45 | PASS | A,B tool abuse + data exposure |
| M1-Q46 | PASS | B pre-action approval, binding signature |
| M1-Q47 | PASS | B sampled review + audit log, low stakes reversible |
| M1-Q48 | PASS | A,B owner + cadence complete chain |
| M1-Q49 | PASS | B retention with owner/evidence/cadence |
| M1-Q50 | PASS | B traceability + per-group fairness |
| M1-Q51 | PASS | B measurable requirements first |
| M1-Q52 | PASS | A,B volume + compliance as open assumptions |
| M1-Q53 | PASS | B legal: compliance/residency/risk/evidence |
| M1-Q54 | PASS | B reversal/migration cost for 40M vectors |
| M1-Q55 | PASS | A,B measured quality + triggers |
| M1-Q56 | PASS | A production cost forecast before rollout |
| M1-Q57 | PASS | B ADR review criteria trigger re-eval |
| M1-Q58 | PASS | B successor-operable docs |
| M1-Q59 | PASS | A,B ops can run + suite green |
| M1-Q60 | PASS | B deny rule on deploy script |
| M1-Q61 | PASS | B org-managed spend guardrails |
| M1-Q62 | PASS | B run tests + inspect + no secrets |
| M1-Q63 | PASS | B runbook quality branch: prompt/model/retrieval drift |

### mocks.md Mock 2 (M2-Q01 .. M2-Q63)

| ID | Verdict | Note |
|---|---|---|
| M2-Q01 | PASS | B fork: routine deterministic + gate |
| M2-Q02 | PASS | B budget rule into design first |
| M2-Q03 | PASS | A verification after ranking, lightweight (reversible invite) |
| M2-Q04 | PASS | A,B trust boundaries: chat input + fraud-model-to-transfer |
| M2-Q05 | PASS | B hybrid for 10% ambiguous |
| M2-Q06 | PASS | B augmented single call (95% one retrieval + judgment) |
| M2-Q07 | PASS | B disagree rule at merge |
| M2-Q08 | PASS | B fan-out three specialists + merge with disagree rule |
| M2-Q09 | PASS | A,B fan-out + validation/reconciliation |
| M2-Q10 | PASS | B net monthly value structure |
| M2-Q11 | PASS | B net: $4k/mo fraud risk vs cost saved, math verified |
| M2-Q12 | PASS | B Fast lookups + stronger itineraries + floor |
| M2-Q13 | PASS | PASS (priority): B router misclassification unique, weak distractors noted |
| M2-Q14 | PASS | B retrieval filter + output check |
| M2-Q15 | PASS | A,B discount gate in code + public catalog |
| M2-Q16 | PASS | A rejection examples + schema |
| M2-Q17 | PASS | B JIT + compaction |
| M2-Q18 | PASS | A,B growth (catalog) + duplication (policy 4x) |
| M2-Q19 | PASS | A hit rate vs break-even with weekly resets |
| M2-Q20 | PASS | B remove overlapping refund tool |
| M2-Q21 | PASS | A,B remove write_policy + delete_employee |
| M2-Q22 | PASS | B dropdown is user input, not authZ |
| M2-Q23 | PASS | B per-team credentials for attribution |
| M2-Q24 | PASS | B OCR 2.5s of 4.5s first |
| M2-Q25 | PASS | B propagate run id through queue |
| M2-Q26 | PASS | A,B grounding + citation checks after generation |
| M2-Q27 | PASS | B structure-aware chunking |
| M2-Q28 | PASS | B live positions behind tool call |
| M2-Q29 | PASS | B direct API, one consumer |
| M2-Q30 | PASS | A,B MCP for shared + CLI wrapper for one-off |
| M2-Q31 | PASS | B monolithic, 6 tools + 800ms SLA |
| M2-Q32 | PASS | B recall on vuln classes primary |
| M2-Q33 | PASS | B adequacy 4/5 with sample + agreement defined |
| M2-Q34 | PASS | B calibrate judge vs human labels |
| M2-Q35 | PASS | A,B edge + adversarial drawers |
| M2-Q36 | PASS | B consistent per-user assignment |
| M2-Q37 | PASS | B prompt layer: instruction removed |
| M2-Q38 | PASS | A,B truncated feed + timing match |
| M2-Q39 | PASS | B JIT section retrieval |
| M2-Q40 | PASS | A tier routing by difficulty |
| M2-Q41 | PASS | B stale eval drawers refreshed |
| M2-Q42 | PASS | B fail closed on ambiguous recipients |
| M2-Q43 | PASS | A,B input screening + sandboxing |
| M2-Q44 | PASS | B excessive agency: scope run_sql read-only |
| M2-Q45 | PASS | A,B injection + excessive agency |
| M2-Q46 | PASS | B post-action sampled, reversible low-stakes |
| M2-Q47 | PASS | B pre-action approval, ER triage |
| M2-Q48 | PASS | B evidence chain for regulator |
| M2-Q49 | PASS | A,B consent gate + minimization |
| M2-Q50 | PASS | B subgroup evaluation per school |
| M2-Q51 | PASS | B measurable requirements first |
| M2-Q52 | PASS | A,B feed reliability + compliance reviewer as open assumptions |
| M2-Q53 | PASS | B engineering: benefit/cost/risk/reversal/ops burden |
| M2-Q54 | PASS | B CEO: business framing |
| M2-Q55 | PASS | A,B measured pilots + triggers |
| M2-Q56 | PASS | B gameable metric, tie to outcome |
| M2-Q57 | PASS | B ADR review criteria trigger re-eval |
| M2-Q58 | PASS | B ADR resolves memory dispute |
| M2-Q59 | PASS | A,B owners + runbook for readiness |
| M2-Q60 | PASS | B deny + redact hooks in shared settings |
| M2-Q61 | PASS | B managed policies for secrets, project defaults for hooks |
| M2-Q62 | PASS | B inspect results, green on weak tests proves little |
| M2-Q63 | PASS | B creds/perms/throttling after migration |

### mocks.md Mock 3 (M3-Q01 .. M3-Q63)

| ID | Verdict | Note |
|---|---|---|
| M3-Q01 | PASS | B fork + gate, baggage claims |
| M3-Q02 | PASS | B rule into design first, auto-block |
| M3-Q03 | PASS | B strongest verification before publish + human sign-off |
| M3-Q04 | PASS | A,B trust boundaries: web input + HR write |
| M3-Q05 | PASS | B deterministic + routed agent for 5% |
| M3-Q06 | PASS | B deterministic workflow, fixed checklist |
| M3-Q07 | PASS | B disagree rule: reason codes + rework path |
| M3-Q08 | PASS | B assessment then fan-out shelter+routing |
| M3-Q09 | PASS | A,B both orderings valid (parallel or strict sequence) |
| M3-Q10 | PASS | B first-year net $76,600, math verified |
| M3-Q11 | PASS | B motion without value, batch latency |
| M3-Q12 | PASS | B Fast lookups + stronger disputes + floor |
| M3-Q13 | PASS | B uncalibrated confidence trigger, use measured check |
| M3-Q14 | PASS | B identity + code gate + output check |
| M3-Q15 | PASS | A,B ad exclusion at index + age check at output |
| M3-Q16 | PASS | A few-shot dual-category + tie-break + schema |
| M3-Q17 | PASS | B JIT papers |
| M3-Q18 | PASS | A,B growth (transcripts) + duplication (action items 3x) |
| M3-Q19 | PASS | B monthly resets bound caching win |
| M3-Q20 | PASS | B limit export tool to 100 rows in schema |
| M3-Q21 | PASS | A,B remove dup tweet tools + drop_database |
| M3-Q22 | PASS | B authN without authZ, guardian roster check |
| M3-Q23 | PASS | B confused deputy, per-user delegation |
| M3-Q24 | PASS | B detect+classify 3.9 of 4.4s first |
| M3-Q25 | PASS | B per-hop latency + run id |
| M3-Q26 | PASS | B parsing/chunking: phantom page metadata |
| M3-Q27 | PASS | A,B grounding + citation checks missing |
| M3-Q28 | PASS | B live prices behind tool call |
| M3-Q29 | PASS | B direct SDK, one consumer |
| M3-Q30 | PASS | A,B direct for single + CLI wrapper for CLI-only |
| M3-Q31 | PASS | B progressive discovery, 40 tools + 15s SLA |
| M3-Q32 | PASS | B recall>=95% + FPR<=2% on held-out |
| M3-Q33 | FIXED | FIXED (priority): rebuilt around missing owner link, old key contradicted lesson chain |
| M3-Q34 | PASS | B judge uncalibrated at 60%, do not trust |
| M3-Q35 | PASS | A,B edge + adversarial drawers |
| M3-Q36 | PASS | B shadow first for risky refund change |
| M3-Q37 | PASS | B model version changed, pin + regression |
| M3-Q38 | PASS | A,B boost authoritative ranking + source-type metadata |
| M3-Q39 | PASS | B incremental embedding (2% change) |
| M3-Q40 | PASS | B tail not median, p99 14s |
| M3-Q41 | PASS | B business-outcome watch with line/window/owner |
| M3-Q42 | PASS | B pre-action approval + fail-closed age check |
| M3-Q43 | PASS | A,B sandbox + allow-list/screening |
| M3-Q44 | PASS | B capability bloat: prune to least privilege |
| M3-Q45 | PASS | A,B CEO credentials: excessive agency + exposure |
| M3-Q46 | PASS | B post-action sampled, deletable in seconds |
| M3-Q47 | PASS | B pre-action approval, termination letters |
| M3-Q48 | PASS | B compliance chain for logs |
| M3-Q49 | PASS | A,B per-state consent + evidence chain |
| M3-Q50 | PASS | B subgroup evaluation, aggregate hides impact |
| M3-Q51 | PASS | B measurable requirements first |
| M3-Q52 | PASS | A,B appeal process + retention as open assumptions |
| M3-Q53 | PASS | B ops: debuggability/traces/on-call/rollback |
| M3-Q54 | PASS | B board: return/cost/risks/reversal |
| M3-Q55 | PASS | A,B note sample + per-class quality |
| M3-Q56 | PASS | B measurable terms replace best-effort |
| M3-Q57 | PASS | B ADR review criteria trigger re-eval |
| M3-Q58 | PASS | B ADR answers the why |
| M3-Q59 | PASS | A,B eval drawers + watches + runbook |
| M3-Q60 | PASS | B enforceable permissions + scoped subagents |
| M3-Q61 | PASS | B light guidance, nothing to protect |
| M3-Q62 | PASS | B verification bar met: review + staging + inspect + secrets |
| M3-Q63 | PASS | B latency branch: context/dependency drift |

### mocks.md Mock 4 (M4-Q01 .. M4-Q63)

| ID | Verdict | Note |
|---|---|---|
| M4-Q01 | PASS | B fork + gate, pharmacy refills |
| M4-Q02 | PASS | B rule into design first, advising |
| M4-Q03 | PASS | A verification after scoring + sampled review |
| M4-Q04 | PASS | A,B trust boundaries: chat input + sentiment-to-ticket |
| M4-Q05 | PASS | B deterministic + routed agent for 3% |
| M4-Q06 | PASS | B classifier for fixed categories (not RAG) |
| M4-Q07 | PASS | B disagree rule, silent default |
| M4-Q08 | PASS | B venue+speakers parallel, sponsors after venue |
| M4-Q09 | PASS | A,B fan-out + critique before merge |
| M4-Q10 | PASS | B monthly net $4,146, math verified |
| M4-Q11 | PASS | B net value: 2% gain vs 10x cost |
| M4-Q12 | PASS | B Fast logistics + stronger eligibility + floor |
| M4-Q13 | PASS | B cost without measurement, route by evals |
| M4-Q14 | PASS | B code classifier on outputs + adversarial test |
| M4-Q15 | PASS | A,B risk gate in code + free balance inquiries |
| M4-Q16 | PASS | A few-shot multi-page + schema |
| M4-Q17 | PASS | B JIT chapter retrieval |
| M4-Q18 | PASS | A,B growth + duplication (notice 5x) |
| M4-Q19 | PASS | B keep caching, 92% hit rate stable prefix |
| M4-Q20 | PASS | B remove delete_event, might-be-useful is not a task |
| M4-Q21 | PASS | A,B remove dup balance + wire_transfer |
| M4-Q22 | PASS | B user-editable profile is a claim |
| M4-Q23 | PASS | B personal creds in config, service identity |
| M4-Q24 | PASS | B vector search 2.3s of 4.0s first |
| M4-Q25 | PASS | B per-hop timings in trace |
| M4-Q26 | PASS | B model/generation layer, chunks great but invented |
| M4-Q27 | PASS | A,B grounding + citation checks |
| M4-Q28 | PASS | B live tracking behind tool call |
| M4-Q29 | PASS | B MCP server for 4 teams 3 langs |
| M4-Q30 | PASS | A,B MCP/shared for logging + CLI wrapper for script |
| M4-Q31 | PASS | B monolithic, 5 tools + 1s SLA |
| M4-Q32 | PASS | B groundedness primary |
| M4-Q33 | PASS | B partially: sampling method/size/cadence or gaming, lesson-grounded (D4.2 + gaming §7) |
| M4-Q34 | PASS | B holdout set, training data measures memorization |
| M4-Q35 | PASS | A,B other languages + malformed drawers |
| M4-Q36 | PASS | B day-of-week confound, consistent per-user |
| M4-Q37 | PASS | B embedding change = retrieval layer |
| M4-Q38 | PASS | A,B 30% dropped + timing match convict index |
| M4-Q39 | PASS | B rerank top 15 only, top 5 always win |
| M4-Q40 | PASS | B truncation broke floor, hold floors |
| M4-Q41 | PASS | B safety watch for toxicity |
| M4-Q42 | PASS | B code check before send, recipient match |
| M4-Q43 | PASS | A,B input screening + payment gate |
| M4-Q44 | PASS | B secrets in prompts, secrets manager |
| M4-Q45 | PASS | A,B injection via DMs + data exposure |
| M4-Q46 | PASS | B pre-action approval, liability |
| M4-Q47 | PASS | PASS (priority): pre-action approval, proportionate review |
| M4-Q48 | PASS | B residency violation, EU region + evidence |
| M4-Q49 | PASS | A,B model inventory + validation evidence |
| M4-Q50 | PASS | B subgroup evaluation for elderly |
| M4-Q51 | PASS | B measurable requirements first |
| M4-Q52 | PASS | A,B liability owner + retention as open assumptions |
| M4-Q53 | PASS | B security axes for multi-agent |
| M4-Q54 | PASS | B product: impact framing |
| M4-Q55 | PASS | A,B staged rollout + triggers/rollback |
| M4-Q56 | PASS | B define insights measurably |
| M4-Q57 | PASS | B ADR review criteria, pricing change |
| M4-Q58 | PASS | B ADR answers the why |
| M4-Q59 | PASS | A,B lifecycle owners + runbook |
| M4-Q60 | PASS | B managed policies org-wide |
| M4-Q61 | PASS | B project defaults for team hooks |
| M4-Q62 | PASS | B verify AI output before acting |
| M4-Q63 | PASS | B creds/perms first after change |

### diagnostic-key.md (16 keys)

| ID | Verdict | Note |
|---|---|---|
| DG-Q01 | PASS | Adjectives lack acceptance criteria, first question targets the measurable note |
| DG-Q02 | PASS | Cap math verified: $2,000/50,000=$0.04, conversion before feasibility |
| DG-Q03 | PASS | Impact x reversibility, auto-sent refunds need stronger review |
| DG-Q04 | PASS | ADR: decision+date, alternatives+rejections, owner |
| DG-Q05 | PASS | 41,000 tokens, cut the 40k input side first |
| DG-Q06 | PASS | Sampling model, code grounding check for dates |
| DG-Q07 | PASS | Monthly updates decide: retrieval over fine-tuning |
| DG-Q08 | PASS | Indirect injection, structural fix + code gate |
| DG-Q09 | PASS | Idempotency key, retry in caller, dedupe on server |
| DG-Q10 | PASS | Caller timeout + service backpressure |
| DG-Q11 | PASS | Logs + metrics + traces, trace links the 14 calls |
| DG-Q12 | PASS | Consistency-availability price, blast radius for deploys |
| DG-Q13 | PASS | UI hiding is not authZ, server-side check |
| DG-Q14 | PASS | Confused deputy, per-user delegated token, narrow scopes |
| DG-Q15 | PASS | Key in prompt + exporter leak, secrets manager |
| DG-Q16 | PASS | Tenant isolation, audit record who/what/when/decision |

## Totals (final)

The 4 priority-flagged items are included in the 477 (Q-M-15 in qb-mixed,
M2-Q13/M3-Q33/M4-Q47 in mocks), not additional.

- Questions audited: 477 / 477 (qb-D1..D7: 175, qb-mixed: 50, mocks: 252)
- Diagnostic keys audited: 16 / 16
- PASS: 489 (473 questions + 16 diagnostic keys)
- FIXED: 4 (Q-M-15, M3-Q33, Q-D3-07, Q-D5-21)
- REJECTED: 0
- PENDING: 0

## Defect classes found

1. Multi-select over-subscription: more defensible answers than the
   select count allows (Q-M-15: three named faults for Select TWO).
2. Key demands an untaught requirement, contradicting the lesson's own
   text (M3-Q33: "measurement conditions" vs the taught
   requirement-metric-threshold-owner chain).
3. Explanation overstates the result the scenario's own arithmetic
   supports (Q-D3-07: 2.9 - 0.7 = 2.2 s still exceeds the 2 s SLA,
   key survives as best first cut, explanation now honest).
4. Arithmetic inconsistency in scenario numbers (Q-D5-21: group math
   gives 90.4%, scenario said 94%, corrected to 90%, key unaffected).

## Attacks attempted and defeated (no edit needed)

- Q-D4-03: option A (accuracy primary) looked like a third valid
  answer, but lesson-D4-1 §9 states "Budget binds → Cost per
  successful task is the primary." Key B,E lesson-grounded.
- M1-Q28: option A (keyword) looked like a third fit, but option B
  establishes the synonym dimension keyword misses, B strictly
  dominates A. Not equally defensible.
- M2-Q13, M4-Q47: probed for second defensible readings, none found.

## Items rejected

None. No item exhausted 3 fix loops. See rejected-items.md (empty).

## Unresolved items

None. Every audited item has a verdict above. Zero PENDING.
