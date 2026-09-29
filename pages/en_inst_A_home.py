from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, photo_slot,
                        ribbon_bar, split, unit_pair, feature_lead, feature_list, route_list, bullets, facts, draft,
                        note)
from links import L
from tokens import C
from pages._en_inst_data import (TRAUMA_PROJECTS, project_items, name, position, email_link, INST_PHONE, zh)

META = {"id": "A", "slug": "home", "title": "Graduate Institute of Nursing", "owner": "院窗口", "site": "en_inst"}

# Structure mirrors pages/inst_A_home.py. Verified facts reused:
#   founded 1979, pioneer of master's nursing education in Taiwan — 歷史沿革 unit/100181/6527;
#   "the first graduate nursing program in Taiwan" — old English page uniten/100010/3353
#   director's name and position — DocDetEn/191/100010/3351/4443
#   project titles — faculty DocDetEn profiles (see pages/_en_inst_data.py)


def render():
    opening = split(
        "".join([
            statement(
                "Taiwan's first graduate nursing program, founded in 1979.",
                draft("The Graduate Institute of Nursing at National Defense Medical University, Taipei, educates "
                      "nurses who ask clinical questions, study them, and bring the evidence back to patient care."),
            ),
            actions(button("Research Collaboration", L("en_inst:E")),
                    text_link("About the Institute", L("en_inst:B")), zh("inst:A")),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch(
            "Graduate Institute of Nursing", "護理研究所", unit="inst",
            illo=illo_slot("Graduate nurse and supervisor reviewing data together (CocoMaterial, recoloured)", "1/1",
                           unit="inst"),
            tab="College of Nursing", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    quick = ribbon_bar([
        ("Research", L("en_inst:D")),
        ("Faculty Expertise", L("en_inst:D-1")),
        ("Collaborate", L("en_inst:E")),
        ("News", L("en_inst:F")),
    ])

    director = split(
        photo_slot("Director of the Institute (portrait 3:4)", "3/4"),
        "".join([
            p("The Institute was established in 1979 to meet the needs of education and research, "
              "and pioneered master's-level nursing education in Taiwan."),
            p(f"{name('pan')}<br>{position('pan')}", muted=True),
            actions(text_link("Director's Message", L("en_inst:B-1")),
                    text_link("Overview and History", L("en_inst:B-2"))),
        ]),
        cols=(3, 9), align="start",
    )

    research = feature_lead(
        "Trauma and disaster nursing",
        [
            p(draft("Military nursing, trauma and disaster care are what set our research apart: how nurses prepare "
                    "for and respond to casualties in combat, disaster and mass-casualty settings.")),
            p("Projects listed on faculty profile pages include:", muted=True),
            bullets(project_items(TRAUMA_PROJECTS)),
        ],
        illo_slot("Combat casualty care simulation (CocoMaterial, recoloured)", "1/1", unit="inst"),
        unit="inst", href=L("en_inst:D"), link_label="Research at the Institute",
    )
    more = "".join([
        feature_list([
            ("Research areas and faculty",
             draft("Faculty members grouped by research area, each with their specialties."), None, "inst", "R"),
            ("Publications",
             draft("Selected recent journal articles by our faculty, listed by year."), None, "inst", "P"),
            ("Academic activities",
             draft("Lectures, conferences and training held by the Institute."), None, "inst", "A"),
        ]),
        actions(text_link("Research Areas and Faculty", L("en_inst:D-1")),
                text_link("Publications", L("en_inst:D-2")),
                text_link("Academic Activities", L("en_inst:D-3"))),
    ])

    news = "".join([
        note("首頁為靜態 HTML，無法自動帶入消息；以英文消息頁導流。英文消息只放研究亮點、論文發表、研究生成果、"
             "學術活動與國際學術交流，不放招生、課務、口試、獎學金公告。"),
        route_list([
            ("News", draft("Research highlights, publications, graduate achievements and seminars"), L("en_inst:F")),
            ("Academic Activities", draft("Records of lectures, conferences and training"), L("en_inst:D-3")),
        ], unit="inst"),
    ])

    contact = "".join([
        p(draft("Researchers and institutions interested in working with us can write to the College of Nursing "
                "office. Please tell us your research theme and the kind of collaboration you have in mind.")),
        p("Email:"),
        actions(email_link()),
        facts([("Telephone", INST_PHONE)]),
        actions(text_link("Collaboration Contact", L("en_inst:E-3"))),
    ])

    family = unit_pair([
        ("college", "College of Nursing", "Faculty directory, research, visits", L("en:A")),
        ("dept", "Department of Nursing", "Undergraduate program and practicum", L("en_dept:A")),
    ])

    return page(
        opening,
        quick,
        name_tape("Director and Institute"),
        director,
        note("所長照片請院窗口提供（直式 3:4）；英文所長的話見 B-1。"),
        name_tape("Research"),
        research,
        more,
        name_tape("News"),
        news,
        name_tape("Collaboration Contact"),
        contact,
        name_tape("College and Department"),
        family,
        actions(text_link("護理研究所中文網站", L("inst:A"))),
        owner=META["owner"],
    )
