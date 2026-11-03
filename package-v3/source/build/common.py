"""Shared helpers: unit loading, architecture SVG, Mermaid rendering, sources, PDF metadata."""
import hashlib, html, json, os, re, subprocess, glob

WORK = os.environ.get('CCAR_WORK', '/home/claude/work')
BUILD = f'{WORK}/build'
CACHE = f'{BUILD}/cache'
os.makedirs(CACHE, exist_ok=True)

ROLES = {
    'fact': ('Key fact', '#1f4e9e', '#7cc4ff'),
    'rule': ('Decision rule', '#1d6b36', '#6ee09a'),
    'tip': ('Exam tip', '#6a3d9a', '#d0a8ff'),
    'trap': ('Trap', '#a4161a', '#ff8a80'),
}

FAMILY_ORDER = ['latency', 'cost', 'quota', 'data location', 'isolation', 'governance', 'scale', 'skill', 'operations']


def esc(s):
    return html.escape(str(s or ''), quote=True)


def load_topics():
    return json.load(open(f'{WORK}/topics.json'))


def load_units(only=None):
    """Return list of (domain dict, unit dict) in topic order. Missing units are skipped."""
    topics = load_topics()
    out = []
    for dom in topics['domains']:
        for uid, title, _ in dom['units']:
            if only and uid not in only and dom['id'] not in only:
                continue
            fn = os.path.join(os.environ.get('UNITS_DIR', f'{WORK}/units'), f'{uid}.json')
            if os.path.exists(fn):
                u = json.load(open(fn))
                u['id'] = uid
                u.setdefault('title', title)
                out.append((dom, u))
    return out


def anchor(uid):
    return 'u-' + uid.replace('.', '-')


# ---------- sources registry ----------
class Sources:
    def __init__(self):
        self.urls = []

    def ref(self, url):
        if not url:
            return ''
        url = url.split('#')[0].rstrip('/')
        if url not in self.urls:
            self.urls.append(url)
        n = self.urls.index(url) + 1
        return f'<sup class="ref"><a href="#src-{n}">{n}</a></sup>'

    def num(self, url):
        url = url.split('#')[0].rstrip('/')
        if url not in self.urls:
            self.urls.append(url)
        return self.urls.index(url) + 1

    def title(self, url):
        f = f'{WORK}/docs/pages/' + url.replace('https://', '').replace('/', '__') + '.md'
        if os.path.exists(f):
            for line in open(f):
                if line.startswith('title:'):
                    return line[6:].strip()
                if line.startswith('# '):
                    return line[2:].strip()
        return url

    def html(self):
        items = ''.join(f'<li id="src-{i+1}">{esc(self.title(u))}. <a href="{esc(u)}">{esc(u)}</a></li>'
                        for i, u in enumerate(self.urls))
        return f'<ol class="sources">{items}</ol>'


# ---------- architecture SVG ----------
def _wrap(text, width=19):
    words, lines, cur = str(text).split(), [], ''
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        lines.append(cur)
    return lines or ['']


def arch_svg(arch, title=''):
    """Grid layout. Layers run left to right in bands of up to 3 columns. Bands stack top to bottom.
    Strokes use currentColor so the page theme decides the color."""
    nodes = arch.get('nodes', [])
    edges = [e for e in arch.get('edges', []) if e.get('from') != e.get('to')]
    ids = [n['id'] for n in nodes]
    if not nodes:
        return ''
    label = {n['id']: n.get('label', n['id']) for n in nodes}
    layer = {i: 0 for i in ids}
    for _ in range(len(ids)):
        changed = False
        for e in edges:
            a, b = e.get('from'), e.get('to')
            if a in layer and b in layer and ids.index(b) > ids.index(a) and layer[b] < layer[a] + 1:
                layer[b] = layer[a] + 1
                changed = True
        if not changed:
            break
    cols = {}
    for i in ids:
        cols.setdefault(layer[i], []).append(i)
    W, BW, LH, RG = 680, 150, 15, 30
    layers = sorted(cols)
    bands = [layers[k:k + 3] for k in range(0, len(layers), 3)]
    pos, size, y = {}, {}, 14
    for band in bands:
        colw = W / len(band)
        col_h = {}
        for L in band:
            hs = [len(_wrap(label[i])) * LH + 20 for i in cols[L]]
            col_h[L] = sum(hs) + RG * (len(hs) - 1)
        band_h = max(col_h.values())
        for ci, L in enumerate(band):
            cy = y + (band_h - col_h[L]) / 2
            for i in cols[L]:
                h = len(_wrap(label[i])) * LH + 20
                pos[i] = (ci * colw + (colw - BW) / 2, cy)
                size[i] = (BW, h)
                cy += h + RG
        y += band_h + 58
    H = y - 58 + 14

    def clip(cx, cy, w, h, dx, dy):
        if dx == 0 and dy == 0:
            return cx, cy
        tx = (w / 2 + 3) / abs(dx) if dx else 1e9
        ty = (h / 2 + 3) / abs(dy) if dy else 1e9
        t = min(tx, ty)
        return cx + dx * t, cy + dy * t

    def border(a, b):
        (ax, ay), (aw, ah) = pos[a], size[a]
        (bx, by), (bw, bh) = pos[b], size[b]
        cx1, cy1, cx2, cy2 = ax + aw / 2, ay + ah / 2, bx + bw / 2, by + bh / 2
        dx, dy = cx2 - cx1, cy2 - cy1
        return clip(cx1, cy1, aw, ah, dx, dy) + clip(cx2, cy2, bw, bh, -dx, -dy)

    dash = {'cloud': '6 4', 'data': '2 3', 'control': '10 3 2 3'}
    parts = [f'<svg class="arch" viewBox="0 0 {W} {H:.0f}" width="100%" role="img" aria-label="{esc(title)}" '
             f'xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" font-size="12">',
             '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
             'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs>']
    labels, legend = [], []
    for e in edges:
        a, b = e.get('from'), e.get('to')
        if a not in pos or b not in pos:
            continue
        x1, y1, x2, y2 = border(a, b)
        parts.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="currentColor" '
                     f'stroke-width="1.2" marker-end="url(#ah)"/>')
        if e.get('label'):
            k = len(legend) + 1
            legend.append(e['label'])
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
            labels.append(f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="8" fill="var(--bg)" stroke="currentColor" stroke-width="1"/>'
                          f'<text x="{lx:.0f}" y="{ly + 3.5:.0f}" text-anchor="middle" font-size="10" '
                          f'fill="currentColor">{k}</text>')
    for n in nodes:
        x, y0 = pos[n['id']]
        bw, h = size[n['id']]
        g = n.get('group', 'client')
        sw = '2.2' if g == 'claude' else '1.2'
        da = f' stroke-dasharray="{dash[g]}"' if g in dash else ''
        parts.append(f'<rect x="{x:.0f}" y="{y0:.0f}" width="{bw}" height="{h}" rx="4" fill="none" '
                     f'stroke="currentColor" stroke-width="{sw}"{da}/>')
        lines = _wrap(label[n['id']])
        top = y0 + h / 2 - (len(lines) - 1) * LH / 2 + 4
        for k, t in enumerate(lines):
            parts.append(f'<text x="{x + bw/2:.0f}" y="{top + k*LH:.0f}" text-anchor="middle" '
                         f'fill="currentColor">{esc(t)}</text>')
    parts += labels
    parts.append('</svg>')
    arch_svg.legend = legend
    return ''.join(parts)


