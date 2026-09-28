#!/usr/bin/env python3
"""Build the CCAR-P D5 study volume as a single self-contained HTML file."""
import base64
import re
from html.parser import HTMLParser

OUT = "/home/hatch/workspace/your_files/ccar-p-cert/05-stakeholder-communication-lifecycle.html"

# ---------- palette (flat, minimal; matches house style) ----------
PAPER = "#F8F7F3"; INK = "#24292F"; MUTED = "#5C6570"; BLUE = "#1F5FBF"
BOARD = "#163D7A"; AMBER = "#A15C07"; CARD = "#FFFFFF"; CODEBG = "#EFF0EA"
RULE = "#E3E0D8"; GREEN = "#2F7D32"; RED = "#C0392B"; TEAL = "#0E7C7B"

CSS = """
:root{--paper:#F8F7F3;--ink:#24292F;--muted:#5C6570;--blue:#1F5FBF;--board:#163D7A;
--amber:#A15C07;--green:#2F7D32;--red:#C0392B;--card:#FFFFFF;--codebg:#EFF0EA;--rule:#E3E0D8;--maxw:74ch}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);
font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif}
a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.87em;
background:var(--codebg);padding:.12em .4em;border-radius:4px;white-space:nowrap}
pre{background:var(--codebg);border:1px solid var(--rule);border-radius:8px;
padding:1em 1.2em;overflow-x:auto;font-size:.85em;line-height:1.55}
pre code{background:none;padding:0}
.layout{display:flex;min-height:100vh}
.rail{position:sticky;top:0;height:100vh;overflow-y:auto;flex:0 0 280px;
border-right:1px solid var(--rule);padding:1.4rem 1.1rem;background:var(--paper)}
.rail h2{font-size:1rem;margin:0 0 .2rem}
.rail .sub{color:var(--muted);font-size:.83rem;margin:0 0 1rem}
.rail nav ul{list-style:none;margin:0;padding:0}
.rail nav>ul>li{margin:.12rem 0}
.rail a.ch{display:block;padding:.42rem .55rem;border-radius:6px;color:var(--ink);font-weight:600;font-size:.9rem}
.rail a.ch:hover{background:var(--codebg);text-decoration:none}
.rail a.ch .n{color:var(--muted);font-weight:400;margin-right:.35em;font-size:.85em}
.rail a.ch.active{background:#E4ECF9;color:var(--board)}
.rail ul.sec{list-style:none;margin:.1rem 0 .4rem 1.1rem;padding:0}
.rail ul.sec a{font-size:.8rem;color:var(--muted);display:block;padding:.12rem 0}
.main{flex:1;min-width:0;padding:2.5rem 2rem 6rem}
.wrap{max-width:var(--maxw);margin:0 auto}
.unit{margin-bottom:4rem}
.unit>h1{font-size:1.95rem;line-height:1.25;letter-spacing:-.01em;margin:0 0 .3rem}
.unit .lede{color:var(--muted);font-size:1.03rem;margin:0 0 1.4rem}
h2{font-size:1.4rem;margin:2.1rem 0 .7rem;letter-spacing:-.01em}
h3{font-size:1.15rem;margin:1.7rem 0 .5rem}
p{margin:.65rem 0}ul,ol{margin:.65rem 0;padding-left:1.5rem}li{margin:.28rem 0}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.9rem;display:block;overflow-x:auto}
th,td{border:1px solid var(--rule);padding:.5rem .65rem;text-align:left;vertical-align:top}
th{background:var(--codebg);font-weight:700}
.fig{background:var(--card);border:1px solid var(--rule);border-radius:10px;
padding:1rem;margin:1.4rem 0;text-align:center}
.fig img{max-width:100%;height:auto;border-radius:6px}
.fig figcaption{font-size:.85rem;color:var(--muted);margin-top:.6rem;text-align:left}
.fig figcaption .src{display:block;margin-top:.3rem;font-size:.8rem}
.howread{background:#FBFAF7;border:1px solid var(--rule);border-radius:0 10px 10px 0;
border-left:4px solid var(--blue);padding:.9rem 1.2rem;margin:0 0 1.6rem}
.howread-title{font-weight:700;margin:0 0 .3rem;font-size:1rem;color:var(--board)}
.howread-sub{font-weight:700;font-size:.88rem;margin:.7rem 0 .2rem;color:var(--ink)}
.howread ol.flow{margin:.4rem 0;padding-left:1.4rem;font-size:.93rem}
.howread ol.flow li{margin:.22rem 0}
.howread table{font-size:.85rem;margin:.5rem 0}
.trap{background:#FFF8EC;border:1px solid #EBD9B4;border-left:4px solid var(--amber);
border-radius:0 10px 10px 0;padding:.9rem 1.2rem;margin:1.4rem 0}
.trap .t-title{font-weight:700;color:var(--amber);margin:0 0 .3rem}
.examq{background:#F2F6FD;border:1px solid #CBDDF5;border-left:4px solid var(--blue);
border-radius:0 10px 10px 0;padding:.9rem 1.2rem;margin:1.4rem 0}
.examq .t-title{font-weight:700;color:var(--board);margin:0 0 .3rem}
.def{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:.9rem 1.2rem;margin:1rem 0}
.def .t-title{font-weight:700;margin:0 0 .2rem}
details{background:var(--card);border:1px solid var(--rule);border-radius:8px;
padding:.7rem 1rem;margin:.8rem 0}
details summary{cursor:pointer;font-weight:600;color:var(--board)}
.note{font-size:.88rem;color:var(--muted)}
.kv{display:grid;grid-template-columns:170px 1fr;gap:.35rem .9rem;margin:.8rem 0;font-size:.93rem}
.kv dt{font-weight:700}.kv dd{margin:0}
@media (max-width:900px){.rail{display:none}.main{padding:1.5rem 1rem 4rem}}
"""

# ---------- svg helpers ----------
def svg_doc(w, h, inner):
    bg = '<rect x="0" y="0" width="%d" height="%d" fill="#FFFFFF"/>' % (w, h)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'font-family="-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif">%s%s</svg>' % (w, h, w, h, bg, inner))

def box(x, y, w, h, fill, stroke, rx=10):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, y, w, h, rx, fill, stroke)

def txt(x, y, s, size=15, fill=INK, anchor="middle", weight=600):
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return ('<text x="%d" y="%d" font-size="%d" fill="%s" text-anchor="%s" font-weight="%d">%s</text>'
            % (x, y, size, fill, anchor, weight, s))

def arrow(x1, y1, x2, y2, color=BOARD, wdt=2.5):
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%.1f" '
            'marker-end="url(#ah)"/>' % (x1, y1, x2, y2, color, wdt))

DEFMARK = ('<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
           'orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#163D7A"/></marker></defs>')

def fig_b64(svg):
    return base64.b64encode(svg.encode("utf-8")).decode("ascii")

def figure(figid, svg, alt, caption, flow_steps, parts):
    rows = "".join(
        "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>" % p for p in parts)
    steps = "".join("<li>%s</li>" % s for s in flow_steps)
    return (
        '<figure class="fig" id="%s"><img src="data:image/svg+xml;base64,%s" alt="%s" loading="lazy">'
        '<figcaption>%s</figcaption></figure>'
        '<div class="howread"><p class="howread-title">How to read this diagram</p>'
        '<p class="howread-sub">Follow the flow</p><ol class="flow">%s</ol>'
        '<p class="howread-sub">Each part, and what breaks without it</p>'
        '<table><thead><tr><th>Part</th><th>What it does</th><th>Why it exists</th>'
        '<th>If you remove it</th></tr></thead><tbody>%s</tbody></table></div>'
        % (figid, fig_b64(svg), alt, caption, steps, rows))

# ================= FIGURE 1: discovery funnel =================
def f1():
    b = [("Success metrics", "how we measure a win"),
         ("Constraints", "latency, budget, rules"),
         ("Data reality", "what data really exists"),
         ("Risk tolerance", "cost of being wrong"),
         ("Decision rights", "who signs off")]
    inner = DEFMARK
    for i, (t, s) in enumerate(b):
        y = 18 + i * 104
        inner += box(20, y, 340, 84, "#EAF0FA", BLUE)
        inner += txt(190, y + 34, t, 17)
        inner += txt(190, y + 60, s, 13, MUTED, weight=400)
        inner += arrow(360, y + 42, 600, 270, BOARD)
    inner += box(600, 130, 500, 300, CARD, BOARD)
    inner += txt(850, 168, "Signed requirements doc", 18, BOARD)
    rows = [("Targets", "the numbers that define done"),
            ("Budgets", "cost and latency caps"),
            ("Data map", "sources, owners, freshness"),
            ("Risk register", "failure modes, who reviews")]
    for i, (t, s) in enumerate(rows):
        y = 196 + i * 56
        inner += '<rect x="624" y="%d" width="452" height="46" rx="8" fill="%s" stroke="%s"/>' % (y, CODEBG, RULE)
        inner += txt(640, y + 29, t + ": " + s, 14, INK, "start", 400)
    inner += txt(560, 545, "Five buckets in. One signed document out. No architecture talk until this exists.", 14, MUTED, weight=400)
    return svg_doc(1120, 570, inner)

