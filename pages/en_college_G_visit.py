from components import (page, name_tape, statement, p, button, text_link, actions, route_list, bullets, facts,
                        draft, note)
from links import L
from pages._en_college_shared import zh, email_link, MAILTO, ADDRESS

META = {"id": "G", "slug": "visit", "title": "Visit and Collaborate", "owner": "國際事務", "site": "en_college"}

# Not a degree-admissions page. The only contact route is the College office email,
# verbatim from pages/K_contact.py (聯絡我們 unit/100010/2199).


def render():
    opening = "".join([
        statement(
            draft("Come and see how military nurses are educated."),
            draft("We welcome academic delegations, visiting scholars and partners who want to work with us. "
                  "Choose the option that fits you, then write to the College office."),
        ),
        actions(button("Email the College", MAILTO), zh("G")),
    ])

    options = route_list([
        ("Academic Visits", draft("For delegations from universities, hospitals and health agencies planning a short visit"),
         L("en:G-1")),
        ("Visiting Scholars", draft("For faculty and researchers proposing a non-degree research or teaching stay"),
         L("en:G-2")),
        ("Collaboration Contact", draft("For institutions proposing joint research, exchange or other collaboration"),
         L("en:G-3")),
    ])

    themes = "".join([
        p(draft("Themes we can share with visitors and partners:")),
        bullets([
            draft("Military nursing"),
            draft("Trauma and disaster nursing"),
            draft("Simulation-based nursing education"),
            draft("The research interests of our faculty"),
        ]),
        actions(text_link("Research Highlights", L("en:D-2")), text_link("Faculty Directory", L("en:D-1"))),
    ])

    contact = "".join([
        facts([
            ("Email", email_link()),
            ("Address", ADDRESS),
        ]),
        p(draft("Please write in English or Chinese and tell us which option you are interested in."), muted=True),
    ])

    return page(
        opening,
        note("本頁不是學位招生頁：不放報名、學費、簽證或表單。聯絡窗口暫用學院信箱（聯絡我們頁已查證）；"
             "若國際事務有專用英文信箱或承辦人職稱，請提供後替換，全站只保留一個對外窗口。"),
        name_tape("Three Ways to Work With Us"),
        options,
        name_tape("Exchange Themes"),
        themes,
        note("交流主題為暫擬，依本院研究特色整理；請國際事務與教發確認可對外開放的主題。"),
        name_tape("One Contact"),
        contact,
        owner=META["owner"],
    )
