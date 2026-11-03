# Practice item brief (original items only)

Write ORIGINAL scenario practice items for the units listed in your assignment. One JSON file per unit: /home/claude/work/practice/items/<UNIT_ID>.json.

## Hard rules
- Do NOT open, read, search, or quote any file under /root/.claude/uploads/ or any practice exam file. Use only the unit JSON files in /home/claude/work/units/<UNIT_ID>.json and the docs mirror /home/claude/work/docs/pages/.
- Write every stem and option yourself. No copied sentence from the docs longer than 8 words.
- Each unit gets exactly 3 items. Item 1 and item 2 select 1 answer. Item 3 selects 2 answers (set "select": 2 and two correct indices).
- Use 4 options per item. Options are short, parallel, and plausible. Exactly one correct answer for select-1 items; exactly two for select-2 items.
- Put the correct answer at different positions across items. Do not use position 0 for every item.
- Each stem describes a scenario with a constraint. The credited answer meets the stated constraint and no more. One distractor is valid but over-built. One distractor violates the constraint. One distractor looks right but names a wrong feature.
- Tag each item with a "trap" that names the wrong choice that looks right, in one sentence.
- Each item cites one official docs URL in "source". The URL must come from the unit's key_facts or sources, and must exist in the docs mirror.

## JSON shape (per unit)
{
  "unit": "D2.5",
  "items": [
    {
      "id": "D2.5-1",
      "select": 1,
      "stem": "A support team sends the same 8,000-token policy in every request. The team must cut cost without changing answers. Which change meets the constraint?",
      "options": ["...", "...", "...", "..."],
      "correct": [2],
      "rationale": "One or two sentences that explain why the credited answer meets the constraint. STE style.",
      "trap": "One sentence on the distractor that looks right.",
      "source": "https://platform.claude.com/docs/en/build-with-claude/prompt-caching"
    }
  ]
}

## Writing rules (ASD-STE100 style)
Same rules as /home/claude/work/SPEC.md. Stems and rationales: max 25 words per sentence. No contractions. No semicolons. No em dash or en dash. No -ing verbs except docs terms. No perfect tense. No banned filler words.

## Self-check
Run: python3 /home/claude/work/tools/lint.py /home/claude/work/practice/items/<UNIT_ID>.json
Fix every issue (the lint checks the JSON strings). Ignore -ing warnings on docs terms only.
Final reply under 80 words: unit IDs written, lint result.
