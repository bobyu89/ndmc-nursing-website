from components import (page, name_tape, statement, p, text_link, actions, photo_slot, split, route_list,
                        draft, note)
from links import L

META = {"id": "B", "slug": "news", "title": "最新消息", "owner": "院窗口"}

FACEBOOK = "https://www.facebook.com/profile.php?id=100063652101597"  # 國防護理Facebook, from the current left menu


def render():
    categories = route_list([
        ("院務公告", draft("由護理學院發布、影響全院或跨學系與研究所的行政事項"), L("B-1")),
        ("學術活動", draft("講座、研討會與其他學術活動"), L("B-2")),
        ("招生訊息", draft("各學制招生消息與招生時程提醒"), L("B-3")),
        ("榮譽榜", draft("師生獲獎、研究與競賽成果"), L("B-4")),
        ("徵才訊息", draft("教師與行政人員徵聘、研究職缺"), L("B-5")),
    ])

    album = split(
        "".join([
            photo_slot("活動花絮主照片（例：高中生參訪）", "16/9"),
            p(draft("照片說明：活動名稱、日期、一句話說明"), muted=True),
        ]),
        "".join([
            photo_slot("活動花絮（例：國內研討會）", "4/3"),
            p(draft("照片說明：活動名稱、日期"), muted=True),
            photo_slot("活動花絮（例：校內活動）", "4/3"),
            p(draft("照片說明：活動名稱、日期"), muted=True),
        ]),
        cols=(8, 4), align="start",
    )

    return page(
        statement(
            draft("學院的消息，依你要找的事分成五類。"),
            draft("公告、活動、招生、榮譽與徵才各有專區，點進去就是該類的完整列表，依日期排列。"),
        ),
        name_tape("消息分類"),
        note("本頁為靜態 HTML，無法自動帶入最新標題；各分類為 CMS 最新消息模組（B-1〜B-5 需新建）。"
             "現行「最新消息」節點 unit/100010/1628 的舊公告，需由院窗口依五類重新歸檔。"),
        categories,
        name_tape("活動花絮"),
        p(draft("國內研討會、高中生參訪等活動的現場照片。")),
        note("請院窗口提供 3 張活動照片（主照片橫式 16:9，其餘 4:3），每張附活動名稱、日期與一句說明；"
             "照片中若有可辨識的學生，請先確認已取得同意。花絮是否另設相簿頁，請一併決定。"),
        album,
        actions(text_link("在國防護理 Facebook 看更多活動", FACEBOOK)),
        name_tape("學系與研究所的消息"),
        p(draft("學系與研究所各自的公告，請到各單位網站查看。")),
        actions(text_link("護理學系", L("D-1")), text_link("護理研究所", L("D-2"))),
        owner=META["owner"],
    )
