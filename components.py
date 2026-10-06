"""Uniform-identity components. Every function returns a CMS-safe HTML string:
inline styles, Bootstrap 5.0.2 classes, FontAwesome 4 icons, <img>; never <style>, <svg>, <section>, <details>."""

import re

from tokens import C, S, TYPE, FONT, TWILL_BG, UNIT

DRAFT_MARKS = True
SITE_UNIT = "college"  # set by build.py from META["site"]
SITE_LANG = "zh"  # "en" on the English sites
UPDATED = "待確認"


def _join(parts):
    return "\n".join(p for p in parts if p)


def _tr(v):
    """Letter-spacing that suits the script: open tracking for CJK, near-default for Latin."""
    return ".01em" if SITE_LANG == "en" else v


def icon(name):
    return f'<i class="fa fa-{name}" aria-hidden="true"></i>'


# ---------- page frame ----------

def page(*blocks, owner="院窗口", updated=None):
    body = _join(blocks)
    updated = updated or UPDATED
    return (
        f'<div id="page-top" class="p-3 p-md-4" style="{TWILL_BG}font-family:{FONT};color:{C["ink"]};{TYPE["body"]}">\n'
        f"{body}\n{status_stamp(owner, updated)}\n</div>"
    )


PUBLIC_UNIT = {
    "zh": {"college": "護理學院", "dept": "護理學系", "inst": "護理研究所"},
    "en": {"college": "College of Nursing", "dept": "Department of Nursing", "inst": "Graduate Institute of Nursing"},
}


def status_stamp(owner, updated):
    """Public stamp names the maintaining unit, never an internal contact; `owner` stays in META for editors."""
    unit = PUBLIC_UNIT[SITE_LANG][SITE_UNIT]
    text = (f"Last updated {updated} · Maintained by {unit}" if SITE_LANG == "en"
            else f"最後更新 {updated}　｜　維護單位：{unit}")
    return (
        f'<p style="margin:{S[8]} 0 0;{TYPE["small"]}color:{C["ink_soft"]};">'
        f'<span style="display:inline-block;padding:6px 12px;border:1.5px dashed {C["rule"]};border-radius:4px;background:{C["tape"]};">'
        f'{icon("calendar-check-o")}&nbsp;{text}</span>'
        f'<span style="display:inline-block;margin-left:{S[2]};">{back_to_top()}</span></p>'
    )


def back_to_top():
    """Return link for long pages; also closes every page beside the status stamp."""
    return text_link("Back to top" if SITE_LANG == "en" else "回到頁首", "#page-top", icon_name="angle-up")


def draft(text):
    """Draft copy awaiting the content owner's confirmation."""
    if not DRAFT_MARKS:
        return text
    return (
        f'{text}<span style="display:inline-block;margin-left:6px;padding:0 6px;{TYPE["small"]}font-weight:700;'
        f'color:{C["ink_soft"]};background:{C["tape"]};border:1px dashed {C["ink_soft"]};border-radius:3px;">待確認</span>'
    )

# ---------- type ----------

def _phrases(text):
    """Wrap each CJK phrase in an inline-block span so lines only break between phrases.
    Phrases split after ，、：； and at an author hint ｜ (removed from output); phrases under 4 characters
    merge into the next so no short fragment sits alone on a line."""
    cut = text.find("<")
    head, tail = (text, "") if cut < 0 else (text[:cut], text[cut:])
    raw = [p for p in re.split(r"(?<=[，、：；])|｜", head) if p]
    parts = []
    for p in raw:
        if parts and len(parts[-1]) < 4:
            parts[-1] += p
        else:
            parts.append(p)
    if len(parts) < 2:
        return head + tail
    return "".join(f'<span style="display:inline-block;max-width:100%;">{p}</span>' for p in parts) + tail


def statement(text, sub=None):
    """The page's opening claim, in words, before any image."""
    out = f'<h2 style="margin:0 0 {S[2]};color:{C["thread"]};text-wrap:balance;{TYPE["display"]}">{_phrases(text)}</h2>'
    if sub:
        out += f'\n<p style="margin:0 0 {S[3]};max-width:34em;font-size:18px;line-height:1.8;color:{C["ink"]};">{sub}</p>'
    return out


