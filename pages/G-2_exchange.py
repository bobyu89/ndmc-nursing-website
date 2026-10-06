from components import (page, name_tape, statement, p, button, text_link, actions, photo, split,
                        tape_surface, route_list, facts, draft, note, todo)
from links import L

META = {"id": "G-2", "slug": "exchange", "title": "學生交流", "owner": "國際事務、辰禧老師"}

FORMS = L("G-2-表單下載")

# 照片取自護理學系首頁輪播（unit/100180/6510），輪播標題「N75學生至美國華盛頓大學交流」。
IMG_UW = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/S__39010787.jpg"


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
            p("本院學生曾赴美國華盛頓大學交流。"),
            p(draft("每一次出國交流，都會記錄交流學校、時間、參加同學與學習內容。")),
            note("「N75學生至美國華盛頓大學交流」取自護理學系網站輪播照片標題。請國際事務確認交流時間、天數、參加人數與內容，"
                 "並提供其他年度的出國交流紀錄。頁面上的屆別代號（N75）請改寫成「某年入學的學生」這類外部讀者看得懂的說法。"),
        ]),
        photo(IMG_UW, "學生赴美國華盛頓大學交流期間，與師長在照護機構門前合影", "4/3",
              caption="學生赴美國華盛頓大學交流"),
        cols=(7, 5), align="start",
    )

    inbound = "".join([
        p(draft("我們也歡迎境外護理學生來校交流。")),
        actions(text_link("護理學系境外學生來校紀錄", L("dept:I-3"))),
        note("請國際事務提供境外學生來校紀錄：年份、來自哪所學校、人數、交流內容與照片。護理學系「境外學生來校交流」頁已有西北大學、八王子的來訪紀錄（年份待確認），上方先連過去。"),
    ])

    # 以下三段在資料收到前只有 todo／note，正式版輸出為空，連同標題一起隱藏。
    records = "".join([
        todo("歷年交流紀錄：每筆的年份、出國或來校、交流學校、內容一句話（國際事務提供）"),
        note("有真實資料後，本段改用年份時間軸（每筆：年份、出國或來校、交流學校、內容一句話）。資料確認前不放任何年份，以免出現假資料。"),
    ])

    reflection = "".join([
        todo("學生交流心得 2 至 3 篇（各 150 字內：去了哪裡、看到什麼、回來後改變了什麼），附學生姓名、入學年、交流學校（辰禧老師協助收集）"),
        note("請辰禧老師協助收集 2 至 3 篇學生心得（各 150 字內），並取得學生本人同意公開姓名與照片；也可放完整心得的附檔連結。"),
    ])

    apply_rows = [(k, v) for k, v in [  # todo() is empty in the final build, so unfilled rows drop out
        ("誰可以申請", todo("申請資格（國際事務提供）")),
        ("申請時間", todo("每年申請時程（國際事務提供）")),
        ("甄選方式", todo("甄選方式（國際事務提供）")),
        ("費用與補助", todo("費用與補助（國際事務提供）")),
        ("出國前準備", todo("行前準備：護照、保險、校內核准程序（國際事務提供）")),
    ] if v]
    apply = "".join([
        '<div id="apply"></div>',
        facts(apply_rows) if apply_rows else "",
        note("請國際事務提供申請資格、每年申請時程、甄選方式、費用與補助、行前準備（護照、保險、校內核准程序）。"
             "未確認前這幾格只在草稿顯示待提供，正式版不出現。"),
        todo("申請表單清單：每份表單的名稱、用途一句話與檔案（國際事務提供）"),
        actions(text_link("申請表單下載", FORMS)),
        note("請國際事務提供實際的表單清單（名稱、用途、檔案）。表單建議放在 CMS 表單下載模組（新建節點），本頁連結會指向該節點；"
             "也可以直接附上檔案連結。"),
    ])

    contact = "".join([
        todo("國際事務窗口的承辦人職稱、電話分機、公務信箱（國際事務提供）"),
        note("請提供承辦人職稱（可不列姓名）、分機與公務信箱。"),
    ])

    return page(
        opening,
        name_tape("出國交流", unit="inst"),
        outbound,
        name_tape("境外學生來校", unit="inst"),
        inbound,
        *([name_tape("歷年交流紀錄", unit="inst"), records] if records else []),
        *([name_tape("學生心得", unit="dept"), reflection] if reflection else []),
        name_tape("申請資訊與表單"),
        apply,
        *([name_tape("諮詢窗口"), contact] if contact else []),
        actions(text_link("國際合作", L("G-1")), text_link("回國際交流", L("G"))),
        owner=META["owner"],
    )
