from components import (page, name_tape, statement, p, split, photo, text_link, actions, timeline,
                        tape_surface, bullets, back_to_top, draft, note)
from links import L
from tokens import C, S
from pages._en_college_shared import zh, IMG_EMBLEM

GENERAL_PHOTO = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E8%BB%8D%E8%AD%B7%E5%A4%A7%E9%A0%AD%E7%85%A71.jpg"

META = {"id": "B-2", "slug": "overview", "title": "Overview and History", "owner": "哲君", "site": "en_college"}

# Plain sentences are faithful translations of verified (non-draft) Chinese text:
#   timeline, origins — pages/C-3_history.py and pages/C-2_overview.py (歷史沿革 unit/100010/6804)
#   units — pages/C-4_organization.py; emblem — pages/C-2_overview.py
#   educational philosophy — pages/C-5_philosophy.py (教育理念 unit/100010/1475)
# The mission sentence comes from the old English History & Vision page (uniten/100010/3353), which predates the
# 2025 College and carries no date, so it stays draft. Years on patches are ROC year + 1911.


def _jump(items, lead=None):
    """Compact jump index in the style of components.roster_index: [(label, href), ...]."""
    links = "".join(
        f'<a href="{href}" style="display:inline-block;min-height:44px;padding:10px 0;margin-right:{S[3]};color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;">{label}</a>'
        for label, href in items)
    head = f'<span style="margin-right:{S[2]};color:{C["ink_soft"]};">{lead}</span>' if lead else ""
    return f'<div style="margin:0 0 {S[2]};max-width:44em;line-height:1.4;">{head}{links}</div>'


def _anchor(anchor_id, *blocks):
    return f'<div id="{anchor_id}">' + "".join(blocks) + "</div>"


