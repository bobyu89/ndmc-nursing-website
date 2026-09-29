from components import (page, name_tape, statement, p, text_link, actions, split, illo_slot, feature_list,
                        route_list, draft, note)
from links import L
from pages._en_college_shared import zh, mark

META = {"id": "E", "slug": "programs", "title": "Academic Programs", "owner": "院窗口", "site": "en_college"}

# For international academic visitors: what the programs are, not how to apply (no international admissions).
# Plain facts: pages/D_units.py (學系／研究所學生專區) and pages/F_admissions.py (115 正期班簡章:
# 8-week basic training, teaching hospital). Doctoral program stays draft (see pages/F_admissions.py note).


def render():
    opening = "".join([
        statement(
            draft("Two levels of nursing education in one college."),
            draft("The College educates nurses from the bachelor's degree to graduate study. "
                  "These pages describe the programs for academic partners and visitors; they are not an admissions guide."),
        ),
        actions(text_link("Program Overview", L("en:E-1")), zh("D")),
    ])

    levels = feature_list([
        ("Bachelor's program",
         "Offered by the Department of Nursing. A four-year program that includes military training courses; "
         "students also complete eight weeks of basic military training. "
         + text_link("Department of Nursing", L("en_dept:C")),
         None, "dept", mark("graduation-cap")),
        ("Master's program",
         "Offered by the Graduate Institute of Nursing. Two years, extendable by up to two years, in four tracks: "
         "adult and gerontological nursing, maternal and child nursing, mental health nursing, and nurse practitioner. "
         + text_link("Graduate Institute of Nursing", L("en_inst:C")),
         None, "inst", mark("book")),
        ("Doctoral program",
         draft("A doctoral program in nursing is offered by the Graduate Institute of Nursing."),
         None, "college", mark("flask")),
    ])

    highlights = split(
        "".join([
            p("The university's teaching hospital is Tri-Service General Hospital."),
            p(draft("Across both levels, students learn in the classroom, in simulation and in clinical practice, "
                    "with military nursing and trauma and disaster nursing as distinctive strengths.")),
            actions(text_link("Facilities", L("en:D-3")), text_link("Research Highlights", L("en:D-2"))),
        ]),
        illo_slot("Nursing students in a simulation ward (CocoMaterial, recolored)", "4/3", unit="dept"),
        cols=(7, 5),
    )

    return page(
        opening,
        note("英文站不做國際學位招生：不放報名方式、學費、簽證與表單。博士班能否對外介紹，待院窗口與護理研究所確認（見中文招生專區備註）。"),
        name_tape("Programs"),
        levels,
        name_tape("Learning Across Settings"),
        highlights,
        name_tape("Learn More"),
        route_list([
            ("Program Overview", draft("Bachelor's and master's programs side by side"), L("en:E-1")),
            ("Visiting Scholars", draft("Non-degree academic visits for faculty and researchers"), L("en:G-2")),
            ("Academic Visits", draft("Short visits by partner delegations"), L("en:G-1")),
        ]),
        owner=META["owner"],
    )
