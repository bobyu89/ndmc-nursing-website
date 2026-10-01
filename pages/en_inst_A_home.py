from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, photo,
                        ribbon_bar, split, unit_pair, feature_lead, feature_list, route_list, bullets, facts, draft,
                        note)
from links import L
from tokens import C
from pages._en_inst_data import (TRAUMA_PROJECTS, project_items, name, position, email_link, INST_PHONE, ADDRESS,
                                 IMG_DIRECTOR)

META = {"id": "A", "slug": "home", "title": "Graduate Institute of Nursing", "owner": "院窗口", "site": "en_inst"}

# Structure mirrors pages/inst_A_home.py. Verified facts reused:
#   founded 1979, pioneer of master's nursing education in Taiwan — 歷史沿革 unit/100181/6527;
#   ("the first graduate nursing program in Taiwan" on the old English page uniten/100010/3353 is not used until
#   院窗口 confirms it; every site uses the hedged "pioneer" wording)
#   director's name and position — DocDetEn/191/100010/3351/4443; portrait — same photo as inst_A_home.py
#   project titles — faculty DocDetEn profiles (see pages/_en_inst_data.py)


def render():
    opening = split(
        "".join([
            statement(
                draft("A pioneer of master's-level nursing education in Taiwan since 1979."),
                draft("The Graduate Institute of Nursing at National Defense Medical University, Taipei, educates "
                      "nurses who ask clinical questions, study them, and bring the evidence back to patient care."),
            ),
            actions(button("Research Collaboration", L("en_inst:E")),
                    text_link("About the Institute", L("en_inst:B"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch(
            "Graduate Institute of Nursing", "護理研究所", unit="inst",
            illo=illo_slot("Graduate nurse and supervisor reviewing data together (CocoMaterial, recolored)", "1/1",
                           unit="inst"),
            tab="College of Nursing", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    # Audience router: each ribbon is a reader; the sub-line says what is behind it. The Chinese site link
    # lives here only (no separate 中文 links in the opening or at the foot of the page).
    quick = ribbon_bar([
        ("Visiting scholars", L("en_inst:E-2"), "Short visits"),
        ("Collaborators", L("en_inst:E-1"), "Areas to work on"),
        ("Nurse researchers", L("en_inst:D-1"), "Faculty by area"),
        ("中文", L("inst:A"), "護理研究所中文網站"),
    ])

    director = split(
        photo(IMG_DIRECTOR, "Professor Hsueh-Hsing Pan, Director of the Graduate Institute of Nursing", "3/4"),
        "".join([
            p("The Institute was established in 1979 to meet the needs of nursing education and research, "
              "and became a pioneer of master's-level nursing education in Taiwan."),
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
        illo_slot("Combat casualty care simulation (CocoMaterial, recolored)", "1/1", unit="inst"),
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
        actions(text_link("Publications", L("en_inst:D-2")),
                text_link("Academic Activities", L("en_inst:D-3"))),
    ])

    news = "".join([
        note("首頁為靜態 HTML，無法自動帶入消息；以英文消息頁導流。英文消息只放研究亮點、論文發表、研究生成果、"
             "學術活動與國際學術交流，不放招生、課務、口試、獎學金公告。"),
        route_list([
            ("News", draft("Research highlights, publications, graduate achievements and seminars"), L("en_inst:F")),
        ], unit="inst"),
    ])

    contact = "".join([
        p(draft("Researchers and institutions interested in working with us can write to the College of Nursing "
                "office. Please tell us your research theme and the kind of collaboration you have in mind.")),
        facts([
            ("Email", email_link()),
            ("Phone", INST_PHONE),
            ("Address", ADDRESS),
        ]),
    ])

    family = unit_pair([
        ("college", "College of Nursing", "Faculty directory, research, visits", L("en:A")),
        ("dept", "Department of Nursing", "Undergraduate program and practicum", L("en_dept:A")),
    ])

    return page(
        opening,
        note("1979 年的寫法全站統一為「a pioneer of master's-level nursing education in Taiwan」（依研究所〈歷史沿革〉）。"
             "學院舊英文頁（uniten/100010/3353）寫「In 1979, we established the first graduate nursing program in Taiwan」，"
             "請院窗口確認能否對外寫「Taiwan's first graduate nursing program」（需有可查證的依據）；確認前一律用 pioneer 的說法。"),
        quick,
        name_tape("Director and Institute"),
        director,
        name_tape("Research"),
        research,
        more,
        name_tape("News"),
        news,
        name_tape("Collaboration Contact"),
        contact,
        name_tape("College and Department"),
        family,
        owner=META["owner"],
    )
