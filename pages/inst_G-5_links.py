from components import page, name_tape, statement, p, route_list, draft, note
from links import L
from tokens import SITE

META = {"id": "G-5", "slug": "links", "title": "研究生常用連結", "owner": "院窗口", "site": "inst"}

# 網址出處（2026-09-29 擷取，皆已確認可開啟，除另註明者）：
#   校務資訊系統、數位學習平台2.0、學生學習歷程系統、教務相關表單：學校網站頂端「線上系統／表單」選單
#   教務處公告資訊、選課停修規定（unit/100002/167）、博碩士班學位論文撰寫規定（unit/100002/165）：
#     研究生手冊引用的教務處頁，網域已由 ndmctsgh 換成 ndmutsgh
#   圖書館、電子資源、院外連線說明、館藏目錄OPAC、BrowZine、ERS、學位論文、論文上傳與查詢系統、
#     Turnitin／iThenticate：圖書館網站選單與「電子資源」「學位論文」頁（unit/100036/43、/2919、/2398）
#   臺灣學術倫理教育資源中心：研究所「必修-研究倫理教育」頁（unit/100181/6800）顯示的網址
# 名稱沿用各網站自己的標示；每行說明為草稿。

NDLTD = ("https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&amp;extralimit=asc=%22%E5%9C%8B%E9%98%B2"
         "%E9%86%AB%E5%AD%B8%E5%A4%A7%E5%AD%B8%22&amp;extralimitunit=%E5%9C%8B%E9%98%B2%E9%86%AB%E5%AD%B8%E5%A4%A7"
         "%E5%AD%B8&amp;searchmode=basic")


def render():
    school = route_list([
        ("校務資訊系統", draft("選課、成績與個人學籍資料"), "https://sas.ndmctsgh.edu.tw/IASS/Logout.aspx"),
        ("學生學習歷程系統", draft("記錄修課、活動與學習成果"), "https://epo.ndmutsgh.edu.tw/NDMCEP"),
        ("教務處公告資訊", draft("選課、註冊、行事曆等教務公告"), SITE + "/news/191/100002/951"),
        ("教務相關表單", draft("教務處的申請表單下載"), SITE + "/unit/100002/158"),
        ("國防醫學大學選課停修規定", draft("停修申請的規定與表單"), SITE + "/unit/100002/167"),
        ("博、碩士班學位論文撰寫規定", draft("論文格式要點、審定書等表單"), SITE + "/unit/100002/165"),
    ], unit="inst")

    elearning = route_list([
        ("數位學習平台2.0", draft("上課教材、線上測驗；口試申請資料與論文輔導紀錄也從這裡上傳"),
         "https://eclass.ndmutsgh.edu.tw/"),
    ], unit="inst")

    library = route_list([
        ("圖書館", draft("圖書館首頁：開放時間、公告與服務"), SITE + "/unit/100036/43"),
        ("館藏目錄OPAC", draft("查紙本書、期刊與館藏位置"), "https://m7.ndmutsgh.edu.tw/webopac/"),
        ("電子資源", draft("資料庫、電子期刊與電子書入口"), SITE + "/unit/100036/2919"),
        ("電子資源查詢系統ERS", draft("用名稱找學校訂購的資料庫與電子期刊"),
         "https://800a.flysheet.com.tw/user/login/?next=https%3A//800a.flysheet.com.tw/"),
        ("電子期刊查詢BrowZine", draft("依學科瀏覽學校可讀的電子期刊"), "https://browzine.com/libraries/1197/subjects"),
        ("院外連線說明", draft("在校外使用電子資源的設定方式"), SITE + "/unit/100036/2256"),
    ], unit="inst")

    thesis = route_list([
        ("學位論文", draft("圖書館說明：論文建檔上傳、延後公開與離校手續"), SITE + "/unit/100036/2398"),
        ("博碩士論文上傳系統", draft("口試通過後上傳論文電子檔"), "https://cloud.ncl.edu.tw/ndmc0/"),
        ("國防醫學大學博碩士論文查詢系統", draft("找學長姐的論文，參考題目與方法"), NDLTD),
        ("Turnitin 論文原創比對", draft("論文建檔前做比對檢測"),
         "https://docs.google.com/forms/d/1ldJI5ak8T1I-Zu5_bi7jTE1kfCSs_bRUDPoMWZ7FBpQ/preview"),
        ("iThenticate 論文原創比對", draft("圖書館提供的另一套比對服務"), SITE + "/unit/100036/7081"),
        ("臺灣學術倫理教育資源中心", draft("研究倫理教育必修課的上課與測驗平台"), "https://ethics.moe.edu.tw/"),
    ], unit="inst")

    return page(
        statement(
            draft("研究生每天會用到的系統，都在這一頁。"),
            draft("選課查成績、上數位學習平台、找文獻、上傳論文。每個連結都附一句話說明用途。"),
        ),
        name_tape("校務資訊"),
        school,
        name_tape("數位學習"),
        elearning,
        name_tape("圖書與研究資源"),
        library,
        name_tape("論文與研究倫理系統"),
        thesis,
        note("以上連結取自學校、教務處、圖書館與研究所現行網頁。研究生手冊中的數位學習網址仍是舊網域"
             "（eclass.ndmctsgh.edu.tw），本頁改用學校選單上的新網域；校務資訊系統網址維持學校選單上的舊網域。"
             "學員生大隊碩博生專區（手冊所列 unit/100030/2277）製作時無法開啟，暫不列入，請所辦確認網址。"
             "若有研究所自己的雲端資料夾或群組，請提供後補上。"),
        p(draft("研究倫理與送審流程另有專頁。"), muted=True),
        route_list([
            ("研究倫理", draft("研究倫理教育、IRB 與三總收案申請"), L("inst:G-2")),
            ("表單下載", draft("指導教授申請、口試申請等研究所表單"), L("inst:G-3")),
        ], unit="inst"),
        owner=META["owner"],
    )
