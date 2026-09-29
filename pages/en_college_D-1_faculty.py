from components import page, name_tape, statement, p, h4, text_link, actions, roster, draft, note
from links import L
from tokens import C, TYPE
from pages._en_college_shared import zh, PROFILE, FACULTY_EN

META = {"id": "D-1", "slug": "faculty", "title": "Faculty Directory", "owner": "院窗口", "site": "en_college"}

# Sources (2026-09-29):
#   Roster, grouping, rank, role, degree, specialty — pages/E-1_faculty.py (verbatim from the Chinese faculty pages).
#     Rank and specialty are translated faithfully from there; where the official English profile already words
#     a specialty the same way, its wording is reused.
#   English names and profile links — official English Faculty page https://wwwndmc.ndmutsgh.edu.tw/Doclisten/191/100010/3351
#     (updated 2026-07-28). Name order is normalised to given name + family name; spelling is kept as published.
#   Degrees — the same English profiles where given, otherwise translated from pages/E-1_faculty.py.
# Full-time faculty only (教授 to 講師). Teaching and research assistants (助教 group) are left to the Chinese page.

NDMC_PHD = "PhD (Nursing), Graduate Institute of Medical Sciences, National Defense Medical Center"

# (group, English name, Chinese name, rank, role, degree, specialty, English profile id or None)
FULLTIME = [
    ("Dean", "Wen-Chii Tzeng", "曾雯琦", "Distinguished Professor", "Dean, College of Nursing",
     "PhD, School of Nursing, University of California, San Francisco, USA",
     "Mental health nursing", "4416"),
    ("Chair and Director", "Chia-Huei Lin", "林佳慧", "Professor", "Chair, Department of Nursing",
     NDMC_PHD,
     "Medical-surgical nursing, nursing administration and management, chronic disease care, health promotion, "
     "exercise training, cardiopulmonary rehabilitation, smart healthcare", "4444"),
    ("Chair and Director", "Hsueh-Hsing Pan", "潘雪幸", "Professor", "Director, Graduate Institute of Nursing",
     NDMC_PHD,
     "Cancer nursing, palliative care, nursing education, acute and critical care nursing, military nursing", "4443"),
    ("Professors", "Jen-Jiuan Liaw", "廖珍娟", "Distinguished Professor", "",
     "PhD in Nursing, University of Washington, USA",
     "A smart holistic care platform for children with cancer and their parents; online mindfulness intervention "
     "in pregnancy; behavioral observation, pain and sleep in preterm infants; developmental supportive care for "
     "preterm infants; psychosocial support for critically ill patients and their families; stress relief for "
     "pregnant women; end-of-life family care; competency-based nursing education; reflective teaching; flipped "
     "teaching; mindfulness apps and chatbots for stress relief and better sleep; AI-supported multimodal learning "
     "for obstetric nursing and practicum", "2361"),
    ("Professors", "Yu-Ju Chen", "陳玉如", "Professor", "",
     "PhD in Nursing, University of Arizona, USA",
     "Adult nursing, critical care nursing, injury mechanisms and biobehavioral responses, biofeedback", "2359"),
    ("Professors", "Hui-Hsun Chiang", "江慧珣", "Professor", "",
     "PhD, Health Promotion and Health Education, National Taiwan Normal University",
     "Emergency nursing, disaster nursing, health promotion, traumatic brain injury, telehealth", "2366"),
    ("Associate Professors", "Chun Yu Liang", "梁鈞瑜", "Associate Professor", "",
     NDMC_PHD,
     "Burn nursing, critical care nursing, care of patients in negative-pressure isolation, gerontological nursing",
     "2364"),
    ("Associate Professors", "Wei Yun Wang", "王蔚芸", "Associate Professor",
     "Deputy Director, Department of Nursing, Tri-Service General Hospital",
     NDMC_PHD,
     "Medical-surgical nursing, emergency nursing, symptom assessment, health management, innovative nursing education",
     "4451"),
    ("Associate Professors", "Pei-Lin Yang", "楊佩陵", "Associate Professor", "",
     "PhD in Nursing, University of Washington, Seattle, USA",
     "Sleep, stress adaptation, circadian rhythms, symptom management", "4513"),
    ("Associate Professors", "Hsiang-Yun Lan", "藍湘勻", "Associate Professor", "",
     "PhD (Nursing), Graduate Institute of Medical Sciences, National Defense Medical University",
     "Pediatric nursing, obstetric nursing, military and disaster nursing, oncology nursing, sleep in children with "
     "cancer, sleep and stress in preterm infants and their caregivers, physical and mental health of military "
     "students and healthcare professionals", "2368"),
    ("Associate Professors", "Ting-Ti Lin", "林挺廸", "Associate Professor", "",
     "PhD in Nursing, University of Illinois Chicago, USA",
     "Community health nursing, occupational health nursing, health behaviors of shift workers, work stressors, "
     "ecological momentary assessment", "2369"),
    ("Associate Professors", "Hsin-Pei Feng", "馮欣蓓", draft("Associate Professor"), "",
     NDMC_PHD,
     "Psychiatric nursing, qualitative and quantitative research, big data analysis", "4458"),
    ("Assistant Professors", "Chia-Chen Yang", "楊嘉禎", "Assistant Professor", "",
     "PhD, Graduate Institute of Clinical Medical Sciences, Chang Gung University",
     "Medical-surgical nursing, critical care nursing, thoracic nursing, health promotion, smoking behavior", "2367"),
    ("Assistant Professors", None, "莊蕙婉", "Assistant Professor",
     "Nursing Supervisor, Department of Nursing, Tri-Service General Hospital",
     NDMC_PHD,
     "Health promotion, care of older adults, medical-surgical nursing, acute and critical care nursing", None),
    ("Assistant Professors", "Yu-Lun Tsai", "蔡育倫", "Assistant Professor",
     "Nursing Supervisor, Department of Nursing, Tri-Service General Hospital",
     NDMC_PHD,
     "Nursing ethics, hospice and palliative care, holistic nursing", "4466"),
    ("Assistant Professors", "Chien Mei Sung", "宋建美", "Assistant Professor", "",
     "PhD in Nursing, Taipei Medical University",
     "Medical-surgical nursing, acute and critical care nursing, geriatric nursing, nursing administration, cognitive training, "
     "3D printing, nurse practitioner practice", "4449"),
    ("Assistant Professors", "Chen-Xi Lin", "林辰禧", "Assistant Professor", "",
     "PhD in Nursing, University of California, San Francisco, USA",
     "Obstetric nursing, women's health, medical-surgical nursing, critical care nursing", "4457"),
    ("Assistant Professors", "Yen-Chung Ho", "賀彥中", "Assistant Professor", "",
     "PhD in Nursing, Taipei Medical University",
     "Psychiatric and mental health nursing, digital psychological monitoring tools, quantitative research, long-term "
     "monitoring of depression, instrument development, longitudinal data analysis, trajectory analysis", "4448"),
    ("Assistant Professors", "Peng-Ciao Chen", "陳芃橋", "Assistant Professor", "",
     "Doctor of Nursing Practice (DNP), National Yang Ming Chiao Tung University",
     "Adult medical-surgical nursing, cardiovascular care, self-care, health promotion, virtual nursing education, "
     "quantitative research, evidence translation", "4541"),
    ("Assistant Professors", "Wan-Ting Huang", "黃琬婷", "Assistant Professor", "",
     "PhD in Nursing, National Yang Ming Chiao Tung University",
     "Medical-surgical nursing, cardiovascular disease care, cardiac rehabilitation, chronic disease care", "4542"),
    ("Assistant Professors", "Yu-Shiu Liu", "劉育秀", "Assistant Professor", "",
     "PhD in Nursing, National Yang Ming Chiao Tung University",
     "Pediatric acute, critical and chronic illness care, congenital heart disease, grit, qualitative and quantitative "
     "research, nurse practitioner practice", "4545"),
    ("Lecturers", "Chiao-Hsuan Lin", "林巧軒", "Lecturer", "",
     "Master's in Nursing (Maternal and Child Nursing track), Graduate Institute of Nursing, National Defense Medical Center",
     "Maternal and child nursing, acute and critical care nursing, psychiatric nursing", "4514"),
    ("Lecturers", "Chieh-Yi Song", "宋皆儀", "Lecturer", "",
     "Master's in Nursing (Adult and Gerontological Nursing track), Graduate Institute of Nursing, National Defense Medical Center",
     "Medical-surgical nursing, critical care nursing, cardiovascular nursing", "4515"),
    ("Lecturers", "Pei-Ping Jao", "饒珮平", "Lecturer", "",
     "Master's in Nursing, Graduate Institute of Nursing, College of Nursing, National Defense Medical University",
     "Medical-surgical nursing, acute and critical care nursing", "4468"),
]