def name_tape(text, level=3, unit=None, top=S[8]):
    """Section heading sewn on as a white name tape with the unit's cloth as a selvedge."""
    cloth = UNIT[unit or SITE_UNIT]["cloth"]
    return (
        f'<h{level} style="display:inline-flex;align-items:center;gap:12px;margin:{top} 0 {S[3]};padding:12px 20px 12px 14px;'
        f'background:{C["tape"]};color:{C["thread"]};font-size:26.5px;line-height:1.2;font-weight:900;letter-spacing:{_tr(".1em")};'
        f'border:1px solid {C["rule"]};border-radius:2px;outline:1px dashed rgba(51,73,63,.35);outline-offset:-5px;">'
        f'<span aria-hidden="true" style="flex:none;width:9px;height:30px;background:{cloth};border-left:3px solid {C["thread"]};"></span>'
        f'{text}</h{level}>'
    )


def h4(text):
    return f'<h4 style="margin:{S[4]} 0 {S[1]};color:{C["thread"]};{TYPE["h3"]}">{text}</h4>'


def p(text, muted=False):
    color = C["ink_soft"] if muted else C["ink"]
    return f'<p style="margin:0 0 {S[2]};max-width:40em;color:{color};overflow-wrap:anywhere;">{text}</p>'


def bullets(items):
    lis = "".join(f'<li style="margin:0 0 {S[1]};overflow-wrap:anywhere;">{t}</li>' for t in items)
    return f'<ul style="margin:0 0 {S[3]};padding-left:1.3em;max-width:40em;">{lis}</ul>'


def tape_surface(*blocks):
    """A long-reading passage laid on name-tape cloth."""
    return (f'<div style="background:{C["tape"]};border:1px solid {C["rule"]};border-radius:3px;'
            f'padding:{S[4]} {S[4]} {S[2]};margin:0 0 {S[4]};">{_join(blocks)}</div>')

# ---------- actions ----------

def button(label, href, primary=True):
    if primary:
        style = (f'background:{C["rose"]};color:{C["white"]};border:2px solid {C["rose"]};')
    else:
        style = (f'background:transparent;color:{C["thread"]};border:2px solid {C["thread"]};')
    return (
        f'<a href="{href}" style="display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:0 22px;'
        f'{style}border-radius:3px;font-weight:800;font-size:16px;letter-spacing:{_tr(".06em")};text-decoration:none;">'
        f'{label}&nbsp;{icon("long-arrow-right")}</a>'
    )


def text_link(label, href, icon_name="angle-right"):
    """Inline link. The label names the destination (build.py rejects bare 前往/了解更多/Learn more)."""
    return (
        f'<a href="{href}" style="display:inline;padding:12px 0;line-height:1.9;color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1.5px;">'
        f'{label}&nbsp;{icon(icon_name)}</a>'
    )


def actions(*items):
    return f'<div class="d-flex flex-wrap align-items-center" style="gap:{S[2]} {S[3]};margin:{S[3]} 0 0;">{"".join(items)}</div>'


# ---------- material placeholders ----------

def illo_slot(label, ratio="4/3", unit="college"):
    """Space reserved for a CocoMaterial illustration recoloured to the palette. Hidden on phones until the art exists."""
    if not DRAFT_MARKS:
        return ""
    pale = UNIT[unit]["pale"]
    return (
        f'<div class="d-none d-md-flex" role="img" aria-label="插圖預留：{label}" style="aspect-ratio:{ratio};width:100%;display:flex;flex-direction:column;'
        f'align-items:center;justify-content:center;gap:6px;background:{pale};color:{C["ink_soft"]};{TYPE["small"]}text-align:center;'
        f'border:1.5px dashed rgba(51,73,63,.35);border-radius:4px;padding:{S[2]};">'
        f'{icon("pencil")}<span>{"Illustration: " if SITE_LANG == "en" else "插圖："}{label}</span></div>'
    )


def photo_slot(label, ratio="4/3", phone=False):
    """Space reserved for a photograph. Hidden on phones (phone=True keeps it, e.g. inside a roster row)."""
    if not DRAFT_MARKS:
        return ""
    cls = "d-flex" if phone else "d-none d-md-flex"
    return (
        f'<div class="{cls}" role="img" aria-label="照片預留：{label}" style="aspect-ratio:{ratio};width:100%;display:flex;flex-direction:column;'
        f'align-items:center;justify-content:center;gap:6px;background:{C["tape"]};color:{C["ink_soft"]};{TYPE["small"]}text-align:center;'
        f'border:1.5px dashed {C["rule"]};border-radius:3px;padding:{S[2]};">'
        f'{icon("camera")}<span>{"Photo: " if SITE_LANG == "en" else "照片："}{label}</span></div>'
    )


