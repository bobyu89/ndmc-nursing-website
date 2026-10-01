from components import (page, name_tape, statement, p, split, photo, actions, text_link, tape_surface,
                        draft, note)
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

    message = tape_surface(
        p(draft("[Greeting] One or two sentences welcoming researchers and partner institutions.")),
        p(draft("[Who we are] What kind of place the Institute is and why nurses need research skills.")),
        p(draft("[Research] The Institute's current research priorities, and its links with Tri-Service General "
                "Hospital and military health care.")),
        p(draft("[Graduates] What kind of nurses the master's program (and doctoral program, if confirmed) "
                "aims to educate.")),
        p(draft("[Invitation] An invitation to international researchers to visit or collaborate.")),
        p(draft(f"[Signature] {name('pan')}, Director, Graduate Institute of Nursing"), muted=True),
    )

    return page(
        opening,
        name_tape("Director"),
        portrait,
        note("請院窗口提供英文版所長的話 250–400 字（可由中文版所長的話翻譯，須所長本人確認）。下方五段為結構草稿，收到原文後整段替換。"
             "官方英文個人頁：DocDetEn/191/100010/3351/4443"),
        name_tape("Director's Message"),
        message,
        actions(text_link("Overview and Educational Goals", L("en_inst:B-2")),
                text_link("Research", L("en_inst:D"))),
        owner=META["owner"],
    )