# ================= FIGURE 2: business to technical translation =================
def f2():
    pairs = [("Lawyers take 45 min per contract", "p95 extraction time under 30 s"),
             ("Clause X must be right", "at least 95% precision, 5 clause types"),
             ("We cannot overspend", "at most $0.40 per contract"),
             ("Legal owns the final call", "human review queue for low confidence")]
    inner = DEFMARK
    inner += txt(250, 40, "Business language", 17, AMBER)
    inner += txt(870, 40, "Technical requirement", 17, BLUE)
    for i, (l, r) in enumerate(pairs):
        y = 70 + i * 105
        inner += box(20, y, 460, 82, "#FFF6E6", AMBER)
        inner += txt(250, y + 48, l, 15, INK, weight=400)
        inner += box(640, y, 460, 82, "#EAF0FA", BLUE)
        inner += txt(870, y + 48, r, 15, INK, weight=400)
        inner += arrow(490, y + 41, 630, y + 41, BOARD)
    inner += txt(560, 510, "Translation is the architect's core move: every business sentence becomes a measurable requirement.", 14, MUTED, weight=400)
    return svg_doc(1120, 535, inner)

# ================= FIGURE 3: trade-off triangle =================
def f3():
    inner = DEFMARK
    inner += '<polygon points="560,70 170,470 950,470" fill="#F1F4FA" stroke="#163D7A" stroke-width="2"/>'
    inner += txt(560, 45, "ACCURACY", 17, BOARD)
    inner += txt(120, 505, "LATENCY", 17, BOARD)
    inner += txt(1000, 505, "COST", 17, BOARD)
    opts = [(560, 165, BLUE, "A: frontier model"), (520, 330, TEAL, "B: balanced"),
            (745, 415, AMBER, "C: cheap and fast")]
    for x, y, c, lab in opts:
        inner += '<circle cx="%d" cy="%d" r="14" fill="%s" stroke="#FFFFFF" stroke-width="3"/>' % (x, y, c)
        inner += txt(x, y - 24, lab, 14, INK)
    inner += txt(560, 545, "Push hard toward one corner and the other two pull back. There is no corner that wins all three.", 14, MUTED, weight=400)
    return svg_doc(1120, 570, inner)

# ================= FIGURE 4: decision memo structure =================
def f4():
    steps = [("1. Decision", "one sentence"), ("2. Options", "two or three"),
             ("3. Recommendation", "your pick, with reasons"),
             ("4. Tripwire", "what would change it")]
    inner = DEFMARK
    for i, (t, s) in enumerate(steps):
        x = 20 + i * 272
        inner += box(x, 40, 252, 120, "#EAF0FA" if i < 3 else "#FFF6E6", BLUE if i < 3 else AMBER)
        inner += txt(x + 126, 88, t, 16)
        inner += txt(x + 126, 118, s, 13, MUTED, weight=400)
        if i < 3:
            inner += arrow(x + 252, 100, x + 272, 100, BOARD)
    inner += box(20, 210, 1080, 150, CARD, BOARD)
    inner += txt(560, 244, "The one table the stakeholder can read", 16, BOARD)
    cols = ["Option", "Cost per 1k", "p95 latency", "Accuracy", "Risk"]
    for i, c in enumerate(cols):
        x = 60 + i * 208
        inner += txt(x + 80, 282, c, 14, MUTED)
    inner += '<line x1="40" y1="296" x2="1080" y2="296" stroke="#E3E0D8" stroke-width="1.5"/>'
    for r, vals in enumerate([["A: frontier", "$18", "9 s", "97%", "low"],
                              ["B: balanced", "$4", "3 s", "94%", "medium"]]):
        y = 322 + r * 30
        for i, v in enumerate(vals):
            x = 60 + i * 208
            inner += txt(x + 80, y, v, 14, INK, weight=400)
    inner += txt(560, 400, "Non-technical stakeholders judge rows they understand: money, speed, correctness, risk.", 14, MUTED, weight=400)
    return svg_doc(1120, 425, inner)

# ================= FIGURE 5: two SLAs =================
def f5():
    inner = ""
    inner += txt(60, 50, "Availability SLA: 99.9% (is it up?)", 17, BLUE, "start")
    inner += '<rect x="60" y="70" width="1000" height="44" rx="8" fill="#EAF0FA" stroke="#1F5FBF" stroke-width="1.5"/>'
    inner += '<rect x="60" y="70" width="4" height="44" rx="2" fill="#C0392B"/>'
    inner += txt(560, 145, "Downtime budget: 43 minutes per month. After that, the SLA is breached.", 14, MUTED, "middle", 400)
    inner += txt(60, 200, "Quality SLA: 95% correct (is it right?)", 17, AMBER, "start")
    for i in range(20):
        x = 60 + i * 50
        c = RED if i == 19 else "#2F7D32"
        inner += '<rect x="%d" y="220" width="42" height="44" rx="6" fill="%s"/>' % (x, c)
    inner += txt(560, 295, "1,000 sampled outputs per week. At most 50 may be wrong. One red cell = 50 wrong outputs.", 14, MUTED, "middle", 400)
    inner += box(60, 330, 1000, 120, CARD, BOARD)
    inner += txt(560, 366, "The contract needs both, measured separately", 16, BOARD)
    inner += txt(560, 400, "Availability is measured by uptime monitors. Quality is measured by human-graded eval samples.", 14, INK, weight=400)
    inner += txt(560, 428, "An availability SLA never covers quality. Promise only what you measure.", 14, INK, weight=400)
    return svg_doc(1120, 475, inner)

# ================= FIGURE 6: error budget burn =================
def f6():
    inner = ""
    inner += '<line x1="80" y1="40" x2="80" y2="400" stroke="#24292F" stroke-width="2"/>'
    inner += '<line x1="80" y1="400" x2="1060" y2="400" stroke="#24292F" stroke-width="2"/>'
    inner += txt(60, 60, "100%", 13, MUTED, "end", 400)
    inner += txt(60, 400, "0%", 13, MUTED, "end", 400)
    inner += '<line x1="80" y1="328" x2="1060" y2="328" stroke="#C0392B" stroke-width="2" stroke-dasharray="8,6"/>'
    inner += txt(1050, 318, "20%: freeze features", 13, RED, "end")
    pts = [(80, 60), (240, 110), (400, 150), (560, 210), (720, 300), (880, 345), (1060, 352)]
    pl = " ".join("%d,%d" % p for p in pts)
    inner += '<polyline points="%s" fill="none" stroke="#1F5FBF" stroke-width="3.5"/>' % pl
    for x, y in pts:
        inner += '<circle cx="%d" cy="%d" r="6" fill="#1F5FBF" stroke="#FFFFFF" stroke-width="2"/>' % (x, y)
    for d, x in [("Day 1", 80), ("Day 10", 406), ("Day 20", 733), ("Day 30", 1060)]:
        inner += txt(x, 425, d, 13, MUTED, weight=400)
    inner += txt(80, 25, "Error budget remaining", 15, BOARD, "start")
    inner += txt(560, 470, "Burn the budget too fast and the team stops shipping features until reliability recovers.", 14, MUTED, weight=400)
    return svg_doc(1120, 495, inner)

# ================= FIGURE 7: stakeholder map =================
def f7():
    inner = ""
    inner += '<line x1="560" y1="40" x2="560" y2="440" stroke="#5C6570" stroke-width="1.5"/>'
    inner += '<line x1="60" y1="240" x2="1060" y2="240" stroke="#5C6570" stroke-width="1.5"/>'
    inner += txt(560, 475, "Interest in the project (low to high)", 14, MUTED, weight=400)
    inner += txt(30, 240, "Influence", 14, MUTED, "start", weight=400)
    quads = [("Manage closely", 810, 140, "#EAF0FA", BLUE),
             ("Keep satisfied", 310, 140, "#FFF6E6", AMBER),
             ("Keep informed", 810, 340, "#EFF0EA", TEAL),
             ("Monitor", 310, 340, "#F4F2ED", MUTED)]
    for lab, x, y, fill, stroke in quads:
        inner += '<rect x="%d" y="%d" width="440" height="160" rx="10" fill="%s" stroke="%s" stroke-width="1.5" opacity="0.55"/>' % (x - 220, y - 80, fill, stroke)
        inner += txt(x, y - 52, lab, 16, stroke)
    dots = [("Exec sponsor", 860, 120, BLUE), ("Legal / compliance", 260, 120, AMBER),
            ("End users", 860, 330, TEAL), ("IT helpdesk", 260, 330, MUTED)]
    for lab, x, y, c in dots:
        inner += '<circle cx="%d" cy="%d" r="11" fill="%s" stroke="#FFFFFF" stroke-width="3"/>' % (x, y, c)
        inner += txt(x, y + 34, lab, 14, INK)
    inner += txt(560, 520, "Plot every stakeholder once. The quadrant decides how much of your week they get.", 14, MUTED, weight=400)
    return svg_doc(1120, 545, inner)

