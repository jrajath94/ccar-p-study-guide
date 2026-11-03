"""Crash course: pitch-black web HTML (live Mermaid) and white print PDF (pre-rendered Mermaid).
Usage: python3 build_crash.py OUTDIR [DOMAIN_OR_UNIT ...]"""
import os, sys
from common import load_units, html_to_pdf
from crash import build_web, build_print

out = sys.argv[1]
only = sys.argv[2:] or None
os.makedirs(out, exist_ok=True)
units = load_units(only)
sample = bool(only)
name = 'sample-chapter' if sample else 'crash-course'

open(f'{out}/{name}.html', 'w').write(build_web(units, sample))
pdf_html = f'{out}/.{name}.print.html'
open(pdf_html, 'w').write(build_print(units, sample))
html_to_pdf(pdf_html, f'{out}/{name}-print.pdf')
os.remove(pdf_html)
print('built', name, len(units), 'units')
