from components import page, name_tape, statement, p, split, photo_slot, actions, text_link, tape_surface, draft, note
from links import L
from pages._en_college_shared import zh, PROFILE

META = {"id": "B-1", "slug": "dean", "title": "Dean's Message", "owner": "三長", "site": "en_college"}

# Dean's name: pages/C-1_dean.py (曾雯琦院長, verbatim from unit/100010/1461).
# English name, title and education: official English profile /DocDetEn/191/100010/3351/4416.


def render():
    opening = "".join([
        statement(
            draft("A message from the Dean."),
            draft("The Dean on why the College educates military nurses, and where it is heading next."),
        ),
        actions(zh("C-1")),
    ])

    portrait = split(
        photo_slot("Dean Wen-Chii Tzeng (portrait 3:4)", "3/4"),
        "".join([
            p("<strong>Wen-Chii Tzeng</strong><br>Distinguished Professor and Dean, College of Nursing"),
            p("PhD, School of Nursing, University of California, San Francisco, USA<br>Specialty: Mental Health Nursing",
              muted=True),
            actions(text_link("Full profile", PROFILE + "4416")),
        ]),
        cols=(4, 8), align="start",
    )

    message = tape_surface(
        p(draft("[Opening] A greeting to international colleagues and one or two sentences on what kind of place the College is.")),
        p(draft("[Mission] The values the Dean holds, and how the College brings military nursing and clinical care "
                "into one education.")),
        p(draft("[Direction] Where the College is heading in teaching, research and international collaboration.")),
        p(draft("[Invitation] A word to partner institutions and visiting scholars.")),
        p(draft("Wen-Chii Tzeng, Dean, College of Nursing"), muted=True),
    )

    return page(
        opening,
        name_tape("The Dean"),
        portrait,
        name_tape("Dean's Message"),
        note("請三長提供院長的話英文定稿（約 300–400 字），寫給國外學者與合作院校，而非高中生與家長；"
             "若只有中文版，請院窗口安排翻譯後由院長確認。以上四段為結構草稿，收到原文後整段替換。"
             "院長英文姓名與職稱取自學校英文師資頁（DocDetEn/…/4416），請一併確認。"),
        message,
        actions(text_link("Overview and History", L("en:B-2")), text_link("Faculty Directory", L("en:D-1"))),
        owner=META["owner"],
    )
