from components import (page, name_tape, statement, p, text_link, actions, feature_list, route_list, facts,
                        draft, note)
from links import L
from tokens import SITE

META = {"id": "F", "slug": "curriculum", "title": "課程", "owner": "院窗口", "site": "dept"}

# 原文來源（2026-09-29 擷取），plain 文字逐字照錄：
#   學生專區 修業規定  https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681
#   《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月，學生專區附件
U_STUDENT = SITE + "/unit/100180/6681"
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = "".join([
        statement(
            draft("先在教室打底，再到醫院、社區與軍中實習。"),
            draft("四年的課從通識、基礎醫學一路走到護理專業，中間穿插臨床實習和每年暑假的軍事訓練。"
                  "想知道修什麼課，看課程資訊；想知道去哪裡實習，看實習資訊。"),
        ),
        actions(text_link("課程資訊", L("dept:F-1")), text_link("實習資訊", L("dept:F-2"))),
    ])

    routes = feature_list([
        ("課程資訊",
         draft("課程怎麼設計、各期班要修多少學分、每門課對應哪些核心能力。"),
         L("dept:F-1"), "dept", "課"),
        ("實習資訊",
         draft("醫院、社區與軍陣三種實習場域，以及實習前一定要讀的規定與表單。"),
         L("dept:F-2"), "dept", "習"),
    ])

    glance = "".join([
        facts([
            ("修業年限", "本學系學士班教育學程為四年（內含軍事訓練課程）"),
            ("最低畢業學分", "113學年以前最低畢業學分數為136學分"
                            "<br>113學年以後最低畢業學分數為132學分"),
            ("主要實習醫院", "三軍總醫院和臺北榮民總醫院"),
            ("暑期軍事訓練", "每年軍事訓練週起迄時間，大約是5月底至8月底，但應以國防部頒訂之該年度之教育行事曆為準。"),
        ]),
        _source("前兩列摘自學生專區〈修業規定〉；後兩列摘自《護理學系學生手冊》（115年8月）。", U_STUDENT, "學生專區"),
        actions(text_link("學生手冊（PDF）", U_HANDBOOK)),
    ])

    news = route_list([
        ("課務公告", "選課、課程與考試", L("dept:B-1")),
        ("實習公告", "實習時程、分發與行前說明", L("dept:B-2")),
    ], unit="dept")

    return page(
        opening,
        name_tape("兩條路"),
        routes,
        name_tape("四年一覽"),
        glance,
        note("院窗口請確認：每年新版學生手冊公布後，核對本表的學分與軍事訓練週說明是否更動。"),
        name_tape("課程與實習公告"),
        news,
        owner=META["owner"],
    )
