from components import (page, name_tape, statement, p, button, text_link, actions, photo, split,
                        feature_list, route_list, draft, note)
from links import L

META = {"id": "I", "slug": "campus-life", "title": "校園生活", "owner": "院窗口", "site": "dept"}

# 「凡本學校護理學系之在學學生均為本會會員。」逐字取自系學會頁圖片 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6796
# 照片標題取自學系首頁輪播 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6510（2026-09-29 擷取）。
# 照片：輪播「N76加冠」（1920×1280，2026-10-01 核對 200 image/jpeg）。
IMG_CAPPING = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/"
               "LINE_ALBUM_1140317N76%E5%8A%A0%E5%86%A0_250706_9.jpg")


def render():
    opening = split(
        "".join([
            statement(
                draft("上課、實習之外，也有一起過的一年。"),
                draft("迎新、加冠、系大會、畢業典禮，多半由系學會和同學一起辦。外國護理學生來訪時，也由同學帶著認識學校。"),
            ),
            actions(button("看學生活動", L("dept:I-2")), text_link("認識系學會", L("dept:I-1"))),
        ]),
        photo(IMG_CAPPING, "加冠典禮：穿白色護理服、戴護士帽的學生與師長大合照", "4/3", caption="加冠典禮合照"),
        cols=(7, 5), align="start",
    )

    entries = feature_list([
        ("系學會",
         "凡本學校護理學系之在學學生均為本會會員。會長、副會長由全系同學投票選出，帶著各組辦活動。",
         L("dept:I-1"), "dept", "會"),
        ("學生活動",
         draft("迎新、加冠、小畢典、系大會、大護盃、校慶，一年的活動與照片都在這裡；也可以找到全校社團。"),
         L("dept:I-2"), "dept", "活"),
        ("境外學生來校交流",
         "美國、日本等地的護理學生來訪，同學接待他們，也分享臺灣的護理與文化。",
         L("dept:I-3"), "dept", "訪"),
    ])

    related = route_list([
        ("海外交流專區", draft("學系學生出國交流的紀錄"), L("dept:H")),
        ("學生專區", draft("獎學金、表單、重要日程與常用連結"), L("dept:J")),
    ], unit="dept")

    return page(
        opening,
        name_tape("三個入口"),
        entries,
        name_tape("在校生也常用"),
        related,
        owner=META["owner"],
    )
