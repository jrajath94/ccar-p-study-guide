"""Build outputs A, B, C (patterns, cheatsheet, mind map), D, F. The crash course guide is build_crash.py.
Usage: python3 build_all.py OUTDIR"""
import sys, json, subprocess
from render import *

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
units = load_units()
COURSE = 'Claude Certified Architect, Professional'


def write(name, text):
    open(f'{OUT}/{name}', 'w').write(text)
    return f'{OUT}/{name}'


# ---------------- A. Curriculum: print PDF, two-up PDF, DOCX ----------------
def build_curriculum():
    src = Sources()
    mer = render_mermaid(mermaid_items(units), 'neutral')
    parts = [f'<h1>{COURSE}. Curriculum</h1>', legend_html(),
             '<p>Read the units in order. Each unit has the same ten parts. Colored text marks a key fact, '
             'a decision rule, an exam tip, or a trap.</p>',
             '<h2 class="nobreak">Topic index</h2>', topic_index_html(units)]
    for dom, u in units:
        parts.append(render_unit_full(dom, u, src, mer))
    parts.append('<h2>Sources</h2>' + src.html())
    p = write('.curriculum.html', page(f'{COURSE}. Curriculum', PRINT_CSS, ''.join(parts)))
    html_to_pdf(p, f'{OUT}/curriculum.pdf')
    two_up(f'{OUT}/curriculum.pdf', f'{OUT}/curriculum-2up.pdf')
    os.remove(p)
    build_docx(src, mer)


