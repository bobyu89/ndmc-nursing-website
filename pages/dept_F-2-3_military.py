from components import (page, name_tape, statement, p, bullets, text_link, actions, split, patch, illo_slot, facts,
                        timeline, draft, note)
from links import L
from tokens import C, SITE

META = {"id": "F-2-3", "slug": "military", "title": "軍陣實習（含軍訓）", "owner": "院窗口", "site": "dept"}

# plain 文字逐字取自（2026-09-29 擷取）：
#   《115 學年度軍事學校正期班甄選入學招生簡章》（學校招生專區 https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2009）：
#     入伍訓練「八週」、「起赴陸軍軍官學校統一實施新生入伍訓練」（與學院 F、F-1 頁同一出處）
#   《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月（學生專區 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681 附件）：
#     附錄六〈暑期軍事訓練週課程期程〉；〈學生學習歷程檔案管理須知〉EMT-1 證照；第二章 肆 學士班教學目標
#   現行「課程地圖」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/3642 圖上的「軍護教育課程（1228 小時）」
U_BACH = SITE + "/unit/100143/2009"
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"
U_MAP = SITE + "/unit/100010/3642"


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = split(
        "".join([
            statement(
                draft("每個暑假，都是一段軍事訓練。"),
                draft("入學先完成八週入伍訓練；之後每年暑假都有軍事訓練週，從衛勤訓練、EMT-1 證照到軍陣醫學實習，一步步學會在軍中照顧傷病。"),
            ),
            p("能扮演克盡職責、勝任使命的軍護專業角色。", muted=True),
            p(draft("這是學士班八項教學目標之一。"), muted=True),
        ]),
        '<div class="mx-auto" style="width:72%;max-width:280px;">'
        + patch("軍陣實習", "含軍事訓練", unit="dept",
                illo=illo_slot("護生練習戰傷救護（CocoMaterial，重新上色）", "1/1", unit="dept"),
                tab="護理學系", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    basic = "".join([
        facts([
            ("入伍訓練", "八週"),
            ("地點", "起赴陸軍軍官學校統一實施新生入伍訓練"),
        ]),
        _source("摘自《115 學年度軍事學校正期班甄選入學招生簡章》；每年以最新簡章為準。", U_BACH, "學校招生專區"),
    ])

    summers = "".join([
        timeline([
            ("一年級", "入伍訓練", "新生報到(1週)、入伍訓練(8週)、準備週", "dept"),
            ("二年級", "衛勤正分班",
             "衛勤正分班(含EMT1及1週兵科見學)（5週）、暑假(3週)、生命倫理與教育實習(3週)、"
             "護理研究專題體驗學習(1週)、軍事訓練(含基本教練)(2週)", "dept"),
            ("三年級", "基礎軍陣護理實務",
             "部訂軍事課程(3週)、博雅課程(通識中心)(2週)、生命教育與倫理實習(3週)、基礎軍陣護理實務(3週)", "dept"),
            ("四年級", "軍陣醫學實習",
             "軍陣醫學實習(2週)、EMT1複訓(1週)、手術室(1週)、急診室(1週)、加護病房見習(1週)、綜合臨床護理學實習（5週）", "dept"),
        ]),
        p("備註：每年軍事訓練週起迄時間，大約是5月底至8月底，但應以國防部頒訂之該年度之教育行事曆為準。"),
        _source("摘自《護理學系學生手冊》（115年8月）附錄〈暑期軍事訓練週課程期程〉。", U_HANDBOOK, "學生手冊（PDF）"),
        note("手冊目錄把這張表寫成「附錄七」，內頁標題是「附錄六」，請學生事務委員會下次改版時統一。"
             "表格原本是一年級到四年級四欄，本頁照欄位順序列出；二年級欄的「暑假(3週)」是否指放假，請確認後決定要不要保留。"),
    ])

    emt = "".join([
        p("初級救護技術員(EMT-1)證照：於本校暑訓之衛勤正分班課程實習取得之證照，且為有效合格證照。"),
        _source("摘自學生手冊〈學生學習歷程檔案管理須知〉。", U_HANDBOOK, "學生手冊（PDF）"),
    ])

    hours = "".join([
        p(draft("課程地圖把四年的軍事與軍護訓練列為「軍護教育課程（1228 小時）」，括號內為時數：")),
        bullets([
            "入伍教育（279）",
            "軍醫院簡介（40）、衛勤教育（149）、軍事訓練（含）基本教練（80）、服務學習（80）",
            "軍事共同性課程（120）、服務學習（80）、基礎軍陣護理實務（120）、博雅教育（80）",
            "軍護專業訓練（120）、戰術醫療訓練（80）",
            "初官基層軍陣醫學訓練、愛國教育",
        ]),
        _source("照抄自現行課程地圖頁的圖（114.05.12 修訂）。", U_MAP, "現行課程地圖頁"),
        p(draft("另外，四年級的護理專業課程裡有一門「軍陣護理學」。")),
        actions(text_link("課程地圖", L("dept:F-1-3"))),
    ])

    supply = note("院窗口請轉學生事務委員會或軍陣護理課程負責老師提供："
                  "軍陣醫學實習、基礎軍陣護理實務在哪裡進行、做哪些事（可公開的範圍）；"
                  "衛勤正分班與 EMT-1 訓練的簡介；兩三張可公開的訓練照片（涉及軍事設施者請先確認可否公開）。"
                  "上方大字與圖說為暫擬。")

    return page(
        opening,
        name_tape("入學前：入伍訓練"),
        basic,
        name_tape("四個暑假"),
        summers,
        name_tape("EMT-1 證照"),
        emt,
        name_tape("軍護教育課程"),
        hours,
        supply,
        actions(text_link("畢業後的服役與職涯", L("dept:D-2")), text_link("實習規定與表單", L("dept:F-2-4"))),
        owner=META["owner"],
    )
