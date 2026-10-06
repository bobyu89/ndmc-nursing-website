from urllib.parse import quote

from components import page, name_tape, statement, p, split, photo, actions, text_link, tape_surface, draft, note, todo
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

    # 全文收到前只有 todo（正式版不輸出），本段連同標題一起隱藏。
    message = todo("所長的話全文 400–600 字：開場問候、辦學理念、研究方向、人才培育、給報考者的話，文末署名（院窗口提供）")

    return page(
        opening,
        name_tape("所長"),
        portrait,
        note("姓名、職稱、專長、研究室連結與照片取自學院專任教師頁（" + U_DIRECTOR + "）。請院窗口提供"
             "所長的話全文 400–600 字（辦學理念、研究與人才培育方向）；收到原文後以 tape_surface 分段放入，文末署名「護理研究所所長　潘雪幸」。"),
        *([name_tape("所長的話"), message] if message else []),
        actions(text_link("研究所簡介", L("inst:C-2")), text_link("研究領域", L("inst:F-1")), text_link("招生資訊", L("inst:D-1"))),
        owner=META["owner"],
    )
