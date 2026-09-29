"""Uniform-identity components. Every function returns a CMS-safe HTML string:
inline styles, Bootstrap 5.0.2 classes, FontAwesome 4 icons, <img>; never <style>, <svg>, <section>, <details>."""

from tokens import C, S, TYPE, FONT, TWILL_BG, UNIT

DRAFT_MARKS = True


def _join(parts):
    return "\n".join(p for p in parts if p)


def icon(name):
    return f'<i class="fa fa-{name}" aria-hidden="true"></i>'


# ---------- page frame ----------

def page(*blocks, owner="院窗口", updated="待確認"):
    body = _join(blocks)
    return (
        f'<div class="p-3 p-md-4" style="{TWILL_BG}font-family:{FONT};color:{C["ink"]};{TYPE["body"]}">\n'
        f"{body}\n{status_stamp(owner, updated)}\n</div>"
    )


def status_stamp(owner, updated):
    return (
        f'<p style="margin:{S[8]} 0 0;{TYPE["small"]}color:{C["ink_soft"]};">'
        f'<span style="display:inline-block;padding:6px 12px;border:1.5px dashed {C["rule"]};border-radius:4px;background:{C["tape"]};">'
        f'{icon("calendar-check-o")}&nbsp;最後更新 {updated}　｜　維護：{owner}</span></p>'
    )


def draft(text):
    """Draft copy awaiting the content owner's confirmation."""
    if not DRAFT_MARKS:
        return text
    return (
        f'{text}<span style="display:inline-block;margin-left:6px;padding:0 6px;{TYPE["small"]}font-weight:700;'
        f'color:{C["ink_soft"]};background:{C["tape"]};border:1px dashed {C["ink_soft"]};border-radius:3px;">待確認</span>'
    )

# ---------- type ----------

def statement(text, sub=None):
    """The page's opening claim, in words, before any image."""
    out = f'<h2 style="margin:0 0 {S[2]};color:{C["thread"]};{TYPE["display"]}">{text}</h2>'
    if sub:
        out += f'\n<p style="margin:0 0 {S[3]};max-width:34em;font-size:18px;line-height:1.8;color:{C["ink"]};">{sub}</p>'
    return out


def name_tape(text, level=3, unit="college", top=S[8]):
    """Section heading sewn on as a white name tape with the unit's cloth as a selvedge."""
    cloth = UNIT[unit]["cloth"]
    return (
        f'<h{level} style="display:inline-flex;align-items:center;gap:12px;margin:{top} 0 {S[3]};padding:11px 18px 10px 12px;'
        f'background:{C["tape"]};color:{C["thread"]};font-size:18px;line-height:1.2;font-weight:800;letter-spacing:.12em;'
        f'border:1px solid {C["rule"]};border-radius:2px;outline:1px dashed rgba(51,73,63,.35);outline-offset:-5px;">'
        f'<span aria-hidden="true" style="flex:none;width:12px;height:20px;background:{cloth};border:1.5px solid {C["thread"]};border-radius:1px;"></span>'
        f'{text}</h{level}>'
    )


def h4(text):
    return f'<h4 style="margin:{S[4]} 0 {S[1]};color:{C["thread"]};{TYPE["h3"]}">{text}</h4>'


def p(text, muted=False):
    color = C["ink_soft"] if muted else C["ink"]
    return f'<p style="margin:0 0 {S[2]};max-width:40em;color:{color};">{text}</p>'


def bullets(items):
    lis = "".join(f'<li style="margin:0 0 {S[1]};">{t}</li>' for t in items)
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
        f'{style}border-radius:3px;font-weight:800;font-size:16px;letter-spacing:.06em;text-decoration:none;">'
        f'{label}&nbsp;{icon("long-arrow-right")}</a>'
    )


def text_link(label, href):
    return (
        f'<a href="{href}" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1.5px;">'
        f'{label}&nbsp;{icon("angle-right")}</a>'
    )


def actions(*items):
    return f'<div class="d-flex flex-wrap align-items-center" style="gap:{S[2]} {S[3]};margin:{S[3]} 0 0;">{"".join(items)}</div>'


# ---------- material placeholders ----------

def illo_slot(label, ratio="4/3", unit="college"):
    """Space reserved for a CocoMaterial illustration recoloured to the palette."""
    pale = UNIT[unit]["pale"]
    return (
        f'<div role="img" aria-label="插圖預留：{label}" style="aspect-ratio:{ratio};width:100%;display:flex;flex-direction:column;'
        f'align-items:center;justify-content:center;gap:6px;background:{pale};color:{C["ink_soft"]};{TYPE["small"]}text-align:center;'
        f'border:1.5px dashed rgba(51,73,63,.35);border-radius:4px;padding:{S[2]};">'
        f'{icon("pencil")}<span>插圖：{label}</span></div>'
    )


