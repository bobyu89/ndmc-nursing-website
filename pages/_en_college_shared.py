"""Shared constants for the College of Nursing English site (en_college_* pages).

Underscore-prefixed, so build.py does not render it as a page. Every value here is copied from a verified source:
  contact details  — pages/K_contact.py (verbatim from the current 聯絡我們 page, unit/100010/2199)
  faculty profiles — official English Faculty page https://wwwndmc.ndmutsgh.edu.tw/Doclisten/191/100010/3351
"""

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
PROFILE = SITE + "/DocDetEn/191/100010/3351/"


def zh(pid, label="中文"):
    """Link to the Chinese counterpart page."""
    return text_link(label, L(pid))


def email_link():
    return text_link(EMAIL, MAILTO)


def mark(name):
    """A FontAwesome 4.7 glyph used as the mark on a feature-list patch (English titles have no single CJK character)."""
    return icon(name)
