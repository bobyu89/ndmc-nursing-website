from urllib.parse import quote

from components import (page, name_tape, statement, p, text_link, actions, feature_list, route_list, draft, note)
from links import L
from tokens import SITE

META = {"id": "E", "slug": "study", "title": "修業資訊", "owner": "院窗口", "site": "inst"}

U_RULES = SITE + "/unit/100181/6533"  # 研究所「學生專區」：入學資格與修業規定、手冊與表單
U_HANDBOOK = SITE + quote("/files/web/192/file_up/100181/13936/國防醫學大學護理研究所碩士研究生手冊_09182025_公告.pdf")


def render():
    opening = statement(
        draft("從入學到口試，修業的每一步都在這裡。"),
        draft("碩士班修業期限兩年，需要時可以延長。課程、規定與學位審查各有一頁，先看你現在走到哪一步。"),
    )

    # 各步驟的依據：研究所學生專區的修業規定與附件表單名稱（附錄3-2、3-3、3-4）。步驟順序為整理後的草稿。
    steps = feature_list([
        ("修研究倫理教育", "新生第一學年必修，0 學分；沒有完成，不能參加學位考試。", L("inst:E-1"), "inst", "倫"),
        ("修課", "依入學學年度與學組修滿學分；有全職工作的人，每學期修課學分有上限。", L("inst:E-2"), "inst", "課"),
        ("申請指導教授", draft("選定老師後，填寫論文指導教授申請表，並保留論文指導記錄。"), L("inst:E-3"), "inst", "師"),
        ("研究計畫口試", draft("完成研究計畫後申請口試；涉及人體研究的，還要通過倫理審查。"), L("inst:E-3"), "inst", "計"),
        ("學位論文口試", draft("論文完成後申請學位考試，通過即可辦理畢業。"), L("inst:E-3"), "inst", "考"),
    ])

    routes = route_list([
        ("課程資訊", draft("碩士班與博士班的課程、課程地圖"), L("inst:E-1")),
        ("修業規定", draft("學分、修業年限、修課上限、補修與抵免"), L("inst:E-2")),
        ("學位審查", draft("研究計畫、論文格式、學位考試與口試流程"), L("inst:E-3")),
    ], unit="inst")

    return page(
        opening,
        name_tape("修業流程"),
        steps,
        note("五個步驟依研究生專區的修業規定與附件表單整理，順序與時間點待確認。研究生手冊內有「碩士班修業規定流程圖」"
             "（圖2-1-1），請院窗口提供圖檔或確認步驟，收到後可在此放流程圖。"),
        name_tape("修業資訊各頁"),
        routes,
        p(draft("完整規定寫在研究生手冊，表單在表單下載。"), muted=True),
        actions(text_link("研究生手冊（PDF）", U_HANDBOOK), text_link("表單下載", L("inst:G-3")),
                text_link("重要日程", L("inst:G-4"))),
        note("研究生手冊與各式表單目前掛在研究所「學生專區」（" + U_RULES + "）。G-3 表單下載模組建好後，"
             "請把表單搬過去，本頁連結不用改。"),
        owner=META["owner"],
    )
