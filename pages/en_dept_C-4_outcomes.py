from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, feature_list,
                        tape_surface, draft, note)
from links import L

META = {"id": "C-4", "slug": "outcomes", "title": "Student Learning Outcomes", "owner": "學生事務", "site": "en_dept"}

# Verified: OSCE teaching in the simulation centre — 教學設備 unit/100010/1463 (pages/E-3_facilities.py);
# core abilities — 學士班課程地圖 unit/100010/3642. Everything about specific achievements is a slot.

SLOT = "[to be supplied]"


def render():
    opening = "".join([
        statement(
            draft("What students can show at the end of four years."),
            draft("Outcomes are easier to see than to describe. This page gathers evidence from courses, "
                  "simulation, practicum, competitions and student projects."),
        ),
        actions(text_link("The thirteen core abilities", L("en_dept:B-2"))),
    ])

    lead = split(
        photo_slot("Students during an OSCE station in the simulation centre (wide)", "16/9"),
        "".join([
            p("OSCE teaching for the bachelor's programme takes place in the simulation centre, which is equipped "
              "with one-way mirrors and a video recording system."),
            p(draft("Each station tests assessment, skills and communication together, as they happen at the bedside.")),
        ]),
        cols=(7, 5), align="center",
    )

    evidence = feature_list([
        ("Courses", draft("A course project or assignment that shows one of the core abilities in action.") + " " + SLOT,
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
        photo_slot("Capping ceremony", "4/3"),
        photo_slot("Graduation ceremony", "4/3"),
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
        note("加冠典禮、畢業典禮照片可取自學系首頁輪播（N76 加冠、114 畢業典禮），請確認授權並附英文圖說。"),
        actions(text_link("Campus Experience", L("en_dept:D")), text_link("中文：大專生研究計畫", L("dept:G"))),
        owner=META["owner"],
    )
