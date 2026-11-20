const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
for(const f of fs.readdirSync('out2').filter(x=>x.endsWith('.html'))){const st=f.includes('9x16');
const p=await b.newPage({viewport:{width:1080,height:st?1920:1080}});
await p.goto('file://'+process.cwd()+'/out2/'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:'out2/'+f.replace('.html','.png')});await p.close();}
await b.close();})();