def _is_slot(html):
    return bool(html) and ('aria-label="插圖預留' in html or 'aria-label="照片預留' in html)


def photo(src, alt, ratio="4/3", fit="cover", caption=None, phone_cap=None):
    """A real image already published on the public site, in the same frame a photo_slot reserves.
    `src` is a full https URL on the university site; `alt` says what the picture shows; `fit="contain"` for logos and charts.
    Portraits (3/4) are capped to 5/12 of the phone width so a face never fills a whole phone screen."""
    if phone_cap is None:
        phone_cap = ratio == "3/4"
    if phone_cap:
        return (f'<div class="row g-0"><div class="col-5 col-md-12">'
                f'{photo(src, alt, ratio, fit, caption, phone_cap=False)}</div></div>')
    pad = f"padding:{S[2]};background:{C['tape']};" if fit == "contain" else ""
    img = (f'<img src="{src}" alt="{alt}" style="display:block;width:100%;aspect-ratio:{ratio};object-fit:{fit};{pad}'
           f'border:1.5px solid {C["rule"]};border-radius:3px;">')
    if not caption:
        return img
    return (f'<div style="margin:0;">{img}<p style="margin:{S[1]} 0 0;{TYPE["small"]}color:{C["ink_soft"]};">{caption}</p></div>')


# ---------- identity pieces ----------

def rocker(text):
    """An arched tab sewn above a shield patch; carries the parent name instead of an eyebrow label."""
    return (
        f'<div style="position:relative;z-index:1;width:84%;margin:0 auto -10px;padding:12px 8px 14px;text-align:center;'
        f'background:{C["tape"]};border:5px solid {C["thread"]};border-radius:50% 50% 8px 8px / 100% 100% 8px 8px;'
        f'outline:1.5px dashed rgba(51,73,63,.45);outline-offset:-10px;color:{C["thread"]};font-weight:900;'
        f'font-size:{"13px;letter-spacing:.04em" if text.isascii() else "15px;letter-spacing:.2em"};line-height:1.2;">{text}</div>'
    )


def _patch_title_size():
    """Latin unit names ("Department") need a smaller phone size to stay whole inside a half-width shield."""
    return "font-size:clamp(14px,3.9vw,21px);" if SITE_LANG == "en" else "font-size:clamp(16px,4.6vw,21px);"


def patch(title, sub=None, href=None, unit="college", shape="shield", illo=None, width="100%", tab=None, backing=None):
    """An embroidered unit patch: cloth, merrowed edge, stitched inset. Optionally a link, a rocker tab,
    and a backing cloth cut to the same outline, larger on every side (depth by layered cloth, not shadow)."""
    cloth = C["tape"] if unit == "tape" else UNIT[unit]["cloth"]
    radius = {
        "shield": "14px 14px 48% 48% / 14px 14px 30% 30%",
        "round": "50%",
        "tab": "8px",
    }[shape]
    pad_bottom = S[6] if shape == "shield" else S[3]
    pad_x = S[1] if shape == "tab" else ("12px" if SITE_LANG == "en" else S[3])  # Latin unit names need the width
    inner = ""
    if illo is not None and not illo:
        illo = None
    if illo:
        hide = ' class="d-none d-md-block"' if _is_slot(illo) else ""
        inner += f'<div{hide} style="margin:0 auto {S[2]};width:78%;">{illo}</div>'
    if title:
        inner += (f'<span style="display:block;color:{C["thread"]};{_patch_title_size()}font-weight:900;letter-spacing:{_tr(".06em")};word-break:keep-all;overflow-wrap:{"break-word" if SITE_LANG == "en" else "anywhere"};'
                  f'line-height:1.35;">{title}</span>')
    if sub:
        inner += f'<span style="display:block;margin-top:6px;color:{C["thread"]};{TYPE["small"]}font-weight:600;">{sub}</span>'
    if href:
        inner += f'<span style="display:inline-block;margin-top:{S[1]};color:{C["thread"]};font-size:20px;">{icon("arrow-circle-right")}</span>'
    box = (
        f'display:block;position:relative;width:{width};background:{cloth};border:6px solid {C["thread"]};border-radius:{radius};'
        f'outline:2px dashed rgba(247,244,239,.85);outline-offset:-13px;padding:{S[4]} {pad_x} {pad_bottom};'
        f'text-align:center;text-decoration:none;'
    )
    if shape == "round":
        box += "aspect-ratio:1/1;display:flex;flex-direction:column;align-items:center;justify-content:center;"
    body = f'<a href="{href}" style="{box}">{inner}</a>' if href else f'<div style="{box}">{inner}</div>'
    if backing:
        body = (
            f'<div style="position:relative;margin:10px;">'
            f'<div aria-hidden="true" style="position:absolute;inset:-10px;background:{backing};border-radius:{radius};'
            f'border:1.5px dashed rgba(51,73,63,.45);"></div>{body}</div>'
        )
    return (rocker(tab) + body) if tab else body