# ================= FIGURE 8: ADR anatomy =================
def f8():
    inner = ""
    inner += box(60, 30, 640, 470, CARD, BOARD)
    inner += txt(380, 62, "ADR-004: Retrieval with rerank", 17, BOARD)
    bands = [("1. Title", "the decision in one line"),
             ("2. Context", "the problem and the forces at play"),
             ("3. Decision", "what we chose, and the options we rejected"),
             ("4. Consequences", "what gets better, what gets worse"),
             ("5. Status", "proposed, accepted, or superseded")]
    for i, (t, s) in enumerate(bands):
        y = 84 + i * 80
        inner += '<rect x="84" y="%d" width="592" height="68" rx="8" fill="%s" stroke="%s"/>' % (y, "#EAF0FA" if i % 2 == 0 else CODEBG, RULE)
        inner += txt(104, y + 28, t, 15, BOARD, "start")
        inner += txt(104, y + 52, s, 13, MUTED, "start", 400)
    inner += box(740, 30, 320, 470, "#FFF6E6", AMBER)
    inner += txt(900, 66, "The rules", 16, AMBER)
    rules = ["Numbered, in order", "Stored with the code", "Short: one page", "Never deleted,",
             "only superseded", "Written at decision", "time, not later"]
    for i, r in enumerate(rules):
        inner += txt(900, 108 + i * 30, r, 14, INK, weight=400)
    inner += txt(560, 535, "Six months later, nobody remembers why. The ADR does.", 14, MUTED, weight=400)
    return svg_doc(1120, 560, inner)

# ================= FIGURE 9: handoff pipeline =================
def f9():
    inner = DEFMARK
    steps = [("Architecture\ndiagram", "the map"), ("Decision\nrecords", "the why"),
             ("Eval set\n+ runner", "the proof"), ("Runbook", "the playbook"),
             ("Named\nowners", "the people")]
    for i, (t, s) in enumerate(steps):
        x = 20 + i * 216
        inner += box(x, 60, 196, 150, "#EAF0FA" if i < 4 else "#E8F3E8", BLUE if i < 4 else GREEN)
        for j, line in enumerate(t.split("\n")):
            inner += txt(x + 98, 112 + j * 24, line, 16)
        inner += txt(x + 98, 182, s, 13, MUTED, weight=400)
        if i < 4:
            inner += arrow(x + 196, 135, x + 216, 135, BOARD)
    inner += box(20, 260, 1080, 110, "#FDECEA", RED)
    inner += txt(560, 300, "The most common handoff failure", 16, RED)
    inner += txt(560, 332, "No named owner for the evals. The eval set rots, quality drifts, nobody notices for months.", 14, INK, weight=400)
    inner += txt(560, 410, "A handoff is not a document dump. It is a transfer of ownership, with names and dates.", 14, MUTED, weight=400)
    return svg_doc(1120, 435, inner)

# ================= FIGURE 10: lifecycle loop =================
def f10():
    import math
    inner = DEFMARK
    cx, cy, R = 560, 280, 190
    phases = ["Discover", "Design", "Build", "Hand off", "Monitor", "Iterate"]
    subs = ["ask first", "decide", "construct", "transfer", "watch", "improve"]
    for i, (p, s) in enumerate(zip(phases, subs)):
        a = -math.pi / 2 + i * math.pi / 3
        x = cx + R * math.cos(a); y = cy + R * math.sin(a)
        inner += '<circle cx="%d" cy="%d" r="62" fill="#EAF0FA" stroke="#1F5FBF" stroke-width="2"/>' % (x, y)
        inner += txt(int(x), int(y) - 2, p, 15, BOARD)
        inner += txt(int(x), int(y) + 20, s, 12, MUTED, weight=400)
    for i in range(6):
        a1 = -math.pi / 2 + i * math.pi / 3 + 0.40
        a2 = -math.pi / 2 + (i + 1) * math.pi / 3 - 0.40
        x1 = cx + R * math.cos(a1); y1 = cy + R * math.sin(a1)
        x2 = cx + R * math.cos(a2); y2 = cy + R * math.sin(a2)
        inner += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#163D7A" stroke-width="2.5" marker-end="url(#ah)"/>' % (x1, y1, x2, y2)
    inner += '<circle cx="%d" cy="%d" r="78" fill="#163D7A"/>' % (cx, cy)
    inner += txt(cx, cy - 6, "EVALS", 17, "#FFFFFF")
    inner += txt(cx, cy + 18, "the steering wheel", 12, "#FFFFFF", weight=400)
    inner += txt(560, 540, "Every loop turns on the evals. Drift shows in the dashboard first, not in user complaints.", 14, MUTED, weight=400)
    return svg_doc(1120, 565, inner)

# ================= BODY =================
INTRO = """
<section class="unit" id="intro">
<h1>D5. Stakeholder Communication and Lifecycle Management</h1>
<p class="lede">14% of the exam, about 9 questions. This is the architect's craft volume: how you learn what to build, how you explain your choices, how you write honest contracts for probabilistic systems, and how you keep the system healthy after handoff.</p>
<div class="def"><p class="t-title">What this domain really tests</p>
<p>Every other domain asks what you would build. D5 asks how you would run the whole engagement: discovery, decision, documentation, handoff, monitoring, iteration. The questions are scenario-based. You will read a situation with stakeholders, constraints, and a disagreement, and pick the move a senior architect makes.</p></div>
<h2>How D5 questions are built</h2>
<p>The exam loves three shapes here:</p>
<ol>
<li><strong>The skipped step.</strong> A team jumped to model selection before discovery, or to handoff before evals. The right answer goes back and does the skipped step.</li>
<li><strong>The dishonest promise.</strong> Someone promised 100% accuracy, or signed an SLA with no measurement plan. The right answer restates the promise in honest, measurable terms.</li>
<li><strong>The missing owner.</strong> Quality drifted and nobody noticed. The right answer names an owner, a metric, and a cadence.</li>
</ol>
<p>Read every D5 item constraint-first: who are the stakeholders, what did they actually agree to, what is being measured, and who owns it. The distractor almost always sounds technically clever but ignores one of those four.</p>
</section>
"""

U1 = """
<section class="unit" id="u1">
<h1>Unit 1. Structured discovery and requirement gathering</h1>
<p class="lede">Discovery is the interview before the design. Structured means you run it from a fixed checklist, not from vibes.</p>

<h2>What it is</h2>
<p>Structured discovery is a planned series of conversations and document reviews that happens before any architecture is drawn. Requirement gathering is the output: a written, signed set of measurable requirements. "Structured" is the key word. An unstructured kickoff meeting produces a wish list. A structured discovery produces numbers, constraints, and named decision makers.</p>
<div class="def"><p class="t-title">Plain definition</p>
<p>Discovery: the phase where the architect learns the business problem, the constraints, and the data reality. Requirement: a single testable statement of what the system must do, like "extract the termination clause with at least 95% precision." Gathering: the disciplined process of turning conversations into those statements and getting stakeholders to sign them.</p></div>

<h2>Why it exists</h2>
<p>Most failed AI projects do not fail on model quality. They fail because the team built the wrong thing, or built the right thing against the wrong definition of done. A support team asked for "an AI assistant" and got a chatbot that answered general questions, when what they needed was a tool that drafted replies inside their existing ticket queue. Discovery is the cheapest phase to fix a misunderstanding. Every week you delay it multiplies the cost of being wrong.</p>
<p>There is a second reason specific to this exam: stakeholders describe solutions, not problems. "We want RAG" is a solution. "Our analysts cannot find the right policy document and each search takes 20 minutes" is a problem. The architect's job in discovery is to refuse the premature solution and dig for the problem underneath.</p>

<h2>How it works under the hood</h2>
<p>Run discovery as short, focused sessions, one per stakeholder type. Sixty minutes each is enough. In each session you fill five buckets:</p>
<dl class="kv">
<dt>1. Success metrics</dt><dd>How will we know this worked? Push for numbers with dates: "cut average handle time from 8 minutes to 5 by Q2." If the stakeholder cannot name a number, the project is not ready for architecture.</dd>
<dt>2. Constraints</dt><dd>Latency caps, cost ceilings, compliance rules, deployment limits. Ask directly: "what is the maximum cost per request you can live with?" and "is there data that must never leave our network?"</dd>
<dt>3. Data reality</dt><dd>What data actually exists, who owns it, how fresh it is, what shape it is in. Demo on real data as early as possible. Synthetic examples hide the mess that will break your system.</dd>
<dt>4. Risk tolerance</dt><dd>What does a wrong answer cost? A wrong movie recommendation costs nothing. A wrong contract clause costs a lawsuit. The answer sets your whole quality bar and your human review budget.</dd>
<dt>5. Decision rights</dt><dd>Who can sign off on scope, on the eval results, on go-live? Write the names down. "The team" is not a decision maker.</dd>
</dl>
<p>Two techniques make this work. First, ask "what does a bad day look like?" It surfaces failure modes that polite questions miss. Second, end every session with a one-page write-up and get an explicit signoff. A requirement nobody signed is a rumor.</p>
<details><summary>You might be wondering: how is this different from normal product discovery?</summary>
<p>It is not different in spirit, but AI systems add two discovery questions that traditional software skips. One: what is the acceptable wrong-answer rate, stated as a number? Traditional software is deterministic, meaning the same input always gives the same output, so this question never comes up. Two: where does human judgment sit in the loop, and who pays for that labor? Every AI system that touches real decisions needs an answer to both before design starts.</p>
</details>

<h2>Worked example: contract review assistant</h2>
<p>A legal team asks for "AI to speed up contract review." Discovery surfaces this:</p>
<table><thead><tr><th>Bucket</th><th>What we learned</th></tr></thead><tbody>
<tr><td>Success metrics</td><td>800 contracts per month, 12 lawyers, current review 45 minutes each. Target: 10 minutes of lawyer time per contract within 6 months.</td></tr>
<tr><td>Constraints</td><td>Contracts are confidential and cannot leave the company network. Budget ceiling $8,000 per month for model calls.</td></tr>
<tr><td>Data reality</td><td>2,400 past contracts with lawyer-marked clauses exist. Scanned PDFs, mixed quality. No clean labels for 2 of the 5 clause types.</td></tr>
<tr><td>Risk tolerance</td><td>A missed termination clause can cost six figures. Every AI-extracted clause gets a 2-minute lawyer check. Wrong answers are caught, but slow answers are not worth it.</td></tr>
<tr><td>Decision rights</td><td>The general counsel signs off on go-live. The head of legal ops owns the eval set.</td></tr>
</tbody></table>
<p>Those notes become signed requirements: extract 5 clause types with at least 95% precision each, p95 latency under 30 seconds, cost at most $0.40 per contract, every output routed through the lawyer check queue, deployment inside the company network. Notice how each requirement traces back to one bucket.</p>

<h2>Common misunderstanding</h2>
<div class="trap"><p class="t-title">Trap: "discovery means asking stakeholders what they want"</p>
<p>Stakeholders describe what they want in terms of solutions ("use the biggest model", "add a chatbot"). If you write those down as requirements, you become an order taker and you own the failure when the solution misses. Discovery means asking what problem they have, what it costs them today, and what "fixed" looks like in numbers. Then you choose the solution.</p></div>

{F1}

{F2}

<div class="examq"><p class="t-title">Exam relevance</p>
<p>D5 discovery questions test whether you do the elicitation step before the architecture step. When a scenario hands you a vague request ("build an AI assistant for support"), the credited move is almost always structured discovery: define success metrics, constraints, data reality, and risk tolerance first. Any answer that picks a model, a retrieval strategy, or a framework before those exist is the trap.</p></div>

<div class="examq"><p class="t-title">How they will ask this</p>
<p><strong>Scenario shape:</strong> a stakeholder request with no numbers: "our support team needs AI help, make it great." Four options: start with model selection, start with RAG design, run structured discovery workshops, or build a prototype immediately.<br>
<strong>The trap:</strong> the prototype option feels fast and the model-selection option feels expert. Both skip the step that makes the rest work.<br>
<strong>The tell:</strong> look for the option that elicits success metrics and constraints before committing to any architecture.</p></div>
</section>
"""

