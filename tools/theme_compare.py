"""Render the home page (A) in the current theme and three alternative themes for side-by-side review.

Usage: python tools/theme_compare.py   ->   docs/themes/封面主題比較.html

Every theme shows the same copy, links and photos as pages/A_home.py; only the visual system changes.
The alternatives obey the same CMS rules as the real build: inline style, Bootstrap 5.0.2 classes,
FontAwesome 4.7 and <img> only; no <style>, <svg>, <script>, web fonts or collapsible blocks.
"""

import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402
import components  # noqa: E402
from links import L  # noqa: E402
from tokens import contrast, FONT  # noqa: E402

OUT = ROOT / "docs" / "themes" / "封面主題比較.html"
TODAY = datetime.date.today().isoformat()

components.DRAFT_MARKS = False
components.UPDATED = TODAY
components.SITE_UNIT = "college"
components.SITE_LANG = "zh"
from pages import A_home  # noqa: E402

SITE_FILES = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192"
IMG = {
    "dean": (A_home.DEAN_PHOTO, "護理學院院長曾雯琦"),
    "emblem": (f"{SITE_FILES}/contents/100010/%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2LOGO.png",
               "護理學院院徽：圓形徽章，中央為紅、紫、白三朵鬱金香，下方標示 1947"),
    "capping": (f"{SITE_FILES}/menu/100180/slider/LINE_ALBUM_1140317N76%E5%8A%A0%E5%86%A0_250706_9.jpg",
                "加冠典禮：穿白色護理服、戴護士帽的學生與師長大合照"),
    "camp": (f"{SITE_FILES}/menu/100010/slider/DSC_8149.jpg", "穿迷彩服的營隊學員與工作人員在室內大廳合影"),
    "trauma": (f"{SITE_FILES}/menu/100181/slider/67455379-4742-4728-8242-D72E16011238.jpg",
               "戰傷災難護理指導員培訓學員穿著迷彩服，手持培訓布條合影"),
}

# The home page's copy, as it reads in the final build.
K = {
    "statement": ("在這裡，", "護理師也是軍官。"),
    "sub": "我們培育能在醫院照護病人、也能在戰傷與災難現場執行任務的軍護人才。從學士到研究所，學習在三軍總醫院的臨床現場發生。",
    "primary": ("招生專區", L("F")),
    "secondary": ("認識本院", L("C")),
    "audiences": [
        ("我想報考", L("F"), "學制與報名", "pencil-square-o"),
        ("我是家長", L("F-1"), "公費與服役", "users"),
        ("在校生", L("dept:J"), "表單與獎學金", "graduation-cap"),
        ("教職員", L("H"), "送審與場地借用", "briefcase"),
        ("English", L("J"), "英文網站", "globe"),
    ],
    "dean": ("曾雯琦", "院長　特聘教授", [("院長的話", L("C-1")), ("學院簡介", L("C-2"))]),
    "units": [
        ("dept", "護理學系", "學士班・臨床與軍陣實習", L("D-1"), "user-md"),
        ("inst", "護理研究所", "碩士班・博士班・研究", L("D-2"), "flask"),
    ],
    "lead": ("軍陣護理", "軍陣護理是本院獨有的核心：在野戰、艦艇、航空與災區等特殊環境中維持照護品質，課程結合軍事訓練與臨床實習。",
             L("dept:F-2-3"), "看護理學系的軍陣實習"),
    "features": [
        ("戰傷與災難護理", "以戰傷救護與大量傷患應變為研究與教學重點，連結模擬教學與實地演練。", L("E-2"), "戰", "看戰傷與災難護理研究", "ambulance"),
        ("國際交流", "與國外護理院校互訪、學生短期交流與學者來訪。", L("G"), "際", "更多國際交流", "globe"),
        ("研究能量", "教師研究計畫與代表成果，由研究所研究成果頁完整呈現。", L("inst:F"), "研", "看研究所研究成果", "line-chart"),
    ],
    "news": [
        ("院務公告", "影響全院或跨系所的行政事項", L("B-1")),
        ("招生訊息", "各學制招生消息與時程", L("B-3")),
        ("學術活動", "講座、研討會", L("B-2")),
        ("榮譽榜", "師生獲獎與成果", L("B-4")),
        ("徵才訊息", "教師與行政人員徵聘", L("B-5")),
    ],
    "all_news": ("所有消息", L("B")),
}


