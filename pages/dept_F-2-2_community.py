from components import (page, name_tape, statement, p, bullets, text_link, actions, split, photo_slot, illo_slot, facts,
                        draft, note)
from links import L
from tokens import SITE

META = {"id": "F-2-2", "slug": "community", "title": "社區實習", "owner": "院窗口", "site": "dept"}

# plain 文字逐字取自《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月
# （學生專區 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681 附件，2026-09-29 擷取）：
#   第二章 柒、三〈臨床實習〉；第三章 柒 表五「社區衛生護理學實習」列。
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = split(
        statement(
            draft("走出醫院，到社區裡照顧一整個家庭。"),
            draft("社區衛生護理學實習在健康服務中心與三軍總醫院社區醫學部進行，練的是群體評估、家庭訪視與團體衛教。"),
        ),
        '<div class="mx-auto" style="max-width:280px;">'
        + illo_slot("護生到社區家庭訪視（CocoMaterial，重新上色）", "1/1", unit="dept") + "</div>",
        cols=(7, 5),
    )

    where = "".join([
        p("社區衛生護理學實習方面，則以台北市政府所屬之內湖和南港兩地的健康服務中心，以及三軍總醫院社區醫學部為主要實習單位。"),
        _source("摘自《護理學系學生手冊》（115年8月）〈臨床實習〉。", U_HANDBOOK, "學生手冊（PDF）"),
    ])

    what = "".join([
        split(
            "".join([
                p(draft("護理師國家考試對社區衛生護理學實習的要求：")),
                bullets([
                    "實習內容包含：社區群體評估與計畫。",
                    "家庭與個人層次：包括家庭訪視、個案管理等。",
                    "團體衛教。",
                ]),
                facts([("實習時數最低標準", "120小時")]),
            ]),
            photo_slot("護生在健康服務中心進行團體衛教", "4/3"),
            cols=(7, 5), align="start",
        ),
        _source("摘自學生手冊表五「實習學科、實習內涵及實習時數最低標準」（考選部規定的最低標準，不是本系實際排定的時數）。",
                U_HANDBOOK, "學生手冊（PDF）"),
    ])

    course = "".join([
        p(draft("課程地圖把「社區衛生護理學」排在四年級的護理專業課程。")),
        actions(text_link("課程地圖", L("dept:F-1-3"))),
        note("院窗口請轉社區衛生護理學課程負責老師提供：實習排在哪一學期、實習幾週、學生在健康服務中心與社區醫學部各做哪些事，"
             "以及過去學生辦過的衛教活動主題或成果照片（民眾不可辨識、學生需同意）。"
             "若社區實習也包含長照機構或其他單位，請一併列出並提供出處。"),
    ])

    return page(
        opening,
        name_tape("實習單位"),
        where,
        name_tape("實習內容"),
        what,
        name_tape("什麼時候去"),
        course,
        actions(text_link("實習規定與表單", L("dept:F-2-4")), text_link("醫院實習", L("dept:F-2-1"))),
        owner=META["owner"],
    )
