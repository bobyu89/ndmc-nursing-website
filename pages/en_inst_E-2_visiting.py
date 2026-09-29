from components import (page, name_tape, statement, p, text_link, actions, bullets, facts, split, photo_slot,
                        route_list, draft, note)
from links import L
from pages._en_inst_data import email_link

META = {"id": "E-2", "slug": "visiting-researchers", "title": "Visiting Researchers", "owner": "國際事務",
        "site": "en_inst"}

# No verified policy for visiting researchers exists on the current sites: every statement about eligibility,
# activities and review is a draft for 國際事務 to confirm. Contact route from pages/K_contact.py.


def render():
    opening = "".join([
        statement(
            draft("Spend time with us as a visiting researcher."),
            draft("The Institute can host researchers for short, non-degree visits built around a shared research "
                  "interest. Every visit is arranged with a faculty host and is subject to the university's review."),
        ),
        actions(text_link("Collaboration Contact", L("en_inst:E-3")),
                text_link("College of Nursing: Visiting Scholars", L("en:G-2"))),
    ])

    activities = split(
        "".join([
            p(draft("Depending on your aims and the host's work, a visit may include:")),
            bullets([
                draft("Joint work on a research project, data analysis or a manuscript"),
                draft("A seminar or lecture for faculty and graduate students"),
                draft("Visits to the simulation center and, with approval, to Tri-Service General Hospital"),
                draft("Meetings with faculty working in related areas"),
            ]),
        ]),
        photo_slot("Visiting researcher with Institute faculty (to be supplied, with consent)", "4/3"),
        cols=(7, 5), align="start",
    )

    matching = "".join([
        p(draft("We match each visitor with a faculty host whose research is closest to the proposed work. "
                "Please look at our research areas first and tell us which area and faculty member fit best.")),
        route_list([
            ("Research Areas and Faculty", draft("Who works on what"), L("en_inst:D-1")),
            ("Areas for Collaboration", draft("Priority themes and example outputs"), L("en_inst:E-1")),
        ], unit="inst"),
    ])

    inquiry = "".join([
        p(draft("Please include the following in your first email:")),
        facts([
            (draft("About you"), draft("Name, position, institution, and a short CV or profile link")),
            (draft("Research theme"), draft("The question or topic you want to work on, and the area it fits")),
            (draft("Proposed activity"), draft("What you would like to do during the visit")),
            (draft("Dates"), draft("Preferred dates and length of stay")),
            (draft("Funding"), draft("How the visit will be funded")),
        ]),
        p("Email:"),
        actions(email_link()),
    ])

    review = "".join([
        p(draft("Visits are confirmed only after review by the Institute and the university. Allow enough time "
                "before your planned dates.")),
    ])

    return page(
        opening,
        note("本頁所有規定均為草稿：現行網站查無訪問研究員的正式規定。請國際事務提供：可接受的訪問類型與期間、"
             "校內審查流程與所需時間、是否需要邀請函或合作備忘錄、訪客可使用的空間與設備、三總參訪的核准方式、"
             "費用與保險，以及是否已有訪問研究員的前例（可公開者附年份、學校、主題與照片）。"),
        name_tape("What a Visit Can Include"),
        activities,
        name_tape("Finding a Faculty Host"),
        matching,
        name_tape("How to Inquire"),
        inquiry,
        name_tape("Review"),
        review,
        note("審查時程、需要幾週前提出申請，請國際事務提供確切說明後替換上段。本頁不處理學位申請；學位招生不在英文站範圍。"),
        owner=META["owner"],
    )
