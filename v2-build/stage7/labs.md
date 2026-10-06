# Labs: nine hands-on exercises

Each lab names its goal, setup, steps, expected observations, and diagnosis practice. Local-first. Bounded-cost where a real API is used. Cleanup documented per lab. Paid API usage is never free: every real-API step carries its cost cap.

:::takeaway
Run the fault, not only the happy path. Each lab breaks one thing on purpose and asks you to name the layer.
:::

## Lab 1: model and API capability verification

Goal: verify that a model routing decision holds on measured capability, not on marketing claims.

Setup: local. A stub model server that returns canned responses per model id. No API key. No cost. Cleanup: kill the stub process. Delete the stub script.

Steps:
1. Start the stub with three model ids: cheap, balanced, flagship.
2. Send the same 20-case classification task to each id through the stub.
3. Record per-model accuracy, latency, and token usage from the stub logs.
4. Write the routing rule: which task class goes to which model, and the quality floor.

Expected observations: the flagship wins on hard cases. The cheap model wins on cost per easy case. The routing rule names the floor: below it, escalate.

Diagnosis practice: swap two stub responses so the cheap model secretly returns flagship-quality answers. Re-run. The router misroutes. The lesson: verify the model behind the id, not the id. Version changes are production changes (V2-D2.1).

## Lab 2: prompt and context comparison

Goal: compare two prompt variants on one fixed task and pick the winner on measured scores, not on prose quality.

Setup: local. A fixed 30-case task set. Token counter in code. Optional real-API variant: cap at 60 calls, Balanced tier, about $0.25 total. Document the spend. Cleanup: none. No state persists.

Steps:
1. Write variant A: zero-shot with a short instruction. Variant B: few-shot with two examples plus one rejection example.
2. Run both over the 30 cases against the stub (or the capped real API).
3. Score with a code check: exact match on the label.
4. Compare accuracy, input tokens per call, and output tokens per call.

Expected observations: variant B usually wins on accuracy and costs more tokens. The decision is a trade: accuracy gain versus token cost per case.

Diagnosis practice: add a third variant C with ten examples. Accuracy stalls while tokens triple. The lesson: the simplest technique that passes the evals wins (V2-D2.3). More examples are not always better.

## Lab 3: prompt caching

Goal: prove the prefix rule with measurements: stable first, variable last.

Setup: local-first. A prefix-order rig that computes the cache key from the prompt assembly order. Optional real-API variant: 200 calls, cap $1. Watch the hit-rate metric the provider reports. Cleanup: none. The provider-side cache expires on its TTL.

Steps:
1. Assemble variant A: 8,000-token system prompt first, user message last.
2. Assemble variant B: user message first, system prompt last.
3. Run 100 identical-prefix calls per variant through the rig (or the capped API).
4. Record the hit rate per variant.

Expected observations: variant A hits near 100% after the first write. Variant B hits near 0%: the variable lead breaks the prefix every call. The V2-D2.5 toy math predicts the bill: $170 per day uncached versus $31.76 cached at 10,000 calls per day.

Diagnosis practice: variant A shows a 2% hit rate. Inspect the assembly code: a timestamp is prepended to the system prompt. Remove it. The hit rate recovers. The lesson: one changing token at the front means zero hits.

## Lab 4: tool calling with safe retries

Goal: prove that the idempotency key, not the retry, makes a retried charge safe.

Setup: local. The simulated flaky ledger from artifact A12. No network. No charges. Cleanup: none. The ledger is in memory.

Steps:
1. Run the ledger with 2 flakes then success, key = charge id. Confirm one charge after 3 attempts.
2. Deliver the same charge twice (network duplicate). Confirm one distinct charge.
3. Replace the business key with a fresh random id per attempt. Re-run. Count the charges.
4. Set the ledger to always fail. Confirm the attempt cap fires with zero charges.

Expected observations: step 1 charges once. Step 2 still one charge. Step 3 charges twice: the random key dedupes nothing. Step 4 raises cleanly. Real output from the local run:

```
run1: {'status': 'charged', 'charged_cents': 4599} attempts: 3 backend calls: 3
run2 duplicate: {'status': 'duplicate', 'charged_cents': 4599} total distinct charges: 1
run3: raised after 3 backend calls. Distinct charges: 0
```

Diagnosis practice: a teammate's retry loop double-charges in staging. Read the code: the key is `uuid4()` per attempt. Name the layer: the key, not the retry count. Fix: key = charge id.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">The key makes the retry safe</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Flaky ledger: 2 flakes, then success. Same 3 attempts, two key choices.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE: RANDOM KEY PER ATTEMPT</text>
<rect x="44" y="144" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="169" font-size="14" text-anchor="middle" fill="#1B2838">2 distinct charges</text>
<text x="44" y="208" font-size="13" fill="#5C6B7A">3 attempts, 3 backend calls.</text>
<text x="44" y="228" font-size="13" fill="#5C6B7A">No key matches. No dedupe.</text>
<text x="44" y="248" font-size="13" fill="#5C6B7A">Double charge.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER: KEY = CHARGE ID</text>
<rect x="420" y="144" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="169" font-size="14" text-anchor="middle" fill="#1B2838">1 distinct charge</text>
<text x="420" y="208" font-size="13" fill="#5C6B7A">3 attempts, 3 backend calls.</text>
<text x="420" y="228" font-size="13" fill="#5C6B7A">Duplicate delivery deduped.</text>
<text x="420" y="248" font-size="13" fill="#5C6B7A">One charge. Cap still fires.</text>
<defs><marker id="ml4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#ml4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">fix the key</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Retries do not cause double charges. Bad keys do.</text>
</svg>
<figcaption>Shell 4. A business key moves the retry from two charges to one. Source: original toy.</figcaption>
</figure>

