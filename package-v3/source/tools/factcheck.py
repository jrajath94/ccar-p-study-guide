#!/usr/bin/env python3
"""Check that each number in a key fact appears in its cited docs page. Usage: factcheck.py FILES"""
import json, re, sys, os
DOCS = '/home/claude/work/docs/pages'
def page(u):
    u = u.split('#')[0].rstrip('/')
    f = os.path.join(DOCS, u.replace('https://', '').replace('/', '__') + '.md')
    return open(f).read() if os.path.exists(f) else None
def norm(s): return s.replace(',', '').replace('\\', '')
bad = tot = 0
for fn in sys.argv[1:]:
    u = json.load(open(fn))
    for c in u.get('components', []):
        for f in c.get('key_facts', []):
            tot += 1
            t, url = f.get('text', ''), f.get('url', '')
            p = page(url) if url else None
            if p is None:
                if f.get('label', 'Fact') == 'Fact':
                    bad += 1; print(f'{u["id"]} NOURL/NOPAGE: {t} | {url}')
                continue
            P = norm(p)
            miss = [n for n in re.findall(r'\d+(?:\.\d+)?', norm(t)) if n not in P]
            if miss:
                bad += 1; print(f'{u["id"]} MISSING {miss}: {t} | {url}')
print(f'facts={tot} flagged={bad}')
