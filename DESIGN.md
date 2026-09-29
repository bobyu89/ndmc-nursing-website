---
name: 國防醫學大學 護理學院・護理學系・護理研究所（中英文六站）
description: The uniform's identity system sewn onto Morandi twill across six sites; every unit a patch, every section a name tape, every page closed by a public stamp.
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
  feature-lead:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "26px"
    fontWeight: 900
    lineHeight: 1.35
  name-tape:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "25.5px"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.1em"
  mark-glyph:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "22px"
    fontWeight: 900
    lineHeight: 1
  faq-question:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "21px"
    fontWeight: 900
    lineHeight: 1.45
  patch-title:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "clamp(16px, 4.6vw, 21px)"
    fontWeight: 900
    lineHeight: 1.35
    letterSpacing: "0.06em"
  headline:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "20.5px"
    fontWeight: 800
    lineHeight: 1.45
  patch-arrow:
    fontSize: "20px"
    lineHeight: 1
  roster-name:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "19px"
    fontWeight: 900
    lineHeight: 1.9
  lede:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.8
  route-title:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "18px"
    fontWeight: 800
    lineHeight: 1.85
    letterSpacing: "0.04em"
  year:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "17px"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0.04em"
  body:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "16.5px"
    fontWeight: 400
    lineHeight: 1.85
  button-label:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "16px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "0.06em"
  ribbon-label:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "15.5px"
    fontWeight: 800
    lineHeight: 1.85
    letterSpacing: "0.06em"
  rocker:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "15px"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.2em"
  label:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.7
  rocker-latin:
    fontFamily: "\"Noto Sans TC\", \"PingFang TC\", \"Microsoft JhengHei\", \"Heiti TC\", sans-serif"
    fontSize: "13px"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.04em"
rounded:
  selvedge: "1px"
  hairline: "2px"
  cloth: "3px"
  slot: "4px"
  tab: "8px"
  shield-shoulder: "14px"
  shield: "14px 14px 48% 48% / 14px 14px 30% 30%"
  rocker-arch: "50% 50% 8px 8px / 100% 100% 8px 8px"
  round: "50%"
spacing:
  "1": "8px"
  "2": "16px"
  "3": "24px"
  "4": "32px"
  "5": "40px"
  "6": "48px"
  "8": "64px"
  "10": "80px"
  stitch-6: "6px"
  layer-10: "10px"
  tape-12: "12px"
components:
  button-primary:
    backgroundColor: "{colors.rose}"
    textColor: "{colors.white}"
    typography: "{typography.button-label}"
    rounded: "{rounded.cloth}"
    padding: "0 22px"
    height: "48px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.thread}"
    typography: "{typography.button-label}"
    rounded: "{rounded.cloth}"
    padding: "0 22px"
    height: "48px"
  text-link:
    textColor: "{colors.thread}"
    padding: "12px 0"
  name-tape:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.thread}"
    typography: "{typography.name-tape}"
    rounded: "{rounded.hairline}"
    padding: "11px 18px 10px 12px"
  selvedge-college:
    backgroundColor: "{colors.college-sage}"
    rounded: "{rounded.selvedge}"
    width: "14px"
    height: "26px"
  selvedge-dept:
    backgroundColor: "{colors.dept-pink}"
    rounded: "{rounded.selvedge}"
    width: "14px"
    height: "26px"
  selvedge-inst:
    backgroundColor: "{colors.inst-blue}"
    rounded: "{rounded.selvedge}"
    width: "14px"
    height: "26px"
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
  patch-backing:
    backgroundColor: "{colors.tape}"
    rounded: "{rounded.shield}"
  rocker-tab:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.thread}"
    typography: "{typography.rocker}"
    rounded: "{rounded.rocker-arch}"
    padding: "12px 8px 14px"
    width: "84%"
  patch-tab:
    backgroundColor: "{colors.college-sage}"
    textColor: "{colors.thread}"
    typography: "{typography.patch-title}"
    rounded: "{rounded.tab}"
    padding: "32px 8px 24px"
  feature-mark:
    backgroundColor: "{colors.college-sage}"
    textColor: "{colors.thread}"
    typography: "{typography.mark-glyph}"
    rounded: "{rounded.round}"
    size: "60px"
  year-patch:
    backgroundColor: "{colors.college-sage}"
    textColor: "{colors.thread}"
    typography: "{typography.year}"
    rounded: "{rounded.round}"
    size: "84px"
  ribbon:
    textColor: "{colors.thread}"
    typography: "{typography.ribbon-label}"
    height: "40px"
  illustration-slot:
    backgroundColor: "{colors.college-sage-pale}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.label}"
    rounded: "{rounded.slot}"
    padding: "16px"
  photo-slot:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.label}"
    rounded: "{rounded.cloth}"
    padding: "16px"
  status-stamp:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.label}"
    rounded: "{rounded.slot}"
    padding: "6px 12px"
