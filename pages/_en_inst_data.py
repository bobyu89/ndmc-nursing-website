"""Shared facts for the Graduate Institute of Nursing English site (en_inst_* pages).

Underscore-prefixed, so build.py does not render it as a page. Every value is copied from a verified source
(all fetched 2026-09-29):
  contact            — pages/K_contact.py (verbatim from the current 聯絡我們 page, unit/100010/2199);
                       institute extension 18165 from pages/F_admissions.py (brochure / 招生專區)
  faculty names, positions, specialties, English project titles
                     — official English faculty list  https://wwwndmc.ndmutsgh.edu.tw/Doclisten/191/100010/3351
                       and each DocDetEn profile (IDs below); ranks cross-checked with pages/E-1_faculty.py
  lab websites       — pages/E-1_faculty.py / pages/E-2_research.py (from the Chinese profile pages)
  history            — 歷史沿革 unit/100181/6527 (same text as pages/C-3_history.py) and the old English page
                       uniten/100010/3353 ("In 1979, we established the first graduate nursing program in Taiwan.")
  master's structure — 研究所「學生專區」 unit/100181/6533
"""

from components import text_link, draft
from links import L
from tokens import SITE

EMAIL = "ndmu_con@mail.ndmutsgh.edu.tw"
MAILTO = f"mailto:{EMAIL}"
TEL = "tel:+886287923100"
MAP = "https://maps.app.goo.gl/MpA4rsvwnFxdnaM37"
ADDRESS = ("College of Nursing<br>National Defense Medical University<br>"
           "No.161, Sec. 6, Minquan E. Rd., Neihu Dist., Taipei City 11490, Taiwan (R.O.C.)")
PHONE = "+886-2-8792-3100 ext. 88916, 18167, 18767, 18165"
INST_PHONE = "+886-2-8792-3100 ext. 18165"
FAX = "+886-2-66005702"

FACULTY_EN = SITE + "/Doclisten/191/100010/3351"
PROFILE = SITE + "/DocDetEn/191/100010/3351/"
U_HISTORY = SITE + "/unit/100181/6527"
U_RULES = SITE + "/unit/100181/6533"
U_ETHICS = SITE + "/unit/100181/6794"
U_INST_HOME = SITE + "/unit/100181/6511"
FACEBOOK = "https://www.facebook.com/profile.php?id=100063652101597"

# key: (English name as on the official English list, reordered given-name first; rank; extra role or "";
#       official English specialty; DocDetEn id; lab website or None)
FACULTY = {
    "tzeng": ("Wen-Chii Tzeng", "Distinguished Professor", "Dean, College of Nursing",
              "Mental health nursing", "4416", "https://sites.google.com/view/wctzeng/home"),
    "clin": ("Chia-Huei Lin", "Professor", "Chair, Department of Nursing",
             "Medical-surgical nursing, nursing administration and management, chronic disease care, health promotion, "
             "exercise training, cardiopulmonary rehabilitation, smart healthcare and telehealth", "4444",
             "https://sites.google.com/view/linchiahuei/"),
    "pan": ("Hsueh-Hsing Pan", "Professor", "Director, Graduate Institute of Nursing",
            "Cancer nursing, palliative care, nursing education, critical care, military nursing", "4443",
            "https://sites.google.com/view/hhpndmc/home"),
    "liaw": ("Jen-Jiuan Liaw", "Distinguished Professor", "",
             "Smart holistic care for children with cancer and their parents; online mindfulness in pregnancy; "
             "behavior, pain and sleep in preterm infants; developmental supportive care; psychosocial care for "
             "critically ill patients and families; competency-based and reflective nursing education; "
             "AI-supported learning in maternal nursing", "2361",
             "https://sites.google.com/view/liaw-jen-jiuan/%E7%A0%94%E7%A9%B6%E6%88%90%E6%9E%9C"),
    "chenyj": ("Yu-Ju Chen", "Professor", "",
               "Medical-surgical nursing, critical care nursing, injury mechanisms and biobehavioral responses",
               "2359", None),
    "chiang": ("Hui-Hsun Chiang", "Professor", "",
               "Emergency nursing, disaster nursing, health promotion, traumatic brain injury, telehealth", "2366",
               "https://sites.google.com/view/hui-hsunchiangndmc/h-ted-lab"),
    "liang": ("Chun Yu Liang", "Associate Professor", "",
              "Burn care nursing, critical care nursing, care of patients in negative-pressure isolation, "
              "elderly care nursing", "2364", None),
    "wang": ("Wei Yun Wang", "Associate Professor", "Deputy Director, Department of Nursing, Tri-Service General Hospital",
             "Medical-surgical nursing, emergency nursing, symptom assessment, health management, nursing education",
             "4451", "https://sites.google.com/view/wywang"),
    "yangpl": ("Pei-Lin Yang", "Associate Professor", "",
               "Adult health, critical care, mental health, chronic illness management; sleep and circadian rhythms",
               "4513", None),
    "lan": ("Hsiang-Yun Lan", "Associate Professor", "",
            "Pediatric nursing, obstetric nursing, military and disaster nursing, oncology nursing; sleep and stress "
            "in children with cancer, preterm infants and caregivers; health of military students and "
            "healthcare professionals", "2368", "https://sites.google.com/view/hsiang-yun-lan-lab-ndmc/lab"),
    "tlin": ("Ting-Ti Lin", "Associate Professor", "",
             "Community health nursing, occupational health nursing, shift-work-related health behaviors, "
             "work stressors, ecological momentary assessment", "2369", None),
    "yangcc": ("Chia-Chen Yang", "Assistant Professor", "",
               "Medical-surgical nursing, critical care nursing, thoracic nursing, health promotion, "
               "smoking-related behaviors", "2367", None),
    "tsai": ("Yu-Lun Tsai", "Assistant Professor", "Supervisor, Department of Nursing, Tri-Service General Hospital",
             "Nursing ethics, hospice and palliative care, holistic nursing", "4466", None),
    "feng": ("Hsin-Pei Feng", "Assistant Professor", "",
             "Psychiatric nursing, qualitative and quantitative research, big data analytics", "4458", None),
    "sung": ("Chien-Mei Sung", "Assistant Professor", "",
             "Medical-surgical nursing, critical care nursing, geriatric nursing, nursing administration, "
             "cognitive training, 3D printing, nurse practitioners", "4449",
             "https://bobyu89.github.io/sung-lab-website/index.html"),
    "cxlin": ("Chen-Xi Lin", "Assistant Professor", "",
              "Women's health, obstetric nursing, medical-surgical nursing, critical care nursing", "4457", None),
    "ho": ("Yen-Chung Ho", "Assistant Professor", "",
           "Psychiatric and mental health nursing, digital psychological monitoring tools, long-term monitoring of "
           "depression, instrument development, longitudinal and trajectory analysis", "4448",
           "https://bobyu89.github.io/ycho-lab-website/index.html"),
    "chenpc": ("Peng-Ciao Chen", "Assistant Professor", "",
               "Adult medical-surgical nursing, cardiovascular care, self-care, health promotion, virtual nursing "
               "education, quantitative research, evidence-based practice", "4541", None),
    "huang": ("Wan-Ting Huang", "Assistant Professor", "",
              "Medical-surgical nursing, cardiovascular disease care, cardiac rehabilitation, chronic disease care",
              "4542", "https://sites.google.com/view/wantinghuang"),
    "liu": ("Yu-Shiu Liu", "Assistant Professor", "",
            "Pediatric critical and chronic care nursing, adult congenital heart disease, grit and positive "
            "psychology, qualitative and mixed-methods research, nurse practitioner education and practice",
            "4545", "https://sites.google.com/view/ysliutw/"),
}


