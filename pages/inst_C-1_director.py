from urllib.parse import quote

from components import page, name_tape, statement, p, split, photo, actions, text_link, tape_surface, draft, note
from links import L
from tokens import SITE

META = {"id": "C-1", "slug": "director", "title": "所長的話", "owner": "院窗口", "site": "inst"}

# 姓名、職稱、專長學科、研究室連結與照片，原文照錄自專任教師個人頁：
U_DIRECTOR = SITE + "/DocDet/191/100010/1738/1662"
IMG_DIRECTOR = SITE + quote("/files/web/192/doctor/100010/1738/潘113師資.jpg")
U_LAB = "https://sites.google.com/view/hhpndmc/home"


def render():
    opening = statement(
        "所長的話",
        draft("所長談研究所想培育什麼樣的護理人才，以及研究要往哪裡走。"),
    )

    portrait = split(
        photo(IMG_DIRECTOR, "護理研究所所長潘雪幸教授", "3/4"),
        "".join([
            p("潘雪幸"),
            p("國防醫學大學護理學院教授暨護理研究所所長", muted=True),
            p("專長學科：癌症護理、安寧療護、護理教育、急重症護理、軍陣護理"),
            actions(text_link("所長研究室", U_LAB), text_link("學經歷與著作（師資陣容）", L("E-1"))),
        ]),
        cols=(4, 8), align="start",
    )

    message = tape_surface(
        p(draft("【開場】向讀者問候，用一兩句話說出護理研究所是什麼樣的地方。")),
        p(draft("【辦學理念】研究所重視的價值：為什麼護理人員需要研究能力，研究如何回到臨床。")),
        p(draft("【研究方向】研究所目前的重點研究領域，以及和三軍總醫院、國軍醫療的連結。")),
        p(draft("【人才培育】碩士班（與博士班）要培養出什麼樣的畢業生。")),
        p(draft("【給報考者】對正在考慮報考的護理師說的一段話。")),
        p(draft("【署名】護理研究所所長　潘雪幸"), muted=True),
    )

    return page(
        opening,
        name_tape("所長"),
        portrait,
        note("姓名、職稱、專長、研究室連結與照片取自學院專任教師頁（" + U_DIRECTOR + "）。請院窗口提供"
             "所長的話全文 400–600 字（辦學理念、研究與人才培育方向）；下方五段為結構草稿，收到原文後整段替換。"),
        name_tape("所長的話"),
        message,
        actions(text_link("研究所簡介", L("inst:C-2")), text_link("研究領域", L("inst:F-1")), text_link("招生資訊", L("inst:D-1"))),
        owner=META["owner"],
    )
