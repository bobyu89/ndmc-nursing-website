import re

from components import (page, name_tape, statement, p, h4, text_link, actions, bullets, tape_surface, back_to_top,
                        draft, note)
from links import L
from tokens import SITE, C, S
from pages._en_inst_data import name, zh, FACULTY_EN

META = {"id": "D-2", "slug": "publications", "title": "Publications and Graduate Research", "owner": "教發",
        "site": "en_inst"}

# Every citation below is copied as printed on the named faculty member's official profile page
# (Chinese DocDet or English DocDetEn, fetched 2026-09-29); impact-factor annotations are left out.
# Only journal articles with a volume/article number or DOI were chosen; "accepted" / "in press" items were skipped.
# Which papers to feature is an editorial draft for 教發 to confirm.
ZH = SITE + "/DocDet/191/100010/1738/"
EN = SITE + "/DocDetEn/191/100010/3351/"

Y2026 = [
    ("fajarini", "sung", ZH + "4100",
     "Fajarini, M., Sung, C. M., Lin, Y. S., Su, P. Y., Chen, R., Chang, L. F., Chiang, K. J., & Chou, K. R. (2026). "
     "Clinical effectiveness and cost-effectiveness of primary community health care nurses: A meta-analysis. "
     "International Journal of Nursing Studies, 105365."),
    ("guan", "cxlin", ZH + "1667",
     "Guan, C. Y., Chen, S. J., Lin, C. X., Hwang, G. J., Chung, P. Y., & Chiang, H. H. (2026). Tabletop "
     "simulation-based learning for mass casualty management in nursing undergraduates: A mixed-methods study. "
     "Clinical Simulation in Nursing, 115, 101957."),
    ("kuan", "pan", ZH + "1662",
     "Chiao-Chi Kuan, Jhe-Cyuan Guo, Shan-Hsiang Shen, Chiun Hsu, Chi-Ming Chu, Chi-Kang Lin, & Hsueh-Hsing Pan* "
     "(2026). A visualized nurse-led ePRO system for chemotherapy toxicity: Content design and validation. "
     "International Journal of Medical Informatics, 214. https://doi.org/10.1016/j.ijmedinf.2026.106402"),
    ("lin", "tlin", ZH + "1666",
     "Lin, T. T., Yang, C. C., Chan, P. C., Tsai, Y. L., Wang, S. H., Chen, Y. J. (2026). Psychosocial Working "
     "Environment, Submarine Deployment, and Sleep among Navy Submarine Crews: An 8-day Longitudinal Study. "
     "Journal of Medical Sciences, 46(1):8-16."),
    ("linyy", "tzeng", ZH + "1659",
     "Lin, Y. Y., Lin, T. T., Hung, Y. L., Feng, H. P., Liang, C. Y., & Tzeng, W. C.* (2026, February). "
     "Spherical video-based virtual reality for nurses' workplace violence management: A convergent mixed-methods "
     "study. Journal of Advanced Nursing. https://doi.org/10.1111/jan.70563"),
    ("liu", "liu", ZH + "4544",
     "Liu, Y. S., Lu, C. W., Chung, H. T., Wang, J. K., Shu, Y. M., & Chen, C. W. (2026). Grit in the workplace "
     "experienced by Taiwanese adults with congenital heart disease: A phenomenological study. Journal of Clinical "
     "Nursing, 35 (2), 866–878. https://doi.org/10.1111/jocn.70051"),
]

Y2025 = [
    ("ho", "ho", EN + "4448",
     "Ho YC, Fang CL, Ching YC, Chang HJ, Wang JY, Wang CC. (2025). Development and Validation of a Cross-Device "
     "Platform for Anhedonia Trend Visualization by Using Ecological Momentary Assessment and Moving Averages "
     "(Part I): Protocol for a Methodological Pilot Study. JMIR Research Protocols, 14, e84024."),
    ("hsiao", "pan", ZH + "1662",
     "Peng-Ching Hsiao, Shu-Yen Lee, Chin Lin, Chou-Ping Chiou, Kai-Jo Chiang, & Hsueh-Hsing Pan*. (2025). "
     "Self-efficacy and family support in the relationship between stress and readiness for disaster response among "
     "nurses: A mediation analysis. BMC Nursing, 25(1), 54."),
    ("huang", "huang", EN + "4542",
     "Huang, W. T., Liu, C. Y., Shih, C.C., Chen Y.S., Chou, C.L., Lee, J.T., and Chiou, A. F. (2025). Effects of a "
     "home-based multicomponent exercise programme on frailty in postcardiac surgery patients: A randomized "
     "controlled trial. European Journal of Cardiovascular Nursing, 24(4), 580–592."),
    ("lan", "lan", ZH + "1665",
     "Lan, H. Y.*, Lewis, F. M., Tsai, Y. L., Liaw, J. J., & Chang, Y. C. (2025). Exploring the mechanisms linking "
     "work environment with nurses' physical and mental health, burnout, and productivity: A structural equation "
     "modelling approach. Journal of Advanced Nursing. https://doi.org/10.1111/jan.70367"),
    ("lien", "feng", ZH + "4036",
     "Lien, Y. J., Feng, H. P., Tseng, Y. H., Chen, C. H., & Tseng, W. H. (2025). Exploring mental health literacy "
     "on twitter: A machine learning approach. Journal of Affective Disorders, 382, 296-303."),
    ("lo", "clin", ZH + "2969",
     "Lo, Y. P., Wang, M. C., Chen, Y. H., Chiang, S. L., & Lin, C. H.* (2025). Effectiveness of a post-acute-care "
     "rehabilitation program in stroke patients: A retrospective cohort study, Life, 15, 1216."),
    ("wang", "tzeng", ZH + "1659",
     "Wang, W.-Y., Wu, Y.-S., Huang, Y., & Tzeng, W.-C.* (2025, October). Early risk detection of metabolic syndrome "
     "using sex-specific machine learning models in military personnel. Frontiers in Public Health, 13, 1625461."),
    ("weng", "liaw", ZH + "1658",
     "Weng, M. H., Chou, H. C., Chang, Y. C., Liaw, J. J.,* (2025). Effects of theory-guided unsupervised exercise "
     "on depression, sleep quality, and sense of control in pregnant women: A randomized controlled trial. "
     "Worldviews on Evidence-Based Nursing, 22(1):e12759."),
]

