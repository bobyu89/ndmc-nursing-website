---
name: 國防醫學大學護理學院 中文站
description: The uniform's identity system sewn onto Morandi twill; every unit a patch, every section a name tape.
colors:
  twill: "#EDE7DE"
  tape: "#F7F4EF"
  thread: "#33493F"
  ink: "#35322F"
  ink-soft: "#5E5852"
  college-sage: "#A4B6AB"
  college-sage-pale: "#D5DED8"
  dept-pink: "#D9B8B3"
  dept-pink-pale: "#EFE0DD"
  inst-blue: "#B9C6CC"
  inst-blue-pale: "#DDE4E7"
  rose: "#8A4F4F"
  rose-pale: "#F3E4E1"
  rule: "#CFC6B9"
  white: "#FFFFFF"
typography:
  display:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "clamp(30px, 7.6vw, 40px)"
    fontWeight: 900
    lineHeight: 1.28
    letterSpacing: "0.01em"
  lede:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.8
  name-tape:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "18px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "0.12em"
  patch-title:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "21px"
    fontWeight: 900
    lineHeight: 1.35
    letterSpacing: "0.08em"
  title:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.5
  body:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "16.5px"
    fontWeight: 400
    lineHeight: 1.85
  label:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.7
rounded:
  hairline: "2px"
  cloth: "3px"
  slot: "4px"
  tab: "8px"
  round: "50%"
  shield: "14px 14px 48% 48% / 14px 14px 30% 30%"
spacing:
  "1": "8px"
  "2": "16px"
  "3": "24px"
  "4": "32px"
  "5": "40px"
  "6": "48px"
  "8": "64px"
  "10": "80px"
components:
  button-primary:
    backgroundColor: "{colors.rose}"
    textColor: "{colors.white}"
    rounded: "{rounded.cloth}"
    padding: "0 22px"
    height: "48px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.thread}"
    rounded: "{rounded.cloth}"
    padding: "0 22px"
    height: "48px"
  text-link:
    textColor: "{colors.thread}"
    height: "44px"
  name-tape:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.thread}"
    typography: "{typography.name-tape}"
    rounded: "{rounded.hairline}"
    padding: "11px 18px 10px 12px"
  tape-surface:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink}"
    rounded: "{rounded.cloth}"
    padding: "32px 32px 16px"
  patch-college:
    backgroundColor: "{colors.college-sage}"
    textColor: "{colors.thread}"
    typography: "{typography.patch-title}"
    rounded: "{rounded.shield}"
    padding: "32px 24px 48px"
  patch-dept:
    backgroundColor: "{colors.dept-pink}"
    textColor: "{colors.thread}"
    typography: "{typography.patch-title}"
    rounded: "{rounded.shield}"
    padding: "32px 24px 48px"
  patch-inst:
    backgroundColor: "{colors.inst-blue}"
    textColor: "{colors.thread}"
    typography: "{typography.patch-title}"
    rounded: "{rounded.shield}"
    padding: "32px 24px 48px"
  patch-tab:
    backgroundColor: "{colors.college-sage}"
    textColor: "{colors.thread}"
    rounded: "{rounded.tab}"
    padding: "32px 24px 24px"
  year-patch:
    backgroundColor: "{colors.college-sage}"
    textColor: "{colors.thread}"
    rounded: "{rounded.round}"
    size: "84px"
  status-stamp:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.label}"
    rounded: "{rounded.slot}"
    padding: "6px 12px"
---

# Design System: 國防醫學大學護理學院 中文站

## Overview

**Creative North Star: "The Uniform Roll"**

The only military nursing college in Taiwan speaks through its uniform's identity system. The page is a length of oatmeal twill with a fine 45° weave. Section headings are off-white name tapes sewn onto it, each carrying a short selvedge of its unit's cloth. Units are embroidered patches with a thick merrowed edge in thread colour and a dashed stitch line inset. The quick entrances are a ribbon rack. Everything reads as cloth and thread, flat and orderly, the way a uniform reads.

The system is quiet by construction. Colour is Morandi (warm ground, cool cloth) and one deep-rose thread is reserved for the single primary action in view. Depth comes only from cloth layered on cloth: a backing cut to the same outline, a rocker tab stitched above a shield, year patches strung on one thread. Nothing floats. Density is reading density: one column of about 40em inside the university's ~800px content column, with stitched ledgers (dashed rows) in place of card grids.

It is built entirely inside a hostile CMS. There is no `<style>`, `<svg>`, `section/article/details/summary` or script; the server strips them. Every rule lives as inline style generated from `tokens.py`, responsiveness comes only from Bootstrap 5.0.2 classes, icons only from FontAwesome 4.7, and type only from the system CJK stack (no `@font-face`). Confirmed rejections: the category default of photo hero + three equal cards + news list, and the College of Pharmacy page's emoji card grid.

