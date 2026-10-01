from components import (page, name_tape, statement, p, text_link, actions, timeline, split, photo, facts,
                        draft, note)
from links import L
from pages._en_inst_data import zh, U_INST_HOME, IMG_FOUR_NATION, IMG_TRAUMA, IMG_AI_LECTURE

META = {"id": "D-3", "slug": "activities", "title": "Academic Activities", "owner": "教發", "site": "en_inst"}

# Event titles and dates from the photo captions on the Institute's current home page (unit/100181/6511,
# fetched 2026-09-29); the ROC-date prefix gives the date (114_0115 = 15 January 2025). Same source as
# pages/inst_F-3_events.py. Only the lecture's caption states what the event was; the "Four-Nation Conference"
# (四國會議) and "Trauma training" (戰傷災難護理培訓) captions are titles only, so their English wording is draft.
# The 國軍持續教育 caption (date only in the file name) is left out until 教發 confirms it is an academic activity.


def render():
    opening = "".join([
        statement(
            draft("Lectures, conferences and training."),
            draft("A record of academic events held by the Graduate Institute of Nursing. For upcoming events, "
                  "see News."),
        ),
        actions(text_link("News", L("en_inst:F")), zh("inst:F-3")),
    ])

    y2025 = timeline([
        ("Jan", "Lecture: Applications of AI in Clinical Nursing and Research",
         "15 January 2025.", "inst"),
        ("Mar", draft("Four-Nation Conference"),
         "19–23 March 2025. " + draft("Participating countries and program to be added."), "inst"),
        ("Jun", draft("Trauma and Disaster Nursing Training"),
         "18–19 June 2025. " + draft("Organizers, participants and content to be added."), "inst"),
    ])

    # Same carousel photos as pages/inst_F-3_events.py; alt text follows the carousel captions.
    photos = "".join([
        split(photo(IMG_FOUR_NATION, "Institute event photo, March 2025 (四國會議)",
                    "4/3", caption=draft("Four-Nation Conference, 19–23 March 2025")),
              photo(IMG_TRAUMA, "Institute training photo, June 2025 (戰傷災難護理培訓)", "4/3",
                    caption=draft("Trauma and disaster nursing training, 18–19 June 2025")),
              cols=(6, 6)),
        split(photo(IMG_AI_LECTURE, "Lecture on applications of AI in clinical nursing and research, January 2025",
                    "4/3", caption="Lecture: Applications of AI in Clinical Nursing and Research, 15 January 2025"),
              "", cols=(6, 6)),
    ])

    template = "".join([
        p(draft("Each new event is added in the same format, newest last.")),
        facts([
            ("Date", "[day month year]"),
            ("Event", "[full title]"),
            ("Type", "[lecture / conference / workshop / training / academic exchange]"),
            ("Speakers or partners", "[name, title, institution]"),
            ("Summary", "[two or three sentences: what happened and who took part]"),
        ]),
    ])

    return page(
        opening,
        name_tape("2025"),
        y2025,
        note("三筆活動只有研究所首頁輪播照片的標題與日期可查（unit/100181/6511）。演講題目為照片標題的翻譯。"
             "「四國會議」與「Trauma training 戰傷災難護理培訓」性質未確認，英文名稱為草稿。請教發或主辦老師提供每場："
             "活動正式英文名稱、主辦與合辦單位、講者或與會學校（四國會議是哪四國、在哪裡舉行）、參加對象、兩三句紀錄。"
             "下方三張照片沿用研究所首頁輪播原圖。「114國軍持續教育」（檔名 1140812）是否屬學術活動請確認後再決定是否列入。"),
        photos,
        name_tape("Adding New Records"),
        template,
        note("教發請提供 2024 年以前（如有）及 2025 年 7 月至今已辦完的學術活動；英文站只列對國際學者有意義的活動，"
             "活動預告放英文 News，辦完後再列入本頁。"),
        actions(text_link("Publications", L("en_inst:D-2")), text_link("Research Collaboration", L("en_inst:E"))),
        owner=META["owner"],
    )
