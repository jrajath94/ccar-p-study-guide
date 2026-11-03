# CCAR-P study package

Read `audit.md` first. It gives unit coverage, check results, and known gaps.

## Contents

| Path | Contents |
|---|---|
| `audit.md` | Coverage and check results |
| `curriculum.pdf`, `curriculum-2up.pdf`, `curriculum.docx` | Full curriculum, in print and Word formats |
| `treatise.html` | Long-form study text |
| `mega-cheatsheet.html`, `mega-cheatsheet.pdf` | One-sheet summary |
| `mind-map.html` | Mind map |
| `practice-test.html`, `practice-test.pdf` | Practice test with 126 original items |
| `practice-answer-key.html` | Answer key for the practice test |
| `question-patterns.html`, `question-patterns.pdf` | Question patterns |
| `console-steps.html`, `console-steps.pdf` | Console steps |
| `video-prompt.md`, `video-summary.md`, `video-gaps.md` | Video prompt, summary, and gap notes |
| `sample/` | D2 sample chapter. `sample-chapter-v1` is the first draft. `sample-chapter-v2` is the revised build. |
| `source/units/` | 42 unit files in JSON (F, D1 to D7) |
| `source/practice/items/` | 42 files, three original practice items each |
| `source/topics.json` | Topic manifest and domain weights |
| `source/build/` | Renderers for each output, and `package.json` |
| `source/tools/` | Schema, review rules, `lint.py`, and `factcheck.py` |

## Build inputs

The build scripts read inputs from a work folder. The default is `/home/claude/work`. Set `CCAR_WORK` to use another folder.

The work folder needs these inputs:

| Input | Source |
|---|---|
| `units/`, `topics.json`, `practice/items/` | Copy from `source/` |
| `docs/pages/` | Local copy of the official Claude documentation pages. About 1,040 pages. Not committed |
| `practice/map.json` | Local map from supplied practice exam items to units. Required by `audit.py`. Not committed |

Keep exam text and `map.json` out of the repository.

## Rebuild

1. Set the work folder. Run `export CCAR_WORK=/path/to/work`.
2. Copy the inputs into the work folder.
3. Install the renderer packages. Run `npm install` in `source/build/`.
4. Install Chromium for Playwright. Skip this step when Chromium is already installed. Run `npx playwright install chromium`.
5. Build the D2 sample. Run `python3 build_crash.py /path/to/out D2` in `source/build/`.
6. Compare the sample with `sample/`. The HTML and print PDF matched the committed v2 files byte for byte on 2026-11-03.
7. Build the practice test. Run `python3 build_practice.py /path/to/out` in `source/build/`.
8. Check a unit file. Run `python3 source/tools/lint.py source/units/<ID>.json` and `python3 source/tools/factcheck.py source/units/<ID>.json`.

## Known limits

- Official exam guide: Not in source. Coverage uses the topic manifest and the docs pages.
- Domain weights are an inference from secondary sources. Check them against the official exam guide.
- `audit.py` fails without `practice/map.json`.
- The Mermaid and Playwright versions are pinned in `source/build/package.json`. Mermaid is 10.9.1.
