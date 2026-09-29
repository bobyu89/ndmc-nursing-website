from components import (page, name_tape, statement, p, h4, text_link, actions, photo_slot, split, facts, draft, note)
from links import L
from pages._en_college_shared import zh

META = {"id": "F-2", "slug": "highlights", "title": "Collaboration Highlights", "owner": "國際事務", "site": "en_college"}

# Two stories are named after unconfirmed carousel titles on the Chinese sites (see pages/G-1_partnerships.py):
# "西北大學參訪" and "N75學生至美國華盛頓大學交流". Titles are draft; every detail is a slot.

SLOT = "〔to be supplied〕"


def _story(title, photo, rows):
    return split(
        photo_slot(photo, "4/3"),
        "".join([
            h4(title),
            facts(rows),
        ]),
        cols=(5, 7), align="start",
    )


def _rows(partner):
    return [
        ("Partner", partner),
        ("Date", SLOT),
        ("What happened", SLOT),
        ("Outputs", SLOT),
        ("Impact", SLOT),
        ("Next steps", SLOT),
    ]


def render():
    opening = "".join([
        statement(
            draft("Stories from our partnerships."),
            draft("Each story tells who we worked with, when, what we did together, what came of it and what comes next."),
        ),
        actions(text_link("Partnership Map", L("en:F-1")), zh("G-1")),
    ])

    stories = "".join([
        _story(draft("A visit to Northwestern University"),
               "Northwestern University visit (to be supplied)",
               _rows(draft("Northwestern University") + " 〔country〕")),
        _story(draft("Nursing students at the University of Washington"),
               "Student exchange at the University of Washington (to be supplied and cleared for publication)",
               _rows(draft("University of Washington, USA"))),
        _story("〔Story title〕", "Collaboration photo (to be supplied)", _rows("〔Partner institution〕")),
    ])

    return page(
        opening,
        name_tape("Highlights", unit="inst"),
        note("前兩則標題取自輪播照片標題，尚未查證：「西北大學參訪」請確認是哪一所西北大學（美國 Northwestern University 或其他）；"
             "「N75學生至美國華盛頓大學交流」英文版不用屆別代號，請提供年份。每則請國際事務提供：日期、交流內容（2–3 句）、"
             "產出（例如講座、共同論文、合作備忘錄）、影響與下一步，以及可公開的照片（照片中可辨識的人須取得同意）。"
             "護理研究所輪播另有「四國會議」「Trauma training 戰傷災難護理培訓」，若屬國際合作，請提供說明後新增為個案。"),
        stories,
        name_tape("Related Pages"),
        actions(text_link("International Collaboration", L("en:F")), text_link("Visit and Collaborate", L("en:G"))),
        owner=META["owner"],
    )
