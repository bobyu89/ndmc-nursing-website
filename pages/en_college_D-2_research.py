from components import (page, name_tape, statement, p, h4, text_link, actions, split, illo_slot, photo,
                        feature_lead, bullets, route_list, draft, note, todo)
from links import L
from pages._en_college_shared import zh, IMG_TALK

META = {"id": "D-2", "slug": "research", "title": "Research Highlights", "owner": "教發", "site": "en_college"}

# Follows pages/E-2_research.py. Plain items are faithful translations of verified text there:
#   the four trauma/disaster project titles and investigators (from each teacher's personal page);
#   lab names, specialties and lab URLs. Investigator names use the official English Faculty page spelling.
# Full publication lists stay with the Graduate Institute (one source per fact).


def render():
    opening = "".join([
        statement(
            draft("From the battlefield to the bedside, research returns to care."),
            draft("Our research centers on military nursing and trauma and disaster nursing, and extends to mental health, "
                  "chronic illness care, sleep and health promotion. This page gives the themes and the teams; "
                  "full publication lists live with the Graduate Institute."),
        ),
        actions(text_link("Faculty Directory", L("en:D-1")), text_link("Institute research", L("en_inst:D")), zh("E-2")),
    ])

    themes = "".join([
        h4(draft("Military nursing and military health")),
        p(draft("Physical and mental health, sleep and stress among service members and nurses in military hospitals.")),
        h4(draft("Trauma and disaster nursing")),
        p(draft("Teaching and research on combat casualty care, mass-casualty management and disaster preparedness.")),
        h4(draft("Mental health and chronic illness care")),
        p(draft("Care and self-management for people with mental illness, cardiovascular disease and cancer.")),
        h4(draft("Nursing education and digital technology")),
        p(draft("Simulation and virtual reality teaching, digital health literacy and artificial intelligence in nursing education.")),
        note("研究特色四項譯自中文「學術研究」頁草稿，待教發中文定稿後同步改英文。"),
    ])

    trauma = feature_lead(
        "Trauma and disaster nursing",
        [
            p(draft("This is the research field that most sets the College apart: how nurses prepare for and respond to "
                    "the battlefield, disaster areas and mass-casualty incidents.")),
            p("Related projects listed on faculty profile pages:", muted=True),
            bullets([
                "Developing and validating disaster resilience, psychological adjustment and quality of life among "
                "nurses in military hospitals (Hsueh-Hsing Pan)",
                "Learning outcomes of a mass-casualty management educational intervention for medical students at a "
                "military university (MND-MAB-D-113120, 2024) (Hui-Hsun Chiang)",
                "Effects of combat casualty care simulation training based on Kolb's experiential learning theory on "
                "nurses' learning outcomes, Ministry of National Defense (Wei Yun Wang)",
                "Effects of technology-assisted disaster and military medicine education on resilience, professional "
                "identity and disaster preparedness among military university students (Hsiang-Yun Lan)",
            ]),
        ],
        illo_slot("Combat casualty care simulation training (CocoMaterial, recolored)", "1/1"),
        href=L("en:D-3"), link_label="Simulation facilities",
    )

    labs = "".join([
        p(draft("Research is organized around faculty labs. The labs below have their own websites.")),
        route_list([
            ("Wen-Chii Tzeng Lab", "Mental health nursing", "https://sites.google.com/view/wctzeng/home"),
            ("Chia-Huei Lin Lab", "Medical-surgical nursing, nursing administration and management, chronic disease care, health "
             "promotion, exercise training, cardiopulmonary rehabilitation, smart healthcare",
             "https://sites.google.com/view/linchiahuei/"),
            ("Hsueh-Hsing Pan Lab", "Cancer nursing, palliative care, nursing education, acute and critical care "
             "nursing, military nursing", "https://sites.google.com/view/hhpndmc/home"),
            ("Hui-Hsun Chiang Lab", "Emergency nursing, disaster nursing, health promotion, traumatic brain injury, "
             "telehealth", "https://sites.google.com/view/hui-hsunchiangndmc/h-ted-lab"),
            ("Wei Yun Wang Lab", "Medical-surgical nursing, emergency nursing, symptom assessment, health management, "
             "innovative nursing education", "https://sites.google.com/view/wywang"),
            ("Hsiang-Yun Lan Lab", "Pediatric nursing, obstetric nursing, military and disaster nursing, oncology nursing",
             "https://sites.google.com/view/hsiang-yun-lan-lab-ndmc/lab"),
            ("Chien-Mei Sung Lab", "Medical-surgical nursing, acute and critical care nursing, geriatric nursing, nursing "
             "administration, cognitive training, 3D printing, nurse practitioner practice",
             "https://bobyu89.github.io/sung-lab-website/index.html"),
            ("Yen-Chung Ho Lab", "Psychiatric and mental health nursing, digital psychological monitoring tools, "
             "quantitative research, long-term monitoring of depression",
             "https://bobyu89.github.io/ycho-lab-website/index.html"),
            ("Wan-Ting Huang Lab", "Medical-surgical nursing, cardiovascular disease care, cardiac rehabilitation, "
             "chronic disease care", "https://sites.google.com/view/wantinghuang"),
            ("Yu-Shiu Liu Lab", "Pediatric acute, critical and chronic illness care, congenital heart disease, grit, "
             "qualitative and quantitative research, nurse practitioner practice", "https://sites.google.com/view/ysliutw/"),
        ]),
        note("研究室網站有的是中文版；請教發確認各研究室是否有英文頁，或是否要在連結旁註明（Chinese）。"
             "跨研究室研究團隊若成立，改以團隊為主，同中文頁。"),
    ])

    outcomes = split(
        "".join([
            todo("全院代表成果三項（論文、計畫或專利）：作者、年份、題名、期刊、DOI，各附一句白話說明它回答了什麼問題（教發提供）"),
            actions(text_link("Faculty profiles and publications", L("en:D-1")),
                    text_link("Institute publications", L("en_inst:D-2"))),
        ]),
        photo(IMG_TALK, "Speaker, faculty and students after a talk on AI in nursing practice and research", "4/3",
              caption=draft("15 January 2025: talk on AI in clinical nursing and nursing research")),
        cols=(7, 5),
    )

    return page(
        opening,
        name_tape("Research Themes", unit="inst"),
        themes,
        name_tape("A Distinctive Field"),
        trauma,
        note("四項計畫名稱譯自中文頁（教師個人頁原文），非計畫的官方英文題名；請教發向主持人取得英文題名，並確認執行狀態。"),
        name_tape("Research Labs", unit="inst"),
        labs,
        name_tape("Representative Outcomes", unit="inst"),
        outcomes,
        note("教發請提供：核心代表論文 3–5 篇（作者、年份、題名、期刊、DOI）與每篇一句英文白話說明；"
             "全院研究成果統計須附資料來源與統計期間。未提供前不列任何數字。"),
        name_tape("Collaborate With Us"),
        p(draft("Interested in joint research on any of these themes? Tell us your topic and we will connect you with "
                "the right faculty member.")),
        actions(text_link("Collaboration Contact", L("en:G-3")), text_link("Visiting Scholars", L("en:G-2"))),
        owner=META["owner"],
    )