U2 = """
<section class="unit" id="u2">
<h1>Unit 2. Communicating architectural decisions and trade-offs</h1>
<p class="lede">The architect's job is not to pick the best technology. It is to make the trade-offs visible so the business can choose knowingly.</p>

<h2>What it is</h2>
<p>Communicating a decision means presenting it in terms the stakeholder can judge. A non-technical executive cannot judge "we will use a reranker over the top 50 chunks." They can judge "Option A costs three times more per request but halves the error rate, which saves an estimated $40,000 a month in rework." Your job is the translation between those two sentences.</p>
<div class="def"><p class="t-title">Plain definition</p>
<p>A trade-off is a choice where improving one dimension costs you another: accuracy, latency, and cost are the classic three. Communicating it means laying out two or three real options side by side, in business terms, with your recommendation and the one fact that would change your mind.</p></div>

<h2>Why it exists</h2>
<p>Two failure modes live here. The first is the black box decision: the architect picks a model, the stakeholder nods, and six months later the bill arrives and nobody remembers agreeing to it. The second is the detail dump: the architect explains chunking strategies for twenty minutes while the executive quietly stops listening, then approves something they do not understand. Both end with misaligned expectations, and misaligned expectations are what D5 is testing.</p>
<p>There is also a risk argument. If you present one option, you own all the risk of that choice. If you present three options with honest trade-offs and the stakeholder picks, the risk is shared and documented. That is not politics. That is good engineering.</p>

<h2>How it works under the hood: the decision memo</h2>
<p>Use the same four-part structure every time:</p>
<ol>
<li><strong>Name the decision in one sentence.</strong> "Which model tier handles first-pass ticket classification?"</li>
<li><strong>Show two or three options as rows in one table.</strong> Columns are things the stakeholder cares about: cost per 1,000 requests, p95 latency, accuracy on our eval set, and risk. Never more than five columns. Never a column the stakeholder cannot interpret.</li>
<li><strong>Give your recommendation with reasons.</strong> "I recommend B, because it hits the latency budget with headroom and the accuracy gap to A is inside our human-review safety net."</li>
<li><strong>State the tripwire: what would change your mind.</strong> "If ticket volume triples, revisit: A becomes cheaper than the rework cost." This one sentence is what separates a senior architect from a confident guesser. It tells the stakeholder exactly when to come back to you.</li>
</ol>
<p>The accuracy-latency-cost triangle is the mental model behind every such memo. You can push hard toward any one corner, but the other two pull back. A frontier model buys accuracy with money and time. A small fast model buys speed and cost with accuracy. There is no corner that wins all three, and anyone selling one is selling something else.</p>

<h2>Worked example with concrete numbers</h2>
<p>Ticket classification, 500,000 tickets per month, each about 800 input tokens and 50 output tokens. Illustrative pricing, rounded for the math:</p>
<table><thead><tr><th>Option</th><th>Cost per 1k requests</th><th>Monthly cost</th><th>p95 latency</th><th>Accuracy on eval set</th></tr></thead><tbody>
<tr><td>A: frontier model</td><td>$18</td><td>$9,000</td><td>9 s</td><td>97%</td></tr>
<tr><td>B: mid-tier model</td><td>$4</td><td>$2,000</td><td>3 s</td><td>94%</td></tr>
<tr><td>C: small model + rules</td><td>$0.80</td><td>$400</td><td>1 s</td><td>88%</td></tr>
</tbody></table>
<p>Now translate for the stakeholder: "Option A is the most accurate but costs $9,000 a month and keeps customers waiting 9 seconds. Option C is nearly free and instant, but 12% of tickets get misrouted and each misroute costs about $6 in agent rework, which is roughly $36,000 a month at our volume. I recommend B: it fits the budget, answers in 3 seconds, and the 6% it misses are caught by the confidence-threshold review queue. Revisit if volume passes 2 million tickets a month, because then A's accuracy starts paying for itself."</p>
<p>Notice what happened: the recommendation is one paragraph, every number traces to the table, and the tripwire names the exact condition for revisiting. That is the whole skill.</p>

<h2>Common misunderstanding</h2>
<div class="trap"><p class="t-title">Trap: "good communication means more technical detail"</p>
<p>More detail helps engineers. It hurts decision makers. The executive does not need to know what a reranker is; they need to know what each option costs, how fast it answers, how often it is wrong, and what you recommend. Detail that does not change the decision is noise. A separate trap: presenting your favorite option alone "to keep it simple." That removes the stakeholder's ability to judge and hands you all the risk.</p></div>

{F3}

{F4}

<div class="examq"><p class="t-title">Exam relevance</p>
<p>Trade-off communication questions give you a stakeholder (often non-technical) and ask for the best next move. The credited answer frames the choice in business terms, shows options with their costs, and makes a recommendation. The traps are: answering with a bare technology pick ("use the frontier model"), drowning the stakeholder in mechanism detail, or presenting one option as the only path.</p></div>

<div class="examq"><p class="t-title">How they will ask this</p>
<p><strong>Scenario shape:</strong> an executive asks "which model should we use for the support assistant?" and the case gives you cost, latency, and accuracy numbers for two tiers.<br>
<strong>The trap:</strong> an option that picks the most accurate model "because quality matters most," with no mention of the budget or latency constraint from the case.<br>
<strong>The tell:</strong> the right answer names the trade-off in the stakeholder's currency (cost per resolved ticket, wait time, error cost), recommends one option, and states what would change the call.</p></div>
</section>
"""

