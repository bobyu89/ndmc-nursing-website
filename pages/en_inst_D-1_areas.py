from components import (page, name_tape, statement, p, h4, text_link, actions, route_list, bullets, draft, note)
from links import L
from pages._en_inst_data import (FACULTY, TRAUMA_PROJECTS, MILITARY_HEALTH_PROJECTS, project_items, person_row,
                                 name, zh, FACULTY_EN)

META = {"id": "D-1", "slug": "areas", "title": "Research Areas and Faculty", "owner": "教發", "site": "en_inst"}

# Names, positions and specialties from the official English faculty list (Doclisten/191/100010/3351) and each
# DocDetEn profile; see pages/_en_inst_data.py. Group labels and group membership are editorial drafts:
# each person is placed once, by the specialties on their profile. Not a supervisor-matching page.

AREAS = [
    ("Military health, trauma and disaster nursing",
     "Disaster preparedness, mass-casualty and combat casualty care, burns and emergency care, and the health of "
     "military personnel.",
     ["pan", "chiang", "lan", "wang", "liang", "tlin"]),
    ("Mental health and psychosocial care",
     "Mental illness, digital health literacy, long-term monitoring of depression, ethics and palliative care.",
     ["tzeng", "feng", "ho", "tsai"]),
    ("Chronic illness, critical and cardiovascular care",
     "Rehabilitation, self-care, symptom management and health promotion for adults with chronic or critical "
     "illness.",
     ["clin", "chenyj", "yangpl", "yangcc", "chenpc", "huang", "sung"]),
    ("Women's, children's and family health",
     "Pregnancy, preterm infants, children with cancer or congenital heart disease, and their families.",
     ["liaw", "cxlin", "liu"]),
]


def render():
    opening = "".join([
        statement(
            draft("Find the people behind the research."),
            draft("Our faculty are grouped here by research area, each with the specialties listed on their "
                  "official profile. Full profiles, publications and contact details are in the College of Nursing "
                  "Faculty Directory."),
        ),
        actions(text_link("Faculty Directory", L("en:D-1")), zh("inst:F-1")),
    ])

    areas = []
    for label, desc, keys in AREAS:
        areas.append(h4(draft(label)))
        areas.append(p(draft(desc), muted=True))
        areas.append(route_list([person_row(k) for k in keys], unit="inst"))

    labs = route_list(
        [(f"{name(k)} research group", "", FACULTY[k][5])
         for k in FACULTY if FACULTY[k][5]],
        unit="inst",
    )

    projects = "".join([
        p("Projects on trauma, disaster and military health, as listed on faculty profile pages:", muted=True),
        bullets(project_items(TRAUMA_PROJECTS + MILITARY_HEALTH_PROJECTS)),
        actions(text_link("Featured research", L("en_inst:D"))),
    ])

    contact = "".join([
        p(draft("To discuss a collaboration with a faculty member, please write to the College of Nursing office "
                "and name the faculty member and research theme. The office will pass your message on.")),
        actions(text_link("Collaboration Contact", L("en_inst:E-3")),
                text_link("Areas for Collaboration", L("en_inst:E-1"))),
    ])

    return page(
        opening,
        note("名單依學院官方英文師資頁（Doclisten/191/100010/3351）助理教授以上教師整理，每人只列一個領域。"
             "分組名稱與歸屬為草稿，請教發確認；是否有正式研究團隊（團隊名稱、召集人、成員），若有請提供，改以團隊呈現。"
             "莊蕙婉老師在中文師資名單但不在官方英文名單，是否加入請確認。馮欣蓓老師職級：中文名單為副教授、中英文個人頁為助理教授，請確認。"),
        name_tape("Research Areas"),
        *areas,
        name_tape("Research Group Websites"),
        labs,
        note("研究室網址取自教師個人頁；請各研究室確認是否有英文版頁面。其他老師的研究室網址待 Google 表單收集後補上。"),
        name_tape("Current Projects"),
        projects,
        note("教發請確認以上計畫是否仍在執行期間；英文題名逐字取自教師官方英文個人頁。其他領域的進行中計畫待彙整後補入。"),
        name_tape("Academic Collaboration"),
        contact,
        owner=META["owner"],
    )
