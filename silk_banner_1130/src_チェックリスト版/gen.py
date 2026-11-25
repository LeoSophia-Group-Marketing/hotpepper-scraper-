import json,os,sys
SC='/tmp/claude-0/-home-user-hotpepper-scraper-/7cdc6278-1f6d-57c9-abf8-2b1dcc209c77/scratchpad'
OUT=SC+'/canvas_root/project/';PRE=SC+'/re/prev/';os.makedirs(PRE,exist_ok=True)
AF=SC+'/artifact-files/2e93268a-a872-42d2-8796-c2b2f300f7c7/'
B='/home/user/hotpepper-scraper-/silk_banner_1130/'
IMG={'LEG':('/_blob/47c971107c6ff92971f986707669e084',AF+'47c971107c6ff92971f986707669e084.jpg'),
 'ARM':('/_blob/e6a34ecb71fb54b4163e86aad9459f60',AF+'e6a34ecb71fb54b4163e86aad9459f60.jpg'),
 'CLS':('/_blob/a20b3108a0915914c9797286f13523de',AF+'a20b3108a0915914c9797286f13523de.jpg'),
 'BACK':('/_blob/5e060296e726d5dafcdafd2b1eedcd23',B+'素材候補/01_先生が背中を補助.jpg'),
 'WIDE':('/_blob/fc5082c6d5e4894e3e53cbd7e61bc66c',B+'素材候補/07_クラス全景と先生_修正.jpg'),
 'LOGO':('/_blob/329e00633c1a10555830a5386a38a2ee',B+'src_通常/logo.png')}
TXT='#3F3430'
TH={'beige':dict(g1='#FBF6F1',g2='#EFE4DA',ac='#56769A',b1='#6E5A4B',b2='#8A7462',soft='#E6D8CC',deep='#D6BFAA'),
    'blue':dict(g1='#F4F7FA',g2='#DCE5EE',ac='#A8677A',b1='#45596C',b2='#5E7488',soft='#CBD7E3',deep='#A9BDD2'),
    'pink':dict(g1='#FBF3F1',g2='#F1E1DD',ac='#56769A',b1='#9A5E6F',b2='#B57A8A',soft='#E8D0CB',deep='#DDB3AC')}
M="font-family: 'Shippori Mincho', serif"
SHP='box-shadow: 0 16px 32px rgba(0,0,0,0.14)'
CARD='background: linear-gradient(180deg, #FFFFFF 0%, #F6F1EF 100%); box-shadow: 0 12px 28px rgba(60,45,40,0.12), inset 0 1px 0 rgba(255,255,255,0.95)'
def img(k,x,y,w,h,extra='',pos='50% 50%',alt='レッスン中の写真'):
  return f'<img src="@{k}@" alt="{alt}" style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; object-fit: cover; object-position: {pos}; {extra}">'
def logo(x,y,w=210): return ''
def _oldlogo(x,y,w=210): return f'<img src="@LOGO@" alt="the SILK" style="position: absolute; left: {x}px; top: {y}px; width: {w}px; z-index: 5">'
def seal(x,y,d,inner,t):
  return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {d}px; height: {d}px; border-radius: 50%; {CARD}; border: 3px solid {t["ac"]}; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; color: {TXT}; line-height: 1.2; z-index: 4">{inner}</div>'
PIE='<svg width="{s}" height="{s}" viewBox="0 0 40 40" aria-hidden="true" style="flex: none"><circle cx="20" cy="20" r="17" fill="none" stroke="{soft}" stroke-width="6"/><circle cx="20" cy="20" r="17" fill="none" stroke="{ac}" stroke-width="6" stroke-dasharray="96.1 106.8" transform="rotate(-90 20 20)"/></svg>'
def lead90(x,y,t,w=None,fs=32,two=False):
  br='<br>' if two else '、'
  return f'<div style="position: absolute; left: {x}px; top: {y}px; display: flex; align-items: center; gap: 16px; font-size: {fs}px; font-weight: 700; color: {TXT}; line-height: 1.4">{PIE.format(s=fs*2,soft=t["soft"],ac=t["ac"])}<span>体験の方の<span style="color: {t["ac"]}">90%以上</span>が{br}ピラティス初心者</span></div>'
