import html

from components import (page, name_tape, statement, p, h4, text_link, actions, bullets, facts, route_list,
                        back_to_top, draft, note, todo)
from links import L
from tokens import SITE, C, S

META = {"id": "F-2", "slug": "publications", "title": "研究發表", "owner": "教發", "site": "inst"}

# 論文條目逐字取自各教師在學院網站的個人頁（DocDet/191/100010/1738/<編號>，2026-09-29 擷取），
# 只去掉原頁的清單編號；未改動作者、標點、期刊名或「已接受／in press」等狀態字樣。
# 收錄範圍：年份為 2026 的期刊論文（不含研究計畫、研討會發表與教學社群）。
# 同一篇出現在多位老師頁面時只列一次，放在通訊作者（*）或最先列出的老師名下。
# 研究生論文查詢連結取自圖書館「學位論文」頁 https://wwwndmc.ndmutsgh.edu.tw/unit/100036/2398。
# 研究生發表要求逐字取自《碩士研究生手冊》（114年8月11日版），手冊掛在 unit/100181/6533。

DOC = SITE + "/DocDet/191/100010/1738/"

# (教師, 個人頁編號, [條目...])
PUB_2026 = [
    ("曾雯琦", "1659", [
        'Chou, Y. J., Chiang, K. J., Huang, H., Chang, H. A., Hung, Y. L., & Tzeng, W. C.* (2026). Determinants of digital health literacy among patients with serious mental illness: A cross-sectional survey. JMIR Mental Health, (accepted).',
        'Feng, H. P., Chien, L. Y., Lin, C. H., Liang, C. Y., & Tzeng, W. C.* (2026). Effects of nonpharmacological interventions on depressive symptoms in post-acute coronary syndrome: A systematic review and meta-analysis. Journal of Medical Sciences (in press).',
        "Lin, Y. Y., Lin, T. T., Hung, Y. L., Feng, H. P., Liang, C. Y., & Tzeng, W. C.* (2026, February). Spherical video-based virtual reality for nurses' workplace violence management: A convergent mixed-methods study. Journal of Advanced Nursing. https://doi.org/10.1111/jan.70563",
    ]),
    ("潘雪幸", "1662", [
        'Chiao-Chi Kuan, Jhe-Cyuan Guo, Shan-Hsiang Shen, Chiun Hsu, Chi-Ming Chu, Chi-Kang Lin, & Hsueh-Hsing Pan* (2026). A visualized nurse-led ePRO system for chemotherapy toxicity: Content design and validation. International Journal of Medical Informatics, 214. https://doi.org/10.1016/j.ijmedinf.2026.106402',
        'Shu-Yen Lee, Chung-Yi Li, Peng-Ching Hsiao, Chieh-Yi Song, Chia-Huei Lin, Kai-Jo Chiang, & Hsueh-Hsing Pan* (2026). Perceived stress and burnout among nurses in acute and critical care settings: The mediating role of self-efficacy. Nursing in Critical Care, 31(2):e70364.',
        'Wen-Chi Yang, Chung-Yi Li, Ching-Liang Ho, Ping-Ying Chang, Li-Fen Wu, & Hsueh-Hsing Pan* (2026). Effectiveness of a social media-based life review intervention on happiness in advanced cancer patients and their family caregivers: A mixed-methods study. Psycho-Oncology, 35(1), e70374.',
        'Li-Fen Wu, Yu-Wen Hung, Li-Fang Chang, & Hsueh-Hsing Pan* (2026). Determinants of do-not-resuscitate decision in terminally ill patients without cancer receiving palliative care consultation service: A retrospective study. Medicine, 105(5), e47241.',
        'Kai-Jo Chiang, Li-Fang Chang, Lin-Ju Chou, Li-Chun Huang, Yu-Ling Kao, Chin Lin, Ya-Hung Chen, Ai-Hsiu Hung, & Hsueh-Hsing Pan* (2026). Perceived stress and compassion satisfaction among nurses: A mediation model of perceived disaster preparedness. Journal of Nursing Research.',
    ]),
    ("王蔚芸", "3772", [
        '施芮珊、藍湘勻、王蔚芸、江慧珣(2026)･照顧一位創傷後腦積水併失智症患者之護理經驗·馬偕護理。(已接受)',
        '陳政廷、王蔚芸、林挺迪、潘雪幸(2026)･心流體驗之概念分析·健康科技期刊。(已接受)',
        '李雅婷、王蔚芸、江慧珣(2026)･照顧一位創傷後腦積水併失智症患者之護理經驗·馬偕護理。(已接受)',
        '謝瓊毅、潘雪幸、王蔚芸(2026)･理想照顧者概念分析·源遠護理雜誌。(已接受)',
        '胡慈修、王蔚芸、王桂芸(2026)･死亡識能概念分析·護理雜誌，73(2)，1-8。',
    ]),
    ("林挺廸", "1666", [
        'Lin, T. T., Yang, C. C., Chan, P. C., Tsai, Y. L., Wang, S. H., Chen, Y. J. (2026). Psychosocial Working Environment, Submarine Deployment, and Sleep among Navy Submarine Crews: An 8-day Longitudinal Study. Journal of Medical Sciences, 46(1):8-16.',
    ]),
    ("林辰禧", "1667", [
        'Chen, J.-L., Lin, C.-X.*, Koester, K. A., Raymond-Flesch, M., Xu, L., Thapar, A. C., & Thapar, J. C. (2026). Optimizing AI Voice for Adolescent Health: Preferences and Trustworthiness across Teens and Parent. Journal of Pediatric Health Care.',
        'Guan, C. Y., Chen, S. J., Lin, C. X., Hwang, G. J., Chung, P. Y., & Chiang, H. H. (2026). Tabletop simulation-based learning for mass casualty management in nursing undergraduates: A mixed-methods study. Clinical Simulation in Nursing, 115, 101957.',
    ]),
    ("林佳慧", "2969", [
        'Lin, C. H., Lai, C. Y., Chang, C. Y., Chao, T. C., Song, C. Y., Chang, C. C., Chang, W. Y., Huang C. Y., Jhuang, J. W., & Chiang, S. L. (2026). Factors associated with reduced anaerobic threshold during exercise and its impact on sleep quality and health-related quality of life in individuals with post-COVID sequelae. PM&R, Accepted, 5, March.',
        "Hung, C. J., Hsiao, C. T., Chang, Y. C., Ke, H. Y., Chiang, S. L., Chang, Y. W., & Lin, C. H.* (2026). A preliminary study on nurses' knowledge, competency, and self-efficacy in delivering nursing instruction for cardiac rehabilitation exercise. Yuan-Yuan Nursing, Accepted.",
    ]),
    ("宋建美", "4100", [
        'Fajarini, M., Sung, C. M., Lin, Y. S., Su, P. Y., Chen, R., Chang, L. F., Chiang, K. J., & Chou, K. R. (2026). Clinical effectiveness and cost-effectiveness of primary community health care nurses: A meta-analysis. International Journal of Nursing Studies, 105365.',
        'Arifin, H., Chen, R., Sung, C. M., Chiang, K. J., & Chou, K. R. (2026). Performance of Malnutrition Screening Tools on People With Chronic Diseases: A Bivariate Meta-Analysis. Journal of Nursing Research, 34(1), e440.',
        'Lin, C. L., Chen, R., Sung, C. M., Su, P. Y., Arifin, H., Ye, J. Y., Chang, L. F., Pien, L. C., & Chou, K. R. (2026). Comparative effectiveness of emotion-oriented therapies for behavioural and cognitive outcomes in people with dementia: a network meta-analysis. The American Journal of Geriatric Psychiatry, 34(5):701-715.',
    ]),
    ("江慧珣", "4214", [
        'Ma, C. Y., Liao, S. J., Chang, Y. C., & Chiang, H. H.* (2026). Effectiveness of a theory-driven Brazilian jiu-jitsu-based medical self-defense training for nurses facing workplace violence: A multicenter quasi-experimental study. International Journal of Nursing Studies, 173, 105260.',
        'Tzeng, H. Y., Chang, C. C., Chen, S. C., Hueng, D. Y., Chu, C. M., & Chiang, H. H.* (2026). Digital Walking Exercise for Functional Capacity and Psychological Health in Mild Traumatic Brain Injury: A Randomized Controlled Trial. Archives of Physical Medicine and Rehabilitation, 107(1), 1-10.',
    ]),
    ("陳芃橋", "4540", [
        'Chen, P. C., Yin, W. H., Chen, K-C., Fan, C-H., Tung, H. H. (2026). Electronic health record-based alerts on guideline-directed medical therapy in heart failure: A Systematic Review. Aging Medicine and Healthcare. (Accepted)',
        'Hsu, C. H., Yeh, H. F., Chen, P. C., Wu, Y. C., 及 Tung, H. H. (2026). Validation of a locomotive syndrome evaluation scale in the Chinese population by Delphi method. Aging Medicine and Healthcare, 17(2), 81-88.',
    ]),
    ("黃琬婷", "4543", [
        'Yang, W. Y., Lan, Y. H., Wang, Y. J., Huang, S. S., 及 Huang, W. T. (2026). Early Assessment of Risk Factors for Emergence Delirium in Adult Patients Undergoing General Anesthesia: A Cross-Sectional Correlational Study. Journal of PeriAnesthesia Nursing. Advance online publication.',
    ]),
    ("劉育秀", "4544", [
        'Liu, Y. S., Lu, C. W., Chung, H. T., Wang, J. K., Shu, Y. M., & Chen, C. W. (2026). Grit in the workplace experienced by Taiwanese adults with congenital heart disease: A phenomenological study. Journal of Clinical Nursing, 35(2), 866–878. https://doi.org/10.1111/jocn.70051 (SCI/SSCI; 14/193)',
    ]),
]