---

# Design System: 國防醫學大學 護理學院・護理學系・護理研究所（中英文六站）

## Overview

**Creative North Star: "The Uniform Roll"**

The only military nursing college in Taiwan speaks through its uniform's identity system, now across six sites: the college, the department and the institute, each in Chinese and English. The page is a length of oatmeal twill with a fine 45° weave. Section headings are off-white name tapes sewn onto it, each carrying a short selvedge of the site's own unit cloth. Units are embroidered patches with a thick merrowed edge in thread colour and a dashed stitch line inset. The quick entrances are a ribbon rack. Everything reads as cloth and thread, flat and orderly, the way a uniform reads.

The system is quiet by construction. Colour is Morandi (warm ground, cool cloth) and one deep-rose thread is reserved for the single primary action in view. Depth comes only from cloth layered on cloth: a backing cut to the patch's own outline, a rocker tab stitched above a shield, year patches strung on one thread. Nothing floats. Density is reading density: one column of about 40em inside the university's ~800px content column, with stitched ledgers (dashed rows) in place of card grids. Two build-time switches carry the world across sites without forking it: the site's unit sets the default cloth, the site's language sets tracking and every fixed label.

It is built entirely inside a hostile CMS. There is no `<style>`, `<svg>`, `section/article/details/summary` or script; the server strips them, and its save filter rewrites `<i>` to `<em>` and drops `aria-*` and `role`. Every rule lives as inline style generated from `tokens.py` and `components.py`, responsiveness comes only from Bootstrap 5.0.2 classes, icons only from FontAwesome 4.7, and type only from the system CJK stack (no `@font-face`). Confirmed rejections: the category default of photo hero + three equal cards + news list, and the College of Pharmacy page's emoji card grid.

**Key Characteristics:**
- Twill ground, name-tape headings, patch units, ribbon-rack entrances.
- Unit identity derived from one token seed: college sage, department pink, institute blue; each site defaults to its own cloth.
- One rose accent per view, reserved for the primary action.
- Flat cloth; depth by layering on the 8px grid, never by shadow.
- Stitched dashed rules as the universal divider.
- Language-aware: CJK tracking opens to .04–.1em, Latin closes to .01em; every fixed label switches with the site.
- Every page ends with a public status stamp: last updated and the maintaining unit.
- Inline style only; Bootstrap 5.0.2 and FontAwesome 4.7 are the only libraries.

## Colors

A warm oatmeal ground with cool, greyed unit cloths and a single deep-rose thread; every text pair is checked for AA by `python tokens.py`.

### Primary
- **Deep Sage Thread** (thread): headings, name-tape type, patch type, merrowed patch borders, timeline and org-tree threads, text links, and bare links themed by the build. It is the colour of stitching and does most of the talking.
- **Deep Rose Thread** (rose): the one primary action per view (the filled button). Also the text of the draft-only editorial note, which `--final` removes.

### Secondary (unit cloths)
- **College Sage** (college-sage) with **Pale Sage** (college-sage-pale): 護理學院 / College of Nursing.
- **Dusty Pink** (dept-pink) with **Pale Pink** (dept-pink-pale): 護理學系 / Department of Nursing.
- **Misty Blue** (inst-blue) with **Pale Blue** (inst-blue-pale): 護理研究所 / Graduate Institute of Nursing.