## Lab 5: MCP with correct authorization

Goal: run an MCP server over local stdio, then prove the authZ rule changes with transport.

Setup: local. A stdio MCP server with one tool and a stub authZ check. No network. Cleanup: kill the server process.

Steps:
1. Start the server on stdio. List tools from a test host. Call the tool. Confirm the typed result.
2. Send a call with a forbidden action. Confirm the authZ deny and the audit record.
3. Reconfigure the same server for network transport without adding OAuth. Run the V2-D3.2 checklist against it.
4. Add the OAuth requirement to the checklist and document the gap.

Expected observations: stdio inherits trust and works with no tokens. The network variant fails the checklist: remote server over the network means OAuth is non-negotiable. The transport changed the verdict.

Diagnosis practice: a teammate exposes the stdio server on a TCP port "for convenience." Name the new threat: unauthenticated network callers. Fix: OAuth or keep it on stdio.

## Lab 6: RAG and retrieval diagnosis

Goal: diagnose a wrong answer at the right layer: retrieval or model.

Setup: local. The 20-document keyword retriever from the lab toy. No network. Cleanup: none. All in memory.

Steps:
1. Run the 3-query baseline. Confirm recall@1 = 3/3.
2. Inject the chunk-split fault: key terms land in different chunks. Re-run. Confirm recall@1 = 2/3 and the wrong chunk wins at rank 1.
3. Run the paraphrase query. Confirm the keyword index returns the wrong top-1.
4. Re-chunk at sentence boundaries. Confirm recall@1 = 3/3.

Expected observations: the split chunk still contains words, so a naive glance says the data is there. Rank 1 tells the truth. The paraphrase failure names the index type as the layer, not the chunker. Real output from the local run:

```
baseline recall@1: 3/3
bad chunk split, recall@1: 2/3 | top-1 for 'damaged item refund window': ['pol-001b']
paraphrase top-1: ['pol-001'] (want pol-002)
re-chunked recall@1: 3/3
```

Diagnosis practice: production shows right-chunk-missing on paraphrased queries only. The fix is semantic retrieval in the hybrid mix (V2-D3.6), not a bigger model. Upgrading the model would cost more per call forever and fix nothing.

## Lab 7: evaluation and regression gates

Goal: build the smallest runner that blocks a bad change.

Setup: local. A 20-case dataset across three drawers: representative, edge, regression. A toy system function. Cleanup: none.

Steps:
1. Run the runner on the current system. Record per-drawer scores as the baseline.
2. Introduce a one-line bug in the system function.
3. Re-run. Confirm the regression drawer catches it and the runner reports red.
4. Fix the bug. Confirm green. Add the bug's case to the regression drawer.

Expected observations: the aggregate barely moves on a one-line bug. The regression drawer names it. The lesson: per-drawer scores, not the aggregate, block the ship.

Diagnosis practice: the runner is green but production is red. Inspect the drawers: the edge drawer is six months old. Refresh it from recent production failures. The lesson: a stale suite is theater (V2-D4.6).

## Lab 8: approval enforcement

Goal: prove that illegal approval transitions are rejected by the machine, not by convention.

Setup: local. The approval state machine from artifact A13. No network. Cleanup: none.

Steps:
1. Run the seven checks. Confirm all pass.
2. Attempt execute-from-requested. Confirm the raise.
3. Attempt approve-from-expired. Confirm the raise.
4. Attempt double approve. Confirm the raise.

Expected observations: all illegal moves raise with a named error. The state never leaves a legal path. Real output from the local run:

```
approval FSM checks: [True, True, True, True, True, True, True] -> ALL PASS
```

Diagnosis practice: staging shows an executed action with no approve event. Read the tool code: it never checks the machine state. Name the layer: enforcement at the tool (A13 security boundary). The machine is decorative until the tool consults it.

## Lab 9: Claude Code team configuration

Goal: write a team config where the deny rules are tested, not assumed.

Setup: local. A sample `.claude/settings.json` plus a matcher test script. No Claude Code install needed for the test. Cleanup: delete the sample files.

Steps:
1. Write the config. Deny `Read(.env)`, `Bash(rm -rf:*)`, `Bash(sudo:*)`. Ask on `Bash(deploy:*)`. Add a PostToolUse lint hook on edits.
2. Write the matcher test: feed 10 command strings, assert each lands in deny, ask, or allow.
3. Add a personal override file `settings.local.json` with one exception. Assert the shared file is unchanged.
4. Document which entries are guidance (CLAUDE.md) and which are enforcement (this file).

Expected observations: the matcher test catches a miswritten glob before any developer does. The override test proves personal exceptions stay out of git.

Diagnosis practice: a developer reports the deny rule "does not work" on `Read(./.env)`. The matcher test shows the glob `Read(.env)` does not match the `./` prefix. Fix the pattern, re-run the test. The lesson: untested deny rules are wishes.

:::takeaway
Nine labs, four with locally executed toys and real output. The rest run against stubs and capped APIs with the spend written down before the first call.
:::
