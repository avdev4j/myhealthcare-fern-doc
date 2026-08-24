---
name: infographics
description: Create consistent, on-brand infographics using the Postman brand system. Use this skill whenever the user asks to visualize data, stats, comparisons, processes, timelines, flows, or any information that would benefit from a visual layout. Trigger on phrases like "make an infographic", "visualize this", "show this as a chart", "create a diagram", "compare these", "illustrate this process", or any request to turn structured information into a visual. Always use this skill even for quick one-off visuals — consistency matters.
---

# Infographics Skill

Creates polished, on-brand infographics rendered inline as SVG or HTML. Always defaults to **light background with dark text** for maximum readability.

---

## Brand System

### Colors — Official Postman 2026 Brand Color System

**Core brand colors:**
```
Postman Orange:  #FF6C37   (hero color — primary accent, use with intention)
Purple:          #7A24F0   (AI/innovation — core brand color)
White:           #FFFFFF   (canvas, clean surfaces)
Black:           #000000   (borders, typography, grounding)
```

**Orange family (O:)** — extends the hero color:
```
O:00 Bright Orange: #FFFBF7   (box fills, lightest tint)
O:10:               #FFF2EB   (box fills)
O:20 Apricot:       #FFD7C7   (box fills, soft)
O:30:               #FFBCA3   (box fills, medium)
O:40 Carrot:        #FFA17F   (borders, accents)
O:50:               #FF875B   (borders, accents)
O:60 Postman Orange:#FF6C37   (full accent — hero)
O:70:               #E0531F   (dark accent, icon strokes)
O:80:               #B03C12   (dark shade)
```

**Purple family (P:)** — AI/innovation:
```
P:00 Bright Purple: #FAF7FF   (box fills, lightest)
P:10:               #F3EBFF   (box fills)
P:20 Blog Purple:   #E3D2FA   (box fills, soft)
P:30:               #CDAFF7   (box fills, medium)
P:40 Soft Purple:   #B387F5   (borders, accents)
P:50:               #9455F2   (borders, accents)
P:60 Purple:        #7A24F0   (full accent — AI identity)
P:70:               #5E1DC0   (dark accent)
P:80 Space Purple:  #491591   (dark shade)
```

**Blue family (B:)** — balance and contrast:
```
B:10:               #E5F4FF   (box fills, lightest)
B:20 Soft Blue:     #CCE7FF   (box fills)
B:30:               #ABD6FF   (box fills)
B:40 Sky Blue:      #80C1FF   (borders, accents)
B:50:               #42A4FF   (borders, accents)
B:60 Azure:         #198CF7   (full accent)
B:70:               #026DD2   (dark accent)
B:80 Cobalt:        #0352A1   (dark shade)
```

**Yellow family (Y:)** — warmth and energy:
```
Y:10:               #FFF9E0   (box fills, lightest)
Y:20:               #FFF0BD   (box fills)
Y:30:               #FFE396   (box fills)
Y:40 Elemental Yellow: #FFD875 (borders, accents)
Y:50:               #FFC642   (borders, accents)
Y:60 Gold:          #FFA90A   (full accent)
Y:70:               #BF7600   (dark accent)
```

**Magenta family (M:)** — analogous bridge between orange and purple:
```
M:10:               #FEF1FD   (box fills, lightest)
M:30:               #FFCCFC   (box fills)
M:60 Core Pink:     #F37FFE   (full accent)
M:80:               #993A90   (dark accent)
```

**Neutrals (N:):**
```
N:00 Bright Gray:   #F9F8F7   (background, subtle fills)
N:05:               #E6E6E6   (dividers)
N:20 Silver:        #CFCFCF   (muted fills)
N:40 Smoke:         #A1A1A1   (muted text, captions)
N:60 Stone:         #737373   (secondary text)
N:80 Graphite:      #454545   (dark fills)
```

**Accent colors (legacy, approved for use):**
```
Flora Green:        #A4EEC4   (box fills — green)
Blog BG Teal:       #D0F9FD   (box fills — teal)
Planet Purple:      #D1DAFA   (box fills — light purple)
Sky Blue:           #ADCDFB   (box fills — light blue)
Rusty Red:          #FF8980   (error/warning accents)
Enterprise Purple:  #6F2CBA   (strong purple accent)
```