def render():
    opening = "".join([
        statement(
            draft("Educating military nurses since 1943."),
            draft("The College of Nursing brings together the Department of Nursing and the Graduate Institute of Nursing. "
                  "Its students study nursing, receive military training and serve as nursing officers after graduation."),
        ),
        _jump([("The College today", "#today"), ("Military nursing", "#military"),
               ("Educational philosophy", "#philosophy"), ("General Mei-Yu Chow", "#general"),
               ("Timeline 1943–2025", "#timeline"), ("The College emblem", "#emblem")]),
        actions(zh("C-2", "中文版：學院簡介"), zh("C-3", "中文版：歷史沿革")),
    ])

    today = "".join([
        p("The College of Nursing was established in 2025. It oversees two academic units: the Department of Nursing, "
          "which runs the undergraduate program, and the Graduate Institute of Nursing, which runs the graduate programs."),
        p(draft("Our mission is to educate nurses who can care for combat casualties, to provide nursing education and "
                "clinical services, and to develop military nursing research that meets national and societal needs.")),
        note("使命一句取自舊英文頁 History & Vision（uniten/100010/3353，學院成立前的「School of Nursing」版本，未註明年份）。"
             "請哲君確認是否仍適用於學院，或提供學院的英文使命／願景定稿。"),
        actions(text_link("Organization", L("en:B-3")), text_link("Academic Units", L("en:C"))),
    ])

    military = "".join([
        p(draft("Military nursing means providing care in special settings such as military units, the field, ships, "
                "aircraft and disaster areas. This is what most clearly distinguishes the College from other nursing schools.")),
        p(draft("The curriculum combines military training with clinical nursing. Students train in military hospitals "
                "such as Tri-Service General Hospital, and trauma and disaster nursing is a focus of teaching and research.")),
        actions(text_link("Research Highlights", L("en:D-2"))),
    ])

    philosophy = tape_surface(
        p("We see nursing education as professional training that joins theory and practice. It stresses hands-on "
          "experience and uses varied teaching strategies, step by step, to build students' knowledge, attitudes and "
          "skills in nursing."),
        p("Our philosophy rests on four concepts:"),
        bullets(["the person", "nursing", "health", "the environment"]),
        actions(zh("C-5", "中文版：教育理念全文")),
    )

    general = split(
        photo(GENERAL_PHOTO, "Black-and-white portrait of General Mei-Yu Chow in military uniform", "3/4"),
        "".join([
            p("General Mei-Yu Chow founded Taiwan's military nursing system and is remembered as its mother."),
            p(draft("She founded the Senior Nursing Vocational Class in 1943 and the Department of Nursing in 1947, "
                    "the beginnings of the College. She was also the first Director of Nursing at Taipei Veterans General "
                    "Hospital and the first President of the Nurses Association of the Republic of China after it resumed in Taiwan.")),
        ]),
        cols=(4, 8), align="start",
    )

    events = timeline([
        ("1943", "The Senior Nursing Vocational Class",
         "Founded by General Mei-Yu Chow in Jiangwan, Shanghai. It admitted junior high school graduates for a "
         "four-and-a-half-year course and was the earliest vocational training program for nurses in the country.",
         "college"),
        ("1947", "Department of Nursing",
         "General Chow went on to establish the Department of Nursing, the country's first institution of higher "
         "nursing education.", "dept"),
        ("1949", "Move to Taiwan",
         "The Department moved to Taiwan with the National Defense Medical Center, to Shuiyuandi in Taipei."),
        ("1979", "Graduate Institute of Nursing",
         "Established to meet the needs of nursing education and research, a pioneer of master's-level nursing education in Taiwan.",
         "inst"),
        ("1990", "In-service bachelor's program",
         "Commissioned by the Ministry of Education, the Department added a bachelor's degree program for working nurses. "
         "It stopped public admission in 1994 and graduated 180 nurses in total.", "dept"),
        ("1999", "Move to Neihu",
         "The campus moved to the National Defense Medical Center in Neihu, where a strong faculty and new facilities "
         "carry on the work of educating nurses."),
        ("2018", "Memorial service for General Chow",
         draft("On 10 March 2018, General Chow's remains were moved to the Armed Forces Loyal Spirits Hall "
               "at the Wuzhishan Military Cemetery.")),
        ("2025", "College of Nursing",
         "The College of Nursing was established, becoming a pioneer in advancing higher nursing education in Taiwan. "
         "Its plaque was unveiled on 16 September 2025.",
         "college"),
    ])

    emblem = split(
        photo(IMG_EMBLEM, "College of Nursing emblem: a round badge with red, purple and white tulips above the year 1947, "
                          "ringed by the College's Chinese and English names", "1/1", fit="contain"),
        "".join([
            p("The emblem expresses the College's teaching philosophy: respect for harmony and balance between people "
              "and their environment. "
              "The taiji symbol stands for health of body, mind, spirit and society, and for teaching that is complete "
              "and well rounded."),
            p("The three flowers in full bloom stand for the faculty's three missions of teaching, service and research, "
              "and for the many graduates those missions have produced."),
        ]),
        cols=(4, 8), align="start",
    )

    return page(
        opening,
        _anchor("today", name_tape("The College Today"), today),
        _anchor("military", name_tape("Military Nursing"), military),
        _anchor("philosophy", name_tape("Educational Philosophy"), philosophy),
        back_to_top(),
        _anchor("general", name_tape("General Mei-Yu Chow"), general),
        note("周將軍簡介第一段已依中文頁查證內容譯出；第二段含中華民國護理學會、臺北榮民總醫院的英文名稱，請確認正式名稱後再拿掉待確認。"
             "照片與中文頁相同（軍護大頭照1.jpg），授權同中文頁。"),
        _anchor("timeline", name_tape("Timeline"), events),
        note("時間軸逐句譯自中文「歷史沿革」已查證段落。2018 一筆的「五指山國軍示範公墓國軍忠靈殿」為暫譯，請確認英文名稱。"
             "「水源地」「國防醫學中心」採音譯與舊英文頁用法（National Defense Medical Center），請確認。"),
        back_to_top(),
        _anchor("emblem", name_tape("The College Emblem"), emblem),
        note("中文院徽說明中的鬱金香花色段落，英文版省略。"),
        owner=META["owner"],
    )
