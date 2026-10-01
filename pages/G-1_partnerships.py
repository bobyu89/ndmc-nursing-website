from components import (page, name_tape, statement, p, text_link, actions, photo, split,
                        feature_list, facts, draft, note)
from links import L

META = {"id": "G-1", "slug": "partnerships", "title": "國際合作", "owner": "國際事務"}

SLOT = "〔待國際事務提供〕"

# 照片取自舊英文頁（uniten/100010/843）輪播，標題分別為「西北大學參訪」「西北大學來訪」。
IMG_NW_VISIT = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/"
                "LINE_ALBUM_1140203NorthwestUniversity_250204_58.jpg")
IMG_NW_GUESTS = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/"
                 "LINE_ALBUM_1140203NorthwestUniversity_250204_25.jpg")


def render():
    opening = statement(
        draft("和世界各地的護理院校，一起培育護理人才。"),
        draft("這裡列出學院的國際盟校與合作備忘錄、來訪的境外學者，以及雙方一起完成的合作成果。"),
    )

    partners = "".join([
        p(draft("與本院簽有合作關係的國外院校：")),
        facts([
            ("〔盟校名稱〕", f"〔國家〕｜〔合作起始年〕｜〔合作內容：學生交流、學者互訪、共同研究…〕　{SLOT}"),
            ("〔盟校名稱〕", f"〔國家〕｜〔合作起始年〕｜〔合作內容〕　{SLOT}"),
        ]),
        note("請國際事務提供盟校名單：學校中英文名稱、國家、合作起始年、合作內容，以及是否為校級或院級合作。"
             "名單確認前不列任何學校名稱；列數依實際數量增減。"),
    ])

    mou = "".join([
        p(draft("合作備忘錄（MOU）是雙方學校正式簽署的合作約定，內容可能包括學生交流、教師互訪與共同研究。")),
        facts([
            ("〔簽約對象〕", f"簽署日期〔年/月〕｜效期〔年限〕｜重點〔一句話〕　{SLOT}"),
        ]),
        note("請國際事務提供每一份合作備忘錄的簽約對象、簽署日期、效期與合作重點；若可公開簽約照片或新聞，請附上。"),
    ])

    visitors = "".join([
        p(draft("境外學者來訪時，會與師生座談、演講或參觀教學設施。")),
        note("請提供歷年境外學者來訪紀錄：日期、學者姓名與職稱、所屬學校、活動內容、照片（須取得當事人同意）。"
             "有資料後可改用年份時間軸呈現；目前不放任何年份。"),
    ])

    results = "".join([
        feature_list([
            ("西北大學參訪", draft("學院與西北大學的參訪交流。"), None, "inst"),
            ("學生赴美國華盛頓大學交流", draft("學生赴美國華盛頓大學交流學習，詳見學生交流。"), L("G-2"), "dept"),
            ("〔其他合作成果〕", draft("共同研究、合辦研討會、師資培訓等。"), None, "college"),
        ]),
        note("「西北大學參訪」「西北大學來訪」取自舊英文頁（uniten/100010/843）輪播標題，照片檔名含 1140203NorthwestUniversity；"
             "「N75學生至美國華盛頓大學交流」取自護理學系網站輪播標題。"
             "請國際事務確認是哪一所西北大學、交流時間、參與者與內容。"
             "另外，護理研究所網站輪播有「114_0319-23四國會議」「1140618-19Trauma_training戰傷災難護理培訓」，"
             "若屬國際合作，請提供說明後一併列入。"),
        split(photo(IMG_NW_VISIT, "西北大學參訪活動的戶外團體合照", "4/3", caption="西北大學參訪"),
              photo(IMG_NW_GUESTS, "西北大學來訪：來訪學者與師長在新春佈置前合影", "4/3", caption="西北大學來訪"),
              cols=(6, 6)),
    ])

    return page(
        opening,
        actions(text_link("學生交流", L("G-2")), text_link("回國際交流", L("G"))),
        name_tape("國際盟校", unit="inst"),
        partners,
        name_tape("合作備忘錄", unit="inst"),
        mou,
        name_tape("境外學者來訪", unit="inst"),
        visitors,
        name_tape("合作成果", unit="inst"),
        results,
        name_tape("English"),
        p(draft("國外院校洽談合作，請看英文網站。")),
        actions(text_link("College of Nursing English Site", L("J"))),
        owner=META["owner"],
    )
