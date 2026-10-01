from components import (page, name_tape, statement, p, timeline, tape_surface, feature_lead, feature_list, illo_slot,
                        photo, split, text_link, actions, draft, note)
from links import L

META = {"id": "C-2-1", "slug": "identity", "title": "學系特色與定位", "owner": "院窗口", "site": "dept"}

# 原文來源（2026-09-29 擷取），以下未包 draft() 的句子皆逐字照錄：
#   歷史沿革            https://wwwndmc.ndmutsgh.edu.tw/unit/100010/6804（與學院 C-3 相同）
#   學士班課程地圖      https://wwwndmc.ndmutsgh.edu.tw/unit/100010/3642（教育宗旨、學生核心能力）
#   學士班課程架構      https://wwwndmc.ndmutsgh.edu.tw/unit/100010/1492
#   115 學年度正期班簡章 https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2009（實習醫院、入伍訓練）
#   學系首頁輪播照片「護理學院全體教師」 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6510（2026-10-01 核對 200 image/jpeg）
IMG_FACULTY = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/"
               "%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E5%85%A8%E9%AB%94%E6%95%99%E5%B8%AB.jpg")


def render():
    opening = statement(
        draft("我國第一個護理學系，也是培育軍護的學系。"),
        draft("護理學系從周美玉將軍的護理班走到今天。我們培養的護理師，在醫院能照顧病人，在部隊與災區也能執行任務。"),
    )

    # 年代與事件取自現行「歷史沿革」頁，說明文字原文照錄；圓章為民國年加 1911 換算的西元年。
    roots = timeline([
        ("1943", "上海江灣「高級護理職業班」",
         "國防醫學大學護理學院護理學系源於上海江灣之「高級護理職業班」，由 周美玉將軍於民國32年創立，"
         "招收初中畢業之學生，修業四年半，為我國最早開辦之護理人員職業教育訓練班。", "college"),
        ("1947", "設立護理學系",
         "民國36年周將軍更進而設立護理學系，成為我國首創之護理高等學府。", "dept"),
        ("1949", "遷台",
         "民國38年護理學系隨國防醫學院遷台至台北水源地。", "dept"),
        ("1990", "在職進修班",
         "民國79年本學系接受教育部委辦，增設護理人員學士學位在職進修班"
         "（註記：在職進修班自83年起已停止對外招生，畢業生共180人）。", "dept"),
        ("1999", "遷至內湖",
         "民國88年校址遷移至內湖的國防醫學中心，以優良的師資與嶄新的硬體設備，訓練優秀的護理專業人才，"
         "繼續發揮百年樹人的志業。"),
        ("2025", "成立護理學院",
         "民國114年成立護理學院，成為推動臺灣高等護理教育的先鋒。", "college"),
    ])

    position = tape_surface(
        p("培育兼具人文素養與護理專業能力，符合軍民健康照顧系統所需之專業人才。"),
        p(draft("「軍民健康照顧系統」的意思是：畢業生不只在軍中服務，也和一般醫院的護理師一樣，"
                "照顧來看病的每一個人。這是學系定位的核心。"), muted=True),
        actions(text_link("八項教育目標與十三項核心能力", L("dept:C-2-2"))),
    )

    course = feature_lead(
        "課程從「人」出發",
        [
            p("整個課程設計與安排根據人（Person）、生命歷程（Life span）、家庭（Family）、護理過程（Nursing process）"
              "及動力變化（Dynamics）等概念。"),
            p(draft("四年先讀通識與基礎醫學，再學各年齡層的照護，最後走進社區與軍陣場域，練習照顧一整個家庭與群體。")),
        ],
        illo_slot("護生在模擬病房為假人量血壓（CocoMaterial，重新上色）", "1/1", unit="dept"),
        unit="dept", href=L("dept:F-1-1"), link_label="看課程規劃",
    )

    marks = feature_list([
        ("三軍總醫院實習",
         "本校實習醫院為三軍總醫院。" + " " + draft("護生在教學醫院的病房跟著臨床教師學習照顧病人。"),
         L("dept:F-2"), "dept", "院"),
        ("軍陣護理",
         draft("軍陣護理是學系十三項核心能力之一：在部隊、野戰與災難等特殊環境中提供照護。"
               "這是本系和一般護理系最不一樣的地方。"),
         L("dept:F-2-3"), "dept", "軍"),
        ("入伍訓練與團體生活",
         draft("新生入學後先完成八週入伍訓練，四年住校、過團體生活，練的是紀律、體能與團隊合作。"),
         L("dept:D-2"), "dept", "訓"),
        ("國際視野",
         draft("國際視野也是核心能力之一。學生有機會出國交流，例如到美國華盛頓大學參訪學習。"),
         L("dept:H"), "dept", "際"),
    ])

    numbers = split(
        "".join([
            p(draft("學系的現況，用幾個數字說明：在校學生、專任教師、歷屆畢業生、護理師考照通過率。")),
            p(draft("數字依年報填入，年報上沒有的就不放。"), muted=True),
        ]),
        photo(IMG_FACULTY, "護理學院全體教師在學院招牌前合影", "4/3", caption="護理學院全體教師"),
        cols=(7, 5),
    )

    return page(
        opening,
        note("Notion 內容清單註明本頁「拿年報的來用」。下方的歷史年表、教育宗旨、課程架構句與實習醫院為現行網站原文；"
             "標「待確認」者為草稿，請院窗口依《護理學院年報》護理學系章節核對、改寫或替換。"),
        name_tape("學系的來歷"),
        roots,
        actions(text_link("完整歷史沿革與軍護傳承", L("C-3"))),
        name_tape("學系定位"),
        position,
        name_tape("學系特色"),
        course,
        marks,
        note("「入伍訓練」一項：八週出自《115 學年度軍事學校正期班甄選入學招生簡章》；"
             "「國際視野」一項：美國華盛頓大學交流出自現行學系首頁輪播照片說明，請院窗口確認可否對外寫出校名，並補上其他交流學校。"),
        name_tape("學系現況"),
        numbers,
        note("請院窗口依年報提供：在校學生人數（依年級）、專任教師人數、歷屆畢業生總數、近三年護理師國考通過率、"
             "學系重要榮譽（年份與名稱）。右側暫用學系首頁輪播的「護理學院全體教師」合照；若有學系師生合照可替換。請勿以推估數字代替。"),
        owner=META["owner"],
    )