def _ribbon_patterns():
    """Six stripe patterns cut from the site's own cloth and the neutrals; no other unit's colour."""
    cloth, pale = UNIT[SITE_UNIT]["cloth"], UNIT[SITE_UNIT]["pale"]
    t, th = C["tape"], C["thread"]
    return [
        [(cloth, 34), (t, 5), (th, 6), (t, 5), (cloth, 50)],
        [(pale, 20), (th, 4), (cloth, 52), (th, 4), (pale, 20)],
        [(cloth, 42), (t, 16), (cloth, 42)],
        [(th, 10), (cloth, 80), (th, 10)],
        [(t, 30), (cloth, 6), (th, 28), (cloth, 6), (t, 30)],
        [(pale, 44), (th, 3), (pale, 6), (th, 3), (pale, 44)],
    ]


def _stripes(bands):
    stops, a = [], 0
    for col, w in bands:
        stops.append(f"{col} {a}% {a + w}%")
        a += w
    return "linear-gradient(90deg," + ",".join(stops) + ")"


def ribbon_bar(items):
    """Entrances as a ribbon rack: ribbons butted edge to edge, each labelled beneath. [(label, href[, sub]), ...]
    The optional sub-line says what is behind the ribbon. Four ribbons wrap 2+2 on phones; five wrap 3+2."""
    basis = "140px" if len(items) == 4 else "104px"
    patterns = _ribbon_patterns()
    cells = []
    for i, (label, href, *sub) in enumerate(items):
        stripes = _stripes(patterns[i % len(patterns)])
        sub_html = (f'<span style="display:block;margin-top:2px;padding:0 4px;text-align:center;{TYPE["small"]}font-weight:400;'
                    f'color:{C["ink_soft"]};letter-spacing:0;">{sub[0]}</span>') if sub and sub[0] else ""
        cells.append(
            f'<a href="{href}" style="flex:1 1 {basis};display:block;text-decoration:none;color:{C["thread"]};margin:0 0 {S[2]};">'
            f'<span style="display:block;height:40px;background:{stripes};border:2px solid {C["thread"]};"></span>'
            f'<span style="display:block;margin-top:10px;padding:0 6px;text-align:center;overflow-wrap:anywhere;font-weight:800;font-size:15.5px;letter-spacing:{_tr(".06em")};'
            f'text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1.5px;">{label}&nbsp;{icon("angle-right")}</span>{sub_html}</a>'
        )
    return (
        f'<div style="display:flex;flex-wrap:wrap;gap:0 {S[1]};margin:{S[5]} 0 0;padding:{S[3]} 0 {S[1]};border-top:1.5px dashed {C["rule"]};">'
        + "".join(cells) + "</div>"
    )

def route_list(items, unit="college"):
    """Stitched list of destinations: [(title, desc, href), ...]. Rows, not cards."""
    rows = []
    for title, desc, href in items:
        rows.append(
            f'<a href="{href}" style="display:flex;align-items:center;justify-content:space-between;gap:{S[2]};'
            f'padding:{S[2]} {S[1]} {S[2]} 0;min-height:56px;border-top:1.5px dashed {C["rule"]};text-decoration:none;color:{C["ink"]};">'
            f'<span><span style="display:block;color:{C["thread"]};font-weight:800;font-size:18px;letter-spacing:{_tr(".04em")};">{title}</span>'
            + (f'<span style="display:block;margin-top:2px;{TYPE["small"]}color:{C["ink_soft"]};">{desc}</span>' if desc else "")
            + f'</span><span style="flex:none;color:{C["thread"]};font-size:22px;">{icon("angle-right")}</span></a>'
        )
    return (f'<div style="margin:0 0 {S[4]};border-bottom:1.5px dashed {C["rule"]};max-width:44em;">'
            + "".join(rows) + "</div>")


