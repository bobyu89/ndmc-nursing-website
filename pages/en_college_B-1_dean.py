from components import page, name_tape, statement, p, split, photo, actions, text_link, tape_surface, draft, note, todo
from links import L
from pages._en_college_shared import zh, PROFILE, DEAN_PHOTO

META = {"id": "B-1", "slug": "dean", "title": "Dean's Message", "owner": "三長", "site": "en_college"}

# Dean's name: pages/C-1_dean.py (曾雯琦院長, verbatim from unit/100010/1461).
# English name, title and education: official English profile /DocDetEn/191/100010/3351/4416.
# FAAN 2026: College news, 2026/07/14 (news/191/100010/1628), which gives the English title verbatim.


def render():
    opening = "".join([
        statement(
            draft("A message from the Dean."),
            draft("The Dean on why the College educates military nurses, and where it is heading next."),
        ),
        actions(zh("C-1")),
    ])

    portrait = split(
        photo(DEAN_PHOTO, "Dean Wen-Chii Tzeng", "3/4"),
        "".join([
            p("<strong>Wen-Chii Tzeng</strong><br>Distinguished Professor and Dean, College of Nursing"),
            p("PhD in Nursing, University of California, San Francisco, USA<br>Specialty: Mental health nursing",
              muted=True),
            p("Fellow of the American Academy of Nursing (FAAN), 2026", muted=True),
            actions(text_link("Dean's full profile and publications", PROFILE + "4416")),
        ]),
        cols=(4, 8), align="start",
    )

    # 全文收到前只有 todo（正式版不輸出），本段連同標題一起隱藏。
    message = todo("院長的話英文定稿約 300–400 字：問候國外學者、治院理念、發展方向、對合作院校的邀請，文末署名 Wen-Chii Tzeng, Dean（三長提供）")

    return page(
        opening,
        name_tape("The Dean"),
        portrait,
        *([name_tape("Dean's Message")] if message else []),
        note("請三長提供院長的話英文定稿（約 300–400 字），寫給國外學者與合作院校，而非高中生與家長；"
             "若只有中文版，請院窗口安排翻譯後由院長確認。收到原文後以 tape_surface 分段放入，文末署名 Wen-Chii Tzeng, Dean, College of Nursing。"
             "院長英文姓名與職稱取自學校英文師資頁（DocDetEn/…/4416），請一併確認。"),
        message,
        actions(text_link("Overview and History", L("en:B-2")), text_link("Faculty Directory", L("en:D-1"))),
        owner=META["owner"],
    )