**Key Characteristics:**
- Twill ground, name-tape headings, patch units, ribbon-rack entrances.
- Unit identity derived from one token seed: college sage, department pink, institute blue.
- One rose accent per view, reserved for the primary action.
- Flat cloth; depth by layering on the 8px grid, never by shadow.
- Stitched dashed rules as the universal divider.
- Every page ends with an honest status stamp: last updated and owner.
- Inline style only; Bootstrap 5.0.2 and FontAwesome 4.7 are the only libraries.

## Colors

A warm oatmeal ground with cool, greyed unit cloths and a single deep-rose thread; every text pair is checked for AA by `python tokens.py`.

### Primary
- **Deep Sage Thread** (thread): headings, name-tape type, patch type, merrowed patch borders, timeline and org-tree threads, text links. It is the colour of stitching and does most of the talking.
- **Deep Rose Thread** (rose): the one primary action per view (the filled button). Also the text of the draft-only editorial note, which `--final` removes.

### Secondary (unit cloths)
- **College Sage** (college-sage) with **Pale Sage** (college-sage-pale): 護理學院 patches, tape selvedges, illustration-slot ground.
- **Dusty Pink** (dept-pink) with **Pale Pink** (dept-pink-pale): 護理學系.
- **Misty Blue** (inst-blue) with **Pale Blue** (inst-blue-pale): 護理研究所.

### Neutral
- **Oatmeal Twill** (twill): the page ground, always carrying the weave (`repeating-linear-gradient(135deg, rgba(51,73,63,.045) 0 1px, transparent 1px 5px)`).
- **Name-Tape White** (tape): name tapes, reading surfaces, org-tree child lists, photo slots, status stamp, and patches for events owned by no unit.
- **Ink** (ink): body text. **Soft Ink** (ink-soft): secondary text, descriptions, stamp text.
- **Stitch Line** (rule): every dashed divider and hairline on twill.
- **Rose Pale** (rose-pale): ground of the draft-only editorial note.

### Named Rules
**The Single Seed Rule.** Unit colour is never picked per page. It comes from `UNIT` in `tokens.py` (college, dept, inst); a patch, selvedge or year patch names its unit and inherits its cloth.

**The One Rose Rule.** Rose appears on one primary action per view. Secondary actions are sage-outlined or underlined text links.

**The Checked Pair Rule.** A new foreground/background pair is added to `TEXT_PAIRS` and must pass `python tokens.py` (4.5:1) before it ships. Thread on sage is the tightest passing pair (4.55); do not lighten either.

## Typography

**Display Font:** System CJK stack: Noto Sans TC, PingFang TC, Microsoft JhengHei, Heiti TC, sans-serif
**Body Font:** the same stack
**Label/Mono Font:** none distinct

**Character:** One family, voiced through weight. Heavy 800–900 carries the uniform's lettering (display, tapes, patches); body sits at a generous 1.85 line height for Chinese reading.

### Hierarchy
- **Display** (900, clamp 30–40px, 1.28): the page's opening statement, a claim in words before any image. One per page, in thread.
- **Lede** (400, 18px, 1.8, max 34em): the sentence or two under the statement.
- **Name tape** (800, 18px, 1.2, 0.12em tracking): every section heading, set on a tape.
- **Patch title** (900, 21px, 0.08em): type embroidered on a patch. Feature-lead titles use 26px/900; FAQ questions 21px/900.
- **Title** (700, 19px, 1.5): h4 within a section, ledger row titles; route-list titles run 18px/800.
- **Body** (400, 16.5px, 1.85, max 40em).
- **Label** (400–700, 14px, 1.7): descriptions, ranks, stamp, slot captions.

### Named Rules
**The Sewn Heading Rule.** A section heading is a name tape; there is no separate eyebrow or kicker above it. The only text stitched above a patch is a rocker tab carrying the parent institution's name, as on a real shoulder patch.

**The System Stack Rule.** No web fonts. Weight and letter-spacing do the display work the platform will not let a typeface do.

## Layout

A single reading column inside the university chrome: about 800px desktop, full width on phones, padded `p-3 p-md-4`. Text measures cap at 34em (lede), 36–40em (body, lists, FAQ answers) and 44em (route lists, fact tables).

All margins and section gaps come from the 8px grid (`S` in `tokens.py`). Name tapes open sections with 64px above and 24px below; blocks close on 24–32px; the status stamp sits 64px below the last block.

Two-column splits use Bootstrap `row` + `col-md-N` with a 32px gutter and 24px row gap, stacking on phones (7/5 for statement + patch, 3/9 or 4/8 for photo + text). Everything that wraps by content, not by column, uses intrinsic flex: the ribbon rack (`flex: 1 1 104px`), org-tree branches (`flex: 1 1 180px`), action rows (`flex-wrap`, 16px/24px gap). The site's Bootstrap ordering makes auto `.col-md` unreliable, so do not use it. Visibility switches only through `d-none d-md-block` / `d-md-none`.

## Elevation & Depth

