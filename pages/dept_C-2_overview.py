from components import page, name_tape, statement, p, feature_list, tape_surface, text_link, actions, draft, note
from links import L

META = {"id": "C-2", "slug": "overview", "title": "學系簡介", "owner": "院窗口", "site": "dept"}

# 教育宗旨取自現行「學士班課程地圖」頁（https://wwwndmc.ndmutsgh.edu.tw/unit/100010/3642），原文照錄。


def render():
    opening = statement(
        draft("護理學系，兩頁就能認識。"),
        draft("一頁講學系從哪裡來、和其他護理系哪裡不一樣；一頁講畢業時你會具備哪些能力。"),
    )

    aim = tape_surface(
        p("培育兼具人文素養與護理專業能力，符合軍民健康照顧系統所需之專業人才。"),
        p(draft("護理學系的教育宗旨"), muted=True),
    )

    pages = feature_list([
        ("學系特色與定位",
         draft("民國36年設立，是我國第一個護理學系。這一頁說明學系的來歷、課程怎麼安排、在哪裡實習，"
               "以及軍陣護理為什麼是我們的特色。"),
         L("dept:C-2-1"), "dept", "特"),
        ("教育目標與核心能力",
         draft("學系訂下八項教育目標與十三項學生核心能力，每一門課都對應其中幾項。想知道讀完四年會變成什麼樣的人，看這一頁。"),
         L("dept:C-2-2"), "dept", "能"),
    ])

    return page(
        opening,
        name_tape("教育宗旨"),
        aim,
        name_tape("學系簡介"),
        pages,
        note("本頁只做導流。學系簡介正文依 Notion 內容清單取自年報，放在「學系特色與定位」（C-2-1）。"),
        actions(text_link("系主任的話", L("dept:C-1")), text_link("護理學院簡介", L("C-2"))),
        owner=META["owner"],
    )
