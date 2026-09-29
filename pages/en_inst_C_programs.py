from components import (page, name_tape, statement, p, h4, text_link, actions, facts, route_list, split,
                        illo_slot, draft, note)
from links import L
from pages._en_inst_data import U_RULES, zh

META = {"id": "C", "slug": "programs", "title": "Graduate Programs", "owner": "院窗口", "site": "en_inst"}

# For international academic visitors: what the programs are, not how to apply (en-sites.md shared rules).
# Master's facts translated from 學生專區「入學資格與修業規定」 unit/100181/6533; teaching hospital from the
# 115 academy brochure (pages/F_admissions.py).


def render():
    opening = "".join([
        statement(
            draft("Graduate study for nurses who want to specialise and do research."),
            draft("The Institute's master's program takes registered nurses with clinical experience into one field "
                  "of advanced practice and trains them to carry out research. This page describes the programs for "
                  "visiting researchers and partner institutions; it is not an admissions page."),
        ),
        actions(zh("inst:C-2")),
    ])

    master = split(
        "".join([
            facts([
                ("Tracks", "Adult and Gerontological Nursing; Women's and Children's Nursing; Mental Health Nursing; "
                           "Nurse Practitioner"),
                ("Length", "Two years, which may be extended by up to two years if needed"),
                ("Credits", "33 credits for students entering from the 2025–26 academic year"),
                ("Hospital", "Tri-Service General Hospital"),
                ("Language", draft("Language of instruction: [to be confirmed]")),
            ]),
            p(draft("Translated from the Institute's study regulations.") + "　"
              + text_link("Source (Chinese)", U_RULES), muted=True),
        ]),
        illo_slot("Graduate seminar around a table (CocoMaterial, recoloured)", "4/3", unit="inst"),
        cols=(7, 5), align="start",
    )

    positioning = "".join([
        p(draft("Our students are experienced nurses. Coursework, research training and a thesis prepare them "
                "for advanced practice, nursing education and military nursing.")),
        route_list([
            ("Curriculum", draft("Curriculum themes, research training and selected graduate courses"),
             L("en_inst:C-1")),
            ("Research Areas and Faculty", draft("The fields our faculty supervise and study"), L("en_inst:D-1")),
        ], unit="inst"),
    ])

    doctoral = "".join([
        p(draft("The Institute also offers a doctoral program in nursing. Its research directions and structure "
                "will be described here once confirmed.")),
        note("博士班狀態未確認：研究所現行網站只列碩士班；《116 學年度博、碩士班招生簡章》列有護理研究所博士班。"
             "請院窗口確認英文站能否介紹；若可以，請提供博士班英文簡介（研究方向、修業年限、課程重點），"
             "不必提供報考資訊。確認前本段維持草稿，不對外介紹則刪除本段。"),
    ])

    return page(
        opening,
        name_tape("Master's Program"),
        master,
        note("本頁只介紹學制給國際學者參考，不放報考資格、考試科目、日期與表單（英文站不招收國際學位生）。"
             "請院窗口確認：授課語言（是否有英語授課課程）；「33 學分」適用 114 學年起入學者，113 學年前入學者為 36–37 學分，"
             "英文站只列現行規定。"),
        name_tape("Positioning"),
        positioning,
        name_tape("Doctoral Program"),
        doctoral,
        h4(draft("Interested in visiting or collaborating?")),
        actions(text_link("Visiting Researchers", L("en_inst:E-2")),
                text_link("Research Collaboration", L("en_inst:E"))),
        owner=META["owner"],
    )