def fa(name, style=""):
    """FontAwesome 4 icon; a styled icon is wrapped in a span so the CMS's <i> -> <em> rewrite stays exact."""
    icon = f'<i class="fa fa-{name}" aria-hidden="true"></i>'
    return f'<span style="{style}">{icon}</span>' if style else icon


def img(key, style):
    src, alt = IMG[key]
    return f'<img src="{src}" alt="{alt}" style="{style}">'


def stamp(color, rule, link_color):
    return (f'<p style="margin:64px 0 0;padding-top:16px;border-top:1px solid {rule};font-size:13.5px;line-height:1.7;color:{color};">'
            f'{fa("calendar-check-o")}&nbsp;最後更新 {TODAY}　｜　維護單位：護理學院　'
            f'<a href="#page-top" style="color:{link_color};font-weight:700;text-decoration:underline;text-underline-offset:4px;">回到頁首&nbsp;{fa("angle-up")}</a></p>')


# ---------------------------------------------------------------- A 典雅學院
def theme_a():
    navy, ink, soft, rule, gold, gold_t, mist = "#17375E", "#23272E", "#5A6270", "#D5DBE3", "#A38449", "#755A26", "#F4F6F9"
    unit_c = {"dept": "#7A3644", "inst": "#2F5D80"}
    serif = "'Noto Serif TC','Source Han Serif TC','Songti TC','PMingLiU',serif"

    def link(label, href, color=navy):
        return (f'<a href="{href}" style="display:inline-block;padding:10px 0;color:{color};font-weight:700;'
                f'text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1px;">{label}&nbsp;{fa("angle-right")}</a>')

    def head(text):
        return (f'<div style="margin:64px 0 24px;border-bottom:1px solid {rule};"><h3 style="display:inline-block;margin:0 0 -1px;'
                f'padding-bottom:10px;border-bottom:2px solid {gold};font-family:{serif};font-size:26px;line-height:1.3;'
                f'font-weight:700;letter-spacing:.08em;color:{navy};">{text}</h3></div>')

    s1, s2 = K["statement"]
    opening = f'''<div class="row g-4 align-items-center">
<div class="col-md-8">
<p style="margin:0 0 14px;font-size:13px;letter-spacing:.14em;color:{gold_t};font-weight:700;">國防醫學大學　護理學院　<span style="display:inline-block;">COLLEGE OF NURSING</span></p>
<h2 style="margin:0;font-family:{serif};font-size:clamp(30px,6.4vw,40px);line-height:1.35;font-weight:700;color:{navy};letter-spacing:.04em;">{s1}<br>{s2}</h2>
<div style="width:56px;height:2px;background:{gold};margin:20px 0;"></div>
<p style="margin:0;max-width:32em;font-size:17px;line-height:1.9;">{K["sub"]}</p>
<div class="d-flex flex-wrap align-items-center" style="gap:8px 28px;margin-top:28px;">
<a href="{K["primary"][1]}" style="display:inline-flex;align-items:center;gap:10px;height:48px;padding:0 24px;background:{navy};color:#fff;font-weight:700;letter-spacing:.1em;text-decoration:none;">{K["primary"][0]}&nbsp;{fa("long-arrow-right")}</a>
{link(*K["secondary"])}
</div>
</div>
<div class="col-md-4 d-none d-md-block text-center">
<div style="display:inline-block;padding:10px;border:1px solid {gold};border-radius:50%;background:#fff;">{img("emblem", "display:block;width:190px;height:190px;border-radius:50%;object-fit:contain;")}</div>
<p style="margin:12px 0 0;font-size:13px;color:{soft};letter-spacing:.12em;">護理學院院徽</p>
</div>
</div>'''

    quick = (f'<div style="margin-top:48px;border-top:2px solid {navy};"><p style="margin:12px 0 0;font-size:13px;letter-spacing:.14em;color:{soft};">依身分查看</p>'
             '<div class="d-flex flex-wrap" style="gap:0 18px;">' + "".join(
                 f'<a href="{href}" style="flex:1 1 100px;display:block;padding:12px 0;border-bottom:1px solid {rule};text-decoration:none;">'
                 f'<span style="display:block;font-family:{serif};font-size:18px;font-weight:700;color:{navy};">{label}&nbsp;{fa("angle-right")}</span>'
                 f'<span style="display:block;font-size:13.5px;color:{soft};">{sub}</span></a>'
                 for label, href, sub, _ in K["audiences"]) + '</div></div>')

    name, title, links = K["dean"]
    dean = f'''{head("院長與學院")}
<div class="row g-4 align-items-start">
<div class="col-4 col-md-3">{img("dean", f"display:block;width:100%;aspect-ratio:3/4;object-fit:cover;padding:6px;border:1px solid {rule};background:#fff;")}</div>
<div class="col-8 col-md-9">
<p style="margin:0;font-family:{serif};font-size:23px;font-weight:700;color:{navy};letter-spacing:.06em;">{name}</p>
<p style="margin:2px 0 0;font-size:15px;color:{soft};">{title}</p>
<div class="d-flex flex-wrap" style="gap:0 24px;margin-top:8px;">{"".join(link(l, h) for l, h in links)}</div>
</div>
</div>'''

    units = head("學術單位") + '<div class="row g-4">' + "".join(
        f'<div class="col-md-6"><a href="{href}" style="display:block;height:100%;padding:24px 24px 20px;border:1px solid {rule};border-top:4px solid {unit_c[u]};background:#fff;text-decoration:none;">'
        f'<span style="display:block;font-family:{serif};font-size:23px;font-weight:700;color:{navy};letter-spacing:.06em;">{nm}</span>'
        f'<span style="display:block;margin-top:4px;font-size:15px;color:{soft};">{sub}</span>'
        f'<span style="display:inline-block;margin-top:18px;font-weight:700;color:{unit_c[u]};border-bottom:1px solid {unit_c[u]};">進入{nm}&nbsp;{fa("long-arrow-right")}</span></a></div>'
        for u, nm, sub, href, _ in K["units"]) + '</div>'

    lt, ltext, lhref, llabel = K["lead"]
    features = (head("學院特色")
                + f'<div style="padding:28px 28px 16px;background:{mist};border-left:3px solid {gold};">'
                  f'<h4 style="margin:0;font-family:{serif};font-size:24px;font-weight:700;color:{navy};letter-spacing:.06em;">{lt}</h4>'
                  f'<p style="margin:10px 0 0;max-width:36em;">{ltext}</p>{link(llabel, lhref)}</div>'
                + '<div class="row g-4" style="margin-top:4px;">' + "".join(
                    f'<div class="col-md-4"><div style="height:100%;padding-top:16px;border-top:1px solid {rule};">'
                    f'<h4 style="margin:0;font-family:{serif};font-size:19px;font-weight:700;color:{navy};">{t}</h4>'
                    f'<p style="margin:8px 0 0;font-size:15px;line-height:1.8;">{tx}</p>{link(lab, h)}</div></div>'
                    for t, tx, h, _, lab, _ in K["features"]) + '</div>')

    def news_item(t, d, h):
        return (f'<a href="{h}" style="display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px 0;border-bottom:1px solid {rule};text-decoration:none;">'
                f'<span><span style="display:block;font-weight:700;color:{navy};">{t}</span><span style="display:block;font-size:13.5px;color:{soft};">{d}</span></span>'
                f'{fa("angle-right", f"color:{gold_t};font-size:18px;")}</a>')
    news = (head("最新消息") + '<div class="row" style="--bs-gutter-x:32px;">'
            f'<div class="col-md-6">{"".join(news_item(*n) for n in K["news"][:3])}</div>'
            f'<div class="col-md-6">{"".join(news_item(*n) for n in K["news"][3:])}</div></div>'
            + link(*K["all_news"]))

    body = "\n".join([opening, quick, dean, units, features, news, stamp(soft, rule, navy)])
    pairs = [(navy, "#FFFFFF"), (ink, "#FFFFFF"), (soft, "#FFFFFF"), (gold_t, "#FFFFFF"), ("#FFFFFF", navy),
             (navy, mist), (ink, mist), (unit_c["dept"], "#FFFFFF"), (unit_c["inst"], "#FFFFFF")]
    return (f'<div id="page-top" class="p-3 p-md-4" style="background:#fff;font-family:{FONT};color:{ink};font-size:16.5px;line-height:1.85;">\n{body}\n</div>', pairs)


