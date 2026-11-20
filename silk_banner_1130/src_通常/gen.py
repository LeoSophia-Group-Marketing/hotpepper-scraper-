C=[
 dict(k='苦手な人ほど',ph='class2.jpg',pos1='42% 30%',pos2='50% 24%',lead='女性専用マシンピラティス',
  h1='運動が<br><em>苦手な人ほど、</em><br>通いやすい。',h2='運動が<em>苦手な人ほど、</em><br>通いやすい。',
  sub='初心者の方が9割以上。<br>先生の声掛けで、正しい動きに。',sub2='初心者の方が9割以上。先生の声掛けで、正しい動きに。'),
 dict(k='先生がそばで',ph='assist2.jpg',pos1='50% 20%',pos2='50% 18%',bg2='url(assist2.jpg) 0 15%/540px auto no-repeat,url(class2.jpg) 100% 30%/540px auto no-repeat',lead='はじめての方へ',
  h1='はじめてでも、<br>先生が<em>そばで</em><br>教えます。',h2='はじめてでも、<br>先生が<em>そばで</em>教えます。',
  sub='プロトレーナーが、一人ひとりの<br>動きを補助。運動が苦手でも大丈夫。',sub2='プロトレーナーが、一人ひとりの動きを補助。'),
 dict(k='来年こそ',ph='class2.jpg',pos1='42% 30%',pos2='50% 24%',lead='女性専用マシンピラティス',
  h1='来年こそ、<br>運動を<br><em>続けられる</em><br>私に。',h2='来年こそ、運動を<br><em>続けられる</em>私に。',
  sub='初心者の方が9割以上。<br>運動が苦手な人ほど、通いやすい。',sub2='初心者9割以上。苦手な人ほど、通いやすい。'),
]
HEAD='''<!doctype html><html lang="ja"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@600;700;800&family=Noto+Sans+JP:wght@500;700&display=block" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
body{background:#F6F2EE;font-family:'Noto Sans JP',sans-serif;color:#4A3F3A;position:relative;overflow:hidden}
em{font-style:normal;color:#B5776A}
.lead{font-weight:700;color:#A2867A;letter-spacing:.12em;display:flex;align-items:center;gap:14px;white-space:nowrap}
.lead:after{content:"";flex:1;height:2px;background:linear-gradient(90deg,#C7A497,rgba(199,164,151,0))}
.h{font-family:'Shippori Mincho',serif;font-weight:800;letter-spacing:.02em;white-space:nowrap}
.sub{font-family:'Shippori Mincho',serif;font-weight:700;color:#5C4E47;border-top:2px solid #E6D6CE;white-space:nowrap}
.pts{display:flex;gap:12px}.pt{background:#fff;border:2px solid #D9C6BC;border-radius:999px;font-weight:700;color:#8C6E62;white-space:nowrap}
.band{position:absolute;left:40px;right:40px;height:104px;background:#9AB0C8;border-radius:10px;display:flex;align-items:center;justify-content:center;gap:28px;color:#fff}
.band .k{border:2px solid #fff;border-radius:8px;padding:4px 18px;font-size:36px;font-weight:500}
.band .m{font-size:54px;font-weight:700;letter-spacing:.04em}
'''
def sq(c):
  return HEAD+f'''body{{width:1080px;height:1080px}}
.ph{{position:absolute;left:0;top:0;width:540px;height:930px;background:url({c['ph']}) {c['pos1']}/cover}}
.ph:after{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(246,242,238,0) 80%,#F6F2EE 100%),linear-gradient(180deg,rgba(246,242,238,0) 88%,#F6F2EE 100%)}}
.r{{position:absolute;left:574px;top:50px;width:470px}}
.logo{{width:190px;display:block;margin-bottom:30px}}
.lead{{font-size:27px}}
.h{{font-size:64px;line-height:1.22;margin-top:18px}}
.sub{{margin-top:22px;padding-top:18px;font-size:29px;line-height:1.5}}
.pts{{margin-top:22px;flex-wrap:wrap}}.pt{{font-size:22px;padding:6px 16px}}
.bdg{{display:block;width:440px;margin-top:24px}}
.band{{bottom:36px}}
</style></head><body><div class="ph"></div>
<div class="r"><img class="logo" src="logo.png"><div class="lead">{c['lead']}</div><div class="h">{c['h1']}</div>
<div class="sub">{c['sub']}</div><img class="bdg" src="badges.png"></div>
<div class="band"><span class="k">手ぶらOK</span><span class="m">体験レッスン予約 ≫</span></div></body></html>'''
def st(c):
  return HEAD+f'''body{{width:1080px;height:1920px}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:800px;background:{c.get('bg2') or 'url('+c['ph']+') '+c['pos2']+'/cover'}}}
.ph:after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(246,242,238,0) 66%,#F6F2EE 100%)}}
.logo{{position:absolute;left:80px;top:676px;width:200px}}
.bdgs{{position:absolute;right:60px;top:560px;display:flex;gap:14px}}
.b{{width:186px;height:186px;border-radius:50%;background:rgba(255,255,255,.92);border:2px solid #B7A090;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'Shippori Mincho',serif;font-weight:700;color:#8A7363;line-height:1.1;box-shadow:0 4px 14px rgba(90,60,50,.12)}}
.b .s{{font-size:26px}}.b .l{{font-size:52px}}.b .l small{{font-size:26px}}.b .m{{font-size:40px;line-height:1.08}}
.b .n{{font-size:34px}}.b .n small{{font-size:18px;writing-mode:vertical-rl;margin-right:2px}}.b .f{{font-size:13px;font-family:'Noto Sans JP';font-weight:500;margin-top:4px}}
.r{{position:absolute;left:80px;top:790px;width:920px}}
.lead{{font-size:34px}}
.h{{font-size:86px;line-height:1.2;margin-top:14px}}
.sub{{margin-top:18px;padding-top:14px;font-size:33px;line-height:1.45}}
.band{{top:1150px}}
</style></head><body><div class="ph"></div>
<div class="bdgs">
 <div class="b"><span class="s">初心者</span><span class="l">90<small>%</small></span><span class="s">以上</span></div>
 <div class="b"><span class="s">安心の</span><span class="m">女性<br>専用</span></div>
 <div class="b"><span class="s">体験者数</span><span class="n"><small>累計</small>80,000<small style="writing-mode:horizontal-tb;font-size:22px">人</small></span><span class="s">突破</span><span class="f">※2026年9月時点</span></div>
</div>
<div class="r"><div class="lead">{c['lead']}</div><div class="h">{c['h2']}</div><div class="sub">{c['sub2']}</div></div>
<div class="band"><span class="k">手ぶらOK</span><span class="m">体験レッスン予約 ≫</span></div>
<img class="logo" src="logo.png"></body></html>'''
for c in C:
  open(f"sq_{c['k']}.html",'w').write(sq(c)); open(f"st_{c['k']}.html",'w').write(st(c))
