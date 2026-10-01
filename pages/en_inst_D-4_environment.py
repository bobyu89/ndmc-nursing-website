from components import (page, name_tape, statement, p, h4, text_link, actions, split, photo, facts, bullets,
                        draft, note)
from links import L
from pages._en_inst_data import name, U_ETHICS, zh, IMG_SIM_CENTER

META = {"id": "D-4", "slug": "environment", "title": "Research Environment", "owner": "教發、圖儀", "site": "en_inst"}

# Facilities translated from the College's current 教學設備 page unit/100010/1463 (pages/E-3_facilities.py);
# observation room and graduate classrooms from the old college English page uniten/100010/867 (undated → draft).
# Simulation-center photo: 虛擬中心.png on the same 教學設備 page. Ward bed count conflicts between the two pages
# (教學設備: 15 general beds; uniten/100010/867: 12 beds + 2 examination beds) → draft.
# Hospital posts from the official English faculty profiles; IRB procedure from 研究倫理專區 unit/100181/6794.
# Method list: each method is named in the listed faculty member's profile specialty, project titles or papers.


def render():
    opening = "".join([
        statement(
            draft("Research close to the ward."),
            draft("Our faculty work between the campus in Neihu, Taipei, and Tri-Service General Hospital. This page "
                  "describes the facilities, methods and support available for research."),
        ),
        actions(text_link("Research Areas and Faculty", L("en_inst:D-1"))),
    ])

    simulation = split(
        "".join([
            h4("Simulation center"),
            p("Three simulation wards around a small central control room with a one-way mirror, video recording, "
              "computers and two electric beds. Sessions can be observed live from the control room or from the "
              "nursing station outside the center."),
            p("The center is used for advanced medical-surgical, advanced obstetric and pediatric, and critical care "
              "courses, and for undergraduate OSCE teaching."),
        ]),
        photo(IMG_SIM_CENTER, "Simulation center at the College of Nursing", "4/3"),
        cols=(7, 5), align="start",
    )

    spaces = facts([
        ("Ward", draft("15 general beds") + " with piped air and suction (installed in 2007), and a long-term care "
                 "demonstration bed added in 2018."),
        ("Lecture hall", "134 seats, holding up to 150 people, for courses and workshops."),
        ("Self-study", "A smart interactive nursing self-learning classroom, opened in 2025."),
        ("Observation", draft("A behavioral development observation suite (one control room, two observation "
                                   "rooms) with a one-way mirror and video recording, used for workshops, group "
                                   "discussion and research.")),
        ("Seminars", draft("Two graduate classrooms for courses, discussions and presentations.")),
    ])

    hospital = "".join([
        p("Tri-Service General Hospital is the university's teaching hospital. Several faculty members also hold "
          f"nursing leadership posts there, including {name('wang')}, Deputy Director of the hospital's Department "
          f"of Nursing, and {name('tsai')}, a nursing supervisor."),
        p("For studies at the hospital, the Institute's research ethics page provides the procedure for obtaining "
          "the unit consent form required by the hospital's institutional review board, and for applying to collect "
          "data in its Department of Nursing."),
        actions(text_link("Research ethics resources (Chinese)", U_ETHICS)),
    ])

    methods = bullets([
        f"Randomized controlled trials: {name('liaw')}, {name('chiang')}, {name('huang')}",
        f"Ecological momentary assessment and intensive longitudinal data: {name('tlin')}, {name('ho')}",
        f"Machine learning and big data analytics: {name('tzeng')}, {name('wang')}, {name('feng')}",
        f"Qualitative and mixed-methods research: {name('feng')}, {name('liu')}",
        f"Instrument development and trajectory analysis: {name('ho')}",
        f"Systematic review and meta-analysis: {name('sung')}",
        f"Virtual reality and simulation in nursing education: {name('pan')}, {name('chenpc')}",
    ])

    resources = "".join([
        p(draft("Faculty and graduate students use the university library and its databases, and statistical "
                "software for quantitative and qualitative analysis.")),
        h4(draft("Cross-unit support")),
        p(draft("Research is supported by the College of Nursing, the Department of Nursing and the Department of "
                "Nursing at Tri-Service General Hospital.")),
    ])

    return page(
        opening,
        name_tape("Research Facilities"),
        simulation,
        spaces,
        note("前三列與模擬中心譯自學院現行〈教學設備〉頁；觀察室與研究生教室取自舊英文頁（uniten/100010/867，年代不明），"
             "請圖儀確認是否仍在使用。另請提供可供研究使用的設備清單（例如生理訊號、穿戴式裝置、VR/MR 設備）與借用方式，"
             "以及照片（模擬中心照片沿用學院〈教學設備〉頁的虛擬中心照片）。"
             "示範病房床數兩個來源不同：學院〈教學設備〉頁（unit/100010/1463）寫一般病床15張，舊英文頁（uniten/100010/867）"
             "寫12張病床加2張檢查床；請圖儀確認現況後再拿掉待確認。"),
        name_tape("Clinical Research Setting"),
        hospital,
        name_tape("Methodological Strengths"),
        p(draft("Methods our faculty use, as shown in their profiles, projects and publications:")),
        methods,
        note("方法與教師的對應依官方個人頁專長、計畫題名與論文整理；「方法學強項」的呈現方式為草稿，請教發確認或增補"
             "（例如統計諮詢、共用研究助理、研究中心）。"),
        name_tape("Academic Resources"),
        resources,
        note("請教發、圖儀提供：圖書館與資料庫、統計軟體授權、研究經費與行政支援、跨單位合作（例如與三總護理部、其他學院）"
             "的實際內容；上方為草稿，未確認前不列具體資料庫或軟體名稱。"),
        actions(text_link("Visiting Researchers", L("en_inst:E-2")), zh("inst:F", "中文版：研究成果")),
        owner=META["owner"],
    )
