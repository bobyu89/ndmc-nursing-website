from components import (page, name_tape, statement, p, button, text_link, actions, split, photo_slot, feature_list,
                        draft, note)
from links import L

META = {"id": "F", "slug": "faculty", "title": "Faculty", "owner": "院窗口", "site": "en_dept"}

# Teaching areas summarize the specialties listed on the full-time faculty roster
# (Doclist/191/100010/1738, via pages/E-1_faculty.py); practicum teaching from the 114學年兼任老師名冊
# (unit/100010/1470). No names or counts are repeated here: the College Faculty Directory is the single source.


def render():
    opening = "".join([
        statement(
            draft("Teachers who practice, research and teach."),
            draft("Department courses are taught by the full-time faculty of the College of Nursing, together with "
                  "adjunct clinical instructors who guide students in practicum."),
        ),
        actions(button("College Faculty Directory", L("en:D-1")), text_link("中文版：師資陣容", L("E-1"))),
    ])

    areas = feature_list([
        ("Adult and critical care",
         "Medical-surgical nursing, critical care, emergency nursing, cardiovascular care, burn care and "
         "cardiopulmonary rehabilitation.", None, "dept", "A"),
        ("Women, children and families",
         "Obstetric and pediatric nursing, premature infant care, and children with cancer and their families.",
         None, "dept", "F"),
        ("Mental health",
         "Mental health and psychiatric nursing, stress and sleep, and digital mental health monitoring.",
         None, "dept", "M"),
        ("Community, older adults and palliative care",
         "Community and occupational health nursing, gerontological care, health promotion, hospice and "
         "palliative care.", None, "dept", "C"),
        ("Military, disaster and trauma nursing",
         "Military nursing, disaster nursing and traumatic brain injury.", None, "dept", "D"),
    ])

    practicum = split(
        "".join([
            p("Adjunct instructors listed in the college's 2025–26 roster teach many of the clinical practicum "
              "courses, including fundamentals, medical-surgical, obstetric, pediatric, mental health and "
              "community health nursing practicum."),
            p(draft("They bring current clinical practice into the program and supervise students on the wards.")),
        ]),
        photo_slot("Clinical instructor with students on a ward (4:3)", "4/3"),
        cols=(7, 5), align="start",
    )

    return page(
        opening,
        name_tape("Teaching and Research Areas"),
        areas,
        note("五組教學領域由學院專任教師名冊的「專長學科」歸納而成，未列任何姓名或人數；分組方式請院窗口確認。"
             "個別老師的英文姓名、職稱、研究興趣與代表著作，統一放在學院英文 Faculty Directory（en:D-1），本頁不重複。"),
        name_tape("Clinical Instructors"),
        practicum,
        name_tape("Full Profiles"),
        p("Names, titles, research interests and selected publications of every faculty member are kept in one place: "
          "the Faculty Directory on the College of Nursing English site."),
        actions(text_link("Chair's Message", L("en_dept:B-1")),
                text_link("Graduate Institute of Nursing", L("en_inst:A"))),
        owner=META["owner"],
    )
