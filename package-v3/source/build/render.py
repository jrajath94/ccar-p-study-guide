"""Unit and page renderers for the print curriculum, the dark crash course, and the web treatise."""
import json
from common import *

FONT = 'Inter'

CSS_BASE = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:Inter,'Inter Display',system-ui,sans-serif;background:var(--bg);color:var(--fg);line-height:1.6}
h1,h2,h3,h4,h5{line-height:1.25;font-weight:650;color:var(--fg);break-after:avoid}
a{color:inherit}
sup.ref{font-size:.7em;line-height:0}
sup.ref a{text-decoration:none;color:var(--muted)}
.c-fact{color:var(--fact)} .c-rule{color:var(--rule)} .c-tip{color:var(--tip)} .c-trap{color:var(--trap)}
.legend span{margin-right:1.4em;white-space:nowrap}
.figure{margin:.6em 0 1em;color:var(--fg);break-inside:avoid}
.figure svg{max-width:100%;height:auto}
.figure .cap{font-size:.82em;color:var(--muted);margin-top:.2em}
.lbl{font-weight:650}
ol.sources{font-size:.85em;word-break:break-all}
.nis li{color:var(--muted)}
.mermaid-box{break-inside:avoid;text-align:center}
.mermaid-box svg{max-width:100%;height:auto;max-height:170mm}
.tag{font-size:.8em;color:var(--muted)}
"""

PRINT_CSS = CSS_BASE + """
:root{--bg:#ffffff;--fg:#2b2b2b;--muted:#5a5a5a;--fact:#1f4e9e;--rule:#1d6b36;--tip:#6a3d9a;--trap:#a4161a}
@page{size:A4;margin:11mm 12mm}
body{font-size:10.2pt;line-height:1.58;text-align:justify;hyphens:auto}
h1{font-size:20pt;margin:0 0 .3em}
h2{font-size:15pt;margin:1.2em 0 .3em;break-before:page}
h2.nobreak{break-before:auto}
h3{font-size:12.5pt;margin:1em 0 .25em}
h4{font-size:10.6pt;margin:.8em 0 .15em}
h5{font-size:10pt;margin:.5em 0 0;font-weight:600}
ul,ol{margin:.2em 0 .5em;padding-left:1.3em}
li{margin:.08em 0}
p{margin:.25em 0 .45em}
.figure{max-width:150mm;margin-left:auto;margin-right:auto}
.toc a{text-decoration:none}
.toc li{text-align:left}
"""

DARK_CSS = CSS_BASE + """
:root{--bg:#000000;--fg:#f2f2f2;--muted:#b8b8b8;--fact:#7cc4ff;--rule:#6ee09a;--tip:#d0a8ff;--trap:#ff8a80}
@page{size:A4;margin:10mm 11mm;background:#000}
html,body{background:#000}
body{font-size:11.5pt;line-height:1.6}
main{max-width:920px;margin:0 auto;padding:16px}
h1{font-size:22pt}
h2{font-size:17pt;margin:1.3em 0 .3em;break-before:page}
h2.nobreak{break-before:auto}
h3{font-size:13.5pt;margin:1.1em 0 .3em}
h4{font-size:11.6pt;margin:.9em 0 .2em}
h5{font-size:11pt;margin:.5em 0 0;font-weight:600}
ul,ol{padding-left:1.3em}
@media screen{body{font-size:17px} main{padding:20px 16px 80px}}
"""


def legend_html():
    return ('<p class="legend">' + ''.join(
        f'<span class="c-{k}">{v[0]}</span>' for k, v in ROLES.items()) + '</p>')


def ul(items, cls=''):
    items = [i for i in (items or []) if str(i).strip()]
    if not items:
        return '<p>Not in source.</p>'
    return f'<ul class="{cls}">' + ''.join(f'<li>{esc(i)}</li>' for i in items) + '</ul>'


def mermaid_block(key, code, mer, live):
    if live:
        return f'<div class="figure mermaid-box"><pre class="mermaid">{esc(clean_mermaid(code))}</pre></div>'
    r = mer.get(key, {})
    if 'svg' in r:
        return f'<div class="figure mermaid-box">{r["svg"]}</div>'
    return '<p class="tag">Diagram failed to render.</p>'


def render_component(u, ci, c, src, mer, live, level=4):
    h = f'h{level}'
    a = []
    a.append(f'<h{level-1} id="{anchor(u["id"])}-c{ci}">{esc(c.get("name"))}</h{level-1}>')
    a.append(f'<{h}>1. Introduction and first principle</{h}>')
    a.append(f'<p><span class="lbl">{esc(c.get("first_principle"))}</span></p>')
    kf = c.get('key_facts') or []
    if kf:
        a.append('<ul>' + ''.join(
            f'<li class="c-fact">{esc(f.get("text"))}'
            + ('' if f.get('label', 'Fact') == 'Fact' else f' ({esc(f.get("label"))})')
            + f'{src.ref(f.get("url"))}</li>' for f in kf) + '</ul>')
    a.append(f'<{h}>2. Architecture</{h}>')
    svg = arch_svg(c.get("architecture", {}), c.get("name"))
    leg = ' '.join(f'{k+1}. {esc(t)}.' for k, t in enumerate(getattr(arch_svg, 'legend', [])))
    a.append(f'<div class="figure">{svg}<div class="cap">Schematic drawn from docs. Arrows: {leg} {ARCH_LEGEND}</div></div>')
    a.append(f'<{h}>3. How it works</{h}>')
    a.append('<ol>' + ''.join(f'<li>{esc(s)}</li>' for s in c.get('steps', [])) + '</ol>')
    a.append(f'<{h}>4. Pros and cons</{h}>')
    a.append('<h5>Pros</h5>' + ul(c.get('pros')) + '<h5>Cons</h5>' + ul(c.get('cons')))
    a.append(f'<{h}>5. Use when, do not use when</{h}>')
    a.append('<h5>Use when</h5>' + ul(c.get('use_when')) + '<h5>Do not use when</h5>' + ul(c.get('do_not_use_when')))
    a.append(f'<{h}>6. Constraint families</{h}>')
    cons = sorted(c.get('constraints', []), key=lambda x: FAMILY_ORDER.index(x.get('family', '').lower())
                  if x.get('family', '').lower() in FAMILY_ORDER else 99)
    for x in cons:
        comb = x.get('combination') or ''
        a.append(f'<h5>{esc(x.get("family", "").capitalize())}</h5><p class="c-rule">{esc(x.get("choice"))}'
                 + (f' Combination when one choice is not enough. {esc(comb)}' if comb.strip() else '') + '</p>')
    a.append(f'<{h}>7. Native cloud services</{h}>')
    for s in c.get('native_services', []):
        a.append(f'<h5>{esc(s.get("service"))}</h5><p>{esc(s.get("text"))}{src.ref(s.get("url"))}</p>')
    a.append(f'<{h}>8. Exam domain and task statement</{h}>')
    a.append(f'<p class="c-tip">{esc(c.get("exam_tie"))}</p>')
    if c.get('exam_tip'):
        a.append(f'<p class="c-tip">{esc(c.get("exam_tip"))}</p>')
    if c.get('decision_rule'):
        a.append(f'<p class="c-rule">{esc(c.get("decision_rule"))}</p>')
    a.append(f'<{h}>9. Trap</{h}>')
    a.append(f'<p class="c-trap">{esc(c.get("trap"))}</p>')
    a.append(f'<{h}>10. Not in source</{h}>')
    a.append(ul(c.get('not_in_source') or ['None recorded for this component.'], 'nis'))
    return ''.join(a)


def render_unit_full(dom, u, src, mer, live=False):
    a = [f'<section class="unit"><h2 id="{anchor(u["id"])}" class="unit-h">{esc(u["id"])} {esc(u["title"])}</h2>']
    a.append(f'<p class="tag">Domain {esc(dom["id"])}, {esc(dom["title"])}. Task statement: {esc(u.get("task_statement"))}</p>')
    for ci, c in enumerate(u.get('components', [])):
        a.append(render_component(u, ci, c, src, mer, live))
    if u.get('decision_flow'):
        a.append('<h3>Decision flow</h3>')
        a.append(mermaid_block(u['id'] + ':flow', u['decision_flow'], mer, live))
    nis = u.get('not_in_source') or []
    if nis:
        a.append('<h4>Unit items not in source</h4>' + ul(nis, 'nis'))
    for s in u.get('sources', []):
        src.num(s)
    a.append('</section>')
    return ''.join(a)


def topic_index_html(units, href=''):
    out, cur = ['<ol class="toc">'], None
    for dom, u in units:
        if dom['id'] != cur:
            if cur is not None:
                out.append('</ol></li>')
            cur = dom['id']
            out.append(f'<li><span class="lbl">{esc(dom["id"])} {esc(dom["title"])}</span>'
                       f' <span class="tag">Weight {esc(dom["weight"])}</span><ol>')
        comps = ', '.join(c.get('name', '') for c in u.get('components', []))
        out.append(f'<li><a href="{href}#{anchor(u["id"])}">{esc(u["id"])} {esc(u["title"])}</a>'
                   f' <span class="tag">{esc(comps)}</span></li>')
    out.append('</ol></li></ol>')
    return ''.join(out)


def page(title, css, body, extra_head=''):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{esc(title)}</title><style>{css}</style>{extra_head}</head><body>{body}</body></html>')


def mermaid_items(units):
    return {u['id'] + ':flow': u['decision_flow'] for _, u in units if u.get('decision_flow')}


MTV = {'dark': '{background:"#000000",primaryColor:"#000000",primaryTextColor:"#f2f2f2",primaryBorderColor:"#d0d0d0",lineColor:"#d0d0d0",secondaryColor:"#000000",tertiaryColor:"#000000",textColor:"#f2f2f2",edgeLabelBackground:"#000000",mainBkg:"#000000",nodeBorder:"#d0d0d0"}',
       'neutral': '{background:"#ffffff",primaryColor:"#ffffff",primaryTextColor:"#2b2b2b",primaryBorderColor:"#4a4a4a",lineColor:"#4a4a4a",secondaryColor:"#ffffff",tertiaryColor:"#ffffff",textColor:"#2b2b2b",edgeLabelBackground:"#ffffff",mainBkg:"#ffffff",nodeBorder:"#4a4a4a"}'}


def mermaid_live_script(theme):
    js = open(f'{BUILD}/node_modules/mermaid/dist/mermaid.min.js').read()
    return (f'<script>{js}</script><script>mermaid.initialize({{startOnLoad:true,theme:"base",themeVariables:{MTV[theme]},'
            f'securityLevel:"strict",fontFamily:"Inter, sans-serif",flowchart:{{htmlLabels:false}}}});</script>')
