from components import (page, name_tape, statement, p, h4, text_link, actions, bullets, facts, tape_surface, draft,
                        note)
from links import L
from pages._en_inst_data import name, email_link

META = {"id": "E-1", "slug": "collaboration-areas", "title": "Areas for Collaboration", "owner": "國際事務、教發",
        "site": "en_inst"}

# Theme labels and priorities are drafts. Expertise = official English profile specialties; example outputs are
# paper titles (year, journal) from the citations on pages/en_inst_D-2_publications.py and project titles from
# pages/_en_inst_data.py — all copied from official faculty profiles.

THEMES = [
    ("Military health, trauma and disaster nursing",
     ["pan", "chiang", "lan", "wang", "liang", "tlin"],
     "Disaster nursing and preparedness, emergency and burn care, traumatic brain injury, military nursing, and the "
     "sleep and occupational health of military personnel.",
     ["Self-efficacy and family support in the relationship between stress and readiness for disaster response among "
      "nurses: A mediation analysis (BMC Nursing, 2025)",
      "Tabletop simulation-based learning for mass casualty management in nursing undergraduates: A mixed-methods "
      "study (Clinical Simulation in Nursing, 2026)",
      "Psychosocial Working Environment, Submarine Deployment, and Sleep among Navy Submarine Crews: An 8-day "
      "Longitudinal Study (Journal of Medical Sciences, 2026)"]),
    ("Mental health and digital health",
     ["tzeng", "feng", "ho"],
     "Mental health nursing, digital health literacy of people with serious mental illness, digital psychological "
     "monitoring, and big data and machine learning.",
     ["Bridging the Digital Divide: A Co-Creation Study to Promote Digital Health Literacy among Individuals with "
      "Serious Mental Illness (NSTC project)",
      "Exploring mental health literacy on twitter: A machine learning approach (Journal of Affective Disorders, "
      "2025)"]),
    ("Chronic illness, critical and cardiovascular care",
     ["clin", "chenyj", "huang", "chenpc", "sung"],
     "Cardiopulmonary and cardiac rehabilitation, critical care, self-care and health promotion for adults with "
     "chronic illness, and care of older people.",
     ["Effects of a home-based multicomponent exercise programme on frailty in postcardiac surgery patients: "
      "A randomized controlled trial (European Journal of Cardiovascular Nursing, 2025)",
      "Effectiveness of a post-acute-care rehabilitation program in stroke patients: A retrospective cohort study "
      "(Life, 2025)"]),
    ("Women's, children's and family health",
     ["liaw", "cxlin", "liu", "lan"],
     "Pregnancy and women's health, preterm infants, children with cancer or congenital heart disease, and their "
     "families.",
     ["Effects of theory-guided unsupervised exercise on depression, sleep quality, and sense of control in pregnant "
      "women: A randomized controlled trial (Worldviews on Evidence-Based Nursing, 2025)",
      "Grit in the workplace experienced by Taiwanese adults with congenital heart disease: A phenomenological "
      "study (Journal of Clinical Nursing, 2026)"]),
]


def render():
    opening = "".join([
        statement(
            draft("Four areas where we are ready to work together."),
            draft("Each area lists the faculty who work in it, their expertise, and examples of recent work. "
                  "To propose a collaboration, write to the College of Nursing office and name the area."),
        ),
        actions(text_link("Collaboration Contact", L("en_inst:E-3")),
                text_link("Faculty Directory", L("en:D-1"))),
    ])

    blocks = [name_tape("Four Areas")]
    for label, keys, expertise, outputs in THEMES:
        blocks += [
            h4(draft(label)),
            p("<strong>Faculty:</strong> " + ", ".join(name(k) for k in keys)),
            p("<strong>Expertise:</strong> " + expertise),
            p("Example outputs:", muted=True),
            bullets(outputs),
        ]

    return page(
        opening,
        note("四個主題與排序為草稿（依官方英文個人頁專長整理），請國際事務與教發確認「優先合作主題」並指定各主題的聯絡老師；"
             "範例成果均為官方個人頁所列論文或計畫的題名。英文站不公開個人信箱，洽詢統一經學院信箱轉介。"),
        *blocks,
        name_tape("Contact"),
        p(draft("Name the area and, if you know it, the faculty member. We will forward your message.")),
        facts([("Email", email_link())]),
        actions(text_link("What to include in your inquiry", L("en_inst:E-3"))),
        owner=META["owner"],
    )
