// Usage: node pdf.js in.html out.pdf A4 0|1 waitMs
const { chromium } = require('playwright');
(async () => {
  const [inp, out, fmt, land, wait] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + inp, { waitUntil: 'load' });
  await p.waitForTimeout(parseInt(wait || '300'));
  await p.emulateMedia({ media: 'print' });
  await p.pdf({ path: out, format: fmt, landscape: land === '1', printBackground: true,
    preferCSSPageSize: true, displayHeaderFooter: false });
  await b.close();
})();
