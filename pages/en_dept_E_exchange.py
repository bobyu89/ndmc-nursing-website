from components import (page, name_tape, statement, p, text_link, actions, split, photo, feature_list,
                        tape_surface, draft, note)
from links import L

META = {"id": "E", "slug": "exchange", "title": "International Exchange", "owner": "國際事務", "site": "en_dept"}

# No partner or exchange record is verified yet. Names below come only from photo captions:
#   "N75學生至美國華盛頓大學交流" — department home carousel (unit/100180/6510)
#   "西北大學參訪" / "西北大學來訪" / "八王子3" — English orphan page carousel (uniten/100010/843)
#   Thammasat (泰國法政) — 中文內容清單 dept I-3 note only
# All stay draft() until 國際事務 confirms.
# Photos (checked 200 image/jpeg on 2026-10-01): department carousel S__39010787.jpg ("N75學生至美國華盛頓大學交流");
# college carousel LINE_ALBUM_1140203NorthwestUniversity_250204_58.jpg ("西北大學參訪") and 106八王子2.jpg ("八王子3").
IMG_UW = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/S__39010787.jpg"
IMG_NW = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/LINE_ALBUM_1140203NorthwestUniversity_250204_58.jpg"
IMG_HACHIOJI = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/106%E5%85%AB%E7%8E%8B%E5%AD%902.jpg"


def render():
    opening = "".join([
        statement(
            draft("Nursing students who learn across borders."),
            draft("Selected exchange outcomes: where our students went, who visited us, and what both sides "
                  "took home. This is a record of exchange, not an application page."),
        ),
        actions(text_link("Visit and collaborate with the College", L("en:G")), text_link("中文版：海外交流專區", L("dept:H"))),
    ])

    outbound = split(
        "".join([
            p("Students of the department have visited the University of Washington in the United States "
              "for an exchange program."),
            p(draft("Each outbound visit records the host institution, dates, participants and learning focus.")),
        ]),
        photo(IMG_UW, "Department students during the exchange to the University of Washington, outside an assisted living facility", "4/3"),
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
        note("除華盛頓大學（學系首頁輪播照片標題已公開）外，本頁交流對象都未經確認，一律標待確認。請國際事務逐項確認後才能拿掉標記。"),
        name_tape("Outbound Exchange"),
        outbound,
        note("來源與照片：學系首頁輪播「N75學生至美國華盛頓大學交流」（照片已沿用，校名已見於公開網站）。"
             "請國際事務提供：交流年份、天數、參加人數、學習內容。屆別代號 N75 請改為入學年份。"),
        name_tape("Visitors and Partners"),
        inbound,
        note("三筆皆未確認：① 西北大學——英文孤兒頁輪播有「西北大學參訪」「西北大學來訪」，請確認是美國 Northwestern University "
             "還是其他「西北大學」，以及是參訪還是來訪、年份；② 八王子——輪播只有「八王子3」，請提供學校全名與交流內容；"
             "③ 泰國法政大學（Thammasat）——僅見於內容清單「境外學生來校交流」備註。未確認者請整列刪除。"),
        name_tape("Participant Reflections"),
        reflection,
        note("請國際事務收集 1〜2 篇參與者心得（英文 80 字內），取得本人同意公開姓名與照片。"),
        name_tape("Gallery"),
        split(photo(IMG_NW, "Visiting faculty and students with our students and faculty, outdoors on campus", "4/3",
                    caption=draft("Visit from Northwestern University")),
              photo(IMG_HACHIOJI, "Visitors from Hachioji, Japan, with our nursing students at a simulation bed", "4/3",
                    caption=draft("Visitors from Hachioji, Japan")), cols=(6, 6), align="start"),
        p(draft("Institutions interested in visits or collaboration can contact the College of Nursing."), muted=True),
        actions(text_link("Visit the Department", L("en_dept:G")),
                text_link("College partnerships", L("en:F"))),
        owner=META["owner"],
    )