### Neutral
- **Oatmeal Twill** (twill): the page ground, always carrying the weave (see the sidecar's `twill-weave` material).
- **Name-Tape White** (tape): name tapes, rocker tabs, patch backings, reading surfaces, org-tree child lists, photo slots, the status stamp, and year patches for events owned by no unit.
- **Ink** (ink): body text. **Soft Ink** (ink-soft): secondary text, descriptions, stamp text.
- **Stitch Line** (rule): every dashed divider and hairline on twill.
- **Rose Pale** (rose-pale): ground of the draft-only editorial note.

### Named Rules
**The Single Seed Rule.** Unit colour is never picked per page. It comes from `UNIT` in `tokens.py`; the build sets `SITE_UNIT` from each page's `META["site"]`, and name-tape selvedges and the org-tree head take that site's cloth by default (college sage, department pink, institute blue). A patch, mark or year patch that names another unit wears that unit's cloth.

**The One Rose Rule.** Rose appears on one primary action per view. Secondary actions are thread-outlined buttons or underlined text links.

**The Checked Pair Rule.** A new foreground/background pair is added to `TEXT_PAIRS` and must pass `python tokens.py` (4.5:1) before it ships. Thread on sage is the tightest passing pair (4.55); do not lighten either.

## Typography

**Display Font:** System CJK stack: Noto Sans TC, PingFang TC, Microsoft JhengHei, Heiti TC, sans-serif
**Body Font:** the same stack, for Chinese and English sites alike
**Label/Mono Font:** none distinct

**Character:** One family, voiced through weight. Heavy 800–900 carries the uniform's lettering (display, tapes, patches, marks); body sits at a generous 1.85 line height for Chinese reading.

### Hierarchy
- **Display** (900, clamp 30–40px, 1.28, .01em): the page's opening statement, a claim in words before any image. One per page, in thread, `text-wrap: balance`, split into phrase-level inline-block spans so lines break only between phrases.
- **Feature lead** (900, 26px, 1.35): the title beside the one leading feature patch.
- **Name tape** (900, 25.5px, 1.2, .1em CJK / .01em Latin): every section heading, set on a tape.
- **Mark glyph** (900, 22px): the single character in a feature-list mark disc; the same 22px sizes route-row chevrons.
- **FAQ question** (900, 21px, 1.45).
- **Patch title** (900, clamp 16–21px, 1.35, .06em CJK, `word-break: keep-all`): type embroidered on shields and tabs.
- **Headline** (800, 20.5px, 1.45): h4 sub-headings inside sections, feature-list, timeline and ledger row titles.
- **Patch arrow** (20px): the `fa-arrow-circle-right` on a linked patch.
- **Roster name** (900, 19px).
- **Lede** (400, 18px, 1.8, max 34em) and **route title** (800, 18px, .04em).
- **Year** (900, 17px, .04em): the year on a year patch.
- **Body** (400, 16.5px, 1.85, max 40em).
- **Button label** (800, 16px, .06em CJK).
- **Ribbon label** (800, 15.5px, .06em CJK).
- **Rocker** (900, 15px, .2em) for CJK text; **rocker Latin** (900, 13px, .04em) when the rocker text is ASCII.
- **Label** (400–700, 14px, 1.7): descriptions, ranks, stamp, slot captions, draft chips, org-tree children.

### Named Rules
**The Sewn Heading Rule.** A section heading is a name tape; there is no separate eyebrow or kicker above it. The only text stitched above a patch is a rocker tab carrying the parent institution's name, as on a real shoulder patch.

**The Script-Aware Tracking Rule.** Tracking follows `SITE_LANG`: CJK sites keep the open values above (.04em route titles and years, .06em buttons, ribbons and patch titles, .1em name tapes); English sites set every one of them to .01em. The rocker decides by its own text: ASCII drops to 13px/.04em.

**The Phrase Break Rule.** A display claim never breaks mid-phrase. The statement is cut after ，、：； and at an author hint ｜ (removed from output); fragments under four characters merge forward.

**The System Stack Constraint.** No web fonts are available on this CMS. Weight and letter-spacing do the display work the platform will not let a typeface do; this is a platform limit, not a stylistic preference, and lifts if the CMS ever allows `@font-face`.

## Layout

A single reading column inside the university chrome: about 800px desktop, full width on phones, padded `p-3 p-md-4`. Text measures cap at 34em (lede), 36–40em (body, lists, timeline text, FAQ answers) and 44em (route lists, fact tables).

All margins and section gaps come from the 8px grid (`S` in `tokens.py`). Name tapes open sections with 64px above and 24px below; blocks close on 24–32px; the status stamp sits 64px below the last block. Three sub-grid steps recur inside components only: 6px (sub-line and title gaps), 10px (backing inset, rocker overlap, button icon gap) and 12px (name-tape selvedge gap, rocker padding, text-link hit padding).

Two-column splits use Bootstrap `row` + `col-md-N` with a 32px gutter and 24px row gap, stacking on phones (7/5 for statement + patch or feature lead, 3/9 or 4/8 for photo + text). Content-driven rows use intrinsic flex: the ribbon rack (`flex: 1 1 140px` for four ribbons so they wrap 2+2, `1 1 104px` otherwise so five wrap 3+2), action rows (`flex-wrap`, 16px/24px gap). Org-tree peers sit on one row from md up (`d-md-flex`, each branch `flex: 1 1 0`, 16px gap) and stack on phones. The site's Bootstrap ordering makes auto `.col-md` unreliable, so do not use it. Visibility switches only through `d-none d-md-block` / `d-md-none`.

Fact tables keep short labels on one line: a label whose visual width is 8 or less (CJK counts 1, ASCII counts half) is `nowrap`; a longer label gets 40% of the table.

## Elevation & Depth

Flat. There is no `box-shadow`, glow, or decorative gradient anywhere. Depth is cloth layered on cloth: a backing cut to the patch's own outline (same radius), 10px larger on every side with a dashed edge; a rocker tab overlapping the top of a shield by 10px; year patches sitting on the thread that runs through them, each stacked one z-index above the last. The only gradients are materials: the twill weave and ribbon stripes.

### Named Rules
**The Sewn, Not Floating Rule.** When something needs to sit forward, give it another layer of cloth behind it. Never a shadow.

**The One Thread Rule.** History is year patches strung on a single 3px thread, oldest first, each in the cloth of the unit the event belongs to (tape when it belongs to none). Entries do not physically overlap each other; entries of real length cannot.

## Shapes

Four silhouettes carry identity. The **shield** has 14px shoulders tapering to a rounded base (`rounded.shield`). The **round patch** (50%) is used for year patches and feature-list mark discs. The **tab** (8px) is the org-tree node. The **rocker arch** (`rounded.rocker-arch`) is a half-ellipse top on 8px feet, sewn above a shield. Patches always wear a thick thread border (6px on shields and tabs, 5px on rockers and year patches, 4px on mark discs) and a dashed inset stitch (outline, negative offset). Everything else is nearly square cloth: 1px on name-tape selvedges, 2px on name tapes, 3px on reading surfaces, buttons, photo slots, org-tree child lists, draft chips and notes, 4px on illustration slots and the stamp. Dividers are 1.5px dashed stitch lines in rule colour; threads (timeline, org tree) are solid 3px in thread.

## Components

### Buttons
Tactile, square-cut, sewn on.
- **Shape:** near-square (3px), 48px tall, 2px border.
- **Primary:** rose fill, white button label, trailing `fa-long-arrow-right`. One per view.
- **Secondary:** transparent with a 2px thread border and thread label.
- **Text link:** inline thread 700, underlined with 5px offset and 1.5px thickness, trailing `fa-angle-right`, 12px vertical padding at line height 1.9 for its hit area. Fixed labels follow the site language: 了解更多 / Learn more, 前往 / Explore, 個人研究頁 / Research page.
- **Bare links:** any `<a>` a page writes without a style is themed by the build to thread, 700, underlined at 4px offset, never the chrome's default blue.
- **Hover / Focus:** inline style cannot carry state; the browser default focus ring stands. Do not remove it.

### Name Tape
The section heading. Tape-white cloth, 1px rule border, a dashed inset stitch, and a 14×26px selvedge before the text in the site's unit cloth unless a unit is named.

### Patches
- **Shield:** unit entrances and the home patch; may carry an illustration slot, a sub-line (14px/600), a patch arrow when linked, a rocker tab, and a backing cloth (`backing=` a colour, normally tape) cut to the shield's own outline.
- **Rocker tab:** 84% of the shield's width, tape cloth, 5px thread border, dashed inset, overlapping the shield by 10px. It carries the parent institution's name.
- **Tab:** org-tree nodes, with child lists on tape below.
- **Mark disc:** 60px round in the item's unit cloth, 4px thread border, tape-coloured dashed inset; carries one character, the first of the title unless a mark is given (English sites pass a mark).

### Ribbon Rack
Quick entrances as ribbons butted edge to edge: 40px striped bars with a 2px thread border, each labelled beneath. Stripe patterns are drawn from the palette and cycle through six. Four ribbons wrap 2+2 on phones; five wrap 3+2.

### Stitched Ledgers
Route lists, feature lists, rosters, FAQs and fact tables are rows separated by dashed stitch lines, never cards. Route rows are at least 56px tall with a trailing chevron. FAQs are fully expanded (no collapse is available) and long ones get a numbered jump list.

### Timeline
Year patches (84px round) on one vertical 3px thread at 40px from the left, oldest first, title and text beside each. Every event names its unit and wears its cloth; unowned events wear tape.

### Org Tree
A head tab in the site's cloth, a 3px drop, then one horizontal bar from md up whose side margins are `(100% − (n−1)·16px) / 2n`, so it runs from the first branch's centre to the last's across the gaps. Each branch drops 24px to its tab. On phones the bar and drop hide and one vertical thread runs through the centre of every branch.

### Status Stamp
Closes every page: dashed rule border on tape, `fa-calendar-check-o`, "最後更新 {date}　｜　維護單位：{unit}" or "Last updated {date} · Maintained by {unit}". It names the public unit of the site (護理學院 / 護理學系 / 護理研究所 and their English names), never an internal contact; the internal owner stays in each page's `META` for editors.

### Placeholders
Illustration slots (unit pale cloth, dashed, `fa-pencil`, 插圖 / Illustration) reserve space for recoloured CocoMaterial art; photo slots (tape, dashed, `fa-camera`, 照片 / Photo) reserve space for photographs. Their `role` and `aria-label` are dropped by the CMS save filter, so the visible caption is the only label.

### Draft Marks (pre-launch only)
待確認 chips and 編輯備註 notes mark unconfirmed copy for content owners. `python build.py --final` removes them and stamps the build date into every status stamp; they are never part of the published system.

## Do's and Don'ts

### Do:
- **Do** generate every colour, space and type value from `tokens.py` and `components.py`; add a new text pair to `TEXT_PAIRS` and run `python tokens.py`.
- **Do** open each section with a name tape; let its selvedge take the site's cloth unless the section belongs to another unit.
- **Do** give each unit its own cloth: college sage, department pink, institute blue.
- **Do** keep one rose primary action per view; everything else is thread.
- **Do** separate rows with 1.5px dashed stitch lines in the rule colour.
- **Do** route every letter-spacing through the language switch so English sites track at .01em.
- **Do** wrap content-driven rows with intrinsic flex (`flex: 1 1 Npx`) and split columns with explicit `col-md-N`.
- **Do** end every page with the status stamp naming the date and the public maintaining unit.
- **Do** run `python build.py`; it applies the CMS save filter, themes bare links, and fails any page containing `<style>`, `<svg>`, `<section>`, `<article>`, `<details>`, `<summary>` or `<script>`.

### Don't:
- **Don't** use drop shadows, glows, or decorative gradients; depth is layered cloth.
- **Don't** lay routes out as equal card grids or use emoji as icons; use stitched ledgers and FontAwesome 4.7.
- **Don't** put an eyebrow or kicker above a heading; the name tape is the heading.
- **Don't** load web fonts or rely on `<style>`, `<svg>`, collapsibles or scripts; the CMS strips them.
- **Don't** put an internal contact on the public stamp; owners stay in `META`.
- **Don't** rely on `aria-*` or `role` for meaning; the CMS drops them, so the visible text must carry it.
- **Don't** use auto `.col-md`; the site's Bootstrap ordering breaks it.
- **Don't** overlap timeline entries; string them on one thread.
- **Don't** ship with draft marks; publish from `python build.py --final`.
