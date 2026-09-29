from components import (page, name_tape, statement, p, text_link, actions, bullets, facts, split, photo_slot,
                        draft, note)
from links import L
from pages._en_college_shared import zh, email_link

META = {"id": "G-1", "slug": "academic-visits", "title": "Academic Visits", "owner": "國際事務", "site": "en_college"}

# Facility names: pages/E-3_facilities.py (verified). Contact: pages/K_contact.py (verified).
# Visit activities and inquiry checklist are our draft; the College has no published visit procedure yet.


def render():
    opening = "".join([
        statement(
            draft("Short visits for academic delegations."),
            draft("Delegations from universities, hospitals and health agencies can visit the College to meet faculty, "
                  "see our teaching facilities and discuss collaboration."),
        ),
        actions(text_link("Visit and Collaborate", L("en:G")), zh("G")),
    ])

    activities = split(
        "".join([
            p(draft("A visit may include:")),
            bullets([
                draft("An introduction to the College and military nursing education"),
                draft("Meetings with faculty whose research matches your interests"),
                draft("A tour of teaching facilities"),
                draft("A lecture or seminar by a visiting guest"),
            ]),
            p("Facilities: Simulation Center, Demonstration Classroom, Demonstration Ward, "
              "Smart Interactive Nursing Self-Learning Classroom."),
            actions(text_link("Facilities", L("en:D-3"))),
        ]),
        photo_slot("Visiting delegation in the Simulation Center (to be supplied)", "4/3"),
        cols=(7, 5), align="start",
    )

    inquiry = bullets([
        draft("Your institution and the purpose of the visit"),
        draft("Proposed dates and length of stay"),
        draft("Number of visitors, with names and titles"),
        draft("Topics you would like to discuss, or faculty you would like to meet"),
        draft("A contact person with email"),
    ])

    contact = facts([
        ("Email", email_link()),
        ("Lead time", "〔How many weeks before the visit to write〕"),
        ("Reply", "〔Expected reply time〕"),
    ])

    return page(
        opening,
        name_tape("What a Visit Can Include"),
        activities,
        note("來訪活動清單為暫擬；請國際事務確認可安排的活動、參觀設施是否對外開放、是否需要校方或國防部核准（例如境外人士入營區的申請程序），"
             "以及提前申請的週數與回覆時間。未確認前表格保持空格。"),
        name_tape("What to Include in Your Inquiry"),
        inquiry,
        name_tape("Contact"),
        contact,
        actions(text_link("Collaboration Contact", L("en:G-3")), text_link("Visiting Scholars", L("en:G-2"))),
        owner=META["owner"],
    )