def split(left, right, cols=(7, 5), reverse=False, align="center"):
    """Two-column row that stacks on phones. reverse puts the right block first on desktop."""
    lo = ' order-md-2' if reverse else ''
    ro = ' order-md-1' if reverse else ''
    # a column whose only content is hidden on phones is hidden itself, so it leaves no gap
    lo += " d-none d-md-block" if left.lstrip().startswith('<div class="d-none d-md-block') else ""
    ro += " d-none d-md-block" if right.lstrip().startswith(('<div class="d-none d-md-block', '<div class="mx-auto d-none d-md-block')) else ""
    return (
        f'<div class="row" style="--bs-gutter-x:{S[4]};row-gap:{S[3]};align-items:{align};margin-bottom:{S[3]};">'
        f'<div class="col-md-{cols[0]}{lo}">{left}</div>'
        f'<div class="col-md-{cols[1]}{ro}">{right}</div></div>'
    )


def feature_lead(title, text_blocks, illo, unit="college", href=None, link_label=None):
    """The one feature that leads: big patch beside text, overlapping the tape surface."""
    body = _join([
        f'<h4 style="margin:0 0 {S[2]};color:{C["thread"]};font-size:26px;font-weight:900;line-height:1.35;">{title}</h4>',
        *text_blocks,
        text_link(link_label or _more(title), href) if href else "",
    ])
    if not illo:
        return body
    hide = " d-none d-md-block" if _is_slot(illo) else ""
    return split(body, f'<div class="mx-auto{hide}" style="max-width:300px;">{patch(None, unit=unit, illo=illo, backing=C["tape"])}</div>', cols=(7, 5))


def _plain(html):
    return re.sub(r"<[^>]+>", "", html)


def _more(title):
    """A link label that names where it goes."""
    t = _plain(title)
    return f"More on {t}" if SITE_LANG == "en" else f"更多{t}"


def feature_list(items):
    """Secondary features as a stitched ledger: [(title, text, href, unit[, mark]), ...]; each round patch carries a mark."""
    rows = []
    for item in items:
        title, text, href, unit = item[:4]
        mark = item[4] if len(item) > 4 and item[4] else title[0]
        label = item[5] if len(item) > 5 else _more(title)
        cloth = C["tape"] if unit == "tape" else UNIT[unit]["cloth"]
        rows.append(
            f'<div class="d-flex" style="gap:{S[3]};padding:{S[3]} 0;border-top:1.5px dashed {C["rule"]};">'
            f'<span aria-hidden="true" style="flex:none;width:60px;height:60px;border-radius:50%;background:{cloth};'
            f'border:4px solid {C["thread"]};outline:1.5px dashed rgba(247,244,239,.9);outline-offset:-9px;display:flex;'
            f'align-items:center;justify-content:center;color:{C["thread"]};font-weight:900;font-size:22px;">{mark}</span>'
            f'<div><h4 style="margin:0 0 6px;color:{C["thread"]};{TYPE["h3"]}">{title}</h4>'
            f'<p style="margin:0 0 6px;max-width:38em;">{text}</p>'
            + (text_link(label, href) if href else "") + "</div></div>"
        )
    return f'<div style="border-bottom:1.5px dashed {C["rule"]};margin-bottom:{S[4]};">' + "".join(rows) + "</div>"

def unit_pair(units):
    """Peer units as two patches: [(unit, title, sub, href), ...]."""
    cols = "".join(
        f'<div class="col-12 col-sm-6"><div class="mx-auto" style="max-width:300px;">{patch(t, sub, href, unit=u, shape="shield")}</div></div>'
        for u, t, sub, href in units
    )
    return f'<div class="row" style="--bs-gutter-x:{S[3]};row-gap:{S[3]};margin-bottom:{S[4]};">{cols}</div>'


