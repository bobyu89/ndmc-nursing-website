from components import (page, name_tape, statement, p, button, text_link, actions, photo_slot, split, facts,
                        route_list, bullets, draft, note)
from links import L

META = {"id": "K", "slug": "alumni", "title": "校友專區", "owner": "院窗口", "site": "dept"}

# 聯絡資料與附件名稱逐字取自現行「校友專區」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6799（2026-09-29 擷取）。
# 系校友會網址取自學院常用連結（pages/L_links.py），2026-09-29 檢查時回應 HTTP 500。
# 「校友」分眾導覽 https://wwwndmc.ndmutsgh.edu.tw/gov/191/100132/146 取自全球資訊網上方選單。
# 校友設立的獎學金名稱取自獎學金專區 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6798

ASSOCIATION = "http://www.ndmcnd.url.tw/"
UNIVERSITY_ALUMNI = "https://wwwndmc.ndmutsgh.edu.tw/gov/191/100132/146"


def render():
    opening = "".join([
        statement(
            draft("畢業以後，學系還是你的家。"),
            draft("看看學長姐在做什麼、找到校友會，也可以回來支持學弟妹。"),
        ),
        actions(button("捐款支持學弟妹", L("I")), text_link("傑出校友", L("dept:K-1"))),
    ])

    news = "".join([
        split(
            "".join([
                p(draft("學長姐回校分享、校慶軍醫大會、校友會活動，學長姐的消息會整理在這裡。")),
                p(draft("〔校友動態標題〕：〔一到兩句說明：誰、做了什麼、何時〕")),
                p(draft("〔校友動態標題〕：〔一到兩句說明〕")),
            ]),
            photo_slot("校友返校活動照片", "4/3"),
            cols=(7, 5), align="start",
        ),
        note("校友動態目前沒有資料。本頁是靜態頁，不會自動更新；建議每學期整理 2 到 3 則（校友獲獎、返校分享、校友會活動），"
             "每則寫標題與一到兩句說明，附照片並取得本人同意公開。若動態較多，建議改發在學系公告的活動訊息，這裡只放連結。"),
    ])

    routes = "".join([
        route_list([
            ("傑出校友", draft("在臨床、軍中與各界服務的學長姐"), L("dept:K-1")),
            ("國防醫學大學護理學系系校友會", draft("系校友會網站：校友聯繫與活動"), ASSOCIATION),
            ("校友（國防醫學大學）", draft("全校校友服務與校友會入口"), UNIVERSITY_ALUMNI),
            ("捐款專區", draft("捐款支持學院與學弟妹"), L("I")),
        ], unit="dept"),
        note("系校友會網址 http://www.ndmcnd.url.tw/ 沿用現行網站所列，2026-09-29 檢查時網站回應錯誤（HTTP 500）。"
             "請院窗口向系校友會確認網站是否仍在使用；若已停用，請提供新的聯絡方式（網站、粉絲專頁或信箱）。"),
    ])

    giving = "".join([
        p(draft("學長姐也用獎學金支持在學的學弟妹，例如：")),
        bullets([
            "護理學系系友聯誼會獎學金",
            "國防醫學大學護理學院第一屆趙理事長獎學金",
        ]),
        actions(text_link("所有獎學金", L("dept:J-1"))),
    ])

    service = "".join([
        p(draft("想到國外執業、需要英文學分認證的校友，可以先看流程圖。本頁下方附件下載：")),
        bullets(["英文學分認證(CGFNS等)申請及填寫流程圖"]),
        note("流程圖是現行校友專區節點的附件，換上新版 html 後仍會顯示在頁面下方。"
             "表單下載節點（100180/6810）另有一份較舊的同名流程圖（1140408 版），請確認是否刪除舊版。"),
    ])

    contact = "".join([
        facts([
            ("單位", "國防醫學大學護理學院辦公室"),
            ("地址", "114台北市內湖區民權東路六段161號4樓護理學院"),
            ("電話", "TEL:886-2-8792-3100  ext 18165、18167"),
            ("傳真", "Fax:886-2-66005702"),
            ("信箱", '<a href="mailto:ndmu_con@mail.ndmutsgh.edu.tw" style="color:inherit;">ndmu_con@mail.ndmutsgh.edu.tw</a>'),
        ]),
        p("備註:學院115.4.16起ndmc88916@mail.ndmutsgh.edu.tw信箱已停用，無法收信", muted=True),
        p("College of Nursing, National Defense Medical University<br>"
          "No.161, Sec. 6, Minquan E. Rd., Neihu Dist., Taipei City 11490, Taiwan (R.O.C.)", muted=True),
    ])

    return page(
        opening,
        name_tape("校友動態"),
        news,
        name_tape("校友入口"),
        routes,
        name_tape("回饋學弟妹"),
        giving,
        name_tape("校友服務"),
        service,
        name_tape("聯絡學院"),
        contact,
        owner=META["owner"],
    )
