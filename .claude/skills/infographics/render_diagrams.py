#!/usr/bin/env python3
"""Render the docs diagrams as SVG, one light and one dark variant each.

Coordinates are derived from a handful of constants rather than written by hand,
which is what the infographics SKILL.md asks for: box positions come from a
formula, connectors are computed from box edges, and every element inside a box
shares one padding constant.

Two deliberate departures from SKILL.md, both because this output is embedded in
a themeable docs site rather than exported as a standalone image:

1. A dark variant exists at all. The skill mandates light backgrounds and forbids
   CSS variables, so theming has to happen by shipping two files and swapping
   them with Fern's `dark:hidden` / `hidden dark:block` classes. The dark variant
   inverts the colour carrier: fills go to a flat dark neutral and the topic
   colour moves to the border, because white text on the palette's dark shades
   fails contrast in places (white on Y:70 is 3.62:1).

2. Kafka topic names stay lowercase. The skill uppercases IBM Plex Mono labels,
   but these are literal identifiers — `charge.captured`, not CHARGE.CAPTURED.

Run: python3 .claude/skills/infographics/render_diagrams.py
"""

import pathlib

OUT = pathlib.Path(__file__).resolve().parents[3] / "fern" / "docs" / "assets" / "diagrams"

# Official Postman 2026 palette values used here.
TOPIC_TINTS = ["#fff3ee", "#eef3ff", "#f0eeff", "#eef8f3", "#fdf3e0"]
TOPIC_ACCENTS = ["#FF6C37", "#80C1FF", "#B387F5", "#A4EEC4", "#FFD875"]

THEMES = {
    "light": dict(
        page="#ffffff", fill=lambda i: TOPIC_TINTS[i % len(TOPIC_TINTS)],
        stroke=lambda i: "#0a0a0a", title="#0a0a0a", body="#454545",
        line="#0a0a0a", label="#737373", pill_fill="#0a0a0a", pill_text="#ffffff",
    ),
    "dark": dict(
        page="none", fill=lambda i: "#161320",
        stroke=lambda i: TOPIC_ACCENTS[i % len(TOPIC_ACCENTS)],
        title="#ffffff", body="#CFCFCF",
        line="#A1A1A1", label="#A1A1A1", pill_fill="#FF6C37", pill_text="#0a0a0a",
    ),
}

INTER = "'Inter',-apple-system,BlinkMacSystemFont,sans-serif"
MONO = "'IBM Plex Mono','SFMono-Regular',Consolas,monospace"

PAD = 15  # single padding constant; every x inside a box derives from it


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def defs(t):
    return (
        f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" '
        f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M2 1L8 5L2 9" fill="none" stroke="{t["line"]}" stroke-width="1.5" '
        f'stroke-linecap="round" stroke-linejoin="round"/></marker></defs>'
    )


def chain_svg(theme_name, title, trigger, steps):
    """Vertical flow: a trigger pill, then one box per step, events on connectors."""
    t = THEMES[theme_name]
    W, BOX_W, BOX_H, GAP = 760, 430, 72, 64
    BOX_X = (W - BOX_W) // 2
    CX = W // 2
    PILL_H, PILL_GAP = 32, 44

    y = 10
    pill_y = y
    first_top = pill_y + PILL_H + PILL_GAP
    tops = [first_top + i * (BOX_H + GAP) for i in range(len(steps))]
    H = tops[-1] + BOX_H + 14

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" role="img" aria-label="{esc(title)}">',
        defs(t),
    ]
    if t["page"] != "none":
        p.append(f'<rect width="{W}" height="{H}" fill="{t["page"]}"/>')

    # Trigger pill, centred, sized to the label.
    pw = max(190, len(trigger) * 8 + 40)
    px = CX - pw // 2
    p.append(
        f'<rect x="{px}" y="{pill_y}" width="{pw}" height="{PILL_H}" rx="16" '
        f'fill="{t["pill_fill"]}"/>'
        f'<text x="{CX}" y="{pill_y + 21}" text-anchor="middle" font-family="{MONO}" '
        f'font-size="13" font-weight="500" fill="{t["pill_text"]}">{esc(trigger)}</text>'
    )
    p.append(
        f'<line x1="{CX}" y1="{pill_y + PILL_H}" x2="{CX}" y2="{first_top}" '
        f'stroke="{t["line"]}" stroke-width="1.5" marker-end="url(#a)"/>'
    )

    for i, (name, desc, event) in enumerate(steps):
        top = tops[i]
        p.append(
            f'<rect x="{BOX_X}" y="{top}" width="{BOX_W}" height="{BOX_H}" rx="8" '
            f'fill="{t["fill"](i)}" stroke="{t["stroke"](i)}" stroke-width="1.5"/>'
            f'<text x="{BOX_X + PAD}" y="{top + 29}" font-family="{MONO}" font-size="14" '
            f'font-weight="500" fill="{t["title"]}">{esc(name)}</text>'
            f'<text x="{BOX_X + PAD}" y="{top + 52}" font-family="{INTER}" font-size="14" '
            f'fill="{t["body"]}">{esc(desc)}</text>'
        )
        if event:  # connector down to the next box, with the topic name beside it
            y1, y2 = top + BOX_H, tops[i + 1]
            p.append(
                f'<line x1="{CX}" y1="{y1}" x2="{CX}" y2="{y2}" stroke="{t["line"]}" '
                f'stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#a)"/>'
                f'<text x="{CX + 14}" y="{(y1 + y2) // 2 + 4}" font-family="{MONO}" '
                f'font-size="12" fill="{t["label"]}">{esc(event)}</text>'
            )

    p.append("</svg>")
    return "\n".join(p)


