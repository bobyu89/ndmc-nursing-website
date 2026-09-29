from components import (page, name_tape, statement, p, bullets, text_link, actions, split, photo_slot, tape_surface,
                        feature_list, draft, note)
from links import L
from tokens import SITE

META = {"id": "F-1-1", "slug": "plan", "title": "課程規劃", "owner": "院窗口", "site": "dept"}

# 沿用＆美化：文字逐字取自現行「課程規劃」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/1492
# （標題「學士班課程架構」＋一段說明＋一張架構圖；頁面更新日期 2025-05-13；2026-09-29 擷取）。
# 原本一整段拆成幾段、按學習階段排開，字句不改。「圖上寫了什麼」是把架構圖上的文字照抄成網頁文字。
U_PAGE = SITE + "/unit/100010/1492"


def render():
    opening = statement(
        draft("從認識人開始，一路學到照顧軍民的健康。"),
        draft("護理學系的四年課程，是繞著「人」一層一層往外排的：先學通識與基礎醫學，再學護理專業，最後走進社區與軍陣。"),
    )

    concept = tape_surface(
        p("整個課程設計與安排根據人（Person）、生命歷程（Life span）、家庭（Family）、護理過程（Nursing process）"
          "及動力變化（Dynamics）等概念。"),
        p("透過全人為主體，其所處的「家庭」與「社會文化」環境為客體的架構，以生命歷程的階段及護理過程的方式來規劃安排課程及設計教學與實習的內容。"),
    )

    stages = feature_list([
        ("通識教育",
         "因此在四年的修業期間，首先接受通識教育課程，經由醫療與社會、藝術賞析、溝通、公民意識、自然科學等陶冶，"
         "培養學生對他人和自然環境的關注及興趣。",
         None, "dept", "通"),
        ("基礎醫學教育",
         "其次是接受健康與疾病的基礎醫學教育，使學生具備從事護理專業所應有的基本生理、心理、社會及靈性之生物醫學和行為科學之知識。",
         None, "dept", "基"),
        ("專業基礎教育",
         "在專業基礎教育中，學生能認識生命歷程中各個發展階段，並且學習符合服務對象健康需求的一般照護技能。",
         None, "dept", "專"),
        ("專業進階教育",
         "在專業進階教育中，學生能以家庭為中心的理念，運用護理過程，發揮專業護理的知識與技能，以解決服務對象現存或潛在的健康問題。",
         None, "dept", "進"),
        (draft("社會、社區與軍陣"),
         "最後，學生能瞭解服務對象所處的社會、社區、軍陣體系的環境脈絡，提供符合其需求與期待的專業護理。",
         None, "dept", "軍"),
    ])

    figure = "".join([
        split(
            photo_slot("學士班課程架構圖（沿用現行課程規劃頁的圖）", "7/8"),
            "".join([
                p(f"<strong>{draft('圖上寫了什麼')}</strong>"),
                bullets([
                    "通識教育課程：文哲藝術、外國語文、醫療與社會、法政心理",
                    "基礎醫學課程：微免、藥理、病理；解剖、生理、有機、生化",
                    "專業基礎課程：身體評估、基本護理、健康促進與營養、護學、人類發展學",
                    "專業核心課程：產科護理學、內外科護理學、兒科護理學、精神衛生護理學、社區衛生護理學、軍陣護理",
                    "以家庭為中心",
                    "軍護教育暨實習課程",
                ]),
            ]),
            cols=(5, 7), align="start",
        ),
        note("現行頁面的架構圖是直接嵌在頁面裡的圖片（data URI），不是獨立檔案，找不到檔案路徑。"
             "上線時請院窗口從現行頁面另存該圖、上傳到 CMS 後換進左側照片位置，並把右側「圖上寫了什麼」當作圖的替代文字（無障礙需要）。"
             "右側文字是照圖抄錄，請課委會核對。"),
    ])

    return page(
        opening,
        name_tape("學士班課程架構"),
        concept,
        name_tape("四年怎麼走"),
        stages,
        p(draft("以上文字摘自現行「課程規劃」頁（更新日期 2025-05-13）。") + "　" + text_link("現行課程規劃頁", U_PAGE),
          muted=True),
        name_tape("課程架構圖"),
        figure,
        name_tape("接著看"),
        actions(text_link("各期班學分表", L("dept:F-1-2")), text_link("課程地圖", L("dept:F-1-3")),
                text_link("教育目標與核心能力", L("dept:C-2-2"))),
        owner=META["owner"],
    )
