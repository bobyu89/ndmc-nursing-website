from components import (page, name_tape, statement, p, h4, text_link, actions, split, illo_slot, photo_slot,
                        feature_lead, bullets, route_list, draft, note)
from links import L

META = {"id": "E-2", "slug": "research", "title": "學術研究", "owner": "教發"}

# 本頁只做摘要與導流；完整論文清單放在護理研究所「研究成果」頁（PRODUCT.md：一個事實一個來源）。
# 「戰傷與災難護理」與「研究室」清單的計畫名稱、專長逐字取自各教師現行個人頁
# https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100010/1738（2026-09-29 擷取），未判斷是否仍在執行。


def render():
    opening = "".join([
        statement(
            draft("從戰場到病房，研究回到照護現場。"),
            draft("本院研究以軍陣護理、戰傷與災難護理為核心，也關注精神衛生、慢性病照護、睡眠與健康促進。"
                  "這一頁整理研究方向與團隊；完整論文清單請到研究所網站。"),
        ),
        actions(text_link("護理研究所網站", L("D-2")), text_link("師資陣容", L("E-1"))),
    ])

    features = "".join([
        h4(draft("軍陣護理與國軍健康")),
        p(draft("官兵與軍醫院護理人員的身心健康、睡眠與壓力。")),
        h4(draft("戰傷與災難護理")),
        p(draft("戰傷救護、大量傷患處置與災難準備度的教學與研究。")),
        h4(draft("精神衛生與慢性病照護")),
        p(draft("精神病人、心血管疾病與癌症病人的照護與自我管理。")),
        h4(draft("護理教育與數位科技")),
        p(draft("擬真與虛擬實境教學、數位健康素養與人工智慧在護理學習上的應用。")),
        note("教發請提供：本院研究特色 3–4 項的定稿文字（每項 2–3 句），以及是否要附代表圖片。"),
    ])

    trauma = feature_lead(
        "戰傷與災難護理",
        [
            p(draft("這是本院與其他護理學院最不同的研究領域：在戰場、災區與大量傷患的情境下，護理人員如何準備、如何處置。")),
            p("教師個人頁列出的相關研究計畫：", muted=True),
            bullets([
                "建構與驗證國軍醫院護理人員面對災難的韌性、心理調適與生活品質（潘雪幸）",
                "軍事院校醫學院學生接受大量處置教育介入之學習成效探討（MND-MAB-D-113120, 2024）（江慧珣）",
                "運用Kolb's體驗式學習理論進行戰鬥傷患照護擬真訓練對護理師之學習成效探討【國防部】（王蔚芸）",
                "以科技輔助災難軍陣醫學教育對軍校大學生的韌力、專業認同與災難準備度之影響（藍湘勻）",
            ]),
        ],
        illo_slot("戰傷救護擬真訓練（CocoMaterial，重新上色）", "1/1"),
        href=L("E-3"), link_label="模擬教學設備",
    )

    teams = "".join([
        p(draft("本院目前以教師研究室為單位進行研究。下列研究室已有自己的網站，專長文字取自教師個人頁。")),
        route_list([
            ("曾雯琦 研究室", "精神衛生護理", "https://sites.google.com/view/wctzeng/home"),
            ("林佳慧 研究室", "內外科護理、護理行政管理、慢性病護理、健康促進、運動訓練、心肺復健、智慧醫療",
             "https://sites.google.com/view/linchiahuei/"),
            ("潘雪幸 研究室", "癌症護理、安寧療護、護理教育、急重症護理、軍陣護理",
             "https://sites.google.com/view/hhpndmc/home"),
            ("江慧珣 研究室", "急診護理、災難護理、健康促進、創傷性腦損傷與遠距醫療",
             "https://sites.google.com/view/hui-hsunchiangndmc/h-ted-lab"),
            ("王蔚芸 研究室", "內外科護理、急診護理、症狀評估、健康管理、創新護理教育",
             "https://sites.google.com/view/wywang"),
            ("藍湘勻 研究室", "兒科護理、產科護理、軍陣暨災難護理、癌症護理",
             "https://sites.google.com/view/hsiang-yun-lan-lab-ndmc/lab"),
            ("宋建美 研究室", "內外科護理、急重症護理、老人護理、護理行政、認知訓練、3D列印、專科護理師",
             "https://bobyu89.github.io/sung-lab-website/index.html"),
            ("賀彥中 研究室", "精神衛生護理學、數位化心理監測工具、量性研究、憂鬱症之長期監測",
             "https://bobyu89.github.io/ycho-lab-website/index.html"),
            ("黃琬婷 研究室", "內外科護理學、心血管疾病照護、心臟復健、慢性病照護",
             "https://sites.google.com/view/wantinghuang"),
            ("劉育秀 研究室", "兒科急重症及慢性病照護、先天性心臟病、恆毅力、質量性研究、專科護理師",
             "https://sites.google.com/view/ysliutw/"),
        ]),
        note("教發請提供：是否有跨研究室的研究團隊（團隊名稱、召集人、成員、主題）；"
             "若有，改以團隊為主、研究室為輔。其他老師的研究室網址將由 Google 表單收集後補上。"),
    ])

    outcomes = split(
        "".join([
            p(draft("本院教師的期刊論文、研究計畫與專利，完整清單由護理研究所的研究成果頁維護，"
                    "本頁不重複列出。每位老師的著作也列在個人頁。")),
            actions(text_link("護理研究所網站", L("D-2")), text_link("各教師個人頁", L("E-1"))),
            note("教發請提供：全院研究成果摘要（例如近年計畫與論文的統計，須附資料來源與統計期間），"
                 "以及研究所「研究成果」頁的網址。研究所現行網站選單尚無此頁，需先建立後再把連結改過去。"),
        ]),
        photo_slot("研究成果發表或研討會現場", "4/3"),
        cols=(7, 5),
    )

    papers = "".join([
        p(draft("每年挑選數篇最能代表本院研究方向的論文，附上一句話說明它回答了什麼問題。")),
        note("教發請提供：核心代表論文 3–5 篇（作者、年份、題名、期刊、DOI 或連結），"
             "以及每篇一句白話說明；由教發與作者確認後刊出。"),
    ])

    projects = "".join([
        p(draft("各老師正在執行的研究計畫，會依計畫主題整理在這裡，方便學生找指導老師、方便合作單位找窗口。"
                "目前各老師的計畫列在個人頁。")),
        note("教發請彙整：各老師進行中研究計畫（計畫名稱、主持人、補助單位、計畫編號、執行期間）。"
             "可併入 Google 表單一起收集；只列仍在執行期間內的計畫。"),
        actions(text_link("師資陣容與個人頁", L("E-1"))),
    ])

    return page(
        opening,
        name_tape("研究特色", unit="inst"),
        features,
        name_tape("特色研究領域"),
        trauma,
        note("教發請確認上列四項計畫的執行狀態，並補充其他戰傷與災難護理相關研究、培訓活動與照片。"),
        name_tape("研究團隊", unit="inst"),
        teams,
        name_tape("全院研究成果", unit="inst"),
        outcomes,
        name_tape("核心代表論文", unit="inst"),
        papers,
        name_tape("進行中研究計畫", unit="inst"),
        projects,
        owner=META["owner"],
    )
