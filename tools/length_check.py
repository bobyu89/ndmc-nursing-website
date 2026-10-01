"""Phone length budget: flag pages longer than 8 phone screens (390 x 844) at 390px width.

Usage: python tools/length_check.py   (preview server must be running on :8801)
"""
import json
import pathlib
import re
import subprocess
import sys

CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "http://127.0.0.1:8801"
SCREEN = 844
BUDGET = 8
CHROME_PX = 230  # mock university bar + breadcrumb above our content in the preview


def measure(pages):
    out = subprocess.run([CH, "--headless=new", "--disable-gpu", "--virtual-time-budget=120000", "--dump-dom",
                          f"{BASE}/_measure390.html#{','.join(pages)}"], capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"H=(\{[^<]*\})", out.stdout)
    return json.loads(m.group(1)) if m else {}


def main():
    probe = ROOT / "preview" / "_measure390.html"
    probe.write_text(
        "<!doctype html><meta charset=\"utf-8\"><body><pre id=o></pre><script>"
        "const pages=location.hash.slice(1).split(',');const out={};"
        "(async()=>{for(const pg of pages){const f=document.createElement('iframe');"
        "f.style.cssText='width:390px;height:600px;border:0';document.body.appendChild(f);"
        "await new Promise(r=>{f.onload=r;f.src=pg+'.html'});await new Promise(r=>setTimeout(r,150));"
        "out[pg]=f.contentDocument.documentElement.scrollHeight;f.remove();}"
        "document.getElementById('o').textContent='H='+JSON.stringify(out);})();</script>",
        encoding="utf-8")
    pages = sorted(p.stem for p in (ROOT / "dist").glob("*.html"))
    heights = {}
    for i in range(0, len(pages), 32):
        heights.update(measure(pages[i:i + 32]))
    over = []
    for pg in pages:
        h = heights.get(pg)
        if h is None:
            print(f"?? {pg} not measured")
            continue
        screens = (h - CHROME_PX) / SCREEN
        if screens > BUDGET:
            over.append((screens, pg))
    for screens, pg in sorted(over, reverse=True):
        print(f"OVER {screens:4.1f} screens  {pg}")
    print(f"{len(heights)} pages measured, {len(over)} over the {BUDGET}-screen phone budget")
    return 0


if __name__ == "__main__":
    sys.exit(main())
