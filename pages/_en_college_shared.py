"""Shared constants for the College of Nursing English site (en_college_* pages).

Underscore-prefixed, so build.py does not render it as a page. Every value here is copied from a verified source:
  contact details  — pages/K_contact.py (verbatim from the current 聯絡我們 page, unit/100010/2199)
  faculty profiles — official English Faculty page https://wwwndmc.ndmutsgh.edu.tw/Doclisten/191/100010/3351
"""

import re
from pathlib import Path

from components import text_link, icon
from links import L
from tokens import SITE

EMAIL = "ndmu_con@mail.ndmutsgh.edu.tw"
MAILTO = f"mailto:{EMAIL}"
TEL = "tel:+886287923100"
MAP = "https://maps.app.goo.gl/MpA4rsvwnFxdnaM37"

ADDRESS = ("College of Nursing (4th floor)<br>National Defense Medical University<br>"
           "No.161, Sec. 6, Minquan E. Rd., Neihu Dist., Taipei City 11490, Taiwan (R.O.C.)")
PHONE = "+886-2-8792-3100 ext. 88916, 18167, 18767, 18165"
FAX = "+886-2-6600-5702"

# Official English faculty list and profile pages (each profile carries position, education, phone, email,
# specialty, lab link, research projects and publications).
FACULTY_EN = SITE + "/Doclisten/191/100010/3351"

# Published images reused from the Chinese pages (same URLs; see the matching Chinese page for each source).
DEAN_PHOTO = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9B%BE%E9%9B%AF%E7%90%A6.jpg"
IMG_EMBLEM = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2LOGO.png"
IMG_FACULTY = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/"
               "%E8%AD%B7%E7%90%86%E5%AD%B8%E9%99%A2%E5%85%A8%E9%AB%94%E6%95%99%E5%B8%AB.jpg")
IMG_WARD1 = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E7%A4%BA%E7%AF%84%E5%AF%A6%E7%BF%92%E7%97%85%E6%88%BF1.png"
IMG_WARD2 = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E7%A4%BA%E7%AF%84%E5%AF%A6%E7%BF%92%E7%97%85%E6%88%BF2.png"
IMG_SIM = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/contents/100010/%E8%99%9B%E6%93%AC%E4%B8%AD%E5%BF%83.png"
IMG_UW = "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100180/slider/S__39010787.jpg"
IMG_NW_VISIT = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/"
                "LINE_ALBUM_1140203NorthwestUniversity_250204_58.jpg")
IMG_NW_GUESTS = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100010/slider/"
                 "LINE_ALBUM_1140203NorthwestUniversity_250204_25.jpg")
IMG_TALK = ("https://wwwndmc.ndmutsgh.edu.tw/files/web/192/menu/100181/slider/LINE_ALBUM_20250115"
            "%E6%BC%94%E8%AC%9B-AI%E5%9C%A8%E8%AD%B7%E7%90%86%E8%87%A8%E5%BA%8A%E5%8F%8A%E7%A0%94%E7%A9%B6"
            "%E4%B9%8B%E6%87%89%E7%94%A8_250204_1.jpg")
PROFILE = SITE + "/DocDetEn/191/100010/3351/"


def zh_title(pid):
    """Title of the Chinese page `pid` ("E-1", "dept:A", "inst:F-1"), read from that page's META; None if not found."""
    site, _, key = pid.rpartition(":")
    prefix = {"": "", "dept": "dept_", "inst": "inst_"}.get(site)
    if prefix is None:
        return None
    for path in sorted(Path(__file__).parent.glob(f"{prefix}{key}_*.py")):
        if not prefix and path.name.startswith(("dept_", "inst_", "en_")):
            continue
        m = re.search(r'"title":\s*"([^"]+)"', path.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return None


def zh(pid, label=None):
    """Language switch to the Chinese counterpart page. The default label names it: 中文版：{Chinese page title}."""
    if label is None:
        title = zh_title(pid)
        label = f"中文版：{title}" if title else "中文版"
    return text_link(label, L(pid))


def email_link():
    return text_link(EMAIL, MAILTO)


def mark(name):
    """A FontAwesome 4.7 glyph used as the mark on a feature-list patch (English titles have no single CJK character)."""
    return icon(name)
