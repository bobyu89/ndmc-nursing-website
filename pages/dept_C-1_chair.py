from components import page, name_tape, statement, p, split, photo, actions, text_link, tape_surface, draft, note
from links import L

META = {"id": "C-1", "slug": "chair", "title": "系主任的話", "owner": "三長", "site": "dept"}

# 系主任姓名、職級、職務、學位、專長與研究室連結取自現行「專任教師」名冊
# （https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100010/1738，列於「系所主管」），與學院師資陣容 E-1 同源，原文照錄。
LAB = "https://sites.google.com/view/linchiahuei/"
# 系主任照片取自同一名冊的個人頁 https://wwwndmc.ndmutsgh.edu.tw/DocDet/191/100010/1738/2969（376×516，2026-10-01 核對 200 image/jpeg）。
IMG_CHAIR = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/"
             "%E6%9E%97%E4%BD%B3%E6%85%A71130221.jpg")


def render():
    opening = statement(
        draft("系主任的話"),
        draft("系主任談護理學系為什麼這樣教，以及對每一位護生的期許。"),
    )

    portrait = split(
        photo(IMG_CHAIR, "護理學系主任林佳慧教授", "3/4"),
        "".join([
            p("護理學系主任　林佳慧教授"),
            p("國防醫學院醫學科學研究所護理組博士", muted=True),
            p("內外科護理、護理行政管理、慢性病護理、健康促進、運動訓練、心肺復健、智慧醫療", muted=True),
            p("電話：02-87923100分機18760　信箱：chlin@mail.ndmutsgh.edu.tw", muted=True),
            actions(text_link("林佳慧老師研究室網站", LAB)),
        ]),
        cols=(4, 8), align="start",
    )

    message = tape_surface(
        p(draft("【開場】向讀者問候，用一兩句話說出護理學系是什麼樣的地方。")),
        p(draft("【辦學理念】系主任重視的價值，以及學系如何把臨床照護、軍事訓練與實習放在同一段養成裡。")),
        p(draft("【學生期許】希望護生在四年裡長成什麼樣的護理人員：對病人、對團隊、對任務。")),
        p(draft("【給高中生與家長】對正在考慮軍護的高中生與家長說的一段話。")),
        p(draft("【署名】護理學系主任　林佳慧"), muted=True),
    )

    return page(
        opening,
        name_tape("系主任"),
        portrait,
        note("請三長提供系主任的話全文 400–600 字，內容包含辦學理念與學生期許；下方五段為結構草稿，收到原文後整段替換。"
             "姓名、職稱、學位、專長、電話、信箱與照片取自現行專任教師名冊個人頁（現職欄：國防醫學大學護理學院教授暨護理學系主任）。"),
        name_tape("系主任的話"),
        message,
        actions(text_link("學系特色與定位", L("dept:C-2-1")), text_link("教育目標與核心能力", L("dept:C-2-2"))),
        owner=META["owner"],
    )
