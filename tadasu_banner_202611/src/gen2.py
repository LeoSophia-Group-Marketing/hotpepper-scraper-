CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--deep:#123F46;--teal:#1D5A62;--sage:#5E8C88;--gold:#B8955A;--gold2:#D9C08E;--paper:#F8F4EC;--paper2:#EFE7D8;--ink:#1F2E31;--mute:#5F6E70;--red:#A9412E}
body{width:1080px;height:var(--H);overflow:hidden;font-family:'Noto Sans JP',sans-serif;color:var(--ink);background:var(--paper);-webkit-font-smoothing:antialiased}
.c{position:relative;width:1080px;height:var(--H);display:flex;flex-direction:column;padding-top:var(--pt);
background:radial-gradient(900px 520px at 100% 0%,#EDE3CF 0%,rgba(237,227,207,0) 70%),radial-gradient(700px 500px at 0% 70%,#F1ECE1 0%,rgba(241,236,225,0) 70%),var(--paper)}
.serif{font-family:'Shippori Mincho',serif}
.brand{display:flex;align-items:center;gap:18px;padding:0 64px}
.brand .lg{display:flex;flex-direction:column;gap:2px}
.brand .sm{font-size:17px;letter-spacing:.32em;color:var(--mute);font-weight:500}
.brand .logo{font-family:'Shippori Mincho',serif;font-size:48px;font-weight:700;letter-spacing:.14em;color:var(--deep);line-height:1}
.brand .rule{width:1px;height:56px;background:var(--gold)}
.brand .store{font-family:'Shippori Mincho',serif;font-size:26px;font-weight:700;color:var(--deep);letter-spacing:.08em}
.brand .tl{font-family:'Shippori Mincho',serif;font-size:19px;color:var(--mute);letter-spacing:.2em}
.ph{background-size:cover;background-position:center;filter:saturate(.92) contrast(1.02)}
.card{background-color:#fff;border-radius:6px;box-shadow:0 18px 40px -18px rgba(18,63,70,.35),0 2px 0 rgba(184,149,90,.25)}
.bar{margin-top:auto;position:relative;background:linear-gradient(105deg,#0F363C 0%,var(--teal) 100%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:30px 56px calc(30px + var(--pb));gap:24px}
.bar:before{content:"";position:absolute;left:0;right:0;top:0;height:3px;background:linear-gradient(90deg,rgba(217,192,142,0),var(--gold2) 20%,var(--gold2) 80%,rgba(217,192,142,0))}
.loc{display:flex;align-items:center;gap:14px;white-space:nowrap}
.loc svg{flex:0 0 auto}
.loc .t{font-size:32px;font-weight:700;letter-spacing:.04em}
.loc b{font-family:'Shippori Mincho',serif;font-size:64px;font-weight:700;line-height:1;margin:0 4px;color:#fff}
.price{position:relative;background:var(--paper);color:var(--ink);display:flex;align-items:center;gap:14px;padding:14px 24px 12px;border-radius:4px;white-space:nowrap}
.price .k{display:flex;flex-direction:column;line-height:1.25}
.price .k i{font-style:normal;font-size:15px;font-weight:700;color:#fff;background:var(--gold);padding:2px 8px;border-radius:2px;align-self:flex-start;margin-bottom:4px;letter-spacing:.08em}
.price .k span{font-size:20px;font-weight:700}
.price b{font-family:'Shippori Mincho',serif;font-size:60px;font-weight:800;color:var(--red);line-height:1;letter-spacing:.01em}
.price b small{font-size:28px}
.num{display:inline-flex;width:44px;height:44px;border-radius:50%;background:var(--deep);color:#fff;justify-content:center;align-items:center;font-family:'Shippori Mincho',serif;font-size:24px;font-weight:700;box-shadow:0 0 0 3px #fff,0 0 0 4px var(--gold2)}
.gl{height:1px;background:linear-gradient(90deg,var(--gold),rgba(184,149,90,0))}
"""
PIN='<svg width="40" height="48" viewBox="0 0 24 29" aria-hidden="true"><path d="M12 28s-9-9.6-9-16.2A9 9 0 0 1 21 11.8C21 18.4 12 28 12 28z" fill="#D9C08E"/><circle cx="12" cy="11.5" r="3.6" fill="#123F46"/></svg>'
FONTS='<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=block" rel="stylesheet">'
def page(body,extra,st):
    H,pt,pb=(1920,'250px','290px') if st else (1080,'50px','0px')
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8">{FONTS}<style>{CSS}:root{{--H:{H}px;--pt:{pt};--pb:{pb}}}{extra}</style></head><body><div class="c {"st" if st else "sq"}">{body}</div></body></html>'
def bar(pre,num,post):
    return f'<div class="bar"><div class="loc">{PIN}<span class="t">{pre}<b>{num}</b>{post}</span></div><div class="price"><div class="k"><i>初回限定</i><span>体験施術 60分</span></div><b><small>¥</small>2,000</b></div></div>'
def brand(store='',tl=False):
    s=f'<div class="rule"></div><div class="store">{store}</div>' if store else ''
    t='<div class="rule"></div><div class="tl">いい明日は、いい姿勢から。</div>' if tl else ''
    return f'<div class="brand"><div class="lg"><div class="sm">オーダーメイド整体</div><div class="logo">TADASU</div></div>{s}{t}</div>'
B={}
B['01_駅からルート_元住吉']=(brand('元住吉院')+"""
<h1 class="serif h">改札を出て、<em>1</em>分。</h1>
<div class="sub"><span class="gl" style="flex:0 0 46px;height:2px"></span>元住吉駅から、この建物の5階へ。</div>
<div class="route">
 <figure class="card"><div class="ph p1"></div><figcaption><span class="num">1</span>元住吉駅を出たら</figcaption></figure>
 <svg class="arw" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="#123F46"/><path d="M16 12l9 8-9 8" fill="none" stroke="#D9C08E" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
 <figure class="card"><div class="ph p2"></div><figcaption><span class="num">2</span>マクドナルドさまの上<b>5階</b></figcaption></figure>
</div>"""+bar('元住吉駅から徒歩','1','分'),"""
.h{padding:0 64px;margin-top:26px;font-size:96px;font-weight:800;letter-spacing:.05em;line-height:1.1}
.h em{font-style:normal;color:var(--teal);font-size:120px;margin:0 2px}
.sub{display:flex;align-items:center;gap:14px;padding:0 64px;margin-top:12px;font-size:28px;font-weight:700;color:var(--mute);letter-spacing:.06em}
.route{display:flex;align-items:center;gap:0;padding:0 46px;margin-top:30px}
.route figure{flex:1;padding:12px 12px 14px}
.route .ph{height:300px;border-radius:3px}
.p1{background-image:url(../img/moto_station.jpg)}.p2{background-image:url(../img/moto_building.jpg)}
.route figcaption{margin-top:14px;font-size:24px;font-weight:700;display:flex;align-items:center;gap:12px;padding-left:4px}
.route figcaption b{font-family:'Shippori Mincho',serif;font-size:30px;color:var(--teal);margin-left:2px}
.arw{width:52px;height:52px;margin:0 -14px;z-index:2;flex:0 0 52px;margin-top:-50px;filter:drop-shadow(0 6px 10px rgba(18,63,70,.3))}
.st .h{font-size:100px;margin-top:44px}.st .h em{font-size:128px}.st .sub{font-size:34px}
.st .route{flex-direction:column;margin-top:44px;padding:0 56px}.st .route figure{width:100%}.st .route .ph{height:360px}.st .arw{transform:rotate(90deg);margin:-16px 0;}
""")
B['02_駅前にできました_市ヶ谷']=("""
<div class="ph hero"></div>
<div class="stamp"><span>NEW</span><b>OPEN</b><i>11.4</i></div>
<div class="note card">
 <div class="to"><span class="gl" style="width:40px;height:2px;background:var(--gold)"></span>市ヶ谷のみなさまへ</div>
 <h1 class="serif">駅前に、整体院が<br>できました。</h1>
 <div class="sig"><span class="sm">オーダーメイド整体</span><b class="serif">TADASU</b><span class="st2 serif">市ヶ谷院</span></div>
 <p class="tl serif">いい明日は、いい姿勢から。</p>
</div>"""+bar('市ヶ谷駅から徒歩','2','分'),"""
.c{padding-top:0}
.hero{position:absolute;left:0;top:0;width:1080px;height:580px;background-image:url(../img/ichi_station.jpg);-webkit-mask-image:linear-gradient(#000 62%,rgba(0,0,0,0));mask-image:linear-gradient(#000 62%,rgba(0,0,0,0))}
.stamp{position:absolute;right:70px;top:250px;width:150px;height:150px;border-radius:50%;background:var(--deep);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 0 5px rgba(255,255,255,.9),0 0 0 7px var(--gold2),0 14px 30px rgba(0,0,0,.25);z-index:3}
.stamp span{font-size:20px;letter-spacing:.3em;font-weight:700;color:var(--gold2)}.stamp b{font-family:'Shippori Mincho',serif;font-size:38px;line-height:1;letter-spacing:.06em}.stamp i{font-style:normal;font-family:'Shippori Mincho',serif;font-size:24px;margin-top:4px}
.note{position:relative;margin:340px 56px 0;padding:40px 48px 34px;border-top:6px solid var(--deep)}
.note:after{content:"";position:absolute;inset:10px;border:1px solid rgba(184,149,90,.45);border-radius:3px;pointer-events:none}
.to{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:700;color:var(--teal);letter-spacing:.16em}
.note h1{font-size:78px;font-weight:800;line-height:1.28;margin-top:14px;letter-spacing:.04em}
.sig{display:flex;align-items:baseline;gap:12px;margin-top:20px}.sig .sm{font-size:20px;color:var(--mute);font-weight:700;letter-spacing:.2em}.sig b{font-size:40px;color:var(--deep);letter-spacing:.12em}.sig .st2{font-size:26px;font-weight:700;color:var(--deep)}
.note .tl{margin-top:8px;font-size:19px;color:var(--mute);letter-spacing:.2em}
.st .hero{top:250px;height:840px}.st .stamp{top:900px;width:170px;height:170px}.st .note{margin-top:930px}.st .note h1{font-size:88px}
""")
B['03_整体通いからの卒業_3ステップ']=(brand(tl=True)+"""
<div class="ph hero card"></div>
<h1 class="serif h">整体通いからの<em>卒業</em>を目指せる</h1>
<div class="steps">
 <div class="s card"><i>STEP 01</i><svg viewBox="0 0 40 40"><circle cx="18" cy="18" r="10" fill="none" stroke="#1D5A62" stroke-width="3"/><path d="M26 26l8 8" stroke="#B8955A" stroke-width="4" stroke-linecap="round"/></svg><b>検査</b><p>AIで姿勢と動きを分析</p></div>
 <div class="s card"><i>STEP 02</i><svg viewBox="0 0 40 40"><path d="M8 28c6-2 8-10 12-14s10-4 12-2-2 8-8 10-10 8-16 6z" fill="none" stroke="#1D5A62" stroke-width="3" stroke-linejoin="round"/><circle cx="30" cy="10" r="3" fill="#B8955A"/></svg><b>施術</b><p>国家資格者の手技で整える</p></div>
 <div class="s card"><i>STEP 03</i><svg viewBox="0 0 40 40"><circle cx="20" cy="8" r="4" fill="#B8955A"/><path d="M20 13v12M12 18l8 3 8-3M14 36l6-11 6 11" fill="none" stroke="#1D5A62" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg><b>運動</b><p>戻りにくい体へ運動療法</p></div>
</div>"""+bar('全員が','国家資格','保有'),"""
.hero{margin:22px 56px 0;height:350px;background-image:url(../img/treat1.jpg);border-radius:6px}
.h{text-align:center;margin-top:26px;font-size:58px;font-weight:800;letter-spacing:.04em}
.h em{font-style:normal;color:var(--red);font-size:76px;position:relative;margin:0 4px}
.h em:after{content:"";position:absolute;left:-4px;right:-4px;bottom:6px;height:14px;background:rgba(217,192,142,.45);z-index:-1}
.steps{display:flex;gap:18px;padding:0 56px;margin-top:22px}
.s{flex:1;padding:0 12px 16px;text-align:center;overflow:hidden}
.s i{font-style:normal;display:block;font-family:'Shippori Mincho',serif;font-size:18px;font-weight:700;letter-spacing:.2em;color:var(--gold);margin:14px 0 2px}
.s svg{width:44px;height:44px}
.s b{display:block;font-family:'Shippori Mincho',serif;font-size:38px;color:var(--deep);line-height:1.15}
.s p{font-size:19px;font-weight:700;margin-top:6px;color:var(--mute)}
.loc b{font-size:50px}
.st .hero{height:540px;margin-top:40px}.st .h{font-size:66px;margin-top:44px}.st .h em{font-size:86px}
.st .steps{flex-direction:column;gap:16px;margin-top:36px}.st .s{display:grid;grid-template-columns:120px 56px 110px 1fr;align-items:center;text-align:left;padding:16px 26px}
.st .s i{margin:0;font-size:20px}.st .s svg{width:48px;height:48px}.st .s b{font-size:44px}.st .s p{font-size:27px;margin:0}
""")
B['04_肩こり×駅チカ_中目黒']=("""
<div class="ph hero"></div>
<div class="body">"""+brand('中目黒院').replace('padding:0 64px','')+"""
<h1 class="serif h">中目黒で働く人の、<br>つらい<em>肩こり</em>に。</h1>
<p class="sub">肩こりの原因は人それぞれ。<br>だから施術も、あなた専用に設計します。</p>
<div class="chips"><span><svg viewBox="0 0 20 20"><path d="M4 10.5l4 4 8-9" fill="none" stroke="#B8955A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>全員が国家資格保有</span><span><svg viewBox="0 0 20 20"><path d="M4 10.5l4 4 8-9" fill="none" stroke="#B8955A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>AIで姿勢を分析</span><span><svg viewBox="0 0 20 20"><path d="M4 10.5l4 4 8-9" fill="none" stroke="#B8955A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>一人ひとりに合わせた施術</span></div>
</div>"""+bar('中目黒駅から徒歩','4','分'),"""
.c{padding-top:0}
.hero{height:410px;background-image:url(../img/katakori.jpg);-webkit-mask-image:linear-gradient(#000 70%,rgba(0,0,0,0));mask-image:linear-gradient(#000 70%,rgba(0,0,0,0))}
.body{padding:0 64px;margin-top:-6px}
.body .brand{padding:0}
.h{font-size:70px;font-weight:800;line-height:1.3;margin-top:18px;letter-spacing:.03em}
.h em{font-style:normal;color:var(--teal);background:linear-gradient(transparent 68%,rgba(217,192,142,.6) 68%)}
.sub{font-size:25px;font-weight:500;color:var(--mute);margin-top:14px;line-height:1.6;letter-spacing:.04em}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.chips span{display:inline-flex;align-items:center;gap:6px;background:#fff;border:1px solid #D8CBB1;border-radius:40px;color:var(--deep);font-weight:700;font-size:21px;padding:8px 18px 8px 12px}
.chips svg{width:22px;height:22px}
.st .hero{margin-top:250px;height:620px}.st .h{font-size:84px;margin-top:24px}.st .sub{font-size:32px}.st .chips span{font-size:26px}
""")
B['05_初回体験の中身']=(brand()+"""
<h1 class="serif h">初回60分・<em>2,000円</em>で、<br>ここまでやります。</h1>
<div class="wrap"><div class="ph pic card"></div>
<ol class="tl">
<li><span class="num">1</span><div><b>カウンセリング</b><p>お悩みと生活習慣をうかがいます</p></div></li>
<li><span class="num">2</span><div><b>AI姿勢分析・検査</b><p>不調の原因を見える化</p></div></li>
<li><span class="num">3</span><div><b>オーダーメイド施術</b><p>国家資格者があなた専用に</p></div></li>
<li><span class="num">4</span><div><b>結果のご説明</b><p>体の状態とこれからをご提案</p></div></li>
</ol></div>"""+bar('全院','駅チカ','で通いやすい'),"""
.h{padding:0 64px;margin-top:22px;font-size:68px;font-weight:800;line-height:1.28;letter-spacing:.03em}
.h em{font-style:normal;color:var(--red)}
.wrap{display:flex;gap:30px;padding:0 56px;margin-top:26px;align-items:stretch}
.pic{width:360px;background-image:url(../img/treat2.jpg);background-position:62% center}
.tl{list-style:none;flex:1;display:flex;flex-direction:column;justify-content:space-between;position:relative}
.tl:before{content:"";position:absolute;left:21px;top:30px;bottom:30px;width:2px;background:repeating-linear-gradient(var(--gold2) 0 6px,transparent 6px 12px)}
.tl li{display:flex;gap:18px;align-items:center;position:relative}
.tl li div{flex:1;background:#fff;border-radius:4px;padding:10px 16px;box-shadow:0 8px 20px -12px rgba(18,63,70,.35)}
.tl b{font-size:26px;color:var(--deep)}.tl p{font-size:18px;color:var(--mute);margin-top:2px}
.loc b{font-size:52px}
.sq .wrap{flex:1;margin-bottom:34px}.sq .pic{width:440px;height:400px;align-self:center;background-position:64% 30%}.sq .tl b{font-size:28px}.sq .tl p{font-size:19px}.sq .tl li div{padding:14px 18px}
.st .h{font-size:80px;margin-top:44px}.st .wrap{flex-direction:column;margin-top:40px;gap:34px}.st .pic{width:100%;height:420px}.st .tl{gap:18px}.st .tl b{font-size:34px}.st .tl p{font-size:24px}.st .tl li div{padding:16px 22px}
""")
import os
os.makedirs('out2',exist_ok=True)
for n,(b,e) in B.items():
    for st in (False,True): open(f'out2/{n}_{"9x16" if st else "1x1"}.html','w').write(page(b,e,st))
