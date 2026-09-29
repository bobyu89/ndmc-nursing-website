from components import page, name_tape, statement, p, text_link, actions, unit_pair, facts, route_list, draft, note
from links import L
from pages._en_college_shared import zh

META = {"id": "C", "slug": "units", "title": "Academic Units", "owner": "院窗口", "site": "en_college"}

# Plain facts are faithful translations of verified text in pages/D_units.py:
#   lineage — 歷史沿革 unit/100010/6804; bachelor's length and credits — 學系學生專區 unit/100180/6681;
#   master's length, tracks and credits — 研究所學生專區 unit/100181/6533.
# Teaching hospital — pages/F_admissions.py (115 正期班簡章).
# C-1 and C-2 are menu links only: they open the Department and Institute English sites.


def render():
    opening = "".join([
        statement(
            draft("One college, two academic units."),
            draft("The Department of Nursing educates undergraduate students who become nurses and officers. "
                  "The Graduate Institute of Nursing offers advanced study and research to experienced nurses."),
        ),
        actions(zh("D")),
    ])

    units = unit_pair([
        ("dept", "Department of Nursing", "Undergraduate program", L("en_dept:A")),
        ("inst", "Graduate Institute of Nursing", "Graduate programs", L("en_inst:A")),
    ])

    lineage = "".join([
        p("The Department of Nursing traces its origin to the Senior Nursing Vocational Class founded by "
          "General Mei-Yu Chow in 1943. In 1947 General Chow established the Department of Nursing, the country's "
          "first institution of higher nursing education."),
        p("The Graduate Institute of Nursing was established in 1979 to meet the needs of nursing education and research, "
          "a pioneer of master's-level nursing education in Taiwan. The College of Nursing followed in 2025."),
        actions(text_link("Overview and History", L("en:B-2"))),
    ])

    dept = "".join([
        facts([
            ("Level", "Bachelor's degree"),
            ("Length", "Four years, including military training courses"),
            ("Credits", "At least 132, from academic year 2024–25"),
            ("Teaching hospital", "Tri-Service General Hospital"),
        ]),
        actions(text_link("Department of Nursing English site", L("en_dept:A")), zh("dept:A", "護理學系中文網站")),
    ])

    inst = "".join([
        facts([
            ("Levels", "Master's degree; " + draft("doctoral program")),
            ("Length", "Master's: two years, extendable by up to two years"),
            ("Tracks", "Adult and Gerontological Nursing; Maternal and Child Nursing; Mental Health Nursing; "
                                "Nurse Practitioner"),
            ("Credits", "Master's: at least 33, for students admitted from academic year 2025–26"),
        ]),
        note("研究所是否對外介紹博士班，中文頁仍待確認（組織圖虛線框、招生簡章已列博士班）；確認前英文版標待確認。"
             "碩士班分組：研究所學生專區列四組，組織圖列「臨床護理組／專科護理師組」兩組，請護理研究所統一英文說法。"),
        actions(text_link("Graduate Institute of Nursing English site", L("en_inst:A")), zh("inst:A", "護理研究所中文網站")),
    ])

    return page(
        opening,
        units,
        name_tape("One Origin"),
        lineage,
        name_tape("Department of Nursing", unit="dept"),
        dept,
        name_tape("Graduate Institute of Nursing", unit="inst"),
        inst,
        name_tape("Related Pages"),
        route_list([
            ("Program Overview", draft("The two levels side by side"), L("en:E-1")),
            ("Faculty Directory", draft("One faculty shared by both units"), L("en:D-1")),
            ("Research Highlights", draft("Military, trauma and disaster nursing and more"), L("en:D-2")),
        ]),
        owner=META["owner"],
    )
