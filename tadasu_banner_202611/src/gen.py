import os
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--teal:#1F5A62;--deep:#16444B;--cream:#F6F1E7;--paper:#FBF8F2;--red:#B23A2E;--ink:#26363A;--line:#CDBFA6}
body{width:1080px;height:var(--H);overflow:hidden;font-family:'Noto Sans JP',sans-serif;color:var(--ink);background:var(--paper)}
.c{position:relative;width:1080px;height:var(--H);display:flex;flex-direction:column;padding:var(--pt) 0 0 0;background:
 radial-gradient(circle at 90% 8%,#EFE7D6 0,rgba(239,231,214,0) 40%),var(--paper)}
.serif{font-family:'Shippori Mincho',serif}
.brand{display:flex;align-items:flex-end;gap:14px;padding:0 64px}
.brand .sm{font-size:20px;letter-spacing:.2em;color:#6B7A7C;margin-bottom:8px}
.brand .logo{font-family:'Shippori Mincho',serif;font-size:50px;font-weight:700;letter-spacing:.08em;color:var(--teal);line-height:1}
.brand .store{font-family:'Shippori Mincho',serif;font-size:26px;font-weight:700;color:var(--teal);margin-bottom:4px}
.tag{display:inline-block;background:var(--teal);color:#fff;font-weight:700;font-size:24px;letter-spacing:.08em;padding:8px 18px}
.bar{margin-top:auto;background:linear-gradient(100deg,var(--deep),var(--teal));color:#fff;display:flex;align-items:center;justify-content:space-between;padding:26px 56px calc(26px + var(--pb)) 56px;gap:20px}
.bar .loc{font-size:34px;font-weight:700;display:flex;align-items:baseline;gap:6px;white-space:nowrap}
.bar .loc b{font-family:'Shippori Mincho',serif;font-size:62px;line-height:1}
.bar .price{background:#fff;color:var(--ink);display:flex;align-items:baseline;gap:12px;padding:10px 22px;white-space:nowrap}
.bar .price span{font-size:22px;font-weight:700;line-height:1.2}
.bar .price b{font-family:'Shippori Mincho',serif;font-size:56px;color:var(--red);line-height:1}
.ph{background-size:cover;background-position:center}
.tagline{font-family:'Shippori Mincho',serif;font-size:20px;color:#7A8789;letter-spacing:.15em}
"""
FONTS='<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@600;700;800&family=Noto+Sans+JP:wght@500;700;900&display=block" rel="stylesheet">'
def page(body,extra,st):
    H,pt,pb=(1920,'250px','300px') if st else (1080,'52px','0px')
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8">{FONTS}<style>{CSS}:root{{--H:{H}px;--pt:{pt};--pb:{pb}}}{extra}</style></head><body><div class="c {"st" if st else "sq"}">{body}</div></body></html>'

def bar(loc_pre,num,loc_post):
    return f'<div class="bar"><div class="loc">📍{loc_pre}<b>{num}</b>{loc_post}</div><div class="price"><span>初回体験施術<br>60分</span><b>¥2,000</b></div></div>'

B={}
# 1 route
B['01_駅からルート_元住吉']=( """
<div class="brand"><div><div class="sm">オーダーメイド整体</div><div class="logo">TADASU</div></div><div class="store">元住吉院</div></div>
<h1 class="serif h">改札を出て、<em>1分。</em></h1>
<p class="sub">元住吉駅から、この建物の5階へ。</p>
<div class="route"><figure><div class="ph p1"></div><figcaption><i>1</i>元住吉駅を出たら</figcaption></figure>
<div class="arw">▶</div>
<figure><div class="ph p2"></div><figcaption><i>2</i>マクドナルドさまの上 5階</figcaption></figure></div>
""" + bar('元住吉駅から徒歩','1','分'),
"""
.h{padding:0 64px;margin-top:22px;font-size:92px;font-weight:800;color:var(--ink);letter-spacing:.04em;line-height:1.15}
.h em{font-style:normal;color:var(--teal)}
.sub{padding:0 64px;margin-top:10px;font-size:30px;font-weight:700;color:#4E5D60}
.route{display:flex;align-items:center;gap:14px;padding:0 48px;margin-top:30px}
.route figure{flex:1;background:#fff;padding:12px;box-shadow:0 10px 26px rgba(22,68,75,.14)}
.route .ph{height:330px}
.p1{background-image:url(img/moto_station.jpg)}.p2{background-image:url(img/moto_building.jpg)}
.route figcaption{margin-top:12px;font-size:26px;font-weight:700;display:flex;align-items:center;gap:10px}
.route i{font-style:normal;display:inline-flex;width:40px;height:40px;border-radius:20px;background:var(--teal);color:#fff;justify-content:center;align-items:center;font-size:24px}
.arw{color:var(--teal);font-size:40px}
.st .h{font-size:96px;margin-top:40px}.st .sub{font-size:36px}.st .route{flex-direction:column;margin-top:50px;gap:10px}.st .route figure{width:100%}.st .route .ph{height:380px}.st .arw{transform:rotate(90deg);font-size:44px}
""")
# 2 notice
B['02_駅前にできました_市ヶ谷']=( """
<div class="ph hero"></div>
<div class="note"><div class="to">市ヶ谷のみなさまへ</div>
<h1 class="serif">駅前に、整体院が<br>できました。</h1>
<div class="info"><span class="tag">11/4 OPEN</span><span class="nm">オーダーメイド整体 <b class="serif">TADASU</b> 市ヶ谷院</span></div>
<p class="tagline">いい明日は、いい姿勢から。</p></div>
""" + bar('市ヶ谷駅から徒歩','2','分'),
"""
.c{padding-top:0}
.hero{position:absolute;left:0;top:0;width:1080px;height:560px;background-image:url(img/ichi_station.jpg);-webkit-mask-image:linear-gradient(#000 70%,rgba(0,0,0,0));mask-image:linear-gradient(#000 70%,rgba(0,0,0,0))}
.note{position:relative;margin:360px 56px 0;background:#fff;border-top:8px solid var(--teal);padding:34px 44px 30px;box-shadow:0 14px 34px rgba(22,68,75,.16)}
.to{font-size:28px;font-weight:700;color:var(--teal);letter-spacing:.12em}
.note h1{font-size:76px;font-weight:800;line-height:1.25;margin-top:8px;color:var(--ink)}
.info{display:flex;align-items:center;gap:16px;margin-top:18px}.nm{font-size:26px;font-weight:700}.nm b{font-size:34px;color:var(--teal);letter-spacing:.06em}
.tagline{margin-top:12px}
.st .hero{top:250px;height:820px}.st .note{margin-top:860px;margin-bottom:30px}.st .note h1{font-size:86px}
""")
# 3 graduate steps
B['03_整体通いからの卒業_3ステップ']=( """
<div class="brand"><div><div class="sm">オーダーメイド整体</div><div class="logo">TADASU</div></div><div class="tagline" style="margin:0 0 8px 6px">いい明日は、いい姿勢から。</div></div>
<div class="ph hero"></div>
<h1 class="serif h">整体通いからの<em>卒業</em>を目指せる</h1>
<div class="steps">
<div class="s"><i>STEP 1</i><b>検査</b><p>AIで姿勢と動きを分析</p></div>
<div class="s"><i>STEP 2</i><b>施術</b><p>国家資格者の手技で整える</p></div>
<div class="s"><i>STEP 3</i><b>運動</b><p>戻りにくい体へ運動療法</p></div>
</div>
""" + bar('全員が','国家資格','保有'),
"""
.hero{margin:22px 0 0;height:380px;background-image:url(img/treat1.jpg)}
.h{text-align:center;margin-top:24px;font-size:60px;font-weight:800;letter-spacing:.02em}
.h em{font-style:normal;color:#C0563E;font-size:74px}
.steps{display:flex;gap:16px;padding:0 48px;margin-top:22px}
.s{flex:1;background:#fff;border:2px solid #E3DACA;padding:16px 14px;text-align:center}
.s i{font-style:normal;display:block;font-size:18px;font-weight:700;color:#fff;background:var(--teal);margin:-16px -14px 10px;padding:4px}
.s b{display:block;font-family:'Shippori Mincho',serif;font-size:40px;color:var(--teal)}
.s p{font-size:20px;font-weight:700;margin-top:4px;line-height:1.35}
.bar .loc b{font-size:48px}
.st .hero{height:560px;margin-top:40px}.st .h{font-size:68px;margin-top:40px}.st .h em{font-size:84px}.st .steps{flex-direction:column;margin-top:36px;gap:14px}
.st .s{display:flex;align-items:center;gap:24px;text-align:left;padding:18px 24px}.st .s i{margin:0;padding:8px 12px;font-size:20px}.st .s b{font-size:44px;width:90px}.st .s p{font-size:28px;margin:0}
""")
# 4 symptom x place
B['04_肩こり×駅チカ_中目黒']=( """
<div class="ph hero"></div>
<div class="body">
<div class="brand" style="padding:0"><div><div class="sm">オーダーメイド整体</div><div class="logo">TADASU</div></div><div class="store">中目黒院</div></div>
<h1 class="serif h">中目黒で働く人の、<br>つらい<em>肩こり</em>に。</h1>
<p class="sub">肩こりの原因は人それぞれ。<br>だから施術も、あなた専用に設計します。</p>
<div class="chips"><span>全員が国家資格保有</span><span>AIで姿勢を分析</span><span>一人ひとりに合わせた施術</span></div>
</div>
""" + bar('中目黒駅から徒歩','4','分'),
"""
.c{padding-top:0}
.hero{height:420px;background-image:url(img/katakori.jpg);-webkit-mask-image:linear-gradient(#000 75%,rgba(0,0,0,0));mask-image:linear-gradient(#000 75%,rgba(0,0,0,0))}
.body{padding:0 64px;margin-top:-10px}
.h{font-size:70px;font-weight:800;line-height:1.25;margin-top:16px}
.h em{font-style:normal;color:var(--teal);border-bottom:6px solid #E7C66B}
.sub{font-size:26px;font-weight:700;color:#4E5D60;margin-top:14px;line-height:1.5}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.chips span{border:2px solid var(--teal);color:var(--teal);font-weight:700;font-size:22px;padding:6px 14px;background:#fff}
.st .hero{margin-top:250px;height:640px}.st .h{font-size:82px}.st .sub{font-size:32px}.st .chips span{font-size:26px}
""")
# 5 trial contents
B['05_初回体験の中身']=( """
<div class="brand"><div><div class="sm">オーダーメイド整体</div><div class="logo">TADASU</div></div></div>
<h1 class="serif h">初回60分・<em>2,000円</em>で、<br>ここまでやります。</h1>
<div class="wrap"><div class="ph pic"></div>
<ol class="tl">
<li><i>1</i><div><b>カウンセリング</b><p>お悩みと生活習慣をうかがいます</p></div></li>
<li><i>2</i><div><b>AI姿勢分析・検査</b><p>不調の原因を見える化</p></div></li>
<li><i>3</i><div><b>オーダーメイド施術</b><p>国家資格者があなた専用に</p></div></li>
<li><i>4</i><div><b>結果のご説明</b><p>体の状態とこれからをご提案</p></div></li>
</ol></div>
""" + bar('全院','駅チカ','で通いやすい'),
"""
.h{padding:0 64px;margin-top:20px;font-size:68px;font-weight:800;line-height:1.25}
.h em{font-style:normal;color:var(--red)}
.wrap{display:flex;gap:28px;padding:0 56px;margin-top:26px;align-items:stretch}
.pic{width:380px;background-image:url(img/treat2.jpg);background-position:62% center;box-shadow:0 10px 26px rgba(22,68,75,.14)}
.tl{list-style:none;flex:1;display:flex;flex-direction:column;gap:12px}
.tl li{display:flex;gap:14px;align-items:center;background:#fff;border-left:6px solid var(--teal);padding:12px 16px}
.tl i{font-style:normal;flex:0 0 46px;height:46px;border-radius:23px;background:var(--teal);color:#fff;display:flex;justify-content:center;align-items:center;font-family:'Shippori Mincho',serif;font-size:26px;font-weight:700}
.tl b{font-size:27px}.tl p{font-size:19px;color:#5A686A;margin-top:2px}
.bar .loc b{font-size:52px}
.st .h{font-size:80px;margin-top:40px}.st .wrap{flex-direction:column;margin-top:40px}.st .pic{width:100%;height:440px}.st .tl{gap:14px}.st .tl b{font-size:34px}.st .tl p{font-size:24px}
""")
for name,(body,extra) in B.items():
    for st in (False,True):
        open(f'out/{name}_{"9x16" if st else "1x1"}.html','w').write(page(body,extra,st))
print(len(B))
