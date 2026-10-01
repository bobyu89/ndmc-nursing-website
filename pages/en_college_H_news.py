from components import page, name_tape, statement, p, text_link, actions, route_list, draft, note
from links import L
from pages._en_college_shared import zh

META = {"id": "H", "slug": "news", "title": "News", "owner": "院窗口", "site": "en_college"}

# Route landing only: no headlines are written here. Facebook link from pages/B_news.py (current left menu).
FACEBOOK = "https://www.facebook.com/profile.php?id=100063652101597"


def render():
    opening = "".join([
        statement(
            draft("News for colleagues and partners abroad."),
            draft("Research, international collaboration, visits and major College updates, "
                  "chosen for international readers. Each category opens a full list, newest first."),
        ),
        actions(zh("B")),
    ])

    categories = route_list([
        ("Research", draft("New projects, publications and research awards"), L("en:H-1")),
        ("International Collaboration", draft("Agreements, exchanges and joint activities with partners abroad"), L("en:H-2")),
        ("Visits and Events", draft("Delegation visits, guest lectures and conferences"), L("en:H-3")),
        ("College Updates", draft("Major institutional news"), L("en:H-4")),
    ])

    units = route_list([
        ("Department of Nursing news", draft("Teaching, practicum and student achievements"), L("en_dept:H")),
        ("Graduate Institute of Nursing news", draft("Research, publications and seminars"), L("en_inst:F")),
    ])

    return page(
        opening,
        name_tape("News Categories"),
        note("本頁為靜態 HTML，無法自動帶入標題；四個分類需在 CMS 新建英文消息模組節點（或一個模組加分類），建好後把連結改過去。"
             "英文消息依讀者挑選，不逐則翻譯中文公告：不放招生、獎學金結果、校內表單與行政通知。每則上線前逐行檢查英文、連結、職稱、學位與圖片替代文字。"),
        categories,
        name_tape("From the Academic Units"),
        units,
        name_tape("More"),
        p(draft("Photos of recent activities are posted on the College's Facebook page, in Chinese.")),
        actions(text_link("College of Nursing on Facebook (Chinese)", FACEBOOK), zh("B")),
        owner=META["owner"],
    )