# 個人頁列有 2025 年論文的老師（依個人頁編號）
PUB_2025_PAGES = [
    ("陳玉如", "1656"), ("廖珍娟", "1658"), ("潘雪幸", "1662"), ("楊嘉禎", "1664"), ("藍湘勻", "1665"),
    ("林辰禧", "1667"), ("林佳慧", "2969"), ("王蔚芸", "3772"), ("馮欣蓓", "4036"), ("宋建美", "4100"),
    ("江慧珣", "4214"), ("陳芃橋", "4540"), ("黃琬婷", "4543"),
]

NDLTD = ("https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&amp;extralimit=asc=%22%E5%9C%8B%E9%98%B2"
         "%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%22&amp;extralimitunit=%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7"
         "%E5%AD%B8&amp;searchmode=basic")


def _jump(items, lead=None):
    """Compact jump index in the style of components.roster_index: [(label, href), ...]."""
    links = "".join(
        f'<a href="{href}" style="display:inline-block;min-height:44px;padding:10px 0;margin-right:{S[3]};color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;">{label}</a>'
        for label, href in items)
    head = f'<span style="margin-right:{S[2]};color:{C["ink_soft"]};">{lead}</span>' if lead else ""
    return f'<div style="margin:0 0 {S[2]};max-width:44em;line-height:1.4;">{head}{links}</div>'