**Multi-topic color rule — use different families for different topics:**
- Topic 1: `#FFF2EB` fill (O:10 orange tint)
- Topic 2: `#F3EBFF` fill (P:10 purple tint)
- Topic 3: `#E5F4FF` fill (B:10 blue tint)
- Topic 4: `#FFF9E0` fill (Y:10 yellow tint)
- Topic 5: `#FEF1FD` fill (M:10 magenta tint)
- Topic 6: `#A4EEC4` fill (Flora Green accent)
- All box borders: `#000000` — always

**Five Forces / hub-and-spoke layout — canonical rules (match this exactly):**
- All 4 corner force cards: identical size `240×160px`, equal padding `16px` all sides
- Force 05 (bottom centre): same width `240px`, height auto to content, same padding `16px`
- Hub: black filled circle, centred, with 4–5 fading concentric rings behind it
- Arrows: dashed, from the nearest corner/edge of each card straight to the hub circle boundary
- Cards sit at diagonal positions from hub — top-left, top-right, bottom-left, bottom-right, bottom-centre
- Gap between card edge and hub circle: ~60–80px
- All text rendered as native SVG `<text>` elements — never `foreignObject` for card content
- Card body text: wrap manually with explicit `<text>` lines, max ~32 chars per line at 11px
- Eyebrow / Stage label: IBM Plex Mono **15px** weight 700, colour matches family accent — this is the minimum. Never use 8px, 9px, or 11px for eyebrows.
- Title: Inter 13px weight 600
- Body: Inter 11px weight 400, colour `#454545`, line-height ~16px

**foreignObject sizing — CRITICAL:** When using `<foreignObject>` inside SVG to render HTML content, always set the `height` large enough to contain all text at any wrapping width. Never use a fixed height that could clip content. The safe approach is to set `height` generously (e.g. 200px for a card that visually needs ~130px) and let the SVG canvas provide the visual boundary. If you need a visible border/background, draw it as a separate SVG `<rect>` sized to the intended visual dimensions, and let the `<foreignObject>` be taller. This ensures text never clips or overflows out of a box.

**Em dashes — NEVER use:** Never use em dashes (—) in any text, labels, captions, or body copy in infographics. Replace with: a comma, a colon, a period, or rewrite the sentence to avoid the need for a dash entirely. If content from a source uses an em dash, rewrite it on output.

**Internal alignment — CRITICAL:** Every element inside a card or box must start at the same x-axis. Use a single padding constant (e.g. `pad=14`) and derive ALL element x positions from `card_x + pad`. This includes: eyebrow labels, icons, headings, body text lines, chips, divider lines, metric labels, and metric values. Never let any element inside a card start at a different x than the others. Divider lines must also START at `card_x + pad` and END at `card_x + card_width - pad`.

**No placeholders:** Never add placeholder content, example text, or dummy items unless the user explicitly asks for them. Only include content that was requested or provided.

**Text containment — CRITICAL:** All text must stay within its bounding box with equal padding on all sides. Rules:
- Set a `usable_width = card_width - 2 * padding` and never let any text line exceed that width
- At 11px Inter, safe line length = `usable_width / 6.5` characters (approximate)
- At 13px Inter 600, safe line length = `usable_width / 7.5` characters
- At 15px Inter 700, safe line length = `usable_width / 8.5` characters
- Always manually hard-wrap every line to fit within usable_width before rendering
- Never use foreignObject for card text — always native SVG text with explicit x/y per line

**Row width consistency — CRITICAL:** When a layout has multiple horizontal rows stacked vertically (e.g. a section label row, a card row, a strip row, a reading order bar), all rows must span exactly the same total width. Never let one row be wider or narrower than another. Derive the total width from the widest natural row (usually the card grid: 5 cards × card_width + 4 gaps), then set every other row — headers, section labels, full-width bars, reading order boxes — to that exact same width.

**Divider lines inside boxes:** Always add a minimum of 15px padding above and below every divider line. In SVG this means the divider `y` must be at least 15px below the last element above it, and the next element must start at least 15px below the divider `y`.

**Divider lines inside boxes (colour rule):** When drawing a horizontal rule to separate sections within a box, use a shade darker than the box fill — not a fixed grey. Derive it from the same colour family:
- Orange box (`#FFF2EB`): divider `#FFBCA3`
- Purple box (`#F3EBFF`): divider `#CDAFF7`
- Blue box (`#E5F4FF`): divider `#80C1FF`
- Yellow box (`#FFF9E0`): divider `#FFD875`
- Magenta box (`#FEF1FD`): divider `#FFCCFC`
- Green box (`#A4EEC4`): divider `#2daa72` at 30% opacity
- Grey box (`#E6E6E6`): divider `#A1A1A1`
- White box (`#fff`): divider `#E6E6E6`

