#!/usr/bin/env python3
"""STE and source lint for unit JSON files. Usage: lint.py FILE [FILE...]"""
import json, re, sys, os, glob

DOCS = os.path.join(os.environ.get('CCAR_WORK', '/home/claude/work'), 'docs', 'pages')
BANNED = ['delve','leverage','unlock','robust','seamless','nuanced','pivotal','landscape','realm',
 'tapestry','underscore','harness','foster','groundbreaking','cutting-edge','game-changing','holistic',
 'multifaceted','it is important to note',"in today's world",'when it comes to','at its core',
 "let's break it down",'not only']
ING_OK = set('''caching streaming routing logging thinking batching chunking embedding embeddings string strings thing things
nothing something anything everything during bring ring king sampling ranking reranking tokenizing prompting
pricing billing tracing monitoring testing training fine-tuning tuning grounding versioning onboarding scaling
rate-limiting throttling retrying sharding indexing parsing scoring labeling filtering processing reasoning
setting settings meaning warning warnings morning spring ceiling building engineering planning offering
listing pairing branching mapping polling hashing pending rolling encoding hosting computing networking
learning modeling programming spending staging timing landing heading headings opening wording rating funding
logging-in sign-in single-sign-on spacing padding wiring trailing leading heading timestamping
handling saving savings pairing counting editing load-balancing failing-open evaluating'''.split())
CONTR = re.compile(r"\b\w+(n't|'re|'ve|'ll|'d|'m)\b|\b(it's|that's|there's|what's|let's|here's|who's)\b", re.I)

def strings(o, path=''):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in ('code', 'mermaid', 'url', 'urls', 'sources', 'svg', 'id', 'nodes', 'edges'):
                continue
            yield from strings(v, f'{path}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from strings(v, f'{path}[{i}]')

def urls(o):
    if isinstance(o, str):
        yield from re.findall(r'https?://[^\s)"\]]+', o)
    elif isinstance(o, dict):
        for v in o.values(): yield from urls(v)
    elif isinstance(o, list):
        for v in o: yield from urls(v)

def url_ok(u):
    u = u.split('#')[0].rstrip('/').rstrip('.')
    if not (u.startswith('https://platform.claude.com/docs/en/') or u.startswith('https://code.claude.com/docs/en/')):
        return None
    f = os.path.join(DOCS, (u.replace('https://', '') + ('' if u.endswith('.md') else '.md')).replace('/', '__'))
    return os.path.exists(f)

def lint(fn):
    issues = []
    try:
        d = json.load(open(fn))
    except Exception as e:
        return [f'INVALID JSON: {e}']
    for p, s in strings(d):
        low = s.lower()
        for b in BANNED:
            if re.search(r'\b' + re.escape(b) + r'\b', low):
                issues.append(f'{p}: banned "{b}"')
        if '—' in s or '–' in s: issues.append(f'{p}: em/en dash')
        if ';' in s: issues.append(f'{p}: semicolon')
        if CONTR.search(s): issues.append(f'{p}: contraction "{CONTR.search(s).group(0)}"')
        for w in re.findall(r'\b([A-Za-z-]+ing)\b', s):
            if w.lower() not in ING_OK and len(w) > 4:
                issues.append(f'{p}: -ing word "{w}" (rewrite unless technical term)')
        if p.endswith(('decision_flow','cheatsheet')): continue
        for sent in re.split(r'(?<=[.!?])\s+', s):
            n = len(sent.split())
            if n > 25: issues.append(f'{p}: sentence {n} words: "{sent[:60]}..."')
        if re.search(r'\b(has|have|had) (been|\w+ed)\b', low): issues.append(f'{p}: perfect tense?')
    for u in set(urls(d)):
        ok = url_ok(u)
        if ok is None: issues.append(f'URL not official docs: {u}')
        elif not ok: issues.append(f'URL not found in mirror: {u}')
    return issues

if __name__ == '__main__':
    tot = 0
    for fn in sys.argv[1:]:
        iss = lint(fn); tot += len(iss)
        print(f'== {fn}: {len(iss)} issues')
        for i in iss[:200]: print('  ' + i)
    sys.exit(1 if tot else 0)
