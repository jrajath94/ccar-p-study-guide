# Lesson 7-1A: software and distributed systems

## 1. Problem this lesson solves

A model call looks like a function call. It is a network call to a busy
stranger. It can fail, hang, or run twice. Code that treats it as local
breaks in production at 2 a.m.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">A function call that lies</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Same code shape. Different failure contract.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="48" rx="8" fill="#E7F1F8"/>
<text x="172" y="177" font-size="14" text-anchor="middle" fill="#1B2838">charge(card) returns</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Local logic. Always answers.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Never twice. Never silent.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="548" y="177" font-size="14" text-anchor="middle" fill="#1B2838">charge(card) may...</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Fail. Hang 90 s. Run twice.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">Network call to a stranger.</text>
<defs><marker id="m71a1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m71a1)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">cross the network</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Every tool call is a remote call. Design it like one.</text>
</svg>
<figcaption>Shell 3. The same call shape gains a failure contract. Source: original toy.</figcaption>
</figure>

## 2. Prerequisites

Lesson 7-4A gives the latency budget: SLOs turn "fast" into a number.
Lesson 7-3A gives the cost fact: model calls spend tokens and take seconds.

| Foundation | What it gives this lesson |
|---|---|
| §7.4 chain | The retry budget is 10 seconds at p95 |
| §7.3 cost | Each retry spends tokens again |

## 3. Mental model

Every remote call can fail, stall, or duplicate. Design for the bad day,
not the demo. Four tools cover most of it: timeouts cap the wait, retries
repeat the attempt, idempotency keys make repeats safe, backoff spaces the
repeats.

<figure class="fig">
<svg viewBox="0 0 720 380" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="380" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Hope is not a retry policy</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">One bare arrow becomes four named tools. Each tool has one job.</text>
<rect x="24" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="96" height="40" rx="999" fill="#E6E2DA"/>
<text x="92" y="173" font-size="13" text-anchor="middle" fill="#1B2838">app</text>
<rect x="180" y="148" width="96" height="40" rx="8" fill="#E7F1F8"/>
<text x="228" y="173" font-size="13" text-anchor="middle" fill="#1B2838">pay API</text>
<line x1="140" y1="168" x2="176" y2="168" stroke="#1B2838" stroke-width="2"/>
<text x="44" y="228" font-size="14" fill="#5C6B7A">One arrow. No timeout.</text>
<text x="44" y="252" font-size="14" fill="#5C6B7A">No retry. No key.</text>
<rect x="400" y="96" width="296" height="196" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="412" y="144" width="128" height="32" rx="999" fill="#F6E7A8"/>
<text x="476" y="165" font-size="13" text-anchor="middle" fill="#1B2838">timeout 4 s</text>
<rect x="412" y="184" width="128" height="32" rx="999" fill="#E7F4EF"/>
<text x="476" y="205" font-size="13" text-anchor="middle" fill="#1B2838">retry x 1</text>
<rect x="548" y="144" width="128" height="32" rx="999" fill="#E7F1F8"/>
<text x="612" y="165" font-size="13" text-anchor="middle" fill="#1B2838">idempotency key</text>
<rect x="548" y="184" width="128" height="32" rx="999" fill="#F4E6D4"/>
<text x="612" y="205" font-size="13" text-anchor="middle" fill="#1B2838">backoff 1 s, 2 s</text>
<text x="412" y="244" font-size="13" fill="#5C6B7A">Each tool owns one failure mode.</text>
<defs><marker id="m71a3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="194" x2="384" y2="194" stroke="#1B2838" stroke-width="2" marker-end="url(#m71a3)"/>
<text x="360" y="178" font-size="13" text-anchor="middle" fill="#1B2838">add the four tools</text>
<text x="24" y="332" font-size="15" fill="#1B2838">Name the tool for each failure. Unnamed failures happen anyway.</text>
</svg>
<figcaption>Shell 3. One bare call becomes four named tools. Source: original toy.</figcaption>
</figure>

## 4. Causal mechanism

