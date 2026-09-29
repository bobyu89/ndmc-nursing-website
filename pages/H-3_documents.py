from components import page, name_tape, statement, p, text_link, actions, unit_pair, route_list, draft, note
from links import L

META = {"id": "H-3", "slug": "documents", "title": "院務文件", "owner": "院窗口"}


def render():
    forms = unit_pair([
        ("dept", "學生相關表單下載", draft("學士班學生"), L("H-3-student")),
        ("inst", "研究生相關表單下載", draft("碩士班・博士班"), L("H-3-grad")),
    ])

    charters = route_list([
        (draft("院級組織章程名稱"), draft("最後修訂日期"), "#待補-章程檔案"),
        (draft("院級組織章程名稱"), draft("最後修訂日期"), "#待補-章程檔案"),
    ])

    return page(
        statement(
            draft("院級組織章程集中在這一頁。"),
            draft("要找表單的學生與研究生，請直接從下面兩個入口進入。"),
        ),
        name_tape("表單下載"),
        forms,
        note("兩個入口的目的頁尚未決定（可能是學系、研究所的表單下載節點，或新建的 CMS 表單下載模組），"
             "請院窗口提供兩個網址後替換。"),
        name_tape("院級組織章程"),
        p(draft("本頁只放護理學院層級的組織章程；學系與研究所的辦法，請到各單位網站查看。")),
        note("請院窗口提供每份院級組織章程的正式名稱、最後修訂日期與檔案（建議 PDF）。"
             "若沿用 CMS「附件下載」模組放檔案，本頁文字可放在模組上方，下方兩列預留格即可刪除。"),
        charters,
        note("現行「下載專區」（unit/100010/729）有三份檔案，都是表單而非章程，請決定去處："
             "「國防醫學大學護理學院財產設備 學院外借用 申請單」、「國防醫學大學護理學院-研究生討論室、置物櫃借用表」"
             "（可移到研究生表單或場地借用）、「護理學院用印申請表」。"),
        actions(text_link("回院務與規章", L("H"))),
        owner=META["owner"],
    )
