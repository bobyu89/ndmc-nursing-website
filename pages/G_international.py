from components import (page, name_tape, statement, p, button, text_link, actions, photo, split,
                        route_list, draft, note)
from links import L

META = {"id": "G", "slug": "international", "title": "國際交流", "owner": "院窗口"}

# 照片取自護理學系首頁輪播（unit/100180/6510），輪播標題「N75學生至美國華盛頓大學交流」。
IMG_UW = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/S__39010787.jpg"


def render():
    opening = "".join([
        statement(
            draft("護理，也在世界各地發生。"),
            draft("學院與國外護理院校互相參訪、交流，學生有機會出國學習，也歡迎境外學者與學生來訪。"),
        ),
        actions(button("學生交流與申請", L("G-2")), text_link("國際合作", L("G-1"))),
    ])

    overview = split(
        "".join([
            p(draft("國際交流分成兩部分：學院層級的國際合作（盟校、合作備忘錄、學者來訪），"
                    "以及學生的出國與來校交流。")),
            p(draft("近年的交流包括學生赴美國華盛頓大學交流、參訪西北大學等。")),
            note("交流實例取自學系網站輪播標題「N75學生至美國華盛頓大學交流」，以及舊英文頁（uniten/100010/843）輪播標題"
                 "「西北大學參訪」「西北大學來訪」（檔名 1140203NorthwestUniversity）。"
                 "請國際事務確認是哪一所西北大學、時間、參與者與交流內容後再上線。"
                 "請另提供一段國際交流概況（合作國家與學校、固定交流項目），不要放未經確認的數字。"),
        ]),
        photo(IMG_UW, "學生赴美國華盛頓大學交流期間，與師長在照護機構門前合影", "4/3",
              caption="學生赴美國華盛頓大學交流"),
        cols=(7, 5), align="start",
    )

    routes = route_list([
        ("國際合作", "國際盟校、合作備忘錄、境外學者來訪、合作成果", L("G-1")),
        ("學生交流", "出國與來校交流紀錄、學生心得、申請資訊與表單下載", L("G-2")),
    ], unit="inst")

    english = "".join([
        p(draft("國外學者、合作院校與交換學生，請看學院英文網站。")),
        p(draft("International scholars, partner institutions and visiting students: please visit our English site.")),
        actions(text_link("College of Nursing English Site", L("J"))),
        note("英文站尚未建置，連結暫時指向待建位置；英文站上線後，請把 links.py 的 J 改成正式網址。英文句子為草稿，請國際事務確認。"),
    ])

    return page(
        opening,
        name_tape("國際交流概況"),
        overview,
        name_tape("兩個入口"),
        routes,
        name_tape("English"),
        english,
        owner=META["owner"],
    )
