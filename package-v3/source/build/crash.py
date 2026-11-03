"""Crash-course renderer. Web copy: pitch-black HTML with live Mermaid. Print copy: white A4 with pre-rendered Mermaid.
Diagrams: a schematic (SVG), a steps flowchart, and Mermaid mind maps (used in place of markmap, so the PDF builds offline).
Kept apart from build_all.py so the other outputs do not change."""
import base64, json, os, re
from pathlib import Path
from common import *
from render import legend_html, topic_index_html, page, ul

TXT = "'Charis SIL', Charis, Georgia, serif"
UI = "Inter, 'Inter Display', system-ui, -apple-system, 'Segoe UI', sans-serif"
FONT_DIR = str(Path(__file__).resolve().parents[3] / 'assets' / 'fonts')
PRACTICE = f'{WORK}/practice/items'
LETTERS = 'ABCD'
ARCH_NOTE = ('Box line style: heavy line is a Claude service, thin line is your system, '
             'long dash is a cloud provider, dots are a data store, dash-dot is a control.')

# Mermaid theme values. Keep equal to build/mermaid_render.js.
MM_VARS = {
    'dark': dict({'background': '#000000', 'primaryColor': '#000000', 'primaryTextColor': '#f2f2f2',
                  'primaryBorderColor': '#d0d0d0', 'lineColor': '#d0d0d0', 'secondaryColor': '#000000',
                  'tertiaryColor': '#000000', 'textColor': '#f2f2f2', 'edgeLabelBackground': '#000000',
                  'mainBkg': '#000000', 'nodeBorder': '#d0d0d0', 'fontSize': '15px'},
                 **{f'cScale{i}': '#141414' for i in range(12)}, **{f'cScaleLabel{i}': '#f2f2f2' for i in range(12)}),
    'neutral': dict({'background': '#ffffff', 'primaryColor': '#ffffff', 'primaryTextColor': '#1c1c1c',
                     'primaryBorderColor': '#4a4a4a', 'lineColor': '#4a4a4a', 'secondaryColor': '#ffffff',
                     'tertiaryColor': '#ffffff', 'textColor': '#1c1c1c', 'edgeLabelBackground': '#ffffff',
                     'mainBkg': '#ffffff', 'nodeBorder': '#4a4a4a', 'fontSize': '15px'},
                    **{f'cScale{i}': '#f1f1f1' for i in range(12)}, **{f'cScaleLabel{i}': '#1c1c1c' for i in range(12)}),
}
FLOW_CFG = {'htmlLabels': False, 'curve': 'basis', 'nodeSpacing': 22, 'rankSpacing': 28,
            'diagramPadding': 4, 'wrappingWidth': 140}