def band(top,t,ever):
  l2='ウェア・ソックスの貸出あり' if ever else '入会金・登録手数料も 0円'
  return (f'<div style="position: absolute; left: 0; right: 0; top: {top}px; height: 190px; box-sizing: border-box; padding: 0 44px; background: linear-gradient(100deg, {t["b1"]} 0%, {t["b2"]} 100%); color: #FFFFFF; display: flex; align-items: center; justify-content: space-between; z-index: 6">'
   f'<div style="display: flex; flex-direction: column; gap: 2px; line-height: 1.1">'
   f'<div style="display: flex; align-items: baseline; gap: 14px; white-space: nowrap"><span style="font-size: 58px; font-weight: 700">初回体験レッスン 50分</span>'
   f'<span style="font-weight: 700; font-size: 126px; line-height: 0.95; letter-spacing: -0.02em"><span style="font-size: 72px; margin-right: 4px">¥</span>0</span></div>'
   f'<div style="font-size: 38px; font-weight: 500; opacity: 0.92; white-space: nowrap">{l2}</div></div>'
   f'<img src="@LOGO@" alt="the SILK" style="width: 170px; flex: none; filter: brightness(0) invert(1)"></div>')
def h1(x,y,html,fs,lh=1.28,w=None,extra=''):
  return f'<h1 style="position: absolute; left: {x}px; top: {y}px; margin: 0; {M}; font-weight: 800; font-size: {fs}px; line-height: {lh}; letter-spacing: 0.02em; color: {TXT}; white-space: nowrap; {extra}">{html}</h1>'
def sub(x,y,html,fs=34):
  return f'<p style="position: absolute; left: {x}px; top: {y}px; margin: 0; font-size: {fs}px; font-weight: 500; line-height: 1.5; color: {TXT}; white-space: nowrap">{html}</p>'
def bg(t,extra=''):
  return f'linear-gradient(165deg, {t["g1"]} 0%, {t["g2"]} 100%){extra}'
U=lambda t,s:f'<span style="color: {t["ac"]}; border-bottom: 6px solid {t["ac"]}; padding-bottom: 2px">{s}</span>'
DOT=lambda t,s:f'<span style="color: {t["ac"]}; border-bottom: 5px dotted {t["ac"]}">{s}</span>'
MARK=lambda t,s:f'<span style="background: linear-gradient(transparent 58%, {t["soft"]} 58%); color: {t["ac"]}">{s}</span>'
EMPH=lambda t,s:f'<span style="color: {t["ac"]}; text-emphasis: filled circle {t["ac"]}; -webkit-text-emphasis: filled circle {t["ac"]}">{s}</span>'
BIG=lambda t,s,fs:f'<span style="color: {t["ac"]}; font-size: {fs}px">{s}</span>'
def armw(x,y,w,h,amp,extra=''):
  return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; {wave(w,h,amp)}; overflow: hidden; {extra}"><img src="@ARM@" alt="先生が生徒の腕の動きを補助している様子" style="position: absolute; left: {-int(w*0.09)}px; top: {-int(h*0.01)}px; width: {int(w*1.12)}px; height: {int(h*1.08)}px; object-fit: cover; object-position: 30% 20%"></div>'
def wave(w,h,amp=40):
  return f"clip-path: path('M0 {amp} C {w*0.25:.0f} 0, {w*0.5:.0f} {amp*2}, {w*0.75:.0f} {amp} S {w} 0, {w} {amp} L {w} {h} L 0 {h} Z')"

def LIGHT(t,cx,cy,h,rays=True):
  g=f'<div style="position: absolute; inset: 0; background: radial-gradient(circle at {cx}px {cy}px, #FFFFFF 0%, {t["g1"]} 28%, {t["deep"]} 100%)"></div>'
  if not rays: return g
  sweeps=[(0.55,140),(0.8,90),(1.05,170),(1.3,110)]
  ps=''
  for k,(f,wd) in enumerate(sweeps):
    if cx<540: d=f"M{cx-200} {cy+int(260*f)} C {int(380*f)} {cy+int(60*f)}, {int(700*f)} {cy+int(700*f)}, {int(1300*f)} {cy+int(520*f)}"
    else: d=f"M{cx+200} {cy+int(260*f)} C {1080-int(380*f)} {cy+int(60*f)}, {1080-int(700*f)} {cy+int(700*f)}, {1080-int(1300*f)} {cy+int(520*f)}"
    ps+=f'<path d="{d}" fill="none" stroke="url(#rg{cx}{cy})" stroke-width="{wd}" stroke-linecap="round"/>'
  return g+f'<svg aria-hidden="true" width="1080" height="{h}" viewBox="0 0 1080 {h}" style="position: absolute; left: 0; top: 0; filter: blur(14px); opacity: 0.9"><defs><radialGradient id="rg{cx}{cy}" cx="{cx}" cy="{cy}" r="1300" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.1"/></radialGradient></defs>{ps}</svg>'
