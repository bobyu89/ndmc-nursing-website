from components import (page, name_tape, statement, p, h4, text_link, actions, photo_slot, split, facts,
                        route_list, draft, note)
from links import L

META = {"id": "I-3", "slug": "inbound", "title": "境外學生來校交流", "owner": "院窗口", "site": "dept"}

# 西北大學、八王子兩段說明（非 draft 部分）逐字取自現行系學會頁圖片「系學會協助辦理活動」
#   https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6796（更新日期 2025-10-28）。
#   原圖「與美國西北大學學學生交流」多一個「學」字，這裡已刪；其餘照錄。
# 泰國法政大學只見於 Notion 內容清單（「西北、八王子、泰國法政學生來交流」），現行網站找不到文字，整段為暫擬。

SLOT = "〔待提供〕"


def visit(title, text_blocks, photo_label, rows, reverse=False):
    return split(
        "".join([h4(title), *text_blocks, facts(rows)]),
        photo_slot(photo_label, "4/3"),
        cols=(7, 5), reverse=reverse, align="start",
    )


def render():
    opening = "".join([
        statement(
            draft("他們來看臺灣的護理，我們也認識他們的。"),
            draft("國外護理學生來校時，由系學會國際事務組和同學一起接待：一起上課、參觀、交流彼此的護理與文化。"),
        ),
        actions(text_link("學系學生出國交流", L("dept:H")), text_link("學院學生交流", L("G-2"))),
    ])

    northwestern = visit(
        "美國西北大學",
        [p("與美國西北大學學生交流，了解護理在不同國家的展現，也與他們分享我們學校的特色與臺灣的特色文化。")],
        "西北大學學生來訪合照",
        [("來訪時間", "2月" + draft("（依系學會活動表）")), ("年份", SLOT), ("人數", SLOT), ("交流內容", SLOT)],
    )

    hachioji = visit(
        "日本八王子",
        [p("與日本八王子學校的學生交流，了解護理在不同國家的展現，也與他們分享我們學校的特色與臺灣的特色文化。")],
        "八王子學校學生來訪交流",
        [("來訪時間", "11月" + draft("（依系學會活動表）")), ("學校全名", SLOT), ("年份", SLOT), ("人數", SLOT)],
        reverse=True,
    )

    thammasat = visit(
        draft("泰國法政大學"),
        [p(draft("泰國法政大學的護理學生曾來校交流。"))],
        "泰國法政大學學生來訪（待提供）",
        [("來訪時間", SLOT), ("年份", SLOT), ("人數", SLOT), ("交流內容", SLOT)],
    )

    visits_note = note("西北大學與八王子的說明取自系學會圖片，月份是系學會活動表上的月份，沒有年份。"
                       "泰國法政大學只出現在內容清單，網站上找不到紀錄，整段為暫擬。"
                       "請院窗口向國際事務確認：三所學校的正式校名（「八王子學校」是哪一所學校）、各次來訪的年份、人數、交流內容，"
                       "以及照片可否公開。沒有資料的學校請整段刪除；未確認前不放任何年份與人數。")

    host = "".join([
        p("國際事務組－負責辦理學系與國外學校交流之活動，接待國外貴賓、師長和與會朋友，協助籌備國際交流之計畫。"),
        p(draft("想參與接待的同學，可以找系學會國際事務組。"), muted=True),
    ])

    routes = route_list([
        ("學生交流（護理學院）", draft("學院層級的出國與來校交流紀錄、申請資訊"), L("G-2")),
        ("國際合作（護理學院）", draft("國際盟校與合作備忘錄"), L("G-1")),
        ("系學會", draft("國際事務組與其他幹部分工"), L("dept:I-1")),
    ], unit="dept")

    return page(
        opening,
        name_tape("來訪的學校"),
        northwestern,
        hachioji,
        thammasat,
        visits_note,
        name_tape("誰負責接待"),
        host,
        name_tape("相關頁面"),
        routes,
        owner=META["owner"],
    )