COMMON_CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:@TXT@;text-align:justify;hyphens:auto;-webkit-hyphens:auto;font-variant-numeric:lining-nums}
h1,h2,h3,h4,h5{font-family:@UI@;font-weight:650;line-height:1.3;color:var(--fg);text-align:left;hyphens:none;break-after:avoid}
p,li,.tag,.cap,.legend,ol.sources{line-height:var(--lh)}
p,li{margin:0 0 .55em}
li{margin:0 0 .25em}
ul,ol{margin:0 0 .6em;padding-left:1.3em}
sup.ref{font-size:.7em;line-height:0}
sup.ref a{text-decoration:none;color:var(--muted)}
.c-fact{color:var(--fact)}
.c-rule{color:var(--rule)}
.c-tip{color:var(--tip)}
.c-trap{color:var(--trap)}
.legend{font-family:@UI@;font-size:.85em;text-align:left;margin:0 0 .6em}
.legend span{margin-right:1.2em;white-space:nowrap}
.figure{margin:.6em 0 1em;break-inside:avoid;text-align:center}
.figure svg{max-width:100%;height:auto}
.cap{font-family:@UI@;font-size:.8em;color:var(--muted);text-align:left;margin:.35em 0 0}
.tag{font-family:@UI@;font-size:.8em;color:var(--muted);text-align:left;margin:0 0 .5em}
.lbl{font-weight:650}
.item{break-inside:avoid;margin:0 0 1.1em}
.opts{list-style:none;padding-left:0;margin:.3em 0 .5em}
.opts li{margin:0 0 .15em}
details{margin:.2em 0 .4em}
summary{font-family:@UI@;font-size:.85em;cursor:pointer;color:var(--muted)}
ol.sources{font-family:@UI@;font-size:.8em;text-align:left;word-break:break-all}
.nis li{color:var(--muted)}
"""

PRINT_CSS = """
:root{--bg:#ffffff;--fg:#1c1c1c;--muted:#555555;--fact:#1f4e9e;--rule:#1d6b36;--tip:#6a3d9a;--trap:#a4161a;--lh:1.55}
@page{size:A4;margin:14mm 15mm}
html,body{background:#ffffff;color:var(--fg)}
body{font-size:10.5pt}
h1{font-size:20pt;margin:0 0 .45em}
h2{font-size:15pt;margin:0 0 .5em;break-before:page}
h2.nobreak{break-before:auto}
h3{font-size:12.5pt;margin:1.2em 0 .45em}
h4{font-size:10.5pt;margin:1em 0 .35em}
h5{font-size:9.8pt;margin:.7em 0 .2em}
.figure svg{max-height:130mm;width:auto}
"""

DARK_CSS = """
:root{--bg:#000000;--fg:#f2f2f2;--muted:#bdbdbd;--fact:#7cc4ff;--rule:#6ee09a;--tip:#d0a8ff;--trap:#ff8a80;--lh:1.6}
html,body{background:#000000;color:var(--fg)}
body{font-size:18px}
main{max-width:44em;margin:0 auto;padding:28px 18px 120px}
h1{font-size:30px;margin:0 0 .5em}
h2{font-size:25px;margin:2.4em 0 .6em}
h3{font-size:21px;margin:1.6em 0 .5em}
h4{font-size:17px;margin:1.2em 0 .4em}
h5{font-size:16px;margin:.8em 0 .2em}
"""


def font_face():
    faces = [('CharisSIL-400-normal.woff2', 400, 'normal'), ('CharisSIL-700-normal.woff2', 700, 'normal'),
             ('CharisSIL-400-italic.woff2', 400, 'italic')]
    out = []
    for fn, w, st in faces:
        data = base64.b64encode(open(f'{FONT_DIR}/{fn}', 'rb').read()).decode()
        out.append("@font-face{font-family:'Charis SIL';src:url(data:font/woff2;base64," + data +
                   ") format('woff2');font-weight:" + str(w) + ";font-style:" + st + ";font-display:block}")
    return ''.join(out)


def css(theme_css):
    common = COMMON_CSS.replace('@TXT@', TXT).replace('@UI@', UI)
    return font_face() + common + theme_css


# ---------- Mermaid source builders ----------
_BAD = re.compile(r'["`\[\](){}<>|#;:&]')


def _m(s, n=None):
    """Plain label text for Mermaid. Removes syntax characters and trims long text at a word."""
    s = str(s or '').replace('—', ' ').replace('–', ' ')
    s = _BAD.sub(' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    if n and len(s) > n:
        s = s[:n].rsplit(' ', 1)[0] + ' ...'
    return s


def steps_code(steps):
    if not steps:
        return None
    lines = ['flowchart TD']
    for i, s in enumerate(steps):
        lines.append(f'  S{i}["{i + 1}. {_m(s, 100)}"]')
    for i in range(len(steps) - 1):
        lines.append(f'  S{i} --> S{i + 1}')
    return '\n'.join(lines)


def constraint_code(c):
    cons = sorted(c.get('constraints') or [], key=family_rank)
    if not cons:
        return None
    lines = ['mindmap', f'  root[{_m(c.get("name"), 70)}]']
    for x in cons:
        lines.append('    ' + _m(x.get('family', '').capitalize(), 40))
        text = x.get('choice') or ''
        if (x.get('combination') or '').strip():
            text += ' ' + x['combination']
        lines.append('      ' + _m(text, 190))
    return '\n'.join(lines)


def decide_code(c):
    use, avoid = c.get('use_when') or [], c.get('do_not_use_when') or []
    if not use and not avoid:
        return None
    lines = ['mindmap', f'  root[{_m(c.get("name"), 70)}]', '    Use when']
    lines += ['      ' + _m(t, 120) for t in use]
    lines.append('    Do not use when')
    lines += ['      ' + _m(t, 120) for t in avoid]
    return '\n'.join(lines)


def platform_code(c):
    svcs = c.get('native_services') or []
    if not svcs:
        return None
    lines = ['mindmap', '  root[Native cloud services]']
    for s in svcs:
        lines.append('    ' + _m(s.get('service'), 60))
        lines.append('      ' + _m(s.get('text'), 130))
    return '\n'.join(lines)


def drill_code(u):
    pats = u.get('patterns') or []
    if not pats:
        return None
    lines = ['mindmap', f'  root[{_m("Question drill " + u["id"], 60)}]']
    for p in pats:
        lines.append('    ' + _m(p.get('wording'), 110))
        lines.append('      ' + _m(p.get('answer_type'), 110))
        lines.append('      ' + _m(p.get('rule'), 130))
        lines += ['      Trap ' + _m(t, 110) for t in p.get('traps') or []]
    return '\n'.join(lines)


def diagram_items(units):
    items = {}
    for _, u in units:
        uid = u['id']
        items[f'{uid}:flow'] = u.get('decision_flow')
        items[f'{uid}:drill'] = drill_code(u)
        for ci, c in enumerate(u.get('components', [])):
            k = f'{uid}:c{ci}'
            items[f'{k}:steps'] = steps_code(c.get('steps'))
            items[f'{k}:constraints'] = constraint_code(c)
            items[f'{k}:decide'] = decide_code(c)
            items[f'{k}:platforms'] = platform_code(c)
    return {k: v for k, v in items.items() if v}


def family_rank(x):
    f = x.get('family', '').lower()
    return FAMILY_ORDER.index(f) if f in FAMILY_ORDER else 99


# ---------- HTML parts ----------
def figure(key, codes, dia, live, caption):
    if key not in codes:
        return ''
    if live:
        inner = f'<pre class="mermaid">{esc(clean_mermaid(codes[key]))}</pre>'
    else:
        inner = dia.get(key, {}).get('svg') or '<p class="tag">Diagram failed to render.</p>'
    return f'<figure class="figure">{inner}<figcaption class="cap">{esc(caption)}</figcaption></figure>'


def arch_figure(c):
    svg = arch_svg(c.get('architecture', {}), c.get('name'))
    if not svg:
        return ''
    leg = ' '.join(f'{i + 1}. {esc(t)}.' for i, t in enumerate(getattr(arch_svg, 'legend', [])))
    return (f'<figure class="figure">{svg}<figcaption class="cap">Schematic drawn from the docs. '
            f'Arrow labels: {leg} {esc(ARCH_NOTE)}</figcaption></figure>')


def component_html(uid, ci, c, src, codes, dia, live):
    k = f'{uid}:c{ci}'
    a = [f'<h3 id="{anchor(uid)}-c{ci}">{esc(c.get("name"))}</h3>',
         '<h4>1. First principle</h4>',
         f'<p><span class="lbl">{esc(c.get("first_principle"))}</span></p>']
    kf = c.get('key_facts') or []
    if kf:
        a.append('<ul>' + ''.join(
            f'<li class="c-fact">{esc(f.get("text"))}'
            + ('' if f.get('label', 'Fact') == 'Fact' else f' ({esc(f.get("label"))})')
            + f'{src.ref(f.get("url"))}</li>' for f in kf) + '</ul>')
    a += ['<h4>2. Architecture</h4>', arch_figure(c)]
    a += ['<h4>3. How it works</h4>',
          '<ol>' + ''.join(f'<li>{esc(s)}</li>' for s in c.get('steps', [])) + '</ol>',
          figure(f'{k}:steps', codes, dia, live, 'Steps, from first to last.')]
    a.append('<h4>4. Constraint families</h4>')
    for x in sorted(c.get('constraints') or [], key=family_rank):
        comb = (x.get('combination') or '').strip()
        a.append(f'<h5>{esc(x.get("family", "").capitalize())}</h5>'
                 f'<p class="c-rule">{esc(x.get("choice"))}'
                 + (f' If one choice is not enough: {esc(comb)}' if comb else '') + '</p>')
    a.append(figure(f'{k}:constraints', codes, dia, live, 'Each constraint family, its choice, and its combination.'))
    a += ['<h4>5. Pros and cons</h4>', '<h5>Pros</h5>', ul(c.get('pros')), '<h5>Cons</h5>', ul(c.get('cons'))]
    a += ['<h4>6. Use when and do not use when</h4>', '<h5>Use when</h5>', ul(c.get('use_when')),
          '<h5>Do not use when</h5>', ul(c.get('do_not_use_when')),
          figure(f'{k}:decide', codes, dia, live, 'Use and avoid conditions for this component.')]
    a.append('<h4>7. Native cloud services</h4>')
    for s in c.get('native_services', []):
        a.append(f'<h5>{esc(s.get("service"))}</h5><p>{esc(s.get("text"))}{src.ref(s.get("url"))}</p>')
    a.append(figure(f'{k}:platforms', codes, dia, live, 'Native cloud services. Each branch gives the text from the docs.'))
    a.append('<h4>8. Exam tie, decision rule, and trap</h4>')
    a.append(f'<p class="c-tip">{esc(c.get("exam_tie"))}</p>')
    if c.get('exam_tip'):
        a.append(f'<p class="c-tip">{esc(c.get("exam_tip"))}</p>')
    if c.get('decision_rule'):
        a.append(f'<p class="c-rule">{esc(c.get("decision_rule"))}</p>')
    a.append(f'<p class="c-trap">{esc(c.get("trap"))}</p>')
    a.append('<h4>9. Not in source</h4>' + ul(c.get('not_in_source') or ['None recorded for this component.'], 'nis'))
    return ''.join(a)


def practice_items(uid):
    fn = f'{PRACTICE}/{uid}.json'
    return json.load(open(fn)).get('items', []) if os.path.exists(fn) else []


def answer_text(it, src):
    ans = ', '.join(LETTERS[c] for c in it.get('correct', []))
    return (f'<p><span class="lbl">Answer: {ans}.</span> {esc(it.get("rationale"))}</p>'
            f'<p class="c-trap">Trap. {esc(it.get("trap"))}</p>'
            f'<p class="tag">Source. {src.ref(it.get("source"))}</p>')


def item_html(it, src, mode):
    prompt = 'Select one answer.' if it.get('select', 1) == 1 else 'Select two answers.'
    opts = ''.join(f'<li><span class="lbl">{LETTERS[k]}.</span> {esc(o)}</li>' for k, o in enumerate(it.get('options', [])))
    h = [f'<div class="item"><p><span class="lbl">{esc(it.get("id"))}.</span> {esc(it.get("stem"))}</p>',
         f'<p class="tag">{prompt}</p><ul class="opts">{opts}</ul>']
    if mode == 'web':
        h.append('<details><summary>Show answer</summary>' + answer_text(it, src) + '</details>')
    h.append('</div>')
    return ''.join(h)


def unit_html(dom, u, src, codes, dia, live, mode):
    uid = u['id']
    a = [f'<section class="unit"><h2 id="{anchor(uid)}">{esc(uid)} {esc(u.get("title"))}</h2>',
         f'<p class="tag">Domain {esc(dom["id"])}, {esc(dom["title"])}. Task statement: {esc(u.get("task_statement"))}</p>']
    for ci, c in enumerate(u.get('components', [])):
        a.append(component_html(uid, ci, c, src, codes, dia, live))
    a.append(figure(f'{uid}:flow', codes, dia, live, 'Decision flow for this unit. Start at the top and follow the labels.'))
    a.append(figure(f'{uid}:drill', codes, dia, live,
                    'Question drill. Each branch gives a wording, the answer type, the rule, and the traps.'))
    items = practice_items(uid)
    if items:
        a.append('<h4>Practice checks</h4>')
        a.append('<p class="tag">Select the answer that meets every constraint in the stem. '
                 'The items are original. They do not copy any exam item.</p>')
        a += [item_html(it, src, mode) for it in items]
    nis = u.get('not_in_source') or []
    if nis:
        a.append('<h4>Unit items not in source</h4>' + ul(nis, 'nis'))
    a.append('</section>')
    return ''.join(a)


def answer_key(units, src):
    parts = ['<h2>Answer key</h2>']
    for _, u in units:
        items = practice_items(u['id'])
        if not items:
            continue
        parts.append(f'<h4>{esc(u["id"])} {esc(u.get("title"))}</h4>')
        parts += [f'<div class="item"><p><span class="lbl">{esc(it.get("id"))}.</span></p>'
                  + answer_text(it, src) + '</div>' for it in items]
    return ''.join(parts)


def title_for(sample):
    return 'Claude Certified Architect, Professional. Crash course' + (' sample chapter' if sample else '')


def body(units, live, theme, mode):
    src = Sources()
    codes = diagram_items(units)
    dia = {} if live else render_mermaid(codes, theme)
    parts = ['<main>', legend_html(),
             '<p>Each unit has the same parts. Each component gives a first principle, an architecture schematic, '
             'steps, constraint choices, use and avoid conditions, native services, and a trap. '
             'The diagrams show the same content in another form. Each unit ends with practice checks.</p>',
             '<h2 class="nobreak">Topic index</h2>', topic_index_html(units)]
    for dom, u in units:
        parts.append(unit_html(dom, u, src, codes, dia, live, mode))
    if mode == 'print':
        parts.append(answer_key(units, src))
    parts.append('<h2>Sources</h2>' + src.html() + '</main>')
    return ''.join(parts)


def live_script():
    js = open(f'{BUILD}/node_modules/mermaid/dist/mermaid.min.js').read()
    cfg = {'startOnLoad': True, 'theme': 'base', 'themeVariables': MM_VARS['dark'],
           'securityLevel': 'strict', 'fontFamily': 'Inter, sans-serif', 'flowchart': FLOW_CFG}
    return f'<script>{js}</script><script>mermaid.initialize({json.dumps(cfg)});</script>'


def build_web(units, sample=False):
    return page(title_for(sample), css(DARK_CSS), body(units, True, 'dark', 'web'), live_script())


def build_print(units, sample=False):
    return page(title_for(sample), css(PRINT_CSS), body(units, False, 'neutral', 'print'))
