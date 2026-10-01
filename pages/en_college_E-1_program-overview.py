from components import page, name_tape, statement, p, h4, text_link, actions, split, facts, route_list, draft, note
from links import L
from pages._en_college_shared import zh

META = {"id": "E-1", "slug": "program-overview", "title": "Program Overview", "owner": "院窗口", "site": "en_college"}

# Plain facts are faithful translations of verified text:
#   bachelor's length, military training courses, 132 credits — pages/D_units.py (學系學生專區 unit/100180/6681)
#   8-week basic training, bachelor's degree, teaching hospital — pages/F_admissions.py (115 正期班簡章)
#   master's length, tracks, 33 credits — pages/D_units.py (研究所學生專區 unit/100181/6533)
#   founding years — pages/C-3_history.py
# No application instructions, fees, visas or forms on this page.


def render():
    opening = "".join([
        statement(
            draft("The bachelor's and master's programs, side by side."),
            draft("A quick comparison for partner institutions and visiting faculty. For course details, "
                  "follow the links to the Department and Institute sites."),
        ),
        actions(zh("D")),
    ])

    bachelor = "".join([
        h4("Bachelor's program"),
        facts([
            ("Offered by", "Department of Nursing (since 1947)"),
            ("Length", "Four years, including military training courses"),
            ("Basic training", "Eight weeks of basic military training"),
            ("Credits", "At least 132, from academic year 2024–25"),
            ("Degree", "Bachelor's degree"),
            ("Clinical", "Tri-Service General Hospital, the university's teaching hospital"),
        ]),
        actions(text_link("Curriculum", L("en_dept:C-1"))),
    ])

    master = "".join([
        h4("Master's program"),
        facts([
            ("Offered by", "Graduate Institute of Nursing (since 1979)"),
            ("Length", "Two years, extendable by up to two years"),
            ("Tracks", "Adult and Gerontological Nursing; Maternal and Child Nursing; Mental Health Nursing; "
                       "Nurse Practitioner"),
            ("Credits", "At least 33, for students admitted from academic year 2025–26"),
            ("Degree", "Master's degree"),
            ("Research", draft("Students complete a thesis")),
        ]),
        actions(text_link("Curriculum", L("en_inst:C-1"))),
    ])

    return page(
        opening,
        name_tape("At a Glance"),
        split(bachelor, master, cols=(6, 6), align="start"),
        note("碩士班學位論文一項現行網站未明寫（中文「學術單位」頁已拿掉此句），請護理研究所確認。"
             "學分數以入學學年度為準；新學年度規定改變時，請學系與研究所同步更新中英文。"),
        name_tape("Doctoral Program", unit="inst"),
        p(draft("The Graduate Institute of Nursing also offers a doctoral program. Details will be added once confirmed.")),
        note("博士班說明待院窗口與護理研究所確認能否對外介紹後再寫（研究方向、修業年限）。"),
        name_tape("Program Sites"),
        route_list([
            ("Department of Nursing", draft("Undergraduate program, curriculum and practicum"), L("en_dept:C")),
            ("Graduate Institute of Nursing", draft("Graduate programs and curriculum"), L("en_inst:C")),
            ("Visit and Collaborate", draft("Academic visits and visiting scholars"), L("en:G")),
        ]),
        owner=META["owner"],
    )