**Owner / label chips inside cards:** Always `background:#000; color:#fff` — black chip, white text. Never light grey chips with grey text.

**Status indicator colors:**
- Check / success: `#A4EEC4` fill with `#000000` ✓ glyph (Flora Green)
- Warning: `#FFD875` fill with `#000000` ! glyph (Y:40 Elemental Yellow)
- Error: `#FF8980` fill with `#000000` ✗ glyph (Rusty Red)

**Hard rule: never use CSS variables or generic diagram ramp classes — always hardcode hex values directly.**

### Typography
Use **Inter** for everything. No other display font.

Type ramp:
- H1: 28px, weight 700, `#0a0a0a` — infographic title/heading. **When H1 appears inside a box, constrain font-size to 15px–28px depending on box size. Never let it overflow or dominate the box.**
- H2: 20px, weight 600, `#0a0a0a` — section titles
- H3: 16px, weight 600, `#0a0a0a` — card/box titles

**Heading alignment:** Always left-aligned by default (`text-align:left`). Only centre or right-align if the user explicitly asks.

**Title case:** All headings and box titles must use title case — capitalise every major word. Articles (a, an, the), short prepositions (in, on, of, at, by), and conjunctions (and, or, but) are lowercase unless they are the first word. IBM Plex Mono labels (axes, tags, captions) use all-uppercase with `text-transform:uppercase`.
- Body: 14px, weight 400, `#444444` — descriptions, body text
- Subtext: 13px, weight 400, `#444444` — supporting text. **Never use weight 300 (light) — always use 400 (regular)**
- Eyebrow / Section label (STAGE 01, METRIC, DIAGRAM 1 etc): **15px**, weight 700, IBM Plex Mono uppercase — always 15px minimum
- Axis / caption label: 11px, weight 400, `#888888`, IBM Plex Mono uppercase, letter-spacing 0.08em — axes, captions, small tags only

Load from Google Fonts in HTML:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@300;400;500&display=swap" rel="stylesheet">
```
For SVG:
- All text: font-family="'Inter',sans-serif"
- Labels/captions only: font-family="'IBM Plex Mono','Courier New',monospace"

### Spacing & Sizing
- **Logo → heading gap: exactly `50px`** — measure from bottom of logo to baseline of H1
- **Padding inside all boxes: `15px` on all sides** — applies to stat cards, flow boxes, table cells, tier cards
- Gap between sections: `32px`
- Border radius: `8px` (cards), `4px` (tags/chips), `100px` (pills)
- Border: `1px solid #e0ddd8`

---

## Format Selection

Choose **SVG** when:
- Static, single-panel visualization
- Will be shared/exported as an image
- Data is primarily visual (bars, circles, flow nodes)
- No interactivity needed

Choose **HTML** when:
- Multiple panels or sections
- Needs hover states, tooltips, or animation
- Rich typography layouts (feature comparisons, timelines with text)
- Grid or responsive layout

---

## Background selection

**Default: always white (`#ffffff`)** — use for website embeds, slide decks, documentation, and any unspecified context.

**Social media gradient** — only use when the user explicitly says the infographic is for social media (LinkedIn, Twitter/X, Instagram, etc.). In that case, ask:

> "Would you like the social media background — a subtle peach-to-lavender gradient — or plain white?"

Then apply based on their answer:

| Context | Background |
|---------|------------|
| Website / docs / general | `background: #ffffff` |
| Slide decks | `background: #ffffff` |
| Social media (if user confirms gradient) | `background: linear-gradient(135deg, #fff8f5 0%, #ffffff 40%, #f5f3ff 100%)` |
| Social media (if user wants plain) | `background: #ffffff` |

Never apply the gradient without asking. Never assume social media context — only act on it when the user states it.

---

## Recurring Visual Patterns (from brand reference)

These are the exact layout patterns used throughout Postman's own documents. Replicate them closely.

### Tiered / Maturity Cards
A vertical stack of cards, each representing a level or tier. Each card has:
- A small `IBM Plex Mono` uppercase label in `#FF6C37` at top (e.g. "LEVEL 1", "CHAPTER 03")
- A bold `Inter 600` title below it
- `Inter 300` body description
- Left border or background tint to distinguish levels — use subtle tints from the same hue family (e.g. a soft orange wash for Level 1, a soft blue wash for Level 2, a soft purple wash for Level 3)
- Rounded corners `8px`, no heavy drop shadows

