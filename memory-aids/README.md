# Memory aids

Three levels of recall aids for the study package.

- `exam-map.html`: the exam-wide sheet. Ten rules, a radial map of all sections, constraint family totals, a section table, and a numbers table with a filter.
- `chapters/<chapter>.html`: one page per chapter. A concept map, then one card for each section.
- Each section card has a memory hook, constraint family bars, rule and trap lines, recall cues, and numbers.
- `print/*.pdf`: white A4 copies for paper study.

Open any HTML file in a browser. Each file carries d3 inline, so it runs offline.

Rebuild:

    python3 build_memory.py
    node build_pdf.js

`build_memory.py` reads `package-v3/source/units`, `package-v3/source/topics.json`, and `hooks.json`. Edit the hooks in `hooks.json`, then rebuild.
