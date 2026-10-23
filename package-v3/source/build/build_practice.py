"""Original practice test: static HTML and print PDF, with an answer key after the items.
Usage: python3 build_practice.py OUTDIR
Reads /home/claude/work/practice/items/<ID>.json. Never reads the uploaded exam files."""
import sys, json, glob, os
from render import *

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
TITLE = 'Claude Certified Architect, Professional. Practice test (original items)'
src_dir = '/home/claude/work/practice/items'
units = {u['id']: (d, u) for d, u in load_units()}
sets = []
for dom, u in load_units():
    fn = f'{src_dir}/{u["id"]}.json'
    if os.path.exists(fn):
        sets.append((dom, u, json.load(open(fn))))

LETTERS = 'ABCD'


def items_html(show_key):
    parts = []
    n = 0
    for dom, u, p in sets:
        parts.append(f'<h3>{esc(u["id"])} {esc(u["title"])}</h3>')
        for it in p.get('items', []):
            n += 1
            sel = it.get('select', 1)
            prompt = 'Select one answer.' if sel == 1 else 'Select two answers.'
            opts = ''.join(f'<li><span class="lbl">{LETTERS[k]}.</span> {esc(o)}</li>' for k, o in enumerate(it['options']))
            parts.append(f'<div class="item"><p><span class="lbl">{n}.</span> {esc(it["stem"])}</p>'
                         f'<p class="tag">{prompt}</p><ol class="opts" type="A">{opts}</ol>')
            if show_key:
                ans = ', '.join(LETTERS[c] for c in it['correct'])
                parts.append(f'<p class="c-rule"><span class="lbl">Answer: {ans}.</span> {esc(it.get("rationale"))}</p>'
                             f'<p class="c-trap">Trap. {esc(it.get("trap"))}</p>'
                             f'<p class="tag">Source. {esc(it.get("source"))}</p>')
            parts.append('</div>')
    return ''.join(parts), n


CSS_EXTRA = ('.opts{list-style:none;padding-left:0} .opts li{margin:.2em 0}'
             '.item{break-inside:avoid;margin:.4em 0 .9em}')


def body(show_key):
    html, n = items_html(show_key)
    head = (f'<h1>{esc(TITLE)}</h1>' + legend_html() +
            f'<p>{n} items, {len(sets)} units. Read each stem and pick the answer that meets every stated constraint. '
            'Each item states how many answers to select. The items are original. They do not copy any exam item.</p>')
    return head + html


body_items = body(False)
css_print = PRINT_CSS + CSS_EXTRA
css_dark = DARK_CSS + CSS_EXTRA
main_items = f'<main>{body_items}</main>'

# Items only for the take-test copy, then the key in a separate copy.
open(f'{OUT}/practice-test.html', 'w').write(page(TITLE, css_dark, '<main>' + body(False) + '</main>'))
key_html = ('<h2 class="nobreak">Answer key</h2>' + items_html(True)[0])
open(f'{OUT}/practice-answer-key.html', 'w').write(page(TITLE + '. Answer key', css_dark, '<main>' + key_html + '</main>'))

tmp = f'{OUT}/.practice-print.html'
open(tmp, 'w').write(page(TITLE, css_print, '<main>' + body(False) + '<h2 class="nobreak">Answer key</h2>' + items_html(True)[0] + '</main>'))
html_to_pdf(tmp, f'{OUT}/practice-test.pdf')
os.remove(tmp)
print('practice items', sum(len(p.get('items', [])) for _, _, p in sets), 'units', len(sets))
