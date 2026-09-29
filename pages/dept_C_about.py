from components import (page, name_tape, statement, p, split, patch, illo_slot, route_list, tape_surface, text_link,
                        actions, button, draft, note)
from links import L
from tokens import C

META = {"id": "C", "slug": "about", "title": "認識本系", "owner": "院窗口", "site": "dept"}

# 原文來源：歷史沿革 https://wwwndmc.ndmutsgh.edu.tw/unit/100010/6804
#           學士班課程地圖（教育宗旨） https://wwwndmc.ndmutsgh.edu.tw/unit/100010/3642


def render():
    opening = split(
        statement(
            draft("國內第一個護理學系，培育軍中的護理人員。"),
            draft("護理學系是護理學院的學士班。四年裡學護理、接受軍事訓練，也到醫院實習；"
                  "這一頁帶你認識學系的來歷、系主任與我們想培養的人。"),
        ),
        '<div class="mx-auto" style="width:70%;max-width:260px;">' + patch(
            "護理學系", "學士班", unit="dept",
            illo=illo_slot("護理學系系徽或護生加冠（CocoMaterial，重新上色）", "1/1", unit="dept"),
            tab="護理學院", backing=C["tape"]) + "</div>",
        cols=(7, 5),
    )

    # 兩段取自現行「歷史沿革」頁（unit/100010/6804），原文照錄。
    roots = tape_surface(
        p("國防醫學大學護理學院護理學系源於上海江灣之「高級護理職業班」，由 周美玉將軍於民國32年創立，"
          "招收初中畢業之學生，修業四年半，為我國最早開辦之護理人員職業教育訓練班。"),
        p("民國36年周將軍更進而設立護理學系，成為我國首創之護理高等學府。"),
        actions(text_link("學院的歷史沿革與軍護傳承", L("C-3"))),
    )

    # 取自現行「學士班課程地圖」頁（unit/100010/3642），原文照錄。
    aim = "".join([
        p("培育兼具人文素養與護理專業能力，符合軍民健康照顧系統所需之專業人才。"),
        p(draft("這是學系的教育宗旨。說得白話一點：我們培養的護理師，要能在一般醫院照顧病人，也能在軍中執行任務。"),
          muted=True),
    ])

    routes = route_list([
        ("系主任的話", draft("系主任談辦學理念，以及對學生的期許"), L("dept:C-1")),
        ("學系簡介", draft("學系是什麼樣的地方，一頁看完"), L("dept:C-2")),
        ("學系特色與定位", draft("學系的來歷、課程與實習的特色"), L("dept:C-2-1")),
        ("教育目標與核心能力", draft("畢業時要具備的八項目標、十三項能力"), L("dept:C-2-2")),
    ], unit="dept")

    faculty = "".join([
        p(draft("學系老師的完整名單，統一放在護理學院的「師資陣容」，可以依職級與專長查看每位老師。")),
        actions(button("看師資陣容", L("E-1"))),
    ])

    return page(
        opening,
        name_tape("學系的起點"),
        roots,
        name_tape("教育宗旨"),
        aim,
        name_tape("認識本系各頁"),
        routes,
        name_tape("師資陣容"),
        faculty,
        note("師資名單只在學院「師資陣容」（E-1）維護一份，本頁不另列老師，避免兩邊資料不一致。"),
        owner=META["owner"],
    )
