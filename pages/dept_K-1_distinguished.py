from components import (page, name_tape, statement, p, text_link, actions, roster, facts, route_list, draft, note)
from links import L

META = {"id": "K-1", "slug": "distinguished", "title": "傑出校友", "owner": "院窗口", "site": "dept"}

# 現行網站沒有傑出校友資料；本頁只有結構，絕不放未經確認的姓名、職稱或事蹟。

SLOT = "〔待提供〕"


def render():
    opening = "".join([
        statement(
            draft("從這裡畢業的護理人，現在在哪裡。"),
            draft("學長姐在醫院、軍中與各個領域服務。這裡介紹幾位傑出校友，也讓學弟妹看見未來的樣子。"),
        ),
        actions(text_link("回校友專區", L("dept:K")), text_link("推薦傑出校友", "#nominate")),
    ])

    people = "".join([
        roster([
            ("〔校友姓名〕", "〔畢業年〕", "護理學系", draft("〔現職單位與職稱〕。〔一到兩句事蹟：做了什麼、得過什麼肯定〕"), None),
            ("〔校友姓名〕", "〔畢業年〕", "護理學系", draft("〔現職單位與職稱〕。〔一到兩句事蹟〕"), None),
            ("〔校友姓名〕", "〔畢業年〕", "護理學系", draft("〔現職單位與職稱〕。〔一到兩句事蹟〕"), None),
        ]),
        note("請院窗口提供傑出校友名單：每位的姓名、畢業年（請寫西元或民國年，不用屆別代號）、現職單位與職稱、"
             "一到兩句事蹟（獲獎請寫獎項全名與年份），以及一張直式大頭照（3:4）。"
             "每位都要取得本人同意公開姓名、照片與事蹟。若校友有自己的介紹頁或報導，可附連結，名字下方會出現連結。"
             "人數不限，照上方格式往下加；排序方式（依畢業年或依獲選年）請一併決定。"),
    ])

    nominate = "".join([
        '<div id="nominate"></div>',
        p(draft("認識值得介紹的學長姐嗎？歡迎推薦給學系。")),
        facts([
            ("推薦條件", SLOT),
            ("推薦方式", SLOT),
            ("聯絡窗口", SLOT),
        ]),
        note("傑出校友的遴選條件與推薦方式目前沒有資料。若學系或校友會有既定的遴選辦法，請提供辦法名稱與重點；"
             "若沒有，可刪除本段，只保留名單。"),
    ])

    related = route_list([
        ("校友專區", draft("校友動態、校友會與校友服務"), L("dept:K")),
        ("捐款專區", draft("捐款支持學院與學弟妹"), L("I")),
    ], unit="dept")

    return page(
        opening,
        name_tape("傑出校友"),
        people,
        name_tape("推薦傑出校友"),
        nominate,
        name_tape("相關頁面"),
        related,
        owner=META["owner"],
    )
