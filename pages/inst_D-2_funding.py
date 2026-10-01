from urllib.parse import quote

from components import (page, name_tape, statement, p, h4, button, text_link, actions, facts, feature_list,
                        draft, note)
from links import L
from tokens import SITE

META = {"id": "D-2", "slug": "funding", "title": "獎助學金", "owner": "院窗口", "site": "inst"}

# 獎學金明細原文照錄自研究所「獎學金專區」（現行節點，沿用）：
U_FUND = SITE + "/unit/100181/6802"
U_ZHAO_RULES = SITE + quote("/files/web/192/file_up/100181/15425/國防醫學大學護理學院第一屆趙理事長獎學金發放辦法1150722.pdf")
U_ZHAO_FORM = SITE + quote("/files/web/192/file_up/100181/15434/國防醫學大學護理學院校友會第一屆趙理事長獎學金申請表.docx")
# 「國防部公餘進修經費補助」一詞見研究所「必修-研究倫理教育」頁：
U_ETHICS_COURSE = SITE + "/unit/100181/6800"

# (獎學金名稱, 相關網站, [(申請資格, 獎金金額)], 申請過程)
SCHOLARSHIPS = [
    ("財團法人黎明文化事業基金會獎學金", "http://www.lmcf.org.tw",
     [("研究生", "一萬元五千元及獎牌ㄧ面")], "依公文規定學生自行申請(約每年十月份申請)"),
    ("劉瑞恆先生獎學金", None,
     [("護理學研究所 碩班一名", "肆仟元")], "由護理碩士班提供得獎人選"),
    ("財團法人海華文教基金會僑生獎助學金", None,
     [("碩士班", "壹萬元及獎狀ㄧ只")], "依公文規定學生自行申請(約每年十月份申請)"),
    ("財團法人佛教慈濟慈善事業基金會獎學金", None,
     [("護理組 研究生", "参萬元")], "依公文規定學生自行申請(約每年十月份申請)"),
    ("臺灣護理學會會員進修獎學金", None,
     [("全職生", "壹萬元"), ("在職生", "壹萬元")], "依公告規定學生自行申請(約每年九月份申請)"),
    ("國防醫學大學護理學院第一屆趙理事長獎學金", None,
     [("護理學院學生", "伍仟元")], "依發放辦法學生自行申請"),
]


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def _scholarship(name, site, tiers, process):
    rows = []
    if site:
        rows.append(("相關網站", text_link(site.replace("http://", ""), site)))
    for who, amount in tiers:
        rows.append(("申請資格", who))
        rows.append(("獎金金額", amount))
    rows.append(("申請過程", process))
    return h4(name) + facts(rows)


def render():
    opening = "".join([
        statement(
            draft("讀研究所，有這些獎學金可以申請。"),
            draft("下面是研究所整理的獎學金明細：誰可以申請、金額多少、怎麼申請。"
                  "多數要自己留意公告、自行送件，申請前請再看獎學金公告。"),
        ),
        actions(button("獎學金公告", L("inst:B-4")), text_link("常見問題", L("inst:D-3"))),
    ])

    ledger = "".join([
        p("國防醫學大學護理學院護理研究所碩士班研究生獎學金明細（111年7月 學生事務委員會製）"),
        "".join(_scholarship(*s) for s in SCHOLARSHIPS),
        _source("以上摘自護理研究所〈獎學金專區〉。", U_FUND, "現行網站：研究所獎學金專區"),
        actions(text_link("趙理事長獎學金發放辦法（PDF）", U_ZHAO_RULES),
                text_link("趙理事長獎學金申請表（Word）", U_ZHAO_FORM)),
        note("明細表是 111年7月 製作，請院窗口與學生事務委員會確認每一項今年是否仍開放、金額是否更新。"
             "黎明文化事業基金會的金額原文寫「一萬元五千元」，疑為筆誤，請確認是「一萬五千元」或其他金額後再改。"
             "表內項目以外的獎助（例如研究生助學金、研究計畫兼任助理）若要列入，請提供辦法與金額來源。"),
    ])

    military = "".join([
        p(draft("軍職公餘生可以申請國防部公餘進修經費補助。研究倫理教育沒有在期限內通過，可能影響補助申請。")),
        actions(text_link("研究倫理教育修課規定", U_ETHICS_COURSE)),
        note("現行網站只在研究倫理教育頁提到「軍職公餘生申請國防部公餘進修經費補助」，沒有補助辦法。"
             "請院窗口提供：補助對象、補助項目、申請時間與承辦單位，或可公開的辦法連結。"),
    ])

    process = feature_list([
        ("留意公告", draft("基金會與學會的獎學金多在每年九、十月公告，研究所會轉發到獎學金公告。"),
         L("inst:B-4"), "inst", "看"),
        ("準備文件", draft("依各獎學金的辦法準備申請表與證明文件；表單放在表單下載。"), L("inst:G-3"), "inst", "備"),
        ("送出申請", draft("多數由學生自行申請；劉瑞恆先生獎學金由護理碩士班提供得獎人選，不必自己送件。"), None, "inst", "送"),
    ])

    return page(
        opening,
        name_tape("獎學金明細"),
        ledger,
        name_tape("軍職公餘生的進修補助"),
        military,
        name_tape("申請流程"),
        process,
        note("申請流程三步為依明細表「申請過程」欄整理的草稿，請院窗口確認研究所實際的收件與轉發方式。"),
        owner=META["owner"],
    )
