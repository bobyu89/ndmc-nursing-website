from components import (page, name_tape, statement, p, split, photo, actions, text_link, tape_surface,
                        draft, note, todo)
from links import L
from pages._en_inst_data import FACULTY, name, position, profile, zh, IMG_DIRECTOR

META = {"id": "B-1", "slug": "director", "title": "Director's Message", "owner": "院窗口", "site": "en_inst"}

# Name, position, specialty and lab link verbatim from the official English profile
# DocDetEn/191/100010/3351/4443 (Chinese: pages/inst_C-1_director.py). Portrait: same photo as the Chinese page.


def render():
    spec, lab = FACULTY["pan"][3], FACULTY["pan"][5]

    opening = "".join([
        statement(
            draft("A message from the Director."),
            draft("The Director of the Graduate Institute of Nursing on what the Institute studies, "
                  "and the nurses it hopes to educate."),
        ),
        actions(zh("inst:C-1")),
    ])

    portrait = split(
        photo(IMG_DIRECTOR, "Professor Hsueh-Hsing Pan, Director of the Graduate Institute of Nursing", "3/4"),
        "".join([
            p(name("pan")),
            p(position("pan"), muted=True),
            p(f"Specialty: {spec}"),
            actions(text_link("Research group website", lab), text_link("Profile in the Faculty Directory",
                                                                         L("en:D-1"))),
        ]),
        cols=(4, 8), align="start",
    )

    # 全文收到前只有 todo（正式版不輸出），本段連同標題一起隱藏。
    message = todo("所長的話英文版 250–400 字：問候研究者、研究所定位、研究重點、培育目標、合作邀請，文末署名（院窗口提供，須所長確認）")

    return page(
        opening,
        name_tape("Director"),
        portrait,
        note("請院窗口提供英文版所長的話 250–400 字（可由中文版所長的話翻譯，須所長本人確認）。收到原文後以 tape_surface 分段放入，文末署名 Director, Graduate Institute of Nursing。"
             "官方英文個人頁：DocDetEn/191/100010/3351/4443"),
        *([name_tape("Director's Message"), message] if message else []),
        actions(text_link("Overview and Educational Goals", L("en_inst:B-2")),
                text_link("Institute Research", L("en_inst:D"))),
        owner=META["owner"],
    )
