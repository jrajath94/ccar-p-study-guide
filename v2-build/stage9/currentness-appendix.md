# Currentness appendix

Product facts move. Exam scope moves slower. This appendix keeps
the two apart. Every dated claim in the build resolves to one of
the two views below.

## View A: the Oct 6, 2026 baseline

Frozen facts. The build teaches against this view unless View B
records a verified change.

- Blueprint: CCAR-P v1.0, effective July 2026. No newer blueprint
  version was found in any source as of Oct 6, 2026.
- Exam format: 63 items, multiple-choice plus multiple-response,
  120 minutes, closed book, Pearson VUE delivery. Passing: 720 on a
  100 to 1000 scaled score, criterion-referenced. Fee: $175 USD per
  attempt. Validity: 12 months. Retakes: 14 days after attempt 1, 30
  days after attempt 2, 90 days after attempt 3, max 4 attempts per
  rolling 12 months.
- Model lineup (secondary-source enrichment, not exam scope): four
  tiers as of Oct 2026. Fast: claude-haiku-4-5, 200K context, $1 in
  and $5 out per 1M tokens. Balanced: claude-sonnet-5-5, 1M
  context, $2 in and $10 out. Capable: claude-opus-5-5, 1M context,
  $4 in and $20 out. Most capable: claude-fable-5-1, 1M context,
  $10 in and $50 out. Sources: agentskit.co (Oct 1, 2026),
  izzedo.chat (Sept 2026), qcode.cc (Sept 29, 2026). The exam
  itself is dated to blueprint v1.0 and tests tier-level
  trade-off judgment, not memorized model IDs. The lessons teach
  tier reasoning and carry the matrix as implementation
  enrichment.
- Prompt caching: write 1.25x, read 0.1x, 5-minute TTL. Secondary
  sources, Oct 2026. Verify against official docs before quoting.
- MCP spec: the 2026-07-28 revision, per independent corroboration.
  The official spec was not opened in-session. Product support per
  primitive is unverified. Re-check before quoting.

## View B: post-baseline changes

Verified changes dated after Oct 6, 2026. A same-day web check on
Oct 6, 2026 found none of the following: no blueprint update past
v1.0, no model launch dated after Oct 6, 2026, no spec revision
dated after Oct 6, 2026. The Opus 5.5 launch (Sept 22, 2026) and
the Sonnet 5.5 launch (six days later) both sit before the
baseline, so they belong to View A. The Google Antigravity
retirement dates (Nov 2, 2026, for older models) were announced
around Oct 3, 2026, also before the baseline.

View B is therefore empty and stays open. When a verified change
lands, record it here with the date, the source, and which View A
facts it supersedes. Until then, View A stands.

## Claim-classification key

Every evidence table in the build uses these classes. Read the
class before you trust the claim.

| Class | Meaning | How to treat it |
|---|---|---|
| Official exam scope via secondary summaries | The claim describes what the exam tests, via four corroborated secondary summaries of the official v1.0 guide (S03, S04, S05, S06, Sept 2026) | Trust the scope. The official guide is the tie-breaker for any conflict. |
| General principle | Long-standing industry or architecture practice | Trust the mechanism. Dates say long-standing. |
| Current product behavior, secondary | Product facts from independent sources, dated Oct 2026 | Use for judgment, not memorization. Verify against official docs before quoting. |
| Current product behavior | Product facts read on official docs in-session, dated | Trust, with the date noted. |
| Spec concepts, corroborated by independent sources | Spec claims checked against independent sources but not read on the official spec in-session | Trust the concept. Re-check the official spec for exact revision wording. |
| Original toy, computed above | Numbers computed inside the lesson on stated toy assumptions | Trust the arithmetic, not the inputs. The direction is exam-relevant. |
| Toy assumption, stated | An input value the toy declares, with no source | Do not quote as fact. |
| Not in source | The builder could not source the value | Do not quote. The lesson says so explicitly. |
| Prior lessons carry over | The claim was taught in an earlier lesson | Follow the pointer. It is not re-proved here. |
