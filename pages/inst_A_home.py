from urllib.parse import quote

from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, photo,
                        ribbon_bar, split, unit_pair, feature_lead, feature_list, route_list, draft, note)
from links import L
from tokens import C, SITE

META = {"id": "A", "slug": "home", "title": "護理研究所", "owner": "院窗口", "site": "inst"}

# 所長照片取自學院專任教師頁（DocDet/191/100010/1738/1662，潘雪幸）。
IMG_DIRECTOR = SITE + quote("/files/web/192/doctor/100010/1738/潘113師資.jpg")


def render():
    opening = split(
        "".join([
            statement(
                draft("把臨床裡的問題，帶回來做成研究。"),
                draft("護理研究所培養能提出問題、設計研究、再把證據帶回照護現場的護理人才。"),
            ),
            actions(button("招生資訊", L("inst:D-1")), text_link("認識本所", L("inst:C"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch(
            "護理研究所", "Graduate Institute of Nursing", unit="inst",
            illo=illo_slot("研究生與指導教師討論數據（CocoMaterial，重新上色）", "1/1"),
            tab="護理學院", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    quick = ribbon_bar([
        ("招生資訊", L("inst:D-1")),
        ("修業資訊", L("inst:E")),
        ("研究成果", L("inst:F")),
        ("研究生專區", L("inst:G")),
    ])

    director = split(
        photo(IMG_DIRECTOR, "護理研究所所長潘雪幸教授", "3/4"),
        "".join([
            p("民國68年為因應教育與研究之需求，設立護理研究所，成為國內護理碩士教育之先驅。"),
            p(draft("「所長的話摘錄，約兩句，說明研究與人才培育的方向。」")),
            actions(text_link("所長的話", L("inst:C-1")), text_link("研究所簡介", L("inst:C-2"))),
        ]),
        cols=(3, 9), align="start",
    )

    research = feature_lead(
        "研究領域",
        [p(draft("研究方向、特色團隊與各指導教師目前招收的研究主題，都整理在研究領域頁。"))],
        illo_slot("研究生在病房蒐集資料", "1/1"),
        unit="inst", href=L("inst:F-1"), link_label="看研究領域",
    )
    more = feature_list([
        ("指導教師", draft("每位教師的專長、研究室與代表著作，收在學院師資陣容。"), L("E-1"), "inst", "師"),
        ("研究發表", draft("教師代表論文、最新研究與研究生成果。"), L("inst:F-2"), "inst", "文"),
        ("學術活動", draft("已舉辦的講座、研討會與學術交流紀錄。"), L("inst:F-3"), "inst", "會"),
    ])

    news = route_list([
        ("招生公告", "招生消息、簡章與重要時程", L("inst:B-1")),
        ("課務公告", "選課、課程與修業", L("inst:B-2")),
        ("口試公告", "學位考試與畢業時程", L("inst:B-3")),
        ("獎學金公告", "獎助學金申請與結果", L("inst:B-4")),
        ("學術活動", "即將舉辦的講座與研討會", L("inst:B-5")),
    ], unit="inst")

    family = unit_pair([
        ("college", "護理學院", "學院首頁・師資・國際交流", L("A")),
        ("dept", "護理學系", "學士班・臨床與軍陣實習", L("D-1")),
    ])

    return page(
        opening,
        quick,
        name_tape("所長與研究所"),
        director,
        name_tape("研究"),
        research,
        more,
        name_tape("研究所公告"),
        note("首頁為靜態 HTML，無法自動帶入公告；以分類入口導向各公告模組。"),
        news,
        actions(text_link("所有公告", L("inst:B"))),
        name_tape("護理學院與學系"),
        family,
        owner=META["owner"],
    )