U3 = """
<section class="unit" id="u3">
<h1>Unit 3. Feedback loops, expectation alignment, and SLAs</h1>
<p class="lede">A promise you cannot measure is a wish. This unit is about writing honest, measurable promises for systems that are sometimes wrong.</p>

<h2>What it is</h2>
<p>An <strong>SLA (service level agreement)</strong> is a contract about performance: what level the system will hit, over what time window, and what happens if it misses. Two companion terms: an <strong>SLI (service level indicator)</strong> is the thing you actually measure (for example, the fraction of successful requests), and an <strong>SLO (service level objective)</strong> is the target you set for it (for example, 99.9%). The SLA is the contract that references the SLO and adds the remedy.</p>
<p>A <strong>feedback loop</strong> is a scheduled checkpoint where stakeholders see real performance data and adjust expectations or plans. Weekly eval reviews with the product owner. Monthly business reviews with executives. The loop is what keeps the SLA honest after signing day.</p>
<div class="def"><p class="t-title">Plain definition</p>
<p>Expectation alignment means the stakeholder's mental model of the system matches reality, on purpose and in writing. For AI systems the hardest part of that is probabilistic honesty: saying plainly, in the contract, that the system will sometimes be wrong, how often, and what happens then.</p></div>

<h2>Why SLAs mean something different for LLM apps</h2>
<p>Traditional software is deterministic: the same input always produces the same output. If the code is correct and the server is up, the answer is right. So one SLA, "the service responds correctly 99.9% of the time," covers everything.</p>
<p>An LLM is probabilistic: the same input can produce different outputs on different runs, and even a healthy, fast system gives wrong answers at some rate. That splits the promise in two:</p>
<ul>
<li><strong>Availability SLA: "is it up?"</strong> The fraction of requests that get a successful response. Measured by uptime monitors. A 99.9% availability SLA over a 30-day month allows about 43 minutes of downtime. This says nothing about whether the answers were good.</li>
<li><strong>Quality SLA: "is it right?"</strong> The fraction of outputs that meet the quality bar. Measured by grading a sample of real outputs, usually by humans against a rubric, on a cadence like weekly. Example: "at least 95% of 1,000 weekly sampled outputs pass review."</li>
</ul>
<p>You need both, written separately, measured separately. An availability SLA never covers quality. This is the single most tested idea in D5.</p>

<h2>How it works under the hood</h2>
<p><strong>Designing the availability SLA.</strong> Pick the SLI (successful responses divided by total requests), the window (usually 30 days), and the target. The target sets the error budget: the amount of failure you are allowed before consequences kick in.</p>
<table><thead><tr><th>Availability target</th><th>Allowed downtime per 30 days</th><th>What it means in practice</th></tr></thead><tbody>
<tr><td>99%</td><td>7 hours 12 min</td><td>One bad afternoon a month is fine.</td></tr>
<tr><td>99.9%</td><td>43 min</td><td>Tight but achievable with one region and retries.</td></tr>
<tr><td>99.99%</td><td>4 min 20 s</td><td>Needs multi-region failover and serious engineering.</td></tr>
</tbody></table>
<p>Each extra nine roughly multiplies the engineering cost. Never promise 99.99% because it sounds good. Promise the target your architecture can actually hold, then write the remedy: service credits, a postmortem within 48 hours, a reliability sprint if the budget burns two months running.</p>
<p><strong>Designing the quality SLA.</strong> This is the unfamiliar one, so go slowly:</p>
<ol>
<li><strong>Define the SLI.</strong> "Fraction of sampled outputs graded correct by two independent reviewers against the clause rubric." Note the three choices hidden in that sentence: sampling (you cannot grade everything), graders (humans, not vibes), rubric (written criteria, not gut feel).</li>
<li><strong>Set the SLO as a number with a window.</strong> "At least 95% correct per weekly sample of 1,000 outputs." The window matters: a bad day should not breach a monthly promise, and a bad month should not hide inside a quarterly average.</li>
<li><strong>Name the measurement cost.</strong> Grading 1,000 outputs a week at 2 minutes each is about 33 reviewer hours. Put that labor in the budget during discovery (Unit 1), not as a surprise later.</li>
<li><strong>Write the remedy.</strong> "Two consecutive weeks below 93% triggers a quality review: pause feature work, diagnose the failing segment, and report to the product owner." A quality SLA without a remedy is a poster.</li>
</ol>
<p><strong>Probabilistic honesty, contractually.</strong> "The model is sometimes wrong" becomes contract language in three clauses: the acceptable wrong rate (the quality SLO), the safety net (which outputs get human review before they matter, for example everything below a confidence threshold plus a random 5% sample), and the drift clause (what happens when the measured rate degrades). Never let a stakeholder leave the room believing the system is always right. Correct that belief in the meeting, in writing, before signatures.</p>
<p><strong>The feedback loop cadence.</strong> Match the loop to the stakeholder's quadrant (see the map below):</p>
<ul>
<li>Weekly: eval dashboard review with the product owner and the eval owner. Fifteen minutes. Red metrics get a named investigator.</li>
<li>Monthly: business review with the executive sponsor. Cost, quality trend, and one upcoming decision.</li>
<li>Quarterly: architecture revisit. New model releases, cost drift, and whether the original trade-offs still hold.</li>
<li>Always: demo on real data early, by week two or three. Nothing aligns expectations faster than watching the system handle the stakeholder's own messy inputs.</li>
</ul>

<h2>Worked example: the support assistant SLA</h2>
<p>Availability: 99.9% monthly, measured by the API gateway's 5xx rate. Error budget: 43 minutes. Remedy: 10% service credit per additional 43 minutes, postmortem within 48 hours.</p>
<p>Quality: at least 94% of weekly sampled responses graded "correct and safe" by reviewers, sample size 800. Two weeks below 92% triggers the quality review: feature work pauses, the failing segment (say, refund-policy questions) gets a dedicated fix, results reported to the product owner. Review labor: 800 outputs times 90 seconds is 20 reviewer hours per week, budgeted and staffed.</p>
<p>Notice the shape: every promise has a number, a window, a measurement method, and a remedy. If any of those four is missing, it is not an SLA.</p>

<h2>Common misunderstanding</h2>
<div class="trap"><p class="t-title">Trap: "our availability SLA is 99.9%, so quality is covered"</p>
<p>Availability measures whether the system answered, not whether the answer was right. A system can be up 100% of the month and wrong 20% of the time. The exam will hand you exactly this confusion: a vendor or a stakeholder pointing at an uptime number as proof of correctness. The correct move is to add the separate quality SLA with its own measurement plan.</p></div>
<div class="trap"><p class="t-title">Trap: promising 100% accuracy to close the deal</p>
<p>It feels helpful in the meeting and it is poison in the contract. No probabilistic system hits 100% on real data. The professional move is to refuse the number kindly and replace it: "we cannot promise 100%, but we can promise at least 95% measured weekly, with human review on every low-confidence output, and a written remedy if we miss two weeks running." Stakeholders respect the honesty, and you can actually deliver it.</p></div>

{F5}

{F6}

{F7}

<div class="examq"><p class="t-title">Exam relevance</p>
<p>SLA questions test the availability-versus-quality split and the four parts of a real SLA (metric, window, measurement, remedy). Expectation questions test probabilistic honesty: the credited answer restates an absolute promise ("100% accurate") as a measured rate with a safety net. Feedback-loop questions test cadence and ownership: who sees what data, how often, and who investigates red metrics.</p></div>

<div class="examq"><p class="t-title">How they will ask this</p>
<p><strong>Scenario shape:</strong> a stakeholder demands 100% accuracy in the contract, or a vendor's 99.9% uptime SLA is presented as proof the answers are reliable. Sometimes paired: "select two" items where one correct move is the quality SLA and the other is the human review safety net.<br>
<strong>The trap:</strong> accepting the 100%, or accepting the uptime number as covering correctness, or proposing an SLA with no measurement method.<br>
<strong>The tell:</strong> look for the answer that splits the promise in two (availability and quality), attaches a measurement plan and a remedy to each, and names who does the grading.</p></div>
</section>
"""

