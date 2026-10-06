#!/usr/bin/env python3
"""Two-pass print-spec PDF build for CCAR-P v2.

Pass 1: render HTML to PDF with headless Chromium (letter, 0.5in margins).
Resolve named-destination page numbers via pypdf /Dests.
Pass 2: inject "page N" into TOC entries, re-render.
Then: stamp running headers + page numbers (pypdf, keep /Dests via
clone_document_from_reader), strip Producer/Creator metadata, verify.
"""
import os, re, sys
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

ROOT = os.path.expanduser("~/workspace/your_files/ccar-p-cert")
CHROME = "/opt/meta-chromium/chrome"
TRACK_TITLE = "CCAR-P Crash Course v2"

def render(src_html, out_pdf):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME,
                              args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = b.new_page()
        pg.goto("file://" + src_html, wait_until="networkidle")
        pg.pdf(path=out_pdf, format="Letter", print_background=True,
               display_header_footer=False,
               margin={"top": "0.5in", "bottom": "0.5in",
                       "left": "0.5in", "right": "0.5in"})
        b.close()
    print("rendered", out_pdf, os.path.getsize(out_pdf), "bytes")

def dest_pages(pdf_path):
    """Named-destination -> 1-based page number, via /Dests (exact, no text guessing)."""
    reader = PdfReader(pdf_path)
    dests = reader.named_destinations
    pages = {}
    for name, dest in dests.items():
        try:
            pages[name.lstrip("/")] = reader.get_destination_page_number(dest) + 1
        except Exception:
            pass
    return pages

def inject_toc_pages(src_html, pages):
    t = open(src_html, encoding="utf-8").read()
    def repl(m):
        href, label = m.group(1), m.group(2)
        pg = pages.get(href)
        if pg:
            return '<a href="#%s">%s <span class="page-marker">%d</span></a>' % (href, label, pg)
        return m.group(0)
    def nav_repl(nm):
        nav = nm.group(0)
        return re.sub(r'<a href="#([^"]+)">((?:(?!</a>).)*)</a>', repl, nav)
    # only inject inside the TOC nav, never in body cross-references
    return re.sub(r'<nav class="toc" id="toc">.*?</nav>', nav_repl, t, flags=re.S)

def stamp(src_pdf, dst_pdf, header_right_default=""):
    reader = PdfReader(src_pdf)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)  # keep /Dests for TOC links
    from pypdf.generic import (ArrayObject, DecodedStreamObject, DictionaryObject,
                               NameObject, NumberObject)
    try:
        from fontTools.ttLib import TTFont
        have_font = True
    except ImportError:
        have_font = False
    n = len(reader.pages)
    for i, page in enumerate(reader.pages):
        pageno = i + 1
        if pageno == 1:
            continue  # cover clean
        text = ("q\nBT /F1 8 Tf 36 756 Td (%s) Tj ET\n"
                "BT /F1 9 Tf 300 36 Td (%d) Tj ET\nQ\n"
                % (TRACK_TITLE.replace("(", "\\(").replace(")", "\\)"), pageno))
        stream = DecodedStreamObject()
        stream.set_data(text.encode("latin-1", "replace"))
        page[NameObject("/Contents")] = ArrayObject(
            [page["/Contents"], stream])
        # minimal font resource
        res = page.get("/Resources")
        if "/Font" not in res:
            res[NameObject("/Font")] = DictionaryObject()
        fonts = res["/Font"]
        if "/F1" not in fonts:
            f = DictionaryObject()
            f.update({NameObject("/Type"): NameObject("/Font"),
                      NameObject("/Subtype"): NameObject("/Type1"),
                      NameObject("/BaseFont"): NameObject("/Helvetica")})
            fonts[NameObject("/F1")] = f
    # strip metadata
    writer._info.get_object().clear()
    with open(dst_pdf, "wb") as f:
        writer.write(f)
    print("stamped", dst_pdf, os.path.getsize(dst_pdf), "bytes")

def expected_secs(src_html):
    t = open(src_html, encoding="utf-8").read()
    return re.findall(r'<section class="domain" id="(sec-[^"]+)"', t)

def render_with_dests(src_html, tmp_pdf, tries=3):
    """Chromium sometimes prints before full layout: retry until all section
    destinations resolve (or the count stops growing)."""
    expected = expected_secs(src_html)
    best = {}
    for _ in range(tries):
        render(src_html, tmp_pdf)
        pages = dest_pages(tmp_pdf)
        if len(pages) > len(best):
            best = pages
        if all(s in pages for s in expected):
            break
    missing = [s for s in expected if s not in best]
    if missing:
        print("WARNING: unresolved sections:", missing)
    return best

def build(name):
    src = os.path.join(ROOT, name + ".html")
    tmp1 = os.path.join("/tmp", name + "-pass1.pdf")
    tmp_html = os.path.join("/tmp", name + "-print2.html")
    out = os.path.join(ROOT, name + ".pdf")
    render(src, tmp1)
    pages = render_with_dests(src, tmp1)
    print("dests resolved:", len(pages))
    t2 = inject_toc_pages(src, pages)
    # /tmp location breaks relative img-v2/ paths: pin them with a base tag
    t2 = t2.replace("<head>",
                    '<head><base href="file://%s/">' % ROOT, 1)
    open(tmp_html, "w", encoding="utf-8").write(t2)
    tmp2 = os.path.join("/tmp", name + "-pass2.pdf")
    render(tmp_html, tmp2)
    stamp(tmp2, out)
    # verify
    r = PdfReader(out)
    print(name, "pages:", len(r.pages))
    assert r.metadata.get("/Producer") in (None, ""), "metadata not stripped"
    return out

if __name__ == "__main__":
    for name in sys.argv[1:] or ["crash-course", "question-bank"]:
        build(name)
