from components import page, name_tape, statement, p, h4, text_link, actions, illo_slot, facts, draft, note
from links import L
from pages._en_college_shared import zh

META = {"id": "F-1", "slug": "partnership-map", "title": "Global Partnership Map", "owner": "國際事務", "site": "en_college"}

# No verified partner list exists (pages/G-1_partnerships.py lists none). This page is structure only:
# every institution, country, year and collaboration type is a slot for 國際事務 to fill.

REGIONS = ["Asia-Pacific", "North America", "Europe", "Other regions"]
ROW = ("〔Partner institution〕",
       "〔Country／region〕｜〔Collaboration type: student exchange, academic visits, visiting scholars, joint research〕"
       "｜〔Since year〕｜〔Linked outcome〕")


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

    regions = []
    for r in REGIONS:
        regions.append(h4(draft(r)))
        regions.append(facts([ROW]))

    return page(
        opening,
        name_tape("Partner Map", unit="inst"),
        map_slot,
        note("地圖為靜態圖片（CMS 不能用 SVG 或互動地圖），盟校名單確認後再繪製並標出所在城市。"),
        name_tape("Partners by Region", unit="inst"),
        p(draft("Each entry shows the partner, its country or region, the type of collaboration, the year it began and a link "
                "to related outcomes.")),
        *regions,
        note("請國際事務提供盟校／合作單位名單：學校英文正式名稱、國家或地區、合作類型、合作起始年、校級或院級、相關成果連結"
             "（可連到 Collaboration Highlights 的個案）。名單確認前不列任何學校名稱；區域依實際名單增刪，列數依實際數量增減。"),
        name_tape("Related Pages"),
        actions(text_link("International Collaboration", L("en:F")), text_link("Collaboration Contact", L("en:G-3"))),
        owner=META["owner"],
    )
