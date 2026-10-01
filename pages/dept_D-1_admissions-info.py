from components import (as_of, page, name_tape, statement, p, button, text_link, actions, facts, route_list, split,
                        illo_slot, draft, note, icon)
from links import L

META = {"id": "D-1", "slug": "admissions-info", "title": "招生資訊", "owner": "學生事務", "site": "dept"}

# 官方出處（2026-09-29 擷取）。未包 draft() 的文字逐字取自下列來源（經學院 F 頁核對）。
U_BACH = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2009"          # 學校招生專區【大學部】：歷年正期班簡章
U_BROCHURE = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100143/14540/"
              "115學年度軍校正期班甄選入學簡章.pdf")
U_SLIDES = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100143/14536/"
            "115學年國防醫學大學招生簡報.pdf")                          # 115 學年度大學部招生資訊（簡報）
U_SCHOOL = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/1861"          # 學校招生專區
U_RDRC_REG = "https://rdrc.mnd.gov.tw/EditPage/?PageID=1aa12f51-0d98-4cf4-87c3-bf114bd6965b"  # 國軍人才招募中心：正期班報名資訊
U_RDRC = "https://rdrc.mnd.gov.tw/"


def _source(text, href, label):
    return p(draft(text) + "　" + text_link(label, href), muted=True)



def render():
    opening = "".join([
        statement(
            draft("報考護理學系，要準備的五件事。"),
            draft("誰可以報名、收多少人、什麼時候報名、簡章在哪裡、去哪裡報名。"
                  "規定每年都可能調整，一切以當年度招生簡章為準。"),
        ),
        actions(button("下載 115 學年度招生簡章", U_BROCHURE)),
    ])

    eligibility = "".join([
        p(draft("護理學系學士班透過「軍事學校正期班甄選入學」招生，由國防部統一辦理報名、體檢與測驗。")),
        as_of("115 學年度軍事學校正期班甄選入學招生簡章"),
        facts([
            ("招生對象", "一、年齡：社會青年、後備役士官兵及替代役備役人員：17 歲至22 歲。<br>"
                        "二、學歷：公私立高中（職）畢業或同等學力。"),
            ("身分別", "軍費生、代訓生（輔導會公費生）"),
        ]),
        _source("摘自《115 學年度軍事學校正期班甄選入學招生簡章》。", U_BACH, "學校招生專區（大學部）"),
        note("請學生事務依當年度簡章補上：體格標準、學科與體能測驗項目、代訓生（輔導會公費生）的額外條件；"
             "請逐字摘錄並註明簡章頁碼，不要改寫條件。"),
    ])

    quota = "".join([
        p(draft("每年的招生名額由國防部核定，公布在當年度招生簡章，各入學管道與身分別的名額不同。")),
        facts([
            ("軍費生", draft("名額待填")),
            ("代訓生（輔導會公費生）", draft("名額待填")),
        ]),
        note("請學生事務從當年度正式簡章抄錄護理學系各身分別名額，並註明學年度與簡章頁碼；"
             "沒有官方出處前，本表保持「名額待填」，不要填推估數字。"),
    ])

    schedule = split(
        "".join([
            p(draft("報名、體檢、測驗、放榜與報到都有固定日程，由國軍人才招募中心公告，也寫在當年度招生簡章裡。")),
            p(draft("錄取後的第一站是新生入伍訓練，之後才回到內湖校區開始四年的護理課程。")),
            actions(text_link("國軍人才招募中心：正期班報名資訊", U_RDRC_REG)),
        ]),
        illo_slot("月曆上圈起報名與測驗日期（CocoMaterial，重新上色）", "4/3", unit="dept"),
        cols=(7, 5),
    )

    brochures = route_list([
        ("115 學年度軍校正期班甄選入學簡章", "PDF，學校招生專區提供", U_BROCHURE),
        ("115 學年度大學部招生資訊（簡報）", "PDF，國防醫學大學招生簡報", U_SLIDES),
        ("歷年正期班招生簡章", "108 至 115 學年度，學校招生專區", U_BACH),
    ], unit="dept")

    links = route_list([
        ("國軍人才招募中心", "正期班報名、體檢與測驗的官方入口", U_RDRC),
        ("國防醫學大學招生專區", "各學系與研究所招生資訊", U_SCHOOL),
        ("護理學院招生專區", "學士班、碩士班、博士班一次比較", L("F")),
    ], unit="dept")

    return page(
        opening,
        name_tape("報考資格"),
        eligibility,
        name_tape("招生名額"),
        quota,
        name_tape("報名時程"),
        schedule,
        note("請學生事務在新學年度簡章公布後，補上報名期間、體檢與測驗日期、放榜與報到日期，逐字取自簡章或國軍人才招募中心公告並註明出處；"
             "新簡章一公布就更新，舊學年度日期不要留在頁面上。"),
        name_tape("招生簡章"),
        brochures,
        name_tape("校部招生連結"),
        links,
        actions(text_link("職涯發展：公費、服役與分發", L("dept:D-2")), text_link("家長常見問題", L("F-1"))),
        owner=META["owner"],
    )
