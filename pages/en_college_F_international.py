from components import (page, name_tape, statement, p, text_link, actions, photo, split, feature_list, facts,
                        route_list, draft, note, todo)
from links import L
from pages._en_college_shared import zh, mark, IMG_UW

META = {"id": "F", "slug": "international", "title": "International Collaboration", "owner": "國際事務", "site": "en_college"}

# No partner, date or figure on this page is verified yet. The only collaboration items on the Chinese site are two
# unconfirmed carousel titles ("西北大學參訪", "N75學生至美國華盛頓大學交流"; see pages/G-1_partnerships.py),
# so both stay draft. The photo is the published Department carousel photo of the University of Washington exchange. Outcomes only; visits and inquiries live under Visit and Collaborate (G).



def render():
    opening = "".join([
        statement(
            draft("Nursing is learned everywhere. We learn with partners abroad."),
            draft("The College exchanges visits, students and scholars with nursing schools abroad. "
                  "This page shows what those partnerships have produced."),
        ),
        actions(text_link("Partnership Map", L("en:F-1")), text_link("Collaboration Highlights", L("en:F-2")), zh("G")),
    ])

    lead = split(
        photo(IMG_UW, "Nursing students and faculty at a care facility during the University of Washington exchange", "4/3",
              caption="Student exchange with the University of Washington"),
        "".join([
            p(draft("Recent exchanges include academic visits with Northwest University (西北大學) and a student "
                    "exchange with the University of Washington in the United States.")),
            note("兩則交流取自輪播照片標題：「西北大學參訪」「西北大學來訪」（舊英文頁 uniten/100010/843，照片檔名 "
                 "1140203NorthwestUniversity）與「N75學生至美國華盛頓大學交流」（護理學系首頁）。"
                 "請國際事務確認：是哪一所「西北大學」及其英文正式名稱、交流時間、參與者與內容；英文版不使用 N75 這類屆別代號。"),
        ]),
        cols=(5, 7), align="start",
    )

    types = feature_list([
        ("Student exchange", draft("Short-term inbound and outbound exchanges for nursing students."),
         None, "dept", mark("users")),
        ("Academic visits", draft("Delegation visits between the College and partner schools."),
         None, "college", mark("handshake-o")),
        ("Visiting scholars", draft("Scholars from abroad who lecture, teach or do research with our faculty."),
         None, "inst", mark("user")),
        ("Joint research", draft("Research projects and publications with partner institutions."),
         None, "inst", mark("flask")),
    ])

    outcomes = "".join([
        todo("合作數字與統計期間：盟校數、國家與地區數、合作備忘錄數、交換學生數、來訪學者數、共同發表數（國際事務提供）"),
        note("請國際事務提供上列各項數字與統計期間（例如近五學年），每項附資料來源；沒有資料的列刪除，不要估計。"),
    ])

    return page(
        opening,
        name_tape("Overview", unit="inst"),
        lead,
        name_tape("Types of Collaboration", unit="inst"),
        types,
        todo("每種合作類型各一句實例（國際事務提供）"),
        note("四種合作類型為暫擬，請國際事務依實際有的項目增刪，並為每類補一句實例。"),
        *([name_tape("Outcomes in Numbers", unit="inst"), outcomes] if outcomes else []),
        name_tape("Explore"),
        route_list([
            ("Global Partnership Map", draft("Partner institutions by country and region"), L("en:F-1")),
            ("Collaboration Highlights", draft("Case stories from visits and joint projects"), L("en:F-2")),
            ("Visit and Collaborate", draft("Plan a visit or propose a collaboration"), L("en:G")),
        ], unit="inst"),
        owner=META["owner"],
    )