### Icon + Text List Items
Bullet-list items where each point has a small square icon (28–32px) to the left, with `#FF6C37` fill or stroke, followed by `Inter 600` bold label + `Inter 400` description inline. Common for "this pattern works for:" style lists.

### Customer Story / Callout Box
A bordered card (1px `#e0ddd8`, `8px` radius) with:
- Company logo at top left
- Bold headline in `Inter 700` 
- Pull quote with large `"` mark in `#FF6C37`
- Attribution: name in `Inter 600`, role in `Inter 300 #888`
- CTA link in `#FF6C37` with `→` arrow at bottom

### Info Tip Box
A small, compact callout used for "get started" / "ready to try" nudges:
- Rounded rect, 1px `#e0ddd8` border
- Small orange `ⓘ` circle icon (24px) on the left
- Short text + orange hyperlink with `→`
- Max width ~380px, sits inline with content

### Section Divider / Chapter Header
Full-width band with:
- Soft tinted background (very light purple/lavender `#f0eeff` or peach `#fff3ee`)
- `IBM Plex Mono` uppercase chapter label in `#FF6C37` (e.g. "CHAPTER 03")
- Large decorative chapter number in outline style (stroke only, no fill)
- `Inter 700` chapter title
- Intro paragraph + author photo chips with circular avatars

### Reference Table
Full-width table for structured comparison of options:
- No background on the outer container — table sits on white
- Header row: `Inter 600`, no background fill — just a bottom border `2px #e0ddd8`
- First column cells: `Inter 600` in `#FF6C37` (the row label/name)
- Body cells: `Inter 400 #444`, `14px`
- Row dividers: `1px #f0ede8` (very subtle)
- No alternating row backgrounds — use row dividers only
- Cell padding: `16px 12px`

### Flow / Architecture Diagram
Boxes connected by arrows for workspace/API topology diagrams:
- Boxes: white fill, `1px #e0ddd8` border, `6px` radius, `Inter 500` label, `Inter 300 #888` subtitle
- Primary boxes (highlighted): soft green or blue tint fill (`#f0f9f4` or `#f0f4ff`)
- Arrow labels: `Inter 300 #888` small text alongside `1px #ccc` lines with arrowheads
- Connector lines: thin `1px`, gray `#ccc`, with simple open arrowheads
- Overall: very airy layout, boxes well-spaced, no crossing lines if possible

**Connector precision rule — CRITICAL:** Connectors must touch box edges exactly.
- Line `x1` = right edge of source box (`box_x + box_width`)
- Line `x2` = left edge of target box (`box_x`)
- Dot midpoints: `cx = (x1 + x2) / 2`
- Never eyeball connector coordinates — always derive them from box positions
- For vertical connectors: `y1` = bottom edge of source, `y2` = top edge of target

**Arrow rule — CRITICAL:** All workflow connectors must use arrowheads to indicate direction of movement. Never use plain lines or dots alone between boxes in a workflow.
- Always include the arrow marker in `<defs>` and apply `marker-end="url(#arrow)"` to every connector line
- For dashed connectors, use a dashed line with an arrowhead at the target end: `stroke-dasharray="5 4"` + `marker-end="url(#arrow)"`
- Never use midpoint dots or circles on connectors — arrows are the only direction indicator
- Arrow marker definition:
```svg
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#0a0a0a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
```

**Spacing rule:** All gaps between boxes must be identical. Calculate once and reuse:
- Pick a `gap` value (e.g. 40px)
- `box_width = (total_usable_width - (n_boxes - 1) * gap) / n_boxes`
- First box at `x = margin`, each subsequent box at `x = prev_x + box_width + gap`
- Never set box positions individually — always derive from the formula

**Multi-topic color rule:** When boxes represent different topics, stages, or concepts, each box gets a distinct brand tint for strong differentiation. Use saturated tints — do not use near-white or barely-visible fills. All boxes use `#0a0a0a` border regardless of fill color. Mapping:
- Topic 1: `#fff3ee` fill (orange tint)
- Topic 2: `#eef3ff` fill (blue tint)
- Topic 3: `#f0eeff` fill (purple tint)
- Topic 4: `#eef8f3` fill (green tint)
- Topic 5: `#fdf3e0` fill (amber tint)
- Topic 6: `#fdeef2` fill (pink tint)
- Border on ALL boxes: `#0a0a0a` — never use a colored or tinted border, the fill provides the color differentiation
- Text in all boxes stays `#0a0a0a` — never change text color per box