U4 = """
<section class="unit" id="u4">
<h1>Unit 4. Architecture documentation and implementation guidance</h1>
<p class="lede">Teams forget why decisions were made. Documentation is how the architecture survives contact with the future.</p>

<h2>What it is</h2>
<p>Architecture documentation has two parts. <strong>Decision records</strong> explain why: the context, the options, the choice, the consequences. <strong>Implementation guidance</strong> explains how: enough detail that an engineering team can build the system without you in the room, but not so much that the documents rot the moment code changes.</p>
<div class="def"><p class="t-title">Plain definition</p>
<p>An <strong>ADR (architecture decision record)</strong> is a short, numbered document that captures one significant decision. The classic format has five parts: title, context, decision, consequences, and status. ADRs live with the code, are never deleted, and are superseded (not edited) when the decision changes. A <strong>runbook</strong> is the operational playbook: how to deploy, how to monitor, what to do when each alert fires.</p></div>

<h2>Why it exists</h2>
<p>Six months after launch, someone will propose "simplifying" the eval pipeline, or swapping the reranker for a cheaper one, or removing the human review queue to cut cost. Without a written record of why those pieces exist, each simplification looks reasonable in isolation and the system's quality dies by a thousand cuts. The ADR is the institutional memory that says "we tried that, here is what happened, here is the number."</p>
<p>The second reason is handoff. The architect rarely operates the system long term. Implementation guidance is what makes the handoff real instead of ceremonial: the team inherits not just diagrams but the eval set, the runbook, and the names of who owns what.</p>

<h2>How it works under the hood</h2>
<p><strong>Writing an ADR.</strong> One decision per record, one page, written at decision time, not reconstructed later. The five parts:</p>
<ol>
<li><strong>Title:</strong> "ADR-004: Retrieval with reranking instead of long-context stuffing." Numbered in order, so the sequence tells the story.</li>
<li><strong>Context:</strong> the problem and the forces. "Support articles average 40k tokens. Stuffing full articles into context costs $X per request at Y latency and buries the answer in noise."</li>
<li><strong>Decision:</strong> what you chose and what you rejected. "We retrieve the top 50 chunks and rerank to 8. We rejected full-context stuffing (too slow, too costly) and fine-tuning (data too thin)."</li>
<li><strong>Consequences:</strong> what gets better and what gets worse, honestly. "Better: 3x cheaper, 4x faster, accuracy up 2 points on the eval set. Worse: new failure mode when the retriever misses; mitigated by the fallback to full-article search on low confidence."</li>
<li><strong>Status:</strong> proposed, accepted, or superseded. When ADR-011 later replaces this decision, ADR-004 stays in the repo marked superseded, with a pointer. History is never rewritten.</li>
</ol>
<p><strong>The handoff package.</strong> Five items, in order, each with a named owner and a date:</p>
<ol>
<li><strong>Architecture diagram:</strong> the current system map, boxes with opinions, data flowing in one direction.</li>
<li><strong>Decision records:</strong> the ADR sequence, so the team knows why each box looks the way it does.</li>
<li><strong>Eval set plus runner:</strong> the tests that prove the system works, with a one-command way to run them. This is the most skipped item and the most expensive to skip.</li>
<li><strong>Runbook:</strong> deploy steps, dashboards, and a playbook per alert ("if quality SLO breaches, do this first").</li>
<li><strong>Named owners:</strong> who owns the evals, who owns the prompts, who is on call. Names, not teams.</li>
</ol>
<p><strong>Implementation guidance</strong> sits between architecture and code: interface contracts, data schemas, the eval bar a change must clear before merging, and the explicit non-goals ("do not add new tools without an ADR"). It tells engineers where they have freedom and where they do not.</p>
<details><summary>You might be wondering: how much documentation is too much?</summary>
<p>The test is simple: can a competent engineer who was not in the room make a safe change? If yes, you have enough. ADRs plus the handoff package pass that test at low maintenance cost because each ADR is one page and the eval set is executable truth. A 60-page architecture wiki fails the test: nobody reads it, so nobody trusts it, so it rots. Short, numbered, and next to the code beats long, pretty, and in a wiki.</p>
</details>

<h2>Worked example: ADR-004 with numbers</h2>
<p>Context: 500,000 support tickets a month, each needing policy context. Two designs on the table. Full-article stuffing: average 40k input tokens per request at an illustrative $3 per million tokens is $0.12 per request, $60,000 a month, p95 latency 14 seconds. Retrieval with rerank: 8 chunks at 500 tokens each plus overhead is about 6k tokens per request, $0.018 per request, $9,000 a month, p95 latency 3 seconds. Eval accuracy: 93% for stuffing, 95% for rerank on the 2,000-case golden set.</p>
<p>Decision: retrieval with rerank. Consequences, stated honestly: we save roughly $51,000 a month and answer 4x faster with slightly better accuracy, but we accept a new failure mode (retriever misses the right article) and we mitigate it with a low-confidence fallback plus a weekly review of fallback cases. Status: accepted, signed by the product owner on the date in the record.</p>
<p>That ADR is why, a year later, nobody "simplifies" the system back to stuffing. The numbers are in the repo.</p>

<h2>Common misunderstanding</h2>
<div class="trap"><p class="t-title">Trap: "documentation means a comprehensive wiki page"</p>
<p>Comprehensive wikis are where decisions go to be forgotten. The exam's version of this trap is a handoff that looks complete on paper: diagrams, wiki links, a walkthrough meeting, but no eval set, no runbook, and no named eval owner. Quality then drifts silently because nobody owns the thing that would have caught it. The credited answer always includes the executable eval set and the named owner.</p></div>

{F8}

{F9}

<div class="examq"><p class="t-title">Exam relevance</p>
<p>Documentation questions test whether you know what makes a handoff real: decision records, an executable eval set, a runbook, and named owners. The classic trap is the handoff missing eval ownership: the scenario describes quality decaying after the architects leave, and the credited answer assigns an eval owner and a review cadence, not a better model.</p></div>

<div class="examq"><p class="t-title">How they will ask this</p>
<p><strong>Scenario shape:</strong> an engineering team inherited a Claude system six months ago and accuracy has drifted downward. Options include retraining, switching models, writing an ADR for the original choices, or establishing eval ownership with a weekly review.<br>
<strong>The trap:</strong> the technical fixes (new model, retraining) feel decisive but address no diagnosed cause.<br>
<strong>The tell:</strong> the scenario never established who owns quality measurement. The right move restores the missing ownership and measurement first: assign the eval owner, reinstate the review cadence, diagnose the failing segment, then decide.</p></div>
</section>
"""

U5 = """
<section class="unit" id="u5">
<h1>Unit 5. Lifecycle management: handoff, monitoring, iteration</h1>
<p class="lede">Handoff is not the end of the project. It is the middle. The system lives or dies on what happens after.</p>

<h2>What it is</h2>
<p>The lifecycle has six phases: <strong>discover</strong> (learn the problem), <strong>design</strong> (choose the architecture), <strong>build</strong> (construct it), <strong>hand off</strong> (transfer ownership), <strong>monitor</strong> (watch it in production), <strong>iterate</strong> (improve it). Then the loop turns again. The steering wheel for the whole loop is the eval set from Unit 4: every iteration is judged by measured results, not by opinions about what should work.</p>
<div class="def"><p class="t-title">Plain definition</p>
<p><strong>Monitoring</strong> is the continuous collection of the four production signals: quality (is it still right?), latency (is it still fast?), cost (is it still affordable?), and safety (is anything harmful happening?). <strong>Iteration</strong> is the disciplined cycle of detecting a change in those signals, diagnosing the cause, fixing it, re-evaluating, and shipping. Lifecycle management is owning that cycle on purpose instead of reacting to user complaints.</p></div>

<h2>Why it exists</h2>
<p>Production systems decay. Data formats change. User behavior shifts. A new model version behaves slightly differently. Without a managed loop, the first sign of decay is an angry customer or a surprising bill, and by then the damage is weeks old. With a managed loop, the eval dashboard shows the dip on Tuesday, the owner investigates on Wednesday, and the fix ships before most users notice.</p>
<p>The deeper reason: an AI system is never "done" the way a bridge is done. Its environment (data, users, models, costs) keeps moving. Lifecycle management is the admission that launch day is a starting line, written into roles, dashboards, and calendars.</p>

<h2>How it works under the hood</h2>
<p><strong>The four signals, each with an owner and a threshold:</strong></p>
<table><thead><tr><th>Signal</th><th>What you watch</th><th>Example threshold</th></tr></thead><tbody>
<tr><td>Quality</td><td>Weekly graded sample pass rate</td><td>Below 93% two weeks running triggers review</td></tr>
<tr><td>Latency</td><td>p95 response time</td><td>Above 5 s for one hour pages the on-call</td></tr>
<tr><td>Cost</td><td>Spend per 1,000 requests</td><td>20% above budget for a week triggers investigation</td></tr>
<tr><td>Safety</td><td>Blocked or flagged outputs, user reports</td><td>Any novel jailbreak pattern triggers same-day review</td></tr>
</tbody></table>
<p><strong>The iteration loop, step by step:</strong></p>
<ol>
<li><strong>Detect:</strong> a signal crosses its threshold. The dashboard, not a human, finds it.</li>
<li><strong>Diagnose the segment:</strong> quality dropped from 96% to 91%. On which segment? Refund questions, after the policy PDF was reformatted. Aggregate numbers hide this; per-segment evals reveal it. Never skip diagnosis.</li>
<li><strong>Fix narrowly:</strong> update the chunking for the new PDF layout, or add the missing examples to the prompt. One change at a time.</li>
<li><strong>Re-evaluate:</strong> run the full eval set, including the regression cases. A fix that heals one segment and breaks another is not a fix.</li>
<li><strong>Ship and watch:</strong> deploy, then watch the signal for a full cycle before declaring victory.</li>
</ol>
<p><strong>Revisit triggers</strong> are the calendar version of the loop: events that force an architecture review whether or not a signal fired. A new model generation ships. Cost doubles. The business enters a regulated market. The original ADRs get re-read and either reaffirmed or superseded. Without triggers, architecture reviews happen never.</p>

<h2>Worked example: the drift that got caught</h2>
<p>Week 14 after launch. The weekly graded sample shows quality at 91%, down from a steady 96%. Per-segment breakdown: refund-policy questions fell from 97% to 82%; everything else is flat. Diagnosis: the company reformatted its refund policy PDF in week 12, and the chunker now splits the key table across two chunks, so the retriever returns half the rule.</p>
<p>Fix: adjust chunk boundaries for table-heavy documents and add 40 refund cases to the golden set. Re-evaluation: full set passes at 96%, refund segment back at 96%, no regressions elsewhere. The fix ships in the normal release train. Total user-visible impact: near zero, because the loop caught it in the dashboard instead of in the support inbox.</p>
<p>Now the counterfactual the exam loves: the same drift with no eval owner and no weekly review. The first signal is a spike in refund complaints in week 20. Diagnosis starts from angry tickets instead of clean data. The fix takes three weeks instead of three days. That gap is what lifecycle management buys.</p>

<h2>Common misunderstanding</h2>
<div class="trap"><p class="t-title">Trap: "monitoring means watching uptime and error rates"</p>
<p>Uptime and error rates are the availability half. For an AI system the dangerous decay is silent: the service is up, the responses are fast, and the answers are slowly getting worse. Quality monitoring (the graded sample) and cost monitoring (spend per request) are what catch the failures that uptime dashboards miss. An answer that only watches infrastructure metrics is the trap.</p></div>
<div class="trap"><p class="t-title">Trap: "when quality drops, switch to a bigger model"</p>
<p>A bigger model is a guess, not a diagnosis. Maybe the data changed, maybe the prompt regressed, maybe one segment broke. The professional loop is detect, diagnose the segment, fix narrowly, re-evaluate. Model switching is what you do after diagnosis says the current tier cannot hit the bar, and then you write the ADR for it.</p></div>

{F10}

<div class="examq"><p class="t-title">Exam relevance</p>
<p>Lifecycle questions test the loop, not the phases in isolation. The scenario gives you post-launch decay and asks for the next move. The credited answer follows the loop: check the eval signals, diagnose the segment, fix narrowly, re-evaluate. Traps jump straight to model changes or blame the data without measurement. Also watch for the "handoff is the end" framing: any option that treats go-live as the finish line is wrong.</p></div>

<div class="examq"><p class="t-title">How they will ask this</p>
<p><strong>Scenario shape:</strong> three months after launch, users report worse answers on a specific topic. Options: switch to the newest model, add more training data, check the eval dashboard and diagnose the failing segment, or roll back to the launch-day prompt.<br>
<strong>The trap:</strong> the newest model feels like progress; the rollback feels safe. Both skip diagnosis.<br>
<strong>The tell:</strong> the right answer starts with measurement (what do the evals say, which segment moved) and only then chooses a fix. If an option mentions per-segment evals, it is usually the credited one.</p></div>
</section>
"""

