from components import (page, name_tape, statement, p, button, text_link, actions, route_list, draft, note)
from links import L

META = {"id": "B", "slug": "news", "title": "研究所公告", "owner": "院窗口", "site": "inst"}

# 國防護理 Facebook：取自現行研究所網站左側選單（unit/100181/6511）。
FACEBOOK = "https://www.facebook.com/profile.php?id=100063652101597"


def render():
    opening = "".join([
        statement(
            draft("研究所的公告，依你要辦的事分成五類。"),
            draft("招生、課務、口試、獎學金與學術活動各有一個公告區。點進去就是該類的完整列表，最新的排在最上面。"),
        ),
        actions(button("招生公告", L("inst:B-1")), text_link("招生資訊", L("inst:D-1"))),
    ])

    categories = route_list([
        ("招生公告", draft("碩士班、博士班的招生消息、簡章與重要時程"), L("inst:B-1")),
        ("課務公告", draft("選課、開課、課程異動與修業相關消息"), L("inst:B-2")),
        ("口試公告", draft("研究計畫口試、學位論文口試與畢業時程"), L("inst:B-3")),
        ("獎學金公告", draft("各項獎助學金的申請公告與結果"), L("inst:B-4")),
        ("學術活動", draft("即將舉辦的講座、研討會與學術交流"), L("inst:B-5")),
    ], unit="inst")

    return page(
        opening,
        name_tape("公告分類"),
        note("本頁為靜態 HTML，無法自動帶入最新標題，只做分類導流。B-1、B-2、B-3、B-5 需在 CMS 新建最新消息模組；"
             "B-4 沿用現行「獎學金專區」節點（unit/100181/6802）。現行研究所「招生專區」節點（unit/100181/6529）是公告彙整列表，"
             "新建 B-1 後請院窗口決定是否把舊公告搬過去。已辦完的活動紀錄放在「研究成果 › 學術活動」（F-3），不放這裡。"),
        categories,
        name_tape("其他消息"),
        p(draft("全院性的公告看學院最新消息；活動照片與日常消息在國防護理 Facebook。")),
        actions(text_link("學院最新消息", L("B")), text_link("學術活動紀錄", L("inst:F-3")),
                text_link("國防護理 Facebook", FACEBOOK)),
        owner=META["owner"],
    )
