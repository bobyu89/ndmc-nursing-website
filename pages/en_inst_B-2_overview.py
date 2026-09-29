from components import (page, name_tape, statement, p, h4, text_link, actions, timeline, feature_list, bullets,
                        tape_surface, draft, note)
from links import L
from pages._en_inst_data import U_HISTORY, U_RULES, zh

META = {"id": "B-2", "slug": "overview", "title": "Overview and Educational Goals", "owner": "院窗口",
        "site": "en_inst"}

# Timeline translated from 歷史沿革 unit/100181/6527 (same events as pages/C-3_history.py and
# pages/inst_C-2_overview.py); years are ROC year + 1911. Master's tracks from 學生專區 unit/100181/6533.
# Mission sentence: the old college English page uniten/100010/3353 (undated; kept as draft).
U_OLD_EN = "https://wwwndmc.ndmutsgh.edu.tw/uniten/100010/3353"


def render():
    opening = "".join([
        statement(
            draft("Graduate nursing education since 1979."),
            draft("The Institute educates experienced nurses to specialize in one field of practice and to design "
                  "and carry out research. This page gives the Institute's history, goals and programs."),
        ),
        actions(zh("inst:C-2")),
    ])

    intro = tape_surface(
        p("In 1979, the Institute was established to meet the needs of nursing education and research, "
          "and became a pioneer of master's-level nursing education in Taiwan."),
        p(draft("Our mission is to educate nurses who can care for combat casualties, to provide nursing education and "
                "clinical services, and to develop military nursing research that meets national and societal needs.")),
        p(draft("[Overview] 150–250 words on the Institute today: its place in the College of Nursing, faculty, "
                "research environment and partnership with Tri-Service General Hospital.")),
    )

    events = timeline([
        ("1943", "Senior Nursing Vocational Class, Shanghai",
         "The College traces its roots to the Senior Nursing Vocational Class founded by General Mei-Yu Chow in "
         "Jiangwan, Shanghai, in 1943: the earliest vocational training program for nurses in the country.",
         "college"),
        ("1947", "Department of Nursing founded",
         "General Chow went on to establish the Department of Nursing, the country's first institution of higher "
         "nursing education.", "dept"),
        ("1949", "Move to Taiwan",
         "The Department moved with the National Defense Medical Center to Shuiyuandi, Taipei."),
        ("1979", "Graduate Institute of Nursing founded",
         "The Institute was established to meet the needs of nursing education and research, and became a pioneer of "
         "master's-level nursing education in Taiwan.", "inst"),
        ("1999", "Move to Neihu",
         "The campus moved to the National Defense Medical Center in Neihu, Taipei."),
        ("2025", "College of Nursing established",
         "The College of Nursing was established as a pioneer in advancing higher nursing education in Taiwan.", "college"),
    ])

    goals = bullets([
        draft("[Goal 1] To educate clinical nurses with advanced practice competence."),
        draft("[Goal 2] To educate nurses who can identify clinical questions and design and conduct research."),
        draft("[Goal 3] To prepare nurses for nursing education and military nursing."),
    ])

    tracks = feature_list([
        ("Adult and Gerontological Nursing", draft("Care of adults and older people, in practice and research."),
         None, "inst", "A"),
        ("Women's and Children's Nursing", draft("Care of mothers, newborns and children, in practice and research."),
         None, "inst", "W"),
        ("Mental Health Nursing", draft("Mental health and psychological care, in practice and research."),
         None, "inst", "M"),
        ("Nurse Practitioner", draft("Advanced nurse practitioner courses and practicum."), None, "inst", "N"),
    ])

    doctoral = "".join([
        p(draft("A doctoral program in nursing is also offered by the Institute. Its focus, research directions "
                "and structure will be described here once confirmed.")),
        note("博士班狀態未確認：研究所現行網站只列碩士班；《116 學年度博、碩士班招生簡章》列有護理研究所博士班（不分組）。"
             "請院窗口確認英文站能否介紹博士班；若可以，請提供成立年份、研究方向與修業年限的英文說明。確認前本段維持草稿，"
             "若不對外介紹請刪除本段。"),
    ])

    return page(
        opening,
        name_tape("The Institute Today"),
        intro,
        note("第一句譯自研究所〈歷史沿革〉（「先驅」的說法，與學院英文站一致）；學院舊英文頁寫「the first graduate nursing program "
             "in Taiwan」，能否採用待院窗口確認（見研究所英文首頁備註）。第二句（使命，與學院英文站同一句）取自舊英文頁 uniten/100010/3353，年代不明，"
             "請院窗口確認是否仍適用於護理學院／研究所。第三段請院窗口提供英文研究所簡介 150–250 字；"
             "教師、研究生、畢業生人數若要放，請附資料來源與統計日期。"),
        name_tape("History"),
        events,
        p(draft("Translated from the Institute's history page.") + "　" + text_link("Source (Chinese)", U_HISTORY),
          muted=True),
        name_tape("Educational Goals"),
        goals,
        note("研究所教育目標目前查無正式文字（中文站 inst:C-2 也是草稿）。請院窗口依研究生手冊或評鑑資料提供正式教育目標"
             "中英文版，收到後整段替換。"),
        name_tape("Graduate Programs"),
        h4("Master's program"),
        p("The master's program has four tracks."),
        tracks,
        p(draft("Track names translated from the Institute's student page.") + "　"
          + text_link("Source (Chinese)", U_RULES), muted=True),
        note("學組英文名稱為本站翻譯，請院窗口確認正式英文名稱；各學組一句說明為草稿。"),
        h4("Doctoral program"),
        doctoral,
        actions(text_link("Graduate Programs", L("en_inst:C")), text_link("Curriculum", L("en_inst:C-1"))),
        owner=META["owner"],
    )
