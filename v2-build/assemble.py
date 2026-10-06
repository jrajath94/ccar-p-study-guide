#!/usr/bin/env python3
"""Assemble CCAR-P v2 crash-course.html and question-bank.html from fragments.

Reads markdown fragments, converts with python-markdown (tables, fenced code,
md_in_html), demotes fragment H1->H2 / H2->H3 so the assembler-injected domain
H1s own the 18pt page-break level, prefixes all ids per section, converts
:::takeaway fenced divs, injects chapter images, builds a nested clickable TOC.
"""
import os, re, sys
import markdown

ROOT = os.path.expanduser("~/workspace/your_files/ccar-p-cert")
VB = os.path.join(ROOT, "v2-build")
IMG = "img-v2"  # relative image dir in the output root

CSS_PRINT = open(os.path.join(VB, "print.css")).read()

CSS_SCREEN = """
body{font-family:"Anthropic Sans",Inter,"Source Sans 3","IBM Plex Sans",sans-serif;
font-size:15px;line-height:1.55;color:#1B2838;background:#F7F4EE;margin:0;padding:0}
.page{max-width:860px;margin:0 auto;background:#FFFDF8;padding:32px 40px;box-shadow:0 0 0 1px #D9D3C7}
h1{font-size:30px;font-weight:700;border-bottom:2px solid #1B2838;padding-bottom:8px}
h2{font-size:22px;font-weight:700;color:#1B2838;margin-top:28px}
h3{font-size:17px;font-weight:700;color:#1B2838}
table{border-collapse:collapse;width:100%;font-size:13px;margin:12px 0}
th,td{border:1px solid #D9D3C7;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#F7F4EE;font-weight:700}
pre{background:#F7F4EE;border:1px solid #D9D3C7;padding:12px;overflow-x:auto;
font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:12.5px;white-space:pre}
code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:13px}
.key-takeaway{border-left:4px solid #1F7A72;background:#E7F4EF;padding:12px 16px;margin:16px 0}
figure.fig{margin:20px auto;text-align:center;max-width:100%}
figure.fig svg,figure.fig img{max-width:100%;height:auto}
figcaption{font-size:12px;color:#5C6B7A;margin-top:6px}
nav.toc{background:#F7F4EE;border:1px solid #D9D3C7;padding:16px 24px;margin:24px 0}
nav.toc ul{list-style:none;padding-left:0}
nav.toc ul ul{padding-left:20px}
nav.toc a{color:#1E4D8C;text-decoration:none}
nav.toc a:hover{text-decoration:underline}
.cover{text-align:center;padding:60px 20px}
.cover h1{font-size:38px;border:none}
.cover img{max-width:640px;width:100%;height:auto;margin:24px auto;display:block}
.meta{color:#5C6B7A;font-size:13px}
"""

def md_to_html(text, slug):
    # :::takeaway fenced divs -> key-takeaway divs (markdown inside)
    def takeaway_repl(m):
        inner = m.group(1).strip("\n")
        return '<div class="key-takeaway" markdown="1">\n\n' + inner + '\n\n</div>'
    text = re.sub(r"^:::takeaway\s*\n(.*?)\n:::\s*$", takeaway_repl, text,
                  flags=re.M | re.S)
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "md_in_html"])
    # demote fragment headings: h1->h2, h2->h3, h3->h4, h4->h5
    for old, new in [("h4", "h5"), ("h3", "h4"), ("h2", "h3"), ("h1", "h2")]:
        html = re.sub(r"<%s(\s|>)" % old, r"<%s\1" % new, html)
        html = re.sub(r"</%s>" % old, "</%s>" % new, html)
    # prefix ids and in-page anchors with the slug
    html = re.sub(r'id="([A-Za-z0-9][A-Za-z0-9\-_]*)"',
                  lambda m: 'id="%s-%s"' % (slug, m.group(1)), html)
    html = re.sub(r'href="#([A-Za-z0-9][A-Za-z0-9\-_]*)"',
                  lambda m: 'href="#%s-%s"' % (slug, m.group(1)), html)
    # assign ids to h2/h3/h4 for TOC
    n = [0]
    def head_id(m):
        n[0] += 1
        tag, attrs, text = m.group(1), m.group(2), m.group(3)
        if 'id=' not in attrs:
            attrs = ' id="%s-h%d"%s' % (slug, n[0], attrs)
        return "<%s%s>%s</%s>" % (tag, attrs, text, tag)
    html = re.sub(r"<(h[234])((?:\s[^>]*)?)>(.*?)</h[234]>", head_id, html, flags=re.S)
    return html