**Box outline rule — CRITICAL:** Every box must have a dark, visible stroke using the brand's text primary color.
- Always use `stroke="#0a0a0a"` (Text primary from the brand color library) with `stroke-width="1.5"` on every box rect
- In HTML, use `border: 1.5px solid #0a0a0a`
- The fill can be a light tint, but the outline must always be `#0a0a0a` — never a tint, never gray, never a color-family border
- This applies to all infographic types — flow diagrams, stat cards, comparison tables, tiered cards
---

## Icons

Icons are **not used by default**. Only include icons when the user explicitly asks for them.

### Style rules
- **Stroke only** — never filled. Icons must be line/stroke style, no solid fills.
- **Stroke weight** — match the box border weight: `stroke-width="1.5"` to stay visually consistent with box outlines
- **Color** — a few shades darker than the box fill tint, using the same color family. Never black, never the accent orange. Use these pairings:
  - Orange box (`#fff3ee`): icon stroke `#cc4f22`
  - Blue box (`#eef3ff`): icon stroke `#3060c0`
  - Purple box (`#f0eeff`): icon stroke `#5b4fd4`
  - Green box (`#eef8f3`): icon stroke `#1e8a58`
  - Amber box (`#fdf3e0`): icon stroke `#9a6c00`
  - Pink box (`#fdeef2`): icon stroke `#b03060`
- **Size** — 24×24px inside a box. Scale to 32×32px for standalone icon callouts.
- **Style** — clean geometric strokes, rounded `stroke-linecap="round"` and `stroke-linejoin="round"`, no decorative details. Think simple symbols: arrows, circles, checkmarks, document, gear, lock, people, chart.
- **Placement** — top of the box before the label, or left-aligned inline with the title. Never centered over text.

### SVG icon template
```html
<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
     stroke="#cc4f22" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round">
  <!-- icon paths here -->
</svg>
```

### Common icon paths (copy-paste ready)
```
Document:  M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6
Gear:      M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm7-3a7 7 0 1 1-14 0 7 7 0 0 1 14 0
Lock:      M19 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2zM7 11V7a5 5 0 0 1 10 0v4
People:    M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75
Chart bar: M18 20V10M12 20V4M6 20v-6
Check:     M20 6L9 17l-5-5
Arrow right: M5 12h14M12 5l7 7-7 7
Clock:     M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6v6l4 2
```


**Status indicator color rules:**
- Check marks / success: `#22a06b` (green) — e.g. ✓ in feature tables, completion states
- Exclamation / warning: `#b8860b` (dark yellow) — e.g. ! alerts, caution states
- Errors / failure: `#e03030` (red) — e.g. ✗ failures, error states
- These override any other color rule — status colors are semantic and must be consistent

---

## Infographic Types

### 1. Data / Stats Visualization
Bar charts, pie charts, sparklines, big-number callouts.

**Key rules:**
- Lead with the most important number in large `Degular Display` type at `48–72px`
- Use `#FF6C37` for the primary/highlighted data series only; use `#888` or `#e0ddd8` for secondary series
- Always include axis labels in `IBM Plex Mono` uppercase at `11px`
- Keep chart area clean — no gridlines unless essential, use subtle `#e0ddd8` if needed
- Add a 1–2 sentence insight below the chart in `Inter` 400 at `13px` color `#444`

### 2. Process Flows & Timelines
Step-by-step flows, numbered sequences, before/after, milestones.

**Key rules:**
- Number steps using `IBM Plex Mono` in `#FF6C37` circles or squares
- Connect steps with thin `1.5px` lines in `#e0ddd8`
- Each step: bold `Inter 600` title + `Inter 300` description below
- For timelines, use a horizontal or vertical spine in `#e0ddd8` with dot markers in `#FF6C37`
- Group related steps with a subtle tinted background block (match the Tiered Cards pattern)

### 3. Comparison / Feature Tables
Side-by-side comparisons, feature matrices, pros/cons.

**Key rules:**
- Follow the Reference Table pattern above exactly
- First-column row labels in `#FF6C37` `Inter 600` to anchor each row visually
- Highlight the "winner" or recommended column with a `#FF6C37` top border (3px)
- Use ✓ in `#FF6C37` and — in `#ccc` for boolean features
- Column headers in `IBM Plex Mono` uppercase

---

## Layout Principles