Failure is detected by the timeout. The caller retries, not the model.
The idempotency key tells the receiver "this is the same charge, not a new
one." Backoff waits longer between attempts so a sick dependency is not
hammered. The circuit breaker stops all calls when failures pass a line,
then lets one probe through later.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Backoff calms the storm</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Five instant retries hammer a sick server. Spaced retries let it recover.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="148" width="256" height="40" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">fail, retry x 5, now</text>
<text x="44" y="212" font-size="13" fill="#5C6B7A">5 hits in 0 seconds.</text>
<text x="44" y="232" font-size="13" fill="#5C6B7A">Sick server gets sicker.</text>
<text x="44" y="252" font-size="13" fill="#5C6B7A">Thundering herd.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="148" width="256" height="40" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">wait 1 s, 2 s, 4 s</text>
<text x="420" y="212" font-size="13" fill="#5C6B7A">1 + 2 + 4 = 7 s of waits.</text>
<text x="420" y="232" font-size="13" fill="#5C6B7A">Server breathes.</text>
<text x="420" y="252" font-size="13" fill="#5C6B7A">Breaker opens if still sick.</text>
<defs><marker id="m71a4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m71a4)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">space the retries</text>
<text x="24" y="352" font-size="15" fill="#1B2838">Backoff trades a little latency for a lot of mercy.</text>
</svg>
<figcaption>Shell 3. Spaced retries replace the instant retry storm. Source: original toy.</figcaption>
</figure>

:::takeaway
Reliability lives in the caller, not in the model. Timeout, retry, key,
backoff, breaker: five names, five jobs, all in code you own.
:::

## 5. Minimal worked example

Toy: a charge tool, 1,000 charges per day, 2% flaky failures.

No retry: 1,000 x 0.02 = 20 failed charges per day. One retry, with the
assumption that failures are independent: 20 x 0.02 = 0.4 residual failures
per day, times 30 = 12 per month. The retry costs 20 extra calls per day,
which is trivial next to 20 lost charges.

Latency budget: attempt p99 is 3 seconds, timeout is 4 seconds, one retry.
Worst case: 4 + 4 = 8 seconds, which fits the 10-second SLO from lesson
7-4A. The idempotency key is the charge ID: a duplicate delivery with the
same key is one charge, not two.

<figure class="fig">
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="400" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">One retry, keyed, changes the count</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">2% flake, 1,000 charges a day. Independence assumed, stated below.</text>
<rect x="24" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">20 failures / day</text>
<text x="44" y="216" font-size="13" fill="#5C6B7A">1,000 x 0.02 = 20.</text>
<text x="44" y="236" font-size="13" fill="#5C6B7A">No retry. No key.</text>
<text x="44" y="256" font-size="13" fill="#5C6B7A">Blind retry risks double charge.</text>
<rect x="400" y="96" width="296" height="216" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#E7F4EF"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">0.4 failures / day</text>
<text x="420" y="216" font-size="13" fill="#5C6B7A">20 x 0.02 = 0.4. Key = charge ID.</text>
<text x="420" y="236" font-size="13" fill="#5C6B7A">Worst case 4 + 4 = 8 s.</text>
<text x="420" y="256" font-size="13" fill="#5C6B7A">8 s fits the 10 s SLO.</text>
<defs><marker id="m71a5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="204" x2="384" y2="204" stroke="#1B2838" stroke-width="2" marker-end="url(#m71a5)"/>
<text x="360" y="188" font-size="13" text-anchor="middle" fill="#1B2838">retry with key</text>
<text x="24" y="352" font-size="15" fill="#1B2838">The key makes the retry safe. The timeout keeps it inside the SLO.</text>
</svg>
<figcaption>Shell 4. A keyed retry cuts failures fifty-fold inside the latency budget. Source: original toy.</figcaption>
</figure>

### The 10-step best-answer method in action

Note: the canonical §17 text was not in this builder's context. The steps
below reconstruct the standard exam method. The coordinator should align
them with §17.

Mini question: "A checkout agent charges cards through a flaky tool (2%
fail). Double charges are unacceptable. Which design fits? A) Prompt the
model to 'try again on failure.' B) Caller-side retry with the charge ID
as idempotency key. C) Queue the charge and retry for 24 hours."

