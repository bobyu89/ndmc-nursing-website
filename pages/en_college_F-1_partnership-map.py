from components import page, name_tape, statement, p, h4, text_link, actions, illo_slot, facts, draft, note, todo
from links import L
from pages._en_college_shared import zh

META = {"id": "F-1", "slug": "partnership-map", "title": "Global Partnership Map", "owner": "國際事務", "site": "en_college"}

# No verified partner list exists (pages/G-1_partnerships.py lists none). This page is structure only:
# every institution, country, year and collaboration type is a slot for 國際事務 to fill.

REGIONS = ["Asia-Pacific", "North America", "Europe", "Other regions"]


def render():
    opening = "".join([
        statement(
            draft("Where our partners are."),
            draft("Partner institutions by region, with the kind of collaboration, the year it began and what it has produced."),
        ),
        actions(text_link("Collaboration Highlights", L("en:F-2")), zh("G-1")),
    ])

    map_slot = '<div class="mx-auto" style="max-width:640px;margin-bottom:24px;">' + illo_slot(
        "World map with partner locations marked (drawn once the partner list is confirmed)", "16/9", unit="inst") + "</div>"

    # 名單收到前只有 todo（正式版不輸出），地圖與名單兩段連同標題一起隱藏。
    listing = todo("盟校名單，依區域（" + "、".join(REGIONS) + "）分組：每校英文正式名稱、國家或地區、合作類型、"
                   "合作起始年、相關成果連結（國際事務提供）")

    return page(
        opening,
        *([name_tape("Partner Map", unit="inst"), map_slot] if listing else []),
        note("地圖為靜態圖片（CMS 不能用 SVG 或互動地圖），盟校名單確認後再繪製並標出所在城市。"),
        *([name_tape("Partners by Region", unit="inst"), listing] if listing else []),
        note("請國際事務提供盟校／合作單位名單：學校英文正式名稱、國家或地區、合作類型、合作起始年、校級或院級、相關成果連結"
             "（可連到 Collaboration Highlights 的個案）。名單確認前不列任何學校名稱；收到後每區用 h4(區域名) + facts([(校名, 國家｜合作類型｜起始年｜成果連結)]) 列出，區域依實際名單增刪。"),
        name_tape("Related Pages"),
        actions(text_link("International Collaboration", L("en:F")), text_link("Collaboration Contact", L("en:G-3"))),
        owner=META["owner"],
    )
