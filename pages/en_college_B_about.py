from components import page, name_tape, statement, p, route_list, actions, text_link, tape_surface, draft
from links import L
from pages._en_college_shared import zh

META = {"id": "B", "slug": "about", "title": "About the College", "owner": "院窗口", "site": "en_college"}

# Origin paragraph: faithful translation of the verbatim 歷史沿革 text in pages/C_about.py (unit/100010/6804).
# Romanisation "General Mei-Yu Chow" follows the official English History & Vision page (uniten/100010/3353).


def render():
    opening = "".join([
        statement(
            draft("From one nursing class to a college of nursing."),
            draft("The College of Nursing at National Defense Medical University educates military nurses "
                  "and oversees the Department of Nursing and the Graduate Institute of Nursing. "
                  "Start here to learn where the College came from and how it is organized."),
        ),
        actions(zh("C")),
    ])

    origin = tape_surface(
        p("The College's Department of Nursing traces its origin to the Senior Nursing Vocational Class in Jiangwan, "
          "Shanghai, founded by General Mei-Yu Chow in 1943. It admitted junior high school graduates for a course of "
          "four and a half years and was the earliest vocational training program for nurses in the country."),
        p("In 2025 the College of Nursing was established, becoming a pioneer in advancing higher nursing education in Taiwan."),
        actions(text_link("Overview and History", L("en:B-2"))),
    )

    routes = route_list([
        ("Dean's Message", draft("The Dean on the College's mission and direction"), L("en:B-1")),
        ("Overview and History", draft("Who we are, military nursing, our emblem and our timeline since 1943"), L("en:B-2")),
        ("Organization", draft("The College, its two academic units and its committees"), L("en:B-3")),
    ])

    return page(
        opening,
        name_tape("Where We Began"),
        origin,
        name_tape("About the College"),
        routes,
        name_tape("Academic Units"),
        route_list([
            ("Department of Nursing", draft("Undergraduate nursing education (English site)"), L("en_dept:A")),
            ("Graduate Institute of Nursing", draft("Graduate education and research (English site)"), L("en_inst:A")),
        ]),
        owner=META["owner"],
    )