def build_docx(src, mer):
    from docx import Document
    from docx.shared import Pt, RGBColor, Mm
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    imgdir = f'{BUILD}/cache/png'
    os.makedirs(imgdir, exist_ok=True)
    jobs, img = [], {}
    for dom, u in units:
        for ci, c in enumerate(u.get('components', [])):
            k = f'{u["id"]}-c{ci}'
            svg = arch_svg(c.get('architecture', {}), c.get('name'))
            img[k] = (f'{imgdir}/{k}.png', list(getattr(arch_svg, 'legend', [])))
            jobs.append({'svg': svg, 'out': img[k][0]})
        r = mer.get(u['id'] + ':flow', {})
        if 'svg' in r:
            img[u['id'] + ':flow'] = (f'{imgdir}/{u["id"]}-flow.png', [])
            jobs.append({'svg': r['svg'], 'out': img[u['id'] + ':flow'][0]})
    json.dump(jobs, open(f'{imgdir}/jobs.json', 'w'))
    subprocess.run(['node', f'{BUILD}/svg2png.js', f'{imgdir}/jobs.json'], check=True, cwd=BUILD)

    col = {k: RGBColor.from_string(v[1][1:]) for k, v in ROLES.items()}
    gray = RGBColor(0x2b, 0x2b, 0x2b)
    d = Document()
    for s in d.sections:
        s.left_margin = s.right_margin = Mm(14)
        s.top_margin = s.bottom_margin = Mm(12)
    st = d.styles['Normal']
    st.font.name = 'Inter'
    st.font.size = Pt(10)
    st.font.color.rgb = gray
    st.paragraph_format.line_spacing = 1.55
    for name in ['Heading 1', 'Heading 2', 'Heading 3', 'Heading 4', 'Title']:
        d.styles[name].font.name = 'Inter'
        d.styles[name].font.color.rgb = gray

    def para(text, role=None, bold=False, style=None):
        p = d.add_paragraph(style=style)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(str(text or ''))
        r.bold = bold
        if role:
            r.font.color.rgb = col[role]
        return p

    def bullets(items, role=None, numbered=False):
        for it in items or ['Not in source.']:
            para(it, role, style='List Number' if numbered else 'List Bullet')

    d.add_heading(f'{COURSE}. Curriculum', 0)
    p = d.add_paragraph()
    for k, v in ROLES.items():
        r = p.add_run(v[0] + '    ')
        r.font.color.rgb = col[k]
    d.add_heading('Topic index', 1)
    for dom, u in units:
        para(f'{u["id"]} {u["title"]}', style='List Bullet')
    for dom, u in units:
        d.add_page_break()
        d.add_heading(f'{u["id"]} {u["title"]}', 1)
        para(f'Domain {dom["id"]}, {dom["title"]}. Task statement: {u.get("task_statement")}')
        for ci, c in enumerate(u.get('components', [])):
            d.add_heading(c.get('name'), 2)
            d.add_heading('1. Introduction and first principle', 3)
            para(c.get('first_principle'), bold=True)
            for f in c.get('key_facts', []):
                n = src.num(f.get('url')) if f.get('url') else None
                para(f'{f.get("text")}' + (f' [{n}]' if n else ''), 'fact', style='List Bullet')
            d.add_heading('2. Architecture', 3)
            k = f'{u["id"]}-c{ci}'
            d.add_picture(img[k][0], width=Mm(150))
            leg = ' '.join(f'{i+1}. {t}.' for i, t in enumerate(img[k][1]))
            para(f'Schematic drawn from docs. Arrows: {leg} {ARCH_LEGEND}')
            d.add_heading('3. How it works', 3)
            bullets(c.get('steps'), numbered=True)
            d.add_heading('4. Pros and cons', 3)
            para('Pros', bold=True); bullets(c.get('pros'))
            para('Cons', bold=True); bullets(c.get('cons'))
            d.add_heading('5. Use when, do not use when', 3)
            para('Use when', bold=True); bullets(c.get('use_when'))
            para('Do not use when', bold=True); bullets(c.get('do_not_use_when'))
            d.add_heading('6. Constraint families', 3)
            for x in c.get('constraints', []):
                para(x.get('family', '').capitalize(), bold=True)
                comb = x.get('combination') or ''
                para(x.get('choice', '') + (f' Combination when one choice is not enough. {comb}' if comb.strip() else ''), 'rule')
            d.add_heading('7. Native cloud services', 3)
            for s in c.get('native_services', []):
                para(s.get('service'), bold=True)
                n = src.num(s['url']) if s.get('url') else None
                para(s.get('text', '') + (f' [{n}]' if n else ''))
            d.add_heading('8. Exam domain and task statement', 3)
            para(c.get('exam_tie'), 'tip')
            if c.get('exam_tip'):
                para(c['exam_tip'], 'tip')
            if c.get('decision_rule'):
                para(c['decision_rule'], 'rule')
            d.add_heading('9. Trap', 3)
            para(c.get('trap'), 'trap')
            d.add_heading('10. Not in source', 3)
            bullets(c.get('not_in_source') or ['None recorded for this component.'])
        if u['id'] + ':flow' in img:
            d.add_heading('Decision flow', 2)
            d.add_picture(img[u['id'] + ':flow'][0], width=Mm(140))
        if u.get('not_in_source'):
            d.add_heading('Unit items not in source', 3)
            bullets(u['not_in_source'])
    d.add_page_break()
    d.add_heading('Sources', 1)
    for i, url in enumerate(src.urls):
        para(f'{i+1}. {src.title(url)}. {url}')
    cp = d.core_properties
    cp.author = 'Author'; cp.last_modified_by = 'Author'; cp.title = ''; cp.subject = ''
    cp.keywords = ''; cp.comments = ''; cp.category = ''; cp.identifier = ''
    d.save(f'{OUT}/curriculum.docx')
    _clean_docx_app(f'{OUT}/curriculum.docx')


def _clean_docx_app(path):
    """Blank the Company and Application fields in docProps/app.xml."""
    import zipfile, shutil
    tmp = path + '.tmp'
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == 'docProps/app.xml':
                s = data.decode()
                s = re.sub(r'<Application>.*?</Application>', '<Application></Application>', s)
                s = re.sub(r'<Company>.*?</Company>', '<Company></Company>', s)
                data = s.encode()
            zout.writestr(item, data)
    shutil.move(tmp, path)