GROUPS = ["Dean", "Chair and Director", "Professors", "Associate Professors", "Assistant Professors", "Lecturers"]


def _name(en, zh_name):
    """Plain text only: roster() also uses the name as the photo slot's label attribute."""
    return f"{en}　{zh_name}" if en else zh_name


def _fields(degree, specialty, pid):
    out = f"<strong>Research interests:</strong> {specialty}"
    out += f'<span style="display:block;margin-top:2px;{TYPE["small"]}color:{C["ink_soft"]};">{degree}</span>'
    if pid:
        out += text_link("Profile, publications and email", PROFILE + pid)
    return out


def _rows(people):
    return [(_name(en, zh_name), rank, role or "College of Nursing", _fields(degree, spec, pid), None)
            for _g, en, zh_name, rank, role, degree, spec, pid in people]


def render():
    opening = "".join([
        statement(
            draft("The people who teach, and the research they lead."),
            draft("The Department of Nursing and the Graduate Institute of Nursing share one full-time faculty. "
                  "Each entry links to an official English profile with research projects, publications and contact details."),
        ),
        actions(text_link("Research Highlights", L("en:D-2")), text_link("Visiting Scholars", L("en:G-2")), zh("E-1")),
        note("英文姓名與個人頁連結取自學校英文師資頁（Doclisten/191/100010/3351，2026-07-28 更新），姓名順序統一為「名 姓」，拼法照原頁；"
             "職級、職務、專長依中文師資陣容頁翻譯。請院窗口向每位老師確認英文姓名寫法、英文專長用詞，以及是否在本頁直接列出公務信箱"
             "（目前信箱只在個人頁，部分老師個人頁用的是私人信箱）。"),
    ])

    fulltime = []
    for g in GROUPS:
        people = [x for x in FULLTIME if x[0] == g]
        fulltime.append(h4(g))
        fulltime.append(roster(_rows(people)))

    others = "".join([
        p("The College also has one joint-appointment professor and a roster of adjunct faculty who teach courses and "
          "clinical practicums; the adjunct roster is renewed every academic year."),
        p(draft("These lists are kept in Chinese on the Chinese faculty page."), muted=True),
        actions(zh("E-1", "中文師資陣容（含合聘與兼任）")),
    ])

    return page(
        opening,
        name_tape("Full-time Faculty"),
        note("莊蕙婉老師不在學校英文師資頁上，暫保留中文姓名，請院窗口提供正式英文姓名與英文個人頁。"
             "馮欣蓓老師職級：中文名單列副教授，中英文個人頁皆寫助理教授，請確認（暫依名單列副教授並標待確認）。"
             "照片可沿用各教師個人頁大頭照。"),
        *fulltime,
        name_tape("Joint and Adjunct Faculty"),
        others,
        owner=META["owner"],
    )