# ---------------------------------------------------------------- B 臨床現代
def theme_b():
    teal, teal_d, mint, ink, soft, rule, wash, amber = "#0E6B6B", "#0B4F50", "#DDF0EC", "#1F2A2E", "#56656A", "#E1E8EA", "#F3F7F7", "#E3A23B"
    tint = {"dept": ("#FBEFEA", "#A2452F"), "inst": ("#EAF0F8", "#2D5B95")}
    shadow = "0 6px 22px rgba(15,60,60,.09)"

    def link(label, href, color=teal_d):
        return (f'<a href="{href}" style="display:inline-flex;align-items:center;gap:6px;padding:10px 0;color:{color};font-weight:800;text-decoration:none;'
                f'border-bottom:2px solid {mint};">{label}&nbsp;{fa("arrow-right")}</a>')

    def pill(label, href, solid):
        s = (f"background:{teal};color:#fff;border:2px solid {teal};" if solid
             else f"background:#fff;color:{teal_d};border:2px solid {teal};")
        return (f'<a href="{href}" style="display:inline-flex;align-items:center;gap:8px;height:48px;padding:0 24px;border-radius:999px;'
                f'{s}font-weight:800;text-decoration:none;">{label}{"&nbsp;" + fa("arrow-right") if solid else ""}</a>')

    def head(text):
        return (f'<div style="margin:64px 0 20px;"><span style="display:block;width:36px;height:4px;border-radius:2px;background:{amber};margin-bottom:12px;"></span>'
                f'<h3 style="margin:0;font-size:26px;line-height:1.3;font-weight:900;color:{ink};">{text}</h3></div>')

    s1, s2 = K["statement"]
    opening = f'''<div class="row g-4 align-items-center">
<div class="col-md-6">
<span style="display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:999px;background:{mint};color:{teal_d};font-size:14px;font-weight:800;">{fa("plus-square")}國防醫學大學　護理學院</span>
<h2 style="margin:16px 0 0;font-size:clamp(30px,6.6vw,40px);line-height:1.3;font-weight:900;color:{teal_d};">{s1}<br>{s2}</h2>
<p style="margin:16px 0 0;font-size:17px;line-height:1.85;">{K["sub"]}</p>
<div class="d-flex flex-wrap align-items-center" style="gap:12px;margin-top:24px;">{pill(*K["primary"], True)}{pill(*K["secondary"], False)}</div>
</div>
<div class="col-md-6">{img("capping", f"display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:20px;box-shadow:{shadow};")}</div>
</div>'''

    quick = ('<div class="d-flex flex-wrap" style="gap:12px;margin-top:40px;">' + "".join(
        f'<a href="{href}" style="flex:1 1 92px;display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 6px 14px;'
        f'background:#fff;border:1px solid {rule};border-radius:16px;box-shadow:{shadow};text-decoration:none;text-align:center;">'
        f'<span style="width:44px;height:44px;border-radius:50%;background:{mint};color:{teal};display:flex;align-items:center;justify-content:center;font-size:19px;">{fa(ic)}</span>'
        f'<span style="display:block;font-weight:800;color:{ink};line-height:1.3;">{label}</span>'
        f'<span style="display:block;font-size:13px;line-height:1.4;color:{soft};">{sub}</span></a>'
        for label, href, sub, ic in K["audiences"]) + '</div>')

    name, title, links = K["dean"]
    dean = (head("院長與學院")
            + f'<div style="display:flex;flex-wrap:wrap;align-items:center;gap:20px;padding:20px;background:{wash};border-radius:18px;">'
            + img("dean", "flex:none;width:112px;height:112px;border-radius:50%;object-fit:cover;object-position:top;")
            + f'<div style="flex:1 1 220px;"><p style="margin:0;font-size:21px;font-weight:900;color:{ink};">{name}</p>'
              f'<p style="margin:0;font-size:15px;color:{soft};">{title}</p><div class="d-flex flex-wrap" style="gap:8px;margin-top:12px;">'
            + "".join(f'<a href="{h}" style="display:inline-flex;align-items:center;gap:6px;padding:7px 16px;border-radius:999px;background:#fff;'
                      f'border:1px solid {rule};color:{teal_d};font-weight:800;text-decoration:none;">{l}&nbsp;{fa("angle-right")}</a>' for l, h in links)
            + '</div></div></div>')

    units = head("學術單位") + '<div class="row g-3">' + "".join(
        f'<div class="col-md-6"><a href="{href}" style="display:block;height:100%;padding:24px;border-radius:18px;background:{tint[u][0]};text-decoration:none;">'
        f'<span style="display:inline-flex;width:48px;height:48px;border-radius:14px;background:#fff;color:{tint[u][1]};align-items:center;justify-content:center;font-size:22px;">{fa(ic)}</span>'
        f'<span style="display:block;margin-top:14px;font-size:22px;font-weight:900;color:{ink};">{nm}</span>'
        f'<span style="display:block;margin-top:2px;font-size:15px;color:{soft};">{sub}</span>'
        f'<span style="display:inline-flex;align-items:center;gap:8px;margin-top:16px;font-weight:800;color:{tint[u][1]};">進入{nm}&nbsp;{fa("arrow-right")}</span></a></div>'
        for u, nm, sub, href, ic in K["units"]) + '</div>'

    lt, ltext, lhref, llabel = K["lead"]
    features = (head("學院特色")
                + f'<div class="row g-0" style="background:#fff;border:1px solid {rule};border-radius:18px;overflow:hidden;box-shadow:{shadow};">'
                + '<div class="col-md-5">' + img("trauma", "display:block;width:100%;height:100%;min-height:220px;object-fit:cover;") + '</div>'
                + f'<div class="col-md-7" style="padding:24px 26px 18px;"><h4 style="margin:0;font-size:23px;font-weight:900;color:{teal_d};">{lt}</h4>'
                  f'<p style="margin:10px 0 0;">{ltext}</p>{link(llabel, lhref)}</div></div>'
                + '<div class="row g-3" style="margin-top:4px;">' + "".join(
                    f'<div class="col-md-4"><div style="height:100%;padding:20px 20px 14px;background:#fff;border:1px solid {rule};border-radius:18px;">'
                    f'<span style="display:inline-flex;width:40px;height:40px;border-radius:50%;background:{mint};color:{teal};align-items:center;justify-content:center;font-size:18px;">{fa(ic)}</span>'
                    f'<h4 style="margin:12px 0 0;font-size:18px;font-weight:900;color:{ink};">{t}</h4>'
                    f'<p style="margin:6px 0 0;font-size:15px;line-height:1.75;color:{soft};">{tx}</p>{link(lab, h)}</div></div>'
                    for t, tx, h, _, lab, ic in K["features"]) + '</div>')

    news = (head("最新消息") + f'<div style="background:#fff;border:1px solid {rule};border-radius:18px;overflow:hidden;">' + "".join(
        f'<a href="{h}" style="display:flex;align-items:center;justify-content:space-between;gap:12px;padding:15px 20px;'
        f'{"" if i == 0 else f"border-top:1px solid {rule};"}text-decoration:none;">'
        f'<span><span style="display:block;font-weight:800;color:{ink};">{t}</span><span style="display:block;font-size:13.5px;color:{soft};">{d}</span></span>'
        f'{fa("chevron-right", f"color:{teal};")}</a>' for i, (t, d, h) in enumerate(K["news"])) + '</div>'
        + f'<div style="margin-top:16px;">{pill(*K["all_news"], False)}</div>')

    body = "\n".join([opening, quick, dean, units, features, news, stamp(soft, rule, teal_d)])
    pairs = [(teal_d, "#FFFFFF"), (ink, "#FFFFFF"), (soft, "#FFFFFF"), ("#FFFFFF", teal), (teal_d, mint), (ink, wash), (soft, wash),
             (soft, tint["dept"][0]), (tint["dept"][1], tint["dept"][0]), (soft, tint["inst"][0]), (tint["inst"][1], tint["inst"][0])]
    return (f'<div id="page-top" class="p-3 p-md-4" style="background:#fff;font-family:{FONT};color:{ink};font-size:16.5px;line-height:1.85;">\n{body}\n</div>', pairs)


