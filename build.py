"""Render pages/*.py into dist/ (CMS paste) and preview/ (inside a mock of the university chrome)."""

import importlib
import pathlib
import re
import sys

import components

ROOT = pathlib.Path(__file__).parent
PAGES = ROOT / "pages"
DIST = ROOT / "dist"
PREVIEW = ROOT / "preview"

FORBIDDEN = [r"<style", r"<svg", r"<section", r"<article", r"<details", r"<summary", r"<script"]

CHROME = """<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — 預覽</title>
<link rel="stylesheet" href="https://wwwndmc.ndmutsgh.edu.tw/formsndmc_19/ndmc/css/bootstrap5.0.2.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head><body style="margin:0;background:#f0f0f0;font-family:'Microsoft JhengHei',sans-serif;">
<div style="background:#0256a6;color:#fff;padding:14px 20px;font-size:14px;">國防醫學大學（校方外框模擬）　<a href="index.html" style="color:#fff;">← 全部頁面</a></div>
<div class="container-lg" style="padding:24px 12px;">
 <div class="row">
  <div class="col-lg-3 d-none d-lg-block"><div style="background:#fff;border-top:40px solid #0256a6;padding:12px;font-size:14px;color:#333;height:100%;min-height:300px;">左側樹狀選單（校方）</div></div>
  <div class="col-lg-9 col-12"><div style="background:#fff;">
   <div style="background:#0256a6;color:#fff;padding:8px 14px;">&gt; {title}</div>
   <div style="padding:30px 30px 0;" class="px-2 px-md-4"><div id="contenR" class="editor">
{body}
   </div></div>
  </div></div>
 </div>
</div></body></html>"""


LINK_STYLE = "color:#33493F;font-weight:700;text-decoration:underline;text-underline-offset:4px;"


def theme_bare_links(html):
    """Any <a> written without a style gets the site's thread link style instead of the chrome's default blue."""
    return re.sub(r'<a href="([^"]*)">', lambda m: f'<a href="{m.group(1)}" style="{LINK_STYLE}">', html)


def cms_normalize(html):
    """Apply the CMS server's save filter (verified byte-for-byte on test node 7696): <i> -> <em>, aria-*/role dropped."""
    html = re.sub(r'<i class="([^"]+)" aria-hidden="true"></i>', r'<em class="\1"></em>', html)
    return re.sub(r' (aria-hidden|aria-label|role)="[^"]*"', "", html)


def load_pages():
    sys.path.insert(0, str(ROOT))
    mods = []
    for f in sorted(PAGES.glob("*.py")):
        if f.name.startswith("_"):
            continue
        mods.append(importlib.import_module(f"pages.{f.stem}"))
    return mods


def main(final=False):
    components.DRAFT_MARKS = not final
    if final:
        import datetime
        components.UPDATED = datetime.date.today().isoformat()
    DIST.mkdir(exist_ok=True)
    PREVIEW.mkdir(exist_ok=True)
    index = []
    problems = 0
    groups = {"college": [], "dept": [], "inst": [], "en_college": [], "en_dept": [], "en_inst": []}
    for m in load_pages():
        meta = m.META
        site = meta.get("site", "college")
        components.SITE_UNIT = site.replace("en_", "")
        components.SITE_LANG = "en" if site.startswith("en_") else "zh"
        html = cms_normalize(theme_bare_links(m.render()))
        for pat in FORBIDDEN:
            if re.search(pat, html, re.I):
                print(f"FORBIDDEN {pat} in {meta['id']}")
                problems += 1
        name = f"{meta['id']}_{meta['slug']}" if site == "college" else f"{site}_{meta['id']}_{meta['slug']}"
        (DIST / f"{name}.html").write_text(html, encoding="utf-8")
        (PREVIEW / f"{name}.html").write_text(CHROME.format(title=meta["title"], body=html, lang="en" if site.startswith("en_") else "zh-Hant"), encoding="utf-8")
        drafts = html.count("待確認")
        groups[site].append(f'<li><a href="{name}.html">{meta["id"]}　{meta["title"]}</a>　<small>{len(html)//1024} KB · 待確認 {drafts}</small></li>')
        print(f"{site:7} {meta['id']:6} {meta['title']:12} {len(html):7} bytes  drafts={drafts}")
    labels = {"college": "護理學院", "dept": "護理學系", "inst": "護理研究所",
              "en_college": "College of Nursing (EN)", "en_dept": "Department of Nursing (EN)",
              "en_inst": "Graduate Institute of Nursing (EN)"}
    for site, items in groups.items():
        if items:
            index.append(f"<h2>{labels[site]}（{len(items)} 頁）</h2><ol>" + "".join(items) + "</ol>")
    (PREVIEW / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>護理學院頁面預覽</title>'
        '<body style="font-family:Microsoft JhengHei,sans-serif;padding:24px;line-height:2;"><h1>護理學院・學系・研究所 中文站預覽</h1>'
        + "".join(index) + "</body>", encoding="utf-8")
    return problems


if __name__ == "__main__":
    sys.exit(main(final="--final" in sys.argv))
