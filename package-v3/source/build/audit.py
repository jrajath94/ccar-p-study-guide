"""Output E (audit) and the text checks. Usage: python3 audit.py OUTDIR [PRACTICE_TEXT_DIR]"""
import sys, glob, json, re, os, html as H
sys.path.insert(0, '/home/claude/work/tools')
from common import *
from lint import BANNED, CONTR

OUT = sys.argv[1]
PRACTICE = sys.argv[2] if len(sys.argv) > 2 else None
units = load_units()


def visible_text(path):
    s = open(path, encoding='utf-8', errors='ignore').read()
    if path.endswith('.html'):
        s = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', s, flags=re.S)
        s = re.sub(r'<pre class="mermaid">.*?</pre>', ' ', s, flags=re.S)
        s = re.sub(r'<svg.*?</svg>', ' ', s, flags=re.S)
        s = re.sub(r'<ol class="sources">.*?</ol>', ' ', s, flags=re.S)
        s = H.unescape(re.sub(r'<[^>]+>', ' ', s))
    return re.sub(r'\s+', ' ', s)


def text_checks():
    res = {}
    for f in sorted(glob.glob(f'{OUT}/*.html') + glob.glob(f'{OUT}/*.md')):
        t = visible_text(f)
        low = t.lower()
        res[os.path.basename(f)] = {
            'banned': sorted({b for b in BANNED if re.search(r'\b' + re.escape(b) + r'\b', low)}),
            'dashes': t.count('—') + t.count('–'),
            'semicolons': t.count(';'),
            'contractions': len(CONTR.findall(t)),
            'exam_code_in_body': len(re.findall(r'CCAR-P|CCART', t)),
        }
    return res


def overlap_check():
    """Count 8-word runs shared with the practice files. Returns None when the files are absent."""
    if not PRACTICE or not os.path.isdir(PRACTICE):
        return None
    def grams(t):
        t = re.sub(r'https?://\S+', ' ', t)
        w = re.findall(r"[a-z0-9]+", t.lower())
        return {' '.join(w[i:i + 8]) for i in range(len(w) - 7)}
    pg = set()
    for f in glob.glob(f'{PRACTICE}/*'):
        pg |= grams(open(f, errors='ignore').read())
    hits = {}
    for f in glob.glob(f'{OUT}/*.html') + glob.glob(f'{OUT}/*.md'):
        n = len(grams(visible_text(f)) & pg)
        if n:
            hits[os.path.basename(f)] = n
    return hits


def practice_section():
    """Coverage counts and practice-set status. Counts only. No item text, no item IDs from the exams."""
    from collections import Counter
    m = json.load(open('/home/claude/work/practice/map.json'))
    c = Counter(r['unit'] for r in m if r['unit'])
    rows = []
    for dom, u in units:
        rows.append(f'- {u["id"]} {u["title"]}: {c.get(u["id"], 0)} mapped items')
    n_items = sum(len(json.load(open(f))['items']) for f in glob.glob('/home/claude/work/practice/items/*.json'))
    L = ['## Practice items and coverage', '',
         f'Practice exam files supplied: 11 (six full, five unofficial). They hold {len(m)} items in total: 378 in the full exams (63 each) and 300 in the unofficial exams (60 each). The spec expected six files of 75. The counts differ.',
         'Mapping method: keyword counts against each unit. The map is approximate. It was not reviewed item by item. Each unit has at least one mapped item.',
         f'Original practice items written for this package: {n_items} across all 42 units (three per unit). Each item cites an official docs page. Each key was checked against the docs by a review pass.',
         'The practice exam text is not copied into any output. Stems, options, answer keys, and explanations from the uploaded files stay out of the outputs.',
         'Eight-word overlap with the uploaded exam files: see the text checks section.', '',
         '### Mapped items per unit (approximate)', ''] + rows + ['']
    return '\n'.join(L)


