from components import (page, name_tape, statement, p, h4, text_link, actions, photo, photo_slot, split, facts, draft,
                        note, todo)
from links import L
from pages._en_college_shared import zh, IMG_NW_VISIT, IMG_UW

META = {"id": "F-2", "slug": "highlights", "title": "Collaboration Highlights", "owner": "國際事務", "site": "en_college"}

# Two stories are named after unconfirmed carousel titles on the Chinese sites (see pages/G-1_partnerships.py):
# "西北大學參訪" and "N75學生至美國華盛頓大學交流". Titles are draft; every detail is a slot.

ASK = "（國際事務提供）"


def _story(title, pic, rows):
    """pic: a published photo() or a photo_slot() still to be filled."""
    return split(
        pic,
        "".join([
            h4(title),
            facts([(k, v) for k, v in rows if v]),  # todo() is empty in the final build, so unfilled rows drop out
        ]),
        cols=(5, 7), align="start",
    )


def _rows(partner, *extra):
    return [
        ("Partner", partner),
        *extra,
        ("Date", todo("日期" + ASK)),
        ("What happened", todo("交流內容 2–3 句" + ASK)),
        ("Outputs", todo("產出，例如講座、共同論文、合作備忘錄" + ASK)),
        ("Impact", todo("影響" + ASK)),
        ("Next steps", todo("下一步" + ASK)),
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
        _story(draft("Academic visits with Northwest University"),
               photo(IMG_NW_VISIT, "Group photo outdoors during the Northwest University (西北大學) visit", "4/3"),
               _rows(draft("Northwest University (西北大學)"), ("Country", todo("這所西北大學所在的國家與英文正式名稱" + ASK)))),
        _story(draft("Nursing students at the University of Washington"),
               photo(IMG_UW, "Nursing students and faculty at a care facility during the University of Washington exchange",
                     "4/3"),
               _rows(draft("University of Washington, USA"))),
    ])

    return page(
        opening,
        name_tape("Highlights", unit="inst"),
        note("前兩則標題取自輪播照片標題，尚未查證：「西北大學參訪」「西北大學來訪」（舊英文頁 uniten/100010/843 輪播，"
             "照片檔名 1140203NorthwestUniversity）請確認是哪一所西北大學及英文正式名稱；兩張照片取自現行輪播；"
             "「N75學生至美國華盛頓大學交流」英文版不用屆別代號，請提供年份。每則請國際事務提供：日期、交流內容（2–3 句）、"
             "產出（例如講座、共同論文、合作備忘錄）、影響與下一步，以及可公開的照片（照片中可辨識的人須取得同意）。"
             "護理研究所輪播另有「四國會議」「Trauma training 戰傷災難護理培訓」，若屬國際合作，請提供說明後新增為個案。"),
        stories,
        todo("其他合作個案：每則標題、合作單位、日期、內容、產出、影響、下一步與可公開的照片" + ASK),
        name_tape("Related Pages"),
        actions(text_link("International Collaboration", L("en:F")), text_link("Visit and Collaborate", L("en:G"))),
        owner=META["owner"],
    )