# ---------------- B. Web treatise ----------------
TREATISE_CSS = CSS_BASE + """
:root{--bg:#ffffff;--fg:#262626;--muted:#5c5c5c;--fact:#1f4e9e;--rule:#1d6b36;--tip:#6a3d9a;--trap:#a4161a;--line:#d4d4d4}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0b0b0b;--fg:#ededed;--muted:#b0b0b0;--fact:#7cc4ff;--rule:#6ee09a;--tip:#d0a8ff;--trap:#ff8a80;--line:#3a3a3a}}
:root[data-theme="dark"]{--bg:#0b0b0b;--fg:#ededed;--muted:#b0b0b0;--fact:#7cc4ff;--rule:#6ee09a;--tip:#d0a8ff;--trap:#ff8a80;--line:#3a3a3a}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
body{font-size:17px}
main{max-width:760px;margin:0 auto;padding:16px 16px 96px}
header.top{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);z-index:2}
header.top .in{max-width:760px;margin:0 auto;padding:8px 16px;display:flex;gap:12px;align-items:center;font-size:14px}
#bar{flex:1;height:4px;border:1px solid var(--line)}
#bar i{display:block;height:100%;width:0;background:var(--fg);transition:width .3s}
section.unit{border-top:1px solid var(--line);padding-top:12px;margin-top:28px}
button.done{font:inherit;font-size:14px;padding:6px 12px;border:1px solid var(--fg);background:var(--bg);color:var(--fg);border-radius:4px;cursor:pointer}
button.done[aria-pressed="true"]{background:var(--fg);color:var(--bg)}
details summary{cursor:pointer;color:var(--muted)}
"""

TREATISE_JS = """
<script>
(function(){
  var KEY='ccap-progress-v1', state={};
  try{state=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){state={}}
  function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}
  var btns=[].slice.call(document.querySelectorAll('button.done'));
  function paint(){
    var n=0;
    btns.forEach(function(b){var on=!!state[b.dataset.unit];b.setAttribute('aria-pressed',on);b.textContent=on?'Done':'Mark as done';if(on)n++;});
    document.querySelector('#bar i').style.width=(100*n/btns.length)+'%';
    document.getElementById('count').textContent=n+' of '+btns.length+' units done';
  }
  btns.forEach(function(b){b.addEventListener('click',function(){state[b.dataset.unit]=!state[b.dataset.unit];save();paint();});});
  paint();
})();
</script>
"""


def build_treatise():
    src = Sources()
    parts = [f'<header class="top"><div class="in"><span id="count"></span><span id="bar"><i></i></span></div></header>',
             f'<main><h1>{COURSE}. Treatise</h1>', legend_html(),
             '<p>Scroll through the units in order. Mark each unit as done when you can state its first principle '
             'and its trap without notes. Your progress stays in this browser only.</p>',
             '<h2>Topic index</h2>', topic_index_html(units)]
    cur = None
    for dom, u in units:
        if dom['id'] != cur:
            cur = dom['id']
            parts.append(f'<h2 id="dom-{dom["id"]}">{esc(dom["id"])} {esc(dom["title"])}</h2>')
        parts.append(f'<section class="unit" id="{anchor(u["id"])}"><h3>{esc(u["id"])} {esc(u["title"])}</h3>')
        for ci, c in enumerate(u.get('components', [])):
            parts.append(f'<h4>{esc(c.get("name"))}</h4>')
            parts.append(f'<p class="lbl">{esc(c.get("first_principle"))}</p>')
            svg = arch_svg(c.get('architecture', {}), c.get('name'))
            leg = ' '.join(f'{k+1}. {esc(t)}.' for k, t in enumerate(getattr(arch_svg, 'legend', [])))
            parts.append(f'<div class="figure">{svg}<div class="cap">Schematic drawn from docs. Arrows: {leg}</div></div>')
            bl = (c.get('steps') or [])[:4]
            parts.append('<ul>' + ''.join(f'<li>{esc(s)}</li>' for s in bl)
                         + ''.join(f'<li class="c-fact">{esc(f["text"])}{src.ref(f.get("url"))}</li>'
                                   for f in (c.get('key_facts') or [])[:3])
                         + (f'<li class="c-rule">{esc(c["decision_rule"])}</li>' if c.get('decision_rule') else '')
                         + '</ul>')
            parts.append(f'<p class="c-tip">{esc(c.get("exam_tie"))}</p>')
            parts.append(f'<p class="c-trap">{esc(c.get("trap"))}</p>')
        parts.append(f'<p><button class="done" type="button" data-unit="{esc(u["id"])}" aria-pressed="false">Mark as done</button></p></section>')
    parts.append('<h2>Sources</h2>' + src.html() + '</main>' + TREATISE_JS)
    write('treatise.html', page(f'{COURSE}. Treatise', TREATISE_CSS, ''.join(parts)))


