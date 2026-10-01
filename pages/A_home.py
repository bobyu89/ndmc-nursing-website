from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, photo,
                        ribbon_bar, split, unit_pair, feature_lead, feature_list, route_list, draft, note)
from links import L
from tokens import C

META = {"id": "A", "slug": "home", "title": "護理學院", "owner": "院窗口"}

# 院長照片與職稱取自現行專任教師頁 https://wwwndmc.ndmutsgh.edu.tw/DocDet/191/100010/1738/1659（alt「曾雯琦 院長」）。
DEAN_PHOTO = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9B%BE%E9%9B%AF%E7%90%A6.jpg"


def render():
    opening = split(
        "".join([
            statement(
                draft("在這裡，護理師也是軍官。"),
                draft("我們培育能在醫院照護病人、也能在戰傷與災難現場執行任務的軍護人才。"
                      "從學士到研究所，學習在三軍總醫院的臨床現場發生。"),
            ),
            actions(button("招生專區", L("F")), text_link("認識本院", L("C"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch("護理學院", "College of Nursing", unit="college",
              illo=illo_slot("身著制服的護理師（CocoMaterial，重新上色）", "1/1"), tab="國防醫學大學", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    quick = ribbon_bar([
        ("招生專區", L("F")),
        ("學術單位", L("D")),
        ("學術資源", L("E")),
        ("國際交流", L("G")),
        ("English", L("J")),
    ])

    dean = split(
        photo(DEAN_PHOTO, "護理學院院長曾雯琦", "3/4"),
        "".join([
            p(draft("「院長的話摘錄，約兩句，說明學院的辦學方向。」"), muted=False),
            p("曾雯琦院長　特聘教授", muted=True),
            actions(text_link("院長的話", L("C-1")), text_link("學院簡介", L("C-2"))),
        ]),
        cols=(3, 9), align="start",
    )

    units = unit_pair([
        ("dept", "護理學系", "學士班・臨床與軍陣實習", L("D-1")),
        ("inst", "護理研究所", draft("碩士班・博士班・研究"), L("D-2")),
    ])

    lead = feature_lead(
        "軍陣護理",
        [p(draft("軍陣護理是本院獨有的核心：在野戰、艦艇、航空與災區等特殊環境中維持照護品質，"
                 "課程結合軍事訓練與臨床實習。"))],
        illo_slot("野戰救護場景", "1/1"),
        href=L("E-2"), link_label="學術研究",
    )
    others = feature_list([
        ("戰傷與災難護理", draft("以戰傷救護與大量傷患應變為研究與教學重點，連結模擬教學與實地演練。"), L("E-2"), "college", "戰"),
        ("國際交流", draft("與國外護理院校互訪、學生短期交流與學者來訪。"), L("G"), "college", "際"),
        ("研究能量", draft("教師研究計畫與代表成果，由研究所研究成果頁完整呈現。"), L("E-2"), "inst", "研"),
    ])

    news = route_list([
        ("院務公告", "影響全院或跨系所的行政事項", L("B-1")),
        ("招生訊息", "各學制招生消息與時程", L("B-3")),
        ("學術活動", "講座、研討會", L("B-2")),
        ("榮譽榜", "師生獲獎與成果", L("B-4")),
        ("徵才訊息", "教師與行政人員徵聘", L("B-5")),
    ])

    return page(
        opening,
        quick,
        name_tape("院長與學院"),
        dean,
        name_tape("學術單位"),
        units,
        name_tape("學院特色"),
        lead,
        others,
        name_tape("最新消息"),
        note("首頁為靜態 HTML，無法自動帶入最新消息；以分類入口導向各消息模組。"),
        news,
        actions(text_link("所有消息", L("B"))),
        owner=META["owner"],
    )
