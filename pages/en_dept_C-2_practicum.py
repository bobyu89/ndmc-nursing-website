from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, photo, bullets, feature_list,
                        tape_surface, draft, note)
from links import L

META = {"id": "C-2", "slug": "practicum", "title": "Clinical and Military Nursing Practicum", "owner": "課委會",
        "site": "en_dept"}

# Verified (plain):
#   teaching hospital — 115 正期班簡章 "本校實習醫院為三軍總醫院。" (pages/F_admissions.py)
#   practicum course titles — 114學年兼任老師名冊 unit/100010/1470 (pages/E-1_faculty.py)
#   military nursing as a core ability; military-nurse role as a goal — unit/100010/3642, 1471 (pages/dept_C-2-2_goals.py)
#   demonstration ward use — 教學設備 unit/100010/1463 (pages/E-3_facilities.py)
#   hospital and community practicum sites, teacher ratio, community practicum content — pages/dept_F-2-1, dept_F-2-2
#     (學生手冊〈臨床實習〉與表五, via the Chinese pages)
# Photo: 示範實習病房1.png on the same 教學設備 page (checked 200 image/png on 2026-10-01).
IMG_WARD = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/"
            "%E7%A4%BA%E7%AF%84%E5%AF%A6%E7%BF%92%E7%97%85%E6%88%BF1.png")

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
        actions(text_link("Curriculum", L("en_dept:C-1")), text_link("中文版：實習資訊", L("dept:F-2"))),
    ])

    before = split(
        "".join([
            p("Before entering the wards, students practice in the demonstration ward, which is mainly used for "
              "undergraduate physical examination and assessment and basic nursing skills."),
            actions(text_link("Simulation and Learning Spaces", L("en_dept:C-3"))),
        ]),
        photo(IMG_WARD, "The demonstration ward: hospital beds with pink privacy curtains", "4/3"),
        cols=(7, 5), align="start",
    )

    settings = feature_list([
        ("Hospital practicum",
         "The university's teaching hospital is Tri-Service General Hospital. Students rotate between "
         "Tri-Service General Hospital and " + draft("Taipei Veterans General Hospital") + ". Clinical teachers "
         "go with students to the hospital; each teacher usually supervises six to seven students.",
         None, "dept", "H"),
        ("Community practicum",
         "Community Health Nursing Practicum takes place mainly at the "
         + draft("Neihu and Nangang District Health Centers") + " of the Taipei City Government and the "
         + draft("Department of Community Medicine, Tri-Service General Hospital") + ". It covers community "
         "assessment and planning, home visits and case management, and group health education.",
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
        note("醫院與社區兩項已譯自中文站 F-2-1、F-2-2 的原文（出自學生手冊〈臨床實習〉與表五）；臺北榮總、內湖與南港健康服務中心、"
             "三總社區醫學部的英文名稱為暫譯，請確認官方英文名。軍陣一項仍為草稿。請課委會提供：各實習的年級與週數、"
             "軍陣實習的內容與地點（可公開範圍）。未確認前不寫任何週數。"),
        name_tape("Practicum Courses"),
        courses,
        note("實習課名譯自 114 學年兼任老師名冊（unit/100010/1470）所列科目，只列學士班常見的實習課；"
             "請課委會確認是否皆為學士班課程、英文課名是否有官方譯名。"),
        name_tape("In Practice"),
        photos,
        note("請提供可公開的實習照片兩張（病人不可入鏡或須去識別），並附英文圖說。"),
        owner=META["owner"],
    )
