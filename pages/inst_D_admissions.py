from components import (page, name_tape, statement, p, button, text_link, actions, route_list, facts, draft, note)
from links import L
from tokens import SITE

META = {"id": "D", "slug": "admissions", "title": "招生專區", "owner": "院窗口", "site": "inst"}

# 官方來源（以下未加「待確認」的文字皆原文照錄）
U_GRAD = SITE + "/unit/100143/2004"   # 學校招生專區【碩、博班】
U_APPLY = "https://sas.ndmctsgh.edu.tw/IASS/FrontShowAdmissionList.aspx?D=OAS.API&N=OAS.API"


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def render():
    opening = "".join([
        statement(
            draft("已經是護理師，想再往上走一步？"),
            draft("護理研究所招收碩士班，分四個學組。每年秋天甄試、冬天一般考試，"
                  "全時進修或一邊工作一邊讀都可以報考。"),
        ),
        actions(button("看招生資訊", L("inst:D-1")), text_link("研究所網路報名系統", U_APPLY)),
    ])

    summary = "".join([
        facts([
            ("分組", "成人暨老人護理學組、婦兒護理學組、精神衛生護理學組、專科護理師組"),
            ("身分別", "全時進修軍費生、全時進修自費生、公餘進修軍職生、公餘進修自費生"),
            ("報名資格", "公立或已立案之私立大學或獨立學院之護理學系畢業得有學士學位或領有護理師證書"
                        "且具護理臨床實務或教學經驗者。"),
            ("甄試入學", "網路報名及報名資料繳交日期:115年09月07日(一)至115年10月16日(五)"),
            ("一般考試入學", "網路報名及報名資料繳交日期:115年12月14日(一)至116年01月28日(四)止"),
        ]),
        _source("以上摘自學校招生專區〈【碩、博班】〉與《116 學年度博、碩士班招生簡章》。", U_GRAD, "碩博士班招生簡章"),
        note("日期為 116 學年度，每年 9 月前請院窗口依新簡章更新。各學組、身分別名額以簡章與報名系統為準，本頁不列。"),
    ])

    doctoral = "".join([
        p(draft("學校招生專區〈【碩、博班】〉的口試日程已列出護理研究所博士班。博士班怎麼報考、研究方向為何，"
                "說明整理中；想報考請先來電詢問。")),
        note("內容清單把博士班寫成未來規劃，但學校招生專區與《116 學年度博、碩士班招生簡章》已列出護理研究所博士班。"
             "請院窗口與研究所確認能否正式對外介紹；確認後改寫為正式說明（招生對象、研究方向、修業年限）。"),
        actions(text_link("博士班報考資格與口試日期", L("inst:D-1"))),
    ])

    routes = route_list([
        ("招生資訊", draft("碩士班、博士班的報考資格、考試科目、時程與簡章"), L("inst:D-1")),
        ("獎助學金", draft("研究生可以申請的獎學金、資格與申請方式"), L("inst:D-2")),
        ("常見問題", draft("報考、修業、指導教授與研究生活"), L("inst:D-3")),
    ], unit="inst")

    contact = "".join([
        facts([
            ("研究所招生", "招生專線：02-87923126"),
            ("護理研究所", "02-87923100#18165"),
            ("上班時間", "週一至週五8:00至17:00(不含例假日及國訂假日)"),
        ]),
        _source("電話摘自學校招生專區與招生簡章。", U_GRAD, "學校招生專區"),
        note("請院窗口確認研究所電話仍有效，並決定是否加上研究所信箱、招生說明會或到所參訪的預約方式。"),
    ])

    return page(
        opening,
        name_tape("碩士班招生摘要"),
        summary,
        name_tape("博士班"),
        doctoral,
        name_tape("招生專區各頁"),
        routes,
        name_tape("招生諮詢"),
        contact,
        actions(text_link("最新招生公告", L("inst:B-1")), text_link("學院招生專區（學士班與碩博士班）", L("F"))),
        owner=META["owner"],
    )
