# Accuracy review brief (Opus reviewer)

You review drafted study units. The units are JSON files in /home/claude/work/units/. Read /home/claude/work/SPEC.md first.

For each unit file assigned to you:
1. Read the file.
2. For every key_fact, native_services entry, step, constraint, use_when, do_not_use_when, trap, decision_rule, and exam_tip:
   - Find the supporting text in the cited official page in /home/claude/work/docs/pages/ (Grep it).
   - If the claim is wrong, fix it to match the page, or move it to not_in_source with "Not in source."
   - If the claim is general practice that no page states, make sure it carries " (Inference)".
   - If a URL is wrong, replace it with the correct page URL from the mirror.
3. Check the teaching logic. The trap must be a wrong choice that looks right, and the text must say why it is wrong. The decision rule must pick the option that meets the stated constraint and no more, with least privilege, and with no extra components.
4. Check that model names, prices, limits, beta status, and platform availability match the docs exactly. Prefer the current models named in about-claude/models/overview.
5. Check that architecture node and edge labels are short (max 6 words) and that the decision_flow and cheatsheet are valid Mermaid flowcharts with plain labels (no quotes, no parentheses, no semicolons inside labels).
6. Keep the schema and the STE writing rules. Edit the file in place.
7. Run: python3 /home/claude/work/tools/lint.py FILE and python3 /home/claude/work/tools/factcheck.py FILE. Fix until both are clean, except -ing warnings on true technical nouns from the docs.

Final reply (under 200 words): for each unit, the count of corrections and the most serious error you fixed. List any claim you could not verify.