def timeline(events):
    """History as year patches sewn along one thread, oldest first: [(year, title, text[, unit]), ...].
    Each patch wears its unit's cloth (college/dept/inst); events owned by no unit wear tape cloth."""
    used = []
    for ev in events:
        u = ev[3] if len(ev) > 3 else "tape"
        if u not in used:
            used.append(u)
    used.sort(key=["college", "dept", "inst", "tape"].index)
    names = {"college": PUBLIC_UNIT[SITE_LANG]["college"], "dept": PUBLIC_UNIT[SITE_LANG]["dept"],
             "inst": PUBLIC_UNIT[SITE_LANG]["inst"], "tape": "Other" if SITE_LANG == "en" else "其他"}
    keys = "".join(
        f'<span style="display:inline-flex;align-items:center;gap:6px;margin-right:{S[3]};">'
        f'<span aria-hidden="true" style="width:16px;height:16px;border-radius:50%;background:{C["tape"] if u == "tape" else UNIT[u]["cloth"]};'
        f'border:2px solid {C["thread"]};"></span>{names[u]}</span>' for u in used)
    legend = (f'<p style="margin:0 0 {S[3]};{TYPE["small"]}color:{C["ink_soft"]};">'
              f'{"Patch colour shows the unit: " if SITE_LANG == "en" else "年份臂章的顏色代表單位："}{keys}</p>') if len(used) > 1 else ""
    rows = []
    for i, ev in enumerate(events):
        year, title, text = ev[:3]
        unit = ev[3] if len(ev) > 3 else "tape"
        cloth = C["tape"] if unit == "tape" else UNIT[unit]["cloth"]
        rows.append(
            f'<div class="d-flex" style="gap:{S[3]};position:relative;padding-bottom:{S[4]};">'
            f'<span style="flex:none;position:relative;z-index:{i + 1};width:84px;height:84px;border-radius:50%;background:{cloth};'
            f'border:5px solid {C["thread"]};outline:1.5px dashed rgba(51,73,63,.45);outline-offset:-10px;display:flex;'
            f'align-items:center;justify-content:center;color:{C["thread"]};font-weight:900;font-size:17px;letter-spacing:{_tr(".04em")};">{year}</span>'
            f'<div style="padding-top:{S[3]};"><h4 style="margin:0 0 6px;color:{C["thread"]};{TYPE["h3"]}">{title}'
            + (f'<span style="display:block;{TYPE["small"]}font-weight:700;color:{C["ink_soft"]};">{names[unit]}</span>' if unit != "tape" else "")
            + '</h4>'
            f'<p style="margin:0;max-width:36em;">{text}</p></div></div>'
        )
    return (legend + f'<div style="position:relative;margin:0 0 {S[4]};">'
            f'<div aria-hidden="true" style="position:absolute;left:40px;top:0;bottom:0;width:3px;background:{C["thread"]};"></div>'
            + "".join(rows) + "</div>")

def roster(people, anchor=None, start=1):
    """Unit roster rows: [(name, rank, unit, fields, href[, img]), ...]. Photo 3:4 left; `img` is a public portrait URL.
    With `anchor="p"` each row gets id p1, p2 ... (counting from `start`) for roster_index."""
    rows = []
    for n, (name, rank, unit, fields, href, *img) in enumerate(people, start):
        pic = photo(img[0], _plain(name), "3/4", phone_cap=False) if img and img[0] else photo_slot(name, "3/4", phone=True)
        rid = f' id="{anchor}{n}"' if anchor else ""
        rows.append(
            f'<div{rid} class="row g-3 align-items-start" style="padding:{S[2]} 0;border-top:1.5px dashed {C["rule"]};margin:0;">'
            f'<div class="col-4 col-md-2">{pic}</div>'
            f'<div class="col-8 col-md-10"><span style="display:block;color:{C["thread"]};font-weight:900;font-size:19px;">{name}'
            f'<span style="margin-left:10px;{TYPE["small"]}font-weight:700;color:{C["ink_soft"]};">{rank}｜{unit}</span></span>'
            f'<span style="display:block;margin-top:4px;">{fields}</span>'
            + (text_link(f"{_plain(name)}’s research page" if SITE_LANG == "en" else f"{_plain(name)}的研究頁", href) if href else "")
            + "</div></div>"
        )
    return f'<div style="border-bottom:1.5px dashed {C["rule"]};margin-bottom:{S[4]};">' + "".join(rows) + "</div>"


