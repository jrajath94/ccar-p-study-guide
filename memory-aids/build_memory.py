#!/usr/bin/env python3
"""Memory aids: an exam-wide map, one page per chapter, and one card per section.
Usage: python3 build_memory.py
Reads package-v3/source (topics.json and units) and memory-aids/hooks.json.
Writes web pages (black theme) to memory-aids/ and print pages (white theme) to memory-aids/print/.
Each page carries d3 inline, so each file works offline. Run build_pdf.py after this to make the PDFs."""
import base64, html, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / 'package-v3' / 'source'
FONTS = HERE.parent / 'assets' / 'fonts'
D3 = (HERE / 'vendor' / 'd3.min.js').read_text()
TOPICS = json.loads((SRC / 'topics.json').read_text())
HOOKS = json.loads((HERE / 'hooks.json').read_text())

UNITS = {}
for p in sorted((SRC / 'units').glob('*.json')):
    unit = json.loads(p.read_text())
    UNITS[unit['id']] = unit

FAMILY_ORDER = ['latency', 'cost', 'quota', 'data location', 'isolation', 'governance', 'scale', 'skill', 'operations']
# Colors from the archify semantic palette, one per constraint family and one per chapter.
FAM_COLOR = {'latency': '#22D3EE', 'cost': '#FBBF24', 'quota': '#FB923C', 'data location': '#A78BFA',
             'isolation': '#FB7185', 'governance': '#60A5FA', 'scale': '#34D399', 'skill': '#F472B6',
             'operations': '#94A3B8'}
DOM_COLOR = {'F': '#94A3B8', 'D1': '#22D3EE', 'D2': '#34D399', 'D3': '#A78BFA', 'D4': '#FBBF24',
             'D5': '#FB7185', 'D6': '#FB923C', 'D7': '#60A5FA'}
THEMES = {
    'web': {'bg': '#000000', 'panel': '#0B0B0B', 'line': '#262626', 'fg': '#F2F2F2', 'muted': '#A3A3A3',
            'chip': '#000000', 'rule': '#6EE09A', 'trap': '#FF8A80', 'tip': '#D0A8FF'},
    'print': {'bg': '#FFFFFF', 'panel': '#FFFFFF', 'line': '#CFCFCF', 'fg': '#1C1C1C', 'muted': '#555555',
              'chip': '#000000', 'rule': '#1D6B36', 'trap': '#A4161A', 'tip': '#6A3D9A'},
}
NUM = re.compile(r'\d')


def esc(s):
    return html.escape(str(s if s is not None else ''), quote=True)


def sjson(obj):
    return json.dumps(obj, ensure_ascii=False).replace('</', '<\\/')


def family_counts(units):
    counts = {f: 0 for f in FAMILY_ORDER}
    for u in units:
        for comp in u.get('components', []):
            for x in comp.get('constraints', []):
                fam = (x.get('family') or '').lower()
                if fam in counts:
                    counts[fam] += 1
    return counts


def number_facts(units):
    rows = []
    for u in units:
        for comp in u.get('components', []):
            for f in comp.get('key_facts', []):
                if NUM.search(f.get('text', '')):
                    rows.append((u['id'], comp.get('name', ''), f))
    return rows


def sections():
    """Return [(domain, [(unit id, title, unit)])] in topic order. Units missing from the source are skipped."""
    out = []
    for dom in TOPICS['domains']:
        rows = []
        for uid, title, _ in dom['units']:
            if uid in UNITS:
                rows.append((uid, UNITS[uid].get('title') or title, UNITS[uid]))
        out.append((dom, rows))
    return out


SECTIONS = sections()
ALL_UNITS = [u for _, rows in SECTIONS for _, _, u in rows]


def b64(name):
    return base64.b64encode((FONTS / name).read_bytes()).decode()