def section_html(slug, title, files, image=None, intro=None):
    parts = ['<section class="domain" id="sec-%s">' % slug,
             "<h1>%s</h1>" % title]
    if image:
        parts.append(
            '<figure class="fig"><img src="%s/%s.webp" alt="%s chapter plate">'
            "<figcaption>Chapter plate. Source: original.</figcaption></figure>"
            % (IMG, image, title))
    if intro:
        parts.append(intro)
    for f in files:
        path = os.path.join(VB, f)
        html = md_to_html(open(path, encoding="utf-8").read(), slug)
        parts.append('<div class="fragment" data-src="%s">\n%s\n</div>' % (f, html))
    parts.append("</section>")
    return "\n".join(parts)

def build_toc(sections_html):
    items = []
    for slug, title, _ in SECTIONS_META:
        sub_items = ""
        for m in re.finditer(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', sections_html):
            if m.group(1).startswith(slug + "-h"):
                sub_items += '<li><a href="#%s">%s</a></li>' % (
                    m.group(1), re.sub(r"<[^>]+>", "", m.group(2))[:80])
        items.append('<li><a href="#sec-%s"><strong>%s</strong></a><ul>%s</ul></li>'
                     % (slug, title, sub_items))
    return '<nav class="toc" id="toc"><h2>Contents</h2><ul>\n' + "\n".join(items) + "\n</ul></nav>"

# (slug, title, image, [fragment paths])
COURSE = [
    ("exam", "Exam Facts and How to Use This Course", None,
     ["stage1/exam-facts-v2.md"]),
    ("diagnostic", "Prerequisite Diagnostic", None,
     ["stage2/diagnostic.md"]),
    ("f74", "Foundation: Architecture and Business", "f74",
     ["stage2/lesson-7-4A.md"]),
    ("f73", "Foundation: LLM Fundamentals", "f73",
     ["stage2/lesson-7-3A.md"]),
    ("f71", "Foundation: Distributed Systems", "f71",
     ["stage2/lesson-7-1A.md"]),
    ("f72", "Foundation: Security and Identity", "f72",
     ["stage2/lesson-7-2A.md"]),
    ("d1", "Domain 1: Solution Design and Architecture (17%)", "d1",
     ["stage3/lesson-D1-1.md", "stage3/lesson-D1-2.md",
      "stage3/lesson-D1-patterns.md", "stage3/lesson-D1-6.md"]),
    ("d2", "Domain 2: Claude Models, Prompting, and Context Engineering (13%)", "d2",
     ["stage3/lesson-D2-1.md", "stage3/lesson-D2-2.md", "stage3/lesson-D2-3.md",
      "stage3/lesson-D2-4.md", "stage3/lesson-D2-5.md"]),
    ("d3", "Domain 3: Integration (19%)", "d3",
     ["stage4/lesson-D3-%d.md" % i for i in range(1, 9)]),
    ("d4", "Domain 4: Evaluation, Testing, and Optimization (16%)", "d4",
     ["stage5/lesson-D4-%d.md" % i for i in range(1, 7)]),
    ("d5", "Domain 5: Governance, Safety, and Risk Management (14%)", "d5",
     ["stage5/lesson-D5-%d.md" % i for i in range(1, 6)]),
    ("d6", "Domain 6: Stakeholder Communication and Lifecycle Management (14%)", "d6",
     ["stage6/lesson-D6-%d.md" % i for i in range(1, 6)]),
    ("d7", "Domain 7: Developer Productivity and Operational Enablement (7%)", "d7",
     ["stage6/lesson-D7-%d.md" % i for i in range(1, 4)]),
    ("compare", "High-Confusion Comparisons", None,
     ["stage7/comparisons-%02d.md" % i for i in range(1, 6)]),
    ("artifacts", "Implementation Artifacts", None,
     ["stage7/artifacts-01.md", "stage7/artifacts-02.md"]),
    ("labs", "Labs", None, ["stage7/labs.md"]),
    ("capstones", "Capstones", None,
     ["stage7/capstone-A.md", "stage7/capstone-B.md", "stage7/capstone-C.md"]),
    ("review", "Final Review Sheets", None, ["stage9/final-review-sheets.md"]),
    ("readiness", "Readiness Dashboard", None, ["stage9/readiness-dashboard.md"]),
    ("errorledger", "Error Ledger", None, ["stage9/error-ledger.md"]),
    ("currentness", "October 6, 2026 Currentness Appendix", None,
     ["stage9/currentness-appendix.md"]),
    ("sources", "Source Registry and Blueprint Ledger", None,
     ["stage1/source-registry-v2.md", "stage1/blueprint-ledger-v2.md"]),
]

BANK = [
    ("bank-key", "Diagnostic Answer Key", None, ["stage8/diagnostic-key.md"]),
    ("bank-d1", "Question Bank: Domain 1", None, ["stage8/qb-D1.md"]),
    ("bank-d2", "Question Bank: Domain 2", None, ["stage8/qb-D2.md"]),
    ("bank-d3", "Question Bank: Domain 3", None, ["stage8/qb-D3.md"]),
    ("bank-d4", "Question Bank: Domain 4", None, ["stage8/qb-D4.md"]),
    ("bank-d5", "Question Bank: Domain 5", None, ["stage8/qb-D5.md"]),
    ("bank-d6", "Question Bank: Domain 6", None, ["stage8/qb-D6.md"]),
    ("bank-d7", "Question Bank: Domain 7", None, ["stage8/qb-D7.md"]),
    ("bank-mixed", "Question Bank: Mixed Domain", None, ["stage8/qb-mixed.md"]),
    ("bank-drills", "Counterfactual Drills", None, ["stage8/counterfactual-drills.md"]),
    ("bank-mocks", "Full-Length Mock Exams", None, ["stage8/mocks.md"]),
]

SECTIONS_META = []

def assemble(sections, out_name, title, cover_image, cover_sub):
    global SECTIONS_META
    SECTIONS_META = [(s, t, f) for s, t, _, f in sections]
    body = []
    for slug, stitle, image, files in sections:
        if not files:
            continue
        body.append(section_html(slug, stitle, files, image))
    all_html = "\n".join(body)
    toc = build_toc(all_html)
    cover = (
        '<div class="cover"><h1>%s</h1><p>%s</p>'
        '<img src="%s/%s.webp" alt="cover art">'
        '<p class="meta">Baseline: October 6, 2026. Blueprint v1.0 (July 2026). '
        "All practice questions are original. No exam dumps.</p></div>"
        % (title, cover_sub, IMG, cover_image))
    doc = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>%s</title>
<style>%s</style>
<style media="print">%s</style>
</head>
<body><div class="page">
%s
%s
%s
</div></body></html>""" % (title, CSS_SCREEN, CSS_PRINT, cover, toc, all_html)
    out = os.path.join(ROOT, out_name)
    open(out, "w", encoding="utf-8").write(doc)
    print("wrote", out, len(doc), "bytes")

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, IMG), exist_ok=True)
    for short in ["cover", "d1", "d2", "d3", "d4", "d5", "d6", "d7",
                  "f74", "f73", "f71", "f72"]:
        src = os.path.join(VB, "images", short + ".webp")
        dst = os.path.join(ROOT, IMG, short + ".webp")
        open(dst, "wb").write(open(src, "rb").read())
    assemble(COURSE, "crash-course.html",
             "Claude Certified Architect - Professional: Crash Course",
             "cover",
             "The shortest defensible route through all 38 published objectives.")
    assemble(BANK, "question-bank.html",
             "CCAR-P Crash Course: Question Bank",
             "cover",
             "477 original questions, 52 counterfactual drills, 4 full mocks.")