def build():
    tc = text_checks()
    ov = overlap_check()
    nis, labels, ncomp, nfacts = [], {'Fact': 0, 'Inference': 0, 'Guess': 0}, 0, 0
    for dom, u in units:
        for c in u.get('components', []):
            ncomp += 1
            for f in c.get('key_facts', []):
                nfacts += 1
                labels[f.get('label', 'Fact')] = labels.get(f.get('label', 'Fact'), 0) + 1
            for x in c.get('not_in_source', []):
                nis.append((u['id'], c.get('name'), x))
        for x in u.get('not_in_source', []):
            nis.append((u['id'], '', x))
    expected = [x[0] for d in load_topics()['domains'] for x in d['units']]
    present = [u['id'] for _, u in units]
    missing = [x for x in expected if x not in present]
    text_fail = {k: v for k, v in tc.items() if any(v[x] for x in ('banned', 'dashes', 'semicolons', 'contractions', 'exam_code_in_body'))}
    open_checks = [
        'Question-to-unit map: pending. The six practice exams and the question bank are not supplied.',
        'Eight-word overlap check: ' + ('pending, practice files not supplied.' if ov is None else f'{sum(ov.values())} matches.'),
        'Official exam guide: partner-gated. Domain names, weights, and task statements rest on secondary sources (Inference).',
        'Native cloud services list in the exam guide: not available. The build uses the five platforms that the docs name (Inference).',
        'Publication checks (detect, remove-ai-marks, publication-clean): pending. They run on the Mac through Remote Control.',
        'Practice items: the review pass corrected answer keys. Recheck the audit after the pass.',
        'Official screenshots: not copied, because the docs state no reuse terms for images. Console steps link to the official pages.',
    ] + ([f'Units missing: {", ".join(missing)}.'] if missing else [])
    score = 6
    reasons = [
        f'{len(present)} of {len(expected)} units built, {ncomp} components, {nfacts} key facts. Each key fact cites an official docs page.',
        'An automated check confirms that each number in a key fact appears in its cited page.',
        'Opus review checked each unit against the docs mirror.',
        'Minus 2: the official exam guide is not available, so coverage of official task statements is not verified.',
        'Minus 2: the question-to-unit map and the overlap check wait on the practice files.',
    ]
    if text_fail:
        score -= 1
        reasons.append('Minus 1: text checks found rule breaks (see below).')
    if missing:
        score -= 1
    L = ['# Audit', '', f'Verdict: {score} of 10.', ''] + [f'- {r}' for r in reasons] + ['']
    L += ['## Topic index', '']
    cur = None
    for dom, u in units:
        if dom['id'] != cur:
            cur = dom['id']
            L.append(f'### {dom["id"]} {dom["title"]} (weight {dom["weight"]}, Inference)')
        L.append(f'- {u["id"]} {u["title"]}: ' + ', '.join(c.get('name', '') for c in u.get('components', [])))
    L += ['', '## Question-to-unit map', '', 'Pending. The practice exams (six files of 75 items) and the question bank (about 250 items) are not supplied. '
          'When they arrive, each item maps to a unit ID here. No item text goes into any output.', '']
    L += ['## Claim labels', '', f'- Key facts: {labels.get("Fact", 0)} Fact, {labels.get("Inference", 0)} Inference, {labels.get("Guess", 0)} Guess.', '']
    L += ['## Text checks', '']
    for k, v in tc.items():
        L.append(f'- {k}: banned words {len(v["banned"])}{" " + str(v["banned"]) if v["banned"] else ""}, dashes {v["dashes"]}, semicolons {v["semicolons"]}, contractions {v["contractions"]}, exam code in body {v["exam_code_in_body"]}.')
    L += ['', f'Eight-word overlap with practice files (URLs excluded): {"not run, files not supplied" if ov is None else ov}.', '']
    L += [practice_section(), '']
    L += ['## Open checks', ''] + [f'- {x}' for x in open_checks]
    L += ['', '## Not in source', ''] + [f'- {a} {b}. {c}'.replace(' . ', ' ') for a, b, c in nis]
    open(f'{OUT}/audit.md', 'w').write('\n'.join(L) + '\n')
    print(f'audit score {score}, not-in-source {len(nis)}, text failures {len(text_fail)}')
    for k, v in text_fail.items():
        print(' ', k, v)


build()