# ---------------- C. Question patterns, cheatsheet, mind map ----------------
def build_patterns():
    parts = [f'<main><h1>{COURSE}. Question patterns</h1>', legend_html(),
             '<p>Each entry maps a generic wording pattern to the answer type, the decision rule, and the traps. '
             'No entry copies an exam item.</p>']
    cur = None
    for dom, u in units:
        if dom['id'] != cur:
            cur = dom['id']
            parts.append(f'<h2 class="nobreak">{esc(dom["id"])} {esc(dom["title"])}</h2>')
        for p in u.get('patterns', []):
            parts.append(f'<h4>"{esc(p.get("wording"))}" <span class="tag">{esc(u["id"])}</span></h4>')
            parts.append(f'<p>Answer type. {esc(p.get("answer_type"))}</p>')
            parts.append(f'<p class="c-rule">{esc(p.get("rule"))}</p>')
            parts.append('<ul>' + ''.join(f'<li class="c-trap">{esc(t)}</li>' for t in p.get('traps', [])) + '</ul>')
    parts.append('</main>')
    css = DARK_CSS + 'h2{break-before:auto} h4{break-after:avoid} h4+p{break-before:avoid}'
    p = write('question-patterns.html', page(f'{COURSE}. Question patterns', css, ''.join(parts)))
    html_to_pdf(p, f'{OUT}/question-patterns.pdf')


def build_cheatsheet():
    items = {u['id']: u['cheatsheet'] for _, u in units if u.get('cheatsheet')}
    mer = render_mermaid(items, 'dark')
    parts = [f'<main><h1>{COURSE}. Mega cheatsheet</h1>']
    for dom, u in units:
        r = mer.get(u['id'], {})
        if 'svg' in r:
            parts.append(f'<div class="cs"><h4>{esc(u["id"])} {esc(u["title"])}</h4><div class="figure mermaid-box">{r["svg"]}</div></div>')
    parts.append('</main>')
    css = DARK_CSS + '.cs{break-inside:avoid;margin-bottom:6mm}.cs .mermaid-box svg{max-height:95mm}'
    p = write('mega-cheatsheet.html', page(f'{COURSE}. Mega cheatsheet', css, ''.join(parts)))
    html_to_pdf(p, f'{OUT}/mega-cheatsheet.pdf')


def build_mindmap():
    rows = []
    for dom, u in units:
        rows.append((dom, u))
    RH, W = 26, 1000
    H = len(rows) * RH + 40
    doms = []
    for dom, _ in rows:
        if dom['id'] not in [d['id'] for d in doms]:
            doms.append(dom)
    svg = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" font-size="14" role="img" aria-label="Mind map of the course">']
    root_y = H / 2
    svg.append(f'<a href="crash-course.html"><text x="10" y="{root_y+5:.0f}" fill="currentColor" font-weight="700" font-size="16">Course</text></a>')
    y = 30
    for dom in doms:
        us = [u for d, u in rows if d['id'] == dom['id']]
        dy = y + (len(us) - 1) * RH / 2
        svg.append(f'<path d="M80,{root_y:.0f} C160,{root_y:.0f} 160,{dy:.0f} 240,{dy:.0f}" fill="none" stroke="currentColor" stroke-width="1.2"/>')
        svg.append(f'<a href="crash-course.html#{anchor(us[0]["id"])}"><text x="248" y="{dy+5:.0f}" fill="currentColor" font-weight="650">{esc(dom["id"])} {esc(dom["title"][:34])}</text></a>')
        for k, u in enumerate(us):
            uy = y + k * RH
            svg.append(f'<path d="M560,{dy:.0f} C600,{dy:.0f} 600,{uy:.0f} 640,{uy:.0f}" fill="none" stroke="currentColor" stroke-width="1"/>')
            svg.append(f'<a href="crash-course.html#{anchor(u["id"])}"><text x="648" y="{uy+5:.0f}" fill="currentColor">{esc(u["id"])} {esc(u["title"][:38])}</text></a>')
        y += len(us) * RH
    svg.append('</svg>')
    css = DARK_CSS + 'main{max-width:1100px} svg a text{text-decoration:underline} @media (max-width:700px){.wrap{overflow-x:auto}.wrap svg{min-width:900px}}'
    write('mind-map.html', page(f'{COURSE}. Mind map', css,
          f'<main><h1>{COURSE}. Mind map</h1><p>Select a heading to open that place in the crash course guide.</p>'
          f'<div class="wrap">{"".join(svg)}</div></main>'))


