from components import (page, name_tape, statement, p, bullets, text_link, actions, split, photo_slot, illo_slot, facts,
                        feature_list, route_list, draft, note)
from links import L
from tokens import SITE

META = {"id": "G", "slug": "research", "title": "大專生研究計畫", "owner": "院窗口", "site": "dept"}

# 真實資料來源（2026-09-29 擷取）：
#   《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月，附錄〈暑期軍事訓練週課程期程〉二年級欄
#   「護理研究專題體驗學習(1週)」（學生專區 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681 附件）
#   現行「課程地圖」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/3642 圖上的「護理研究導論」「護理專業問題研討」
# 學校與學系網站上找不到護理學系學生的大專生研究計畫名單（醫學系有，見 unit/100003/3943），所以本頁只放架構與待填欄位，
# 不列任何計畫名稱或學生姓名。
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"
U_NSTC = "https://www.nstc.gov.tw/folksonomy/list/2af9ad9a-1f47-450d-b5a1-2cb43de8290c?l=ch"


def render():
    opening = split(
        statement(
            draft("大學四年，也可以帶著自己的研究問題畢業。"),
            draft("學士班學生可以在老師指導下提出研究計畫，申請國科會大專學生研究計畫。"
                  "從臨床看到的一個問題開始，學會查文獻、蒐集資料、寫成報告。"),
        ),
        '<div class="mx-auto" style="max-width:280px;">'
        + illo_slot("護生和指導老師討論研究海報（CocoMaterial，重新上色）", "1/1", unit="dept") + "</div>",
        cols=(7, 5),
    )

    in_course = "".join([
        p(draft("研究不是四年級才開始。課程裡已經安排了幾個接觸研究的機會：")),
        feature_list([
            ("護理研究專題體驗學習",
             draft("二年級暑期，為期一週。") + "　" + text_link("學生手冊（PDF）", U_HANDBOOK),
             None, "dept", "體"),
            ("護理研究導論",
             draft("課程地圖把它排在三年級的護理專業課程。"),
             L("dept:F-1-3"), "dept", "研"),
            ("護理專業問題研討",
             draft("課程地圖把它排在四年級的護理專業課程。"),
             L("dept:F-1-3"), "dept", "討"),
        ]),
        note("課委會請確認：上面三門課的年級是從學生手冊與課程地圖圖檔判讀的；若有一句話的課程簡介，請提供替換暫擬文字。"),
    ])

    projects = "".join([
        p(draft("這裡會列出護理學系學生通過的大專學生研究計畫。")),
        facts([
            ("年度", draft("待提供")),
            ("計畫名稱", draft("待提供")),
            ("學生（期班）", draft("待提供")),
            ("指導老師", draft("待提供")),
        ]),
        split(photo_slot("研究成果海報或發表照片", "4/3"), photo_slot("學生在研討會報告", "4/3"), cols=(6, 6), align="start"),
        note("學校與學系網站上找不到護理學系學生的大專生研究計畫名單，所以這裡沒有列任何計畫。"
             "院窗口請向研究發展處或各指導老師蒐集：近幾年通過的計畫年度、計畫名稱、學生姓名與期班、指導老師，"
             "以及是否獲研究創作獎；學生姓名上網前須取得本人同意。"
             "醫學系的做法可參考：以年度整理成一份通過名單 PDF（" + SITE + "/unit/100003/3943）。"
             "若有學生以研究成果在研討會發表，也請提供照片與研討會名稱。"),
    ])

    how = "".join([
        bullets([
            draft("找一位研究方向相近的老師，先談談你想研究的問題。"),
            draft("和老師一起寫研究計畫，在國科會公告的期限內提出申請。"),
            draft("計畫通過後，在老師指導下執行研究，完成成果報告。"),
        ]),
        note("院窗口請轉研究發展處或負責老師確認：申請流程、校內截止時間、聯絡窗口，以及學系是否另有獎勵；"
             "確認後替換上方三句暫擬步驟。"),
        actions(text_link("國科會大專學生研究計畫", U_NSTC)),
    ])

    mentors = route_list([
        ("研究成果", draft("老師們的研究主題與近期成果"), L("inst:F")),
        ("師資陣容", draft("全院老師的專長，找指導老師從這裡開始"), L("E-1")),
    ], unit="dept")

    return page(
        opening,
        name_tape("課程裡的研究"),
        in_course,
        name_tape("歷年研究計畫"),
        projects,
        name_tape("怎麼開始"),
        how,
        name_tape("找指導老師"),
        mentors,
        owner=META["owner"],
    )