# ---------------------------------------------------------------- C 軍護榮譽
def theme_c():
    olive_d, olive, khaki, khaki_p, cream = "#1E2A21", "#34452F", "#C9B98C", "#EEE8D6", "#F7F5EE"
    crimson, brass, ink, soft, rule = "#8E2A2A", "#A8842F", "#1E221F", "#525A51", "#D9D2BE"
    unit_bg = {"dept": olive, "inst": "#23344A"}

    def link(label, href, color=crimson):
        return (f'<a href="{href}" style="display:inline-block;padding:10px 0;color:{color};font-weight:800;letter-spacing:.04em;'
                f'text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:2px;">{label}&nbsp;{fa("angle-right")}</a>')

    def head(text):
        stripes = "".join(f'<span style="display:block;width:22px;height:4px;background:{crimson};"></span>' for _ in range(3))
        return (f'<div style="display:flex;align-items:center;gap:14px;margin:64px 0 24px;">'
                f'<span style="flex:none;display:flex;flex-direction:column;gap:3px;">{stripes}</span>'
                f'<h3 style="margin:0;font-size:24px;line-height:1.3;font-weight:900;letter-spacing:.14em;color:{ink};white-space:nowrap;">{text}</h3>'
                f'<span style="flex:1 1 auto;border-top:1px solid {brass};"></span></div>')

    def ribbon(a, b):
        return f'<span style="display:block;width:44px;height:12px;background:linear-gradient(90deg,{a} 0 30%,{b} 30% 70%,{a} 70%);"></span>'

    s1, s2 = K["statement"]
    opening = f'''<div style="background:{olive_d};padding:32px 24px;border-bottom:4px solid {brass};">
<div class="row g-4 align-items-center">
<div class="col-md-7">
<p style="margin:0;font-size:13px;letter-spacing:.3em;color:{khaki};font-weight:700;">國防醫學大學　護理學院</p>
<div style="display:flex;gap:4px;margin:16px 0;">{ribbon(crimson, khaki)}{ribbon(olive, khaki)}{ribbon(khaki, crimson)}</div>
<h2 style="margin:0;font-size:clamp(30px,6.8vw,42px);line-height:1.3;font-weight:900;color:#fff;letter-spacing:.04em;">{s1}<br>{s2}</h2>
<p style="margin:16px 0 0;font-size:17px;line-height:1.85;color:{khaki_p};">{K["sub"]}</p>
<div class="d-flex flex-wrap align-items-center" style="gap:12px 24px;margin-top:24px;">
<a href="{K["primary"][1]}" style="display:inline-flex;align-items:center;gap:10px;height:48px;padding:0 24px;background:{crimson};color:#fff;font-weight:800;letter-spacing:.12em;text-decoration:none;outline:1px solid {khaki};outline-offset:-5px;">{K["primary"][0]}&nbsp;{fa("long-arrow-right")}</a>
{link(*K["secondary"], color=khaki)}
</div>
</div>
<div class="col-md-5">{img("camp", f"display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border:3px solid {brass};")}</div>
</div>
</div>'''

    quick = ('<div class="d-flex flex-wrap" style="gap:8px;margin-top:24px;">' + "".join(
        f'<a href="{href}" style="flex:1 1 120px;display:block;padding:12px 14px;background:{khaki_p};border-left:6px solid {olive};text-decoration:none;">'
        f'<span style="display:block;font-weight:900;color:{ink};letter-spacing:.08em;">{label}</span>'
        f'<span style="display:block;font-size:13px;color:{soft};">{sub}</span></a>'
        for label, href, sub, _ in K["audiences"]) + '</div>')

    name, title, links = K["dean"]
    dean = f'''{head("院長與學院")}
<div class="row g-4 align-items-center">
<div class="col-4 col-md-3">{img("dean", f"display:block;width:100%;aspect-ratio:3/4;object-fit:cover;border:4px solid {olive};")}</div>
<div class="col-8 col-md-9">
<p style="margin:0;font-size:23px;font-weight:900;color:{ink};letter-spacing:.1em;">{name}</p>
<p style="margin:2px 0 0;font-size:15px;color:{soft};">{title}</p>
<div class="d-flex flex-wrap" style="gap:0 24px;margin-top:8px;">{"".join(link(l, h) for l, h in links)}</div>
</div>
</div>'''

    units = head("學術單位") + '<div class="row g-3">' + "".join(
        f'<div class="col-md-6"><a href="{href}" style="display:block;height:100%;padding:26px 26px 22px;background:{unit_bg[u]};text-decoration:none;'
        f'outline:1px solid {khaki};outline-offset:-8px;">'
        f'<span style="display:block;font-size:24px;font-weight:900;letter-spacing:.14em;color:#fff;">{nm}</span>'
        f'<span style="display:block;margin-top:4px;font-size:15px;color:{khaki_p};">{sub}</span>'
        f'<span style="display:inline-flex;align-items:center;gap:8px;margin-top:18px;font-weight:800;color:{khaki};">進入{nm}&nbsp;{fa("long-arrow-right")}</span></a></div>'
        for u, nm, sub, href, _ in K["units"]) + '</div>'

    lt, ltext, lhref, llabel = K["lead"]
    features = (head("學院特色")
                + f'<div class="row g-0" style="background:{olive_d};">'
                + '<div class="col-md-5">' + img("trauma", "display:block;width:100%;height:100%;min-height:220px;object-fit:cover;") + '</div>'
                + f'<div class="col-md-7" style="padding:26px 26px 16px;"><h4 style="margin:0;font-size:24px;font-weight:900;letter-spacing:.14em;color:#fff;">{lt}</h4>'
                  f'<p style="margin:10px 0 0;color:{khaki_p};">{ltext}</p>{link(llabel, lhref, color=khaki)}</div></div>'
                + '<div class="row g-4" style="margin-top:4px;">' + "".join(
                    f'<div class="col-md-4"><span style="display:inline-flex;width:46px;height:46px;align-items:center;justify-content:center;'
                    f'border:2px solid {crimson};color:{crimson};font-size:22px;font-weight:900;">{g}</span>'
                    f'<h4 style="margin:12px 0 0;font-size:19px;font-weight:900;color:{ink};letter-spacing:.06em;">{t}</h4>'
                    f'<p style="margin:6px 0 0;font-size:15px;line-height:1.8;">{tx}</p>{link(lab, h)}</div>'
                    for t, tx, h, g, lab, _ in K["features"]) + '</div>')

    news = (head("最新消息") + f'<div style="border-top:3px solid {olive};">' + "".join(
        f'<a href="{h}" style="display:flex;align-items:center;gap:14px;padding:14px 4px;border-bottom:1px solid {rule};text-decoration:none;">'
        f'<span style="flex:none;width:8px;height:8px;background:{brass};"></span>'
        f'<span style="flex:1 1 auto;"><span style="display:block;font-weight:900;color:{ink};letter-spacing:.06em;">{t}</span>'
        f'<span style="display:block;font-size:13.5px;color:{soft};">{d}</span></span>{fa("angle-right", f"color:{olive};font-size:18px;")}</a>'
        for t, d, h in K["news"]) + '</div>' + link(*K["all_news"]))

    body = "\n".join([opening, quick, dean, units, features, news, stamp(soft, rule, crimson)])
    pairs = [("#FFFFFF", olive_d), (khaki, olive_d), (khaki_p, olive_d), ("#FFFFFF", crimson), (ink, cream), (soft, cream),
             (crimson, cream), (ink, khaki_p), (soft, khaki_p), ("#FFFFFF", olive), (khaki_p, olive), (khaki, olive),
             ("#FFFFFF", unit_bg["inst"]), (khaki, unit_bg["inst"]), (khaki_p, unit_bg["inst"])]
    return (f'<div id="page-top" class="p-3 p-md-4" style="background:{cream};font-family:{FONT};color:{ink};font-size:16.5px;line-height:1.85;">\n{body}\n</div>', pairs)


