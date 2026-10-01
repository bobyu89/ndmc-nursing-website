from components import page, name_tape, statement, p, split, photo, actions, text_link, tape_surface, draft, note
from links import L

META = {"id": "C-1", "slug": "dean", "title": "院長的話", "owner": "三長"}

# 照片、職級、學位、專長取自現行專任教師個人頁 https://wwwndmc.ndmutsgh.edu.tw/DocDet/191/100010/1738/1659；
# 院士榮譽取自學院最新消息（2026/07/14）https://wwwndmc.ndmutsgh.edu.tw/news/191/100010/1628
DEAN_PHOTO = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9B%BE%E9%9B%AF%E7%90%A6.jpg"


def render():
    opening = statement(
        "院長的話",
        draft("院長談學院為什麼培育軍護人才，以及接下來要往哪裡走。"),
    )

    # 院長姓名取自現行「現任院長」頁（unit/100010/1461），原文照錄。
    portrait = split(
        photo(DEAN_PHOTO, "護理學院院長曾雯琦", "3/4"),
        "".join([
            p("護理學院 曾雯琦院長"),
            p("特聘教授｜美國加州大學舊金山分校護理哲學博士｜專長：精神衛生護理", muted=True),
            p("2026 年獲選美國護理科學院院士（Fellow of the American Academy of Nursing, FAAN）", muted=True),
        ]),
        cols=(4, 8), align="start",
    )

    message = tape_surface(
        p(draft("【開場】向讀者問候，用一兩句話說出護理學院是什麼樣的地方。")),
        p(draft("【治院理念】院長重視的價值，以及學院如何把軍陣護理與臨床照護放在同一個教育裡。")),
        p(draft("【發展願景】未來幾年學院在教學、研究與國際交流上的方向。")),
        p(draft("【給學生與家長】對想加入學院的高中生與家長說的一段話。")),
        p(draft("【署名】護理學院院長　姓名"), muted=True),
    )

    return page(
        opening,
        name_tape("院長"),
        portrait,
        note("照片暫用現行專任教師個人頁的院長照（「現任院長」頁另有一張形象照，約 20MB，不適合直接引用）；如要更換請三長提供。"
             "請三長提供院長的話全文 400–600 字，內容包含治院理念與發展願景。以下四段為結構草稿，收到原文後整段替換。"),
        name_tape("院長的話"),
        message,
        actions(text_link("學院簡介", L("C-2")), text_link("教育理念", L("C-5"))),
        owner=META["owner"],
    )