CSS = """
@font-face{font-family:'Charis SIL';src:url(data:font/woff2;base64,@R@) format('woff2');font-weight:400;font-style:normal;font-display:block}
@font-face{font-family:'Charis SIL';src:url(data:font/woff2;base64,@B@) format('woff2');font-weight:700;font-style:normal;font-display:block}
:root{--bg:@bg@;--panel:@panel@;--line:@line@;--fg:@fg@;--muted:@muted@;--rule:@rule@;--trap:@trap@;--tip:@tip@;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--serif:'Charis SIL',Georgia,serif}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--fg)}
body{font-family:var(--serif);font-size:17px;line-height:1.6;text-align:justify;hyphens:auto;-webkit-hyphens:auto}
main{max-width:1180px;margin:0 auto;padding:28px 18px 96px}
a{color:var(--fg)}
h1{font-family:var(--mono);font-size:30px;line-height:1.2;margin:6px 0 10px;text-align:left;letter-spacing:-.02em}
h2{font-family:var(--mono);font-size:16px;line-height:1.3;margin:44px 0 14px;text-align:left;text-transform:uppercase;letter-spacing:.08em}
h3{font-family:var(--mono);font-size:17px;line-height:1.35;margin:0 0 8px;text-align:left}
h4{font-family:var(--mono);font-size:12px;line-height:1.4;margin:16px 0 4px;text-align:left;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
p{margin:0 0 8px}
.label{font-family:var(--mono);font-size:11px;line-height:1.4;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 6px;text-align:left}
.hook{font-family:var(--mono);font-size:19px;line-height:1.4;font-weight:700;text-align:left;margin:10px 0 14px}
.cap{font-family:var(--mono);font-size:12px;line-height:1.5;color:var(--muted);text-align:left}
.chip{display:inline-block;font-family:var(--mono);font-size:12px;font-weight:700;line-height:1;padding:5px 9px;border-radius:999px;color:@chip@;margin-right:10px;vertical-align:middle}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:0 0 18px;break-inside:avoid}
.card h3{margin-top:8px}
b.rule{color:var(--rule);font-weight:700}
b.trap{color:var(--trap);font-weight:700}
b.tip{color:var(--tip);font-weight:700}
.cue{font-family:var(--mono);font-size:13px;font-weight:700}
.fam{margin:4px 0 6px;max-width:760px}
.fam svg{display:block;width:100%;height:auto}
.fam text{font-family:var(--mono)}
.scroll{overflow-x:auto;padding-bottom:6px}
#concept svg{display:block}
#concept text{font-family:var(--mono)}
details{border-top:1px solid var(--line);padding:6px 0}
summary{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;cursor:pointer;color:var(--muted);padding:4px 0}
details ol,details ul{margin:8px 0 6px;padding-left:20px}
details li{margin:0 0 8px;text-align:left}
details li ul{margin:4px 0 0}
.nav{margin:14px 0 0}
.nav a{font-family:var(--mono);font-size:12px;text-decoration:none;border:1px solid var(--line);padding:4px 10px;border-radius:999px;margin:0 6px 6px 0;display:inline-block}
.grid2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;align-items:start}
#radial{min-width:0}
#panel{min-width:0}
#radial svg{display:block;width:100%;height:auto}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:8px;vertical-align:middle}
.legend-list{list-style:none;margin:0;padding:0;font-family:var(--mono);font-size:13px}
.legend-list li{padding:6px 0;border-bottom:1px solid var(--line);text-align:left}
.rules{list-style:none;margin:0;padding:0;counter-reset:r}
.rules li{counter-increment:r;position:relative;padding:9px 0 9px 46px;border-bottom:1px solid var(--line);text-align:left}
.rules li::before{content:counter(r);position:absolute;left:0;top:8px;font-family:var(--mono);font-weight:700;font-size:15px;color:var(--c)}
table{width:100%;border-collapse:collapse;font-size:15px;line-height:1.5}
th,td{border-bottom:1px solid var(--line);padding:8px 8px;text-align:left;vertical-align:top}
th{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
td .chip{margin-right:0}
input.filter{width:100%;max-width:420px;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-family:var(--mono);font-size:14px;margin:4px 0 12px}
a.src{font-family:var(--mono);font-size:12px}
@media (max-width:860px){.grid2{grid-template-columns:minmax(0,1fr)} body{font-size:16px} main{padding:20px 14px 80px} h1{font-size:24px}}
@media print{@page{size:A4;margin:12mm} body{font-size:10.5pt} h2{break-after:avoid} .card,details{break-inside:avoid} input.filter{display:none} .scroll{overflow:visible}}
"""

