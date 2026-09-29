from components import (page, name_tape, statement, p, bullets, tape_surface, text_link, actions, draft, note)
from links import L
from tokens import C, S, TYPE, SITE

META = {"id": "C-2-2", "slug": "goals", "title": "教育目標與核心能力", "owner": "課委會", "site": "dept"}

# 原文來源（2026-09-29 擷取），逐字照錄、只改版面：
#   教育宗旨與目標  https://wwwndmc.ndmutsgh.edu.tw/unit/100010/1471
#     現行頁面內容是兩張圖（學士班教育目標、碩士班教育目標，皆標「114.02.10修訂」），本頁把學士班那張圖的文字轉為網頁文字。
#   學士班課程地圖  https://wwwndmc.ndmutsgh.edu.tw/unit/100010/3642（教育宗旨、學生核心能力、核心能力與課程關聯圖）
U_GOALS = SITE + "/unit/100010/1471"
U_MAP = SITE + "/unit/100010/3642"
U_MATRIX = SITE + "/files/web/192/file_up/100010/8644/@學士班核心能力與課程關聯圖1101012.pdf"

AIM = "培育兼具人文素養與護理專業能力，符合軍民健康照顧系統所需之專業人才。"

GOALS = [
    "能具有人文關懷與尊重生命的素養",
    "能具備醫護專業知識及國際視野",
    "能提供安全有品質的護理照護",
    "能以臨床推理解決服務對象的健康需求與問題",
    "能應用倫理與法律思維提供適切的護理",
    "能與服務對象及跨領域團隊成員溝通合作",
    "能扮演克盡職責、勝任使命的軍護專業角色",
    "能終生學習與自我成長",
]

ABILITIES = ["人文關懷", "尊重生命", "生物醫學知識", "國際視野", "護理技能", "批判性思考", "實證護理",
             "倫理思維", "溝通合作", "領導統御", "克盡職責", "軍陣護理", "終生學習"]


def tape_row(words):
    """Built inline (no component for it): short name-tape labels sewn in a wrapping row, one per core ability.
    Widths follow the words, so the row reads as a set of tapes, not a grid of equal cards."""
    lis = "".join(
        f'<li style="margin:0;padding:9px 14px 8px;background:{C["tape"]};color:{C["thread"]};font-weight:800;'
        f'font-size:16px;line-height:1.3;letter-spacing:.08em;border:1px solid {C["rule"]};border-radius:2px;'
        f'outline:1px dashed rgba(51,73,63,.35);outline-offset:-4px;">{w}</li>'
        for w in words
    )
    return (f'<ul style="list-style:none;display:flex;flex-wrap:wrap;gap:{S[1]} 10px;margin:0 0 {S[3]};padding:0;'
            f'max-width:44em;">{lis}</ul>')


def source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = statement(
        draft("讀完四年，你會成為什麼樣的護理人員？"),
        draft("學系把答案寫成一句宗旨、八項教育目標和十三項核心能力。課程與實習，都是照著這些目標安排的。"),
    )

    aim = tape_surface(p(f'<strong style="color:{C["thread"]};{TYPE["h3"]}">{AIM}</strong>'))

    goals = "".join([
        p(draft("畢業時，我們希望每一位學生都能做到下面八件事。")),
        bullets(GOALS),
        source("學士班教育目標，114.02.10 修訂。", U_GOALS, "現行「教育宗旨與目標」頁"),
    ])

    abilities = "".join([
        p(draft("這十三項能力，是四年課程要練出來的本事。每一門課都標了它負責培養哪幾項。")),
        tape_row(ABILITIES),
        source("學生核心能力摘自學士班課程地圖頁。", U_MAP, "現行「學士班課程地圖」頁"),
        actions(text_link("核心能力與課程關聯圖（PDF）", U_MATRIX), text_link("課程地圖", L("dept:F-1-3"))),
    ])

    return page(
        opening,
        note("本頁沿用現行「教育宗旨與目標」（unit/100010/1471）與「學士班課程地圖」（unit/100010/3642）的文字，逐字照錄、只重新排版；"
             "現行 1471 頁的目標是兩張圖片，改成網頁文字後手機可放大、讀屏軟體也讀得到。"
             "請課委會確認：① 目標是否仍為 114.02.10 修訂版；② 核心能力與課程關聯圖（1101012 版）是否有新版；"
             "③ 碩士班教育目標改放護理研究所網站，學系頁不再列出。"),
        name_tape("教育宗旨"),
        aim,
        name_tape("學士班教育目標"),
        goals,
        name_tape("學生核心能力"),
        abilities,
        name_tape("碩士班"),
        p(draft("碩士班的教育目標，請看護理研究所的介紹。")),
        actions(text_link("護理研究所簡介", L("inst:C-2"))),
        owner=META["owner"],
    )
