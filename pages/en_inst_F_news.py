from components import (page, name_tape, statement, p, text_link, actions, bullets, route_list, draft, note)
from links import L
from pages._en_inst_data import FACEBOOK, zh

META = {"id": "F", "slug": "news", "title": "News", "owner": "院窗口", "site": "en_inst"}

# Route landing only: this static page cannot pull headlines, and no English news items exist yet, so no headlines
# are shown. Facebook link from the Institute's current left menu (pages/inst_B_news.py).


def render():
    opening = "".join([
        statement(
            draft("Research news from the Institute."),
            draft("English news covers research highlights, publications, graduate achievements, seminars and "
                  "international academic exchange. Admissions and internal notices are published in Chinese only."),
        ),
        actions(zh("inst:B")),
    ])

    what = "".join([
        p(draft("We post English news about:")),
        bullets([
            draft("Research highlights and new projects"),
            draft("Publications by faculty and graduate students"),
            draft("Graduate student achievements and awards"),
            draft("Seminars, lectures and conferences"),
            draft("International academic exchange and visits"),
        ]),
    ])

    routes = route_list([
        ("Academic Activities", draft("Records of lectures, conferences and training already held"),
         L("en_inst:D-3")),
        ("Publications and Graduate Research", draft("Selected recent papers by year"), L("en_inst:D-2")),
        ("College of Nursing News", draft("College-wide research, collaboration and visits"), L("en:H")),
    ], unit="inst")

    return page(
        opening,
        name_tape("What We Post"),
        what,
        note("英文消息需在 CMS 新建英文最新消息模組（en_inst 尚無節點）；建立後把本頁連到該模組，並由院窗口依上列五類挑選發布。"
             "不翻譯招生、課務、口試、獎學金公告與校內行政通知。目前沒有任何英文消息，本頁不放範例標題。"),
        name_tape("Where to Look Now"),
        routes,
        p(draft("Photos and day-to-day updates, mostly in Chinese, are posted on the 國防護理 (Defense Nursing) "
                "Facebook page."), muted=True),
        actions(text_link("國防護理 on Facebook", FACEBOOK), zh("inst:B")),
        owner=META["owner"],
    )
