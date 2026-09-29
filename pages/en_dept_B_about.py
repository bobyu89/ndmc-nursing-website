from components import (page, name_tape, statement, p, split, patch, illo_slot, route_list, tape_surface, text_link,
                        actions, draft, note)
from links import L
from tokens import C

META = {"id": "B", "slug": "about", "title": "About the Department", "owner": "院窗口", "site": "en_dept"}

# Verified sources: 歷史沿革 unit/100010/6804 (history); 學士班課程地圖 unit/100010/3642 (aim).


def render():
    opening = split(
        statement(
            draft("The country's first nursing department, rooted in military nursing."),
            draft("The Department of Nursing is the undergraduate unit of the College of Nursing. "
                  "This section introduces where it came from, who leads it and what it expects of its graduates."),
        ),
        '<div class="mx-auto" style="width:70%;max-width:260px;">' + patch(
            "Department of Nursing", "Bachelor's program", unit="dept",
            illo=illo_slot("Capping ceremony", "1/1", unit="dept"),
            tab="College of Nursing", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    roots = tape_surface(
        p("The department traces its origin to the Advanced Nursing Vocational Class in Jiangwan, Shanghai, "
          "founded by General Mei-Yu Chow in 1943, the country's earliest vocational training program for nurses."),
        p("In 1947 General Chow established the Department of Nursing, the country's first institution of "
          "higher nursing education."),
        actions(text_link("Full history and learning outcomes", L("en_dept:B-2"))),
    )

    aim = "".join([
        p("To educate professionals with a grounding in the humanities and strong nursing competence, ready to meet "
          "the needs of both the military and the civilian health care systems."),
        p(draft("In plain terms: our graduates care for patients in any hospital, and can also serve on military missions."),
          muted=True),
    ])

    routes = route_list([
        ("Chair's Message", draft("The chair on how the department teaches and what it expects of students"),
         L("en_dept:B-1")),
        ("Overview and Learning Outcomes", draft("History, educational goals and core competencies"), L("en_dept:B-2")),
        ("Faculty", draft("Teaching areas, with full profiles in the College Faculty Directory"), L("en_dept:F")),
    ], unit="dept")

    return page(
        opening,
        name_tape("Where We Began"),
        roots,
        name_tape("Educational Aim"),
        aim,
        name_tape("In This Section"),
        routes,
        note("周將軍英文名 General Mei-Yu Chow 沿用現行英文孤兒頁 uniten/100010/3353 的寫法；"
             "「高級護理職業班」譯為 Advanced Nursing Vocational Class 為本頁譯法。請院窗口確認學院正式英文用語。"),
        actions(text_link("中文：認識本系", L("dept:C")), text_link("College of Nursing", L("en:A"))),
        owner=META["owner"],
    )
