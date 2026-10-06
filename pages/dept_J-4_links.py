from components import page, name_tape, statement, route_list, draft, note
from links import L

META = {"id": "J-4", "slug": "links", "title": "學生常用連結", "owner": "院窗口", "site": "dept"}

# 連結名稱與網址皆取自國防醫學大學網站（2026-09-29 擷取）：
# - 全球資訊網頁尾「線上系統」「各類表單」「學生社團」（任一 wwwndmc 頁面頁尾）
# - 教務處「常用系統連結」 https://wwwndmc.ndmutsgh.edu.tw/LinkList/191/100002/4087
# - 教務處「獎學金專區」與「公告資訊」
# - 學院常用連結（pages/L_links.py）已查到的圖書館、台灣護理學會
# 說明文字皆為暫擬。


def render():
    study = route_list([
        ("數位學習平台2.0", draft("上課教材、作業繳交與線上課程（Eclass）"), "https://eclass.ndmutsgh.edu.tw/"),
        ("校務資訊系統", draft("選課、成績查詢與個人學籍資料"), "https://sas.ndmctsgh.edu.tw/IASS/index.aspx"),
        ("學生學習歷程系統", draft("記錄修課、實習與活動成果，準備學習歷程"), "https://epo.ndmutsgh.edu.tw/NDMCEP"),
        ("國防醫學院個人信箱入口", draft("學校電子郵件；獎學金等申請資訊常以電子郵件通知"),
         "https://webmail.mail.ndmctsgh.edu.tw/owa/auth/logon.aspx?replaceCurrent=1&amp;url=https%3a%2f%2fwebmail.mail.ndmctsgh.edu.tw%2fowa%2f"),
    ], unit="dept")

    school = route_list([
        ("115學年度教育行事曆", draft("全校開學、考試與假期日期（教務處公告）"),
         "https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/951/11594"),
        ("教務相關表單", draft("註冊、選課、成績與學籍相關表單"), "https://wwwndmc.ndmutsgh.edu.tw/unit/100002/158"),
        ("學務相關表單", draft("請假、生活與輔導相關表單"), "https://wwwndmc.ndmutsgh.edu.tw/unit/100030/488"),
        ("獎學金專區（教務處）", draft("全校與校外基金會的獎學金申請公告"), "https://wwwndmc.ndmutsgh.edu.tw/news/191/100002/1750"),
        ("報修系統", draft("教室、宿舍等設備故障時線上報修"), "https://fix.ndmctsgh.edu.tw/ndmc/"),
    ], unit="dept")

    learning = route_list([
        ("國防醫學大學圖書館", draft("館藏查詢、電子期刊與資料庫"), "https://wwwndmc.ndmutsgh.edu.tw/unit/100036/43"),
        ("AREE臺灣學術倫理教育資源中心", draft("免費線上學術倫理課程，寫報告、做研究前先修"), "https://ethics.moe.edu.tw/"),
        ("台灣護理學會", draft("護理專業學會：研討會、繼續教育與學生會員資訊"), "https://www.twna.org.tw/"),
    ], unit="dept")

    life = route_list([
        ("社團總覽", draft("全校社團介紹，依服務、學術、藝術、體育、康樂分類"), "https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100030/2947"),
        ("聯合餐廳菜單", draft("本週餐廳菜單"), "https://wwwndmc.ndmutsgh.edu.tw/unit/100026/4698"),
        ("文宣新聞", draft("學生社團的文宣新聞粉絲專頁（Facebook）"), "https://www.facebook.com/profile.php?id=61579054463407"),
    ], unit="dept")

    dept = route_list([
        ("表單下載", draft("學系的作業要點、學生手冊與申請表單"), L("dept:J-2")),
        ("重要日程", draft("本學期選課、考試、實習與系上活動日期"), L("dept:J-3")),
    ], unit="dept")

    return page(
        statement(
            draft("上課、選課、查資料，常用的系統都在這裡。"),
            draft("每個連結都寫了用途；登入帳號密碼的問題，請洽學校資訊單位。"),
        ),
        name_tape("上課與學習系統"),
        study,
        note("內容清單寫到「E-learning」，學校網站上只找到「數位學習平台2.0」（eclass.ndmutsgh.edu.tw）。"
             "若 E-learning 是另一個系統，請院窗口提供名稱與網址。信箱入口的名稱與網址照教務處常用系統連結所列，請確認學生信箱是否也用這一個。"),
        name_tape("校務與表單"),
        school,
        note("行事曆連結是 115 學年度的公告，每學年請換成新公告。「文宣新聞」「報修系統」「聯合餐廳菜單」取自全球資訊網頁尾，請確認學生適用。"),
        name_tape("圖書與免費學習資源"),
        learning,
        note("內容清單提到「免費學習網站資源」，學校網站上只找到 AREE 學術倫理教育資源中心。"
             "若老師推薦其他免費資源（例如護理技術影片、英文學習、國考準備網站），請院窗口提供名稱、網址與一句話用途。"),
        name_tape("校園生活"),
        life,
        name_tape("學系自己的頁面"),
        dept,
        owner=META["owner"],
    )