def _anchor(anchor_id, *blocks):
    return f'<div id="{anchor_id}">' + "".join(blocks) + "</div>"


def _year_block(entries):
    out = []
    for n, (name, doc_id, items) in enumerate(entries, 1):
        out.append(_anchor(f"t2026-{n}",
                           h4(name),
                           bullets([html.escape(t, quote=False) for t in items]),
                           p(f'來源：<a href="{DOC}{doc_id}">{name} 老師個人頁</a>', muted=True)))
    return "".join(out)


def render():
    # 代表論文收到前只有 todo／note（正式版不輸出），本節連同標題與跳轉連結一起隱藏。
    representative = "".join([
        todo("每位指導教師一到三篇代表論文：作者（年份）．題名．期刊，卷(期)，頁碼．DOI，各附一句白話說明這篇回答了什麼問題（教發向各教師收集）"),
        note("教發請向各指導教師收集代表論文（每人一到三篇，含 DOI 或連結）與一句白話說明，由作者本人確認後刊出。"
             "未收齊前本節只在草稿顯示，不代替老師挑選；收到後以 facts([(教師姓名, 書目<br>白話說明)]) 列出。"),
    ])

    opening = "".join([
        statement(
            draft("老師們今年發表了什麼，一頁看完。"),
            draft("這裡依年份列出本所老師的期刊論文，每篇都標明出自哪位老師的個人頁。"
                  "想了解某位老師的完整著作，請到學院師資陣容。"),
        ),
        _jump(([("教師代表論文", "#representative")] if representative else [])
              + [("2026 年論文", "#y2026"), ("2025 年論文", "#y2025"), ("研究生成果", "#students"), ("完整著作", "#complete")]),
        _jump([(name, f"#t2026-{n}") for n, (name, _i, _t) in enumerate(PUB_2026, 1)], lead="2026 年依教師："),
        actions(text_link("師資陣容", L("E-1"))),
    ])

    y2026 = "".join([
        p("以下條目逐字取自各教師個人頁，含已接受、尚未刊出的論文。", muted=True),
        _year_block(PUB_2026),
        note("本節只收個人頁上年份為 2026 的期刊論文，一篇只列一次（放在通訊作者名下）。"
             "王蔚芸老師個人頁有兩篇同名論文（施芮珊等、李雅婷等，題名皆為「照顧一位創傷後腦積水併失智症患者之護理經驗」），"
             "藍湘勻老師頁面同一篇期刊名寫作「馬偈護理」，請老師確認後更正個人頁。"
             "老師更新個人頁後，教發每學期同步一次本節。"),
    ])

    y2025 = "".join([
        p(draft("2025 年的論文請看各老師個人頁；下列老師的個人頁已列出 2025 年論文。")),
        route_list([(f"{n} 老師個人頁", draft("2025 年期刊論文"), DOC + i) for n, i in PUB_2025_PAGES], unit="inst"),
        note("教發請決定 2025 年是否也像 2026 年逐篇列出（去除重複後約五十篇）。"
             "若列出，建議改為每年只列本所老師為第一或通訊作者的論文，頁面較短。"
             "更早年份的論文不在本頁列出，一律連到個人頁。"),
    ])

    students = "".join([
        p(draft("研究生在學位口試前，都要有期刊論文與學術發表。")),
        p("研究生手冊列出的碩士學位論文口試條件包括：", muted=True),
        bullets([
            "具備一篇以上已發表在ISSN學術期刊之論文（含綜論或個案報告）抽印本或投稿證明。",
            "修業期間參加學術論文發表會口頭或海報發表。",
        ]),
        route_list([
            ("國防醫學大學博碩士論文查詢系統", draft("查本校歷屆碩士論文（國家圖書館臺灣博碩士論文知識加值系統）"), NDLTD),
        ], unit="inst"),
        todo("歷年研究生成果：年份、研究生姓名、指導教師、論文或發表題名、期刊或研討會名稱（所辦與指導教師提供）"),
        note("所辦與各指導教師請提供：每年畢業研究生的期刊論文與研討會發表（研究生姓名、指導教師、題名、期刊或會議、年份），"
             "以及是否得獎。研究生姓名須取得本人同意才刊出。"),
    ])

    return page(
        opening,
        _anchor("representative", name_tape("教師代表論文"), representative) if representative else "",
        _anchor("y2026", name_tape("最新研究發表：2026 年"), y2026),
        back_to_top(),
        _anchor("y2025", name_tape("2025 年"), y2025),
        back_to_top(),
        _anchor("students", name_tape("研究生成果"), students),
        back_to_top(),
        _anchor("complete", name_tape("完整著作"),
                p(draft("每位老師的完整學經歷與著作，由學院師資陣容與老師個人頁維護。")),
                actions(text_link("師資陣容", L("E-1")), text_link("研究領域", L("inst:F-1")))),
        owner=META["owner"],
    )
