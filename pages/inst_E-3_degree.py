from urllib.parse import quote

from components import (page, name_tape, statement, p, h4, button, text_link, actions, bullets, feature_list,
                        draft, note)
from links import L
from tokens import SITE

META = {"id": "E-3", "slug": "degree", "title": "學位審查", "owner": "院窗口", "site": "inst"}

# 表單名稱原文照錄自研究所「學生專區」附件；研究倫理教育規定原文照錄自「必修-研究倫理教育」頁。
U_RULES = SITE + "/unit/100181/6533"
U_ETHICS_COURSE = SITE + "/unit/100181/6800"
U_HANDBOOK = SITE + quote("/files/web/192/file_up/100181/13936/國防醫學大學護理研究所碩士研究生手冊_09182025_公告.pdf")


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = "".join([
        statement(
            draft("從找指導教授到論文口試，一步一步來。"),
            draft("這一頁說明學位審查的順序，以及每一步要用的表單。表單統一放在表單下載，時程看重要日程與口試公告。"),
        ),
        actions(button("表單下載", L("inst:G-3")), text_link("重要日程", L("inst:G-4"))),
    ])

    flow = feature_list([
        ("研究倫理教育", draft("第一學期完成線上課程與測驗，才能參加學位考試。"), "#ethics", "inst", "倫"),
        ("指導教授", draft("申請指導教授，並定期留下指導紀錄。"), "#advisor", "inst", "師"),
        ("研究計畫口試", draft("研究計畫完成後申請口試；需要時送倫理審查。"), "#proposal", "inst", "計"),
        ("學位論文口試", draft("論文完成後申請學位考試。"), "#defense", "inst", "考"),
    ])

    ethics = "".join([
        '<div id="ethics"></div>',
        p("須於「1上」完成課程，如未完成者，不得學位考；完成者，始得學位考。"),
        _source("摘自研究所〈必修-研究倫理教育〉。", U_ETHICS_COURSE, "修課方式與測驗規定"),
    ])

    advisor = "".join([
        '<div id="advisor"></div>',
        p(draft("先在學院師資陣容與研究領域頁認識老師，談好之後送出申請。指導期間的討論要留下紀錄。")),
        bullets(["附錄3-2-2_論文指導教授申請表", "附錄3-2-3_論文指導記錄表", "附錄3-2-4、更換指導教授聲明書"]),
        actions(text_link("師資陣容", L("E-1")), text_link("研究領域", L("inst:F-1"))),
    ])

    proposal = "".join([
        '<div id="proposal"></div>',
        p(draft("研究計畫完成、指導教授同意後，申請研究計畫口試。研究若涉及人體或需在三軍總醫院收案，"
                "要先完成倫理審查與收案申請。")),
        bullets(["附錄3-3-1至3-3-7_論文研究計劃口試申請"]),
        actions(text_link("研究倫理（IRB 與收案申請）", L("inst:G-2"))),
    ])

    fmt = "".join([
        p(draft("論文格式依研究生手冊規定。")),
        actions(text_link("研究生手冊（PDF）", U_HANDBOOK)),
        note("現行網站沒有論文格式說明或範本。請院窗口提供：論文格式規範（或手冊章節頁碼）、Word 範本檔、"
             "論文比對（原創性檢測）規定與門檻、紙本與電子論文繳交方式。"),
    ])

    defense = "".join([
        '<div id="defense"></div>',
        p(draft("論文完成後申請學位考試。表單依學組（專科護理師組與非專師組）和入學學年度（113學年前、114學年後）分成四版，"
                "請選對自己的版本。")),
        bullets([
            "附錄3-4-1至附錄3-4-12_學位論文口試（非專師組）-113前",
            "附錄3-4-1至附錄3-4-12_學位論文口試（非專師組）-114後",
            "附錄3-4-1至附錄3-4-12_學位論文口試（專師組）-113前",
            "附錄3-4-1至附錄3-4-12_學位論文口試（專師組）-114後",
        ]),
        actions(text_link("口試公告", L("inst:B-3"))),
    ])

    return page(
        opening,
        name_tape("審查順序"),
        flow,
        note("現行研究所網站只有表單，沒有學位審查的程序說明。請院窗口依研究生手冊第三章提供：各階段的申請時限、"
             "口試委員組成與人數、送審文件、口試通過後的修改與繳交期限；上方順序與說明為草稿。"),
        name_tape("研究倫理教育"),
        ethics,
        name_tape("指導教授"),
        advisor,
        name_tape("研究計畫"),
        proposal,
        name_tape("論文格式"),
        fmt,
        name_tape("學位考試與口試"),
        defense,
        _source("表單名稱摘自護理研究所〈學生專區〉附件下載。", U_RULES, "原頁面"),
        note("以上表單目前掛在研究所「學生專區」（unit/100181/6533）。G-3 表單下載模組建好後，請院窗口把表單搬過去，"
             "並保留相同檔名，方便學生對照本頁。"),
        owner=META["owner"],
    )
