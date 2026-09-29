from components import page, name_tape, statement, p, split, photo_slot, actions, text_link, tape_surface, draft, note
from links import L

META = {"id": "C-1", "slug": "chair", "title": "系主任的話", "owner": "三長", "site": "dept"}

# 系主任姓名、職級、職務、學位、專長與研究室連結取自現行「專任教師」名冊
# （https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100010/1738，列於「系所主管」），與學院師資陣容 E-1 同源，原文照錄。
LAB = "https://sites.google.com/view/linchiahuei/"


def render():
    opening = statement(
        draft("系主任的話"),
        draft("系主任談護理學系為什麼這樣教，以及對每一位護生的期許。"),
    )

    portrait = split(
        photo_slot("系主任照片（直式 3:4）", "3/4"),
        "".join([
            p("護理學系主任　林佳慧教授"),
            p("國防醫學院醫學科學研究所護理組博士", muted=True),
            p("內外科護理、護理行政管理、慢性病護理、健康促進、運動訓練、心肺復健、智慧醫療", muted=True),
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
        note("請三長提供：① 確認系主任姓名與職稱（現行專任教師名冊「系所主管」列林佳慧教授，職務為護理學系主任；"
             "學位與專長一行同名冊，請確認是否沿用）；② 系主任直式照片（3:4）；"
             "③ 系主任的話全文 400–600 字，內容包含辦學理念與學生期許。下方五段為結構草稿，收到原文後整段替換。"),
        name_tape("系主任的話"),
        message,
        actions(text_link("學系特色與定位", L("dept:C-2-1")), text_link("教育目標與核心能力", L("dept:C-2-2"))),
        owner=META["owner"],
    )
