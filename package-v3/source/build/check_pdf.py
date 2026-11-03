"""Blank-page and metadata check. Usage: check_pdf.py FILE.pdf ..."""
import sys, subprocess, tempfile, glob, os
from PIL import Image, ImageStat
from pypdf import PdfReader
for f in sys.argv[1:]:
    r = PdfReader(f)
    d = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', '20', '-gray', f, f'{d}/p'], check=True)
    blank = []
    for i, png in enumerate(sorted(glob.glob(f'{d}/p-*.pgm'))):
        st = ImageStat.Stat(Image.open(png))
        if st.stddev[0] < 2.0:
            blank.append(i + 1)
    print(f'{os.path.basename(f)}: pages={len(r.pages)} blank={blank} meta={dict(r.metadata or {})}')