# Trauma, disaster and military-health projects: English titles verbatim from the DocDetEn profiles,
# except Wang's, which appears only on the Chinese profile (E-2_research.py) and is translated here.
# Whether each project is still running is not stated on the profiles.
TRAUMA_PROJECTS = [
    ("pan", "Construction and validation on disaster resilience, mental adjustment, and quality of life among "
            "military hospital nurses"),
    ("chiang", "Effectiveness of mass casualty management education intervention in military medical school "
               "students (MND-MAB-D-113120, 2024)"),
    ("lan", "Effects of Technology-Assisted Disaster Military Medical Education on Resilience, Professional "
            "Identity and Disaster Preparedness of Military College Students"),
]
TRAUMA_PROJECT_TRANSLATED = ("wang", "Effects of combat casualty care simulation training based on Kolb's "
                                     "experiential learning theory on nurses' learning outcomes (Ministry of National "
                                     "Defense)")
MILITARY_HEALTH_PROJECTS = [
    ("tlin", "Promoting sleep and health resilience for military personnel exposed to noise (2025–2026)"),
    ("tlin", "The impact of light exposure on sleep and mental health among military personnel (2026–2027)"),
    ("chiang", "Developing a Machine Learning-Based Predictive Model for the Sleep Quality of Volunteer Military "
               "Personnel (MND-MAB-D-114150, 2025)"),
    ("tzeng", "The impact of nurses' digital health literacy on quality of nursing care in military hospitals "
              "(MND-MAB-D-115159)"),
]


def project_items(projects):
    return [f"{title} — {name(key)}" for key, title in projects]


def name(key):
    return FACULTY[key][0]


def position(key):
    n, rank, role, *_ = FACULTY[key]
    if key == "feng":  # Chinese faculty list says 副教授; both profile pages say Assistant Professor
        rank = draft(rank)
    return f"{rank}; {role}" if role else rank


def profile(key):
    return PROFILE + FACULTY[key][4]


def person_row(key):
    """(title, desc, href) for route_list: every person links to the College English Faculty Directory."""
    n, rank, role, spec, _id, _lab = FACULTY[key]
    return (n, f"{position(key)}. {spec}", L("en:D-1"))


def zh(pid, label="中文"):
    """Link to the Chinese counterpart page."""
    return text_link(label, L(pid))


def email_link():
    return text_link(EMAIL, MAILTO)
