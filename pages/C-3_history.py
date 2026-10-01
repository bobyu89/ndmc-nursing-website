from tokens import C
from components import (page, name_tape, statement, p, split, photo, text_link, actions, timeline, tape_surface,
                        draft, note)
from links import L

META = {"id": "C-3", "slug": "history", "title": "歷史沿革與軍護傳承", "owner": "哲君"}

# 周將軍遷厝暨追思典禮紀念影片，連結取自現行「周將軍遷厝暨追思典禮」頁（unit/100010/1519）。
MEMORIAL_VIDEO = "https://www.youtube.com/watch?v=X6k9rzHZADc"

# 照片：周將軍肖像取自「周將軍紀念影片」頁（unit/100010/1474）；典禮照片取自「周將軍遷厝暨追思典禮」頁（unit/100010/1519）。
GENERAL_PHOTO = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E8%BB%8D%E8%AD%B7%E5%A4%A7%E9%A0%AD%E7%85%A71.jpg"
CEREMONY_PHOTO = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E6%8A%95%E5%BD%B1%E7%89%873.JPG"


def _roc(roc):
    """Year patch on the Chinese page: 民國 above the year, two lines that fit the 84px patch."""
    return (f'<span style="display:block;text-align:center;line-height:1.2;">'
            f'<span style="display:block;font-size:14px;font-weight:700;letter-spacing:.1em;">民國</span>{roc}年</span>')


def _t(title, roc):
    """Event title with the AD year beside it in label size."""
    return (f'{title}<span style="margin-left:10px;font-size:14px;font-weight:700;color:{C["ink_soft"]};">'
            f'{roc + 1911}</span>')


def render():
    opening = statement(
        draft("從周美玉將軍的護理班開始。"),
        "本院的歷史，從民國32年上海江灣的一個護理班算起。這一頁記下學院走過的路，以及軍護傳承的起點。",
    )

    general = split(
        photo(GENERAL_PHOTO, "周美玉將軍身著軍裝的黑白肖像", "3/4"),
        # 簡介文字依「周將軍遷厝暨追思典禮」頁（unit/100010/1519）與「歷史沿革」頁（unit/100010/6804）整理。
        "".join([
            p("周美玉將軍是我國軍護制度的創始者，有「軍護之母」之稱。"),
            p("她於民國32年創立「高級護理職業班」，民國36年設立護理學系，也是本院的起點。"
              "她曾任臺北榮民總醫院首任護理部主任、中華民國護理學會在臺復會首任理事長。"),
        ]),
        cols=(4, 8), align="start",
    )

    video = "".join([
        photo(CEREMONY_PHOTO, "周美玉將軍遷厝暨追思典禮：國軍忠靈殿內，軍官在周將軍靈位前摺疊國旗", "16/9"),
        p("民國107年3月10日，周將軍遷厝五指山國軍示範公墓國軍忠靈殿，學系師生與校友代表出席追思典禮。", muted=True),
        actions(text_link("觀看遷厝暨追思典禮紀念影片（YouTube）", MEMORIAL_VIDEO)),
    ])

    # 年代與事件取自現行「歷史沿革」頁（unit/100010/6804），說明文字原文照錄；
    # 中文頁一律用民國紀年：年份圓章為民國年，下方小字為加 1911 換算的西元年。2018 一則取自 unit/100010/1519（影片標題「1070310」）；
    # 揭牌典禮日期取自學院首頁輪播標題「1140916_護理學院揭牌典禮」。
    events = timeline([
        (_roc(32), _t("上海江灣「高級護理職業班」", 32),
         "國防醫學大學護理學院護理學系源於上海江灣之「高級護理職業班」，由 周美玉將軍於民國32年創立，"
         "招收初中畢業之學生，修業四年半，為我國最早開辦之護理人員職業教育訓練班。", "college"),
        (_roc(36), _t("設立護理學系", 36),
         "民國36年周將軍更進而設立護理學系，成為我國首創之護理高等學府。", "dept"),
        (_roc(38), _t("遷台", 38),
         "民國38年護理學系隨國防醫學院遷台至台北水源地。"),
        (_roc(68), _t("設立護理研究所", 68),
         "民國68年為因應教育與研究之需求，設立護理研究所，成為國內護理碩士教育之先驅。", "inst"),
        (_roc(79), _t("在職進修班", 79),
         "民國79年本學系接受教育部委辦，增設護理人員學士學位在職進修班"
         "（註記：在職進修班自83年起已停止對外招生，畢業生共180人）。", "dept"),
        (_roc(88), _t("遷至內湖", 88),
         "民國88年校址遷移至內湖的國防醫學中心，以優良的師資與嶄新的硬體設備，訓練優秀的護理專業人才，"
         "繼續發揮百年樹人的志業。"),
        (_roc(107), _t("周美玉將軍遷厝暨追思典禮", 107),
         "民國107年3月10日，周將軍遷厝五指山國軍示範公墓國軍忠靈殿。"),
        (_roc(114), _t("成立護理學院", 114),
         "民國114年成立護理學院，成為推動臺灣高等護理教育的先鋒。"
         "民國114年9月16日舉行護理學院揭牌典禮。", "college"),
    ])

    book = tape_surface(
        p(draft("七十週年紀念專刊的電子版，可以在線上翻閱。")),
        actions(text_link("閱讀七十週年紀念專刊（電子書）", "#待補-七十週年紀念專刊")),
    )

    return page(
        opening,
        name_tape("周美玉將軍"),
        general,
        note("肖像沿用現行「周將軍紀念影片」頁的 軍護大頭照1.jpg，請哲君確認使用授權；"
             "上方簡介依現行網站兩頁內容整理，如需改寫成 150 字內定稿請提供。"),
        name_tape("紀念影片"),
        video,
        note("上圖為追思典禮照片，連結為典禮紀念影片。請哲君提供周美玉將軍紀錄片的線上播放連結"
             "（現行「周將軍紀念影片」頁只有光碟封面圖 紀錄片1.jpg，沒有可播放的影片）。"),
        name_tape("流年史與大事記"),
        events,
        note("請哲君補齊：① 雲端「流年史＆大事記」資料中的其他年份事件；② 歷次評鑑的年份、評鑑單位與結果，"
             "依年份插入上方時間軸。現行網站找不到評鑑資料，請勿以推估的年份填入。"),
        name_tape("七十週年紀念專刊"),
        book,
        note("請哲君提供：七十週年紀念專刊電子書的網址，以及專刊的出版年份。"),
        owner=META["owner"],
    )
