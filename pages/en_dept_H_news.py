from components import page, name_tape, statement, p, text_link, actions, route_list, split, illo_slot, draft, note
from links import L

META = {"id": "H", "slug": "news", "title": "News", "owner": "院窗口", "site": "en_dept"}


def render():
    opening = statement(
        draft("News from the Department of Nursing"),
        draft("Stories chosen for international readers: new ways of teaching, practicum highlights, student "
              "achievements and exchange outcomes."),
    )

    topics = route_list([
        ("Teaching innovation", draft("Simulation, VR and MR, and new course designs"), L("en_dept:C-3")),
        ("Practicum highlights", draft("Hospital, community and military nursing practicum"), L("en_dept:C-2")),
        ("Student achievements", draft("Competitions, student research and milestones"), L("en_dept:C-4")),
        ("Exchange outcomes", draft("Visits, partner institutions and participant reflections"), L("en_dept:E")),
    ], unit="dept")

    college = split(
        "".join([
            p(draft("College-wide research, international collaboration and visits are published on the College of "
                    "Nursing English site.")),
            actions(text_link("College of Nursing News", L("en:H")),
                    text_link("中文：學系公告", L("dept:B"))),
        ]),
        illo_slot("Students reading a notice board (CocoMaterial, recoloured)", "4/3", unit="dept"),
        cols=(7, 5),
    )

    return page(
        opening,
        note("英文消息需新建 CMS 最新消息模組節點；本頁為靜態 HTML，無法自動帶入標題，暫以四類主題導向相關頁面。"
             "消息模組建立後，請院窗口把下方四列改為各分類的消息列表連結。選稿原則：只放對國外讀者有意義的消息"
             "（教學創新、實習亮點、學生成就、交流成果），不翻譯招生、獎學金結果與校內行政公告；每則附英文圖說。"),
        name_tape("Topics"),
        topics,
        name_tape("College News"),
        college,
        owner=META["owner"],
    )
