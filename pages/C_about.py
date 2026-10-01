from components import page, name_tape, statement, p, route_list, actions, text_link, tape_surface, draft
from links import L

META = {"id": "C", "slug": "about", "title": "認識本院", "owner": "院窗口"}


def render():
    opening = statement(
        draft("從一個護理班，走到今天的護理學院。"),
        # 下設單位取自現行「組織架構」頁（unit/100010/4125）架構圖。
        "國防醫學大學護理學院培育軍護人才，下設護理學系與護理研究所。"
        "這一頁幫你找到學院的來歷、理念與組織。",
    )

    # 取自現行「歷史沿革」頁（unit/100010/6804），原文照錄。
    origin = tape_surface(
        p("國防醫學大學護理學院護理學系源於上海江灣之「高級護理職業班」，由 周美玉將軍於民國32年創立，"
          "招收初中畢業之學生，修業四年半，為我國最早開辦之護理人員職業教育訓練班。"),
        p("民國114年成立護理學院，成為推動臺灣高等護理教育的先鋒。"),
        actions(text_link("看完整歷史沿革", L("C-3"))),
    )

    routes = route_list([
        ("院長的話", "院長談治院理念與發展方向", L("C-1")),
        ("學院簡介", "學院是什麼、軍陣護理的定位、院徽的意義", L("C-2")),
        ("歷史沿革與軍護傳承", "周美玉將軍與學院的大事年表", L("C-3")),
        ("組織架構", "學院、學系、研究所與各委員會的關係", L("C-4")),
        ("教育理念", "我們對人、護理、健康與環境的看法", L("C-5")),
    ])

    return page(
        opening,
        name_tape("學院的起點"),
        origin,
        name_tape("認識本院各頁"),
        routes,
        owner=META["owner"],
    )
