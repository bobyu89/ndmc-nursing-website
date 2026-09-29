from components import page, name_tape, statement, p, split, photo_slot, actions, text_link, tape_surface, draft, note
from links import L

META = {"id": "C-1", "slug": "dean", "title": "院長的話", "owner": "三長"}


def render():
    opening = statement(
        draft("院長的話"),
        draft("院長談學院為什麼培育軍護人才，以及接下來要往哪裡走。"),
    )

    # 院長姓名取自現行「現任院長」頁（unit/100010/1461），原文照錄。
    portrait = split(
        photo_slot("院長照片（直式 3:4）", "3/4"),
        "".join([
            p("護理學院 曾雯琦院長"),
            p(draft("職稱與學經歷一行，例如最高學歷、專長領域。"), muted=True),
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
        note("請三長提供：① 院長姓名與職稱確認（現行網站寫「曾雯琦院長」，請確認仍為現任）；"
             "② 院長直式照片（3:4，現行「現任院長」頁已有一張形象照，可沿用或更新）；"
             "③ 院長的話全文 400–600 字，內容包含治院理念與發展願景。以下四段為結構草稿，收到原文後整段替換。"),
        name_tape("院長的話"),
        message,
        actions(text_link("學院簡介", L("C-2")), text_link("教育理念", L("C-5"))),
        owner=META["owner"],
    )
