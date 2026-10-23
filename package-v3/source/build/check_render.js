// Usage: node check_render.js file.html ...  Prints JSON per file.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const f of process.argv.slice(2)) {
    const res = { file: f, errors: [] };
    for (const vw of [390, 1024]) {
      const p = await b.newPage({ viewport: { width: vw, height: 900 } });
      p.on('pageerror', e => res.errors.push(String(e).slice(0, 200)));
      await p.goto('file://' + f, { waitUntil: 'load' });
      await p.waitForTimeout(1500);
      const r = await p.evaluate(() => {
        const pre = [...document.querySelectorAll('pre.mermaid')];
        const failed = pre.filter(x => !x.querySelector('svg') || /Syntax error/i.test(x.textContent)).length;
        const doc = document.documentElement;
        const overflow = doc.scrollWidth > doc.clientWidth + 1;
        const clipped = [...document.querySelectorAll('p,li,h1,h2,h3,h4,h5')].filter(e => e.scrollWidth > e.clientWidth + 2).length;
        const svgs = document.querySelectorAll('svg').length;
        return { mermaid: pre.length, failed, overflow, clipped, svgs };
      });
      res['w' + vw] = r;
      await p.close();
    }
    console.log(JSON.stringify(res));
  }
  await b.close();
})();
