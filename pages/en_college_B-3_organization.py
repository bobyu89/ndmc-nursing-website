from components import page, name_tape, statement, p, org_tree, bullets, actions, text_link, draft, note
from links import L
from pages._en_college_shared import zh

META = {"id": "B-3", "slug": "organization", "title": "Organization", "owner": "哲君", "site": "en_college"}

# Structure and names: faithful translation of pages/C-4_organization.py (組織架構 unit/100010/4125).
# Committee names are our translations; the College has no published English names for them yet.


def render():
    opening = "".join([
        statement(
            draft("One college, two academic units."),
            draft("The College of Nursing oversees the Department of Nursing and the Graduate Institute of Nursing. "
                  "College affairs are run by the College Council and six committees."),
        ),
        actions(zh("C-4")),
    ])

    chart = org_tree("College of Nursing", [
        ("College Council", [
            "College Development Committee",
            "College Faculty Evaluation Committee",
            "College Faculty Development Committee",
            "College Curriculum Committee",
            "College Student Affairs Committee",
            "College Library, Equipment and Welfare Committee",
        ], "college"),
        ("Graduate Institute of Nursing", [
            "Doctoral program",
            "Master's program: Clinical Nursing track",
            "Master's program: Nurse Practitioner track",
        ], "inst"),
        ("Department of Nursing", [draft("Undergraduate program")], "dept"),
    ])

    rules = bullets([
        "Charter of the College of Nursing, National Defense Medical University",
        "Regulations of the College Development Committee",
        "Regulations of the College Faculty Development Committee",
        "Regulations of the College Curriculum Development Committee",
        "Regulations of the College Student Affairs Committee",
        "Regulations of the College Library, Equipment and Welfare Committee",
    ])

    return page(
        opening,
        name_tape("Organization Chart"),
        chart,
        note("委員會英文名稱為本站暫譯（院務會議 College Council；院圖儀福利委員會 Library, Equipment and Welfare Committee 等），"
             "請哲君確認或提供校方既有英文名稱。中文頁待確認事項（博士班虛線框、院課程委員會名稱）確認後，英文版同步修改。"),
        name_tape("Charter and Regulations"),
        p(draft("The College's charter and committee regulations are published in Chinese only.")),
        rules,
        actions(text_link("Documents (in Chinese)", L("H-3"))),
        name_tape("Academic Units"),
        actions(text_link("Department of Nursing", L("en_dept:A")), text_link("Graduate Institute of Nursing", L("en_inst:A"))),
        owner=META["owner"],
    )
