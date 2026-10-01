from components import (page, name_tape, statement, p, h4, text_link, actions, photo_slot, photo, split, timeline,
                        bullets, draft, note)
from links import L

META = {"id": "I-2", "slug": "activities", "title": "學生活動", "owner": "院窗口", "site": "dept"}

# 活動名稱、月份與說明（非 draft 部分）逐字取自現行系學會頁圖片「系學會協助辦理活動」
#   https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6796（更新日期 2025-10-28）
# 照片標題取自學系首頁輪播 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6510（2026-09-29 擷取）
# 社團名稱取自學員生大隊「社團總覽」 https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100030/2947
# 全校典禮專區取自全球資訊網頁尾「相關消息」。

GRADUATION = "https://wwwndmc.ndmutsgh.edu.tw/news/191/10000/2?type=34"
ANNIVERSARY = "https://wwwndmc.ndmutsgh.edu.tw/news/191/10000/2?type=35"
CLUBS = "https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100030/2947"
# 照片：學系首頁輪播「N76_加冠典禮-傳光」「114小畢典」（皆 2026-10-01 核對 200 image/jpeg）。
IMG_LIGHT = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/"
             "LINE_ALBUM_1140317N76%E5%8A%A0%E5%86%A0_250706_68.jpg")
IMG_GRAD = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/114%E5%B0%8F%E7%95%A2%E5%85%B8.jpg"


def render():
    opening = "".join([
        statement(
            draft("一年裡，一起走過的幾個重要日子。"),
            draft("從入伍訓回來後的迎新，到大二的加冠、大四的小畢典，這些活動多半由系學會和同學一起籌辦。"),
        ),
        actions(text_link("系學會", L("dept:I-1")), text_link("境外學生來校交流", L("dept:I-3"))),
    ])

    welcome = split(
        "".join([
            h4("系上迎新"),
            p("歡迎大一的同學們成功結束入伍訓回到國醫，為了讓他們更了解彼此與各自的小家直屬們，辦理迎新以及小家活動。"),
            p(draft("照片說明：新生與直屬學長姐在迎新活動中的合照。"), muted=True),
        ]),
        photo_slot("系上迎新（10月）", "4/3"),
        cols=(7, 5), align="start",
    )

    capping = split(
        "".join([
            h4("加冠典禮"),
            p("為即將進入臨床實習的大二學生進行加冠典禮，祝福他們在未來的實習當中都可以順利。"),
            p("照片說明：加冠典禮上的傳光儀式。", muted=True),
        ]),
        photo(IMG_LIGHT, "加冠典禮傳光儀式：戴上護士帽的學生在舞台上排列站立", "4/3"),
        cols=(7, 5), reverse=True, align="start",
    )

    graduation = split(
        "".join([
            h4("小畢典與畢業典禮"),
            p("為即將畢業的大四與研究生學長姐們進行小畢典的活動，祝福他們未來鵬程萬里。"),
            p(draft("全校的學位證書頒授暨正冠典禮，照片與消息放在學校的典禮專區。")),
            p("照片說明：114 年小畢典，畢業生穿著學位服在校園合影。", muted=True),
            actions(text_link("學位證書頒授暨正冠典禮專區", GRADUATION)),
        ]),
        photo(IMG_GRAD, "114 年小畢典：穿著學位服的畢業生與師長在校舍前合影", "4/3"),
        cols=(7, 5), align="start",
    )

    ceremonies_note = note("加冠與小畢典照片沿用學系首頁輪播的「N76_加冠典禮-傳光」「114小畢典」。"
                           "迎新目前沒有找到照片，請系學會提供，並確認照片中的學生同意公開；迎新照片說明為暫擬，請依實際照片改寫。")

    year = timeline([
        ("1月", "大護盃", "與其他學校的護理系一同在球場上競技，展現我們優秀的體育才能。", "dept"),
        ("1月", "年初系大會", "大一到大四的同學們一同參與，讓大家了解系上的大小事，同時會舉辦講座，讓大家吸取不一樣的知識。", "dept"),
        ("4月", "在校生關懷座談會", "系主任會與各期班導師及同學進行座談，了解大家目前不論在課業上還是在生活上的狀況，"
                                   "如果有問題也可以即時地提出、反應，老師們都會協助處理。", "dept"),
        ("6月", "新生座談會", "正在進行調適周的入伍生進行座談會，讓入伍生們能夠更了解未來的生活，以及入伍訓的狀況。", "dept"),
        ("8月", "國防迷彩天使災難救護營", "辦理迷彩天使災難救護營給高中生們，讓他們了解軍護的角色以及更加了解我們國防醫學大學。"
                                        f'<br>{text_link("迷彩天使營介紹", L("dept:E"))}', "dept"),
        ("9月", "年中系大會", "大一到大四的同學們一同參與，讓大家了解系上的大小事，同時會舉辦講座，讓大家吸取不一樣的知識。", "dept"),
        ("10月", "學長姐Q&amp;A", "針對一到四年級各自有的問題可以在這裡提出反應，有問題的話，也可以向學長姐們請教。", "dept"),
        ("11月", "校慶", "校慶合併軍醫大會，期間會有許多講座以及優秀的前輩們回來分享，還會有懇親、運動會、園遊會擺攤及社團表演活動。"
                        f'<br>{text_link("校慶暨軍醫大會專區", ANNIVERSARY)}', "dept"),
        ("11月", "在職座談會", "邀請在臨床、特殊單位、現在在其他各界服務的學長姐回來分享他們各自的心路歷程、正在做的事，以及對學弟妹們的忠告。", "dept"),
        ("考試前", "期中期末夜點", "鼓勵大家認真讀書，在營養方面支持大家的精神，補足肚子後更有力氣迎接接下來的考試。", "dept"),
    ])

    year_notes = "".join([
        p(draft("2 月的西北大學接待、11 月的八王子接待，請看境外學生來校交流。")),
        actions(text_link("境外學生來校交流", L("dept:I-3"))),
        note("月份與說明取自系學會圖片（原圖「期中期末夜點」月份標示不清，這裡暫標「考試前」），實際日期每年不同；確切日期請看「重要日程」頁。"
             "系學會圖片中每項活動都有一張照片，若要在時間軸旁放照片，請系學會提供原始照片檔。"),
    ])

    clubs = "".join([
        p(draft("課餘時間，同學可以參加全校社團。學員生大隊的社團總覽依類型列出各社團：")),
        bullets([
            "服務性社團：心輔社、大山醫療服務社、崇德青年志工社、口腔衛生服務社",
            "學術性社團：傳統醫學社、曉鐘生命哲學社、國術社、圍棋社、健康與福祉永續發展社、桌遊社",
            "藝術性社團：美術社、攝影社",
            "體育性社團：排球社、籃球社、足球社、網球社、羽球社、棒球社等",
            "康樂性社團：管樂社、鳳鳴國樂社、熱音社、源遠合唱團、戲劇社等",
        ]),
        actions(text_link("全校社團總覽", CLUBS)),
        note("社團名稱取自學員生大隊「社團總覽」（2026-09-29 擷取），會隨學年變動，連結頁為準。"
             "大綱提到的「社群」（例如系上的讀書會、學習社群）目前找不到資料；若有，請院窗口提供名稱、做什麼、怎麼加入與照片，"
             "本頁再加一段；若沒有，保留社團即可。"),
    ])

    return page(
        opening,
        name_tape("迎新、加冠、畢業"),
        welcome,
        capping,
        graduation,
        ceremonies_note,
        name_tape("一年的活動"),
        year,
        year_notes,
        name_tape("社團"),
        clubs,
        owner=META["owner"],
    )
