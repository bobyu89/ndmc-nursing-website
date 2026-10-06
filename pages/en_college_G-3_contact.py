from components import (page, name_tape, statement, p, button, text_link, actions, bullets, facts, route_list,
                        draft, note, todo)
from links import L
from pages._en_college_shared import zh, email_link, MAILTO, TEL, MAP, ADDRESS, PHONE, FAX

META = {"id": "G-3", "slug": "contact", "title": "Collaboration Contact", "owner": "國際事務", "site": "en_college"}

# Contact details: verbatim from pages/K_contact.py (聯絡我們 unit/100010/2199), including the English address.
# Inquiry types and response process are draft; reply time is a slot.


def render():
    opening = "".join([
        statement(
            draft("One contact for every collaboration inquiry."),
            draft("Write to the College office. We will pass your message to the right faculty member or unit."),
        ),
        actions(button("Email the College", MAILTO), zh("K")),
    ])

    contact = facts([
        ("Email", email_link()),
        ("Phone", PHONE + "<br>" + text_link("Call the College", TEL)),
        ("Fax", FAX),
        ("Address", ADDRESS + "<br>" + text_link("Open in Google Maps", MAP)),
    ])

    types = route_list([
        ("Academic visits", draft("Short delegation visits"), L("en:G-1")),
        ("Visiting scholars", draft("Non-degree research or teaching stays"), L("en:G-2")),
        ("Research collaboration", draft("Joint projects, publications or grant proposals"), L("en:D-2")),
        ("Institutional partnerships", draft("Agreements and exchange with partner institutions"), L("en:F")),
    ])

    what = bullets([
        draft("Your name, title and institution"),
        draft("The type of inquiry and a short description"),
        draft("Proposed dates, if any"),
        draft("Faculty members or themes you are interested in"),
    ])

    process = "".join([
        p(draft("The College office confirms receipt, forwards the inquiry to the relevant faculty member or unit, "
                "and replies with next steps.")),
        todo("預計回覆的工作天數（國際事務提供），收到後列為 Expected reply 一列"),
    ])

    return page(
        opening,
        name_tape("Contact Point"),
        contact,
        note("聯絡資料逐字取自中文「聯絡我們」頁。若國際事務有專責英文窗口（職稱、信箱、分機），請提供後改為唯一窗口；"
             "中文頁的分機尚未分工，英文版照列。辦公時間中文頁仍待補，英文版暫不列。"),
        name_tape("Inquiry Types"),
        types,
        name_tape("What to Send"),
        what,
        name_tape("What Happens Next"),
        process,
        note("回覆流程與回覆天數請國際事務確認；未確認前正式版不列。"),
        name_tape("Related Units"),
        route_list([
            ("Department of Nursing", draft("Visits focused on undergraduate teaching and simulation"), L("en_dept:G")),
            ("Graduate Institute of Nursing", draft("Research collaboration with the Institute"), L("en_inst:E-3")),
        ]),
        owner=META["owner"],
    )