# ---------------------------------------------------------------- comparison page
THEMES = [
    {"key": "current", "tag": "現行", "name": "制服臂章",
     "concept": "把軍護制服的名條、臂章和緞帶，縫在莫蘭迪色的斜紋布上。",
     "swatches": ["#EDE7DE", "#33493F", "#A4B6AB", "#D9B8B3", "#B9C6CC", "#8A4F4F"],
     "feel": "親切、有記憶點、帶點手作感", "fit": "吸引高中生，跟其他護理學校做出區隔", "risk": "可能被認為太可愛、不夠正式"},
    {"key": "a", "tag": "A", "name": "典雅學院",
     "concept": "白底、深藍配金線、明體標題，以院徽為中心，像大學的正式出版品。",
     "swatches": ["#FFFFFF", "#17375E", "#A38449", "#F4F6F9", "#7A3644", "#2F5D80"],
     "feel": "穩重、學術、正式", "fit": "院方與資深教師，對外正式場合",
     "risk": "和一般大學網站差異小，對高中生吸引力較弱；電腦沒有思源宋體時，標題會顯示成新細明體"},
    {"key": "b", "tag": "B", "name": "臨床現代",
     "concept": "白底、醫療青綠、圓角卡片和大照片，像新式醫學中心的網站。",
     "swatches": ["#FFFFFF", "#0E6B6B", "#DDF0EC", "#E3A23B", "#FBEFEA", "#EAF0F8"],
     "feel": "乾淨、親切、現代", "fit": "高中生和家長，尤其是用手機看的人",
     "risk": "最像一般醫護學校，軍護特色要靠照片和文字撐起來"},
    {"key": "c", "tag": "C", "name": "軍護榮譽",
     "concept": "墨綠、卡其、深紅與黃銅，用勳表色條和印章字，莊重地表現軍校身分。",
     "swatches": ["#1E2A21", "#34452F", "#C9B98C", "#EEE8D6", "#8E2A2A", "#A8842F"],
     "feel": "莊重、有紀律、有榮譽感", "fit": "強調軍護定位；家長看了比較安心",
     "risk": "軍事感最強，部分學生可能覺得有距離；深色區塊多，照片品質要夠好"},
]