# ---------------- D. Video prompt ----------------
def build_video():
    scenes = [('Opening', 'Black screen. White title text with the course name. Four colored words appear: Key fact in blue, '
               'Decision rule in green, Exam tip in purple, Trap in red.',
               'This course teaches one decision at a time. Watch for four colors. Blue is a key fact. Green is a decision rule. '
               'Purple is an exam tip. Red is a trap.')]
    for dom, u in units:
        c = (u.get('components') or [{}])[0]
        names = ', '.join(x.get('architecture', {}).get('nodes', [{}])[0].get('label', '') for x in u['components'][:1])
        nodes = ', '.join(n.get('label', '') for n in c.get('architecture', {}).get('nodes', []))
        visual = (f'Black background. Draw a line diagram with white outlined boxes for: {nodes}. '
                  f'Arrows appear one at a time in order. Then show the decision rule in green text and the trap in red text.')
        narr = f'{u["title"]}. {c.get("first_principle", "")} {c.get("decision_rule", "")} The trap: {c.get("trap", "")}'
        scenes.append((f'{u["id"]} {u["title"]}', visual, narr))
    scenes = scenes[:43]
    lines = [f'# {COURSE}. Video prompt for Muse', '',
             'Format: numbered scenes. Each scene has a visual and a narration. Use a pitch-black background, one sans-serif typeface, '
             'white outlined shapes, and colored text only for the four roles. Use no logo, no watermark, no stock footage, '
             'no human presenter, and no on-screen credit.', '',
             f'Scene count: {len(scenes)}. Target length per scene: 20 to 30 seconds.', '']
    for i, (t, v, n) in enumerate(scenes, 1):
        lines += [f'## Scene {i}. {t}', '', f'Visual. {v}', '', f'Narration. {n}', '']
    write('video-prompt.md', '\n'.join(lines))
    summ = [f'# Video summary', '', f'Scenes: {len(scenes)}. Estimated length: {len(scenes)*20//60} to {len(scenes)*30//60} minutes.', '']
    summ += [f'{i}. {t}' for i, (t, _, _) in enumerate(scenes, 1)]
    write('video-summary.md', '\n'.join(summ) + '\n')
    gaps = ['# Video gaps', '',
            'The video covers the curriculum units only. It contains no practice question text.', '',
            'The items below are not in the official docs. The video must not state them as fact.', '']
    for dom, u in units:
        for c in u.get('components', []):
            for x in c.get('not_in_source', []):
                gaps.append(f'- {u["id"]} {c.get("name")}. {x}')
    write('video-gaps.md', '\n'.join(gaps) + '\n')


# ---------------- F. Console steps ----------------
def build_console():
    src = Sources()
    parts = [f'<main><h1>{COURSE}. Console steps</h1>',
             '<p>Each step names its official docs page. The docs pages show the official screenshots. '
             'This file does not copy them, because the reuse terms for docs images are not stated. '
             'A unit without official console steps shows "Not in source."</p>']
    for dom, u in units:
        parts.append(f'<h3 id="{anchor(u["id"])}">{esc(u["id"])} {esc(u["title"])}</h3>')
        steps = u.get('console_steps') or []
        if not steps:
            parts.append('<p>Not in source.</p>')
            continue
        parts.append('<ol>' + ''.join(f'<li>{esc(s.get("step"))}{src.ref(s.get("url"))}</li>' for s in steps) + '</ol>')
    parts.append('<h2>Sources</h2>' + src.html() + '</main>')
    css = PRINT_CSS + 'h2{break-before:auto} main{max-width:820px;margin:0 auto;padding:0 16px}'
    p = write('console-steps.html', page(f'{COURSE}. Console steps', css, ''.join(parts)))
    html_to_pdf(p, f'{OUT}/console-steps.pdf')


if __name__ == '__main__':
    which = sys.argv[2:] or ['curriculum', 'treatise', 'patterns', 'cheatsheet', 'mindmap', 'video', 'console']
    for w in which:
        globals()['build_' + w]()
        print('built', w)
