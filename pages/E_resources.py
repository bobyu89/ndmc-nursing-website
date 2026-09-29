from components import (page, name_tape, statement, p, button, text_link, actions, split, photo_slot, illo_slot,
                        bullets, route_list, draft, note)
from links import L

META = {"id": "E", "slug": "resources", "title": "學術資源", "owner": "院窗口"}

# 設備名稱逐字取自現行「教學設備」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/1463
# 師資分類逐字取自現行「師資介紹」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/716


def render():
    opening = "".join([
        statement(
            draft("老師、研究與教室，都在這一頁找得到。"),
            draft("護理學系與護理研究所共用同一群老師、同一套研究能量與教學空間。"
                  "由學院統一整理，兩個單位的網站都連回這裡。"),
        ),
        actions(button("師資陣容", L("E-1")), text_link("學術研究", L("E-2")), text_link("教學設備", L("E-3"))),
    ])

    faculty = split(
        "".join([
            p(draft("依專任、合聘與兼任分列，每位老師附上職級、專長與研究室連結。"
                    "想找論文指導教授，或想知道誰教哪一門課，從這裡開始。")),
            bullets(["專任教師", "合聘教師", "兼任老師"]),
            actions(text_link("看全部師資", L("E-1"))),
        ]),
        photo_slot("全院教師合照", "4/3"),
        cols=(7, 5),
    )

    research = split(
        "".join([
            p(draft("軍陣護理與戰傷與災難護理是本院研究的核心，另有精神衛生、慢性病照護、"
                    "睡眠與健康促進等方向。完整的研究成果與論文清單放在研究所網站。")),
            actions(text_link("學術研究", L("E-2")), text_link("護理研究所網站", L("D-2"))),
        ]),
        illo_slot("研究討論場景（CocoMaterial，重新上色）", "4/3", unit="inst"),
        cols=(7, 5), reverse=True,
    )

    facilities = split(
        "".join([
            p(draft("學生先在模擬的病房與情境中反覆練習，再進入臨床。")),
            bullets(["示範教室", "示範實習病房", "虛擬中心", "智慧互動護理自學教室"]),
            actions(text_link("教學設備", L("E-3"))),
        ]),
        photo_slot("示範實習病房", "4/3"),
        cols=(7, 5),
    )

    return page(
        opening,
        name_tape("師資陣容"),
        faculty,
        name_tape("學術研究", unit="inst"),
        research,
        name_tape("教學設備", unit="dept"),
        facilities,
        note("三張圖片待補：全院教師合照（現行學系網站輪播已有「護理學院全體教師」照片可沿用）、"
             "研究情境插圖、示範實習病房照片（現行教學設備頁已有兩張可沿用）。"),
        name_tape("相關頁面"),
        route_list([
            ("護理學系", "學士班", L("D-1")),
            ("護理研究所", "碩士班", L("D-2")),
            ("教師資格審查", "審查規定、流程與表單", L("H-1")),
        ]),
        owner=META["owner"],
    )
