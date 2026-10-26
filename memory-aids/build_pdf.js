// Usage: node build_pdf.js
// Prints each print/*.html to A4 PDF in the same folder, then blanks the PDF metadata.
const { chromium } = require('playwright');
const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const dir = path.join(__dirname, 'print');
const CLEAN = 'import sys\nfrom pypdf import PdfReader, PdfWriter\n' +
  'p = sys.argv[1]\nr = PdfReader(p)\nw = PdfWriter(clone_from=r)\nw.metadata = None\n' +
  "w.add_metadata({'/Author': 'Author', '/Title': '', '/Creator': '', '/Producer': '', '/Subject': '', '/Keywords': ''})\n" +
  'with open(p, "wb") as f:\n    w.write(f)\n';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 1400 } });
  for (const name of fs.readdirSync(dir).filter(n => n.endsWith('.html'))) {
    await page.goto('file://' + path.join(dir, name), { waitUntil: 'load' });
    await page.waitForTimeout(800);
    const out = path.join(dir, name.replace(/\.html$/, '.pdf'));
    await page.pdf({ path: out, format: 'A4', printBackground: true,
      margin: { top: '12mm', bottom: '12mm', left: '12mm', right: '12mm' } });
    const res = spawnSync('python3', ['-c', CLEAN, out]);
    if (res.status !== 0) { console.log('metadata clean failed', name, String(res.stderr)); }
    console.log('pdf', path.basename(out));
  }
  await browser.close();
})();