OUTRO = """
<section class="unit" id="exam-tactics">
<h1>D5 exam tactics</h1>
<p class="lede">Five rules that answer most D5 questions.</p>
<ol>
<li><strong>Constraint-first reading.</strong> Before looking at the options, write down the stakeholders, the numbers, and the missing pieces. The trap option almost always ignores one of them.</li>
<li><strong>The skipped step is the answer.</strong> Discovery before architecture. Measurement before promises. Diagnosis before fixes. Ownership before handoff.</li>
<li><strong>Split every absolute promise.</strong> "100% accurate" becomes a measured quality rate with a safety net. "99.9% uptime" never covers correctness.</li>
<li><strong>Name the owner.</strong> If the scenario has drifting quality and no named eval owner, the answer creates one. Metrics without owners are decorations.</li>
<li><strong>Recommend, do not decree.</strong> Show options in business terms, recommend one, state the tripwire. That is the senior architect's voice the exam rewards.</li>
</ol>
<p class="note">All figures in this volume were constructed from first principles for this study guide (no external image sources applied to these abstract process concepts). Cost and pricing numbers are illustrative, rounded for teaching the math, not quotes.</p>
</section>
"""

# ================= ASSEMBLY =================
NAV = """
<div class="layout">
<aside class="rail">
<h2>D5. Stakeholder Communication</h2>
<p class="sub">CCAR-P study guide &middot; 14% &middot; ~9 questions</p>
<nav><ul>
<li><a class="ch" href="#intro"><span class="n">0</span>Domain orientation</a></li>
<li><a class="ch" href="#u1"><span class="n">1</span>Structured discovery</a></li>
<li><a class="ch" href="#u2"><span class="n">2</span>Decisions and trade-offs</a></li>
<li><a class="ch" href="#u3"><span class="n">3</span>Feedback loops and SLAs</a></li>
<li><a class="ch" href="#u4"><span class="n">4</span>Documentation and handoff</a></li>
<li><a class="ch" href="#u5"><span class="n">5</span>Lifecycle management</a></li>
<li><a class="ch" href="#exam-tactics"><span class="n">6</span>Exam tactics</a></li>
</ul></nav>
</aside>
<div class="main"><div class="wrap">
"""

FOOTER = """
</div></div></div>
</body></html>
"""

