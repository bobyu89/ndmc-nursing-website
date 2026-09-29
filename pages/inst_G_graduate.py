from urllib.parse import quote

from components import (page, name_tape, statement, p, button, text_link, actions, route_list, draft, note)
from links import L
from tokens import SITE

META = {"id": "G", "slug": "graduate", "title": "研究生專區", "owner": "院窗口", "site": "inst"}

# 現行節點 https://wwwndmc.ndmutsgh.edu.tw/unit/100181/6533（「學生專區」）內容：
# 「入學資格與修業規定(詳見研究生手冊)」全文 + 研究生手冊與 11 個附件表單。
# 改版後：修業規定文字歸「修業資訊」E／E-2，附件表單歸 G-3 表單下載模組，本頁只帶路。
# 研究生手冊 PDF 與校務資訊系統網址取自該節點。

U_HANDBOOK = SITE + quote("/files/web/192/file_up/100181/13936/國防醫學大學護理研究所碩士研究生手冊_09182025_公告.pdf")
U_SAS = "https://sas.ndmctsgh.edu.tw/IASS/Logout.aspx"


def render():
    opening = "".join([
        statement(
            draft("研究生要辦的事，從這裡開始。"),
            draft("報到選課、研究倫理、表單、重要日期與常用系統，各有一頁。"
                  "規定以研究生手冊為準，手冊放在最上面。"),
        ),
        actions(button("研究生手冊（PDF）", U_HANDBOOK), text_link("校務資訊系統", U_SAS)),
    ])

    tasks = route_list([
        ("剛入學：報到、選課、選指導教授", draft("新生須知、註冊、第一學期必修與指導教授申請"), L("inst:G-1")),
        ("做研究前：研究倫理與送審", draft("研究倫理教育必修課、人體試驗審議與三總護理部收案申請"), L("inst:G-2")),
        ("要交件：表單下載", draft("指導教授申請、研究計劃口試、學位論文口試與抵免學分等表單"), L("inst:G-3")),
        ("排時間：重要日程", draft("選課、研究計劃口試、學位論文口試與畢業的時間點"), L("inst:G-4")),
        ("找系統：研究生常用連結", draft("校務資訊、數位學習平台、圖書館電子資源與論文系統"), L("inst:G-5")),
    ], unit="inst")

    rules = "".join([
        p(draft("學分、修業年限、研究計劃與學位論文口試的完整規定，放在修業資訊。")),
        actions(text_link("修業資訊", L("inst:E")), text_link("修業規定", L("inst:E-2")),
                text_link("學位審查", L("inst:E-3"))),
    ])

    return page(
        opening,
        name_tape("我要辦的事"),
        tasks,
        note("現行「學生專區」節點（unit/100181/6533）的修業規定文字，改版後移到修業規定頁；"
             "研究生手冊與 11 個附件表單移到表單下載模組（G-3）。搬移前請所辦確認附件都是最新版（目前為 2025 年 8–9 月版）。"),
        name_tape("修業規定"),
        rules,
        name_tape("最新消息"),
        p(draft("選課、口試與獎學金的通知，會發在研究所公告。")),
        actions(text_link("課務公告", L("inst:B-2")), text_link("口試公告", L("inst:B-3")),
                text_link("獎學金公告", L("inst:B-4"))),
        owner=META["owner"],
    )