def roster_index(people, anchor="p", start=1):
    """Compact name index for a long roster: names wrap as a line of links to roster(..., anchor=) rows."""
    links = "".join(
        f'<a href="#{anchor}{n}" style="display:inline-block;min-height:44px;padding:10px 0;margin-right:{S[3]};color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;">{_plain(p[0])}</a>'
        for n, p in enumerate(people, start))
    return f'<div style="margin:0 0 {S[3]};max-width:44em;line-height:1.4;">{links}</div>'


def faq(items, prefix="q"):
    """Questions fully expanded (no collapse available): [(q, a_html), ...]. Each question carries an id for faq_index."""
    rows = []
    for i, (q, a) in enumerate(items, 1):
        rows.append(
            f'<div id="{prefix}{i}" style="padding:{S[4]} 0 {S[3]};border-top:1.5px dashed {C["rule"]};">'
            f'<h4 style="margin:0 0 {S[2]};color:{C["thread"]};font-size:21px;line-height:1.45;font-weight:900;">{q}</h4>'
            f'<div style="max-width:40em;">{a}</div></div>'
        )
    return f'<div style="border-bottom:1.5px dashed {C["rule"]};margin-bottom:{S[4]};">' + "".join(rows) + "</div>"


def as_of(text):
    """Visible as-of line beside year-specific facts and dates."""
    label = "As of: " if SITE_LANG == "en" else "資料日期："
    return p(f'{icon("calendar")}&nbsp;<strong>{label}</strong>{text}', muted=True)


def fact_line(text):
    """The answer in one line, before any explanation."""
    return (f'<p style="margin:0 0 {S[2]};max-width:40em;color:{C["thread"]};font-size:18.5px;line-height:1.6;font-weight:700;">'
            f'{text}</p>')


def source_quote(text, source):
    """Original regulation or brochure wording, set below the plain explanation and smaller than it."""
    return (f'<div style="margin:{S[2]} 0 {S[2]};padding:{S[2]} {S[3]};max-width:40em;background:{C["tape"]};'
            f'border:1px solid {C["rule"]};border-radius:3px;{TYPE["small"]}color:{C["ink_soft"]};">'
            f'<span style="display:block;margin-bottom:4px;font-weight:700;color:{C["thread"]};">{source}</span>{text}</div>')


def faq_set(groups, prefix="q"):
    """A long FAQ as groups of at most five questions: a grouped jump list, then each group's questions,
    every answer closing with a link back to the list. groups = [(group_title, [(q, a_html), ...]), ...]."""
    back_label = "Back to the questions" if SITE_LANG == "en" else "回到問題列表"
    index, blocks, n = [], [], 0
    for title, items in groups:
        assert len(items) <= 5, f"FAQ group {title} has {len(items)} questions; split it"
        lis, rows = [], []
        for q, a in items:
            n += 1
            lis.append(f'<li><a href="#{prefix}{n}" style="display:block;padding:10px 0;min-height:44px;color:{C["thread"]};'
                       f'font-weight:700;text-decoration:underline;text-underline-offset:5px;">{q}</a></li>')
            rows.append(
                f'<div id="{prefix}{n}" style="padding:{S[4]} 0 {S[3]};border-top:1.5px dashed {C["rule"]};">'
                f'<h4 style="margin:0 0 {S[2]};color:{C["thread"]};font-size:21px;line-height:1.45;font-weight:900;">{q}</h4>'
                f'<div style="max-width:40em;">{a}</div>'
                f'<p style="margin:{S[2]} 0 0;">{text_link(back_label, f"#{prefix}-list", icon_name="angle-up")}</p></div>')
        index.append(f'<h4 style="margin:{S[3]} 0 0;color:{C["thread"]};{TYPE["h3"]}">{title}</h4>'
                     f'<ol start="{n - len(items) + 1}" style="margin:0;padding-left:1.4em;max-width:40em;color:{C["thread"]};">{"".join(lis)}</ol>')
        blocks.append(name_tape(title, top=S[6]) +
                      f'<div style="border-bottom:1.5px dashed {C["rule"]};">{"".join(rows)}</div>')
    return (f'<div id="{prefix}-list" style="margin:0 0 {S[4]};">{"".join(index)}</div>' + "".join(blocks)
            + f'<div style="margin-bottom:{S[4]};"></div>')


