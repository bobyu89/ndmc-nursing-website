import importlib

from components import (page, name_tape, statement, p, h4, text_link, actions, illo_slot, bullets,
                        feature_lead, feature_list, route_list, draft, note)
from links import L

META = {"id": "F-1", "slug": "areas", "title": "研究領域", "owner": "教發", "site": "inst"}

# 教師姓名、職級、專長與研究室連結直接取自學院師資頁 pages/E-1_faculty.py（逐字擷取自現行教師個人頁，
# https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100010/1738，2026-09-29）——一個事實一個來源，不在此重抄。
# 四項戰傷與災難護理計畫名稱逐字取自各教師個人頁（同 pages/E-2_research.py）。
# 指導教授資格與名額逐字取自《國防醫學大學護理研究所碩士研究生手冊》（114年8月11日版）
# 「指導教授指導研究生實施要點」，手冊掛在 https://wwwndmc.ndmutsgh.edu.tw/unit/100181/6533。
# 研究方向分組是依「專長學科」歸納的草稿，每位老師只列在專長文字有對應詞的方向下；
# 唯一例外：王蔚芸列入「軍陣、戰傷與災難護理」是依其個人頁所列的戰鬥傷患照護擬真訓練計畫。

_faculty = importlib.import_module("pages.E-1_faculty")
SUPERVISOR_GROUPS = ["院長", "系所主管", "教授", "副教授", "助理教授"]

# (方向, 臂章字, 說明草稿, [教師])
DIRECTIONS = [
    ("軍陣、戰傷與災難護理", "軍", "官兵與軍醫院護理人員的準備度與身心健康，以及戰傷、災難與大量傷患情境下的照護與教學。",
     ["潘雪幸", "江慧珣", "藍湘勻", "王蔚芸"]),
    ("成人、急重症與慢性病照護", "重", "內外科、重症、急診、燒傷、心血管與胸腔病人的照護，以及心臟與心肺復健。",
     ["林佳慧", "陳玉如", "梁鈞瑜", "王蔚芸", "楊嘉禎", "莊蕙婉", "宋建美", "林辰禧", "陳芃橋", "黃琬婷", "王桂芸"]),
    ("癌症、安寧與護理倫理", "安", "癌症病人與家庭的照護、安寧療護、臨終關懷與護理倫理。",
     ["潘雪幸", "蔡育倫", "藍湘勻", "廖珍娟", "王桂芸"]),
    ("婦兒與家庭照護", "兒", "孕產婦、早產兒、兒童急重症與慢性病，以及照顧者的睡眠與壓力。",
     ["廖珍娟", "藍湘勻", "林辰禧", "劉育秀"]),
    ("精神衛生、睡眠與壓力調適", "心", "精神衛生照護、憂鬱的長期監測，以及睡眠、生理節律與心理壓力調適。",
     ["曾雯琦", "馮欣蓓", "賀彥中", "楊佩陵"]),
    ("健康促進、高齡與職業衛生", "健", "社區與職場的健康促進、輪班工作者健康、吸菸行為，以及高齡者照護與認知訓練。",
     ["林挺廸", "江慧珣", "莊蕙婉", "林佳慧", "楊嘉禎", "宋建美", "梁鈞瑜", "陳芃橋"]),
    ("護理教育、數位與智慧照護", "數", "護理教育與教學創新、虛擬與人工智慧學習環境、遠距醫療、數位監測工具與大數據。",
     ["廖珍娟", "潘雪幸", "王蔚芸", "陳芃橋", "林佳慧", "賀彥中", "宋建美", "江慧珣", "馮欣蓓"]),
]


def _people(groups):
    return [x for x in _faculty.FULLTIME if x[0] in groups]


def _route_rows(people):
    return [(f"{name}　{rank}", spec, href) for _g, name, rank, _role, _deg, spec, href in people]


