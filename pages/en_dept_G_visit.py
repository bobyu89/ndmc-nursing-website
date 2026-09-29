from components import (page, name_tape, statement, p, button, text_link, actions, split, photo_slot, facts,
                        feature_list, bullets, draft, note)
from links import L

META = {"id": "G", "slug": "visit", "title": "Visit the Department", "owner": "院窗口", "site": "en_dept"}

# Contact details: verbatim from 聯絡我們 unit/100010/2199 (pages/K_contact.py), incl. the English address.
# Facility facts: 教學設備 unit/100010/1463 (pages/E-3_facilities.py).
EMAIL = "ndmu_con@mail.ndmutsgh.edu.tw"
MAP = "https://maps.app.goo.gl/MpA4rsvwnFxdnaM37"


def render():
    opening = "".join([
        statement(
            draft("Come and see how we teach nursing."),
            draft("We welcome nursing educators, scholars and partner institutions who want to see our undergraduate "
                  "teaching, simulation and military nursing education at first hand."),
        ),
        actions(button("Email the College of Nursing", f"mailto:{EMAIL}"), text_link("中文：聯絡我們", L("K"))),
    ])

    themes = feature_list([
        ("Simulation-based teaching",
         "The simulation centre, used for OSCE teaching and advanced clinical courses, and the demonstration ward. "
         + draft("Visitors can observe a session from the control room when classes allow."), None, "dept", "S"),
        ("Military nursing education",
         draft("How military training and nursing education are combined in one undergraduate programme."),
         None, "dept", "M"),
        ("Curriculum and outcomes",
         draft("Curriculum design around the thirteen core abilities, and how outcomes are assessed."),
         None, "dept", "C"),
    ])

    format_ = split(
        "".join([
            p(draft("A typical visit is half a day: a short introduction to the department, a tour of the simulation "
                    "centre and demonstration ward, and a discussion with faculty on a shared theme.")),
            p(draft("Please send your inquiry at least one month before the proposed date. Visits to a military campus "
                    "need advance registration of every visitor.")),
            p(draft("Please include in your inquiry:")),
            bullets([
                draft("Your institution, and the names and roles of the visitors"),
                draft("Proposed dates and length of the visit"),
                draft("Themes you would like to discuss or observe"),
                draft("A contact person and email address"),
            ]),
        ]),
        photo_slot("Visitors in the simulation centre control room (4:3)", "4/3"),
        cols=(7, 5), align="start",
    )

    # The email sits below the table: an unbreakable address beside a nowrap label overflows a phone screen.
    contact = "".join([
        facts([
            ("Address", "College of Nursing, National Defense Medical University<br>"
                        "No.161, Sec. 6, Minquan E. Rd., Neihu Dist., Taipei City 11490, Taiwan (R.O.C.)"),
            ("Phone", "+886-2-8792-3100 ext. 88916, 18167, 18767, 18165<br>"
                      + text_link("Call the College", "tel:+886287923100")),
            ("Fax", "+886-2-6600-5702"),
            ("Map", text_link("Open in Google Maps", MAP)),
        ]),
        p("Email<br>" + text_link(EMAIL, f"mailto:{EMAIL}")),
    ])

    return page(
        opening,
        name_tape("What You Can See"),
        themes,
        name_tape("Planning a Visit"),
        format_,
        note("參訪形式、提前天數與入校登記為草稿。請院窗口確認：① 參訪受理單位（學院或學系）與承辦人職稱；"
             "② 需提前多久申請、訪客需提供哪些證件資料；③ 可開放參觀的空間與是否可觀課；④ 是否有英文參訪簡報。"),
        name_tape("Contact"),
        contact,
        note("地址、電話、傳真、信箱照錄中文「聯絡我們」頁（電話與傳真改為國際格式，傳真原文 886-2-66005702）。"
             "目前沒有學系專屬的英文聯絡窗口，暫用學院信箱；若學系另有窗口請提供。辦公時間待院窗口提供後補上。"),
        p(draft("For college-wide collaboration, visiting scholar arrangements and academic visits, see the "
                "College of Nursing's Visit and Collaborate page."), muted=True),
        actions(text_link("Visit and Collaborate (College)", L("en:G")),
                text_link("Simulation and Learning Spaces", L("en_dept:C-3"))),
        owner=META["owner"],
    )
