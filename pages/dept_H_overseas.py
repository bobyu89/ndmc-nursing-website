from components import (page, name_tape, statement, p, text_link, actions, photo, split, facts, route_list,
                        tape_surface, draft, note, todo)
from links import L

META = {"id": "H", "slug": "overseas", "title": "海外交流專區", "owner": "院窗口", "site": "dept"}

# 真實素材：
# - 學系首頁輪播照片標題「N75學生至美國華盛頓大學交流」 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6510（2026-09-29 擷取）
# - 學生專區附件「國防醫學大學護理學院學生海外研見習規定」（1141013 訂定） https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681
# - 系學會「國際事務組」職掌，逐字取自系學會頁圖片 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6796
# 申請資格、時程與表單已在學院「學生交流」頁（G-2），本頁不重複，只導流。

# 照片：同一張輪播照片（1565×1046，2026-10-01 核對 200 image/jpeg）。
IMG_UW = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/S__39010787.jpg"



def render():
    opening = "".join([
        statement(
            draft("出國看別人怎麼照護，再帶回來。"),
            draft("這裡記錄護理學系學生出國交流的經過：去了哪裡、看到什麼。申請方式與表單，請看學院的學生交流頁。"),
        ),
        actions(text_link("申請資訊與表單（學院學生交流）", L("G-2")), text_link("境外學生來校", L("dept:I-3"))),
    ])

    record = split(
        "".join([
            p("學系學生曾赴美國華盛頓大學交流。"),
            facts([(k, v) for k, v in [  # todo() is empty in the final build, so unfilled rows drop out
                ("交流學校", "美國華盛頓大學"),
                ("參加學生", todo("參加學生人數與入學年（院窗口向國際事務確認）")),
                ("時間與天數", todo("交流年份與天數（院窗口向國際事務確認）")),
                ("學了什麼", todo("交流內容（院窗口向國際事務確認）")),
            ] if v]),
        ]),
        photo(IMG_UW, "學生赴美國華盛頓大學交流期間，在當地一處長照機構（Assisted Living）前合影", "4/3",
              caption="學生赴美國華盛頓大學交流（學系首頁輪播照片）"),
        cols=(7, 5), align="start",
    )

    more = "".join([
        p(draft("每一次出國交流，都依同樣格式記錄：交流學校、時間、參加同學與學習內容，由新到舊排列。")),
        note("「N75學生至美國華盛頓大學交流」取自學系首頁輪播照片標題，是目前唯一找得到的出國紀錄。"
             "照片沿用該張輪播照片。請院窗口向國際事務確認：交流年份、天數、參加人數、交流內容；"
             "頁面上請把屆別代號（N75）改寫成「某年入學的學生」這類外部讀者看得懂的說法。"
             "其他年度的出國紀錄請一併提供，每筆照上方格式補一組；資料確認前不放任何年份。"),
    ])

    rules = "".join([
        tape_surface(
            p("國防醫學大學護理學院學生海外研見習規定"),
            p(draft("出國研習、見習前，請先讀這份規定。全文放在學生專區的附件下載。"), muted=True),
            actions(text_link("到學生專區下載規定", L("dept:J"))),
        ),
        note("規定檔名取自學生專區（unit/100180/6681）附件，檔名標示 1141013 訂定。請確認這是最新版本；"
             "若要另放一份摘要（誰可以申請、出國前要辦哪些手續），請國際事務提供重點，本頁再加一段。"),
    ])

    team = "".join([
        p("國際事務組－負責辦理學系與國外學校交流之活動，接待國外貴賓、師長和與會朋友，協助籌備國際交流之計畫。"),
        p(draft("想參與交流活動的同學，也可以找系學會國際事務組。"), muted=True),
    ])

    routes = route_list([
        ("學生交流（護理學院）", draft("申請資格、時程、甄選方式與表單下載"), L("G-2")),
        ("境外學生來校交流", draft("國外護理學生來學系交流的紀錄"), L("dept:I-3")),
        ("系學會", draft("國際事務組與其他幹部分工"), L("dept:I-1")),
    ], unit="dept")

    return page(
        opening,
        name_tape("出國交流紀錄"),
        record,
        more,
        name_tape("出國前要讀的規定"),
        rules,
        name_tape("系學會國際事務組"),
        team,
        name_tape("相關頁面"),
        routes,
        owner=META["owner"],
    )
