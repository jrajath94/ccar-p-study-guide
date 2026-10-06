# Stage 6 Report: Domains 6 and 7 (Oct 6, 2026)

Builder: Stage 6 worker. Scope: 8 objectives, 8 lessons, all in
`~/workspace/your_files/ccar-p-cert/v2-build/stage6/`.

## Objective map

| Objective | Lesson file | Status |
|---|---|---|
| V2-D6.1 structured discovery | lesson-D6-1.md | Built |
| V2-D6.2 trade-off communication | lesson-D6-2.md | Built |
| V2-D6.3 feedback and expectation alignment | lesson-D6-3.md | Built |
| V2-D6.4 architecture documentation | lesson-D6-4.md | Built |
| V2-D6.5 lifecycle phases | lesson-D6-5.md | Built |
| V2-D7.1 team configuration | lesson-D7-1.md | Built |
| V2-D7.2 AI-assisted workflows | lesson-D7-2.md | Built |
| V2-D7.3 debugging and operational resolution | lesson-D7-3.md | Built |

Each lesson carries the mandatory 16-part template: problem,
prerequisites, mental model, causal mechanism, worked example
with the canonical 10-step best-answer method trained verbatim,
product and protocol mapping, current limitations, nearest
alternatives, decisive scenario constraints, valid-but-inferior
option, counterfactual where the alternative wins, closed-book
recall prompt, unseen transfer question without answer,
evidence table, and a page-audit table with no blank figure
cells.

## Evidence

| Claim | Class | Source | Date |
|---|---|---|---|
| D6.1-D6.5, D7.1-D7.3 objective scope | Official exam scope via secondary summaries | S03, S04, blueprint ledger | Sept 2026 |
| Claude Code settings scopes, allow/ask/deny rules, hooks, CLAUDE.md as guidance not enforcement, managed-settings priority | Current product behavior | Official docs docs.claude.com/en/docs/claude-code/settings | Oct 6, 2026 |
| Subagent frontmatter fields (tools, model), SKILL.md format, MCP server scopes | Current product behavior via secondary sources | GitHub skill references | Oct 6, 2026 |
| All cost arithmetic in figures (discovery payoff, trade-off pricing, breach day, ADR value, runbook savings, guardrail spend) | Original toys, computed in the lessons | This stage | Oct 6, 2026 |

D7.1 verification: the four settings scopes (user
`~/.claude/settings.json`, shared `.claude/settings.json`,
local `.claude/settings.local.json`, managed), the
allow/ask/deny rule kinds, PreToolUse/PostToolUse hooks, and
the CLAUDE.md guidance role were all read on the official
settings page on Oct 6, 2026. MCP configs live in
`~/.claude.json` per the same page.

## Corrections made during the build

1. ste_check.py hard fails fixed: 4 semicolons, 1 en dash
   (D6-5 prereq table), and 1 -ing main verb (D7-2).
   Final scan: 0 hard fails across all 8 files.
2. Linter false positive: `->` arrow escapes in D7-3 figure
   text flagged as semicolons. Replaced `->` with "then"
   wording instead of suppressing.
3. 25 figure copy errors found by XML parse check: `<rect>`
   tags closed with `</text>`. Fixed. All 32 SVGs now parse.
4. One figure rendered to PNG and inspected visually: layout,
   palette, arrow, footer all correct.

## Gaps and open items

- §13 transfer questions carry no answers by design. Stage 8
  owns all keys.
- Toy arithmetic uses stated toy assumptions, not real
  vendor prices. The exam-relevant direction is real. The
  numbers are marked "Original toy" in evidence tables. "Not in
  source" appears once, for the delayed-refund dollar cost
  in D6-1.
- D7.1 managed-settings and plan requirements verified on
  official docs. Subagent `tools` frontmatter verified via
  secondary sources only. Mark kept as such in evidence.

## Stage 7 needs

- Confusion matrices and labs that reuse these lessons must
  not re-teach: D6.1 eleven-question grid, D6.2 five fields
  and five audiences, D6.3 six-part contract and iterate
  rule, D6.4 nine-field ADR, D6.5 five phases and return
  rule, D7.1 guidance vs enforcement, D7.2 four-part
  evidence, D7.3 symptom map. Reference by name.
- The D7.1 guidance-vs-enforcement discrimination is the
  highest-yield trap in this stage. Stage 7 should include
  at least one confusion pair: CLAUDE.md note vs deny rule.
- Figure audit for Stage 7: 32 SVGs verified parseable.
  Re-render check recommended at assembly time.
