---
name: ndmc-nursing-cms
description: How to operate the National Defense Medical University (國防醫學大學) departmental website backend/CMS at eipwndmc.ndmctsgh.edu.tw/forms/act/actp099_backstage.aspx, specifically for the 護理學院/護理學系/護理研究所 (School of Nursing) websites. Use this whenever the user asks to edit, update, add, or take down content on the 護理學院 (or 護理學系/護理研究所) website — news posts (最新消息), downloadable files/forms (表單下載 nodes like 校友專區/下載專區/教師資格審查專區), static page text (html編輯功能 pages like 師資介紹/認識本院/軍護簡介/學生專區), menu structure changes, or visibility/enable toggles. Also use when the user mentions this backstage URL, "後台", "護理學院網站", or asks what format to send material in for a website update. This is a real, live, public-facing university website — always get explicit user confirmation before submitting any add/delete/enable-toggle/save action.
---

# NDMC 護理學院網站後台管理系統

Backend CMS at `https://eipwndmc.ndmctsgh.edu.tw/forms/act/actp099_backstage.aspx` for managing the National Defense Medical University (國防醫學大學) School of Nursing website content. Legacy ASP.NET WebForms app, tree-structured page/menu editor.

## Before anything else: login

Login requires the user's personal Office365 account + a numeric CAPTCHA. **Never enter credentials on the user's behalf** — this is a prohibited action regardless of what the user says. Open the login page in the Browser pane, ask the user to log in themselves (in that same pane, since it's the only browser surface you can both see), then confirm with them before proceeding.

Session auto-logs-out after **30 minutes of inactivity** — the header shows a live countdown ("登出倒數"). If a page read looks like it reverted to the login form, the session expired; ask the user to log in again.

## Who can manage what

The logged-in account's permissions live under the **權限管理** toolbar button → **負責網頁** tab: it lists which unit(s) (by 代號, e.g. T04=護理學院, T20=護理學系, T21=護理研究所) the account has full rights over. The **負責網頁** dropdown at the top switches which of those units' node tree you're viewing/editing. The **使用者** tab under 權限管理 is where additional editors would be added (empty by default — ask the user if they want to add someone rather than guessing).

## The node tree (left panel)

The entire site menu is one tree. Each row is a "node" (a page or menu entry) with:

| Column | Meaning |
|---|---|
| L | Depth level (1 = top-level unit page, 2 = its menu items, deeper = sub-pages) |
| 鎖 (lock) | Prevents accidental edits/deletion |
| 選單 | Checked = appears in the site's visible navigation menu |
| 啟用 | Checked = page is publicly live. **Unchecking this is the safe way to "take a page down" — prefer it over deleting** |
| 模組 | Icon showing which content-editor type this node opens (see below) |
| 名稱 | Menu label |

Each row has inline action icons: ➕ 新增下一層節點 (add child node), ❌ 刪除 (delete, asks for confirmation), ⬆️⬇️ 排序上移/下移 (reorder). **Clicking the 模組 icon itself** (not the name text) opens that node's content editor in the right panel.

## Node-level settings (top of every content editor)

Regardless of module type, every node's editor starts with the same block of metadata fields:

- **網址伴號** — the node's live front-end URL (read-only, e.g. `https://wwwndmc.ndmutsgh.edu.tw/news/191/100010/1628`)
- **名稱** — menu label text
- **主題分類 / 施政分類 / 服務分類** — three government-web-standard taxonomy dropdowns (required by NDMC's compliance rules; when unsure what to pick, match a sibling node of the same type, or ask the user)
- **登入後瀏覽 / 選單 / 啟用** checkboxes, **排序** (sort order number)
- **連結設定** (連結方式: 超連結 etc.) + **連結方式** (開新視窗/目前視窗/直接連結) + **連結網址** — only relevant for pure link-out nodes (e.g. 杏網相連, 國防護理Facebook)
- **備註** — internal note field
- **更新時間 / 最後更新者** — auto-filled, read-only

## Content modules (bottom half of the editor, varies by type)

The 模組 icon tells you which editor loads below the metadata block. Confirmed by direct testing:

### 最新消息 (News/announcement list) — e.g. the "最新消息" node
A list of posts, each independently editable. Columns: 標題 (title), 資料夾, 啟用, 置頂 (pin to top), 發佈日 (publish date), 截止日 (expiry date), 發佈時間. Add via the green 新增 button above the list; edit/delete via the pencil/✕ icons per row.

**⚠️ Important quirk: every day at 3:00 AM the system automatically disables and deletes attachments for any post past its 截止日.** If the user wants a post to stay up indefinitely, either leave 截止日 blank or set it far in the future — confirm with them which they want.

**Format needed from the user for a new post:** 標題 (title text), 內文/公告內容, 發佈日, 截止日 (or "no expiry"), whether it should be 置頂, and any attachment files.

### 表單下載 (File/form download) — e.g. 校友專區, 下載專區, 教師資格審查專區, 教學設備暨教室借用專區
A list of uploaded files. Columns: 編號, 啟用, 排序, 檔案名稱, 替代格式, 更新日期, 下載次數.

**⚠️ Important quirk: Office files (docx/xlsx/pptx) must have their ODF-format counterpart (.odt/.ods/.odp) uploaded too — the system auto-converts if you upload the ODF version first.** If the user only has a .docx, tell them the system will handle the conversion — no need for them to manually create the .odt themselves.

**Format needed from the user:** the file itself (any common office/PDF format is fine), the display name/label for it, and whether it replaces an existing file or is new.

### html編輯功能 (Rich-text static page) — e.g. 軍護簡介, 師資介紹, 認識本院, 學生專區
DevExpress ASPxHtmlEditor inside an iframe (`#ASPxSplitter1_1i1i1_CC` → `forms/tpl/tpl_Html.aspx`). Client object `hle_templete` exposes `SetHtml(html)` / `GetHtml()` — the reliable way to inject prepared HTML from the Browser pane is `javascript_tool` on the iframe's `contentWindow`, then click the `#btn_save` (內文存檔) button by coordinate. Other buttons there: 內文刪除, 檔案管理, RWD修正 (untested — avoid), image/file upload inputs.

**Server-side filter on save (verified 2026-09-14 on test node 7696):** keeps inline `style` (any property, incl. flex/gap/gradient/aspect-ratio/box-shadow/position:fixed), `class`, `id`, `h2/div/p/span/a/ul/li/table/img` (external URLs and `data:` URIs, `alt`). **Strips `<style>` and `<svg>` entirely; strips `<section>/<article>/<details>/<summary>` tags but keeps their text; converts `<i>` to `<em>` (FontAwesome still works by class); deletes every `aria-*` and `role` attribute (verified 2026-09-29).** The public site loads Bootstrap 5.0.2, so grid/utility classes (`row`, `col-md-*`, `d-none d-md-block`, `order-md-*`) work for responsiveness. Full matrix in `~/ndmc-nursing-website/docs/superpowers/specs/2026-09-14-nursing-site-design-system.md` §2.3.

**Format needed from the user:** for plain edits, text is enough. For the redesigned pages, the HTML is generated by the Python build in `~/ndmc-nursing-website` (`dist/*.html`) — paste that output, never hand-edit inside the WYSIWYG.

**Test node:** `__測試節點（勿啟用）` (id 7696; its edit icon is `#ASPxSplitter1_tl_master_tDC5_7696_imb_edit`; the Browser pane runs at devicePixelRatio 1.2, so multiply CSS coordinates by 1.2 before clicking; the editor iframe can reset to homepage.aspx on its own — inject and save in one go) under 護理學院, 啟用/選單 both off — safe scratch space for paste tests. Don't delete it. Disabled nodes redirect to the university home page, so they cannot be previewed on the front end.

### Other module types seen but not yet explored in detail
單位介紹, 學術特色, 學術成果, 學術活動, 相關連結 — each likely a specialised variant of the list/rich-text pattern above (e.g. 學術成果 is probably a publication list). **Open the specific node and look at its editor before assuming its format** — don't guess field names from this doc alone for these types.

## Other toolbar tools (not yet fully verified this session)
- **首頁圖片輪播** — manages the homepage image carousel/slideshow
- **瀏覽統計** — site traffic stats
- **節點搜尋** — jump to a node by its numeric 網址代號

These buttons didn't render their popup in this Browser-pane test session — likely the same CSP/AJAX quirk below. Try them fresh (ideally right after a 畫面重整 refresh) when actually needed.

## Known technical quirk: AJAX panel switching in the sandboxed Browser

This site uses ASP.NET UpdatePanel-style partial postbacks with nonce-based inline scripts. In Claude's sandboxed Browser pane, **only the first one or two module-icon clicks after a page load/refresh reliably swap the right-hand editor panel** — later clicks in the same session sometimes silently no-op (right panel doesn't change, or shows the previous node's data). If a click on a module icon doesn't change the visible content, click the **畫面重整** (refresh) toolbar icon first, then retry. This may be specific to this sandboxed browser's stricter CSP enforcement rather than a problem for the user's own regular browser.

## Before submitting any change

This is a live, public university website. Before clicking any 新增/儲存/確定/刪除 that commits a change:
1. Show the user exactly what will be added/changed/removed.
2. Get explicit confirmation in chat.
3. After saving, re-read the page to confirm the change actually took (given the AJAX quirk above, a "successful" click isn't always trustworthy at face value).

Never take a page down (啟用 off) or delete a node without confirming — prefer disabling over deleting since it's reversible.
