from components import (page, name_tape, statement, p, button, text_link, actions, facts, route_list, draft, note)
from links import L

META = {"id": "J-3", "slug": "calendar", "title": "重要日程", "owner": "院窗口", "site": "dept"}

# 學校行事曆：教務處公告「公告本校115學年度教育行事曆(已奉核定)」
#   https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/951/11594（刊登日 2026/6/9，附件為 115 學年度教育行事曆 PDF）
# 教務處公告資訊列表 https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/951（每學年的新行事曆都在這裡公告）
# 系上活動月份取自系學會頁圖片 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6796

SLOT = "〔待提供〕"
CALENDAR = "https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/951/11594"
ACADEMIC_NEWS = "https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/951"


def render():
    opening = "".join([
        statement(
            draft("這學期什麼時候選課、考試、去實習？"),
            draft("下面是本學期護理學系學生最常查的日期。完整日期以學校當學年度的教育行事曆為準。"),
        ),
        actions(button("115學年度教育行事曆", CALENDAR), text_link("教務處公告", ACADEMIC_NEWS)),
    ])

    first = facts([
        ("開學", SLOT),
        ("選課與加退選", SLOT),
        ("期中考", SLOT),
        ("期末考", SLOT),
        ("實習", SLOT),
        ("寒假", SLOT),
    ])

    second = facts([
        ("開學", SLOT),
        ("選課與加退選", SLOT),
        ("期中考", SLOT),
        ("期末考", SLOT),
        ("實習", SLOT),
        ("暑假", SLOT),
    ])

    events = "".join([
        facts([
            ("系上迎新", "10月" + draft("（往年月份）") + "　" + SLOT),
            ("加冠典禮", "3月" + draft("（往年月份）") + "　" + SLOT),
            ("系大會", "1月、9月" + draft("（往年月份）") + "　" + SLOT),
            ("小畢典", "6月" + draft("（往年月份）") + "　" + SLOT),
            ("校慶", "11月" + draft("（往年月份）") + "　" + SLOT),
        ]),
        actions(text_link("每項活動在做什麼", L("dept:I-2"))),
    ])

    how = note("本頁是靜態頁，日期不會自動更新。每學期開學前，請院窗口依教務處公告的教育行事曆，填入兩學期的"
               "開學、選課與加退選、期中考、期末考、寒暑假日期；實習日期請實習負責老師依當學期實習安排提供（各年級不同時，"
               "請分年級列出）；系上活動日期請系學會提供。活動欄的月份取自系學會活動表，只是往年慣例，填入實際日期後請刪去。"
               "新學年的行事曆公告後，請把上方按鈕的連結與文字換成新的一年。")

    related = route_list([
        ("課務公告", draft("選課、課程與考試的最新公告"), L("dept:B-1")),
        ("實習公告", draft("實習時程、分發與行前說明"), L("dept:B-2")),
        ("學生專區", draft("獎學金、表單下載與常用連結"), L("dept:J")),
    ], unit="dept")

    return page(
        opening,
        how,
        name_tape("第一學期"),
        first,
        name_tape("第二學期"),
        second,
        name_tape("系上活動"),
        events,
        name_tape("日期有變動時"),
        p(draft("臨時異動會發布在學系公告，請以公告為準。")),
        related,
        owner=META["owner"],
    )
