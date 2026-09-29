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

CHROME = """<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
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
    for m in load_pages():
        meta = m.META
        html = cms_normalize(m.render())
        for pat in FORBIDDEN:
            if re.search(pat, html, re.I):
                print(f"FORBIDDEN {pat} in {meta['id']}")
                problems += 1
        name = f"{meta['id']}_{meta['slug']}"
        (DIST / f"{name}.html").write_text(html, encoding="utf-8")
        (PREVIEW / f"{name}.html").write_text(CHROME.format(title=meta["title"], body=html), encoding="utf-8")
        drafts = html.count("待確認")
        index.append(f'<li><a href="{name}.html">{meta["id"]}　{meta["title"]}</a>　<small>{len(html)//1024} KB · 待確認 {drafts}</small></li>')
        print(f"{meta['id']:5} {meta['title']:12} {len(html):7} bytes  drafts={drafts}")
    (PREVIEW / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>護理學院頁面預覽</title>'
        '<body style="font-family:Microsoft JhengHei,sans-serif;padding:24px;line-height:2;"><h1>護理學院中文站 預覽</h1><ol>'
        + "".join(index) + "</ol></body>", encoding="utf-8")
    return problems


if __name__ == "__main__":
    sys.exit(main(final="--final" in sys.argv))
