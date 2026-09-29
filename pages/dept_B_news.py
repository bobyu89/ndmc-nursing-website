from components import page, name_tape, statement, p, text_link, actions, route_list, split, illo_slot, draft, note
from links import L

META = {"id": "B", "slug": "news", "title": "學系公告", "owner": "院窗口", "site": "dept"}


def render():
    opening = statement(
        draft("學系的公告，依你要找的事分成四類。"),
        draft("上課、實習、獎學金、活動各有自己的公告欄。點進去就是那一類的完整列表，最新的排在最上面。"),
    )

    categories = route_list([
        ("課務公告", draft("選課、課程異動、考試與教務消息"), L("dept:B-1")),
        ("實習公告", draft("實習時程、分組分發、行前說明"), L("dept:B-2")),
        ("獎學金公告", draft("獎學金申請辦法與得獎名單"), L("dept:B-3")),
        ("活動訊息", draft("系上活動、學生活動與招生活動"), L("dept:B-4")),
    ], unit="dept")

    elsewhere = split(
        "".join([
            p(draft("跨學系的院務公告、招生消息與徵才訊息，由護理學院統一發布。")),
            p(draft("在學同學要找表單、獎學金辦法或重要日期，學生專區整理得比較完整。")),
            actions(text_link("護理學院最新消息", L("B")), text_link("學生專區", L("dept:J"))),
        ]),
        illo_slot("學生在公告欄前看實習分組（CocoMaterial，重新上色）", "4/3", unit="dept"),
        cols=(7, 5),
    )

    return page(
        opening,
        name_tape("公告分類"),
        note("本頁為靜態 HTML，無法自動帶入最新公告標題；四類皆為 CMS 最新消息模組。"
             "B-3 獎學金公告目前掛在 unit/100180/6798，與學生專區「獎學金」（J-1）共用同一節點，請院窗口決定是否拆開；"
             "B-1、B-2、B-4 需新建。學系目前的「最新消息」連到學院節點 unit/100010/1628，舊公告需由院窗口依四類重新歸檔。"),
        categories,
        name_tape("其他消息"),
        elsewhere,
        owner=META["owner"],
    )
