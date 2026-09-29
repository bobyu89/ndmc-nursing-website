from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, bullets, feature_list,
                        tape_surface, draft, note)
from links import L

META = {"id": "C-2", "slug": "practicum", "title": "Clinical and Military Nursing Practicum", "owner": "課委會",
        "site": "en_dept"}

# Verified (plain):
#   teaching hospital — 115 正期班簡章 "本校實習醫院為三軍總醫院。" (pages/F_admissions.py)
#   practicum course titles — 114學年兼任老師名冊 unit/100010/1470 (pages/E-1_faculty.py)
#   military nursing as a core ability; military-nurse role as a goal — unit/100010/3642, 1471 (pages/dept_C-2-2_goals.py)
#   demonstration ward use — 教學設備 unit/100010/1463 (pages/E-3_facilities.py)

PRACTICA = [
    "Fundamentals of Nursing Practicum",
    "Medical-Surgical Nursing Practicum",
    "Obstetric Nursing Practicum",
    "Pediatric Nursing Practicum",
    "Mental Health Nursing Practicum",
    "Community Health Nursing Practicum",
    "Nursing Administration Practicum",
    "Comprehensive Clinical Nursing Practicum (I) and (II)",
]


def render():
    opening = "".join([
        statement(
            draft("Learning care at the bedside, in the community and in the field."),
            draft("Practicum is where students turn classroom knowledge into clinical judgment. "
                  "Each setting asks for a different kind of judgment."),
        ),
        actions(text_link("Curriculum", L("en_dept:C-1")), text_link("中文：實習資訊", L("dept:F-2"))),
    ])

    before = split(
        "".join([
            p("Before entering the wards, students practice in the demonstration ward, which is mainly used for "
              "undergraduate physical examination and assessment and basic nursing skills."),
            actions(text_link("Simulation and Learning Spaces", L("en_dept:C-3"))),
        ]),
        photo_slot("Students practicing in the demonstration ward (4:3)", "4/3"),
        cols=(7, 5), align="start",
    )

    settings = feature_list([
        ("Hospital practicum",
         "The university's teaching hospital is Tri-Service General Hospital. "
         + draft("Students care for patients on its wards under the guidance of clinical teachers."),
         None, "dept", "H"),
        ("Community practicum",
         "Community Health Nursing Practicum is part of the practicum sequence. "
         + draft("Students practice health education and home-based care in community and long-term care settings."),
         None, "dept", "C"),
        ("Military nursing",
         "Military nursing is one of the program's thirteen core competencies, and graduates are expected to fulfill "
         "the professional role of a military nurse. "
         + draft("Training covers care in military, field and disaster settings."),
         None, "dept", "M"),
    ])

    courses = tape_surface(
        p("Practicum courses listed in the college's 2025–26 adjunct faculty roster include:"),
        bullets(PRACTICA),
        p(draft("Clinical instructors from partner settings teach many of these courses alongside full-time faculty."),
          muted=True),
    )

    photos = split(
        photo_slot("Hospital practicum at Tri-Service General Hospital (4:3)", "4/3"),
        photo_slot("Military nursing or field training (4:3)", "4/3"),
        cols=(6, 6), align="start",
    )

    return page(
        opening,
        name_tape("Preparing for Practice"),
        before,
        name_tape("Three Settings"),
        settings,
        note("醫院、社區、軍陣三類實習的說明為草稿（中文站 F-2-1〜F-2-3 尚未撰寫）。請課委會提供：各實習的年級與週數、"
             "主要實習單位（除三軍總醫院外的社區或長照機構名稱）、軍陣實習的內容與地點（可公開範圍）、臨床教師與學生比。"
             "未確認前不寫任何週數或機構名稱。"),
        name_tape("Practicum Courses"),
        courses,
        note("實習課名譯自 114 學年兼任老師名冊（unit/100010/1470）所列科目，只列學士班常見的實習課；"
             "請課委會確認是否皆為學士班課程、英文課名是否有官方譯名。"),
        name_tape("In Practice"),
        photos,
        note("請提供可公開的實習照片兩張（病人不可入鏡或須去識別），並附英文圖說。"),
        owner=META["owner"],
    )
