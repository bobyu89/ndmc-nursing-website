from components import (page, name_tape, statement, p, text_link, actions, split, illo_slot, feature_list, route_list,
                        draft, note)
from links import L
from tokens import SITE

META = {"id": "F-2", "slug": "practicum", "title": "實習資訊", "owner": "院窗口", "site": "dept"}

# plain 文字逐字取自《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月，第二章 柒、三〈臨床實習〉
# （學生專區附件，https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681，2026-09-29 擷取）。
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"


def render():
    opening = split(
        "".join([
            statement(
                draft("從病房、社區到軍陣，實習是四年裡最長的一堂課。"),
                draft("護理學系的實習分成醫院、社區與軍陣三種場域；出發之前，先讀實習規定。"),
            ),
            actions(text_link("實習規定與表單", L("dept:F-2-4"))),
        ]),
        '<div class="mx-auto" style="max-width:300px;">'
        + illo_slot("護生跟著臨床老師在病房交班（CocoMaterial，重新上色）", "1/1", unit="dept") + "</div>",
        cols=(7, 5),
    )

    why = "".join([
        p("欲培養學生成為一位優良的護理人員，除課室內的學理教學外，必須加以臨床實習的配合。"),
        p(draft("摘自《護理學系學生手冊》（115年8月）〈臨床實習〉。") + "　" + text_link("學生手冊（PDF）", U_HANDBOOK),
          muted=True),
    ])

    sites = feature_list([
        ("醫院實習",
         draft("在三軍總醫院、臺北榮民總醫院等教學醫院，實習基本護理、內外科、產兒科、精神衛生與護理行政。"),
         L("dept:F-2-1"), "dept", "院"),
        ("社區實習",
         draft("到健康服務中心與三軍總醫院社區醫學部，練習社區評估、家庭訪視與團體衛教。"),
         L("dept:F-2-2"), "dept", "社"),
        ("軍陣實習（含軍訓）",
         draft("入學先完成入伍訓練，之後每年暑假接受軍事訓練與軍陣護理實務。"),
         L("dept:F-2-3"), "dept", "軍"),
        ("實習規定與表單",
         draft("服裝、出勤、請假、病人隱私，以及實習要交的表單。"),
         L("dept:F-2-4"), "tape", "規"),
    ])

    return page(
        opening,
        name_tape("為什麼要實習"),
        why,
        name_tape("實習場域"),
        sites,
        note("院窗口請提供：各場域實習的照片（學生正面需取得同意），以及一段學生或臨床老師的實習心得（需本人同意具名）。"),
        name_tape("實習公告"),
        route_list([
            ("實習公告", "實習時程、分發與行前說明", L("dept:B-2")),
            ("重要日程", "實習與考試等重要日期", L("dept:J-3")),
        ], unit="dept"),
        owner=META["owner"],
    )
