from components import (page, name_tape, statement, p, h4, text_link, actions, split, photo, photo_slot, illo_slot,
                        route_list, draft, note)
from links import L

META = {"id": "E-3", "slug": "facilities", "title": "教學設備", "owner": "圖儀、哲君"}

# 設備說明逐字取自現行「教學設備」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/1463（2026-09-29 擷取）。
# 該頁後半的研討室預約與借用規定屬 H-2 場地借用，本頁只導流過去。
# 三張照片也取自該頁。
IMG_VR = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E8%99%9B%E6%93%AC%E4%B8%AD%E5%BF%83.png"
IMG_WARD1 = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E7%A4%BA%E7%AF%84%E5%AF%A6%E7%BF%92%E7%97%85%E6%88%BF1.png"
IMG_WARD2 = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E7%A4%BA%E7%AF%84%E5%AF%A6%E7%BF%92%E7%97%85%E6%88%BF2.png"


def render():
    opening = "".join([
        statement(
            draft("先在模擬病房練熟，再走進臨床。"),
            "從階梯教室、示範病房到虛擬中心，學生在接近真實的環境裡反覆練習身體評估、護理技術與急重症照護。",
        ),
        actions(text_link("場地借用", L("H-2")), text_link("學術資源", L("E"))),
    ])

    simulation = "".join([
        split(
            "".join([
                h4("虛擬中心"),
                p("內含三間虛擬病房，中間設有一個小中控室，可同時觀察成人及兒童實驗室之操作。"
                  "內含單面鏡、錄影系統、電腦、電動病床2張等配備，並可連線致虛擬中心外的護理站同步觀察虛擬實驗室內的操作實況。"
                  "學生可於護理站同步學習，提高此設備之效能。"),
                p("本虛擬中心提供高級內外科、高級產兒科、急重症護理課程使用外，亦做為學士班OSCE教學使用。"),
            ]),
            photo(IMG_VR, "虛擬中心的虛擬病房：病床、床旁櫃與監視螢幕", "4/3"),
            cols=(7, 5), align="start",
        ),
        split(
            "".join([
                h4(draft("VR 與 MR 模擬教學")),
                p(draft("以虛擬實境（VR）與混合實境（MR）模擬臨床情境，讓學生在安全的環境中練習。")),
            ]),
            illo_slot("戴著 MR 眼鏡練習的護理學生（CocoMaterial，重新上色）", "4/3", unit="inst"),
            cols=(7, 5), reverse=True, align="start",
        ),
        note("圖儀、哲君請提供：VR／MR 設備名稱與用途、使用的課程、放置地點，以及實際使用照片；"
             "現行網站沒有這部分的文字，上方為暫擬。"),
    ])

    classroom = split(
        "".join([
            p("134個座位之階梯教室，最多可容納到150人，供本系所有課程、研習會…等使用。"),
        ]),
        photo_slot("示範教室（階梯教室）全景", "16/9"),
        cols=(5, 7), align="start",
    )

    ward = "".join([
        p(draft("備有一般病床15張（每張病床配有床旁桌與床上桌各1張）")
          + "、於107年於病房內建置一張長照示範病床。"
          "自民國96年設置中央氣體教學設備，提供每張床氣流（空氣）與抽吸功能，使該實習病房更趨近臨床配置。"),
        p("本示範病房主要提供大學部身體檢查與評估、基本護理技術操作實習、醫研營等課程使用。"),
        split(photo(IMG_WARD1, "示範實習病房：成排病床，床邊有粉色隔簾與床上桌", "4/3"),
              photo(IMG_WARD2, "示範實習病房另一側：病床、點滴架與壁掛電視", "4/3"),
              cols=(7, 5), align="start"),
        note("病床數兩處說法不同：中文「教學設備」頁（unit/100010/1463）寫一般病床15張；"
             "舊英文頁「Facilities & Resources」（uniten/100010/867）寫 12 general beds, 2 examination beds。請圖儀確認現況。"
             "兩張照片取自中文教學設備頁；若有長照示範病床的照片請提供。"),
    ])

    learning = "".join([
        split(
            "".join([
                h4("智慧互動護理自學教室"),
                p("114年新建置。"),
                p(draft("提供學生自主練習護理技術的空間。")),
            ]),
            photo_slot("智慧互動護理自學教室", "4/3"),
            cols=(7, 5), align="start",
        ),
        split(
            "".join([
                h4(draft("MR 教學影片")),
                p(draft("以混合實境（MR）製作的教學影片，供學生課前預習與課後複習。")),
            ]),
            photo_slot("MR 影片封面（影片連結待提供）", "16/9"),
            cols=(7, 5), reverse=True, align="start",
        ),
        note("圖儀、哲君請提供：智慧互動護理自學教室的設備、開放時間與使用方式（上方說明為暫擬）；"
             "MR 影片的主題與播放連結（CMS 能否內嵌影片待確認，暫以封面圖加連結呈現）。"),
    ])

    return page(
        opening,
        name_tape("模擬教學"),
        simulation,
        name_tape("示範教室", unit="dept"),
        classroom,
        note("圖儀、哲君請提供示範教室照片一張（現行網站沒有）。"),
        name_tape("示範病房", unit="dept"),
        ward,
        name_tape("設備與學習資源", unit="inst"),
        learning,
        name_tape("借用與預約"),
        route_list([
            ("場地借用", "研討室預約、場地管理與儀器設備借用規定", L("H-2")),
            ("學術研究", "模擬教學相關的戰傷與災難護理研究", L("E-2")),
        ]),
        owner=META["owner"],
    )
