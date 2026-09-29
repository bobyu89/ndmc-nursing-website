from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, feature_list,
                        tape_surface, draft, note)
from links import L

META = {"id": "E", "slug": "exchange", "title": "International Exchange", "owner": "國際事務", "site": "en_dept"}

# No partner or exchange record is verified yet. Names below come only from photo captions:
#   "N75學生至美國華盛頓大學交流" — department home carousel (unit/100180/6510)
#   "西北大學參訪" / "西北大學來訪" / "八王子3" — English orphan page carousel (uniten/100010/843)
#   Thammasat (泰國法政) — 中文內容清單 dept I-3 note only
# All stay draft() until 國際事務 confirms.


def render():
    opening = "".join([
        statement(
            draft("Nursing students who learn across borders."),
            draft("Selected exchange outcomes: where our students went, who visited us, and what both sides "
                  "took home. This is a record of exchange, not an application page."),
        ),
        actions(text_link("Visit and collaborate with the College", L("en:G")), text_link("中文：海外交流專區", L("dept:H"))),
    ])

    outbound = split(
        "".join([
            p(draft("Students of the department have visited the University of Washington in the United States "
                    "for an exchange program.")),
            p(draft("Each outbound visit records the host institution, dates, participants and learning focus.")),
        ]),
        photo_slot("Students at the University of Washington (to be confirmed for publication)", "4/3"),
        cols=(7, 5), align="start",
    )

    inbound = feature_list([
        (draft("Northwestern University"), draft("Visits between the college and Northwestern University."),
         None, "dept", "N"),
        (draft("Hachioji, Japan"), draft("Student exchange with an institution in Hachioji, Japan."),
         None, "dept", "H"),
        (draft("Thammasat University, Thailand"), draft("Visiting nursing students from Thammasat University."),
         None, "dept", "T"),
    ])

    reflection = tape_surface(
        p(draft("“A reflection of three or four sentences from a participant: where they went, what they saw, "
                "what they brought back to their practice.”")),
        p("[Participant name]　[Year of entry]　[Host institution]", muted=True),
    )

    return page(
        opening,
        note("本頁所有交流對象目前都未經確認，一律標待確認。請國際事務逐項確認後才能拿掉標記。"),
        name_tape("Outbound Exchange"),
        outbound,
        note("來源：學系首頁輪播「N75學生至美國華盛頓大學交流」。請國際事務提供：交流年份、天數、參加人數、學習內容、"
             "可公開照片。屆別代號 N75 請改為入學年份。"),
        name_tape("Visitors and Partners"),
        inbound,
        note("三筆皆未確認：① 西北大學——英文孤兒頁輪播有「西北大學參訪」「西北大學來訪」，請確認是美國 Northwestern University "
             "還是其他「西北大學」，以及是參訪還是來訪、年份；② 八王子——輪播只有「八王子3」，請提供學校全名與交流內容；"
             "③ 泰國法政大學（Thammasat）——僅見於內容清單「境外學生來校交流」備註。未確認者請整列刪除。"),
        name_tape("Participant Reflections"),
        reflection,
        note("請國際事務收集 1〜2 篇參與者心得（英文 80 字內），取得本人同意公開姓名與照片。"),
        name_tape("Gallery"),
        split(photo_slot("Exchange activity photo 1 (with English caption)", "4/3"),
              photo_slot("Exchange activity photo 2 (with English caption)", "4/3"), cols=(6, 6), align="start"),
        p(draft("Institutions interested in visits or collaboration can contact the College of Nursing."), muted=True),
        actions(text_link("Visit the Department", L("en_dept:G")),
                text_link("College partnerships", L("en:F"))),
        owner=META["owner"],
    )
