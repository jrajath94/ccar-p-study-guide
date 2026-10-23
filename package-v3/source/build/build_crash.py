"""Crash course: dark guide HTML (live diagrams) and dark PDF (pre-rendered diagrams).
Usage: python3 build_crash.py OUTDIR [DOMAIN_OR_UNIT ...]"""
import sys
from render import *

out = sys.argv[1]
only = sys.argv[2:] or None
os.makedirs(out, exist_ok=True)
units = load_units(only)
name = 'sample-chapter' if only else 'crash-course'
TITLE = 'Claude Certified Architect, Professional. Crash course' + (' sample chapter' if only else '')


def body(live):
    src = Sources()
    mer = {} if live else render_mermaid(mermaid_items(units), 'dark')
    parts = [f'<main><h1>{esc(TITLE)}</h1>', legend_html(),
             '<p>Each unit gives a first principle, an architecture schematic, the steps, the choices for each '
             'constraint, the trap, and the items that the docs do not confirm.</p>',
             '<h2 class="nobreak">Topic index</h2>', topic_index_html(units)]
    for dom, u in units:
        parts.append(render_unit_full(dom, u, src, mer, live))
    parts.append('<h2>Sources</h2>' + src.html() + '</main>')
    return ''.join(parts)


html_live = page(TITLE, DARK_CSS, body(True), mermaid_live_script('dark'))
open(f'{out}/{name}.html', 'w').write(html_live)
pdf_html = f'{out}/.{name}.print.html'
open(pdf_html, 'w').write(page(TITLE, DARK_CSS, body(False)))
html_to_pdf(pdf_html, f'{out}/{name}.pdf')
os.remove(pdf_html)
print('built', name, len(units), 'units')
