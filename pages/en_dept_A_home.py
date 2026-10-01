from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, ribbon_bar,
                        split, unit_pair, feature_lead, feature_list, route_list, draft, note)
from links import L
from tokens import C

META = {"id": "A", "slug": "home", "title": "Department of Nursing", "owner": "院窗口", "site": "en_dept"}

# Structure mirrors pages/dept_A_home.py. Verified facts reused:
#   1947 founding, "country's first institution of higher nursing education" — 歷史沿革 unit/100010/6804
#   teaching hospital, 4-year program, bachelor's degree, 8-week basic training — 115 正期班簡章 (pages/F_admissions.py)
#   educational aim — 學士班課程地圖 unit/100010/3642 (pages/dept_C-2-2_goals.py)
#   community practicum content and sites — pages/dept_F-2-2_community.py (學生手冊〈臨床實習〉與表五)


def render():
    opening = split(
        "".join([
            statement(
                draft("Educating nurses for military and civilian care since 1947."),
                draft("The Department of Nursing runs the undergraduate nursing program of the College of Nursing, "
                      "National Defense Medical University, in Taipei. Students learn nursing, train as future officers, "
                      "and practice in hospital, community and military settings."),
            ),
            actions(button("Visit the Department", L("en_dept:G")),
                    text_link("About the Department", L("en_dept:B"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch(
            "Department of Nursing", "護理學系", unit="dept",
            illo=illo_slot("Student nurse at a bedside", "1/1",
                           unit="dept"),
            tab="College of Nursing", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    # Audience router: each ribbon is a reader; the sub-line says what is behind it. The Chinese site link
    # lives here only (no separate 中文 links in the opening or at the foot of the page).
    quick = ribbon_bar([
        ("Partner schools", L("en_dept:C"), "Four-year program"),
        ("Nurse educators", L("en_dept:F"), "Who teaches here"),
        ("Exchange students", L("en_dept:E"), "Exchange stories"),
        ("中文", L("dept:A"), "護理學系中文網站"),
    ])

    program = feature_lead(
        "Four years, three settings",
        [
            p("The bachelor's program lasts four years. New students first complete eight weeks of basic military "
              "training."),
            p(draft("Classroom learning, simulation and clinical practicum are planned as one pathway, "
                    "from basic nursing skills to care in military and disaster settings.")),
        ],
        illo_slot("Student and clinical teacher", "1/1", unit="dept"),
        unit="dept", href=L("en_dept:C-2"), link_label="Clinical and Military Nursing Practicum",
    )
    settings = feature_list([
        ("Hospital practicum",
         "Clinical courses take place at Tri-Service General Hospital, the university's teaching hospital.",
         None, "dept", "H"),
        ("Community practicum",
         "Community assessment and planning, home visits and case management, and group health education, "
         "mainly at Taipei City district health centers and Tri-Service General Hospital.", None, "dept", "C"),
        ("Military nursing",
         "Military nursing is one of the thirteen core competencies every graduate is expected to develop.",
         None, "dept", "M"),
    ])

    aim = "".join([
        p("Our educational aim: to educate professionals with a grounding in the humanities and strong nursing competence, "
          "ready to meet the needs of both the military and the civilian health care systems."),
        route_list([
            ("Overview and Learning Outcomes", draft("History, educational goals and the thirteen core competencies"),
             L("en_dept:B-2")),
            ("Student Learning Outcomes", draft("What students do in courses, simulation and practicum"),
             L("en_dept:C-4")),
            ("Campus Experience", draft("Student life and the military nursing context"), L("en_dept:D")),
        ], unit="dept"),
    ])

    news = "".join([
        note("首頁為靜態 HTML，無法自動帶入消息；以英文消息頁導流。英文消息只放教學創新、實習亮點、學生成就、交流成果，"
             "不放招生與校內行政公告。"),
        route_list([
            ("News", draft("Teaching innovation, practicum highlights, student achievements and exchange outcomes"),
             L("en_dept:H")),
        ], unit="dept"),
    ])

    family = unit_pair([
        ("college", "College of Nursing", "Faculty directory, research, visits", L("en:A")),
        ("inst", "Graduate Institute of Nursing", "Graduate programs and research", L("en_inst:A")),
    ])

    return page(
        opening,
        quick,
        name_tape("The Program"),
        program,
        settings,
        name_tape("Learning Outcomes"),
        aim,
        name_tape("News"),
        news,
        name_tape("College and Institute"),
        family,
        owner=META["owner"],
    )
