const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch();
 for (const [f,w,h] of [['sq.html',1080,1080],['st.html',1080,1920]]){
  const fs=require('fs'); if(!fs.existsSync(f)) continue;
  const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
  await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  const ok=await p.evaluate(()=>[...document.fonts].filter(x=>x.status==='loaded').map(x=>x.family).join(','));
  console.log(f,'fonts:',ok.slice(0,120));
  await p.screenshot({path:f.replace('.html','.png')});
 }
 await b.close();
})();
