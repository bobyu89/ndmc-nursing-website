from urllib.parse import quote

from components import (page, name_tape, statement, p, h4, text_link, actions, photo, split, timeline,
                        facts, draft, note)
from links import L
from tokens import SITE

META = {"id": "F-3", "slug": "events", "title": "學術活動", "owner": "教發", "site": "inst"}

# 活動名稱逐字取自護理研究所現行首頁輪播照片標題（https://wwwndmc.ndmutsgh.edu.tw/unit/100181/6511，2026-09-29 擷取）；
# 日期依標題前綴的民國年月日換算（114_0115 = 2025/1/15）。「國軍持續教育」標題只有「114」，
# 月日取自照片檔名 1140812國軍持續教育.jpg，故標待確認。輪播中的揭牌典禮、小畢典與全體教師照不屬學術活動，未列入。
# 活動內容說明一律待主辦老師提供，本頁不補寫講者、國家或人數。
# 照片直接引用同一輪播的原圖（/files/web/192/menu/100181/slider/），替代文字依輪播標題。

SLIDER = SITE + "/files/web/192/menu/100181/slider/"
IMG_FOUR = SLIDER + "480575237_1193085299489862_5549031880442815728_n.jpg"  # 114_0319-23四國會議
IMG_TRAUMA = SLIDER + "67455379-4742-4728-8242-D72E16011238.jpg"  # 1140618-19Trauma_training戰傷災難護理培訓
IMG_AI = SLIDER + quote("LINE_ALBUM_20250115演講-AI在護理臨床及研究之應用_250204_1.jpg")  # 114_0115_演講
IMG_CE = SLIDER + quote("1140812國軍持續教育.jpg")  # 114國軍持續教育


def render():
    opening = "".join([
        statement(
            draft("辦過的每一場，都留下紀錄。"),
            draft("這一頁收錄本所已經辦過的演講、研討會、培訓與學術交流。"
                  "想參加接下來的活動，請看學術活動公告。"),
        ),
        actions(text_link("即將舉辦的活動", L("inst:B-5")), text_link("研究領域", L("inst:F-1"))),
    ])

    y2025 = "".join([
        h4("2025 年（民國114年）"),
        timeline([
            ("1/15", "演講-AI在護理臨床及研究之應用",
             "研究所網站輪播照片標題：「114_0115_演講-AI在護理臨床及研究之應用」。", "inst"),
            ("3/19–23", "四國會議",
             "研究所網站輪播照片標題：「114_0319-23四國會議」。", "inst"),
            ("6/18–19", "Trauma training 戰傷災難護理培訓",
             "研究所網站輪播照片標題：「1140618-19Trauma_training戰傷災難護理培訓」。", "inst"),
            ("8/12", "國軍持續教育",
             "研究所網站輪播照片標題：「114國軍持續教育」。" + draft("日期取自照片檔名 1140812。"), "inst"),
        ]),
        note("四場活動只有標題與日期可查，內容說明待補。請主辦老師或所辦提供每場："
             "活動全名、主辦與合辦單位、講者或與會學校（四國會議是哪四國、在哪裡舉行）、參加對象與人數、一段兩三句的紀錄。"
             "下方四張照片沿用研究所首頁輪播原圖，若有更合適的照片可替換。"
             "「國軍持續教育」請確認日期（檔名為 1140812）以及是否屬學術活動。"),
        split(photo(IMG_FOUR, "2025年3月四國會議活動照片", "4/3", caption="四國會議（2025/3/19–23）"),
              photo(IMG_TRAUMA, "2025年6月戰傷災難護理培訓活動照片", "4/3", caption="戰傷災難護理培訓（2025/6/18–19）"),
              cols=(6, 6)),
        split(photo(IMG_AI, "2025年1月「AI在護理臨床及研究之應用」演講活動照片", "4/3",
                    caption="演講：AI在護理臨床及研究之應用（2025/1/15）"),
              photo(IMG_CE, "2025年國軍持續教育活動照片", "4/3", caption="國軍持續教育（2025）"),
              cols=(6, 6)),
    ])

    template = "".join([
        p(draft("之後每辦完一場活動，就照同樣的格式補一筆，最新的放在最下面。")),
        facts([
            ("日期", "〔年/月/日〕"),
            ("活動名稱", "〔全名〕"),
            ("類型", "〔演講／研討會／培訓／學術交流〕"),
            ("講者或與會單位", "〔姓名、職稱、所屬單位〕"),
            ("紀錄", "〔兩三句：做了什麼、誰參加〕"),
        ]),
        note("教發請提供 2024 年以前的活動紀錄（如有），以及 2025 年下半年至今已辦完的活動。"
             "活動預告放在學術活動公告（消息模組），辦完後再搬到本頁成為紀錄，兩邊不重複。"),
    ])

    return page(
        opening,
        name_tape("活動紀錄"),
        y2025,
        name_tape("新增紀錄的格式"),
        template,
        name_tape("相關頁面"),
        actions(text_link("學術活動公告", L("inst:B-5")), text_link("研究發表", L("inst:F-2")),
                text_link("學院國際合作", L("G-1"))),
        owner=META["owner"],
    )
