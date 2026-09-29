from components import page, name_tape, statement, p, text_link, actions, bullets, facts, draft, note
from links import L
from pages._en_college_shared import zh, email_link

META = {"id": "G-2", "slug": "visiting-scholars", "title": "Visiting Scholars", "owner": "國際事務", "site": "en_college"}

# Non-degree scholarly visits only. No verified visiting-scholar scheme exists on the Chinese site, so all copy is draft;
# the contact route is the verified College office email (pages/K_contact.py).


def render():
    opening = "".join([
        statement(
            draft("Research and teach with us for a while."),
            draft("Faculty and researchers from other institutions can propose a non-degree visit to do research, "
                  "teach or exchange ideas with our faculty. Every visit is subject to review."),
        ),
        actions(text_link("Faculty Directory", L("en:D-1")), zh("G-1")),
    ])

    what = "".join([
        p(draft("A visiting scholar stay may include:")),
        bullets([
            draft("Joint research with a host faculty member"),
            draft("Guest lectures or seminars for students and faculty"),
            draft("Exchange on teaching, simulation-based education or clinical practice"),
        ]),
        p(draft("This is not a degree program and does not lead to a qualification.")),
    ])

    matching = "".join([
        p(draft("Each visit is built around a host faculty member whose research matches yours. "
                "Please look through the Faculty Directory and Research Highlights, and name a possible host in your inquiry.")),
        actions(text_link("Faculty Directory", L("en:D-1")), text_link("Research Highlights", L("en:D-2"))),
    ])

    review = "".join([
        p(draft("All proposals are reviewed by the College and the University before a visit is confirmed.")),
        facts([
            ("Eligibility", "〔Who may apply〕"),
            ("Length of stay", "〔Minimum and maximum〕"),
            ("Review", "〔Who reviews and how long it takes〕"),
            ("Support", "〔Office space, library access, accommodation, if any〕"),
        ]),
    ])

    inquiry = "".join([
        bullets([
            draft("A short CV and your current affiliation"),
            draft("Your proposed research or teaching plan"),
            draft("Proposed dates and length of stay"),
            draft("A possible host faculty member"),
        ]),
        facts([("Email", email_link())]),
    ])

    return page(
        opening,
        name_tape("What a Visit Involves", unit="inst"),
        what,
        name_tape("Finding a Host", unit="inst"),
        matching,
        name_tape("Review", unit="inst"),
        review,
        note("國際事務請提供：訪問學者的資格、停留期間、審查流程與所需時間（院內、校方、是否需國防部核准）、可提供的支援"
             "（研究空間、圖書館、住宿）。沒有既定辦法的項目請刪除，不要寫推測內容。"),
        name_tape("How to Inquire"),
        inquiry,
        owner=META["owner"],
    )