1. **One accent rule** — `#FF6C37` should appear in 1–2 places maximum per infographic. It's a punch, not a paint.
2. **Hierarchy first** — Title → Key insight → Supporting data → Labels. Font size and weight carry the hierarchy; color is secondary.
3. **Breathe** — Generous padding. Never crowd elements. White space is intentional.
4. **Labels are small** — Axis labels, captions, tags: `10–12px`, `IBM Plex Mono`, muted color `#888`.
5. **Consistent sizing** — Stick to a type scale: `72px` hero numbers, `24px` section titles, `16px` body, `13px` secondary, `11px` labels.

---

## SVG Template (minimal)

```svg
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="background:#f0ede8;font-family:'Inter',sans-serif;">
  <!-- Background -->
  <rect width="800" height="500" fill="#f0ede8"/>

  <!-- Card -->
  <rect x="32" y="32" width="736" height="436" rx="8" fill="#ffffff" stroke="#e0ddd8" stroke-width="1"/>

  <!-- Accent top bar -->
  <rect x="32" y="32" width="736" height="4" rx="2" fill="#FF6C37"/>

  <!-- Title -->
  <text x="56" y="88" font-family="'Degular Display',Georgia,serif" font-size="28" font-weight="600" fill="#0a0a0a">Title Here</text>

  <!-- Mono label -->
  <text x="56" y="110" font-family="'IBM Plex Mono','Courier New',monospace" font-size="15" fill="#888888" letter-spacing="1" text-transform="uppercase">SUBTITLE LABEL</text>

  <!-- Content goes here -->

</svg>
```

---

## HTML Template (minimal)

```html
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=IBM+Plex+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #f0ede8; font-family: 'Inter', sans-serif; color: #0a0a0a; padding: 32px; }
  .card { background: #fff; border: 1px solid #e0ddd8; border-radius: 8px; border-top: 4px solid #FF6C37; padding: 32px; }
  .title { font-family: 'Degular Display', Georgia, serif; font-size: 28px; font-weight: 600; }
  .label { font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: #888; }
  .accent { color: #FF6C37; }
  .body { font-size: 14px; line-height: 1.6; color: #444; font-weight: 300; }
</style>
</head>
<body>
  <div class="card">
    <!-- content -->
  </div>
</body>
</html>
```

---

## Checklist Before Rendering

- [ ] Background is `#f0ede8` or `#fff` (never dark unless a specific contrast block)
- [ ] All body text is `#0a0a0a` or `#444` — readable at small sizes
- [ ] `#FF6C37` used in max 2 places
- [ ] Headlines use `Degular Display` (or serif fallback)
- [ ] Labels/axes use `IBM Plex Mono` uppercase
- [ ] Adequate padding (min 24px inside cards)
- [ ] No decorative gradients — flat, clean surfaces only
- [ ] A clear visual hierarchy: one dominant element per infographic

---

## Logo Usage

No header logo — the infographic header should not include the wordmark logo. The only brand asset used is the **watermark** (logomark only, bottom of infographic).

---

## Watermark

**Every infographic must include the Postman logomark as a watermark by default.** The user can explicitly ask to remove it, but it must be present unless told otherwise.

