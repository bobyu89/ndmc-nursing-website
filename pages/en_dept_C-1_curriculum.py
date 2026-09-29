from components import (page, name_tape, statement, p, h4, bullets, text_link, actions, facts, illo_slot, split,
                        timeline, draft, note)
from links import L
from tokens import SITE

META = {"id": "C-1", "slug": "curriculum", "title": "Curriculum", "owner": "課委會", "site": "en_dept"}

# Verified (plain):
#   4 years, bachelor's degree, 8-week basic training — 115 正期班簡章 (pages/F_admissions.py)
#   five curriculum concepts — 學士班課程架構 unit/100010/1492 (pages/dept_C-2-1_identity.py)
#   13 core abilities, core-ability/course matrix PDF — 學士班課程地圖 unit/100010/3642 (pages/dept_C-2-2_goals.py)
# Drafted: credit totals and the year-by-year military component come from the English orphan page
#   uniten/100010/3396 (Bachelor Curriculum); not yet matched against the current Chinese 學分表.
U_MATRIX = SITE + "/files/web/192/file_up/100010/8644/@學士班核心能力與課程關聯圖1101012.pdf"


def render():
    opening = statement(
        draft("A four-year curriculum mapped to thirteen core competencies."),
        draft("General education, basic medical sciences and nursing courses are sequenced so that each year "
              "builds on the last, alongside military education."),
    )

    design = split(
        "".join([
            p("The whole curriculum is designed around five concepts: Person, Life span, Family, Nursing process "
              "and Dynamics."),
            p("Every course is linked to one or more of the program's thirteen core competencies, from humanistic "
              "care and evidence-based nursing to military nursing and lifelong learning."),
            actions(text_link("Core competencies and course map (PDF, Chinese)", U_MATRIX)),
        ]),
        illo_slot("Curriculum map: courses linked to core competencies (redrawn in English)", "4/3", unit="dept"),
        cols=(7, 5), align="start",
    )

    structure = "".join([
        facts([
            ("Length", "4 years"),
            ("Total", draft("At least 136 credits to graduate")),
            ("Compulsory", draft("95 credits")),
            ("General", draft("39 credits of general education and electives")),
            ("Electives", draft("2 credits of professional electives")),
            ("Military", draft("Military courses carry no credit")),
        ]),
        note("學分數取自英文孤兒頁 uniten/100010/3396（Bachelor Curriculum），與中文現行網站尚未核對；"
             "該頁另寫「Military courses (no credit): 8 credits」前後矛盾，本頁暫只寫 Non-credit。"
             "請課委會依現行學分表（中文站 F-1-2，需分期班呈現）確認：畢業最低學分、必修／通識選修／專業選修學分，"
             "以及軍事課程是否計學分；確認後拿掉待確認標記。"),
    ])

    years = timeline([
        ("Year 1", draft("Entry"),
         draft("Enlistment education, basic training and physical training."), "dept"),
        ("Year 2", draft("Service and skills"),
         draft("Military courses on campus, liberal arts, summer training with OSCE, and service learning."), "dept"),
        ("Year 3", draft("Professional training"),
         draft("Professional training in emergency, operating room and intensive care settings; health promotion; "
               "project-based education."), "dept"),
        ("Year 4", draft("Commitment"),
         draft("Patriotic education before commissioning."), "dept"),
    ])

    military = "".join([
        p("New students complete eight weeks of military basic training before starting nursing studies."),
        p(draft("Military nursing education runs alongside the nursing curriculum in all four years, "
                "totaling 1,228 hours. Its main components by year:")),
        years,
        note("「1,228 hours」與逐年軍陣護理教育內容取自英文孤兒頁 uniten/100010/3396，屬舊資料；"
             "請課委會依現行課程規劃（中文站 F-1-1）核對，並補上每一學年的主要護理課程（中文課程架構目前為圖片，無法轉錄）。"),
    ])

    return page(
        opening,
        name_tape("Curriculum Design"),
        design,
        note("課程地圖圖檔為中文；請課委會決定是否提供英文版課程地圖（圖或表），完成後替換上方插圖預留框。"),
        name_tape("Credits"),
        structure,
        name_tape("Military Education"),
        military,
        h4("Related pages"),
        actions(text_link("Clinical and Military Nursing Practicum", L("en_dept:C-2")),
                text_link("Simulation and Learning Spaces", L("en_dept:C-3")),
                text_link("中文：課程資訊", L("dept:F-1"))),
        owner=META["owner"],
    )
