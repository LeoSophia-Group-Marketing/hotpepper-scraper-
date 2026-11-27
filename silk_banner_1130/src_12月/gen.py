V={
 '年内':('<div class="lead">運動しないまま、</div><div class="big2">今年を<br>終えますか？</div>'),
 '苦手歓迎':('<div class="lead">運動が本当に苦手な方、</div><div class="big2">大歓迎<br>です。</div>'),
 '来年こそ':('<div class="lead">来年こそ、</div><div class="big2">続けられる<br>私に。</div>'),
 '天王寺':('<div class="lead">天王寺MIO直結</div><div class="big2">天王寺へ<br><span class="s">通勤している方へ</span></div>'),
}
CSS='''*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:%dpx;overflow:hidden;background:url(base_%s.png) 0 0/1080px %dpx no-repeat;position:relative}
.blk{position:absolute;left:52px;top:%dpx;width:570px;color:#4F4540}
.lead{white-space:nowrap;font-family:'Noto Sans JP',sans-serif;font-weight:700;font-size:31px;letter-spacing:.14em;color:#8A7766;display:flex;align-items:center;gap:14px}
.lead:after{content:"";flex:0 0 100px;height:2px;background:linear-gradient(90deg,#B7A493,rgba(183,164,147,0))}
.big2{font-family:'Shippori Mincho',serif;font-weight:800;font-size:80px;line-height:1.12;letter-spacing:.02em;margin-top:4px;white-space:nowrap}
.big2 .s{font-size:58px}
.cov{position:absolute;background:#F7F4EF}
.offer{position:absolute;left:51px;top:%dpx;width:555px}
.rib{display:inline-block;background:#D2C2B2;color:#fff;font-family:'Noto Sans JP',sans-serif;font-weight:700;font-size:30px;letter-spacing:.12em;padding:4px 40px 4px 24px;clip-path:polygon(0 0,100%% 0,calc(100%% - 22px) 50%%,100%% 100%%,0 100%%)}
.box{margin-top:12px;background:#AA957A;color:#fff;border-radius:6px;height:84px;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-family:'Noto Sans JP',sans-serif;font-weight:700}
.box .t{font-size:30px;letter-spacing:.04em}
.box .z{font-size:64px;letter-spacing:-.01em;line-height:1}.box .z small{font-size:34px;margin-left:2px}
.note{position:absolute;left:0;right:0;top:%dpx;text-align:center;font-family:'Noto Sans JP',sans-serif;font-size:17px;color:#7A6E66}'''
for sz,(H,off) in {'sq':(1080,0),'st':(1920,219)}.items():
  for k,inner in V.items():
    css=CSS%(H,sz,H,206+off,700+off,1020+off)
    html=f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@600;700;800&family=Noto+Sans+JP:wght@500;700&display=block" rel="stylesheet"><style>{css}</style></head><body>
<div class="cov" style="left:40px;top:{690+off}px;width:590px;height:170px"></div>
<div class="cov" style="left:120px;top:{996+off}px;width:840px;height:72px"></div>
<div class="blk">{inner}</div>
<div class="offer"><div class="rib">今なら</div><div class="box"><span class="t">入会金・登録手数料</span><span class="z">0<small>円</small></span></div></div>
<div class="note">※適用条件あり</div>
</body></html>'''
    open(f'{sz}_{k}.html','w').write(html)
