// Usage: node svg2png.js list.json   list: [{"svg": "...", "out": "/path.png"}]
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const items = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 2, viewport: { width: 760, height: 600 } });
  for (const it of items) {
    await p.setContent(`<html><head><style>:root{--bg:#fff}body{margin:0;background:#fff;color:#2b2b2b;font-family:Inter,sans-serif}
      #w{width:720px;padding:8px}#w svg{width:100%;height:auto;max-height:none}</style></head><body><div id="w">${it.svg}</div></body></html>`);
    const el = await p.$('#w');
    await el.screenshot({ path: it.out });
  }
  await b.close();
})();
