from components import (page, name_tape, statement, p, h4, text_link, actions, facts, bullets, split,
                        illo_slot, draft, note)
from links import L
from pages._en_inst_data import U_RULES, U_ETHICS, zh

META = {"id": "C-1", "slug": "curriculum", "title": "Curriculum", "owner": "院窗口", "site": "en_inst"}

# Written for international academic visitors (en-sites.md), not for applicants.
# Verified sources:
#   credit structure, Research Ethics Education, teaching-assistant requirement — 學生專區 unit/100181/6533
#   research milestones (supervisor, proposal defense, thesis defense) — the forms listed on the same page
#   graduate course titles — 114學年兼任老師名冊 (pages/E-1_faculty.py, ADJUNCT), translated here


def render():
    opening = "".join([
        statement(
            draft("Advanced practice and research, learned side by side."),
            draft("The master's curriculum combines advanced nursing courses in each track with research methods, "
                  "evidence-based nursing and a thesis. Military nursing runs through it."),
        ),
        actions(zh("inst:E-1")),
    ])

    themes = split(
        "".join([
            h4(draft("Advanced practice")),
            p(draft("Advanced courses and practicum in adult and gerontological, women's and children's, "
                    "and mental health nursing, and in the nurse practitioner role.")),
            h4(draft("Research and evidence")),
            p(draft("Research methods, data analysis and evidence-based nursing prepare every student to "
                    "complete a thesis.")),
            h4(draft("Military nursing")),
            p(draft("Advanced military nursing links graduate study to care in military and disaster settings.")),
        ]),
        illo_slot("Nurse researcher with a laptop and field notes (CocoMaterial, recolored)", "4/3", unit="inst"),
        cols=(7, 5), align="start",
    )

    credits = "".join([
        bullets([
            "Adult and Gerontological, Women's and Children's, and Mental Health Nursing tracks: "
            "27 compulsory credits + 6 elective credits = 33 credits.",
            "Nurse Practitioner track: 30 compulsory credits + 3 elective credits = 33 credits. Students who plan to "
            "sit the nurse practitioner licensing exam also take Advanced Nurse Practitioner Practicum III.",
        ]),
        p("Applies to students entering from the 2025–26 academic year.", muted=True),
    ])

    training = "".join([
        bullets([
            "Research Ethics Education: a required course in the first year (0 credits). Students who have not "
            "completed it may not sit the degree examination.",
            "Thesis supervision: each student applies for a thesis supervisor, then presents a research proposal "
            "at an oral examination before the final thesis defense.",
            "Teaching experience: full-time students funded by the military serve as teaching assistants for one year "
            "(at least 108 hours per academic year), taking part in the College's administration and clinical "
            "teaching.",
        ]),
        p(draft("Translated from the Institute's study regulations.") + "　"
          + text_link("Source (Chinese)", U_RULES), muted=True),
        p("The Institute's research ethics page provides Tri-Service General Hospital's procedure for obtaining "
          "the unit consent form required by its institutional review board, and for applying to collect data in "
          "the hospital's Department of Nursing.", muted=True),
        actions(text_link("Research ethics resources (Chinese)", U_ETHICS)),
    ])

    courses = "".join([
        p("Graduate courses taught in the 2025–26 academic year include:"),
        bullets([
            "Advanced Military Nursing",
            "Advanced Evidence-Based Nursing I and II",
            "Advanced Research Methods",
            "Advanced Data Analysis Methodology",
            "Advanced Mental Health Nursing I and II",
            "Advanced Nurse Practitioner Practicum I, II and III",
        ]),
        p(draft("Course titles translated from the 2025–26 teaching roster."), muted=True),
    ])

    interdisciplinary = "".join([
        p(draft("Students learn alongside clinicians at Tri-Service General Hospital, and faculty research draws on "
                "medicine, public health, data science and education.")),
    ])

    return page(
        opening,
        name_tape("Curriculum Themes"),
        themes,
        note("課程主題三段為草稿，請院窗口依課程地圖（研究生手冊 圖2-1-2）確認或改寫。"),
        name_tape("Credit Structure"),
        credits,
        name_tape("Research Training"),
        training,
        note("三總研究收案流程依研究所〈研究倫理專區〉所列「三總護理部申請人體試驗審議會計畫單位同意書及護理部研究計畫收案作業申請流程」改寫。"),
        name_tape("Selected Graduate Courses"),
        courses,
        note("課名譯自 114 學年兼任老師名冊中的「進階」課程，只列課名、不列授課教師。請院窗口提供：各學組正式課程清單與官方英文課名"
             "（分必修、選修、學分），收到後替換本段；未確認前請勿依印象增補課名。"),
        name_tape("Interdisciplinary Learning"),
        interdisciplinary,
        note("請院窗口提供跨領域學習的實例（例如與醫學系、公共衛生、資訊或三總各部門合開的課程、共同指導的論文）；"
             "上方文字為草稿。"),
        actions(text_link("Graduate Programs", L("en_inst:C")), text_link("Research Areas and Faculty",
                                                                         L("en_inst:D-1"))),
        owner=META["owner"],
    )
