from components import page, name_tape, statement, p, text_link, actions, unit_pair, route_list, draft, note
from links import L

META = {"id": "H-3", "slug": "documents", "title": "院務文件", "owner": "院窗口"}


def render():
    forms = unit_pair([
        ("dept", "學生相關表單下載", "學士班學生", L("H-3-student")),
        ("inst", "研究生相關表單下載", draft("碩士班・博士班"), L("H-3-grad")),
    ])

    # 院級章程與設置要點：名稱、訂定日期與 PDF 連結取自現行「組織架構」頁（unit/100010/4125）附件區。
    charters = route_list([
        ("國防醫學大學護理學院組織章程", "114年9月8日訂定（PDF）",
         "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100010/14343/%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E7%B5%84%E7%B9%94%E7%AB%A0%E7%A8%8B1140908%E8%A8%82%E5%AE%9A.pdf"),
        ("國防醫學大學護理學院院務發展委員會設置要點", "114年10月13日訂定（PDF）",
         "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100010/14344/%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E9%99%A2%E5%8B%99%E7%99%BC%E5%B1%95%E5%A7%94%E5%93%A1%E6%9C%83%E8%A8%AD%E7%BD%AE%E8%A6%81%E9%BB%9E1141013%E8%A8%82%E5%AE%9A.pdf"),
        ("國防醫學大學護理學院院教師發展委員會設置要點", "114年12月8日訂定（PDF）",
         "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100010/14856/%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E9%99%A2%E6%95%99%E5%B8%AB%E7%99%BC%E5%B1%95%E5%A7%94%E5%93%A1%E6%9C%83%E8%A8%AD%E7%BD%AE%E8%A6%81%E9%BB%9E1141208%E8%A8%82%E5%AE%9A.pdf"),
        ("國防醫學大學護理學院院課程發展委員會設置要點", "114年10月13日訂定（PDF）",
         "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100010/14345/%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E9%99%A2%E8%AA%B2%E7%A8%8B%E7%99%BC%E5%B1%95%E5%A7%94%E5%93%A1%E6%9C%83%E8%A8%AD%E7%BD%AE%E8%A6%81%E9%BB%9E1141013%E8%A8%82%E5%AE%9A.pdf"),
        ("國防醫學大學護理學院院學生事務委員會設置要點", "114年11月12日訂定（PDF）",
         "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100010/14857/%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E9%99%A2%E5%AD%B8%E7%94%9F%E4%BA%8B%E5%8B%99%E5%A7%94%E5%93%A1%E6%9C%83%E8%A8%AD%E7%BD%AE%E8%A6%81%E9%BB%9E1141112%E8%A8%82%E5%AE%9A.pdf"),
        ("國防醫學大學護理學院院圖儀福利委員會設置要點", "114年12月8日訂定（PDF）",
         "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100010/14858/%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E9%99%A2%E5%9C%96%E5%84%80%E7%A6%8F%E5%88%A9%E5%A7%94%E5%93%A1%E6%9C%83%E8%A8%AD%E7%BD%AE%E8%A6%81%E9%BB%9E1141208%E8%A8%82%E5%AE%9A.pdf"),
    ])

    return page(
        statement(
            "院級組織章程集中在這一頁。",
            "要找表單的學生與研究生，請直接從下面兩個入口進入。",
        ),
        name_tape("表單下載"),
        forms,
        note("兩個入口的目的頁尚未決定（可能是學系、研究所的表單下載節點，或新建的 CMS 表單下載模組），"
             "請院窗口提供兩個網址後替換。"),
        name_tape("院級組織章程"),
        p("本頁只放護理學院層級的組織章程；學系與研究所的辦法，請到各單位網站查看。"),
        note("下列六份章程與設置要點目前掛在「組織架構」節點（unit/100010/4125）的附件區，連結直接指向該處的 PDF。"
             "改版時若改用 CMS「附件下載」模組放檔案，本頁文字可放在模組上方，下方清單即可刪除。"
             "「院教師評審委員會」沒有設置要點附件，請院窗口確認是否要補。"),
        charters,
        note("現行「下載專區」（unit/100010/729）有三份檔案，都是表單而非章程，請決定去處："
             "「國防醫學大學護理學院財產設備 學院外借用 申請單」、「國防醫學大學護理學院-研究生討論室、置物櫃借用表」"
             "（可移到研究生表單或場地借用）、「護理學院用印申請表」。"),
        actions(text_link("回院務與規章", L("H"))),
        owner=META["owner"],
    )
