from components import page, name_tape, statement, p, split, photo, actions, text_link, tape_surface, draft, note, todo
from links import L

META = {"id": "B-1", "slug": "chair", "title": "Chair's Message", "owner": "三長", "site": "en_dept"}

# Chair's name, rank, role, degree and specialties: 專任教師名冊 Doclist/191/100010/1738 (via pages/dept_C-1_chair.py).
LAB = "https://sites.google.com/view/linchiahuei/"
# Portrait: same file as the Chinese page (DocDet/191/100010/1738/2969), checked 200 image/jpeg on 2026-10-01.
IMG_CHAIR = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/"
             "%E6%9E%97%E4%BD%B3%E6%85%A71130221.jpg")


def render():
    opening = statement(
        draft("A message from the Chair"),
        draft("The Chair of the Department of Nursing on how we educate nurses, and what we hope every student becomes."),
    )

    portrait = split(
        photo(IMG_CHAIR, "Portrait of the Chair of the Department of Nursing", "3/4"),
        "".join([
            p(draft("Professor Chia-Huei Lin") + "<br>Chair, Department of Nursing"),
            p(draft("PhD in Nursing, Graduate Institute of Medical Sciences, National Defense Medical Center"),
              muted=True),
            p("Medical-surgical nursing, nursing administration and management, chronic illness care, health promotion, "
              "exercise training, cardiopulmonary rehabilitation, smart health care.", muted=True),
            actions(text_link("Professor Lin's research website", LAB)),
        ]),
        cols=(4, 8), align="start",
    )

    # 全文收到前只有 todo（正式版不輸出），本段連同標題一起隱藏。
    message = todo("系主任的話英文版 300–450 字：問候國外同儕、教育方式（臨床、軍事訓練與實習）、對學生的期許、合作邀請，文末署名（三長提供）")

    return page(
        opening,
        name_tape("The Chair"),
        portrait,
        note("請三長確認：① 系主任英文姓名拼法（暫依研究室網址 linchiahuei 寫作 Chia-Huei Lin）與英文職稱；"
             "② 學位英文寫法（中文原文：國防醫學院醫學科學研究所護理組博士）。照片已沿用中文名冊個人頁的照片。"
             "專長一行譯自專任教師名冊。"),
        *([name_tape("Message"), message] if message else []),
        note("請三長提供系主任的話英文版（300–450 字，對象為國外護理教育者與合作院校，不寫招生內容）。"
             "若只有中文版，請提供中文原文，由國際事務協助翻譯；收到後以 tape_surface 分段放入，文末署名 Chair, Department of Nursing。"),
        actions(text_link("Overview and Learning Outcomes", L("en_dept:B-2")),
                text_link("中文版：系主任的話", L("dept:C-1"))),
        owner=META["owner"],
    )
