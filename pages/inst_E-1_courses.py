from urllib.parse import quote

from components import (page, name_tape, statement, p, h4, text_link, actions, facts, illo_slot, draft, note)
from links import L
from tokens import SITE

META = {"id": "E-1", "slug": "courses", "title": "課程資訊", "owner": "院窗口", "site": "inst"}

# 現行研究所網站沒有課程清單頁；以下課程相關規定原文照錄自研究所「學生專區」：
U_RULES = SITE + "/unit/100181/6533"
U_HANDBOOK = SITE + quote("/files/web/192/file_up/100181/13936/國防醫學大學護理研究所碩士研究生手冊_09182025_公告.pdf")
U_SAS = "https://sas.ndmctsgh.edu.tw/IASS/Logout.aspx"  # 校務資訊系統（研究所網站頁尾「線上系統」）


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = statement(
        draft("碩士班要修哪些課，從這一頁開始看。"),
        draft("課程依入學學年度與學組而不同。每個人都要修的課列在前面，各學組的課程清單正在整理。"),
    )

    common = "".join([
        facts([
            ("研究倫理教育",
             "研究所新生第一學年必修「9990160研究倫理教育Research Ethics Education」課程，此課為0學分"),
            ("生物統計學", "（113學年前入學者）含選修科目內至少選修一門生物統計學3學分，2擇1"),
            ("進階專科護理學實習(三)", "專科護理師組有考照需求者須選修進階專科護理學實習(三)才能畢業"),
        ]),
        p("碩士班修課內容與修業規定依據研究生入學當年的教育計劃實施"),
        _source("以上摘自護理研究所〈學生專區〉的「入學資格與修業規定」。", U_RULES, "現行網站：研究所學生專區"),
    ])

    master = "".join([
        h4("課程地圖"),
        illo_slot("碩士班課程地圖（研究生手冊 圖2-1-2，沿用原圖）", "4/3", unit="inst"),
        h4("各學組課程"),
        facts([
            ("成人暨老人護理學組", draft("必修與選修課程清單待補")),
            ("婦兒護理學組", draft("必修與選修課程清單待補")),
            ("精神衛生護理組", draft("必修與選修課程清單待補")),
            ("專科護理師組", draft("必修與選修課程清單待補")),
        ]),
        note("現行研究所網站沒有課程清單，課程地圖只在研究生手冊（圖2-1-2）。請院窗口提供各學組的"
             "課程名稱、學分、必選修與開課學期，並分「113學年前入學」與「114學年後入學」兩版；"
             "課程地圖請提供原圖檔。收到前請勿依印象補課名。"),
    ])

    doctoral = "".join([
        p(draft("博士班課程整理中。")),
        note("博士班對外介紹方式待院窗口與研究所確認（見招生資訊頁備註）。確認後請提供博士班必修、選修課程與學分。"),
    ])

    return page(
        opening,
        name_tape("每個人都要修的課"),
        common,
        name_tape("碩士班課程"),
        master,
        name_tape("博士班課程"),
        doctoral,
        p(draft("選課在校務資訊系統線上完成；學分與畢業條件看修業規定。"), muted=True),
        actions(text_link("修業規定", L("inst:E-2")), text_link("研究生手冊（PDF）", U_HANDBOOK),
                text_link("校務資訊系統（選課）", U_SAS), text_link("課務公告", L("inst:B-2"))),
        owner=META["owner"],
    )
