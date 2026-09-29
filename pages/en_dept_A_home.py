from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, ribbon_bar,
                        split, unit_pair, feature_lead, feature_list, route_list, draft, note)
from links import L
from tokens import C

META = {"id": "A", "slug": "home", "title": "Department of Nursing", "owner": "院窗口", "site": "en_dept"}

# Structure mirrors pages/dept_A_home.py. Verified facts reused:
#   1947 founding, "country's first institution of higher nursing education" — 歷史沿革 unit/100010/6804
#   teaching hospital, 4-year programme, bachelor's degree, 8-week basic training — 115 正期班簡章 (pages/F_admissions.py)
#   educational aim — 學士班課程地圖 unit/100010/3642 (pages/dept_C-2-2_goals.py)


def render():
    opening = split(
        "".join([
            statement(
                draft("Educating nurses for military and civilian care since 1947."),
                draft("The Department of Nursing runs the undergraduate nursing programme of the College of Nursing, "
                      "National Defense Medical University, in Taipei. Students learn nursing, train as future officers, "
                      "and practise in hospital, community and military settings."),
            ),
            actions(button("Visit the Department", L("en_dept:G")),
                    text_link("About the Department", L("en_dept:B")),
                    text_link("中文", L("dept:A"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch(
            "Department of Nursing", "護理學系", unit="dept",
            illo=illo_slot("Student nurse at a bedside", "1/1",
                           unit="dept"),
            tab="College of Nursing", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    quick = ribbon_bar([
        ("Undergraduate Program", L("en_dept:C")),
        ("Simulation", L("en_dept:C-3")),
        ("Exchange", L("en_dept:E")),
        ("Faculty", L("en_dept:F")),
    ])

    program = feature_lead(
        "Four years, three settings",
        [
            p("The bachelor's programme lasts four years. New students first complete eight weeks of basic military "
              "training. The university's teaching hospital is Tri-Service General Hospital."),
            p(draft("Classroom learning, simulation and clinical practicum are planned as one pathway, "
                    "from basic nursing skills to care in military and disaster settings.")),
        ],
        illo_slot("Student and clinical teacher", "1/1", unit="dept"),
        unit="dept", href=L("en_dept:C"), link_label="The undergraduate program",
    )
    settings = feature_list([
        ("Hospital practicum",
         "Clinical courses take place at Tri-Service General Hospital, the university's teaching hospital.",
         None, "dept", "H"),
        ("Community practicum",
         draft("Students practise health education and home-based care in community settings."), None, "dept", "C"),
        ("Military nursing",
         "Military nursing is one of the thirteen core abilities every graduate is expected to develop.",
         None, "dept", "M"),
    ])

    aim = "".join([
        p("Our educational aim: to educate professionals with humanistic literacy and nursing competence "
          "who meet the needs of both the military and the civilian health care systems."),
        route_list([
            ("Overview and Learning Outcomes", draft("History, educational goals and the thirteen core abilities"),
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
            ("International Exchange", draft("Selected inbound and outbound exchange outcomes"), L("en_dept:E")),
        ], unit="dept"),
    ])

    family = unit_pair([
        ("college", "College of Nursing", "Faculty directory, research, visits", L("en:A")),
        ("inst", "Graduate Institute of Nursing", "Graduate programmes and research", L("en_inst:A")),
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
        actions(text_link("護理學系中文網站", L("dept:A"))),
        owner=META["owner"],
    )
