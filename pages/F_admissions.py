from components import (as_of, page, name_tape, statement, p, button, text_link, actions, illo_slot, split,
                        route_list, facts, back_to_top, draft, note)
from links import L

META = {"id": "F", "slug": "admissions", "title": "招生專區", "owner": "院窗口"}

# Official sources (verbatim text below is copied from these)
U_BACH = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2009"      # 學校招生專區【大學部】：正期班簡章
U_GRAD = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2004"      # 學校招生專區【碩、博班】：研究所簡章與日期
U_GRAD_APPLY = "https://sas.ndmctsgh.edu.tw/IASS/FrontShowAdmissionList.aspx?D=OAS.API&N=OAS.API"
U_RDRC = "https://rdrc.mnd.gov.tw/"                               # 國防部人才招募
U_CAMP = L("F-2")


def _source(text, href, label):
    """Where the plain (verbatim) lines above came from."""
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def _anchor(anchor_id, *blocks):
    return f'<div id="{anchor_id}">' + "".join(blocks) + "</div>"


def render():
    opening = "".join([
        statement(
            draft("想當護理師，也想穿上軍服？從這裡選你的路。"),
            draft("護理學院有學士班、碩士班與博士班。高中畢業就能報考學士班；已經是護理師、想再深造，可以讀碩士班；"
                  "有護理相關碩士學位、想走研究與教學，可以讀博士班。三種學制適合誰、去哪裡報名，這一頁都看得到。"),
        ),
        actions(button("看學士班招生簡章", U_BACH), button("看碩、博士班招生簡章", U_GRAD, primary=False)),
    ])

    # One router for the one decision: which programme fits (the three programmes, plus parents and the camp).
    choose = route_list([
        ("學士班（護理學系）：高中（職）生，想成為軍護",
         draft("給高中（職）畢業生。四年學護理、也接受軍事訓練；畢業後軍費生任官，成為軍中的護理人員，"
               "代訓生由輔導會分發服務。"
               "每年 3 月透過「軍事學校正期班甄選入學」報名。"),
         "#bachelor"),
        ("碩士班（護理研究所）：已是護理師，想專精或當專科護理師",
         draft("給已有護理學士學位或護理師證書、想專精一科的人，包括想成為專科護理師的臨床護理師。"
               "分四個組，每年秋天甄試、冬天一般考試。"),
         "#master"),
        ("博士班（護理研究所）：有護理碩士學位，想走研究與教學",
         draft("給已有護理相關碩士學位、想投入研究與教學的人。招生資訊整理中，以學校公告為準。"),
         "#doctoral"),
        ("我是家長，想先了解公費與服役", draft("家長常見問題一次整理"), L("F-1")),
        ("還不確定軍旅適不適合自己", draft("先來暑期營隊待一天"), "#camp"),
    ])

    bachelor = "".join([
        p(draft("學士班由護理學系負責。入學前要先通過國防部的甄選、體檢與測驗，入學後先完成入伍訓練，"
                "再開始四年的護理課程與臨床實習。")),
        as_of("115 學年度軍事學校正期班甄選入學招生簡章"),
        facts([
            ("招生對象", "一、年齡：社會青年、後備役士官兵及替代役備役人員：17 歲至22 歲。<br>"
                        "二、學歷：公私立高中（職）畢業或同等學力。"),
            ("身分別", "軍費生、代訓生（輔導會公費生）<br>"
                      + draft("兩種都是公費生，差別在畢業以後：軍費生畢業任官，服常備軍官現役；"
                              "代訓生是由國軍退除役官兵輔導委員會（輔導會）提供公費的學生，畢業後由輔導會分發所屬機構服務。")),
            ("入伍訓練", "八週"),
            ("修業年限", "修業 4 年。"),
            ("學位授予", "畢業授予所屬學系學士學位。"),
            ("實習醫院", "本校實習醫院為三軍總醫院。"),
            ("公費與服役", draft("入學前請務必了解，見") + " " + text_link("家長常見問題", L("F-1"))),
        ]),
        _source("以上摘自《115 學年度軍事學校正期班甄選入學招生簡章》，新學年度請以新簡章為準。", U_BACH, "歷年大學部招生簡章"),
        note("每年新簡章公布後，請院窗口核對此表；各入學管道與名額每年不同，本頁不列名額，"
             "請導向簡章。若護理學系有可公開的課程特色、實習安排或畢業生出路，請補在此段。"),
        actions(text_link("國防部人才招募（報名、體檢、測驗）", U_RDRC), text_link("護理學系網站", L("D-1"))),
    ])

    master = "".join([
        p(draft("碩士班由護理研究所負責，分四個組；已在醫院工作的護理師，可以選公餘進修。")),
        as_of("116 學年度博、碩士班招生簡章"),
        facts([
            ("分組", "成人暨老人護理學組、婦兒護理學組、精神衛生護理學組、專科護理師組"),
            ("身分別", "全時進修軍費生、全時進修自費生、公餘進修軍職生、公餘進修自費生"),
            ("報名資格", "公立或已立案之私立大學或獨立學院之護理學系畢業得有學士學位或領有護理師證書"
                        "且具護理臨床實務或教學經驗者。<br>"
                        + draft("專科護理師組另有臨床執業年資規定，請看簡章。")),
            ("甄試入學", "網路報名及報名資料繳交日期:115年09月07日(一)至115年10月16日(五)"),
            ("一般考試入學", "網路報名及報名資料繳交日期:115年12月14日(一)至116年01月28日(四)止"),
        ]),
        _source("以上摘自學校招生專區〈【碩、博班】〉與《116 學年度博、碩士班招生簡章》。", U_GRAD, "碩博士班招生簡章"),
        note("報名日期為 116 學年度，每年 9 月前請院窗口更新；各分組、身分別名額以簡章與報名系統為準，本頁不列。"),
        actions(text_link("研究所網路報名系統", U_GRAD_APPLY), text_link("護理研究所網站", L("D-2"))),
    ])

    doctoral = "".join([
        p(draft("博士班的招生說明正在整理。是否招生、如何報考，請以學校招生專區公告為準，也歡迎直接來電詢問。")),
        note("內容清單的分析把博士班寫成「未來博士班」，但學校招生專區〈【碩、博班】〉頁與《116 學年度博、碩士班一般考試入學招生簡章》"
             "已列出「護理學院護理研究所」博士班（不分組；報名資格原文：「具護理相關之碩士學位或同等學力者。」）。"
             "請院窗口與護理研究所確認能否正式對外介紹，確認後本段改寫為正式說明（研究方向、修業年限、指導教授）。"),
        actions(text_link("碩博士班招生簡章", U_GRAD)),
    ])

    camp = split(
        "".join([
            p(draft("還在猶豫嗎？學院在暑假舉辦「國防迷彩天使災難救護營」，高中職生可以先來待一天。")),
            p("結合災難應變、緊急救護、戰術撤離與軍護特色體驗，帶領高中職生與護理學生認識災難情境下的護理專業角色與實務價值。"),
            _source("營隊說明摘自營隊頁面。", U_CAMP, "營隊介紹與報名"),
        ]),
        illo_slot("學員練習傷患包紮（CocoMaterial，重新上色）", "4/3", unit="dept"),
        cols=(7, 5),
    )

    contact = "".join([
        facts([
            ("學士班招生", "教務處招生承辦人：02-87926692。"),
            ("護理學系辦公室", "02-87923100 轉 18165、18167。"),
            ("研究所招生", "招生專線：02-87923126"),
            ("護理研究所", "02-87923100#18165"),
            ("國軍招募客服", "0800-000050"),
            ("上班時間", "週一至週五8:00至17:00(不含例假日及國訂假日)"),
        ]),
        _source("電話摘自招生簡章與學校招生專區。", U_BACH, "學校招生專區"),
        note("請院窗口確認各電話仍有效，並決定是否加上招生信箱、LINE 官方帳號或到校參訪預約方式。"),
    ])

    return page(
        opening,
        note("本頁的 CMS 節點目前是學校招生專區（unit/100143/1861），不是學院自己的頁面；上線時需為學院新建「招生專區」節點。"),
        _anchor("choose", name_tape("三種學制，怎麼選"), choose),
        _anchor("bachelor", name_tape("學士班", unit="dept"), bachelor),
        back_to_top(),
        _anchor("master", name_tape("碩士班", unit="inst"), master),
        back_to_top(),
        _anchor("doctoral", name_tape("博士班", unit="inst"), doctoral),
        _anchor("camp", name_tape("暑期營隊"), camp),
        _anchor("contact", name_tape("招生諮詢"), contact),
        actions(text_link("最新招生訊息", L("B-3"))),
        owner=META["owner"],
    )