COMMON_JS = """
function famBars(el, counts) {
  const keys = Object.keys(counts);
  const max = Math.max(1, ...Object.values(counts));
  const width = Math.max(300, el.clientWidth || 640);
  const left = 130, rowH = 22, barW = width - left - 44;
  const svg = d3.select(el).append('svg')
    .attr('viewBox', [0, 0, width, keys.length * rowH + 4])
    .attr('role', 'img').attr('aria-label', 'Constraint family counts for this section');
  const row = svg.selectAll('g').data(keys).join('g')
    .attr('transform', (d, i) => `translate(0,${i * rowH})`);
  row.append('text').attr('x', 0).attr('y', 15).attr('fill', THEME.muted).attr('font-size', 12).text(d => d);
  row.append('rect').attr('x', left).attr('y', 4).attr('width', barW).attr('height', 14).attr('rx', 3).attr('fill', THEME.line);
  row.filter(d => counts[d] > 0).append('rect')
    .attr('x', left).attr('y', 4).attr('height', 14).attr('rx', 3)
    .attr('width', d => barW * counts[d] / max).attr('fill', d => FAM[d]);
  row.append('text').attr('x', left + barW + 10).attr('y', 15).attr('fill', THEME.fg)
    .attr('font-size', 12).attr('font-weight', 700).text(d => counts[d]);
}

function conceptTree(el, data) {
  const root = d3.hierarchy(data);
  const dx = 30, dy = 440;
  d3.tree().nodeSize([dx, dy])(root);
  let x0 = Infinity, x1 = -Infinity;
  root.each(d => { if (d.x < x0) x0 = d.x; if (d.x > x1) x1 = d.x; });
  const h = x1 - x0 + dx * 2, w = dy * 2 + 440;
  const svg = d3.select(el).append('svg')
    .attr('width', w).attr('height', h).attr('viewBox', [-16, x0 - dx, w, h]);
  svg.append('g').attr('fill', 'none').attr('stroke', THEME.line).attr('stroke-width', 1.4)
    .selectAll('path').data(root.links()).join('path')
    .attr('d', d3.linkHorizontal().x(d => d.y).y(d => d.x));
  const node = svg.append('g').selectAll('g').data(root.descendants()).join('g')
    .attr('transform', d => `translate(${d.y},${d.x})`);
  node.append('circle')
    .attr('r', d => d.depth === 0 ? 8 : d.depth === 1 ? 6 : 4.5)
    .attr('fill', d => d.depth === 2 ? THEME.bg : (d.data.color || THEME.fg))
    .attr('stroke', d => d.data.color || THEME.fg).attr('stroke-width', 2);
  node.append('text').attr('x', 14).attr('dy', '0.32em')
    .attr('fill', THEME.fg)
    .attr('font-size', d => d.depth === 1 ? 13 : 12)
    .attr('font-weight', d => d.depth === 1 ? 700 : 400)
    .text(d => d.data.name);
}

function radialTree(el, data, onSelect) {
  const root = d3.hierarchy(data);
  const radius = 330, margin = 110;
  d3.cluster().size([2 * Math.PI, radius])(root);
  const size = 2 * (radius + margin);
  const svg = d3.select(el).append('svg')
    .attr('viewBox', [-size / 2, -size / 2, size, size])
    .attr('role', 'img').attr('aria-label', 'Exam map. Select a section.');
  svg.append('g').attr('fill', 'none').attr('stroke', THEME.line).attr('stroke-width', 1.2)
    .selectAll('path').data(root.links()).join('path')
    .attr('d', d3.linkRadial().angle(d => d.x).radius(d => d.y));
  const node = svg.append('g').selectAll('g').data(root.descendants()).join('g')
    .attr('transform', d => `rotate(${d.x * 180 / Math.PI - 90}) translate(${d.y},0)`)
    .style('cursor', d => d.depth === 2 ? 'pointer' : 'default')
    .on('click', (event, d) => { if (d.depth === 2) onSelect(d.data); });
  node.append('circle')
    .attr('r', d => d.depth === 2 ? 6 : d.depth === 1 ? 9 : 11)
    .attr('fill', d => d.data.color || THEME.fg).attr('stroke', THEME.bg).attr('stroke-width', 1.5);
  node.append('text').attr('dy', '0.32em')
    .attr('x', d => (d.x < Math.PI) === !d.children ? 11 : -11)
    .attr('text-anchor', d => (d.x < Math.PI) === !d.children ? 'start' : 'end')
    .attr('transform', d => d.x >= Math.PI ? 'rotate(180)' : null)
    .attr('fill', d => d.depth === 2 ? d.data.color : THEME.fg)
    .attr('font-family', 'ui-monospace, Menlo, Consolas, monospace')
    .attr('font-size', 12).attr('font-weight', d => d.depth === 2 ? 400 : 700)
    .text(d => d.data.label);
  node.append('title').text(d => d.data.full || d.data.label);
}

function donut(el, counts) {
  const entries = Object.entries(counts).filter(e => e[1] > 0);
  const total = d3.sum(entries, e => e[1]);
  const size = 280, r = 130, ir = 72;
  const svg = d3.select(el).append('svg')
    .attr('viewBox', [-size / 2, -size / 2, size, size]).attr('width', 280).attr('height', 280)
    .attr('role', 'img').attr('aria-label', 'Constraint family totals across all sections');
  const arc = d3.arc().innerRadius(ir).outerRadius(r);
  svg.selectAll('path').data(d3.pie().value(e => e[1]).sort(null)(entries)).join('path')
    .attr('d', arc).attr('fill', d => FAM[d.data[0]])
    .attr('stroke', THEME.bg).attr('stroke-width', 2);
  svg.append('text').attr('text-anchor', 'middle').attr('dy', '0.35em')
    .attr('fill', THEME.fg).attr('font-size', 30).attr('font-weight', 700)
    .attr('font-family', 'ui-monospace, Menlo, Consolas, monospace').text(total);
}

function filterTable(input) {
  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    document.querySelectorAll('#' + input.dataset.target + ' tbody tr').forEach(tr => {
      tr.hidden = q !== '' && !tr.textContent.toLowerCase().includes(q);
    });
  });
}
"""


