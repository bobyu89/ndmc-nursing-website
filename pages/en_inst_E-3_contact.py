from components import (page, name_tape, statement, p, button, text_link, actions, facts, bullets, route_list,
                        photo_slot, draft, note)
from links import L
from pages._en_inst_data import (EMAIL, MAILTO, TEL, MAP, ADDRESS, PHONE, INST_PHONE, FAX, email_link, zh)

META = {"id": "E-3", "slug": "contact", "title": "Collaboration Contact", "owner": "國際事務、院窗口",
        "site": "en_inst"}

# Contact facts verbatim from pages/K_contact.py (current 聯絡我們 page, unit/100010/2199; English address from the
# same page). Institute extension 18165 from pages/F_admissions.py. Office hours are not published for the College,
# so they stay draft.


def render():
    opening = "".join([
        statement(
            draft("One address for research inquiries."),
            draft("Research collaboration and visit inquiries for the Graduate Institute of Nursing go to the "
                  "College of Nursing office, which forwards them to the right faculty member."),
        ),
        actions(button("Email Us", MAILTO), zh("inst:A", "中文")),
    ])

    details = facts([
        ("Telephone", f"{PHONE}<br>{text_link('Call the College office', TEL)}"),
        ("Institute", INST_PHONE),
        ("Fax", FAX),
        ("Address", ADDRESS),
        ("Hours", draft("Monday to Friday, 8:00–17:00 Taiwan time (UTC+8), except public holidays")),
    ])

    include = "".join([
        p(draft("To help us reply quickly, please include:")),
        bullets([
            draft("Your name, position and institution"),
            draft("The research theme, and the faculty member or area you have in mind"),
            draft("The activity you propose: joint research, a visit, a seminar or something else"),
            draft("Preferred dates"),
        ]),
    ])

    follow_up = "".join([
        p(draft("We acknowledge each inquiry, forward it to the relevant faculty member, and reply with next steps. "
                "Visits and formal agreements go through the university's review before they are confirmed.")),
    ])

    related = route_list([
        ("College of Nursing: Collaboration Contact", draft("College-wide partnerships and visits"), L("en:G-3")),
        ("Department of Nursing: Visit the Department", draft("Undergraduate teaching and simulation visits"),
         L("en_dept:G")),
        ("Visiting Researchers", draft("Non-degree research visits to the Institute"), L("en_inst:E-2")),
    ], unit="inst")

    return page(
        opening,
        name_tape("Contact Details"),
        p("Email:"),
        actions(email_link()),
        details,
        note("辦公時間：學院網站目前未公布，上方暫用學校網站頁尾的上班時間（週一至週五 8:00–17:00，不含例假日及國訂假日），"
             "請院窗口確認。請國際事務確認研究合作洽詢是否統一由學院信箱收件；若研究所另有對外英文窗口（職稱與公務信箱），"
             "請提供後替換。英文站不公開教師個人信箱。"),
        name_tape("What to Send"),
        include,
        name_tape("What Happens Next"),
        follow_up,
        note("請國際事務提供實際的回覆流程與預計回覆時間（例如幾個工作天內回覆），確認後替換上段草稿。"),
        name_tape("Finding Us"),
        photo_slot("College of Nursing building, Neihu campus", "16/9"),
        actions(text_link("Open in Google Maps", MAP)),
        name_tape("Related Contacts"),
        related,
        owner=META["owner"],
    )
