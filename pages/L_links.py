from components import page, name_tape, statement, p, route_list, draft, note
from links import L

META = {"id": "L", "slug": "links", "title": "常用連結", "owner": "院窗口"}


def render():
    # URLs: 國防護理Facebook and 護理學系校友會 from the current left menu; the rest from the current
    # 杏網相連 link list (LinkList/191/100010/934). Titles are the site's own labels.
    ours = route_list([
        ("國防護理Facebook", draft("給想看學院活動、營隊與日常的高中生、家長與校友"),
         "https://www.facebook.com/profile.php?id=100063652101597"),
        ("國防護理 Instagram", draft("給習慣用 IG 的學生與高中生，看活動照片與短影音"), L("instagram")),
        ("國防醫學大學護理學系系校友會", draft("給畢業校友：校友聯繫與活動"), "http://www.ndmcnd.url.tw/"),
    ])

    others = route_list([
        ("國防醫學大學招生專區", draft("給考生與家長：全校各學制招生資訊"), "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/1861"),
        ("國軍人才招募中心", draft("給想了解從軍管道與軍職待遇的考生與家長"), "https://rdrc.mnd.gov.tw/"),
        ("國防醫學大學圖書館", draft("給師生：館藏查詢與電子資源"), "https://wwwndmc.ndmutsgh.edu.tw/unit/100036/43"),
        ("國防醫學大學 校務資訊整合系統", draft("給在校師生：選課、成績等校務系統"), "https://sas.ndmctsgh.edu.tw/IASS/index.aspx"),
        ("三軍總醫院", draft("本院臨床教學與實習的主要醫院"), "https://www.tsgh.ndmctsgh.edu.tw/"),
        ("台灣護理學會", draft("給護理學生與護理人員：專業學會的研討會與繼續教育"), "https://www.twna.org.tw/"),
        ("中華民國護理師護士公會全國聯合會", draft("給護理人員：執業與公會事務"), "http://www.nurse.org.tw/Default.aspx"),
        ("醫事系統入口網", draft("給護理人員：醫事人員執業登記與繼續教育積分查詢"), "https://ma.mohw.gov.tw/maportal/"),
    ])

    return page(
        statement(
            draft("學院的社群與校友入口。"),
            draft("追蹤學院動態、聯繫校友會，或前往學校系統與護理專業團體。"),
        ),
        name_tape("學院社群與校友"),
        ours,
        note("網站上找不到國防護理 Instagram 帳號，請院窗口提供正確網址後替換。"
             "校友會網址 http://www.ndmcnd.url.tw/ 為現行網站所列，請確認仍在使用。"),
        name_tape("學校與護理專業網站"),
        p(draft("以下沿用現有連結清單，依你是誰標示用途。")),
        others,
        note("以上八個連結來自現行「杏網相連」清單（護理學系系校友會已移到上方）。請院窗口確認哪些要保留、每一行的用途說明是否正確。"
             "若本頁沿用 CMS 連結模組而非 html 頁，說明文字請改填在各連結的描述欄位。"),
        owner=META["owner"],
    )
