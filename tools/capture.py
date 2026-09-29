"""Capture review screenshots sized to each page's measured height (desktop 1440, true 390px phone via iframe).

Usage: python tools/capture.py <out_dir> page1,page2,...   (preview server must be running on :8801)
"""
import json
import pathlib
import re
import subprocess
import sys

CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "http://127.0.0.1:8801"


def measure(pages):
    out = subprocess.run([CH, "--headless=new", "--disable-gpu", "--virtual-time-budget=40000", "--dump-dom",
                          f"{BASE}/_measure.html#{','.join(pages)}"], capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"H=(\{[^<]*\})", out.stdout)
    return json.loads(m.group(1))


def shoot(url, width, height, path):
    subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=6000",
                    f"--window-size={width},{height}", f"--screenshot={path}", url], capture_output=True)


def main(out_dir, pages):
    out = ROOT / out_dir
    out.mkdir(parents=True, exist_ok=True)
    heights = measure(pages)
    (out / "heights.json").write_text(json.dumps(heights, indent=1), encoding="utf-8")
    frame = ROOT / "preview" / "_m.html"
    for pg in pages:
        d, m = heights[f"{pg}@1440"] + 300, heights[f"{pg}@390"] + 300
        shoot(f"{BASE}/{pg}.html", 1440, d, out / f"{pg}-desktop.png")
        frame.write_text(re.sub(r"height:\d+px;border", f"height:{m}px;border", frame.read_text(encoding="utf-8")), encoding="utf-8")
        shoot(f"{BASE}/_m.html#{pg}.html", 390, m, out / f"{pg}-mobile.png")
        print(pg, d, m)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2].split(","))
