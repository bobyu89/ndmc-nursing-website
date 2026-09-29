from components import (page, name_tape, statement, p, text_link, actions, route_list, tape_surface, draft, note)
from links import L
from tokens import SITE

META = {"id": "F-1", "slug": "courses", "title": "課程資訊", "owner": "院窗口", "site": "dept"}

# 「選課方式」逐字取自《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月，
# 第二章 捌、四（學生專區附件，https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681，2026-09-29 擷取）。
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"


def render():
    opening = statement(
        draft("修什麼課、修幾學分，三頁看懂。"),
        draft("課程規劃講整體設計，學分表依你的期班列出畢業門檻，課程地圖把每一年的課和核心能力連起來。"),
    )

    routes = route_list([
        ("課程規劃", draft("四年課程怎麼從通識走到護理專業"), L("dept:F-1-1")),
        ("學分表", draft("各期班的畢業學分與英文門檻"), L("dept:F-1-2")),
        ("課程地圖", draft("一到四年級的課程與核心能力"), L("dept:F-1-3")),
    ], unit="dept")

    enroll = "".join([
        tape_surface(
            p("於教務處公告選課期程後，學生須依照個人入學期別之教育計畫，選擇修業年限之課程修習。"),
            p("學生與導師討論後，確認當學期修課課程科目，列印選課單，由導師審核後，"
              "於本學系規定繳交選課單期限內繳交至系辦公室助教，呈核系主任後完成初選。"),
            p("本學系各課程的第一堂課皆為課程介紹，由課程負責教師向學生說明該課程的教學目標與內容、授課方式及評核方式，"
              "並且使學生瞭解該課程於整個教育學程中的關聯性，讓學生可以調整個人修課計畫，進行課程的加退選。"),
        ),
        p(draft("摘自《護理學系學生手冊》（115年8月）〈選課方式〉。") + "　" + text_link("學生手冊（PDF）", U_HANDBOOK),
          muted=True),
    ])

    return page(
        opening,
        name_tape("課程資訊"),
        routes,
        name_tape("選課怎麼進行"),
        enroll,
        note("院窗口請轉課委會確認：每學期選課期程是否固定在某個月份；若固定，可在此補一句並連到「重要日程」。"),
        actions(text_link("課務公告", L("dept:B-1")), text_link("重要日程", L("dept:J-3"))),
        owner=META["owner"],
    )
