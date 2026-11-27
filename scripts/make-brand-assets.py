"""
產生《字戰星河》網站圖示全套與社群分享預覽圖（2026-11-27）

用法（專案根目錄，先開本機伺服器）：
  python -m http.server 8796 -d .        （另一個視窗）
  python scripts/make-brand-assets.py
需要：pip install playwright pillow，並執行過 playwright install chromium

輸出（專案根目錄）：
  favicon.svg、favicon.ico（16/32/48）、apple-touch-icon.png（180，滿版）
  icon-192.png、icon-512.png、icon-192-maskable.png、icon-512-maskable.png
  og-image.jpg（1200×630，LINE／Facebook 分享卡片，含遊戲實際畫面與石門國小校徽）
素材：scripts/brand/school-logo.png（校徽正式檔四角去白底，不重畫）
"""
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
BRAND = ROOT / 'scripts' / 'brand'
LOCAL = 'http://127.0.0.1:8796/'

FONT = "'Noto Sans TC','Microsoft JhengHei','PingFang TC',sans-serif"


def icon_svg(full_bleed=False, scale=1.0):
    """深藍星空底＋金色星門環＋發光的「字」。"""
    rx = 0 if full_bleed else 14
    s = scale
    t = f'translate({32 - 32 * s} {32 - 32 * s}) scale({s})'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1a3f"/><stop offset="1" stop-color="#1e1b4b"/></linearGradient>
