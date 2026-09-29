from components import (page, name_tape, statement, p, text_link, actions, timeline, facts, split, photo_slot,
                        draft, note)
from links import L

META = {"id": "D-2", "slug": "career", "title": "職涯發展", "owner": "學生事務", "site": "dept"}

# 標示「簡章原文」者逐字取自《115 學年度軍事學校正期班甄選入學招生簡章》，與學院「家長常見問題」（pages/F-1_parents.py）
# 使用同一批已核對的句子；研究所身分別取自學院「招生專區」（pages/F_admissions.py）所引《116 學年度博、碩士班招生簡章》。
U_BACH = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2009"
U_BROCHURE = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/file_up/100143/14540/"
              "115學年度軍校正期班甄選入學簡章.pdf")
U_GRAD = "https://wwwndmc.ndmutsgh.edu.tw/unit/100143/2004"
U_MND = "https://www.mnd.gov.tw"
U_VAC = "https://www.vac.gov.tw/mp-1.html"


def _official(text):
    return p(f"簡章原文：「{text}」")


def _cite(label="出自《115 學年度軍事學校正期班甄選入學招生簡章》；每年以最新簡章為準。", href=U_BACH, link="簡章下載頁"):
    return p(draft(label) + "　" + text_link(link, href), muted=True)


def render():
    opening = statement(
        draft("從入伍到任官，先把這條路看清楚。"),
        draft("讀軍護和讀一般護理系最大的不同，是畢業之後的路：公費讀書、任官、服役、分發。"
              "這一頁依時間順序說明，規定一律以當年度招生簡章與國防部公告為準。"),
    )

    path = timeline([
        ("入學", "新生入伍訓練",
         draft("錄取後先到陸軍軍官學校接受八週入伍訓練，再回學校開始護理課程。"), "dept"),
        ("在學", "公費讀四年",
         draft("在學期間享有公費待遇，住校、上課、到三軍總醫院實習，同時接受軍事訓練。"), "dept"),
        ("畢業", "任官",
         draft("軍費生畢業後任官，正式成為護理軍官；代訓生畢業後由輔導會分發服務。"), "dept"),
        ("服役", "分發與服役",
         draft("依規定分發單位，服滿規定年限。年限從任官那天開始算。"), "dept"),
        ("之後", "專業與進修",
         draft("在醫院與部隊累積臨床經驗，也可以回到護理研究所進修碩士。"), "inst"),
    ])

    training = "".join([
        _official("起赴陸軍軍官學校統一實施新生入伍訓練"),
        facts([("入伍訓練", "八週")]),
        _cite(),
    ])

    funding = "".join([
        p(draft("學士班分為「軍費生」與「代訓生（輔導會公費生）」兩種身分，在學期間都享有公費待遇，"
                "但畢業後服務的單位與年限不同。")),
        _official("公費待遇包括主（副）食費、學雜費（含實驗費）、書籍費、制服費、平安保險費、宿舍費（含電腦網路使用費）"
                  "及應屆畢業生旅行參觀費等，上述公費待遇項目之標準，由輔導會報請行政院核定之。"),
        p(draft("上面這句是代訓生（輔導會公費生）的公費待遇內容。"), muted=True),
        _official("軍費生在校期間及畢業任官後之福利、待遇相關事項，依國防部訂頒之相關法令辦理（現行相關內容請參考國防部網站 "
                  "https：//www.mnd.gov.tw 相關網頁）。"),
        _official("學生在校就讀期間不具現役軍人身分，學生親屬不適用現行軍人眷屬之各項福利優待。"),
        _cite(),
        actions(text_link("國防部網站", U_MND)),
        note("待遇金額會隨國防部規定調整，本頁不列數字。若要寫出在學與任官後的待遇，請學生事務提供可公開的正式出處。"),
    ])

    service = "".join([
        _official("護理學院護理學系、公共衛生學院公共衛生學系畢業後服常備軍官現役最少年限 10 年。"),
        _official("自任官之日起服常備軍官現役最少年限 10 年。"),
        _official("畢業後，應依國軍退除役官兵輔導委員會（以下稱輔導會）分發規定，由輔導會分發所屬機構服務 4 年；"
                  "未依規定完成服務義務前，其護理師證書正本由輔導會保管。"),
        p(draft("如果沒有服滿規定年限，需要依規定賠償：")),
        _official("各學系軍費生於規定之服役期間，未履行其服役義務期滿者，專業證書(醫師證書、牙醫師證書、藥師證書、護理師證書、"
                  "公共衛生師證書)由軍醫局保管；另依應服滿與未服滿役期之比率賠償，償還其在學期間所受領公費待遇、津貼總金額之四倍賠償金。"),
        _cite(),
    ])

    rank = "".join([
        p(draft("軍費生畢業後「任官」，也就是正式成為軍官；任官的階級與相關規定，依國防部規定辦理。")),
        note("簡章沒有寫明任官階級。若要在本頁寫出階級，請學生事務提供可公開的正式出處。"),
    ])

    assignment = "".join([
        p(draft("軍費生畢業後的分發，依國防部相關規定辦理；代訓生由輔導會分發所屬機構。")),
        _official("畢業時，由輔導會統籌協調相關單位辦理分發作業；其分發作業服務要點，由輔導會另定之。"),
        _cite(),
        actions(text_link("國軍退除役官兵輔導委員會", U_VAC)),
        note("簡章只寫了代訓生的分發方式。軍費生可分發的單位類型（例如哪些醫院、部隊）能否公開、怎麼寫，請學生事務確認並提供出處。"),
    ])

    growth = split(
        "".join([
            p(draft("畢業後的職涯，從臨床護理開始，也可以往專科、教學、管理或研究發展。")),
            p(draft("護理研究所的碩士班設有給現職軍人進修的身分別：")),
            facts([("研究所身分別", "全時進修軍費生、全時進修自費生、公餘進修軍職生、公餘進修自費生")]),
            _cite("研究所身分別摘自《116 學年度博、碩士班招生簡章》。", U_GRAD, "碩博士班招生簡章"),
            actions(text_link("護理研究所", L("inst:A"))),
        ]),
        photo_slot("學姊在病房帶學妹交班（直式 3:4）", "3/4"),
        cols=(8, 4), align="start",
    )

    return page(
        opening,
        note("公費、服役、授階、分發、待遇等內容可公開到什麼程度尚未決定。全頁上線前，須由學生事務與院窗口逐段確認可公開範圍。"
             "標示「簡章原文」者逐字摘自《115 學年度軍事學校正期班甄選入學招生簡章》（" + U_BROCHURE + "）；其餘文字為草稿。"),
        name_tape("四年之後的路"),
        path,
        name_tape("入伍訓練"),
        training,
        name_tape("公費制度與待遇"),
        funding,
        name_tape("服役義務"),
        service,
        name_tape("授階"),
        rank,
        name_tape("分發"),
        assignment,
        name_tape("職涯發展"),
        growth,
        note("請學生事務提供：① 可公開的畢業生職涯路徑範例（例如臨床、專科護理師、教學、管理），不寫個人姓名除非本人同意；"
             "② 一兩位學長姐的經驗分享（需本人授權）；③ 一張可公開的臨床照片。沒有出處的就業率或升遷數字請勿填入。"),
        name_tape("給家長"),
        p(draft("家長最常問的九件事，護理學院整理在「家長常見問題」，每一題都附上簡章原文。")),
        actions(text_link("家長常見問題", L("F-1")), text_link("招生資訊", L("dept:D-1"))),
        owner=META["owner"],
    )
