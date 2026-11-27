const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
 for(const f of fs.readdirSync('.').filter(x=>x.endsWith('.html'))){const st=f.startsWith('st_');
  const p=await b.newPage({viewport:{width:1080,height:st?1920:1080},deviceScaleFactor:1});
  await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
  await p.screenshot({path:f.replace('.html','.png')});}
 await b.close();})();
