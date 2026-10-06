# Stage 8d audit changelog

Every edit to a bank file, with ID, verdict, before/after, and rationale.
Question IDs stay stable. Fix-loop count per item is tracked, loop 3
failure means REJECTED (see rejected-items.md).

## Q-M-15 (qb-mixed.md) - FIXED, loop 1

- Verdict: FAIL on audit (multi-select over-subscription), fixed.
- Attack: the scenario evidences THREE named V2-D2.4 context faults:
  growth (full 60,000-token season load every call), duplication
  (overlapping sensors repeat readings), and dilution (March data
  answers July questions, lesson-D2-4 defines dilution as a named fault,
  "the middle answer is wrong," i.e. the model attends to the wrong span
  of a bloated context). The question asked for TWO. A learner who
  correctly names all three faults cannot express the right answer.
  The key's defense ("C is a symptom of A, not a fault") contradicts
  the lesson taxonomy, which lists dilution as one of the five failure
  modes.
- Before: `## Q-M-15 (V2-D2.4), Select TWO` / "Which TWO context faults
  are present? Select TWO." / Answer A, B, method walk step 8-10 and
  explanation points 1, 4, 5, 6, 9, 10 defended the A,B-only reading.
- After: `## Q-M-15 (V2-D2.4), Select THREE` / "Which THREE context
  faults are present? Select THREE." / Answer A, B, C, method walk and
  explanation rewritten to name all three faults and their distinct
  fixes (retrieval, dedupe, fewer better-placed chunks). D (exhaustion:
  no overflow stated) and E (loss: no vanishing turns) remain the
  rejected options. Misconception repointed: "growth alone explains
  every context failure."
- Why this fix: preserves difficulty (three-way diagnosis, still two
  clean rejects) and matches the lesson taxonomy. The alternative
  (deleting the March/July evidence) would remove the dilution
  coverage entirely.

## M2-Q13 (mocks.md) - PASS

- Attack attempted: looked for a second defensible risk (e.g. tier
  choice itself). None found: A ("No risk. Keywords are perfect.") is a
  documented trap, C and D are incoherent. Key B (router
  misclassification both directions + router needs evals) is uniquely
  defensible.
- Note: distractors are weak (absurd rather than plausible). Key
  survives, no edit. Difficulty note only.

## M3-Q33 (mocks.md) - FIXED, loop 1

- Verdict: FAIL on audit (key demands an untaught requirement,
  contradicts lesson), fixed.
- Attack: the key (B) claimed "p95 under 2 seconds" is an incomplete
  threshold because it lacks "measurement conditions." The Lesson 7-4A
  / lesson-D4-1 chain is requirement, metric, threshold, owner, the
  lesson's own worked example presents "p95 under 5 seconds" as a
  complete guard ("Each guard is a metric with a threshold and an
  owner"). Per the taught chain, option A ("Yes. Latency is named with
  a number") was the more defensible answer, and the key's
  "measurement conditions" requirement was invented to protect B.
- Before: question "Is this a complete threshold?" with key B.
- After: scenario adds "No one is named to answer for the threshold."
  Question: "Which link of the Lesson 7-4A requirement chain is still
  missing?" Options: A) Nothing: all four links present (trap: "the
  team" is not a named owner). B) The owner (key). C) The requirement
  was never written down (contradicts scenario). D) The metric was
  never named (contradicts scenario). Key explanation cites the taught
  chain and the drift risk ("Thresholds expire when the ticket mix
  changes," lesson-D4-1).
- Why this fix: tests the genuinely missing taught link instead of an
  invented one. Difficulty preserved (A is a live trap for sloppy
  readers).

## M4-Q47 (mocks.md) - PASS

- Attack attempted: (1) shape mislabel - the review happens before the
  consequential action (publish), so pre-action approval is the right
  shape name, post-action (C) fails. (2) "is it right" - challenged as
  opinion: public headlines carry reputation risk, but harm is
  reversible (correct/retract), drafts are "usually fine" (low
  uncertainty), and the editor reads with context (V2-D5.3's reviewer
  requirement). Pre-action approval is proportionate. No other option
  defensible. Key A survives, no edit.

## Q-D3-07 (qb-D3.md) - FIXED, loop 1 (explanation only, key survives)

- Verdict: key A survives the attack, but the explanation overstated the
  result. Attack: the scenario's own numbers show A removes 700 ms from
  a 2.9 s p95, leaving 2.2 s, which still exceeds the 2 s SLA. The old
  explanation framed A against the objective "p95 under 2 s" without
  naming the residual 200 ms gap.
- Defense of the key: the question asks for the best NEXT action. A is
  unambiguously the best first cut (worst ms-per-point stage removed,
  floor held at 92%). No other option is better: B adds latency, C
  breaks the floor (89%), D at best saves a fraction of 400 ms.
- Before: explanation point 7 said only "A spends 1 point of headroom",
  method walk step 8 said "removing it gives 2.2 s and 92%, still above
  the floor."
- After: point 7 now states that 2.2 s still sits 200 ms above the SLA,
  so A is the best first cut, not the full fix, and names the next cuts
  (reasoning trim or retrieval cache, each re-measured, evals re-run).
  Step 8 carries the same caveat.
- Why this fix: trust-by-verify means the explanation must not imply a
  result the scenario's own arithmetic contradicts.

## Q-D4-03 (qb-D4.md) - PASS (attack defeated by the lesson)

- Attack attempted: option A ("Make refund accuracy the primary metric")
  looked equally defensible against key option E ("cost per successful
  refund as the primary business metric"), which would be a multi-select over-subscription FAIL like Q-M-15.
- Defense: lesson-D4-1 §9 decisive-constraint table states verbatim
  "Budget binds → Cost per successful task is the primary," and "Safety
  or security at stake → Add the guard metric with a zero threshold."
  The scenario states "The budget binds" and "unauthorized refunds must
  be zero." Both keyed options map 1:1 to the lesson's table rows. A is
  the documented misconception ("accuracy is always the primary").
- No edit. The attack failed, the key stands on the lesson's own text.

## Q-D5-21 (qb-D5.md) - FIXED, loop 1 (numbers, key survives)

- Verdict: arithmetic inconsistency in the scenario, key unaffected.
- Attack: the scenario's numbers do not add up. 800 applicants at 96%
  (768 correct) plus 200 at 68% (136 correct) = 904/1000 = 90.4%
  overall, but the scenario, option A, and the explanation all said
  "94%." A learner who checks the math loses trust in the item.
- The key (B: block the ship on the per-group floor) never depended on
  the overall number, so the key survives.
- Before: "scores 94% correct overall", A) "Ship. The 94% overall
  exceeds the floor.", explanation "The 94% hides the 68%" and
  "the aggregate moved 94 to 95."
- After: "scores 90% correct overall", A) "Ship. The 90% overall meets
  the floor.", explanation "The 90% hides the 68%" and "the aggregate
  moved 90 to 91." The trap still works: the aggregate meets the
  floor while Group B (68%) fails the per-group floor.

## M1-Q28 (mocks.md) - PASS (attack defeated)

- Attack attempted: option A (keyword search) looked like a third
  defensible answer for a Select TWO asking "which TWO fit," since
  keyword search is a legitimate strategy for description text.
- Defense: option B explicitly establishes the synonym dimension
  ("waterproof" vs "rain-proof"), which keyword search misses. B
  strictly dominates A on the stated evidence, they are not equally
  defensible. The key's counterfactual correctly scopes A to the
  exact-SKU scenario. Unlike Q-M-15 (where dilution was a named fault
  with direct evidence), here A is a weaker-but-wrong answer, the
  standard distractor role.
- No edit.