| Step | Action on this question |
|---|---|
| 1. Read the stem once | Type: design choice under a money constraint |
| 2. Mark the hard constraints | No double charge. 2% flake |
| 3. Predict before reading options | Retry must be safe and keyed |
| 4. Read every option | Do not stop at the first plausible one |
| 5. Delete constraint breakers | A breaks safety: model retries are non-deterministic and unobservable |
| 6. Delete different-problem solvers | C solves durability, not the double-charge. Checkout needs an answer now |
| 7. Compare survivors on cost, risk, reversibility | B bounds latency at 8 seconds. C delays settlement a day |
| 8. Hunt the traps | "The model can retry" confuses who owns reliability |
| 9. Match the decisive constraint | B is the only option with a safe, bounded retry |
| 10. Stress-test the pick | B survives production: the key dedupes, the timeout bounds the wait |

Verdict: B. The decisive constraint is the double charge, and only B
makes the retry safe by construction.

## 6. Product and protocol mapping

| Concept | Where it lives | Exam use |
|---|---|---|
| HTTP plus streaming | Messages API transport, general protocol | V2-D3.7 integration mechanism choice |
| Queues and events | Async agent work, webhooks | V2-D1.2 architecture, V2-D4.6 production monitoring |
| Traces | Request ID across model, tools, retries | V2-D3.4 observability at scale |
| Rollback | Deploy the previous version | V2-D7.1 team configuration |

## 7. Current limitations

Retries do not fix correlated outages: if the region is down, every retry
fails too. Idempotency needs a real business key. A fresh random ID per
attempt dedupes nothing. Backoff adds tail latency. Breakers need tuned
thresholds or they flap open and closed.

<figure class="fig">
<svg viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, 'Source Sans 3', sans-serif">
<rect x="0" y="0" width="720" height="360" fill="#F7F4EE"/>
<text x="24" y="44" font-size="28" font-weight="600" fill="#1B2838">Retries cannot fix a dead region</text>
<text x="24" y="72" font-size="15" fill="#5C6B7A">Retry helps flakes. It cannot help outages. The breaker must open.</text>
<rect x="24" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="44" y="128" font-size="13" font-weight="500" fill="#5C6B7A">BEFORE</text>
<rect x="44" y="144" width="256" height="48" rx="8" fill="#F3D4D8"/>
<text x="172" y="173" font-size="14" text-anchor="middle" fill="#1B2838">3 retries, 0 successes</text>
<text x="44" y="220" font-size="14" fill="#5C6B7A">Region is down.</text>
<text x="44" y="244" font-size="14" fill="#5C6B7A">Every retry fails.</text>
<rect x="400" y="96" width="296" height="176" rx="12" fill="#FFFDF8" stroke="#D9D3C7" stroke-width="1.5"/>
<text x="420" y="128" font-size="13" font-weight="500" fill="#5C6B7A">AFTER</text>
<rect x="420" y="144" width="256" height="48" rx="8" fill="#F6E7A8"/>
<text x="548" y="173" font-size="14" text-anchor="middle" fill="#1B2838">breaker opens</text>
<text x="420" y="220" font-size="14" fill="#5C6B7A">Calls stop at once.</text>
<text x="420" y="244" font-size="14" fill="#5C6B7A">One probe tests recovery.</text>
<defs><marker id="m71a7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#1B2838"/></marker></defs>
<line x1="336" y1="184" x2="384" y2="184" stroke="#1B2838" stroke-width="2" marker-end="url(#m71a7)"/>
<text x="360" y="168" font-size="13" text-anchor="middle" fill="#1B2838">dependency is dead</text>
<text x="24" y="312" font-size="15" fill="#1B2838">Know which failure you face. Flakes get retries. Outages get breakers.</text>
</svg>
<figcaption>Shell 3. The breaker replaces useless retries during an outage. Source: original toy.</figcaption>
</figure>

## 8. Nearest alternatives

