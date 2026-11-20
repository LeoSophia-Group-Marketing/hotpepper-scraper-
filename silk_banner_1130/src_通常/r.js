const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();for(const f of fs.readdirSync('.').filter(f=>f.endsWith('.html'))){const h=f.startsWith('sq')?1080:1920;const p=await b.newPage({viewport:{width:1080,height:h}});await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const bb=await p.evaluate(()=>{let mx=0,mn=1e9;document.querySelectorAll('.r *,.band,.bdgs,.logo').forEach(e=>{const r=e.getBoundingClientRect();if(r.height){mx=Math.max(mx,r.bottom);mn=Math.min(mn,r.top)}});return [mn,mx,document.querySelector('.r').scrollWidth]});console.log(f,bb);
await p.screenshot({path:f.replace('.html','.png')});}await b.close()})();
