from components import (page, name_tape, statement, p, text_link, actions, split, photo, route_list,
                        tape_surface, draft, note)
from links import L
from pages._en_inst_data import name, position, zh, U_HISTORY, IMG_DIRECTOR

META = {"id": "B", "slug": "about", "title": "About the Institute", "owner": "院窗口", "site": "en_inst"}

# Mirrors pages/inst_C_about.py. Founding sentence translated from 歷史沿革 unit/100181/6527;
# director from the official English profile DocDetEn/191/100010/3351/4443.


def render():
    opening = "".join([
        statement(
            draft("A pioneer of master's-level nursing education in Taiwan since 1979."),
            draft("The Graduate Institute of Nursing is part of the College of Nursing, National Defense Medical "
                  "University. This section introduces the Director, the Institute's history and its goals."),
        ),
        actions(zh("inst:C")),
    ])

    origin = tape_surface(
        p("The Institute was established in 1979 to meet the needs of nursing education and research, "
          "and became a pioneer of master's-level nursing education in Taiwan."),
        p(draft("Translated from the Institute's history page.") + "　" + text_link("Chinese page: Institute History", U_HISTORY),
          muted=True),
    )

    director = split(
        photo(IMG_DIRECTOR, "Professor Hsueh-Hsing Pan, Director of the Graduate Institute of Nursing", "3/4"),
        "".join([
            p(name("pan")),
            p(position("pan"), muted=True),
            actions(text_link("Director's Message", L("en_inst:B-1"))),
        ]),
        cols=(3, 9), align="start",
    )

    routes = route_list([
        ("Director's Message", draft("The Director on the Institute's research and graduate education"),
         L("en_inst:B-1")),
        ("Overview and Educational Goals", draft("History, educational goals and the graduate programs"),
         L("en_inst:B-2")),
        ("Graduate Programs", draft("Master's program tracks and curriculum themes"), L("en_inst:C")),
        ("Faculty Directory", draft("Full faculty profiles, kept by the College of Nursing"), L("en:D-1")),
    ], unit="inst")

    return page(
        opening,
        name_tape("Where We Began"),
        origin,
        name_tape("Director"),
        director,
        name_tape("In This Section"),
        routes,
        note("師資只由學院英文站 Faculty Directory（en:D-1）一處維護，本所英文站不另建教師名單。"),
        owner=META["owner"],
    )