Flat. There is no `box-shadow`, glow, or decorative gradient anywhere. Depth is cloth layered on cloth: a patch's backing cut to the same outline 10px larger on every side with a dashed edge; a rocker tab overlapping the top of a shield by 10px; year patches sitting on the thread that runs through them. The only gradients are materials: the twill weave and ribbon stripes.

### Named Rules
**The Sewn, Not Floating Rule.** When something needs to sit forward, give it another layer of cloth behind it. Never a shadow.

**The One Thread Rule.** History is year patches strung on a single 3px thread, oldest first. Entries do not physically overlap each other; entries of real length cannot.

## Shapes

Three silhouettes carry identity: the shield (14px shoulders tapering to a 48%/30% rounded base), the round patch (50%, used for year patches and ledger marks), and the tab (8px, org tree). Patches always wear a thick thread border (6px on shields and tabs, 5px on year patches, 4px on ledger marks) and a dashed inset stitch (outline, negative offset). Everything else is nearly square cloth: 2px on name tapes, 3px on reading surfaces, buttons and photo slots, 4px on illustration slots and the stamp. Dividers are 1.5px dashed stitch lines in rule colour; threads (timeline, org tree) are solid 3px in thread.

## Components

### Buttons
Tactile, square-cut, sewn on.
- **Shape:** near-square (3px), 48px tall, 2px border.
- **Primary:** rose fill, white 16px/800 label with 0.06em tracking and a trailing `fa-long-arrow-right`. One per view.
- **Secondary:** transparent with a 2px thread border and thread label.
- **Text link:** thread, 700, underlined with 5px offset and 1.5px thickness, trailing `fa-angle-right`, 44px minimum target.
- **Hover / Focus:** inline style cannot carry state; the browser default focus ring stands. Do not remove it.

### Name Tape
The section heading. Tape-white cloth, 1px rule border, a dashed inset stitch, and a 12×20px selvedge in the unit's cloth before the text.

### Patches
- **Shield:** unit entrances and the home college patch; may carry an illustration slot, a sub-line, a `fa-arrow-circle-right` when linked, a rocker tab, and a backing cloth.
- **Tab:** org-tree nodes, with child lists on tape below.
- **Round ledger mark:** 60px, a single CJK character from the title, leading each row of a feature list.

### Ribbon Rack
Quick entrances as ribbons butted edge to edge: 40px striped bars with a 2px thread border, each labelled beneath in 15.5px/800 thread. Stripe patterns are drawn from the palette and cycle; the rack wraps intrinsically (3+2 on phones).

### Stitched Ledgers
Route lists, feature lists, rosters, FAQs and fact tables are rows separated by dashed stitch lines, never cards. Route rows are at least 56px tall with a trailing chevron. FAQs are fully expanded (no collapse is available) and long ones get a numbered jump list.

### Timeline
Year patches (84px round, unit cloth or tape) on one vertical thread, oldest first, title and text beside each.

### Status Stamp
Closes every page: dashed rule border on tape, `fa-calendar-check-o`, "最後更新 {date}｜維護：{owner}".

### Placeholders
Illustration slots (unit pale cloth, dashed, `fa-pencil`) reserve space for recoloured CocoMaterial art; photo slots (tape, dashed, `fa-camera`) reserve space for photographs. Both carry `role="img"` and a label.

### Draft Marks (pre-launch only)
待確認 chips and 編輯備註 notes mark unconfirmed copy for content owners. `python build.py --final` removes them; they are never part of the published system.

## Do's and Don'ts

### Do:
- **Do** generate every colour, space and type value from `tokens.py`; add a new text pair to `TEXT_PAIRS` and run `python tokens.py`.
- **Do** open each section with a name tape carrying its unit's selvedge.
- **Do** give each unit its own cloth: college sage, department pink, institute blue.
- **Do** keep one rose primary action per view; everything else is thread.
- **Do** separate rows with 1.5px dashed stitch lines in the rule colour.
- **Do** wrap content-driven rows with intrinsic flex (`flex: 1 1 Npx`) and split columns with explicit `col-md-N`.
- **Do** end every page with the status stamp naming the date and owner.
- **Do** run `python build.py`; it fails any page containing `<style>`, `<svg>`, `<section>`, `<article>`, `<details>`, `<summary>` or `<script>`.

### Don't:
- **Don't** use drop shadows, glows, or decorative gradients; depth is layered cloth.
- **Don't** lay routes out as equal card grids or use emoji as icons; use stitched ledgers and FontAwesome 4.7.
- **Don't** put an eyebrow or kicker above a heading; the name tape is the heading.
- **Don't** load web fonts or rely on `<style>`, `<svg>`, collapsibles or scripts; the CMS strips them.
- **Don't** use auto `.col-md`; the site's Bootstrap ordering breaks it.
- **Don't** overlap timeline entries; string them on one thread.
- **Don't** ship with draft marks; publish from `python build.py --final`.
