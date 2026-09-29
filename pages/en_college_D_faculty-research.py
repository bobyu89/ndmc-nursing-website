from components import (page, name_tape, statement, p, button, text_link, actions, split, photo_slot, illo_slot,
                        bullets, route_list, draft, note)
from links import L
from pages._en_college_shared import zh

META = {"id": "D", "slug": "faculty-research", "title": "Faculty and Research", "owner": "院窗口", "site": "en_college"}

# Follows pages/E_resources.py. Facility names: pages/E-3_facilities.py (教學設備 unit/100010/1463).


def render():
    opening = "".join([
        statement(
            draft("One faculty, shared by both units."),
            draft("The Department of Nursing and the Graduate Institute of Nursing share one faculty, one research "
                  "community and one set of teaching spaces. The College keeps them together on these pages."),
        ),
        actions(button("Faculty Directory", L("en:D-1")), text_link("Research Highlights", L("en:D-2")), zh("E")),
    ])

    faculty = split(
        "".join([
            p(draft("Every full-time faculty member with rank, role, degree and research interests, "
                    "linked to an official English profile with publications and contact details.")),
            actions(text_link("Faculty Directory", L("en:D-1"))),
        ]),
        photo_slot("College of Nursing faculty group photo", "4/3"),
        cols=(7, 5),
    )

    research = split(
        "".join([
            p(draft("Military nursing and trauma and disaster nursing are at the core of our research, alongside mental "
                    "health, chronic illness care, sleep and health promotion.")),
            actions(text_link("Research Highlights", L("en:D-2")), text_link("Institute research", L("en_inst:D"))),
        ]),
        illo_slot("Research discussion (CocoMaterial, recolored)", "4/3", unit="inst"),
        cols=(7, 5), reverse=True,
    )

    facilities = split(
        "".join([
            p(draft("Students practice in simulated wards and scenarios before they go to the bedside.")),
            bullets(["Simulation Center", "Demonstration Classroom", "Demonstration Ward",
                     "Smart Interactive Nursing Self-Learning Classroom"]),
            actions(text_link("Facilities", L("en:D-3"))),
        ]),
        photo_slot("Demonstration Ward", "4/3"),
        cols=(7, 5),
    )

    return page(
        opening,
        name_tape("Faculty"),
        faculty,
        name_tape("Research", unit="inst"),
        research,
        name_tape("Facilities", unit="dept"),
        facilities,
        note("三張圖片與中文「學術資源」頁共用：全院教師合照、研究情境插圖、示範實習病房照片。"),
        name_tape("Related Pages"),
        route_list([
            ("Visiting Scholars", draft("Non-degree research and teaching visits"), L("en:G-2")),
            ("Collaboration Contact", draft("One contact point for research collaboration"), L("en:G-3")),
        ]),
        owner=META["owner"],
    )
