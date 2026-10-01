from components import (page, name_tape, statement, p, bullets, timeline, tape_surface, text_link, actions, draft, note)
from links import L
from tokens import C, TYPE

META = {"id": "B-2", "slug": "overview", "title": "Overview and Learning Outcomes", "owner": "課委會", "site": "en_dept"}

# Translated from verified Chinese text:
#   history      — 歷史沿革 unit/100010/6804 (pages/dept_C-2-1_identity.py, pages/C-3_history.py)
#   aim, abilities — 學士班課程地圖 unit/100010/3642 (pages/dept_C-2-2_goals.py)
#   goals        — 教育宗旨與目標 unit/100010/1471, 學士班教育目標 114.02.10 修訂 (pages/dept_C-2-2_goals.py)
#   curriculum concepts — 學士班課程架構 unit/100010/1492 (pages/dept_C-2-1_identity.py)

AIM = ("To educate professionals with a grounding in the humanities and strong nursing competence, ready to meet "
       "the needs of both the military and the civilian health care systems.")

GOALS = [
    "Care for people with compassion and respect for life.",
    "Have sound medical and nursing knowledge and a global perspective.",
    "Provide safe, high-quality nursing care.",
    "Use clinical reasoning to address the health needs and problems of the people they serve.",
    "Apply ethical and legal thinking to provide appropriate nursing care.",
    "Communicate and collaborate with the people they serve and with interprofessional team members.",
    "Fulfill the professional role of a military nurse with dedication and a sense of mission.",
    "Keep learning and growing throughout their careers.",
]

ABILITIES = ["Humanistic care", "Respect for life", "Biomedical knowledge", "Global perspective", "Nursing skills",
             "Critical thinking", "Evidence-based nursing", "Ethical reasoning", "Communication and collaboration",
             "Leadership", "Dedication to duty", "Military nursing", "Lifelong learning"]


def render():
    opening = statement(
        draft("What our graduates are prepared to do"),
        draft("The department states its purpose as one aim, eight educational goals and thirteen core competencies. "
              "Courses and practicum are mapped to them."),
    )

    history = timeline([
        ("1943", "A nursing class in Shanghai",
         "General Mei-Yu Chow founded the Advanced Nursing Vocational Class in Jiangwan, Shanghai. It admitted "
         "junior high school graduates for four and a half years of study, the country's earliest vocational "
         "training program for nurses.", "college"),
        ("1947", "Department of Nursing founded",
         "General Chow established the Department of Nursing, the country's first institution of higher nursing "
         "education.", "dept"),
        ("1949", "Move to Taiwan",
         "The department moved to Taiwan with the National Defense Medical Center, to Shuiyuan in Taipei.", "dept"),
        ("1979", "Graduate Institute of Nursing",
         "The Graduate Institute of Nursing was established, a pioneer of master's-level nursing education "
         "in Taiwan.", "inst"),
        ("1990", "In-service bachelor's program",
         "Commissioned by the Ministry of Education, the department added an in-service bachelor's degree "
         "program for nurses. It stopped admitting students in 1994 and graduated 180 nurses in total.", "dept"),
        ("1999", "Neihu campus",
         "The campus moved to the National Defense Medical Center in Neihu, Taipei."),
        ("2025", "College of Nursing",
         "The College of Nursing was established to lead the advancement of higher nursing education in Taiwan.",
         "college"),
    ])

    aim = tape_surface(p(f'<strong style="color:{C["thread"]};{TYPE["h3"]}">{AIM}</strong>'))

    curriculum = "".join([
        p("The whole curriculum is designed around five concepts: Person, Life span, Family, Nursing process "
          "and Dynamics."),
        actions(text_link("See the curriculum", L("en_dept:C-1"))),
    ])

    goals = "".join([
        p("Bachelor's program educational goals (revised 10 February 2025). Graduates will be able to:"),
        bullets(GOALS),
    ])

    abilities = "".join([
        p(draft("Every course is mapped to the core competencies it develops.")),
        bullets(ABILITIES),
        actions(text_link("Student Learning Outcomes in practice", L("en_dept:C-4"))),
    ])

    return page(
        opening,
        note("本頁歷史、宗旨、目標、核心能力與課程概念皆譯自現行中文網站原文（見檔頭來源）。1990 年一筆「民國83年起停招」"
             "換算為 1994；1999 年一筆原文為「校址遷移至內湖的國防醫學中心」。請課委會確認英譯用詞，"
             "尤其是 13 項核心能力的英文名稱是否已有學院慣用譯法。"),
        name_tape("Our History"),
        history,
        name_tape("Educational Aim"),
        aim,
        curriculum,
        name_tape("Educational Goals"),
        goals,
        name_tape("Core Competencies"),
        abilities,
        actions(text_link("中文版：教育目標與核心能力", L("dept:C-2-2")),
                text_link("中文版：學系特色與定位", L("dept:C-2-1"))),
        owner=META["owner"],
    )
