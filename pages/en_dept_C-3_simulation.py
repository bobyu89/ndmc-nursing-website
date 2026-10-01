from components import (page, name_tape, statement, p, h4, text_link, actions, split, photo_slot, photo, illo_slot,
                        draft, note)
from links import L

META = {"id": "C-3", "slug": "simulation", "title": "Simulation and Learning Spaces", "owner": "圖儀、哲君",
        "site": "en_dept"}

# Plain sentences translate the verified text of 教學設備 unit/100010/1463 (pages/E-3_facilities.py, 2026-09-29).
# VR/MR and the self-learning classroom's use are drafted there too and stay drafted here.
# Photos: the two images published on 教學設備 unit/100010/1463 (checked 200 image/png on 2026-10-01).
IMG_SIM = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E8%99%9B%E6%93%AC%E4%B8%AD%E5%BF%83.png"
IMG_WARD = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/"
            "%E7%A4%BA%E7%AF%84%E5%AF%A6%E7%BF%92%E7%97%85%E6%88%BF2.png")


def render():
    opening = "".join([
        statement(
            draft("Practice in the simulation room first, then at the bedside."),
            draft("From the amphitheater and the demonstration ward to the simulation center, students rehearse "
                  "assessment, nursing skills and critical care in settings close to real practice."),
        ),
        actions(text_link("Visit the Department", L("en_dept:G")), text_link("中文：教學設備", L("E-3"))),
    ])

    center = split(
        "".join([
            p("The simulation center has three simulation rooms with a small central control room between them, "
              "from which the adult and pediatric labs can be observed at the same time."),
            p("It is equipped with one-way mirrors, a video recording system, computers and two electric beds, and is "
              "linked to the nursing station outside, where other students can watch the simulation live."),
            p("The center is used for advanced medical-surgical nursing, advanced obstetric and pediatric nursing, "
              "and critical care nursing courses, and for OSCE teaching in the bachelor's program."),
        ]),
        photo(IMG_SIM, "A pediatric simulation room in the simulation center, with a crib and bedside equipment", "4/3"),
        cols=(7, 5), align="start",
    )

    ward = "".join([
        photo(IMG_WARD, "Demonstration ward: a row of hospital beds with privacy curtains", "16/9"),
        p(draft("The demonstration ward has 15 general beds, each with a bedside table and an overbed table.") + " "
          "A long-term care demonstration bed was added in 2018."),
        p("Since 2007 a central gas system has supplied air flow and suction to every bed, bringing the ward "
          "closer to a clinical setting."),
        p("The ward is mainly used for undergraduate physical examination and assessment, basic nursing skills "
          "practice and the medical research camp."),
    ])

    amphitheater = split(
        photo_slot("Demonstration classroom (amphitheater)", "4/3"),
        "".join([
            p("The amphitheater has 134 seats and can hold up to 150 people. It is used for all department courses "
              "and for workshops."),
        ]),
        cols=(5, 7), align="center",
    )

    new_tools = "".join([
        split(
            "".join([
                h4("Smart interactive self-learning classroom"),
                p("Opened in 2025."),
                p(draft("A space where students practice nursing skills on their own.")),
            ]),
            photo_slot("Smart interactive self-learning classroom", "4/3"),
            cols=(7, 5), align="start",
        ),
        split(
            "".join([
                h4(draft("VR and MR simulation")),
                p(draft("Virtual reality (VR) and mixed reality (MR) scenarios let students practice clinical "
                        "situations safely, and MR teaching videos support preparation and review.")),
            ]),
            illo_slot("Nursing student practicing with an MR headset (CocoMaterial, recolored)", "4/3", unit="dept"),
            cols=(7, 5), reverse=True, align="start",
        ),
    ])

    return page(
        opening,
        name_tape("Simulation Center"),
        center,
        name_tape("Demonstration Ward"),
        ward,
        note("「長照示範病床 2018」「中央氣體 2007」由原文民國 107、96 年換算。原文「醫研營」暫譯 medical research camp，"
             "請確認英文名稱。照片沿用中文教學設備頁的虛擬中心與示範實習病房照片。床數兩處公開資料不一致：中文教學設備頁（unit/100010/1463）寫一般病床 15 張；舊英文設施頁（uniten/100010/867）寫「12 general beds, 2 examination beds」。本頁暫依中文頁並標待確認，請圖儀確認現況。"),
        name_tape("Amphitheater"),
        amphitheater,
        name_tape("New Learning Tools"),
        new_tools,
        note("圖儀、哲君請提供：自學教室的設備與使用方式、VR／MR 設備名稱、使用課程與實際照片（中文站此段亦為暫擬）；"
             "每張照片附一句英文圖說。"),
        owner=META["owner"],
    )