def faq_index(items, prefix="q"):
    """Jump list to every question on a long FAQ page."""
    lis = "".join(
        f'<li><a href="#{prefix}{i}" style="display:block;padding:10px 0;min-height:44px;color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;">{q}</a></li>'
        for i, (q, _) in enumerate(items, 1)
    )
    return f'<ol style="margin:0 0 {S[4]};padding-left:1.4em;max-width:40em;color:{C["thread"]};">{lis}</ol>'

def _label_width(label):
    """Short labels stay on one line; digits and Latin count as half a CJK character."""
    plain = re.sub(r"<[^>]+>", "", label)
    visual = sum(0.5 if ch.isascii() else 1 for ch in plain)
    return "white-space:nowrap;" if visual <= 8 else "width:40%;"


def facts(rows):
    """Label/value ledger, e.g. contact details: [(label, value_html), ...]."""
    trs = "".join(
        f'<tr><th scope="row" style="padding:{S[2]} {S[3]} {S[2]} 0;vertical-align:top;{_label_width(k)}color:{C["thread"]};'
        f'font-weight:800;border-top:1.5px dashed {C["rule"]};">{k}</th>'
        f'<td style="padding:{S[2]} 0;border-top:1.5px dashed {C["rule"]};overflow-wrap:anywhere;">{v}</td></tr>'
        for k, v in rows
    )
    return f'<table style="width:100%;max-width:44em;border-collapse:collapse;margin:0 0 {S[4]};">{trs}</table>'


def org_tree(head, branches, head_unit=None):
    """Chain of command: head patch, branches [(title, [children...], unit)].
    Desktop: branches hang from one stitched bar. Phone: one vertical thread runs from the head through every branch."""
    cols = []
    for title, children, unit in branches:
        kids = "".join(
            f'<li style="padding:6px 8px;border-top:1px dashed {C["rule"]};{TYPE["small"]}">{k}</li>' for k in children
        )
        cols.append(
            f'<div style="flex:1 1 0;min-width:0;position:relative;z-index:1;margin-bottom:{S[3]};">'
            f'<div aria-hidden="true" style="width:3px;height:{S[3]};margin:0 auto;background:{C["thread"]};"></div>'
            f'{patch(title, unit=unit, shape="tab")}'
            + (f'<ul style="list-style:none;margin:{S[2]} 0 0;padding:0;background:{C["tape"]};border:1px solid {C["rule"]};border-radius:3px;">{kids}</ul>' if kids else "")
            + "</div>"
        )
    return (
        f'<div style="position:relative;margin:0 0 {S[5]};">'
        f'<div aria-hidden="true" class="d-md-none" style="position:absolute;left:50%;top:0;bottom:0;width:3px;margin-left:-1.5px;background:{C["thread"]};"></div>'
        f'<div style="position:relative;z-index:1;max-width:320px;margin:0 auto;">{patch(head, unit=head_unit or SITE_UNIT, shape="tab")}</div>'
        f'<div aria-hidden="true" class="d-none d-md-block" style="width:3px;height:{S[3]};background:{C["thread"]};margin:0 auto;"></div>'
        f'<div aria-hidden="true" class="d-none d-md-block" style="height:3px;background:{C["thread"]};margin:0 calc((100% - {len(branches) - 1} * {S[2]}) / {2 * len(branches)});"></div>'
        f'<div class="d-md-flex" style="gap:{S[2]};">'
        + "".join(cols) + "</div></div>"
    )

def todo(text):
    """Something an owner must supply (e.g. the dean's message). Draft builds show a dashed request box;
    the final build shows nothing, so instructions never read as published copy."""
    if not DRAFT_MARKS:
        return ""
    return (f'<p style="margin:0 0 {S[2]};padding:{S[1]} {S[2]};max-width:40em;{TYPE["small"]}color:{C["ink_soft"]};'
            f'border:1.5px dashed {C["rule"]};border-radius:3px;">{icon("pencil")}&nbsp;待提供：{text}</p>')


def note(text):
    """A plain editorial note for the content owner (e.g. what goes here), shown only while drafts are marked."""
    if not DRAFT_MARKS:
        return ""
    return (f'<p style="margin:{S[3]} 0 {S[3]};padding:{S[1]} {S[2]};max-width:40em;{TYPE["small"]}color:{C["rose"]};'
            f'background:{C["rose_pale"]};border-radius:3px;overflow-wrap:anywhere;">{icon("info-circle")}&nbsp;編輯備註：{text}</p>')