def render():
    opening = "".join([
        statement(
            draft("想做什麼研究，先找到對的老師。"),
            draft("這一頁依研究方向整理本所的指導教師，附上每位老師的專長與研究室。"
                  "看完再和老師約時間談，會更快找到題目。"),
        ),
        actions(text_link("研究方向", "#directions"), text_link("特色研究", "#feature"),
                text_link("指導教師", "#supervisors")),
    ])

    directions = "".join([
        p(draft("下面七個方向依老師們的專長整理。同一位老師可能出現在不同方向。")),
        feature_list([
            (draft(title), draft(desc) + "<br>相關教師：" + "、".join(names), None, "inst", mark)
            for title, mark, desc, names in DIRECTIONS
        ]),
        note("分組是依學院師資頁「專長學科」歸納的草稿，只把老師放在專長文字有對應詞的方向下"
             "（王蔚芸老師列入軍陣方向，是依個人頁所列的戰鬥傷患照護擬真訓練計畫）。"
             "教發請確認方向名稱、分組與每位老師的歸屬；是否要合併或拆分，由所長與教發決定。"),
    ])

    feature = "".join([
        feature_lead(
            "戰傷與災難護理",
            [
                p(draft("這是本所最有特色的研究：在戰場、災區與大量傷患的情境下，護理人員怎麼準備、怎麼處置，"
                        "以及怎麼教。")),
                p("教師個人頁列出的相關研究計畫：", muted=True),
                bullets([
                    "建構與驗證國軍醫院護理人員面對災難的韌性、心理調適與生活品質（潘雪幸）",
                    "軍事院校醫學院學生接受大量處置教育介入之學習成效探討（MND-MAB-D-113120, 2024）（江慧珣）",
                    "運用Kolb's體驗式學習理論進行戰鬥傷患照護擬真訓練對護理師之學習成效探討【國防部】（王蔚芸）",
                    "以科技輔助災難軍陣醫學教育對軍校大學生的韌力、專業認同與災難準備度之影響（藍湘勻）",
                ]),
            ],
            illo_slot("戰傷救護擬真訓練（CocoMaterial，重新上色）", "1/1", unit="inst"),
            unit="inst", href=L("inst:F-3"), link_label="看戰傷災難護理培訓紀錄",
        ),
        note("教發請確認四項計畫的執行狀態（個人頁未標示是否仍在執行），並說明本所是否有正式的跨研究室團隊："
             "團隊名稱、召集人、成員、主題。若有，本節改以團隊為主；目前不列任何團隊名稱。"),
    ])

    rules = bullets([
        "研究生之主論文指導教授須符合本系專任助理教授(含)以上、合聘教師及臨床教師之資格者。",
        "主論文指導教授需符合下列任一條件，始得招收及指導研究生：<br>"
        "1. 研究計畫部分：須在五年內曾執行具有審查制度之研究經費補助之研究計畫。<br>"
        "2. 研究論文部分：須在五年內有一篇以第一作者或通訊作者發表於SCI、SCCI、EI、或TSSCI之論文。",
        "每位專任主論文指導教授指導本院（含其他系所）研究生名額，每年以兩名為原則。",
        "本學院每位研究生至多有兩位共同指導教授，指導研究生人數及學分數以均分計算，且其中一位論文指導教授應為本學院專任教師。",
    ])

    supervisors = "".join([
        p(draft("先看老師的專長，再點進研究室或個人頁，看老師最近在做什麼。")),
        h4("指導教授的資格"),
        rules,
        p("摘自《碩士研究生手冊》「指導教授指導研究生實施要點」。", muted=True),
        h4("專任教師（助理教授以上）"),
        route_list(_route_rows(_people(SUPERVISOR_GROUPS)), unit="inst"),
        h4("合聘教師"),
        route_list(_route_rows(_faculty.JOINT), unit="inst"),
        note("所辦與教發請提供：本學年每位老師可收的研究生名額與招生主題（一句話），以及符合上列資格、"
             "本學年可擔任主指導的老師名單。收到後在每位老師下方加上「本學年招生主題」。"
             "名單依職級排列；講師與助教不列。臨床教師是否列入，請所長決定。"),
        actions(text_link("申請指導教授的表單", L("inst:G-3")), text_link("師資陣容（完整學經歷與著作）", L("E-1"))),
    ])

    return page(
        opening,
        '<div id="directions"></div>',
        name_tape("研究方向"),
        directions,
        '<div id="feature"></div>',
        name_tape("特色研究"),
        feature,
        '<div id="supervisors"></div>',
        name_tape("指導教師與招生方向"),
        supervisors,
        name_tape("相關頁面"),
        actions(text_link("研究發表", L("inst:F-2")), text_link("學術活動", L("inst:F-3")),
                text_link("研究倫理", L("inst:G-2"))),
        owner=META["owner"],
    )