| Alternative | Character | When it fits |
|---|---|---|
| Fail fast, human retries | No retry logic | Internal tool, a human is in the loop anyway |
| At-least-once queue plus dedupe | Queue guarantees delivery | Async work, minutes of delay are fine |
| Caller retry plus idempotency key (this lesson) | Bounded and safe | Sync user-facing calls with side effects |

## 9. Decisive scenario constraints

| Constraint | Verdict |
|---|---|
| Money moves or state changes | Caller retry plus idempotency key |
| Read-only call | Simple retry, no key needed |
| User waits on the response | Bound the total: timeout times (retries + 1) fits the SLO |
| Work can wait minutes | Queue instead of sync retry |

## 10. Valid-but-inferior option

"Try again" inside the prompt. Valid: sometimes the model recovers.
Inferior: no timeout, no key, no backoff, no trace. On the toy, the model
retries until it decides to stop: unbounded cost, unbounded latency, and
the double-charge risk stays exactly where it was.

| Option | Why valid | Why inferior on this toy |
|---|---|---|
| Prompt retry | Zero code to write | Unbounded, unobservable, unsafe for money |

## 11. Counterfactual where the alternative wins

Local deterministic function. No network, no flake. Retry machinery is
pure overhead: extra code, extra latency math, nothing to protect.

| Situation | Winner | Why |
|---|---|---|
| Local call, no network | No retry machinery | There is no failure mode to cover |

## 12. Recall prompt

```
Cover the answers. Say each aloud.
1. The retry lives in the ______.
2. The ______ makes a retried charge safe.
3. ______ spaces the attempts.
4. Worst case with 4 s timeout and one retry: ______ s.
Uncover. Fix misses. Repeat once.
```

## 13. Unseen transfer question

```
A clinic books appointments through a flaky scheduling API.
A double booking is worse than a missed booking.
Sketch the retry design. Name the key.
Do not answer yet. The key ships in Stage 8.
```

## 14. Evidence and date

| Claim | Class | Source | Date |
|---|---|---|---|
| Retry, backoff, idempotency, breaker mechanics | General principle | Distributed-systems canon | Long-standing |
| Toy failure arithmetic | Original toy, computed above | This lesson | Oct 6, 2026 |
| Independence of failures | Toy assumption, stated | This lesson | Oct 6, 2026 |
| Exam tests right-layer diagnosis | Official exam scope via secondary summaries | S03, S04 | Sept 2026 |

:::takeaway
The exam asks where the fix belongs. Timeout, retry, key, breaker: the
fix lives in the caller. "The model will retry" is almost always the
distractor.
:::

## Page audit

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Model call is a network call | Looks like a function call | Fails, hangs, duplicates | f01 | SVG | Original |
| u02 | SLO and cost carry over | -- | Prerequisite table | f02 | Table | §7.4, §7.3 |
| u03 | Four tools, four jobs | One bare arrow | Timeout, retry, key, backoff | f03 | SVG | Original |
| u04 | Backoff calms the storm | 5 instant retries | Waits of 1, 2, 4 s | f04 | SVG | Original |
| u05 | Keyed retry cuts failures | 20 failures per day | 0.4 per day, 8 s worst case | f05 | SVG | Original |
| u05b | 10-step method picks B | Three options | B matches no-double-charge | f05b | Table | Original |
| u06 | Concepts map to exam objectives | -- | Mapping table | f06 | Table | S03, S04 |
| u07 | Breaker beats retry in outages | 3 failed retries | Breaker opens, one probe | f07 | SVG | Original |
| u08 | Alternatives compared | -- | Comparison table | f08 | Table | Original |
| u09 | Constraints decide the pattern | -- | Constraint verdict table | f09 | Table | Original |
| u10 | Prompt retry is valid but inferior | -- | Validity vs inferiority table | f10 | Table | Original |
| u11 | Local call needs no machinery | -- | Counterfactual table | f11 | Table | Original |
| u12 | Five tools from memory | Blank recall card | Filled from memory | f12 | ASCII | Original |
| u13 | Transfer to appointment booking | Unseen question | Key in Stage 8 | f13 | ASCII | Original |
| u14 | Claims classified by date | -- | Evidence table | f14 | Table | Mixed |
