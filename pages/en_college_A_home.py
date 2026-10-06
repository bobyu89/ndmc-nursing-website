from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, photo,
                        ribbon_bar, split, unit_pair, feature_lead, feature_list, route_list, facts, draft, note, todo)
from links import L
from tokens import C
from pages._en_college_shared import mark, email_link, ADDRESS, DEAN_PHOTO

META = {"id": "A", "slug": "home", "title": "College of Nursing", "owner": "院窗口", "site": "en_college"}

# Structure follows pages/A_home.py. Verified facts reused (plain text):
#   1943 / 1947 / 1949 / 1979 / 2025 milestones — pages/C-3_history.py (歷史沿革 unit/100010/6804)
#   teaching hospital Tri-Service General Hospital — pages/F_admissions.py (115 正期班簡章)
#   two academic units — pages/C-4_organization.py
#   Dean's English name and title — official English profile /DocDetEn/191/100010/3351/4416
#   Simulation Center use (OSCE, advanced courses) — pages/E-3_facilities.py


def render():
    opening = split(
        "".join([
            statement(
                draft("Where nurses are also officers."),
                draft("The College of Nursing at National Defense Medical University educates military nurses "
                      "for care in hospitals, in the field and in disasters. Its roots go back to 1943, "
                      "and its students train clinically at Tri-Service General Hospital."),
            ),
            actions(button("Visit and Collaborate", L("en:G")), text_link("About the College", L("en:B"))),
        ]),
        '<div class="mx-auto d-none d-md-block" style="width:72%;max-width:320px;">' + patch(
            "College of Nursing", "護理學院", unit="college",
            illo=illo_slot("A nurse in uniform (CocoMaterial, recolored)", "1/1"),
            tab="NDMU", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    # Audience router: each ribbon is a reader; the sub-line says what is behind it. The Chinese site link
    # lives here only (no separate 中文 links in the opening or at the foot of the page). Delegations reach
    # Academic Visits through the primary button (Visit and Collaborate), so they get no ribbon of their own.
    quick = ribbon_bar([
        ("Visiting scholars", L("en:G-2"), "Research or teach"),
        ("Partner schools", L("en:F"), "Partnership results"),
        ("Exchange students", L("en_dept:E"), "Exchange stories"),
        ("中文", L("A"), "護理學院中文網站"),
    ])

    quick_facts = "".join([
        facts([
            ("Origins", "1943: the Senior Nursing Vocational Class, founded by General Mei-Yu Chow in Jiangwan, Shanghai"),
            ("Department", "1947: the Department of Nursing, the country's first institution of higher nursing education"),
            ("Institute", "1979: the Graduate Institute of Nursing, a pioneer of master's-level nursing education in Taiwan"),
            ("College", "2025: the College of Nursing is established"),
            ("Units", "Department of Nursing (undergraduate); Graduate Institute of Nursing (graduate)"),
            ("Teaching hospital", "Tri-Service General Hospital"),
            ("Campus", "Neihu District, Taipei, Taiwan"),
        ]),
        note("Quick Facts 只放已查證的年份與名稱。學生數、專任教師數、畢業生數等數字，請院窗口依《護理學院年報》提供（附統計日期）後再加；"
             "舊英文頁（uniten/100010/3353）的畢業生人數 2,135／441／10 未註明統計年份，未採用。"),
    ])

    dean = split(
        photo(DEAN_PHOTO, "Dean Wen-Chii Tzeng", "3/4"),
        "".join([
            todo("院長的話英文摘錄兩句，談學院的辦學方向（三長提供，與中文首頁同一段）"),
            p("Wen-Chii Tzeng, Distinguished Professor and Dean", muted=True),
            actions(text_link("Dean's Message", L("en:B-1")), text_link("Overview and History", L("en:B-2"))),
        ]),
        cols=(3, 9), align="start",
    )

    lead = feature_lead(
        "Military nursing",
        [p(draft("Military nursing is what sets the College apart: keeping care safe and effective in field, "
                 "shipboard, aviation and disaster settings. Teaching combines military training with clinical practice."))],
        illo_slot("Field casualty care scene (CocoMaterial, recolored)", "1/1"),
        href=L("en_dept:C-2"), link_label="Clinical and Military Nursing Practicum",
    )
    others = feature_list([
        ("Trauma and disaster nursing",
         draft("Combat casualty care, mass-casualty response and disaster preparedness in teaching and research."),
         None, "college", mark("medkit")),
        ("Simulation-based learning",
         "The Simulation Center is used for advanced medical-surgical, obstetric and pediatric, and critical care courses, "
         "and the undergraduate OSCE. " + text_link("Facilities", L("en:D-3")),
         None, "dept", mark("heartbeat")),
        ("International collaboration",
         draft("Academic visits, visiting scholars and exchanges with nursing schools abroad.") + " "
         + text_link("Global Partnership Map", L("en:F-1")),
         None, "inst", mark("globe")),
    ])

    units = unit_pair([
        ("dept", "Department of Nursing", "Undergraduate program", L("en_dept:A")),
        ("inst", "Graduate Institute of Nursing", "Graduate programs and research", L("en_inst:A")),
    ])

    news = "".join([
        note("首頁為靜態 HTML，無法自動帶入消息；以英文消息頁導流。英文消息只放研究、國際合作、來訪與重大院務，不放招生與校內行政公告。"),
        route_list([
            ("News", draft("Research, international collaboration, visits and major College updates"), L("en:H")),
            ("Collaboration Highlights", draft("Stories from partnerships and visits"), L("en:F-2")),
        ]),
    ])

    contact = "".join([
        facts([
            ("Email", email_link()),
            ("Address", ADDRESS),
        ]),
        actions(text_link("Collaboration Contact", L("en:G-3")), text_link("Faculty Directory", L("en:D-1"))),
    ])

    return page(
        opening,
        quick,
        name_tape("Quick Facts"),
        quick_facts,
        name_tape("The Dean"),
        dean,
        name_tape("What We Are Known For"),
        lead,
        others,
        name_tape("Academic Units"),
        p(draft("Each unit keeps its own English site; the College site holds the full faculty directory "
                "and international collaboration.")),
        units,
        name_tape("News"),
        news,
        name_tape("Contact"),
        contact,
        owner=META["owner"],
    )