def fanout_svg(theme_name, title, source, targets):
    """One source event fanning out over a bus into a grid of reacting services.

    Colour carries meaning here: the group index picks the tint, so the four
    kinds of reaction (seed, snapshot, publish, record) read as four families
    rather than nine arbitrary colours.
    """
    t = THEMES[theme_name]
    W, COLS, GAP, M = 760, 3, 16, 10
    CARD_W = (W - 2 * M - (COLS - 1) * GAP) // COLS
    CARD_H = 78
    CX = W // 2
    PILL_H = 34

    col_cx = [M + c * (CARD_W + GAP) + CARD_W // 2 for c in range(COLS)]
    pill_bottom = 10 + PILL_H
    bus_y = pill_bottom + 24
    grid_top = bus_y + 24

    rows = (len(targets) + COLS - 1) // COLS
    H = grid_top + rows * CARD_H + (rows - 1) * GAP + 14

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" role="img" aria-label="{esc(title)}">',
        defs(t),
    ]
    if t["page"] != "none":
        p.append(f'<rect width="{W}" height="{H}" fill="{t["page"]}"/>')

    pw = max(200, len(source) * 8 + 40)
    p.append(
        f'<rect x="{CX - pw // 2}" y="10" width="{pw}" height="{PILL_H}" rx="17" '
        f'fill="{t["pill_fill"]}"/>'
        f'<text x="{CX}" y="{10 + 22}" text-anchor="middle" font-family="{MONO}" '
        f'font-size="13" font-weight="500" fill="{t["pill_text"]}">{esc(source)}</text>'
    )

    # Distribution bus: one drop from the pill, one horizontal run, one arrow per column.
    p.append(
        f'<line x1="{CX}" y1="{pill_bottom}" x2="{CX}" y2="{bus_y}" '
        f'stroke="{t["line"]}" stroke-width="1.5"/>'
        f'<line x1="{col_cx[0]}" y1="{bus_y}" x2="{col_cx[-1]}" y2="{bus_y}" '
        f'stroke="{t["line"]}" stroke-width="1.5"/>'
    )
    for cx in col_cx:
        p.append(
            f'<line x1="{cx}" y1="{bus_y}" x2="{cx}" y2="{grid_top}" stroke="{t["line"]}" '
            f'stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#a)"/>'
        )

    for i, (name, group, desc) in enumerate(targets):
        r, c = divmod(i, COLS)
        x = M + c * (CARD_W + GAP)
        y = grid_top + r * (CARD_H + GAP)
        p.append(
            f'<rect x="{x}" y="{y}" width="{CARD_W}" height="{CARD_H}" rx="8" '
            f'fill="{t["fill"](group)}" stroke="{t["stroke"](group)}" stroke-width="1.5"/>'
            f'<text x="{x + PAD}" y="{y + 26}" font-family="{MONO}" font-size="12" '
            f'font-weight="500" fill="{t["title"]}">{esc(name)}</text>'
        )
        for j, line in enumerate(desc):
            p.append(
                f'<text x="{x + PAD}" y="{y + 46 + j * 16}" font-family="{INTER}" '
                f'font-size="12.5" fill="{t["body"]}">{esc(line)}</text>'
            )

    p.append("</svg>")
    return "\n".join(p)


CHAIN = dict(
    title="Encounter to cash: five services, five events",
    trigger="encounter.ended",
    steps=[
        ("charge-capture-service", "Builds a charge from the encounter", "charge.captured"),
        ("claims-submission-service", "Builds and submits the claim", "claim.submitted"),
        ("claims-adjudication-service", "Adjudicates against the payer", "claim.adjudicated"),
        ("invoicing-service", "Computes patient responsibility", "invoice.issued"),
        ("notifications-service", "Sends the statement", None),
    ],
)

# group 0 = seeds a record, 1 = snapshots the patient, 2 = publishes, 3 = records
FANOUT = dict(
    title="One patient created, nine services react",
    source="patient.created",
    targets=[
        ("eligibility", 0, ["Seeds a pending", "eligibility check"]),
        ("patient-consent", 0, ["Seeds a HIPAA", "consent record"]),
        ("patient-preferences", 0, ["Seeds default", "preferences"]),
        ("patient-timeline", 1, ["Snapshots the patient", "locally"]),
        ("patient-search", 1, ["Snapshots the patient", "locally"]),
        ("patient-relationships", 1, ["Snapshots the patient", "locally"]),
        ("ehr", 1, ["Snapshots the patient", "locally"]),
        ("patient-communications", 2, ["Publishes a welcome", "notification.requested"]),
        ("analytics-events", 3, ["Records the event"]),
    ],
)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for mode in ("light", "dark"):
        (OUT / f"encounter-to-cash-{mode}.svg").write_text(chain_svg(mode, **CHAIN))
        (OUT / f"patient-created-fanout-{mode}.svg").write_text(fanout_svg(mode, **FANOUT))
    for f in sorted(OUT.iterdir()):
        print(f"{f.name}  {f.stat().st_size:,} bytes")
