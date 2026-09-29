from components import (page, name_tape, statement, p, h4, button, text_link, actions, feature_lead, illo_slot,
                        bullets, route_list, draft, note)
from links import L
from pages._en_inst_data import (TRAUMA_PROJECTS, TRAUMA_PROJECT_TRANSLATED, MILITARY_HEALTH_PROJECTS,
                                 project_items, zh)

META = {"id": "D", "slug": "research", "title": "Research", "owner": "教發", "site": "en_inst"}

# The Institute's research pages are the source for research content (護理學院架構: 研究所「研究成果」是研究內容母站);
# the College English site keeps the full faculty profiles (en:D-1).
# Project titles verbatim from the official English faculty profiles, except TRAUMA_PROJECT_TRANSLATED.


def render():
    opening = "".join([
        statement(
            draft("From the battlefield to the bedside."),
            draft("Our research centers on military nursing and trauma and disaster care, alongside mental health, "
                  "chronic illness, sleep and occupational health, and nursing education."),
        ),
        actions(button("Research Areas and Faculty", L("en_inst:D-1")), zh("inst:F")),
    ])

    strengths = "".join([
        h4(draft("Military health and trauma and disaster nursing")),
        p(draft("Disaster preparedness and resilience of military nurses, mass-casualty education, combat casualty "
                "care simulation, and the sleep and mental health of military personnel.")),
        h4(draft("Mental health and psychosocial care")),
        p(draft("Digital health literacy and long-term monitoring of mental illness, and psychosocial care for "
                "patients and families.")),
        h4(draft("Chronic illness, critical and cardiovascular care")),
        p(draft("Rehabilitation, self-care and symptom management for people with chronic and critical illness.")),
        h4(draft("Women's, children's and family health")),
        p(draft("Preterm infants, pregnancy, children with cancer or heart disease, and their families.")),
        h4(draft("Nursing education and digital technology")),
        p(draft("Simulation, virtual reality and artificial intelligence in nursing education and practice.")),
        note("研究特色五項為依教師官方英文個人頁專長歸納的草稿，請教發確認分類與每項 1–2 句定稿。"),
    ])

    featured = feature_lead(
        "Trauma and disaster nursing",
        [
            p(draft("This is where our research differs most from other nursing schools: how nurses prepare for, and "
                    "care for casualties in, combat, disaster and mass-casualty settings.")),
            p("Projects listed on faculty profile pages:", muted=True),
            bullets(project_items(TRAUMA_PROJECTS) + [
                draft(project_items([TRAUMA_PROJECT_TRANSLATED])[0])]),
        ],
        illo_slot("Mass-casualty triage exercise (CocoMaterial, recolored)", "1/1", unit="inst"),
        unit="inst", href=L("en_inst:E-1"), link_label="Collaborate on this theme",
    )

    military = "".join([
        p("Projects on the health of military personnel, listed on faculty profile pages:", muted=True),
        bullets(project_items(MILITARY_HEALTH_PROJECTS)),
    ])

    tasks = route_list([
        ("Research Areas and Faculty", draft("Who works on what, grouped by research area"), L("en_inst:D-1")),
        ("Publications and Graduate Research", draft("Selected faculty publications by year"), L("en_inst:D-2")),
        ("Academic Activities", draft("Lectures, conferences and training held by the Institute"), L("en_inst:D-3")),
        ("Research Environment", draft("Facilities, methods and support for research"), L("en_inst:D-4")),
        ("Research Collaboration", draft("Themes, formats and how to contact us"), L("en_inst:E")),
    ], unit="inst")

    graduate = "".join([
        p(draft("Every master's student completes a thesis under faculty supervision. Selected recent theses will "
                "be listed here.")),
        note("教發請提供：近年代表性碩士論文 5–10 篇（年份、研究生、指導教授、論文英文題名），以及研究生海報、得獎紀錄"
             "（須附可查證來源）。未提供前本段不列任何論文。"),
    ])

    return page(
        opening,
        name_tape("Research Strengths"),
        strengths,
        name_tape("Featured Research"),
        featured,
        note("教發請確認上列計畫的執行狀態。前三項英文題名逐字取自教師官方英文個人頁；王蔚芸老師的計畫只見於中文個人頁，"
             "英文題名為本站翻譯，請老師提供正式英文題名。"),
        military,
        name_tape("Explore Our Research"),
        tasks,
        name_tape("Graduate Research"),
        graduate,
        owner=META["owner"],
    )
