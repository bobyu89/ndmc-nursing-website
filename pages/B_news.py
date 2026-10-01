from components import (page, name_tape, statement, p, text_link, actions, photo, split, route_list,
                        draft, note)
from links import L

META = {"id": "B", "slug": "news", "title": "最新消息", "owner": "院窗口"}

FACEBOOK = "https://www.facebook.com/profile.php?id=100063652101597"  # 國防護理Facebook, from the current left menu

# 活動照片取自現行輪播（學院 unit/100010/16、研究所 unit/100181/6511），說明照輪播標題。
IMG_PLAQUE = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/DSC_9009-%E5%85%A8%E6%99%AF.jpg"
IMG_CAMP = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/DSC_7376.jpg"
IMG_TRAUMA = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100181/slider/"
              "67455379-4742-4728-8242-D72E16011238.jpg")


def render():
    categories = route_list([
        ("院務公告", "由護理學院發布、影響全院或跨學系與研究所的行政事項", L("B-1")),
        ("學術活動", "講座、研討會與其他學術活動", L("B-2")),
        ("招生訊息", "各學制招生消息與招生時程提醒", L("B-3")),
        ("榮譽榜", "師生獲獎、研究與競賽成果", L("B-4")),
        ("徵才訊息", "教師與行政人員徵聘、研究職缺", L("B-5")),
    ])

    album = split(
        "".join([
            photo(IMG_PLAQUE, "護理學院揭牌典禮全景：師長、來賓與學生在演講廳合影", "16/9"),
            p("民國114年9月16日　護理學院揭牌典禮", muted=True),
        ]),
        "".join([
            photo(IMG_CAMP, "國防迷彩天使災難救護營學員與師長在演講廳合影", "4/3"),
            p("民國114年　國防迷彩天使災難救護營", muted=True),
            photo(IMG_TRAUMA, "戰傷災難護理指導員培訓學員穿著迷彩服，手持培訓布條合影", "4/3"),
            p("民國114年6月18–19日　戰傷災難護理培訓", muted=True),
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
        p("國內研討會、高中生參訪等活動的現場照片。"),
        note("目前三張取自現行學院與研究所網站輪播（揭牌典禮、114天使營、戰傷災難護理培訓），說明照輪播標題。"
             "之後換新照片時，每張請附活動名稱、日期與一句說明；花絮是否另設相簿頁，請院窗口決定。"),
        album,
        actions(text_link("在國防護理 Facebook 看更多活動", FACEBOOK)),
        name_tape("學系與研究所的消息"),
        p(draft("學系與研究所各自的公告，請到各單位網站查看。")),
        actions(text_link("護理學系", L("D-1")), text_link("護理研究所", L("D-2"))),
        owner=META["owner"],
    )
