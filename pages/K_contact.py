from components import (page, name_tape, statement, p, button, text_link, actions, photo_slot, facts, route_list,
                        draft, note)
from links import L

META = {"id": "K", "slug": "contact", "title": "聯絡我們", "owner": "院窗口"}

EMAIL = "ndmu_con@mail.ndmutsgh.edu.tw"
# Map link published on the university fundraising site for the same campus address (民權東路六段161號).
MAP = "https://maps.app.goo.gl/MpA4rsvwnFxdnaM37"
# Transport: verbatim from the university 交通資訊 page.
TRAFFIC = "https://wwwndmc.ndmutsgh.edu.tw/unit/100141/955"


def render():
    # Contact facts: verbatim from the current 聯絡我們 page (unit/100010/2199).
    details = facts([
        ("地址", "114台北市內湖區民權東路六段161號4樓護理學院"),
        ("電話", "886-2-8792-3100&nbsp;&nbsp;ext 88916、18167、18767、18165"
                 f'<br>{text_link("撥打學院電話", "tel:+886287923100")}'),
        ("傳真", "886-2-66005702"),
        ("信箱", text_link(EMAIL, f"mailto:{EMAIL}")),
        ("辦公時間", draft("週一至週五8:00至17:00（不含例假日及國訂假日）")),
    ])

    english = p("College of Nursing<br>National Defense Medical University<br>"
                "No.161, Sec. 6, Minquan E. Rd., Neihu Dist., Taipei City 11490, Taiwan (R.O.C.)")

    units = route_list([
        ("護理學系", draft("學士班課程、實習與學生事務"), L("D-1")),
        ("護理研究所", draft("碩士班、博士班與研究生事務"), L("D-2")),
    ])

    return page(
        statement(
            "國防醫學大學護理學院辦公室",
            draft("地址、電話與信箱都在這裡；用手機瀏覽時，點一下就能撥號或寄信。"),
        ),
        actions(button("寄信給學院", f"mailto:{EMAIL}")),
        name_tape("聯絡方式"),
        details,
        note("辦公時間暫填學校網站頁尾的全校上班時間，請院窗口確認學院辦公室是否相同（含午休是否受理）。"
             "電話分機若有分工（例：招生、學務、院務），也請提供每個分機負責的事項。"),
        name_tape("英文地址"),
        english,
        name_tape("怎麼到學院"),
        photo_slot("學院所在大樓外觀或校區位置圖", "16/9"),
        facts([
            ("公車", "國防醫學大學站--617、645、645副、903、紅32、藍36"),
            ("自行開車", "行經中山高速公路，請下內湖成功交流道，南下車輛右轉(北上車輛左轉)往成功路二段，"
                        "約一公里後右轉往民權東路六段，約五百公尺後左轉進國防醫學大學大門。因停車位有限，請多利用大眾交通系統。"),
            ("三軍總醫院接駁車", "可搭乘三軍總醫院接駁車，至三總內湖院區後步行至醫學院。"),
        ]),
        actions(text_link("在 Google 地圖開啟", MAP), text_link("學校交通資訊（完整公車路線）", TRAFFIC)),
        note("交通說明逐字取自學校「交通資訊」頁。請院窗口提供大樓外觀照片，以及從校門口到學院（4樓）的步行指引。"),
        name_tape("學系與研究所"),
        p(draft("學系或研究所的事務，也可以直接到各單位網站查詢聯絡方式。")),
        units,
        owner=META["owner"],
    )
