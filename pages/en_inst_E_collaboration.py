from components import (page, name_tape, statement, p, button, text_link, actions, feature_list, route_list, facts,
                        split, illo_slot, draft, note)
from links import L
from pages._en_inst_data import name, email_link, INST_PHONE, ADDRESS

META = {"id": "E", "slug": "collaboration", "title": "Research Collaboration", "owner": "國際事務", "site": "en_inst"}

# Themes group the specialties on the official English faculty profiles (see D-1); theme wording and the
# collaboration formats are drafts. Contact route from pages/K_contact.py. No Chinese counterpart page exists.


def render():
    opening = "".join([
        statement(
            draft("Work with us on nursing research that matters in the field."),
            draft("We welcome researchers and institutions who share our interests in military, trauma and disaster "
                  "nursing, mental health, chronic illness, and family health. Start with a theme, then write to us."),
        ),
        actions(button("Collaboration Contact", L("en_inst:E-3")),
                text_link("Areas for Collaboration", L("en_inst:E-1"))),
    ])

    themes = feature_list([
        (draft("Military health, trauma and disaster nursing"),
         f"{name('pan')}, {name('chiang')}, {name('lan')}, {name('wang')}, {name('tlin')}", None, "inst", "T"),
        (draft("Mental health and digital health"),
         f"{name('tzeng')}, {name('feng')}, {name('ho')}", None, "inst", "M"),
        (draft("Chronic illness, critical and cardiovascular care"),
         f"{name('clin')}, {name('chenyj')}, {name('huang')}, {name('chenpc')}", None, "inst", "C"),
        (draft("Women's, children's and family health"),
         f"{name('liaw')}, {name('cxlin')}, {name('liu')}", None, "inst", "F"),
    ])

    formats = split(
        "".join([
            p(draft("Collaboration can take several forms, depending on the theme and the people involved:")),
            route_list([
                (draft("Joint research projects"), draft("Shared questions, data collection or analysis"),
                 L("en_inst:E-1")),
                (draft("Visiting researcher stays"), draft("Short, non-degree research visits, subject to review"),
                 L("en_inst:E-2")),
                (draft("Seminars and lectures"), draft("Talks for faculty and graduate students"), L("en_inst:D-3")),
            ], unit="inst"),
        ]),
        illo_slot("Two researchers comparing notes across a table (CocoMaterial, recolored)", "4/3", unit="inst"),
        cols=(7, 5), align="start",
    )

    tasks = route_list([
        ("Areas for Collaboration", draft("Priority themes, expertise and example outputs"), L("en_inst:E-1")),
        ("Visiting Researchers", draft("Non-degree research visits: activities and what to send"), L("en_inst:E-2")),
        ("Collaboration Contact", draft("One inquiry point and what happens next"), L("en_inst:E-3")),
    ], unit="inst")

    contact = "".join([
        facts([
            ("Email", email_link()),
            ("Phone", INST_PHONE),
            ("Address", ADDRESS),
        ]),
        p(draft("Please write in English or Chinese, and tell us your research theme, the activity you propose and "
                "your preferred dates."), muted=True),
    ])

    return page(
        opening,
        name_tape("Themes and Faculty"),
        themes,
        note("主題分類與教師對應依官方英文個人頁專長整理，為草稿；請國際事務與教發確認哪些主題對外開放合作，以及每個主題的聯絡老師。"),
        name_tape("Ways to Collaborate"),
        formats,
        note("合作形式為草稿。請國際事務確認本所實際接受的合作形式（例如共同研究、訪問研究員、合辦研討會、共同指導研究生），"
             "以及是否需經校級審查或簽訂合作備忘錄。英文站只呈現成果與洽詢，不做學位招生。"),
        name_tape("Start Here"),
        tasks,
        name_tape("Inquiries"),
        contact,
        actions(text_link("College of Nursing: Visit and Collaborate", L("en:G"))),
        owner=META["owner"],
    )