### Placement — CRITICAL: fixed position, exact spacing
- **Always top-right corner, 25px padding from both the top and right edges** — no exceptions unless user asks
- Use `position:absolute; top:25px; right:25px` on the watermark SVG, with `position:relative` on the outer wrapper
- The wrapper must have enough top padding to prevent content from sitting behind the watermark — use `padding-top:61px (25px offset + 36px mark height) on the content area
- Size: 36px × 36px
- Opacity: 0.18
- If the user asks to move it, honour their placement but keep 25px margins
- **SVG infographics: do not embed the watermark in SVG** — SVG `<image>` and nested SVG rendering is unreliable in the widget. For SVG infographics, skip the watermark entirely or switch to HTML.

### Implementation
Always use this exact inline SVG block. The SVG paths are from `assets/Postman_Logomark_orange.svg`.

**CRITICAL: never use `<style>` blocks or CSS classes inside the watermark SVG.** Class names conflict across multiple SVGs on the same page and break the rendering. Always use inline `fill` attributes.

Wrap the entire infographic in a `position:relative` div. Place the watermark SVG as a direct child:
## ⚠️ WATERMARK SVG — COPY THIS BLOCK EXACTLY. NEVER MODIFY. NEVER ABBREVIATE. NEVER REGENERATE.

The watermark must always be this exact SVG, copied verbatim. Do not rewrite it. Do not shorten it. Do not change any paths. If you generate a new watermark from scratch it will break. Always paste this block as-is:

```html
<svg width="36" height="36" viewBox="0 0 210 208" xmlns="http://www.w3.org/2000/svg"
     style="position:absolute;top:25px;right:25px;opacity:1;pointer-events:none;">
  <circle fill="#fff" cx="105.5" cy="103.1" r="87.3"/>
  <path fill="#fff" d="M106,190.4c48.8,0,88.3-39.5,88.3-88.3S154.8,13.8,106,13.8,17.7,53.3,17.7,102.1s39.5,88.3,88.3,88.3h0Z"/>
  <path fill="#ff6c37" d="M160.9,54.3c-.1,0-.2.2-.3.3-.1,0-.2.2-.2.4v.4c0,.2,0,.3.1.4.3.6.4,1.2.3,1.9,0,.7-.3,1.2-.8,1.8,0,.1-.2.2-.2.4v.4c0,.1,0,.3.1.4,0,.1.1.2.3.3.1,0,.2.2.4.2h.4c.1,0,.3,0,.4-.1.1,0,.2-.2.3-.3.7-.8,1.1-1.8,1.2-2.9.1-1.1,0-2.2-.5-3.1,0-.1-.1-.2-.3-.3-.1,0-.2-.2-.4-.2h-.4c-.1,0-.3,0-.4.1h0v-.1Z"/>
  <path fill="#ff6c37" d="M118.2,6.9C65.7.2,17.6,37.3,10.9,89.9c-6.8,52.6,30.4,100.6,82.9,107.3,52.6,6.8,100.6-30.4,107.4-82.9,6.8-52.5-30.4-100.6-82.9-107.3h0l-.1-.1ZM138,66.8c-1.8,0-3.5.8-4.7,2l-35.6,35.6-7.6-7.6c35.1-35,41.4-35.3,47.9-30h0ZM99.1,105.7l35.5-35.5c.9-.9,2.2-1.4,3.5-1.4s2.6.5,3.5,1.4c.5.5.9,1.1,1.1,1.7s.4,1.3.3,2c0,.7-.2,1.3-.5,1.9s-.7,1.2-1.2,1.6l-37.6,33-4.7-4.7h.1ZM101.7,111.2l-8.8,1.9h-.3c-.1,0-.2-.1-.2-.2v-.3s0-.2.1-.3l5.2-5.2,4.1,4.1h-.1ZM79.3,107.5l9.4-9.4,7,7-15.8,3.4h-.4c-.1,0-.2-.2-.3-.3v-.4c0-.1,0-.2.2-.4h0l-.1.1ZM50.2,156c-.1,0-.2,0-.3-.1,0,0-.2-.2-.2-.3v-.3c0-.1,0-.2.2-.3l7.6-7.6,9.8,9.8-17-1.2h-.1ZM69.6,145.9h0c-.4.2-.6.5-.8.9s-.2.8-.1,1.2l1.6,6.9v.6c0,.2-.2.4-.4.5s-.4.1-.6.1-.4-.1-.6-.3l-9.8-9.8,30.1-30.1,14.6-3.1,7,7c-10,8.8-23.8,17.6-40.8,26.1h-.2ZM111.8,118.5l-6.7-6.7,37.6-33c.4-.3.7-.7.9-1-1.2,10.8-16.2,26-31.8,40.7h0ZM141,66.8c-2.6-2.7-4.2-6.2-4.2-10s1.3-7.4,3.8-10.1c2.5-2.8,6-4.5,9.8-4.7,3.7-.2,7.4,1,10.3,3.3l-12.9,12.9c-.2.2-.3.4-.3.7s.1.5.3.7l10,10c-2.7,1.4-5.8,1.8-8.8,1.3s-5.8-1.9-7.9-4.1h-.1ZM161.6,66.8c-.7.7-1.4,1.2-2.2,1.8l-9.6-9.7,12.3-12.3c2.5,2.8,3.9,6.4,3.8,10.2,0,3.8-1.6,7.3-4.3,10h0Z"/>