def photo_slot(label, ratio="4/3"):
    return (
        f'<div role="img" aria-label="照片預留：{label}" style="aspect-ratio:{ratio};width:100%;display:flex;flex-direction:column;'
        f'align-items:center;justify-content:center;gap:6px;background:{C["tape"]};color:{C["ink_soft"]};{TYPE["small"]}text-align:center;'
        f'border:1.5px dashed {C["rule"]};border-radius:3px;padding:{S[2]};">'
        f'{icon("camera")}<span>照片：{label}</span></div>'
    )


# ---------- identity pieces ----------

def rocker(text):
    """An arched tab sewn above a shield patch; carries the parent name instead of an eyebrow label."""
    return (
        f'<div style="position:relative;z-index:1;width:84%;margin:0 auto -10px;padding:12px 8px 14px;text-align:center;'
        f'background:{C["tape"]};border:5px solid {C["thread"]};border-radius:50% 50% 8px 8px / 100% 100% 8px 8px;'
        f'outline:1.5px dashed rgba(51,73,63,.45);outline-offset:-10px;color:{C["thread"]};font-weight:900;'
        f'font-size:15px;letter-spacing:.2em;line-height:1.2;">{text}</div>'
    )


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
    inner = ""
    if illo:
        inner += f'<div style="margin:0 auto {S[2]};width:78%;">{illo}</div>'
    inner += (f'<span style="display:block;color:{C["thread"]};font-size:21px;font-weight:900;letter-spacing:.08em;'
              f'line-height:1.35;">{title}</span>')
    if sub:
        inner += f'<span style="display:block;margin-top:6px;color:{C["thread"]};{TYPE["small"]}font-weight:600;">{sub}</span>'
    if href:
        inner += f'<span style="display:inline-block;margin-top:{S[1]};color:{C["thread"]};font-size:20px;">{icon("arrow-circle-right")}</span>'
    box = (
        f'display:block;position:relative;width:{width};background:{cloth};border:6px solid {C["thread"]};border-radius:{radius};'
        f'outline:2px dashed rgba(247,244,239,.85);outline-offset:-13px;padding:{S[4]} {S[3]} {pad_bottom};'
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


RIBBON_STRIPES = [
    [(C["sage"], 34), (C["tape"], 5), (C["thread"], 6), (C["tape"], 5), (C["sage"], 50)],
    [(C["pink"], 20), (C["thread"], 4), (C["pink"], 52), (C["thread"], 4), (C["pink"], 20)],
    [(C["blue"], 42), (C["tape"], 16), (C["blue"], 42)],
    [(C["thread"], 10), (C["sage"], 80), (C["thread"], 10)],
    [(C["tape"], 30), (C["blue"], 6), (C["thread"], 28), (C["blue"], 6), (C["tape"], 30)],
    [(C["sage_pale"], 44), (C["thread"], 3), (C["sage_pale"], 6), (C["thread"], 3), (C["sage_pale"], 44)],
]


def _stripes(bands):
    stops, a = [], 0
    for col, w in bands:
        stops.append(f"{col} {a}% {a + w}%")
        a += w
    return "linear-gradient(90deg," + ",".join(stops) + ")"


def ribbon_bar(items):
    """Quick entrances as a ribbon rack: ribbons butted edge to edge, each labelled beneath. [(label, href), ...]"""
    cells = []
    for i, (label, href) in enumerate(items):
        stripes = _stripes(RIBBON_STRIPES[i % len(RIBBON_STRIPES)])
        cells.append(
            f'<a href="{href}" style="flex:1 1 104px;display:block;text-decoration:none;color:{C["thread"]};margin:0 0 {S[2]} -2px;">'
            f'<span style="display:block;height:40px;background:{stripes};border:2px solid {C["thread"]};"></span>'
            f'<span style="display:block;margin-top:10px;text-align:center;font-weight:800;font-size:15.5px;letter-spacing:.06em;">{label}</span></a>'
        )
    return (
        f'<div style="display:flex;flex-wrap:wrap;margin:{S[5]} 0 0 2px;padding:{S[3]} 0 {S[1]};border-top:1.5px dashed {C["rule"]};">'
        + "".join(cells) + "</div>"
    )

def route_list(items, unit="college"):
    """Stitched list of destinations: [(title, desc, href), ...]. Rows, not cards."""
    rows = []
    for title, desc, href in items:
        rows.append(
            f'<a href="{href}" style="display:flex;align-items:center;justify-content:space-between;gap:{S[2]};'
            f'padding:{S[2]} {S[1]} {S[2]} 0;min-height:56px;border-top:1.5px dashed {C["rule"]};text-decoration:none;color:{C["ink"]};">'
            f'<span><span style="display:block;color:{C["thread"]};font-weight:800;font-size:18px;letter-spacing:.04em;">{title}</span>'
            + (f'<span style="display:block;margin-top:2px;{TYPE["small"]}color:{C["ink_soft"]};">{desc}</span>' if desc else "")
            + f'</span><span style="flex:none;color:{C["thread"]};font-size:22px;">{icon("angle-right")}</span></a>'
        )
    return (f'<div style="margin:0 0 {S[4]};border-bottom:1.5px dashed {C["rule"]};max-width:44em;">'
            + "".join(rows) + "</div>")


def split(left, right, cols=(7, 5), reverse=False, align="center"):
    """Two-column row that stacks on phones. reverse puts the right block first on desktop."""
    lo = ' order-md-2' if reverse else ''
    ro = ' order-md-1' if reverse else ''
    return (
        f'<div class="row" style="--bs-gutter-x:{S[4]};row-gap:{S[3]};align-items:{align};margin-bottom:{S[3]};">'
        f'<div class="col-md-{cols[0]}{lo}">{left}</div>'
        f'<div class="col-md-{cols[1]}{ro}">{right}</div></div>'
    )


def feature_lead(title, text_blocks, illo, unit="college", href=None, link_label="了解更多"):
    """The one feature that leads: big patch beside text, overlapping the tape surface."""
    body = _join([
        f'<h4 style="margin:0 0 {S[2]};color:{C["thread"]};font-size:26px;font-weight:900;line-height:1.35;">{title}</h4>',
        *text_blocks,
        text_link(link_label, href) if href else "",
    ])
    return split(body, f'<div class="mx-auto" style="max-width:300px;">{patch(title, unit=unit, illo=illo, backing=C["tape"])}</div>', cols=(7, 5))


def feature_list(items):
    """Secondary features as a stitched ledger: [(title, text, href, unit[, mark]), ...]; each round patch carries a mark."""
    rows = []
    for item in items:
        title, text, href, unit = item[:4]
        mark = item[4] if len(item) > 4 else title[0]
        cloth = C["tape"] if unit == "tape" else UNIT[unit]["cloth"]
        rows.append(
            f'<div class="d-flex" style="gap:{S[3]};padding:{S[3]} 0;border-top:1.5px dashed {C["rule"]};">'
            f'<span aria-hidden="true" style="flex:none;width:60px;height:60px;border-radius:50%;background:{cloth};'
            f'border:4px solid {C["thread"]};outline:1.5px dashed rgba(247,244,239,.9);outline-offset:-9px;display:flex;'
            f'align-items:center;justify-content:center;color:{C["thread"]};font-weight:900;font-size:22px;">{mark}</span>'
            f'<div><h4 style="margin:0 0 6px;color:{C["thread"]};{TYPE["h3"]}">{title}</h4>'
            f'<p style="margin:0 0 6px;max-width:38em;">{text}</p>'
            + (text_link("前往", href) if href else "") + "</div></div>"
        )
    return f'<div style="border-bottom:1.5px dashed {C["rule"]};margin-bottom:{S[4]};">' + "".join(rows) + "</div>"

def unit_pair(units):
    """Peer units as two patches: [(unit, title, sub, href), ...]."""
    cols = "".join(
        f'<div class="col-6">{patch(t, sub, href, unit=u, shape="shield")}</div>' for u, t, sub, href in units
    )
    return f'<div class="row" style="--bs-gutter-x:{S[3]};row-gap:{S[3]};margin-bottom:{S[4]};">{cols}</div>'


def timeline(events):
    """History as year patches sewn along one thread, oldest first: [(year, title, text[, unit]), ...].
    Each patch wears its unit's cloth (college/dept/inst); events owned by no unit wear tape cloth."""
    rows = []
    for i, ev in enumerate(events):
        year, title, text = ev[:3]
        unit = ev[3] if len(ev) > 3 else "tape"
        cloth = C["tape"] if unit == "tape" else UNIT[unit]["cloth"]
        rows.append(
            f'<div class="d-flex" style="gap:{S[3]};position:relative;padding-bottom:{S[4]};">'
            f'<span style="flex:none;position:relative;z-index:{i + 1};width:84px;height:84px;border-radius:50%;background:{cloth};'
            f'border:5px solid {C["thread"]};outline:1.5px dashed rgba(51,73,63,.45);outline-offset:-10px;display:flex;'
            f'align-items:center;justify-content:center;color:{C["thread"]};font-weight:900;font-size:17px;letter-spacing:.04em;">{year}</span>'
            f'<div style="padding-top:{S[3]};"><h4 style="margin:0 0 6px;color:{C["thread"]};{TYPE["h3"]}">{title}</h4>'
            f'<p style="margin:0;max-width:36em;">{text}</p></div></div>'
        )
    return (f'<div style="position:relative;margin:0 0 {S[4]};">'
            f'<div aria-hidden="true" style="position:absolute;left:40px;top:0;bottom:0;width:3px;background:{C["thread"]};"></div>'
            + "".join(rows) + "</div>")

def roster(people):
    """Unit roster rows: [(name, rank, unit, fields, href), ...]. Photo 3:4 left."""
    rows = []
    for name, rank, unit, fields, href in people:
        rows.append(
            f'<div class="row g-3 align-items-start" style="padding:{S[2]} 0;border-top:1.5px dashed {C["rule"]};margin:0;">'
            f'<div class="col-4 col-md-2">{photo_slot(name, "3/4")}</div>'
            f'<div class="col-8 col-md-10"><span style="display:block;color:{C["thread"]};font-weight:900;font-size:19px;">{name}'
            f'<span style="margin-left:10px;{TYPE["small"]}font-weight:700;color:{C["ink_soft"]};">{rank}｜{unit}</span></span>'
            f'<span style="display:block;margin-top:4px;">{fields}</span>'
            + (text_link("個人研究頁", href) if href else "") + "</div></div>"
        )
    return f'<div style="border-bottom:1.5px dashed {C["rule"]};margin-bottom:{S[4]};">' + "".join(rows) + "</div>"


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


def faq_index(items, prefix="q"):
    """Jump list to every question on a long FAQ page."""
    lis = "".join(
        f'<li><a href="#{prefix}{i}" style="display:block;padding:10px 0;min-height:44px;color:{C["thread"]};'
        f'font-weight:700;text-decoration:underline;text-underline-offset:5px;">{q}</a></li>'
        for i, (q, _) in enumerate(items, 1)
    )
    return f'<ol style="margin:0 0 {S[4]};padding-left:1.4em;max-width:40em;color:{C["thread"]};">{lis}</ol>'

def facts(rows):
    """Label/value ledger, e.g. contact details: [(label, value_html), ...]."""
    trs = "".join(
        f'<tr><th scope="row" style="padding:{S[2]} {S[3]} {S[2]} 0;vertical-align:top;white-space:nowrap;color:{C["thread"]};'
        f'font-weight:800;border-top:1.5px dashed {C["rule"]};">{k}</th>'
        f'<td style="padding:{S[2]} 0;border-top:1.5px dashed {C["rule"]};">{v}</td></tr>'
        for k, v in rows
    )
    return f'<table style="width:100%;max-width:44em;border-collapse:collapse;margin:0 0 {S[4]};">{trs}</table>'


def org_tree(head, branches):
    """Chain of command: head patch, branches [(title, [children...], unit)].
    Desktop: branches hang from one stitched bar. Phone: one vertical thread runs from the head through every branch."""
    cols = []
    for title, children, unit in branches:
        kids = "".join(
            f'<li style="padding:6px 8px;border-top:1px dashed {C["rule"]};{TYPE["small"]}">{k}</li>' for k in children
        )
        cols.append(
            f'<div style="flex:1 1 180px;position:relative;z-index:1;">'
            f'<div aria-hidden="true" style="width:3px;height:{S[3]};margin:0 auto;background:{C["thread"]};"></div>'
            f'{patch(title, unit=unit, shape="tab")}'
            + (f'<ul style="list-style:none;margin:{S[2]} 0 0;padding:0;background:{C["tape"]};border:1px solid {C["rule"]};border-radius:3px;">{kids}</ul>' if kids else "")
            + "</div>"
        )
    return (
        f'<div style="position:relative;margin:0 0 {S[5]};">'
        f'<div aria-hidden="true" class="d-md-none" style="position:absolute;left:50%;top:0;bottom:0;width:3px;margin-left:-1.5px;background:{C["thread"]};"></div>'
        f'<div style="position:relative;z-index:1;max-width:320px;margin:0 auto;">{patch(head, unit="college", shape="tab")}</div>'
        f'<div aria-hidden="true" class="d-none d-md-block" style="width:3px;height:{S[3]};background:{C["thread"]};margin:0 auto;"></div>'
        f'<div aria-hidden="true" class="d-none d-md-block" style="height:3px;background:{C["thread"]};margin:0 90px;"></div>'
        f'<div style="display:flex;flex-wrap:wrap;gap:{S[3]};">'
        + "".join(cols) + "</div></div>"
    )

def note(text):
    """A plain editorial note for the content owner (e.g. what goes here), shown only while drafts are marked."""
    if not DRAFT_MARKS:
        return ""
    return (f'<p style="margin:{S[3]} 0 {S[3]};padding:{S[1]} {S[2]};max-width:40em;{TYPE["small"]}color:{C["rose"]};'
            f'background:{C["rose_pale"]};border-radius:3px;">{icon("info-circle")}&nbsp;編輯備註：{text}</p>')
