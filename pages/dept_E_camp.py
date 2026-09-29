from components import (page, name_tape, statement, p, text_link, actions, split, photo_slot, feature_list,
                        facts, timeline, draft, note)
from links import L

META = {"id": "E", "slug": "camp", "title": "國防迷彩天使災難救護營", "owner": "學生事務", "site": "dept"}

# 未包 draft() 的文字逐字取自現行營隊頁（https://wwwndmc.ndmutsgh.edu.tw/unit/100010/4575，2026-09-29 擷取），
# 只改版面；原頁的表情符號、陰影卡片與英文小標不沿用。
U_MAP = "https://maps.app.goo.gl/RyKdKV1pQhW8ZsFU8"
U_BRIEF = "https://drive.google.com/uc?export=download&id=1B7Uu67r7Jf91GyeYxiqFJuV9vXuiWehI"          # 活動簡章
U_SIZE = "https://drive.google.com/uc?export=download&id=1h0_YP3MZd6R5QcZR_MBFO24wuTHuu2f5"           # 營隊服尺寸參考表
U_CONSENT_HS = "https://drive.google.com/uc?export=download&id=1IUaqnqqPIZbUetizkLXGzPB1tRzokG6t"     # （高中職生）家長同意書
U_CONSENT_NS = "https://drive.google.com/uc?export=download&id=1dkn7j_73uR126QlLNpY1nqcgAZNrcs9r"     # （護理學生）家長同意書


def render():
    opening = "".join([
        statement(
            draft("暑假一天，先穿上迷彩體驗軍護。"),
            "結合災難應變、緊急救護、戰術撤離與軍護特色體驗，帶領高中職生與護理學生認識災難情境下的護理專業角色與實務價值。",
        ),
        actions(text_link("報名資訊與活動簡章", "#signup"), text_link("學系招生專區", L("dept:D"))),
    ])

    purpose = split(
        "".join([
            p("因應災難與重大緊急事件日益頻繁，配合全民國防教育政策，特辦理本災難救護營，分設高中職生及護理學生兩場次。"
              "高中職生場著重建立災難應變與基本救護概念，培養安全意識並認識護理專業；"
              "護理學生場則結合情境教學、實作訓練及三軍總醫院特色單位體驗，強化災難評估、初步救護與團隊合作能力，"
              "培育具備實務應變能力之護理人才，提升社會整體健康與防災韌性。"),
        ]),
        photo_slot("營隊學員練習傷患搬運（橫式 4:3）", "4/3"),
        cols=(7, 5), align="start",
    )

    program = "".join([
        p("本營隊以實作導向與情境體驗為核心，課程涵蓋傷患包紮與搬運、止血救護、戰術撤離及空中救護等內容，"
          "結合講解、示範與分站操作，讓學員在互動中學習災難應變與緊急救護技能。"),
        feature_list([
            ("災難救護實作", "傷患包紮、搬運、止血救護與分站操作。", None, "dept", "救"),
            ("軍護特色體驗", "戰術撤離、空中救護及特殊情境中的護理角色。", None, "dept", "軍"),
            ("專業醫療視野", "護理學生場結合臨床特色單位體驗，深化專業應用。", None, "dept", "醫"),
        ]),
    ])

    sessions = facts([
        ("高中職生場", "以護理探索與基礎救護體驗為主，帶領學員認識災難情境下的基本處置與護理角色。<br>"
                     "全國各公私立高中職學生皆可報名，含國三升高一學生。"),
        ("護理學生場", "結合化生放核防護、高壓氧等臨床特色單位體驗，強化專業知識與實務應用能力。<br>"
                     "全國各公私立大專院校護理科系在學學生皆可報名。"),
    ])

    info = "".join([
        '<div id="signup"></div>',
        facts([
            ("活動日期", "高中職場次 115/8/18（二）<br>護理學生場次 115/8/19（三）"),
            ("招生名額", "各 100 員"),
            ("活動時間", "09:00–18:00<br>08:40 開始報到"),
            ("活動地點", "國防醫學大學護理學院<br>台北市內湖區民權東路六段161號<br>" + text_link("Google Maps 導航", U_MAP)),
            ("活動費用", "新臺幣 1,500 元整<br>完成繳費後恕不退費"),
            ("報名期限", "即日起至 115/6/15"),
            ("錄取方式", "依報名表繳交順序進行審查與錄取"),
            ("繳費提醒", "公布錄取名單後，錄取者將收到繳費資訊，請於 3 日內完成繳費；逾時未繳費者，名額將由候補學員遞補。"
                        "本學院保有最終審核及錄取之決定權。"),
        ]),
        p(draft("以上為 115 年（2026）營隊資訊，已辦理完畢；下一屆日期與報名表公布後更新。"), muted=True),
        actions(text_link("115 年活動簡章", U_BRIEF), text_link("營隊服尺寸參考表", U_SIZE), text_link("（高中職生）家長同意書", U_CONSENT_HS),
                text_link("（護理學生）家長同意書", U_CONSENT_NS)),
    ])

    organisers = facts([
        ("指導單位", "國防部軍醫局"),
        ("主辦單位", "國防醫學大學護理學院"),
        ("協辦單位", "三軍總醫院、台灣護理學會、國防醫學大學校友會、護理學院校友會"),
    ])

    history = "".join([
        timeline([
            ("2026", "國防迷彩天使災難救護營",
             "高中職場次 115/8/18（二）<br>護理學生場次 115/8/19（三）", "college"),
        ]),
        split(photo_slot("115 年高中職生場活動照片（橫式 4:3）", "4/3"),
              photo_slot("115 年護理學生場活動照片（橫式 4:3）", "4/3"), cols=(6, 6)),
    ])

    return page(
        opening,
        name_tape("天使營簡介"),
        purpose,
        program,
        name_tape("兩個場次"),
        sessions,
        name_tape("報名資訊"),
        info,
        note("請學生事務每年更新：日期、名額、費用、報名期限、錄取方式與兩個報名表單連結（報名期間才放表單，截止後移除）。"
             "現行頁的「高中職錄取名單」「護生錄取名單」含學員姓名，本頁不轉載；行前通知上架後再加。"
             "現行頁主視覺圖片連到 Facebook 暫存網址（會過期），請提供原始圖檔上傳到學校網站。"),
        name_tape("辦理單位"),
        organisers,
        name_tape("歷年成果"),
        history,
        note("現行網站只有 2026 年（115 年）這一屆的資料。請學生事務提供：歷年辦理年份（西元與民國）、各屆場次與實際參加人數、"
             "每屆 2–3 張可公開的活動照片（學員可辨識者需有同意書），以及活動成果或回饋摘要。"
             "收到後依年份加入上方時間軸，最早的一屆放最上面；沒有紀錄的年份不要補。"),
        actions(text_link("護理學系招生資訊", L("dept:D-1")), text_link("家長常見問題", L("F-1"))),
        owner=META["owner"],
    )
