from components import (page, name_tape, statement, p, h4, text_link, actions, split, photo_slot, illo_slot,
                        route_list, draft, note)
from links import L
from pages._en_college_shared import zh

META = {"id": "D-3", "slug": "facilities", "title": "Facilities", "owner": "圖儀、哲君", "site": "en_college"}

# Plain descriptions are faithful translations of verified text in pages/E-3_facilities.py
# (教學設備 unit/100010/1463). Years on that page are ROC years (107 = 2018, 96 = 2007, 114 = 2025).
# The Memorial Hall paragraph comes only from the old English Facilities & Resources page (uniten/100010/867),
# which is undated and not on the Chinese site, so it stays draft.


def render():
    opening = "".join([
        statement(
            draft("Practice in the simulation ward, then go to the bedside."),
            draft("From a tiered lecture hall to a demonstration ward and a simulation center, students rehearse "
                  "physical assessment, nursing skills and critical care in settings close to the real thing."),
        ),
        actions(text_link("Academic Visits", L("en:G-1")), zh("E-3")),
    ])

    simulation = "".join([
        split(
            "".join([
                h4("Simulation Center"),
                p("The center has three simulation wards around a small central control room, from which the adult and "
                  "pediatric labs can be observed at the same time. It is equipped with a one-way mirror, a video "
                  "recording system, computers and two electric beds."),
                p("It can be linked to the nurses' station outside, so students there can watch the simulation live "
                  "and learn alongside. Besides advanced medical-surgical, advanced obstetric and pediatric, and critical "
                  "care courses, the center is used for the undergraduate OSCE."),
            ]),
            photo_slot("Simulation Center and control room", "4/3"),
            cols=(7, 5), align="start",
        ),
        split(
            "".join([
                h4(draft("VR and MR simulation")),
                p(draft("Virtual reality (VR) and mixed reality (MR) scenarios let students practice clinical situations "
                        "in a safe environment.")),
            ]),
            illo_slot("Nursing student practicing with an MR headset (CocoMaterial, recolored)", "4/3", unit="inst"),
            cols=(7, 5), reverse=True, align="start",
        ),
        note("VR／MR 一段在中文頁仍為暫擬；圖儀、哲君提供設備名稱、用途與使用課程後，中英文一起定稿。"),
    ])

    classroom = split(
        p("A tiered lecture hall with 134 seats that can hold up to 150 people, used for courses and workshops."),
        photo_slot("Demonstration Classroom (tiered lecture hall)", "16/9"),
        cols=(5, 7), align="start",
    )

    ward = "".join([
        p("The ward has 15 general beds, each with a bedside table and an over-bed table. A long-term care "
          "demonstration bed was added in 2018. Since 2007 a central gas system has supplied air flow and suction to "
          "every bed, bringing the ward closer to a clinical setting."),
        p("It is used mainly for undergraduate physical examination and assessment, basic nursing skills practice, "
          "and medical research camps."),
        split(photo_slot("Demonstration Ward: bed area", "4/3"), photo_slot("Demonstration Ward: long-term care bed", "4/3"),
              cols=(7, 5), align="start"),
    ])

    learning = "".join([
        split(
            "".join([
                h4("Smart Interactive Nursing Self-Learning Classroom"),
                p("Newly set up in 2025."),
                p(draft("A space where students practice nursing skills on their own.")),
            ]),
            photo_slot("Smart Interactive Nursing Self-Learning Classroom", "4/3"),
            cols=(7, 5), align="start",
        ),
        split(
            "".join([
                h4(draft("General Mei-Yu Chow Memorial Hall")),
                p(draft("A memorial hall recreates the office General Chow used when she led the school, with her desk, "
                        "chairs and bookcases. It is open to alumni and students at the annual anniversary.")),
            ]),
            photo_slot("General Mei-Yu Chow Memorial Hall", "4/3"),
            cols=(7, 5), reverse=True, align="start",
        ),
        note("周美玉將軍紀念室只見於舊英文頁（uniten/100010/867），中文教學設備頁沒有；請哲君確認紀念室是否仍在、開放方式，"
             "以及能否列為來訪參觀點。舊英文頁的示範病房床數（12 張＋2 張檢查床）與中文頁（15 張）不同，本頁採中文頁。"),
    ])

    return page(
        opening,
        name_tape("Simulation"),
        simulation,
        name_tape("Demonstration Classroom", unit="dept"),
        classroom,
        name_tape("Demonstration Ward", unit="dept"),
        ward,
        name_tape("Learning Spaces", unit="inst"),
        learning,
        name_tape("Seeing the Facilities"),
        p(draft("Visiting delegations can ask to see the teaching facilities as part of an academic visit.")),
        route_list([
            ("Academic Visits", draft("Plan a short delegation visit"), L("en:G-1")),
            ("Research Highlights", draft("Simulation-related research in trauma and disaster nursing"), L("en:D-2")),
        ]),
        owner=META["owner"],
    )
