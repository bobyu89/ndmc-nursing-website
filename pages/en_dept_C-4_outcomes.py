from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, photo, feature_list,
                        tape_surface, draft, note)
from links import L

META = {"id": "C-4", "slug": "outcomes", "title": "Student Learning Outcomes", "owner": "學生事務", "site": "en_dept"}

# Verified: OSCE teaching in the simulation center — 教學設備 unit/100010/1463 (pages/E-3_facilities.py);
# core abilities — 學士班課程地圖 unit/100010/3642. Everything about specific achievements is a slot.

# Milestone photos: department home carousel "N76加冠" and "114小畢典" (unit/100180/6510), checked 200 image/jpeg on 2026-10-01.
IMG_CAPPING = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/LINE_ALBUM_1140317N76%E5%8A%A0%E5%86%A0_250706_9.jpg"
IMG_GRAD = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/114%E5%B0%8F%E7%95%A2%E5%85%B8.jpg"

SLOT = "[to be supplied]"


def render():
    opening = "".join([
        statement(
            draft("What students can show at the end of four years."),
            draft("Outcomes are easier to see than to describe. This page gathers evidence from courses, "
                  "simulation, practicum, competitions and student projects."),
        ),
        actions(text_link("The thirteen core competencies", L("en_dept:B-2"))),
    ])

    lead = split(
        photo_slot("Students during an OSCE station in the simulation center (wide)", "16/9"),
        "".join([
            p("OSCE teaching for the bachelor's program takes place in the simulation center, which is equipped "
              "with one-way mirrors and a video recording system."),
            p(draft("Each station tests assessment, skills and communication together, as they happen at the bedside.")),
        ]),
        cols=(7, 5), align="center",
    )

    evidence = feature_list([
        ("Courses", draft("A course project or assignment that shows one of the core competencies in action.") + " " + SLOT,
         None, "dept", "C"),
        ("Simulation", draft("A simulation scenario and what students learned from the debriefing.") + " " + SLOT,
         None, "dept", "S"),
        ("Practicum", draft("A short story from hospital, community or military nursing practicum.") + " " + SLOT,
         None, "dept", "P"),
        ("Competitions", draft("Nursing skills or innovation competitions: event, year and result.") + " " + SLOT,
         None, "dept", "A"),
        ("Student research", draft("Undergraduate research projects: title, year and supervisor.") + " " + SLOT,
         None, "dept", "R"),
    ])

    story = tape_surface(
        p(draft("“A student reflection of three or four sentences: what they did, what was hard, "
                "what changed in how they care for patients.”")),
        p("[Student name]　[Year of entry]　[Setting]", muted=True),
    )

    gallery = split(
        photo(IMG_CAPPING, "Capping ceremony: students in white nursing uniforms and caps with faculty", "4/3",
              caption="Capping ceremony"),
        photo(IMG_GRAD, "Graduates in academic gowns with faculty in front of a campus building", "4/3",
              caption="Department graduation celebration, 2025"),
        cols=(6, 6), align="start",
    )

    return page(
        opening,
        name_tape("Simulation and OSCE"),
        lead,
        name_tape("Evidence of Learning"),
        evidence,
        note("請學生事務依五類各提供 1 則實例（名稱、年份、一句說明、照片），並確認可公開。"
             "競賽得獎與大專生研究計畫（中文站 G）請附官方名稱與年份；沒有資料的類別整列刪除，不要留空或推估。"),
        name_tape("In Their Words"),
        story,
        note("請學生事務收集 1〜2 篇學生心得（英文 80 字內，或中文由國際事務翻譯），並取得本人同意公開姓名與照片。"
             "屆別代號（例 N76）請改寫為入學年份。"),
        name_tape("Milestones"),
        gallery,
        note("加冠典禮、畢業照片沿用學系首頁輪播「N76加冠」「114小畢典」（114 年＝2025）；英文圖說為暫擬，請確認。"),
        actions(text_link("Campus Experience", L("en_dept:D")), text_link("中文：大專生研究計畫", L("dept:G"))),
        owner=META["owner"],
    )