def card_html(dom, uid, title, u, mode):
    hook = HOOKS['units'].get(uid, '')
    opn = ' open' if mode == 'print' else ''
    parts = [f'<article class="card" id="{esc(uid)}">',
             f'<p><span class="chip" style="background:{DOM_COLOR[dom["id"]]}">{esc(uid)}</span>'
             f'<span class="label">Chapter {esc(dom["id"])}, {esc(dom["title"])}</span></p>',
             f'<h3>{esc(title)}</h3>',
             f'<p class="hook">{esc(hook)}</p>',
             '<h4>Constraint families</h4>',
             f'<div class="fam" data-counts="{esc(json.dumps(family_counts([u]), ensure_ascii=False))}"></div>']
    for comp in u.get('components', []):
        parts.append(f'<h4>{esc(comp.get("name"))}</h4>')
        if comp.get('first_principle'):
            parts.append(f'<p>{esc(comp["first_principle"])}</p>')
        parts.append(f'<p><b class="rule">Rule</b> {esc(comp.get("decision_rule"))}</p>')
        parts.append(f'<p><b class="trap">Trap</b> {esc(comp.get("trap"))}</p>')
        if comp.get('exam_tip'):
            parts.append(f'<p><b class="tip">Exam tip</b> {esc(comp.get("exam_tip"))}</p>')
    pats = u.get('patterns') or []
    if pats:
        items = []
        for pt in pats:
            traps = ''.join(f'<li>{esc(t)}</li>' for t in pt.get('traps') or [])
            items.append(f'<li><span class="cue">{esc(pt.get("wording"))}</span><br>'
                         f'<b class="rule">Answer</b> {esc(pt.get("answer_type"))}<br>'
                         f'<b class="rule">Rule</b> {esc(pt.get("rule"))}'
                         + (f'<ul>{traps}</ul>' if traps else '') + '</li>')
        parts.append(f'<details{opn}><summary>Recall cues ({len(pats)})</summary><ol>{"".join(items)}</ol></details>')
    nums = number_facts([u])
    if nums:
        items = ''.join(f'<li>{esc(f.get("text"))} <a class="src" href="{esc(f.get("url"))}">source</a></li>'
                        for _, _, f in nums)
        parts.append(f'<details{opn}><summary>Numbers and versions ({len(nums)})</summary><ul>{items}</ul></details>')
    parts.append('</article>')
    return ''.join(parts)


def chapter_tree(dom, rows):
    col = DOM_COLOR[dom['id']]
    return {'name': f'{dom["id"]} {dom["title"]}', 'color': col, 'children': [
        {'name': f'{uid} {title}', 'color': col,
         'children': [{'name': c.get('name', ''), 'color': col} for c in u.get('components', [])]}
        for uid, title, u in rows]}