def SILK(t,y,h,w=1080):
  return (f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position: absolute; left: 0; top: {y}px"><defs><linearGradient id="sk{y}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["soft"]}"/><stop offset="1" stop-color="{t["deep"]}"/></linearGradient></defs>'
   f'<path d="M0 {h*0.42:.0f} C {w*0.3:.0f} {h*0.05:.0f}, {w*0.55:.0f} {h*0.85:.0f}, {w} {h*0.25:.0f} L{w} {h} L0 {h} Z" fill="url(#sk{y})" opacity="0.65"/>'
   f'<path d="M0 {h*0.62:.0f} C {w*0.35:.0f} {h*0.30:.0f}, {w*0.62:.0f} {h*1.0:.0f}, {w} {h*0.48:.0f} L{w} {h} L0 {h} Z" fill="url(#sk{y})"/>'
   f'<path d="M0 {h*0.62:.0f} C {w*0.35:.0f} {h*0.30:.0f}, {w*0.62:.0f} {h*1.0:.0f}, {w} {h*0.48:.0f}" fill="none" stroke="#FFFFFF" stroke-width="4" opacity="0.8"/></svg>')
def BAND2(t,y,h,ang):
  d=f"M-80 {y+h*0.9:.0f} C 300 {y-h*0.2:.0f}, 700 {y+h*1.3:.0f}, 1160 {y+h*0.1:.0f}"
  return (f'<svg aria-hidden="true" width="1080" height="1920" viewBox="0 0 1080 1920" style="position: absolute; left: 0; top: 0"><defs><linearGradient id="bd{y}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["deep"]}"/><stop offset="0.5" stop-color="{t["soft"]}"/><stop offset="1" stop-color="{t["deep"]}"/></linearGradient></defs>'
   f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="{h+16}" stroke-linecap="round"/><path d="{d}" fill="none" stroke="url(#bd{y})" stroke-width="{h}" stroke-linecap="round"/></svg>')
def RINGS(t,cx,cy,rs): return f'<div style="position: absolute; left: {cx-rs[-1]}px; top: {cy-rs[-1]}px; width: {2*rs[-1]}px; height: {2*rs[-1]}px; border-radius: 50%; background: radial-gradient(circle, #FFFFFF 0%, rgba(255,255,255,0.85) 35%, rgba(255,255,255,0) 70%)"></div>'+''.join(f'<div style="position: absolute; left: {cx-r}px; top: {cy-r}px; width: {2*r}px; height: {2*r}px; border-radius: 50%; border: 8px solid rgba(255,255,255,0.9); box-shadow: 0 0 0 10px {t["soft"]}"></div>' for r in rs)
def WIN(x,y,t,n=3,w=130,h=300,gap=40,skew=-28):
  W=n*w+(n-1)*gap
  return (f'<svg aria-hidden="true" width="{W+200}" height="{h+200}" viewBox="0 0 {W+200} {h+200}" style="position: absolute; left: {x-100}px; top: {y-100}px; filter: blur(6px)">'
   + ''.join(f'<path d="M{100+i*(w+gap)*0.9:.0f} {100+h:.0f} C {100+i*(w+gap)*0.9+w*0.2:.0f} {100+h*0.4:.0f}, {100+i*(w+gap)*0.9+w*1.6:.0f} {100+h*0.5:.0f}, {100+i*(w+gap)*0.9+w*1.9:.0f} 100" fill="none" stroke="#FFFFFF" stroke-opacity="{0.85-i*0.15:.2f}" stroke-width="{w*0.55:.0f}" stroke-linecap="round"/>' for i in range(n))
   + '</svg>')
def RIB(t,pts,wd,id_):
  # thick flowing ribbon along a cubic path, with white edge highlight
  d=f"M{pts[0]} C {pts[1]}, {pts[2]}, {pts[3]}"
  return (f'<svg aria-hidden="true" width="1080" height="1920" viewBox="0 0 1080 1920" style="position: absolute; left: 0; top: 0; overflow: visible"><defs><linearGradient id="{id_}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.45" stop-color="{t["soft"]}"/><stop offset="1" stop-color="{t["deep"]}"/></linearGradient></defs>'
   f'<path d="{d}" fill="none" stroke="{t["deep"]}" stroke-width="{wd+16}" stroke-linecap="round" opacity="0.35"/>'
   f'<path d="{d}" fill="none" stroke="url(#{id_})" stroke-width="{wd}" stroke-linecap="round"/>'
   f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity="0.9"/></svg>')
D={}
# ---------- A 初心者×先生（キャンペーン）
t=TH['beige']
D['Main']=('A 初心者×先生 4:5',1350,t,bg(t),[
 LIGHT(t,40,0,1160),
 img('LEG',500,0,580,1000,f'border-radius: 290px 0 0 0; {SHP}','50% 40%','先生が生徒の脚の動きを補助している様子'),
  WIN(40,930,t,3,120,220,36),
 logo(64,64),lead90(64,170,t,two=True),
 h1(64,330,f'運動が<br>苦手でも、<br>先生が<br>{U(t,"そばに")}。',88),
 sub(64,820,'動きを見ながら、<br>その場で声をかけます。'),
 seal(530,870,260,f'<span style="font-size: 28px; font-weight: 700">11/30まで</span><span style="font-size: 26px">月会費 最大3か月</span><span style="{M}; font-size: 50px; font-weight: 800; color: {t["ac"]}">50%OFF</span>',t),
 seal(830,900,200,f'<span style="{M}; font-size: 44px; font-weight: 800; line-height: 1.1">女性<br>専用</span>',t),
 band(1160,t,False)])
D['A_story']=('A 初心者×先生 9:16',1920,t,bg(t),[
 LIGHT(t,40,760,1920),
 WIN(560,1060,t,3,110,260,34),
 img('WIDE',0,0,1080,780,'','50% 30%','先生が前で教えるクラスの様子'),
 f'<div style="position: absolute; left: 0; top: 560px; width: 1080px; height: 240px; background: linear-gradient(180deg, rgba(251,246,241,0) 0%, {t["g1"]} 100%)"></div>',
 img('LEG',690,450,340,340,f'border-radius: 50%; border: 8px solid #FFFFFF; box-sizing: border-box; {SHP}','50% 40%','先生が生徒の脚の動きを補助している様子'),
 logo(826,850,190),
 seal(64,560,200,f'<span style="{M}; font-size: 44px; font-weight: 800; line-height: 1.1">女性<br>専用</span>',t),
 seal(280,540,260,f'<span style="font-size: 28px; font-weight: 700">11/30まで</span><span style="font-size: 26px">月会費 最大3か月</span><span style="{M}; font-size: 50px; font-weight: 800; color: {t["ac"]}">50%OFF</span>',t),
 lead90(64,850,t),
 h1(64,950,f'運動が苦手でも、<br>先生が{U(t,"そばに")}。',96),
 sub(64,1230,'動きを見ながら、その場で声をかけます。',36),
 band(1370,t,False)])
# ---------- B 駅チカ×時間帯（東京・要差し替え）
t=TH['blue']
def timepanel(x,y,w,t,fs=72):
  clock=f'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{t["ac"]}" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
  cell=lambda a,b:f'<div style="flex: 1; display: flex; flex-direction: column; gap: 4px; align-items: flex-start"><div style="display: flex; align-items: center; gap: 10px; font-size: 30px; font-weight: 700">{clock}{a}</div><div style="{M}; font-size: {fs}px; font-weight: 800; line-height: 1.1; white-space: nowrap">{b}</div></div>'
  return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; padding: 26px 32px; border-radius: 20px; {CARD}; display: flex; gap: 28px; color: {TXT}">{cell("朝は","[0:00]〜")}<div style="width: 3px; background: {t["ac"]}; border-radius: 2px"></div>{cell("夜は","〜[0:00]")}</div>'
STN=lambda t,fs:f'<div style="display: inline-flex; align-items: center; gap: 14px"><span style="width: 8px; height: {int(fs*1.1)}px; background: {t["ac"]}; border-radius: 4px"></span>[駅名]駅から徒歩[X]分</div>'
D['B_station']=('B 駅チカ×時間帯 4:5（[ ]は差し替え）',1350,t,bg(t),[
 LIGHT(t,1060,0,1160),
 WIN(640,560,t,3,110,520,40,24),
 img('CLS',0,0,470,1160,'-webkit-mask-image: linear-gradient(to right, #000 78%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(to right, #000 78%, rgba(0,0,0,0) 100%)','40% 30%','マシンピラティスのクラスを受ける女性たち'),
 logo(806,64),
 f'<div style="position: absolute; left: 500px; top: 190px; font-size: 34px; font-weight: 700; color: {TXT}">{STN(t,34)}</div>',
 h1(500,270,f'[駅名]に<br>通っている<br>方へ。',92),
 sub(500,670,'朝も夜も、<br>通勤の途中でクラスへ。'),
 timepanel(500,830,516,t,46),
 band(1160,t,False)])
D['B_story']=('B 駅チカ×時間帯 9:16（[ ]は差し替え）',1920,t,bg(t),[
 LIGHT(t,1060,760,1920),
 WIN(560,780,t,3,110,560,40,24),
 img('WIDE',0,0,1080,780,'','50% 30%','窓の大きいスタジオでのクラスの様子'),
 f'<div style="position: absolute; left: 0; top: 560px; width: 1080px; height: 240px; background: linear-gradient(180deg, rgba(244,247,250,0) 0%, {t["g1"]} 100%)"></div>',
 logo(826,800,190),
 f'<div style="position: absolute; left: 64px; top: 800px; font-size: 38px; font-weight: 700; color: {TXT}">{STN(t,38)}</div>',
 h1(64,880,'[駅名]に<br>通っている方へ。',96),
 sub(64,1140,'朝も夜も、通勤の途中でクラスへ。',36),
 timepanel(64,600,952,t,68).replace('top: 600px','top: 1210px').replace('padding: 26px 32px','padding: 18px 32px'),
 band(1370,t,False)])
# ---------- C 11月中に×延長
t=TH['pink']
def offcard(x,y,w,t):
  return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; padding: 22px 30px; border-radius: 20px; {CARD}; border-top: 6px solid {t["ac"]}; color: {TXT}"><div style="font-size: 30px; font-weight: 700">月会費 最大3か月</div><div style="{M}; font-size: 92px; font-weight: 800; line-height: 1.05; color: {t["ac"]}">50%OFF</div></div>'
WAVE=lambda t,y,h:f'<svg aria-hidden="true" width="1080" height="{h}" viewBox="0 0 1080 {h}" style="position: absolute; left: 0; top: {y}px"><path d="M0 {h*0.55:.0f} C 260 {h*0.15:.0f}, 520 {h*0.95:.0f}, 1080 {h*0.35:.0f} L1080 {h} L0 {h} Z" fill="{t["soft"]}" opacity="0.7"/><path d="M0 {h*0.75:.0f} C 300 {h*0.45:.0f}, 640 {h:.0f}, 1080 {h*0.6:.0f} L1080 {h} L0 {h} Z" fill="{t["soft"]}"/></svg>'
D['C_extend']=('C 11月中にはじめる×延長 4:5',1350,t,bg(t),[
 LIGHT(t,900,0,1160,False),
 RIB(t,['1180 60','720 80','1060 460','720 700'],150,'r1'),
 RIB(t,['1200 420','960 420','1000 800','420 1200'],70,'r2'),
 SILK(t,700,460),
 logo(64,64),lead90(64,170,t),
 h1(64,270,f'はじめての<br>ピラティスは、<br>{MARK(t,"11月中に")}。',84),
 sub(64,620,'好評につき、11/30まで延長しました。'),
 armw(580,690,450,450,36),
 offcard(64,720,480,t),
 band(1160,t,False)])
D['C_story']=('C 11月中にはじめる×延長 9:16',1920,t,bg(t),[
 LIGHT(t,900,250,1920,False),
 RIB(t,['-120 420','260 360','200 700','520 820'],150,'r1'),
 RIB(t,['-100 160','300 120','420 520','1200 780'],70,'r2'),
 armw(420,250,620,620,44),
 logo(64,300,190),
 offcard(64,560,420,t).replace('font-size: 92px','font-size: 80px'),
 lead90(64,880,t),
 h1(64,960,f'はじめての<br>ピラティスは、<br>{MARK(t,"11月中に")}。',80),
 sub(64,1280,'好評につき、11/30まで延長しました。',36),
 band(1370,t,False)])
# ---------- E 苦手な人ほど（通常）
t=TH['beige']
def panel(x,y,w,h): return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: 28px; background: linear-gradient(180deg, #FFFFFF 0%, #F6F1EF 100%); box-shadow: 0 28px 56px rgba(60,45,40,0.22), inset 0 1px 0 rgba(255,255,255,0.95)"></div>'
D['E_nigate']=('通常 苦手な人ほど 4:5',1350,t,bg(t),[
 img('WIDE',-60,300,1200,900,'filter: blur(22px) saturate(0.9); opacity: 0.75','50% 60%',''),
 img('WIDE',0,0,1080,660,'-webkit-mask-image: linear-gradient(180deg, #000 80%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(180deg, #000 80%, rgba(0,0,0,0) 100%)','50% 35%','先生が前で教えるクラスの様子'),
 panel(40,560,1000,560),
 seal(820,380,200,f'<span style="{M}; font-size: 44px; font-weight: 800; line-height: 1.1">女性<br>専用</span>',t),
 logo(820,1040-430,170).replace('top: 610px','top: 1060px').replace('left: 820px','left: 830px'),
 lead90(96,600,t),
 h1(96,700,f'運動が{DOT(t,"苦手な人ほど")}、<br>通いやすい。',84),
 sub(96,930,'マシンが動きを支えるから、<br>筋力に自信がなくても大丈夫。'),
 band(1160,t,True)])
D['E_nigate_story']=('通常 苦手な人ほど 9:16',1920,t,bg(t),[
 img('WIDE',-80,600,1240,1340,'filter: blur(24px) saturate(0.9); opacity: 0.75','50% 60%',''),
 img('WIDE',0,0,1080,900,'-webkit-mask-image: linear-gradient(180deg, #000 82%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(180deg, #000 82%, rgba(0,0,0,0) 100%)','50% 35%','先生が前で教えるクラスの様子'),
 panel(40,800,1000,540),
 seal(816,600,200,f'<span style="{M}; font-size: 44px; font-weight: 800; line-height: 1.1">女性<br>専用</span>',t),
 logo(826,1250,160),
 lead90(96,840,t),
 h1(96,940,f'運動が{DOT(t,"苦手な人ほど")}、<br>通いやすい。',84),
 sub(96,1170,'マシンが動きを支えるから、<br>筋力に自信がなくても大丈夫。'),
 band(1370,t,True)])
# ---------- F 先生がそばで（通常）
t=TH['blue']
def tag(x,y,s,t): return f'<div style="position: absolute; left: {x}px; top: {y}px; padding: 10px 22px; border-radius: 12px; background: #FFFFFF; border: 2px solid {t["ac"]}; font-size: 28px; font-weight: 700; color: {TXT}; z-index: 4; box-shadow: 0 8px 18px rgba(0,0,0,0.10)">{s}</div>'
def ribbon(y,h,t): return f'<div style="position: absolute; left: 0; right: 0; top: {y}px; height: {h}px; background: linear-gradient(90deg, {t["soft"]} 0%, #FFFFFF 50%, {t["soft"]} 100%)"></div>'
D['F_sensei']=('通常 先生がそばで 4:5',1350,t,bg(t),[
 LIGHT(t,1060,0,1160,False),
 logo(64,64),lead90(64,170,t),
 h1(64,270,f'はじめてでも、<br>先生が{EMPH(t,"そばで")}<br>教えます。',88),
 BAND2(t,770,250,-9),
 img('BACK',64,680,410,410,f'border-radius: 24px; border: 8px solid #FFFFFF; box-sizing: border-box; {SHP}','50% 30%','先生が生徒の背中に手を添えて補助している様子'),
 img('LEG',606,640,410,410,f'border-radius: 24px; border: 8px solid #FFFFFF; box-sizing: border-box; {SHP}','50% 40%','先生が生徒の脚の動きを補助している様子'),
 tag(84,1050,'姿勢を手で整える',t),tag(626,1010,'動きをその場で補助',t),
 band(1160,t,True)])
D['F_sensei_story']=('通常 先生がそばで 9:16',1920,t,bg(t),[
 LIGHT(t,1060,250,1920,False),
 BAND2(t,420,300,-9),
 img('BACK',64,320,440,460,f'border-radius: 24px; border: 8px solid #FFFFFF; box-sizing: border-box; {SHP}','50% 30%','先生が生徒の背中に手を添えて補助している様子'),
 img('LEG',576,270,440,460,f'border-radius: 24px; border: 8px solid #FFFFFF; box-sizing: border-box; {SHP}','50% 40%','先生が生徒の脚の動きを補助している様子'),
 tag(84,720,'姿勢を手で整える',t),tag(596,670,'動きをその場で補助',t),
 logo(64,830,190),lead90(64,930,t),
 h1(64,1030,f'はじめてでも、<br>先生が{EMPH(t,"そばで")}教えます。',84),
 band(1370,t,True)])
# ---------- G 来年こそ（通常）
t=TH['pink']
D['G_rainen']=('通常 来年こそ 4:5',1350,t,bg(t),[
 LIGHT(t,820,300,1160,False),
 RIB(t,['1200 40','640 -40','560 520','1180 760'],120,'g1'),
 RIB(t,['1220 300','760 320','820 1000','520 1160'],70,'g2'),
 img('CLS',600,80,440,1000,f'border-radius: 220px 220px 24px 24px; border: 10px solid #FFFFFF; box-sizing: border-box; {SHP}','45% 35%','マシンピラティスのクラスを受ける女性たち'),
 logo(64,64),lead90(64,170,t,two=True),
 h1(64,330,f'来年こそ、<br>運動を<br>{BIG(t,"続けられる",100)}<br>私に。',84,1.3),
 sub(64,860,'運動が苦手な人ほど、<br>通いやすいピラティス。'),
 seal(500,880,200,f'<span style="{M}; font-size: 44px; font-weight: 800; line-height: 1.1">女性<br>専用</span>',t).replace('left: 500px','left: 520px'),
 band(1160,t,True)])
D['G_rainen_story']=('通常 来年こそ 9:16',1920,t,bg(t),[
 LIGHT(t,900,800,1920,False),
 RIB(t,['1200 260','620 200','560 900','1200 1100'],120,'g1'),
 img('WIDE',0,0,1080,760,'','50% 30%','先生が前で教えるクラスの様子'),
 f'<div style="position: absolute; left: 0; top: 540px; width: 1080px; height: 240px; background: linear-gradient(180deg, rgba(251,243,241,0) 0%, {t["g1"]} 100%)"></div>',
 logo(826,820,190),
 seal(816,600,200,f'<span style="{M}; font-size: 44px; font-weight: 800; line-height: 1.1">女性<br>専用</span>',t),
 lead90(64,820,t),
 h1(64,910,f'来年こそ、運動を<br>{BIG(t,"続けられる",108)}私に。',90,1.3),
 sub(64,1210,'運動が苦手な人ほど、通いやすいピラティス。',36),
 band(1370,t,True)])

FONT='<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@600;700;800&amp;family=Noto+Sans+JP:wght@500;700&amp;display=swap" rel="stylesheet">'
def page(title,h,t,bgv,els,local):
  body='\n'.join(els)
  for k,(u,p) in IMG.items(): body=body.replace(f'@{k}@',('file://'+p) if local else u)
  root=f'<div style="width: 1080px; height: {h}px; position: relative; overflow: hidden; background: {bgv}; font-family: \'Noto Sans JP\', sans-serif; color: {TXT}">\n{body}\n</div>'
  if local: return f'<!doctype html><html lang="ja"><head><meta charset="utf-8">{FONT}<style>body{{margin:0}}</style></head><body>{root}</body></html>'
  props=json.dumps({"$preview":{"width":1080,"height":h}})
  return f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>
body{{margin:0}}
a{{color:#56769A}}a:hover{{color:#3F5A78}}
</style>
</helmet>
{root}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
for k,(title,h,t,bgv,els) in D.items():
  open(OUT+k+'.dc.html','w').write(page(title,h,t,bgv,els,False))
  open(PRE+k+'.html','w').write(page(title,h,t,bgv,els,True))
json.dump({k:(v[0],v[1]) for k,v in D.items()},open(SC+'/re/meta.json','w'),ensure_ascii=False)
print(list(D))
