from components import page, name_tape, statement, p, text_link, actions, route_list, draft, note
from links import L

META = {"id": "H", "slug": "admin", "title": "院務與規章", "owner": "院窗口"}


def render():
    # 各入口說明依 Notion 內容清單（content/notion/college-zh.md）H-1〜H-3 的頁面內容。
    routes = route_list([
        ("教師資格審查", "給送審教師：審查規定、流程與表單", L("H-1")),
        ("場地借用", draft("給要借用學院場地的師生與單位"), L("H-2")),
        ("院務文件", "院級組織章程，以及學生、研究生表單下載入口", L("H-3")),
        ("評鑑", draft("歷年評鑑結果，收在歷史沿革的大事記中"), L("C-3")),
    ])

    return page(
        statement(
            draft("教職員要辦的事，從這裡進去。"),
            draft("教師資格審查、場地借用、院務文件與評鑑資料各有專頁，本頁只負責帶路。"),
        ),
        name_tape("行政入口"),
        routes,
        note("場地借用目前以 SurveyCake 統計、再人工設定門禁，流程仍在討論；本頁只保留連結，不改動現行流程。"
             "另：links.py 中場地借用（H-2）與教學設備（E-3）目前指向同一節點 unit/100010/1463，確定分頁後請更新。"),
        name_tape("找不到要辦的事"),
        p(draft("不確定該找哪一頁，請直接聯絡學院辦公室。")),
        actions(text_link("聯絡我們", L("K"))),
        owner=META["owner"],
    )
