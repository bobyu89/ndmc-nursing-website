from components import (page, name_tape, statement, p, text_link, actions, bullets, facts, tape_surface,
                        route_list, draft, note)
from links import L

META = {"id": "J-1", "slug": "scholarships", "title": "獎學金", "owner": "院窗口", "site": "dept"}

# 獎學金名稱、「其他」段落與附件名稱逐字取自現行「獎學金專區」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6798
# （2026-09-29 擷取；原文以「一、二、……十一、」編號，這裡改為不編號的清單）。
# 教務處獎學金專區 https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/1750 為全校獎學金公告。

SLOT = "〔待提供〕"
UNIVERSITY = "https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/1750"


def render():
    opening = "".join([
        statement(
            draft("學系、校友與學會都設有獎學金。"),
            draft("先看有哪些獎學金，再看資格與申請方式。每次開放申請，都會另外公告。"),
        ),
        actions(text_link("獎學金公告", L("dept:B-3")), text_link("全校獎學金（教務處）", UNIVERSITY)),
    ])

    items = bullets([
        "護理學系實習成績優良麥範德博士紀念獎助學金",
        "國防醫學大學護理學系周美玉將軍紀念獎學金",
        "護理學系系友聯誼會獎學金",
        "護理學系劉俊老師獎學金",
        "大學部應屆畢業生優良獎狀－「護理學系實習總成績第一名」",
        "台灣護理學會應屆畢業生護理實習成績第一名獎學金",
        "詹益欣教育長獎學金",
        "彭孟緝將軍暨夫人紀念獎學金—績優獎學金",
        "台灣護理學會助學金",
        "國防醫學大學護理學院第一屆趙理事長獎學金發放辦法",
    ])

    others = tape_surface(
        p("財團法人林國長先生獎學金、台灣護理學會會員進修獎助學金、財團法人黎明文化事業基金會獎助學金、"
          "財團法人佛教慈濟慈善事業基金會慈濟醫學獎學金等等各項獎學金，相關申請資訊將另行以電子郵件通知，符合資格之同學可自行申請。"),
    )

    eligibility = "".join([
        p(draft("每一項獎學金的資格與遴選方式，寫在「學生獎學金遴選標準」裡；趙理事長獎學金另有發放辦法與申請表。"
                "這三份文件放在本頁下方的附件下載：")),
        bullets([
            "國防醫學大學護理學院護理學系學生獎學金遴選標準",
            "國防醫學大學護理學院第一屆趙理事長獎學金發放辦法",
            "國防醫學大學護理學院校友會第一屆趙理事長獎學金申請表",
        ]),
        note("附件名稱取自現行獎學金專區節點的附件模組（遴選標準檔名標示 1141110 修訂、趙理事長辦法標示 1150722），"
             "換上新版 html 後仍會顯示在頁面下方。若希望同學不用開 PDF 就看懂，"
             "請院窗口依遴選標準整理每項獎學金的「對象、條件、名額」一句話，本頁再改成對照表；請勿自行估計金額或名額。"),
    ])

    steps = "".join([
        facts([
            ("何時開放", SLOT),
            ("在哪裡看公告", draft("學系獎學金公告，以及電子郵件通知")),
            ("要準備什麼", SLOT),
            ("交到哪裡", SLOT),
            ("何時公布結果", SLOT),
        ]),
        note("現行頁只寫到「相關申請資訊將另行以電子郵件通知」，沒有申請流程。請院窗口提供：每年開放申請的時間、"
             "要繳的文件、繳交地點或方式、承辦窗口與分機、結果公布方式。未確認前每一格保持〔待提供〕。"
             "另外：內容清單裡「獎學金公告」（dept:B-3）與本頁目前是同一個節點（100180/6798），"
             "公告模組新建後，請把 links.py 的 B-3 改成新節點。"),
    ])

    related = route_list([
        ("全校獎學金公告", draft("教務處獎學金專區：校外基金會與全校獎學金的申請公告"), UNIVERSITY),
        ("校友專區", draft("系友聯誼會與校友會設立的獎學金，來自學長姐的支持"), L("dept:K")),
        ("學生專區", draft("表單下載、重要日程與常用連結"), L("dept:J")),
    ], unit="dept")

    return page(
        opening,
        name_tape("學系獎學金"),
        items,
        name_tape("其他獎學金"),
        others,
        name_tape("資格與遴選標準"),
        eligibility,
        name_tape("申請流程"),
        steps,
        name_tape("也可以看看"),
        related,
        owner=META["owner"],
    )