def exam_tree():
    kids = []
    for dom, rows in SECTIONS:
        col = DOM_COLOR[dom['id']]
        kids.append({'label': dom['id'], 'full': dom['title'], 'color': col, 'children': [
            {'label': uid, 'full': f'{uid} {title}', 'color': col} for uid, title, _ in rows]})
    return {'label': 'Exam', 'full': 'Claude Certified Architect, Professional', 'children': kids}


def css(mode):
    th = THEMES[mode]
    s = CSS.replace('@R@', b64('CharisSIL-400-normal.woff2')).replace('@B@', b64('CharisSIL-700-normal.woff2'))
    for k, v in th.items():
        s = s.replace('@' + k + '@', v)
    return s


def preamble(mode):
    th = THEMES[mode]
    return ('const THEME = ' + sjson({'fg': th['fg'], 'muted': th['muted'], 'line': th['line'], 'bg': th['bg']}) + ';\n'
            'const FAM = ' + sjson(FAM_COLOR) + ';\n' + COMMON_JS)


def page(title, mode, body, init_js):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{esc(title)}</title><style>{css(mode)}</style></head>'
            f'<body><main>{body}</main>'
            f'<script>{D3}</script><script>{preamble(mode)}{init_js}</script></body></html>')


def nav_html(here, mode):
    """Web pages only. Links go to the exam map and to each chapter."""
    if mode == 'print':
        return ''
    chap = [f'<a href="{"" if here != "exam" else "chapters/"}{d["id"]}.html">{d["id"]}</a>' for d, _ in SECTIONS]
    if here == 'exam':
        return '<p class="nav">' + ''.join(chap) + '</p>'
    return '<p class="nav"><a href="../exam-map.html">Exam map</a>' + ''.join(chap) + '</p>'


def chapter_page(dom, rows, mode):
    ncomp = sum(len(u.get('components', [])) for _, _, u in rows)
    ncue = sum(len(u.get('patterns') or []) for _, _, u in rows)
    weight = dom.get('weight', '')
    weight_line = ('Foundations. Not weighted.' if weight == 'Not weighted'
                   else f'Weight {weight}. Inference from secondary sources.')
    head = ('<header>'
            f'<p class="label">Chapter {esc(dom["id"])}</p>'
            f'<h1>{esc(dom["title"])}</h1>'
            f'<p class="label">{esc(weight_line)}</p>'
            f'<p class="hook">{esc(HOOKS["chapters"][dom["id"]])}</p>'
            f'<p class="cap">{len(rows)} sections, {ncomp} components, {ncue} recall cues.</p>'
            + nav_html(dom['id'], mode) + '</header>')
    body = (head + '<h2>Concept map</h2>'
            '<p class="cap">Units branch to components. On a small screen, scroll sideways.</p>'
            '<div class="scroll"><div id="concept"></div></div>'
            '<h2>Sections</h2>'
            + ''.join(card_html(dom, uid, title, u, mode) for uid, title, u in rows))
    init = (f'const TREE = {sjson(chapter_tree(dom, rows))};\n'
            'conceptTree(document.getElementById("concept"), TREE);\n'
            'document.querySelectorAll(".fam").forEach(el => famBars(el, JSON.parse(el.dataset.counts)));')
    return page(f'{dom["id"]} {dom["title"]}. Memory aids', mode, body, init)


