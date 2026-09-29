from components import (page, name_tape, statement, p, button, text_link, actions, split, photo_slot, route_list,
                        tape_surface, draft, note)
from links import L
from tokens import SITE

META = {"id": "C", "slug": "about", "title": "認識本所", "owner": "院窗口", "site": "inst"}

U_INST_HISTORY = SITE + "/unit/100181/6527"      # 研究所「歷史沿革」
U_DIRECTOR = SITE + "/DocDet/191/100010/1738/1662"  # 專任教師個人頁：潘雪幸


def render():
    opening = statement(
        draft("國內護理碩士教育，從這裡起步。"),
        draft("護理研究所成立於民國68年，培育能提出臨床問題、做研究，再把結果帶回照護現場的護理人才。"
              "這一頁幫你找到所長、研究所的來歷與指導教師。"),
    )

    # 原文照錄自研究所「歷史沿革」頁。
    origin = tape_surface(
        p("民國68年為因應教育與研究之需求，設立護理研究所，成為國內護理碩士教育之先驅。"),
        p(draft("摘自護理研究所〈歷史沿革〉。") + "　" + text_link("原頁面", U_INST_HISTORY), muted=True),
        actions(text_link("研究所簡介與發展沿革", L("inst:C-2"))),
    )

    # 職稱原文照錄自專任教師個人頁（DocDet 1662）。
    director = split(
        photo_slot("所長照片（直式 3:4）", "3/4"),
        "".join([
            p("潘雪幸"),
            p("國防醫學大學護理學院教授暨護理研究所所長", muted=True),
            actions(text_link("所長的話", L("inst:C-1"))),
        ]),
        cols=(3, 9), align="start",
    )

    routes = route_list([
        ("所長的話", draft("所長談研究所的辦學理念與人才培育方向"), L("inst:C-1")),
        ("研究所簡介", draft("研究特色、發展沿革、教育目標與碩博士班定位"), L("inst:C-2")),
        ("師資陣容", draft("指導教師的專長與研究室，收在學院師資陣容"), L("E-1")),
    ], unit="inst")

    return page(
        opening,
        name_tape("研究所的起點"),
        origin,
        name_tape("所長"),
        director,
        note("所長姓名與職稱取自學院專任教師頁（" + U_DIRECTOR + "）。請院窗口確認仍為現任，並提供直式照片。"),
        name_tape("認識本所各頁"),
        routes,
        note("師資只由學院「師資陣容」一處維護，本所不另建教師名單；若要只列研究所指導教師，請在學院頁加篩選或錨點。"),
        actions(button("招生專區", L("inst:D")), text_link("研究領域", L("inst:F-1"))),
        owner=META["owner"],
    )
