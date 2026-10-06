"""Handoff package: what each content owner still has to confirm or supply, and the CMS node plan.

Usage: python tools/handoff.py
Writes handoff/待確認清單.csv (open in Excel), handoff/待確認清單.md, handoff/節點清單.csv.
Every page is rendered once with recording versions of draft()/todo()/note(), so the lists always match the pages.
"""
import csv
import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import components  # noqa: E402
import links  # noqa: E402

OUT = ROOT / "handoff"
SITE_NAME = {"college": "護理學院", "dept": "護理學系", "inst": "護理研究所",
             "en_college": "英文學院", "en_dept": "英文學系", "en_inst": "英文研究所"}
NODE_TABLE = {"college": links.NODE, "dept": links.DEPT_NODE, "inst": links.INST_NODE,
              "en_college": links.EN_NODE, "en_dept": links.EN_DEPT_NODE, "en_inst": links.EN_INST_NODE}

RECORD = []
_draft, _todo, _note = components.draft, components.todo, components.note


def _plain(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(text))).strip()


def draft(text):
    RECORD.append(("待確認", _plain(text)))
    return _draft(text)


def todo(text):
    RECORD.append(("待提供", _plain(text)))
    return _todo(text)


def note(text):
    RECORD.append(("編輯備註", _plain(text)))
    return _note(text)


components.draft, components.todo, components.note = draft, todo, note


PEOPLE = ["院窗口", "三長", "哲君", "教發", "圖儀", "國際事務", "學生事務", "學務", "課委會", "辰禧老師", "系學會", "研究所", "學系"]


def mentioned(text):
    """Who a note or request names (often not the page owner)."""
    return "、".join(p for p in PEOPLE if p in text)


def file_name(site, meta):
    return f"{meta['id']}_{meta['slug']}" if site == "college" else f"{site}_{meta['id']}_{meta['slug']}"


def parent_id(pid):
    return pid.rsplit("-", 1)[0] if "-" in pid else ("" if pid == "A" else "A")


def main():
    OUT.mkdir(exist_ok=True)
    rows, nodes = [], []
    for f in sorted((ROOT / "pages").glob("*.py")):
        if f.name.startswith("_"):
            continue
        m = importlib.import_module(f"pages.{f.stem}")
        meta = m.META
        site = meta.get("site", "college")
        components.SITE_UNIT = site.replace("en_", "")
        components.SITE_LANG = "en" if site.startswith("en_") else "zh"
        components.DRAFT_MARKS = True
        RECORD.clear()
        m.render()
        name = file_name(site, meta)
        node = NODE_TABLE[site].get(meta["id"])
        live = f"{links.SITE}/unit/{node}" if node else "需新建"
        nodes.append([SITE_NAME[site], meta["id"], meta["title"], parent_id(meta["id"]), live,
                      f"dist/{name}.html", meta.get("owner", "院窗口")])
        seen = set()
        for kind, text in RECORD:
            if (kind, text) in seen or not text:
                continue
            seen.add((kind, text))
            rows.append([meta.get("owner", "院窗口"), SITE_NAME[site], meta["id"], meta["title"], kind, text,
                         f"preview/{name}.html", mentioned(text) if kind != "待確認" else ""])

    order = {"待提供": 0, "編輯備註": 1, "待確認": 2}
    rows.sort(key=lambda r: (r[0], list(SITE_NAME.values()).index(r[1]), r[2], order[r[4]]))
    head = ["負責人", "網站", "頁面ID", "頁面", "類型", "內容", "預覽檔", "文中提到的人"]
    with open(OUT / "待確認清單.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(head + ["處理結果（請填）"])
        w.writerows(r + [""] for r in rows)
    with open(OUT / "節點清單.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["網站", "頁面ID", "選單名稱", "上層ID", "現有節點（或需新建）", "要貼上的檔案", "負責人"])
        w.writerows(nodes)

    md = ["# 待確認清單（依負責人）", "",
          "類型說明：**待提供** = 需要你提供的資料（目前正式版不顯示）；**編輯備註** = 給你的說明或問題；"
          "**待確認** = 已寫好的句子，請確認內容正確或修改。", ""]
    owners = {}
    for r in rows:
        owners.setdefault(r[0], []).append(r)
    for owner, items in sorted(owners.items(), key=lambda kv: -len(kv[1])):
        counts = {k: sum(1 for r in items if r[4] == k) for k in order}
        md.append(f"## {owner}（待提供 {counts['待提供']}、備註 {counts['編輯備註']}、待確認 {counts['待確認']}）")
        page = None
        for r in items:
            if (r[1], r[2]) != page:
                page = (r[1], r[2])
                md.append(f"\n### {r[1]} {r[2]} {r[3]}（`{r[6]}`）")
            md.append(f"- [ ] **{r[4]}**：{r[5]}" + (f"（→ {r[7]}）" if r[7] and r[7] != owner else ""))
        md.append("")
    (OUT / "待確認清單.md").write_text("\n".join(md), encoding="utf-8")
    new = sum(1 for n in nodes if n[4] == "需新建")
    print(f"{len(rows)} items for {len(owners)} owners; {len(nodes)} pages, {new} need new CMS nodes")


if __name__ == "__main__":
    main()