<radialGradient id="core" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fde047" stop-opacity="0.55"/><stop offset="1" stop-color="#6366f1" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="1.4" result="b"/><feFlood flood-color="#38bdf8"/><feComposite in2="b" operator="in"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="64" height="64" rx="{rx}" fill="url(#bg)"/>
<g transform="{t}">
<circle cx="13" cy="14" r="1.2" fill="#e2e8f0"/><circle cx="52" cy="11" r="0.9" fill="#e2e8f0"/><circle cx="54" cy="50" r="1.1" fill="#e2e8f0"/>
<circle cx="32" cy="32" r="25" fill="url(#core)"/>
<ellipse cx="32" cy="32" rx="25" ry="25" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="7 4.2"/>
<text x="32" y="33" text-anchor="middle" dominant-baseline="central" font-family="{FONT}" font-weight="900" font-size="32" fill="#f0f9ff" filter="url(#glow)">字</text>
</g></svg>'''


def render_png(page, svg, size, out):
    page.set_viewport_size({'width': size, 'height': size})
    page.set_content('<html><body style="margin:0;background:transparent">'
                     f'<div style="width:{size}px;height:{size}px">'
                     f'{svg.replace("<svg ", f"<svg width={size} height={size} ", 1)}</div></body></html>')
    page.wait_for_timeout(150)
    page.screenshot(path=str(out), omit_background=True, clip={'x': 0, 'y': 0, 'width': size, 'height': size})


OG_HTML = '''<html><head><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@500;700;900&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;height:630px;font-family:"Noto Sans TC";position:relative;overflow:hidden;color:#f8fafc;
 background:radial-gradient(circle at 80% 20%,rgba(99,102,241,.35) 0,transparent 45%),radial-gradient(circle at 10% 90%,rgba(56,189,248,.18) 0,transparent 40%),linear-gradient(150deg,#020617 0%,#0b1430 60%,#1e1b4b 100%)}
.stars i{position:absolute;width:3px;height:3px;border-radius:50%;background:#e2e8f0;opacity:.7}
.kicker{position:absolute;left:64px;top:62px;font-size:26px;font-weight:700;letter-spacing:6px;color:#7dd3fc}
h1{position:absolute;left:58px;top:104px;font-size:128px;font-weight:900;letter-spacing:10px;line-height:1.1;
 background:linear-gradient(120deg,#e0f2fe 10%,#7dd3fc 45%,#fde047 95%);-webkit-background-clip:text;background-clip:text;color:transparent;
 filter:drop-shadow(0 0 22px rgba(56,189,248,.45))}
.sub{position:absolute;left:64px;top:270px;font-size:32px;font-weight:700;color:#cbd5e1;line-height:1.5}
.sub b{color:#fde047}
.tags{position:absolute;left:62px;top:390px;display:flex;gap:12px}
.tag{border:3px solid #38bdf8;color:#e0f2fe;background:rgba(14,116,144,.25);border-radius:999px;padding:6px 20px;font-size:24px;font-weight:900}
.tag.y{border-color:#fbbf24;background:rgba(202,138,4,.2)}.tag.g{border-color:#34d399;background:rgba(6,95,70,.25)}
.shot{position:absolute;right:-60px;top:118px;width:600px;height:338px;border-radius:18px;overflow:hidden;border:4px solid #38bdf8;
 box-shadow:0 0 40px rgba(56,189,248,.35),0 24px 48px rgba(0,0,0,.6);transform:rotate(-3deg)}
.shot img{width:100%;height:100%;object-fit:cover}
.foot{position:absolute;left:0;right:0;bottom:0;height:86px;background:rgba(2,6,23,.85);border-top:3px solid #fbbf24;
 display:flex;align-items:center;gap:16px;padding:0 56px;font-size:26px;font-weight:900}
.logo{width:62px;height:62px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}
.logo img{width:56px;height:56px;object-fit:contain}
.foot small{display:block;font-size:19px;font-weight:700;color:#94a3b8}
.foot .url{margin-left:auto;font-weight:700;color:#7dd3fc;font-size:24px}
</style></head><body>
<div class="stars"><i style="left:120px;top:40px"></i><i style="left:520px;top:80px"></i><i style="left:700px;top:30px"></i><i style="left:980px;top:60px"></i><i style="left:600px;top:500px"></i><i style="left:430px;top:240px"></i></div>
<div class="kicker">全漢字橫向捲軸射擊遊戲</div>
<h1>字戰星河</h1>
<div class="sub">敵機、子彈、爆炸全都是<b>漢字</b><br>穿越八大星域，擊敗最終魔王「源」</div>
<div class="tags"><span class="tag">八大星域</span><span class="tag y">78 種漢字敵機</span><span class="tag g">免安裝即玩</span></div>
<div class="shot"><img src="game-shot.jpg"></div>
<div class="foot"><div class="logo"><img src="school-logo.png"></div><div>阿凱老師<small>桃園市龍潭區石門國民小學</small></div><span class="url">cagoooo.github.io/zizhan-xinghe</span></div>
</body></html>'''


def capture_game(browser):
    """開本機遊戲、按出擊、等開場結束後截戰場畫面。"""
    page = browser.new_page(viewport={'width': 1280, 'height': 900}, device_scale_factor=1.5)
    page.goto(LOCAL, wait_until='networkidle')
    page.wait_for_timeout(1200)
    page.click('#btn-start')
    page.wait_for_timeout(4600)          # 開場約 4 秒
    box = page.locator('#game-canvas').bounding_box()
    # 讓自機在中左方移動，畫面比較有戲
    for i in range(16):
        page.mouse.move(box['x'] + box['width'] * 0.22, box['y'] + box['height'] * (0.35 + 0.3 * (i % 2)))
        page.wait_for_timeout(260)
    page.locator('#game-canvas').screenshot(path=str(BRAND / 'game-shot.jpg'), type='jpeg', quality=90)
    page.close()


def main():
    (ROOT / 'favicon.svg').write_text(icon_svg(), encoding='utf-8')
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        for s in (16, 32, 48):
            render_png(page, icon_svg(), s, BRAND / f'_f{s}.png')
        render_png(page, icon_svg(full_bleed=True), 180, ROOT / 'apple-touch-icon.png')
        for s in (192, 512):
            render_png(page, icon_svg(), s, ROOT / f'icon-{s}.png')
            render_png(page, icon_svg(full_bleed=True, scale=0.72), s, ROOT / f'icon-{s}-maskable.png')
        capture_game(b)
        og_file = BRAND / '_og.html'
        og_file.write_text(OG_HTML, encoding='utf-8')
        og = b.new_page(viewport={'width': 1200, 'height': 630})
        og.goto(og_file.as_uri(), wait_until='networkidle')
        og.evaluate('document.fonts.ready')
        og.wait_for_timeout(800)
        og.screenshot(path=str(BRAND / '_og.png'))
        og_file.unlink()
        b.close()
    imgs = [Image.open(BRAND / f'_f{s}.png').convert('RGBA') for s in (16, 32, 48)]
    imgs[2].save(ROOT / 'favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)], append_images=imgs[:2])
    Image.open(BRAND / '_og.png').convert('RGB').save(ROOT / 'og-image.jpg', quality=88, optimize=True)
    for f in BRAND.glob('_*.png'):
        f.unlink()
    for f in ['favicon.svg', 'favicon.ico', 'apple-touch-icon.png', 'icon-512.png', 'og-image.jpg']:
        print(f, (ROOT / f).stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
