from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot,
                        ribbon_bar, split, unit_pair, feature_lead, feature_list, route_list, draft, note)
from links import L
from tokens import C

META = {"id": "A", "slug": "home", "title": "護理學系", "owner": "院窗口", "site": "dept"}


def render():
    opening = split(
        "".join([
            statement(
                draft("四年，從護生到軍官。"),
                draft("學士班把護理專業和軍事訓練放在同一段養成裡：在教室學照護、在模擬病房練手，"
                      "再到醫院、社區與軍陣場域實習。"),
            ),
            actions(button("招生專區", L("dept:D")), text_link("認識本系", L("dept:C"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:320px;">' + patch(
            "護理學系", "Department of Nursing", unit="dept",
            illo=illo_slot("護生在模擬病房練習照護（CocoMaterial，重新上色）", "1/1"),
            tab="護理學院", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    # 分眾入口：每條緞帶是一種讀者。主按鈕「招生專區」與「我想報考」同一目的地。
    quick = ribbon_bar([
        ("我想報考", L("dept:D"), "公費、報名與營隊"),
        ("我是家長", L("F-1"), "公費、服役與在校生活"),
        ("在校生", L("dept:J"), "表單、獎學金、日程"),
        ("校友", L("dept:K"), "校友會與傑出校友"),
    ])

    practice = feature_lead(
        "三種實習場域",
        [p(draft("護理學系的實習從醫院延伸到社區，再到軍陣環境；每一種場域練的是不同的照護判斷。"))],
        illo_slot("護生跟著學姊在病房交班", "1/1"),
        unit="dept", href=L("dept:F-2"), link_label="實習資訊",
    )
    sites = feature_list([
        ("醫院實習", draft("在教學醫院的各科病房，跟著臨床教師照顧真實的病人。"), L("dept:F-2-1"), "dept", "院"),
        ("社區實習", draft("走進社區與長照場域，練習衛教與居家照護。"), L("dept:F-2-2"), "dept", "社"),
        ("軍陣實習", draft("結合軍事訓練，在野外與特殊環境中執行救護任務。"), L("dept:F-2-3"), "dept", "軍"),
    ])

    growth = route_list([
        ("大專生研究計畫", "學士班學生的研究成果", L("dept:G")),
        ("海外交流", "出國交流與海外學習紀錄", L("dept:H")),
        ("校園生活", "系學會、迎新、加冠、畢業典禮", L("dept:I")),
    ], unit="dept")

    news = route_list([
        ("課務公告", "選課、課程與考試", L("dept:B-1")),
        ("實習公告", "實習時程、分發與行前說明", L("dept:B-2")),
        ("獎學金公告", "申請與結果", L("dept:B-3")),
        ("活動訊息", "系所活動與招生活動", L("dept:B-4")),
    ], unit="dept")

    family = unit_pair([
        ("college", "護理學院", "學院首頁・師資・國際交流", L("A")),
        ("inst", "護理研究所", "碩士班・研究", L("D-2")),
    ])

    return page(
        opening,
        quick,
        name_tape("實習特色"),
        practice,
        sites,
        name_tape("學習成果"),
        growth,
        name_tape("學系公告"),
        note("首頁為靜態 HTML，無法自動帶入公告；以分類入口導向各公告模組。"),
        news,
        actions(text_link("所有公告", L("dept:B"))),
        name_tape("護理學院與研究所"),
        family,
        owner=META["owner"],
    )