</svg>
```

This block has exactly 4 elements: `<circle>`, white `<path>`, small orange `<path>`, large orange `<path>`. That is all. Do not add, remove, or alter any element. Do not use `<style>` tags or CSS classes inside it. Inline `fill` attributes only. Opacity always 1.

```html
<div style="position:relative;padding:28px;padding-top:61px;">
  <svg width="36" height="36" viewBox="0 0 210 208" xmlns="http://www.w3.org/2000/svg"
       style="position:absolute;top:25px;right:25px;opacity:1;pointer-events:none;">
    <circle fill="#fff" cx="105.5" cy="103.1" r="87.3"/>
    <path fill="#fff" d="M106,190.4c48.8,0,88.3-39.5,88.3-88.3S154.8,13.8,106,13.8,17.7,53.3,17.7,102.1s39.5,88.3,88.3,88.3h0Z"/>
    <path fill="#ff6c37" d="M160.9,54.3c-.1,0-.2.2-.3.3-.1,0-.2.2-.2.4v.4c0,.2,0,.3.1.4.3.6.4,1.2.3,1.9,0,.7-.3,1.2-.8,1.8,0,.1-.2.2-.2.4v.4c0,.1,0,.3.1.4,0,.1.1.2.3.3.1,0,.2.2.4.2h.4c.1,0,.3,0,.4-.1.1,0,.2-.2.3-.3.7-.8,1.1-1.8,1.2-2.9.1-1.1,0-2.2-.5-3.1,0-.1-.1-.2-.3-.3-.1,0-.2-.2-.4-.2h-.4c-.1,0-.3,0-.4.1h0v-.1Z"/>
    <path fill="#ff6c37" d="M118.2,6.9C65.7.2,17.6,37.3,10.9,89.9c-6.8,52.6,30.4,100.6,82.9,107.3,52.6,6.8,100.6-30.4,107.4-82.9,6.8-52.5-30.4-100.6-82.9-107.3h0l-.1-.1ZM138,66.8c-1.8,0-3.5.8-4.7,2l-35.6,35.6-7.6-7.6c35.1-35,41.4-35.3,47.9-30h0ZM99.1,105.7l35.5-35.5c.9-.9,2.2-1.4,3.5-1.4s2.6.5,3.5,1.4c.5.5.9,1.1,1.1,1.7s.4,1.3.3,2c0,.7-.2,1.3-.5,1.9s-.7,1.2-1.2,1.6l-37.6,33-4.7-4.7h.1ZM101.7,111.2l-8.8,1.9h-.3c-.1,0-.2-.1-.2-.2v-.3s0-.2.1-.3l5.2-5.2,4.1,4.1h-.1ZM79.3,107.5l9.4-9.4,7,7-15.8,3.4h-.4c-.1,0-.2-.2-.3-.3v-.4c0-.1,0-.2.2-.4h0l-.1.1ZM50.2,156c-.1,0-.2,0-.3-.1,0,0-.2-.2-.2-.3v-.3c0-.1,0-.2.2-.3l7.6-7.6,9.8,9.8-17-1.2h-.1ZM69.6,145.9h0c-.4.2-.6.5-.8.9s-.2.8-.1,1.2l1.6,6.9v.6c0,.2-.2.4-.4.5s-.4.1-.6.1-.4-.1-.6-.3l-9.8-9.8,30.1-30.1,14.6-3.1,7,7c-10,8.8-23.8,17.6-40.8,26.1h-.2ZM111.8,118.5l-6.7-6.7,37.6-33c.4-.3.7-.7.9-1-1.2,10.8-16.2,26-31.8,40.7h0ZM141,66.8c-2.6-2.7-4.2-6.2-4.2-10s1.3-7.4,3.8-10.1c2.5-2.8,6-4.5,9.8-4.7,3.7-.2,7.4,1,10.3,3.3l-12.9,12.9c-.2.2-.3.4-.3.7s.1.5.3.7l10,10c-2.7,1.4-5.8,1.8-8.8,1.3s-5.8-1.9-7.9-4.1h-.1ZM161.6,66.8c-.7.7-1.4,1.2-2.2,1.8l-9.6-9.7,12.3-12.3c2.5,2.8,3.9,6.4,3.8,10.2,0,3.8-1.6,7.3-4.3,10h0Z"/>
  </svg>
  <!-- infographic content here -->
</div>
```

### Rules
- Always `position:absolute; top:25px; right:25px` — exact, no deviations without user instruction
- Outer wrapper must be `position:relative` so the absolute offset is contained
- Content area must have `padding-top` ≥ 96px so it never overlaps the watermark
- Never embed the watermark inside SVG — HTML only; SVG infographics skip it
- User can ask to remove it — omit the SVG element entirely
- User can ask to reposition — honour their placement, keep 25px margins
- Never recolor or resize beyond 36×36px