ARCH_LEGEND = ('Box line style: heavy line is a Claude service, thin line is your system, '
               'long dash is a cloud provider, dots are a data store, dash-dot is a control.')


# ---------- Mermaid ----------
def clean_mermaid(code):
    code = (code or '').replace('\\n', '\n').strip()
    code = code.replace('—', ',').replace('–', ',').replace(';', ',')
    # Diamonds grow with their text. Hexagons keep decision nodes compact.
    code = re.sub(r'(\b[A-Za-z0-9_]+)\{(?!\{)([^{}]+)\}(?!\})', r'\1{{\2}}', code)
    return code


def render_mermaid(items, theme):
    """items: {key: code} -> {key: {'svg'|'error'}}. Cached per theme and code."""
    out, todo = {}, {}
    for k, code in items.items():
        code = clean_mermaid(code)
        h = hashlib.sha1((theme + code).encode()).hexdigest()[:16]
        f = f'{CACHE}/{h}.json'
        if os.path.exists(f):
            out[k] = json.load(open(f))
        else:
            todo[h] = code
            out[k] = h
    if todo:
        inp, outp = f'{CACHE}/in.json', f'{CACHE}/out.json'
        json.dump({'theme': theme, 'items': todo}, open(inp, 'w'))
        subprocess.run(['node', f'{BUILD}/mermaid_render.js', inp, outp], check=True, cwd=BUILD)
        res = json.load(open(outp))
        for h, v in res.items():
            json.dump(v, open(f'{CACHE}/{h}.json', 'w'))
        for k in out:
            if isinstance(out[k], str):
                out[k] = res[out[k]]
    return out


# ---------- PDF ----------
def html_to_pdf(html_path, pdf_path, fmt='A4', landscape=False, wait_ms=300):
    subprocess.run(['node', f'{BUILD}/pdf.js', html_path, pdf_path, fmt, '1' if landscape else '0', str(wait_ms)],
                   check=True, cwd=BUILD)
    clean_pdf_meta(pdf_path)


def clean_pdf_meta(pdf_path):
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(pdf_path)
    w = PdfWriter(clone_from=r)
    w.metadata = None
    w.add_metadata({'/Author': 'Author', '/Title': '', '/Creator': '', '/Producer': '', '/Subject': '', '/Keywords': ''})
    with open(pdf_path, 'wb') as f:
        w.write(f)
    # pypdf may stamp its own producer. Replace it in place.
    data = open(pdf_path, 'rb').read()
    data = re.sub(rb'/Producer \((?:pypdf|PyPDF\d?)[^)]*\)', lambda m: b'/Producer ()' + b' ' * (len(m.group(0)) - 12), data)
    open(pdf_path, 'wb').write(data)


def two_up(src, dst):
    from pypdf import PdfReader, PdfWriter, Transformation, PageObject
    r = PdfReader(src)
    w = PdfWriter()
    pw = float(r.pages[0].mediabox.width)
    ph = float(r.pages[0].mediabox.height)
    sheet_w, sheet_h = ph, pw  # landscape sheet of the same paper size
    s = min((sheet_w / 2) / pw, sheet_h / ph)
    off_y = (sheet_h - ph * s) / 2
    pages = list(r.pages)
    for i in range(0, len(pages), 2):
        sheet = PageObject.create_blank_page(width=sheet_w, height=sheet_h)
        for k, p in enumerate(pages[i:i + 2]):
            off_x = k * sheet_w / 2 + (sheet_w / 2 - pw * s) / 2
            sheet.merge_transformed_page(p, Transformation().scale(s).translate(off_x, off_y))
        w.add_page(sheet)
    for pg in w.pages:
        pg.compress_content_streams(level=9)
    with open(dst, 'wb') as f:
        w.write(f)
    clean_pdf_meta(dst)


def plain(text):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', text or '')).strip()
