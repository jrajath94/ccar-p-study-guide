// Usage: node mermaid_render.js in.json out.json
// in: {"theme":"neutral"|"dark", "items":{"key":"code",...}}  out: {"key":{"svg":...,"error":...}}
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const inp = JSON.parse(fs.readFileSync(process.argv[2]));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent('<html><body><div id="c"></div></body></html>');
  await page.addScriptTag({ path: require.resolve('mermaid/dist/mermaid.min.js') });
  const out = await page.evaluate(async ({ theme, items }) => {
    const tvx = { fontSize: '15px' };
    const tv0 = theme === 'dark'
      ? { background:'#000000', primaryColor:'#000000', primaryTextColor:'#f2f2f2', primaryBorderColor:'#d0d0d0', lineColor:'#d0d0d0', secondaryColor:'#000000', tertiaryColor:'#000000', textColor:'#f2f2f2', edgeLabelBackground:'#000000', mainBkg:'#000000', nodeBorder:'#d0d0d0' }
      : { background:'#ffffff', primaryColor:'#ffffff', primaryTextColor:'#2b2b2b', primaryBorderColor:'#4a4a4a', lineColor:'#4a4a4a', secondaryColor:'#ffffff', tertiaryColor:'#ffffff', textColor:'#2b2b2b', edgeLabelBackground:'#ffffff', mainBkg:'#ffffff', nodeBorder:'#4a4a4a' };
    // Mind map section colors. Values match MM_VARS in crash.py.
    const cs = theme === 'dark' ? ['#141414', '#f2f2f2'] : ['#f1f1f1', '#1c1c1c'];
    for (let i = 0; i < 12; i++) { tv0['cScale' + i] = cs[0]; tv0['cScaleLabel' + i] = cs[1]; }
    const tv = Object.assign({}, tv0, tvx);
    mermaid.initialize({ startOnLoad: false, theme: 'base', themeVariables: tv, securityLevel: 'strict',
      fontFamily: 'Inter, sans-serif', flowchart: { htmlLabels: false, curve: 'basis', nodeSpacing: 22, rankSpacing: 28, diagramPadding: 4, wrappingWidth: 140 } });
    const res = {};
    let i = 0;
    for (const [k, code] of Object.entries(items)) {
      try {
        await mermaid.parse(code);
        const { svg } = await mermaid.render('m' + (i++), code);
        res[k] = { svg };
      } catch (e) { res[k] = { error: String(e.message || e).slice(0, 300) }; }
    }
    return res;
  }, inp);
  fs.writeFileSync(process.argv[3], JSON.stringify(out));
  await browser.close();
})();
