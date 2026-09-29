from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, illo_slot, facts,
                        feature_lead, route_list, draft, note)
from links import L

META = {"id": "C", "slug": "program", "title": "Undergraduate Program", "owner": "課委會", "site": "en_dept"}

# Verified facts: 115 學年度軍事學校正期班甄選入學招生簡章 (via pages/F_admissions.py, pages/dept_D_admissions.py);
# aim from 學士班課程地圖 unit/100010/3642; simulation center use from 教學設備 unit/100010/1463 (pages/E-3_facilities.py).


def render():
    opening = "".join([
        statement(
            draft("One program for the ward, the community and the field."),
            draft("The Bachelor of Science in Nursing program combines nursing education with military training. "
                  "This page gives international colleagues a short map of how it is built."),
        ),
        actions(text_link("Curriculum", L("en_dept:C-1")), text_link("中文：課程", L("dept:F"))),
    ])

    at_a_glance = facts([
        ("Length", "4 years"),
        ("Degree", "Bachelor's degree in nursing, awarded by the Department of Nursing"),
        ("Basic training", "8 weeks of military basic training before nursing studies begin"),
        ("Teaching hospital", "Tri-Service General Hospital"),
        ("Educational aim", "Professionals with a grounding in the humanities and strong nursing competence for both the military "
                            "and the civilian health care systems"),
    ])

    shape = feature_lead(
        "Built around the person",
        [
            p("The curriculum is designed around five concepts: Person, Life span, Family, Nursing process and Dynamics."),
            p(draft("Students start with general education and basic medical sciences, move on to nursing care "
                    "across the life span, and finish in community and military settings.")),
        ],
        illo_slot("Student checking a manikin", "1/1", unit="dept"),
        unit="dept", href=L("en_dept:C-1"), link_label="Curriculum structure",
    )

    practice = split(
        "".join([
            p("The simulation center is used for advanced medical-surgical, advanced obstetric and pediatric, "
              "and critical care nursing courses, and for OSCE teaching in the bachelor's program."),
            p(draft("Clinical practicum then takes students into the teaching hospital, the community and "
                    "military nursing settings.")),
        ]),
        photo_slot("Students in the simulation center (4:3)", "4/3"),
        cols=(7, 5), align="start",
    )

    tasks = route_list([
        ("Curriculum", draft("Structure, course sequence and the core-competency map"), L("en_dept:C-1")),
        ("Clinical and Military Nursing Practicum", draft("Hospital, community and military nursing practicum"),
         L("en_dept:C-2")),
        ("Simulation and Learning Spaces", draft("Simulation center, demonstration ward and self-learning spaces"),
         L("en_dept:C-3")),
        ("Student Learning Outcomes", draft("What students achieve, told through photos and short stories"),
         L("en_dept:C-4")),
    ], unit="dept")

    return page(
        opening,
        name_tape("At a Glance"),
        at_a_glance,
        note("上表譯自《115 學年度軍事學校正期班甄選入學招生簡章》（修業 4 年、學士學位、入伍訓練八週、實習醫院三軍總醫院）"
             "與學士班課程地圖的教育宗旨。本頁對象為國外教育者，不放報名、名額與公費說明。"),
        name_tape("Curriculum Design"),
        shape,
        name_tape("From Simulation to Practice"),
        practice,
        name_tape("Explore the Program"),
        tasks,
        owner=META["owner"],
    )
