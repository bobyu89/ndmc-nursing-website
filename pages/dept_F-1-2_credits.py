from components import (page, name_tape, statement, p, h4, text_link, actions, facts, tape_surface, draft, note, todo)
from links import L
from tokens import C, S, TYPE, SITE

META = {"id": "F-1-2", "slug": "credits", "title": "學分表", "owner": "課委會", "site": "dept"}

# 原文來源（2026-09-29 擷取），plain 文字與數字逐字照錄，不自行計算：
#   學生專區〈修業規定(依各年班教育計畫為主)〉 https://wwwndmc.ndmutsgh.edu.tw/unit/100180/6681（更新日期 2026-09-24）
#   《國防醫學大學護理學院護理學系學生手冊（學士班）》民國115年8月：
#     圖一「大學部護理學系修業圖(適用N76)」、圖二「大學部護理學系修業圖(適用N77及之後年班)」（第12–13頁）
#     第二章 壹拾〈學生學習歷程檔案管理須知〉三、(三)2. 英文語文能力（第16頁）
U_STUDENT = SITE + "/unit/100180/6681"
U_HANDBOOK = SITE + "/files/web/192/file_up/100180/14297/國防醫學大學護理學系115學生手冊-20260820.pdf"
U_RULES = (SITE + "/files/web/192/file_up/100002/6876/"
           "國防醫學大學學生研究生每學期修習最低學分數、成績核算方式、成績繳交及學位考試規定.pdf")

COHORTS = ["N76", "N77 及之後年班"]

# (項目, N76, N77及之後, 是否為子項)。數字照抄學生手冊圖一、圖二。
ROWS = [
    ("畢業學分", "共136學分", "共132學分", False),
    ("專業必修", "97學分", "93學分", False),
    ("基礎醫學科目", "26學分 (27%)", "25學分 (27%)", True),
    ("護理專業科目", "71學分 (73%)", "68學分 (73%)", True),
    ("專業選修", "3學分", "3學分", False),
    ("通識必修", "30學分", "30學分", False),
    ("政治教育科目", "12學分 (40%)", "12學分 (40%)", True),
    ("共同領域科目", "18學分 (60%)", "18學分 (60%)", True),
    ("通識選修", "6學分", "6學分", False),
]


def cohort_table(cohorts, rows):
    """Built inline (facts() has only label/value): one stitched ledger with a column per cohort,
    so a student reads across to their own 期班. Three short columns fit a phone."""
    cell = f'padding:{S[1]} {S[1]} {S[1]} 0;border-top:1.5px dashed {C["rule"]};vertical-align:top;'
    head = "".join(
        f'<th scope="col" style="{cell}text-align:left;color:{C["thread"]};font-weight:900;">{c}</th>' for c in cohorts
    )
    trs = []
    for label, *vals, sub in rows:
        lab_style = (f'padding-left:{S[2]};font-weight:600;color:{C["ink_soft"]};' if sub
                     else f'font-weight:800;color:{C["thread"]};')
        tds = "".join(f'<td style="{cell}{"color:" + C["ink_soft"] + ";" if sub else ""}">{v}</td>' for v in vals)
        trs.append(f'<tr><th scope="row" style="{cell}{lab_style}text-align:left;">{label}</th>{tds}</tr>')
    return (
        f'<table style="width:100%;max-width:44em;border-collapse:collapse;margin:0 0 {S[3]};{TYPE["body"]}">'
        f'<thead><tr><th scope="col" style="{cell}text-align:left;color:{C["ink_soft"]};{TYPE["small"]}">期班</th>{head}</tr></thead>'
        f'<tbody>{"".join(trs)}</tbody></table>'
    )


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)


def _cohorts():
    """One row per cohort's education plan; rows still waiting hold a todo() and drop out of the final build."""
    rows = [(c, todo("本期班教育計畫（逐學期科目與學分，課委會提供）")) for c in ("N76", "N77", "N78", "N79")]
    known = [(k, v) for k, v in rows if v]
    return facts(known) if known else ""


