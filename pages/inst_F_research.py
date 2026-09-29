from components import (page, name_tape, statement, p, button, text_link, actions, patch, illo_slot, split,
                        bullets, feature_list, route_list, draft, note)
from links import L
from tokens import C

META = {"id": "F", "slug": "research", "title": "研究成果", "owner": "教發", "site": "inst"}

# 研究內容單一來源：本節（F、F-1、F-2、F-3）是全院研究內容的母站；學院「學術研究」E-2 只做摘要並連過來，
# 完整教師學經歷與著作由學院「師資陣容」E-1 維護。
# 指導教授資格一句逐字取自《國防醫學大學護理研究所碩士研究生手冊》（114年8月11日版）
# 「指導教授指導研究生實施要點」第二點；手冊掛在 https://wwwndmc.ndmutsgh.edu.tw/unit/100181/6533。


def render():
    opening = split(
        "".join([
            statement(
                draft("研究從照護現場開始，也回到照護現場。"),
                draft("護理研究所以軍陣護理、戰傷與災難護理為特色，也做成人與急重症、婦兒、精神衛生、"
                      "癌症與安寧照護等研究。研究方向、老師的論文與學術活動，都從這裡進去。"),
            ),
            actions(button("研究領域", L("inst:F-1")), text_link("研究發表", L("inst:F-2"))),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:300px;">' + patch(
            "研究成果", "Research", unit="inst",
            illo=illo_slot("研究生整理問卷與數據（CocoMaterial，重新上色）", "1/1", unit="inst"),
            tab="護理研究所", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    strengths = "".join([
        p(draft("老師們的專長集中在下面幾個方向。每個方向有哪些老師、各自的研究室，都列在研究領域頁。")),
        bullets([
            draft("軍陣、戰傷與災難護理"),
            draft("成人、急重症與慢性病照護"),
            draft("癌症、安寧與護理倫理"),
            draft("婦兒與家庭照護"),
            draft("精神衛生、睡眠與壓力調適"),
            draft("健康促進、高齡與職業衛生"),
            draft("護理教育、數位與智慧照護"),
        ]),
        note("七個方向是依學院師資頁各教師「專長學科」歸納的草稿分組，不是正式研究群。"
             "教發請確認分組與名稱；若本所有正式的研究群或特色團隊，請提供名稱、召集人與成員後替換。"),
    ])

    supervisors = "".join([
        p(draft("選指導教授前，先看老師的專長與研究室，再和老師談。")),
        p("研究生之主論文指導教授須符合本系專任助理教授(含)以上、合聘教師及臨床教師之資格者。"),
        p("摘自《碩士研究生手冊》「指導教授指導研究生實施要點」。", muted=True),
        actions(text_link("指導教師與招生方向", L("inst:F-1")), text_link("師資陣容（學經歷與著作）", L("E-1"))),
    ])

    routes = feature_list([
        ("研究領域", draft("研究方向、戰傷與災難護理特色研究，以及每位指導教師的專長與研究室。"),
         L("inst:F-1"), "inst", "域"),
        ("研究發表", draft("老師個人頁列出的最新期刊論文，依年份整理；也收研究生的發表成果。"),
         L("inst:F-2"), "inst", "文"),
        ("學術活動", draft("已經辦過的演講、研討會與培訓紀錄。即將舉辦的活動看學術活動公告。"),
         L("inst:F-3"), "inst", "會"),
    ])

    return page(
        opening,
        name_tape("研究特色"),
        strengths,
        name_tape("指導教師"),
        supervisors,
        name_tape("研究成果分頁"),
        routes,
        actions(text_link("即將舉辦的學術活動", L("inst:B-5")), text_link("學院學術研究摘要", L("E-2"))),
        owner=META["owner"],
    )
