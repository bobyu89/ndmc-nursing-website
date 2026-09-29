from components import (page, name_tape, statement, p, button, text_link, actions, photo_slot, split,
                        tape_surface, route_list, facts, draft, note)
from links import L

META = {"id": "G-2", "slug": "exchange", "title": "學生交流", "owner": "國際事務、辰禧老師"}

SLOT = "〔待提供〕"
FORMS = L("G-2-表單下載")


def render():
    opening = "".join([
        statement(
            draft("出國看看別人怎麼照護病人，再把學到的帶回來。"),
            draft("這裡整理本院學生出國交流、境外學生來校的紀錄與心得，以及申請交流要準備什麼、表單在哪裡下載。"),
        ),
        actions(button("下載申請表單", FORMS), text_link("看申請資訊", "#apply")),
    ])

    outbound = split(
        "".join([
            p(draft("本院學生曾赴美國華盛頓大學交流。")),
            p(draft("每一次出國交流，都會記錄交流學校、時間、參加同學與學習內容。")),
            note("「N75學生至美國華盛頓大學交流」取自護理學系網站輪播照片標題。請國際事務確認交流時間、天數、參加人數與內容，"
                 "並提供其他年度的出國交流紀錄。頁面上的屆別代號（N75）請改寫成「某年入學的學生」這類外部讀者看得懂的說法。"),
        ]),
        photo_slot("學生赴美國華盛頓大學交流（待提供並確認可公開）", "4/3"),
        cols=(7, 5), align="start",
    )

    inbound = "".join([
        p(draft("我們也歡迎境外護理學生來校交流。")),
        note("請國際事務提供境外學生來校紀錄：年份、來自哪所學校、人數、交流內容與照片。若目前沒有來校交流，請刪除此段或改寫為未來規劃。"),
    ])

    records = "".join([
        p(draft("歷年交流紀錄依年份排列，由新到舊。")),
        note("有真實資料後，本段改用年份時間軸（每筆：年份、出國或來校、交流學校、內容一句話）。資料確認前不放任何年份，以免出現假資料。"),
    ])

    reflection = "".join([
        tape_surface(
            p(draft("「學生交流心得摘錄，約三到四句：去了哪裡、看到什麼、回來後改變了什麼。」")),
            p("〔學生姓名〕　〔入學年／年級〕　〔交流學校〕", muted=True),
        ),
        note("請辰禧老師協助收集 2 至 3 篇學生心得（各 150 字內），並取得學生本人同意公開姓名與照片；也可放完整心得的附檔連結。"),
    ])

    apply = "".join([
        '<div id="apply"></div>',
        facts([
            ("誰可以申請", SLOT),
            ("申請時間", SLOT),
            ("甄選方式", SLOT),
            ("費用與補助", SLOT),
            ("出國前準備", SLOT),
        ]),
        note("請國際事務提供申請資格、每年申請時程、甄選方式、費用與補助、行前準備（護照、保險、校內核准程序）。"
             "未確認前每一格保持〔待提供〕。"),
        route_list([
            ("〔表單名稱一〕", "〔用途一句話〕", FORMS),
            ("〔表單名稱二〕", "〔用途一句話〕", FORMS),
        ], unit="inst"),
        note("請國際事務提供實際的表單清單（名稱、用途、檔案）。表單建議放在 CMS 表單下載模組（新建節點），本頁連結會指向該節點；"
             "也可以直接附上檔案連結。"),
    ])

    contact = "".join([
        facts([
            ("國際事務窗口", SLOT),
            ("電話", SLOT),
            ("電子信箱", SLOT),
        ]),
        note("請提供承辦人職稱（可不列姓名）、分機與公務信箱。"),
    ])

    return page(
        opening,
        name_tape("出國交流", unit="inst"),
        outbound,
        name_tape("境外學生來校", unit="inst"),
        inbound,
        name_tape("歷年交流紀錄", unit="inst"),
        records,
        name_tape("學生心得", unit="dept"),
        reflection,
        name_tape("申請資訊與表單"),
        apply,
        name_tape("諮詢窗口"),
        contact,
        actions(text_link("國際合作", L("G-1")), text_link("回國際交流", L("G"))),
        owner=META["owner"],
    )