def exam_page(mode):
    n_comp = sum(len(u.get('components', [])) for u in ALL_UNITS)
    n_cue = sum(len(u.get('patterns') or []) for u in ALL_UNITS)
    nums = [(uid, comp, f) for uid, comp, f in number_facts(ALL_UNITS)]
    fam_total = family_counts(ALL_UNITS)
    rules = ''.join(
        f'<li style="--c:{DOM_COLOR[SECTIONS[i % len(SECTIONS)][0]["id"]]}">{esc(t)}</li>'
        for i, t in enumerate(HOOKS['exam_rules']))
    chapters_legend = ''.join(
        f'<li><span class="dot" style="background:{DOM_COLOR[d["id"]]}"></span>{esc(d["id"])} {esc(d["title"])}</li>'
        for d, _ in SECTIONS)
    fam_legend = ''.join(
        f'<li><span class="dot" style="background:{FAM_COLOR[f]}"></span>{esc(f)}, {fam_total[f]}</li>'
        for f in FAMILY_ORDER)
    sec_rows = ''.join(
        f'<tr><td><span class="chip" style="background:{DOM_COLOR[dom["id"]]}">{esc(uid)}</span></td>'
        f'<td>{esc(title)}</td><td>{esc(HOOKS["units"].get(uid, ""))}</td></tr>'
        for dom, rows in SECTIONS for uid, title, _ in rows)
    num_rows = ''.join(
        f'<tr><td><span class="chip" style="background:{DOM_COLOR[UNIT_DOM[uid]]}">{esc(uid)}</span></td>'
        f'<td>{esc(f.get("text"))}</td><td><a class="src" href="{esc(f.get("url"))}">source</a></td></tr>'
        for uid, _, f in nums)
    head = ('<header>'
            '<p class="label">Exam map</p>'
            '<h1>Claude Certified Architect, Professional. Memory sheet</h1>'
            '<p class="hook">Seven chapters, 42 sections, and ten rules that cut across them.</p>'
            f'<p class="cap">{len(ALL_UNITS)} sections, {n_comp} components, {n_cue} recall cues, '
            f'{len(nums)} numbers and versions.</p>'
            + nav_html('exam', mode) + '</header>')
    panel = ('<div id="panel"><p class="cap">Select a section on the map to open its card.</p></div>'
             if mode == 'web' else '')
    body = (head
            + '<h2>Ten rules</h2><ol class="rules">' + rules + '</ol>'
            + '<h2>Map</h2>'
            + '<p class="cap">Inner ring: chapters. Outer ring: sections. Select a section to open its card.</p>'
            + '<div class="grid2"><div id="radial"></div>' + panel + '</div>'
            + '<h2>Chapters</h2><ul class="legend-list">' + chapters_legend + '</ul>'
            + '<h2>Constraint families across all sections</h2>'
            + '<div class="grid2"><div id="donut"></div><ul class="legend-list">' + fam_legend + '</ul></div>'
            + '<h2>Sections</h2>'
            + ('<input class="filter" data-target="sections-table" placeholder="Filter sections">' if mode == 'web' else '')
            + '<table id="sections-table"><thead><tr><th>Section</th><th>Title</th><th>Memory hook</th></tr></thead>'
            + f'<tbody>{sec_rows}</tbody></table>'
            + '<h2>Numbers and versions</h2>'
            + ('<input class="filter" data-target="numbers-table" placeholder="Filter numbers, for example Haiku">' if mode == 'web' else '')
            + '<table id="numbers-table"><thead><tr><th>Section</th><th>Fact</th><th>Source</th></tr></thead>'
            + f'<tbody>{num_rows}</tbody></table>')
    if mode == 'web':
        for dom, rows in SECTIONS:
            for uid, title, u in rows:
                body += f'<template id="tpl-{esc(uid)}">{card_html(dom, uid, title, u, mode)}</template>'
    init = (f'const TREE = {sjson(exam_tree())};\n'
            'donut(document.getElementById("donut"), ' + sjson(fam_total) + ');\n'
            + ('radialTree(document.getElementById("radial"), TREE, showSection);\n'
               'function showSection(d) {\n'
               '  const tpl = document.getElementById("tpl-" + d.label);\n'
               '  const panel = document.getElementById("panel");\n'
               '  panel.replaceChildren(tpl.content.cloneNode(true));\n'
               '  panel.querySelectorAll(".fam").forEach(el => famBars(el, JSON.parse(el.dataset.counts)));\n'
               '  panel.scrollIntoView({behavior: "smooth", block: "nearest"});\n'
               '}\n'
               'document.querySelectorAll("input[data-target]").forEach(filterTable);'
               if mode == 'web' else
               'radialTree(document.getElementById("radial"), TREE, () => {});'))
    return page('Claude Certified Architect, Professional. Memory sheet', mode, body, init)


UNIT_DOM = {uid: dom['id'] for dom, rows in SECTIONS for uid, _, _ in rows}


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print('wrote', path.relative_to(HERE.parent))


def main():
    for mode, base in (('web', HERE), ('print', HERE / 'print')):
        if mode == 'web':
            write(base / 'exam-map.html', exam_page(mode))
            for dom, rows in SECTIONS:
                write(base / 'chapters' / f'{dom["id"]}.html', chapter_page(dom, rows, mode))
        else:
            write(base / 'exam-map.html', exam_page(mode))
            for dom, rows in SECTIONS:
                write(base / f'chapter-{dom["id"]}.html', chapter_page(dom, rows, mode))


if __name__ == '__main__':
    main()
