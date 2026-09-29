from components import (page, name_tape, statement, p, button, text_link, actions, facts, feature_list, split,
                        illo_slot, draft, note)
from links import L

META = {"id": "D", "slug": "admissions", "title": "招生專區", "owner": "院窗口", "site": "dept"}

# 事實與電話沿用學院「招生專區」（pages/F_admissions.py）已核對的內容，
# 原出處：《115 學年度軍事學校正期班甄選入學招生簡章》與學校招生專區【大學部】。
U_BACH = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2009"


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = "".join([
        statement(
            draft("想當軍護，從護理學系的學士班開始。"),
            draft("高中（職）畢業就能報考。四年讀護理、接受軍事訓練，在學期間享有公費，畢業後任官成為護理軍官。"
                  "報名方式、公費與服役、營隊體驗，這一頁幫你找到入口。"),
        ),
        actions(button("看招生資訊", L("dept:D-1")), text_link("家長常見問題", L("F-1"))),
    ])

    summary = "".join([
        facts([
            ("招生對象", "一、年齡：社會青年、後備役士官兵及替代役備役人員：17 歲至22 歲。<br>"
                        "二、學歷：公私立高中（職）畢業或同等學力。"),
            ("身分別", "軍費生、代訓生（輔導會公費生）"),
            ("入伍訓練", "八週"),
            ("修業年限", "修業 4 年。"),
            ("學位授予", "畢業授予所屬學系學士學位。"),
            ("實習醫院", "本校實習醫院為三軍總醫院。"),
        ]),
        _source("摘自《115 學年度軍事學校正期班甄選入學招生簡章》，新學年度請以新簡章為準。", U_BACH, "學校招生專區（大學部）"),
    ])

    paths = feature_list([
        ("招生資訊",
         draft("報考資格、名額、報名時程與招生簡章，以及學校與國防部的報名入口。"),
         L("dept:D-1"), "dept", "招"),
        ("職涯發展",
         draft("從入伍訓練、公費、任官到分發：讀完四年之後的路怎麼走，服役義務要先了解清楚。"),
         L("dept:D-2"), "dept", "職"),
        ("國防迷彩天使災難救護營",
         draft("還在猶豫？暑假先來營隊待一天，練包紮、搬運與戰術撤離，看看軍護是不是你想走的路。"),
         L("dept:E"), "dept", "營"),
    ])

    family = split(
        "".join([
            p(draft("公費怎麼算、要服役幾年、在學校過什麼樣的生活，護理學院為家長整理了常見問題，"
                    "每一題都附上招生簡章的原文。")),
            actions(text_link("家長常見問題", L("F-1")), text_link("護理學院招生專區", L("F"))),
        ]),
        illo_slot("家長陪孩子看招生簡章（CocoMaterial，重新上色）", "4/3", unit="dept"),
        cols=(7, 5),
    )

    contact = "".join([
        facts([
            ("學士班招生", "教務處招生承辦人：02-87926692。"),
            ("護理學系辦公室", "02-87923100 轉 18165、18167。"),
            ("國軍招募客服", "0800-000050"),
            ("上班時間", "週一至週五8:00至17:00(不含例假日及國訂假日)"),
        ]),
        _source("電話摘自招生簡章與學校招生專區。", U_BACH, "學校招生專區"),
        note("請院窗口確認各電話仍有效，並決定是否加上學系招生信箱、到校參訪預約方式。"),
    ])

    return page(
        opening,
        note("公費、服役、授階、分發等內容可公開到什麼程度尚未決定，本頁只做摘要與導流，細節放在「職涯發展」（D-2）與學院「家長常見問題」（F-1），"
             "上線前請學生事務與院窗口確認。"),
        name_tape("學士班招生重點"),
        summary,
        name_tape("招生、職涯與營隊"),
        paths,
        name_tape("給家長"),
        family,
        name_tape("招生諮詢"),
        contact,
        actions(text_link("活動與招生訊息", L("dept:B-4"))),
        owner=META["owner"],
    )