# Papers whose first author was a master's student, as annotated (碩士生…第一作者) on Prof. Chiang's English profile.
STUDENT_LED = [
    "Ma, C. Y., Liao, S. J., Chang, Y. C., & Chiang, H. H.* (2026). Effectiveness of a theory-driven Brazilian "
    "jiu-jitsu-based medical self-defense training for nurses facing workplace violence: A multicenter "
    "quasi-experimental study. International Journal of Nursing Studies, 173, 105260.",
    "Tzeng, H. Y., Chang, C. C., Chen, S. C., Hueng, D. Y., Chu, C. M., & Chiang, H. H.* (2026). Digital Walking "
    "Exercise for Functional Capacity and Psychological Health in Mild Traumatic Brain Injury: A Randomized "
    "Controlled Trial. Archives of Physical Medicine and Rehabilitation, 107(1), 1-10.",
    "Ma, C. Y., Lan, H. Y., Li, W. P., & Chiang, H. H.* (2025). Impact of policies and salary satisfaction on "
    "quality of life during COVID-19 pandemic: a moderated mediation model. BMC Nursing, 24(1), 773.",
]


def _wrap_urls(cite):
    """Turn each DOI URL into a real link that can wrap on a phone (the citation text itself is unchanged).
    The bare <a href> is themed by build.py; the span only lets the long URL wrap. No component covers it."""
    return re.sub(r"(https?://\S+?)(?=[.,;]?(?:\s|$))",
                  r'<span style="overflow-wrap:anywhere;"><a href="\1">\1</a></span>', cite)


def _citations(rows):
    return bullets([f"{_wrap_urls(cite)}<br>{text_link('Author profile: ' + name(who), url)}"
                    for _sort, who, url, cite in rows])


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


def render():
    opening = "".join([
        statement(
            draft("What our faculty and students publish."),
            draft("A selection of recent journal articles by Institute faculty, listed by year, and work led by our "
                  "graduate students. Complete publication lists are on each faculty member's profile."),
        ),
        _jump([("Selected publications 2026", "#y2026"), ("Selected publications 2025", "#y2025"),
               ("Papers led by graduate students", "#graduate"), ("Theses", "#theses"),
               ("Posters and awards", "#posters"), ("Contact an author", "#contact")]),
        actions(text_link("Faculty Directory", L("en:D-1")), zh("inst:F-2")),
    ])

    graduate = "".join([
        p("Papers from Professor Hui-Hsun Chiang's group whose first author was a master's student:"),
        bullets([_wrap_urls(c) for c in STUDENT_LED]),
        p("As noted on Professor Chiang's faculty profile.", muted=True),
        _anchor("theses", h4(draft("Theses")),
                p(draft("Selected recent master's theses will be listed here, with the student, supervisor and year."))),
        _anchor("posters", h4(draft("Posters and awards")),
                p(draft("Conference posters and awards by graduate students will be listed here."))),
    ])

    return page(
        opening,
        note("以下論文逐字取自各教師官方個人頁（中文 DocDet 或英文 DocDetEn，2026-09-29 擷取），只選已有卷期或 DOI 的期刊論文，"
             "未收「已接受／in press」者；選哪幾篇為草稿，請教發與作者確認後定稿（建議每年 5–8 篇）。影響係數等註記不列。"
             "完整著作以學院英文 Faculty Directory 為準。"),
        _anchor("y2026", name_tape("Selected Publications 2026"), _citations(Y2026)),
        back_to_top(),
        _anchor("y2025", name_tape("Selected Publications 2025"), _citations(Y2025)),
        back_to_top(),
        _anchor("graduate", name_tape("Graduate Research"), graduate),
        note("研究生第一作者論文依江慧珣老師英文個人頁的「碩士生…（第一作者）論文成果發表」註記；請教發確認為本所研究生。"
             "其他老師若有研究生為第一作者的論文，請一併提供。另請提供：近年碩士論文代表作（年份、研究生、指導教授、英文題名）、"
             "研究生海報與得獎紀錄（須附可查證來源）。未提供前 Theses 與 Posters 兩段不列任何項目。"),
        _anchor("contact", tape_surface(
            p(draft("Looking for a specific paper or collaborator? Write to us and we will connect you with the "
                    "author.")),
            actions(text_link("Collaboration Contact", L("en_inst:E-3"))),
        )),
        owner=META["owner"],
    )