FRAME = """<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<base target="_blank">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head><body style="margin:0;background:#f0f0f0;font-family:'Microsoft JhengHei',sans-serif;">
<div style="background:#0256a6;color:#fff;padding:14px 20px;font-size:14px;">國防醫學大學（校方外框模擬）</div>
<div class="container-lg" style="padding:24px 12px;"><div class="row">
<div class="col-lg-3 d-none d-lg-block"><div style="background:#fff;border-top:40px solid #0256a6;padding:12px;font-size:14px;color:#333;height:100%;min-height:300px;">左側樹狀選單（校方）</div></div>
<div class="col-lg-9 col-12"><div style="background:#fff;"><div style="background:#0256a6;color:#fff;padding:8px 14px;">&gt; 護理學院</div>
<div style="padding:30px 30px 0;" class="px-2 px-md-4"><div id="contenR" class="editor">
__BODY__
</div></div></div></div></div></div>
<script>
(function(){var key="__KEY__";function send(){parent.postMessage({themeFrame:key,h:document.body.scrollHeight},"*");}
window.addEventListener("load",send);Array.prototype.forEach.call(document.images,function(i){i.addEventListener("load",send);i.addEventListener("error",send);});
if(window.ResizeObserver){new ResizeObserver(send).observe(document.body);}send();})();
</script></body></html>"""


def main():
    current = build.cms_normalize(build.theme_bare_links(A_home.render()))
    bodies = {"current": current}
    problems = 0
    for key, fn in (("a", theme_a), ("b", theme_b), ("c", theme_c)):
        html, pairs = fn()
        html = build.cms_normalize(html)
        for pat in build.FORBIDDEN:
            if re.search(pat, html, re.I):
                print(f"FORBIDDEN {pat} in theme {key}")
                problems += 1
        for fg, bg in pairs:
            r = contrast(fg, bg)
            if r < 4.5:
                print(f"CONTRAST theme {key}: {fg} on {bg} = {r:.2f}")
                problems += 1
        bodies[key] = html
    docs = {k: FRAME.replace("__BODY__", v).replace("__KEY__", k) for k, v in bodies.items()}
    page = (ROOT / "tools" / "theme_compare.html").read_text(encoding="utf-8")
    page = page.replace("__THEMES__", json.dumps(THEMES, ensure_ascii=False)).replace("__DOCS__", json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")).replace("__DATE__", TODAY)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page) // 1024} KB); problems: {problems}")
    return problems


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