def render():
    opening = statement(
        draft("要修多少學分，看你是哪一期入學。"),
        draft("畢業門檻依各期班的教育計畫而定。先找到自己的期班，再往下看必修、選修各要幾學分。"),
    )

    rule = "".join([
        tape_surface(
            p("依據教育部及國防部規定，本學系學士班教育學程為四年（內含軍事訓練課程），"
              "113學年以前最低畢業學分數為136學分，其中包括通識必修科目30學分、通識選修科目6學分(須跨選四大領域中至少三大領域)、"
              "專業必修科目97學分、以及專業選修科目3學分(見圖一)。"),
            p("113學年以後最低畢業學分數為132學分，其中包括通識必修科目30學分、通識選修科目6學分(須跨選四大領域中至少三大領域)、"
              "專業必修科目93學分、以及專業選修科目3學分(見圖二)。"),
        ),
        _source("摘自學生專區〈修業規定(依各年班教育計畫為主)〉。", U_STUDENT, "學生專區"),
    ])

    table = "".join([
        cohort_table(COHORTS, ROWS),
        facts([
            ("通識選修", "至少選三領域：醫學人文領域、文哲與藝術領域、外國語文領域、社政與心理領域"),
        ]),
        _source("摘自《護理學系學生手冊》（115年8月）圖一「大學部護理學系修業圖(適用N76)」、"
                "圖二「大學部護理學系修業圖(適用N77及之後年班)」。", U_HANDBOOK, "學生手冊（PDF）"),
        note("學生專區的說法是「113學年以前／以後」，學生手冊的說法是「適用N76／適用N77及之後年班」，兩處都指圖一、圖二。"
             "請課委會確認兩種說法一致後，決定網頁上統一用哪一種。"),
    ])

    english = "".join([
        p("此外，學生於二年級上學期結束前若無法通過全民英檢中高級初試或以上，必須選修「進階英語」（0學分）課程，"
          "並且該科成績及格後始得畢業。"),
        _source("摘自學生專區〈修業規定〉。", U_STUDENT, "學生專區"),
        facts([
            (draft("學習歷程採計的英文成績"),
             "全民英檢中高級初試或以上，或其他國際英文檢定標準(紙筆托福543分、網路托福72分、國際英語測試(IELTS)5.5分、"
             "TOEIC 785分、外語能力(FLPT)195分、或ALCPT 80分)、其他英文能力測驗需經通識中心英文老師認可，"
             "或選修「進階英文」課程及格證明。"),
        ]),
        _source("摘自《護理學系學生手冊》〈學生學習歷程檔案管理須知〉。", U_HANDBOOK, "學生手冊（PDF）"),
        note("這份檢定清單出自學習歷程檔案須知，不是修業規定本身。請課委會確認它是否就是英文畢業門檻的認定標準；"
             "若不是，請提供正式的門檻標準，並刪掉這一列。"),
    ])

    plans = "".join([
        h4(draft("各期班教育計畫")),
        p(draft("每一期入學的學生，都有一份自己的教育計畫，列出四年每學期要修的科目與學分。"
                "選課時請以自己期班的教育計畫為準。")),
        _cohorts(),
        note("課委會請提供：N76、N77、N78、N79 各期班的教育計畫（逐學期科目與學分表，PDF 或表格皆可）。"
             "內容清單註明「記得分期班呈現」，所以每一期班各放一份；拿到後可改成每列一個連結，或把學分表直接轉成網頁表格。"
             "期班依學生手冊（115年8月）導師名單列出的七十六期至七十九期；新期班入學時請加一列。"
             "目前網站上找不到逐科學分表，本頁不自行填寫任何科目學分。"),
    ])

    return page(
        opening,
        name_tape("修業規定"),
        rule,
        name_tape("各期班畢業學分"),
        table,
        name_tape("英文畢業門檻"),
        english,
        name_tape("教育計畫"),
        plans,
        actions(text_link("學校修業規定（最低學分數、成績核算）", U_RULES), text_link("課程地圖", L("dept:F-1-3"))),
        owner=META["owner"],
    )
