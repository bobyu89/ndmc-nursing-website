from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, photo, feature_list, facts,
                        draft, note)
from links import L

META = {"id": "D", "slug": "campus", "title": "Campus Experience", "owner": "學生事務", "site": "en_dept"}

# Verified: Neihu campus since 1999 — 歷史沿革 unit/100010/6804; 8-week basic training — 115 正期班簡章;
# English address — 聯絡我們 unit/100010/2199 (pages/K_contact.py).
MAP = "https://maps.app.goo.gl/MpA4rsvwnFxdnaM37"
# Student-life photos: department home carousel (unit/100180/6510) "N76_加冠典禮-傳光", "1140303_系大會", "114小畢典";
# checked 200 image/jpeg on 2026-10-01.
IMG_LIGHT = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/LINE_ALBUM_1140317N76%E5%8A%A0%E5%86%A0_250706_68.jpg"
IMG_ASSEMBLY = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/LINE_ALBUM_0303%E7%B3%BB%E5%A4%A7%E6%9C%83_250706_21.jpg"
IMG_GRAD = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/114%E5%B0%8F%E7%95%A2%E5%85%B8.jpg"


def render():
    opening = "".join([
        statement(
            draft("Student nurses and future officers, on one campus."),
            draft("Our students live, study and train together. Their days combine lectures, skills practice, "
                  "physical training and the ceremonies that mark each step into the profession."),
        ),
        actions(text_link("Visit the Department", L("en_dept:G")), text_link("中文版：校園生活", L("dept:I"))),
    ])

    campus = split(
        photo_slot("Neihu campus of the National Defense Medical Center (wide)", "16/9"),
        "".join([
            p("Since 1999 the department has been based on the Neihu campus of the National Defense Medical Center "
              "in Taipei."),
            p(draft("The campus sits next to Tri-Service General Hospital, so classroom, simulation and clinical "
                    "learning happen within walking distance.")),
        ]),
        cols=(7, 5), align="center",
    )

    military = feature_list([
        ("Basic training",
         "Every new student completes eight weeks of military basic training before nursing studies begin.",
         None, "dept", "B"),
        ("Residential life",
         draft("Students live on campus as a cohort, which builds discipline, fitness and teamwork."),
         None, "dept", "R"),
        ("Military nursing",
         draft("Military nursing, care in field, disaster and other special settings, is part of the curriculum "
               "and gives the campus its character."),
         None, "dept", "M"),
    ])

    life = "".join([
        split(photo(IMG_LIGHT, "Capping ceremony: capped students standing in rows on stage", "4/3",
                    caption="Capping ceremony: passing the light"),
              photo(IMG_ASSEMBLY, "Students and faculty at the department general assembly in a lecture hall", "4/3",
                    caption="Department general assembly, March 2025"), cols=(6, 6), align="start"),
        p(draft("Milestones include the welcome for new students, the capping ceremony and graduation. "
                "The student association organizes events through the year.")),
        split(photo(IMG_GRAD, "Graduates in academic gowns with faculty in front of a campus building", "4/3",
                    caption="Department graduation celebration, 2025"),
              photo_slot("Sports or cultural activity", "4/3"), cols=(6, 6), align="start"),
    ])

    visitors = facts([
        ("Address", "No.161, Sec. 6, Minquan E. Rd., Neihu Dist., Taipei City 11490, Taiwan (R.O.C.)"),
        ("College office", "College of Nursing, 4th floor"),
        ("Map", text_link("Open in Google Maps", MAP)),
    ])

    return page(
        opening,
        name_tape("Our Campus"),
        campus,
        note("「校區緊鄰三軍總醫院」為草稿，請學生事務確認可否如此描述，並提供校園外觀照片。"),
        name_tape("Military Nursing Context"),
        military,
        note("住校與團體生活的描述為草稿，請學生事務確認可公開的範圍（作息、住宿、服儀）；不寫任何規定細節。"),
        name_tape("Student Life"),
        life,
        note("加冠、系大會、小畢典三張沿用學系首頁輪播照片（1140303 系大會＝2025 年 3 月；114 小畢典＝2025 年），英文圖說為暫擬。"
             "請學生事務再提供 1 張迎新、運動或社團照片，附英文圖說與年份；學生入鏡需取得同意。"),
        name_tape("For Visitors"),
        visitors,
        note("地址與樓層取自中文「聯絡我們」頁（College of Nursing 位於 4 樓）。軍事校區訪客須事先申請，"
             "請院窗口補一句訪客入校方式（例：需提前幾天提供名單與證件），確認前不寫。"),
        actions(text_link("International Exchange", L("en_dept:E")),
                text_link("Student Learning Outcomes", L("en_dept:C-4"))),
        owner=META["owner"],
    )