def main():
    figs = {
        "{F1}": figure("fig1", f1(),
            "Discovery funnel: five elicitation buckets converging into one signed requirements document",
            "Structured discovery: five buckets in, one signed requirements document out.",
            ["Start with the five buckets on the left: success metrics, constraints, data reality, risk tolerance, decision rights.",
             "Fill each bucket in a focused 60-minute session with the right stakeholder type.",
             "Follow the arrows right: every bucket contributes rows to the signed requirements document.",
             "Read the document's four parts: targets, budgets, data map, risk register.",
             "No architecture work starts until this document is signed."],
            [("Success metrics", "Numbers that define done", "Without them the project cannot be judged", "You build the wrong thing and nobody can prove it"),
             ("Constraints", "Latency, budget, compliance caps", "They rule out whole architectures early", "You design something illegal or unaffordable"),
             ("Data reality", "What data exists and its shape", "Demo on real data or inherit surprises", "The system breaks on the messy real inputs"),
             ("Risk tolerance", "Cost of a wrong answer", "Sets the quality bar and review budget", "No safety net where one was needed"),
             ("Decision rights", "Named people who sign off", "'The team' cannot approve anything", "Decisions stall or get reversed later")]),
        "{F2}": figure("fig2", f2(),
            "Translation map: four business statements on the left each converted to a measurable technical requirement on the right",
            "The architect's core move: every business sentence becomes a measurable requirement.",
            ["Read a business statement on the left, in the stakeholder's own words.",
             "Follow the arrow to the technical requirement on the right.",
             "Check that each requirement has a number: 30 seconds, 95%, $0.40, a named queue.",
             "A business sentence with no measurable translation is not a requirement yet."],
            [("Business language", "What the stakeholder says", "It carries the real need", "You solve the stated solution instead of the problem"),
             ("Arrow", "The translation step", "This is the architect's value-add", "Vague wishes become vague systems"),
             ("Technical requirement", "A testable statement", "It can be built and verified", "No definition of done exists"),
             ("Numbers", "Every row has one", "Numbers make promises checkable", "Expectations drift silently")]),
        "{F3}": figure("fig3", f3(),
            "Trade-off triangle with accuracy, latency, and cost at the corners and three plotted options A, B, and C",
            "The accuracy-latency-cost triangle: push toward one corner, the other two pull back.",
            ["Read the three corners: accuracy at the top, latency and cost at the base.",
             "Find option A near the accuracy corner: frontier model, best answers, expensive and slow.",
             "Find option C near the latency-cost edge: cheap and fast, least accurate.",
             "Find option B in the middle: the balanced pick most systems land on."],
            [("Accuracy corner", "How often the answer is right", "The dimension stakeholders ask for first", "Chasing it blindly blows the budget"),
             ("Latency corner", "How fast the answer arrives", "Users feel every second", "Ignoring it kills adoption"),
             ("Cost corner", "What each answer costs", "Scale multiplies every cent", "Ignoring it kills the project at volume"),
             ("The triangle", "You cannot win all three", "Forces honest choices", "Someone promises a free corner that does not exist")]),
        "{F4}": figure("fig4", f4(),
            "Decision memo structure: four steps flowing into a stakeholder-readable comparison table",
            "The decision memo: four steps, one table the stakeholder can actually read.",
            ["Step 1 names the decision in one sentence.",
             "Step 2 lays out two or three options as rows.",
             "Step 3 gives your recommendation with reasons tied to the table.",
             "Step 4 states the tripwire: the one fact that would change your mind.",
             "The table below uses only columns the stakeholder can judge: money, speed, correctness, risk."],
            [("Decision", "One sentence naming the choice", "Focuses the whole conversation", "The meeting drifts across five topics"),
             ("Options", "Two or three real alternatives", "Lets the stakeholder exercise judgment", "One option means you own all the risk"),
             ("Recommendation", "Your pick, with reasons", "Stakeholders pay for judgment", "No recommendation is abdication"),
             ("Tripwire", "What would change your mind", "Says exactly when to come back", "The decision silently goes stale"),
             ("The table", "Business-unit columns only", "Non-technical readers can decide", "Mechanism detail they cannot judge")]),
        "{F5}": figure("fig5", f5(),
            "Two SLA tracks: a 99.9% availability bar with a 43-minute downtime budget, and a 95% quality bar showing 50 allowed wrong outputs per 1,000",
            "Two SLAs, measured separately: availability asks 'is it up', quality asks 'is it right'.",
            ["Top track: the availability SLA. The bar is one month; the red tip is the 43-minute downtime budget.",
             "Read the caption: after 43 minutes down, the SLA is breached. Monitors measure this.",
             "Bottom track: the quality SLA. Twenty cells stand for 1,000 graded outputs; one red cell is the 50 allowed wrong.",
             "Read the bottom box: the two promises need different metrics, different measurement, different owners."],
            [("Availability SLA", "Fraction of successful responses", "Proves the service answers", "Downtime with no contract or remedy"),
             ("Downtime budget", "43 min per month at 99.9%", "Makes the target concrete", "A percentage nobody can picture"),
             ("Quality SLA", "Fraction of outputs graded correct", "Proves the answers are good", "A fast, up, confidently wrong system"),
             ("Human grading", "Sampled outputs vs a rubric", "The only honest quality metric", "Vibes-based quality claims")]),
        "{F6}": figure("fig6", f6(),
            "Error budget burn-down chart over 30 days with a dashed 20% line marked freeze features",
            "Error budget burn: spend the budget too fast and feature work stops until reliability recovers.",
            ["The vertical axis is budget remaining, from 100% at the top to 0% at the bottom.",
             "The blue line burns downward as incidents consume the budget across the month.",
             "The dashed red line at 20% is the policy tripwire.",
             "Crossing it freezes feature work: the team fixes reliability until the budget recovers."],
            [("Budget", "Allowed failure for the window", "Turns reliability into a number", "Arguments about whether things are 'bad enough'"),
             ("Burn line", "How fast failure is consumed", "Shows trouble weeks before the budget hits zero", "Surprise breaches at month end"),
             ("20% tripwire", "The freeze-features policy", "Protects reliability automatically", "Feature pressure burns the budget to zero"),
             ("The freeze", "Stop features, fix reliability", "Prevents death spirals", "Shipping features on a burning system")]),
        "{F7}": figure("fig7", f7(),
            "Stakeholder map: influence versus interest grid with four plotted stakeholders in four quadrants",
            "The stakeholder map: the quadrant decides how much of your week each person gets.",
            ["Horizontal axis is interest in the project, vertical axis is influence over it.",
             "Top right is manage closely: the executive sponsor, weekly contact.",
             "Top left is keep satisfied: legal and compliance, consulted on risk, not drowned in detail.",
             "Bottom right is keep informed: end users, demos and updates. Bottom left is monitor: helpdesk, light touch."],
            [("Manage closely", "High influence, high interest", "They can fund or kill the project", "The sponsor is surprised at the worst moment"),
             ("Keep satisfied", "High influence, low interest", "They can block on risk grounds", "Compliance vetoes at go-live"),
             ("Keep informed", "Low influence, high interest", "They live with the system daily", "Users reject a system they never saw"),
             ("Monitor", "Low influence, low interest", "Cheap to keep in the loop", "Small issues become surprises")]),
        "{F8}": figure("fig8", f8(),
            "ADR anatomy: a document with five numbered bands (title, context, decision, consequences, status) and a rules panel",
            "ADR anatomy: five short parts that explain one decision forever.",
            ["Band 1 is the title: the decision in one line, with its number.",
             "Band 2 is context: the problem and the forces that shaped the choice.",
             "Band 3 is the decision: what was chosen and what was rejected.",
             "Band 4 is consequences: what gets better and what gets worse, stated honestly.",
             "Band 5 is status: proposed, accepted, or superseded. The rules panel on the right says ADRs live with the code and are never deleted."],
            [("Title", "The decision in one line", "Findable later", "Nobody can locate the decision"),
             ("Context", "Problem and forces", "Explains why it was reasonable", "Future readers judge with hindsight"),
             ("Decision", "Choice plus rejected options", "Shows the road not taken", "'Simplifications' that repeat old mistakes"),
             ("Consequences", "Honest trade-offs", "Prevents selective memory", "Only the wins are remembered"),
             ("Status", "Proposed, accepted, superseded", "History stays accurate", "Edited history nobody trusts")]),
        "{F9}": figure("fig9", f9(),
            "Handoff pipeline: five boxes from architecture diagram to named owners, with a red warning strip about missing eval ownership",
            "The handoff pipeline: five items, each with a named owner. The red strip names the most common failure.",
            ["Follow the five boxes left to right: diagram, decision records, eval set with runner, runbook, named owners.",
             "Each box is a transfer: the team receives something they can use, not just read.",
             "Read the red strip: the most common failure is handing off with no named owner for the evals.",
             "Without that owner the eval set rots, quality drifts, and nobody notices for months."],
            [("Architecture diagram", "The system map", "Shared mental model", "Everyone holds a different picture"),
             ("Decision records", "Why each box exists", "Stops repeated mistakes", "Good decisions get 'simplified' away"),
             ("Eval set + runner", "Executable proof it works", "Quality is checkable by anyone", "Quality becomes unmeasurable"),
             ("Runbook", "Deploy and alert playbooks", "On-call can act at 3am", "Every incident is a fresh panic"),
             ("Named owners", "People, not teams", "Someone is accountable", "Diffusion of responsibility")]),
        "{F10}": figure("fig10", f10(),
            "Lifecycle loop: six phases arranged in a circle around a central hub labeled evals, the steering wheel",
            "The lifecycle loop: six phases turning around the evals at the center.",
            ["Start at the top with Discover and move clockwise: design, build, hand off, monitor, iterate.",
             "Each phase feeds the next; the arrows show the loop never ends at handoff.",
             "The dark hub in the center is the evals: every phase checks against measured results.",
             "Read the caption: drift appears in the dashboard first, in user complaints last."],
            [("Discover", "Learn the problem", "Builds the right thing", "Elegant solutions to wrong problems"),
             ("Design", "Choose the architecture", "Trade-offs made deliberately", "Accidental architecture"),
             ("Build", "Construct the system", "Turns decisions into software", "Nothing to hand off"),
             ("Hand off", "Transfer ownership", "The team can run it alone", "Architect as permanent bottleneck"),
             ("Monitor", "Watch the four signals", "Catches decay early", "Decay found by angry users"),
             ("Iterate", "Fix, re-evaluate, ship", "Compounds improvements", "Launch-and-abandon"),
             ("Evals hub", "The steering wheel", "Every loop turns on measurement", "Opinions steer instead of data")]),
    }

    body = INTRO + U1 + U2 + U3 + U4 + U5 + OUTRO
    for k, v in figs.items():
        body = body.replace(k, v)
    assert "{F" not in body, "unreplaced figure placeholder"

    html = ("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            "<title>CCAR-P D5: Stakeholder Communication and Lifecycle Management</title>"
            "<style>" + CSS + "</style></head><body>" + NAV + body + FOOTER)

    # ---------- QA ----------
    errors = []
    if html.count("\u2014") > 0:
        errors.append("em dash found")
    if re.search(r"linear-gradient|radial-gradient", html):
        errors.append("gradient found")
    if re.search(r"<img[^>]+src=\"http", html):
        errors.append("hotlinked image found")
    if re.search(r"TODO|lorem ipsum|coming soon", html, re.I):
        errors.append("placeholder found")
    if "{F" in html:
        errors.append("unreplaced placeholder")
    ids = re.findall(r'id="([^"]+)"', html)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        errors.append("duplicate ids: %s" % dupes)

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stack = []
            self.bad = []
        def handle_starttag(self, tag, attrs):
            if tag not in ("meta", "link", "img", "br", "hr", "input", "source"):
                self.stack.append(tag)
        def handle_endtag(self, tag):
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            elif tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.bad.append("unclosed: " + self.stack.pop())
                self.stack.pop()
            else:
                self.bad.append("stray close: " + tag)
    p = P()
    p.feed(html)
    if p.bad or p.stack:
        errors.append("tag imbalance: %s / %s" % (p.bad[:5], p.stack[:5]))

    # figure + walkthrough coverage per unit
    for uid in ["intro", "u1", "u2", "u3", "u4", "u5", "exam-tactics"]:
        sec = re.search(r'<section class="unit" id="%s">(.*?)</section>' % uid, html, re.S)
        if not sec:
            errors.append("missing section " + uid)
            continue
        if uid not in ("intro", "exam-tactics"):
            if sec.group(1).count('class="fig"') < 1:
                errors.append(uid + " has no figure")
            if 'class="howread"' not in sec.group(1):
                errors.append(uid + " has no walkthrough")
            if "How they will ask this" not in sec.group(1):
                errors.append(uid + " missing exam-ask box")

    # verify each svg decodes to parseable, non-trivial xml
    import xml.etree.ElementTree as ET
    for m in re.finditer(r'data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)', html):
        raw = base64.b64decode(m.group(1))
        try:
            root = ET.fromstring(raw)
        except Exception as e:
            errors.append("svg parse fail: %s" % e)
            continue
        if len(list(root.iter())) < 10:
            errors.append("svg suspiciously empty")

    n_img = html.count("<img")
    print("images:", n_img, "| sections:", html.count('<section class="unit"'),
          "| howread:", html.count('class="howread"'), "| chars:", len(html))
    if errors:
        print("QA FAIL:")
        for e in errors:
            print(" -", e)
        raise SystemExit(1)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("QA PASS. Wrote", OUT)

main()
