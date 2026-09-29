"""Design tokens: the single seed every page and unit colour derives from."""

FONT = "'Noto Sans TC','PingFang TC','Microsoft JhengHei','Heiti TC',sans-serif"

C = {
    "twill": "#EDE7DE",       # page ground (oatmeal twill)
    "tape": "#F7F4EF",        # name tape / reading surface
    "thread": "#33493F",      # deep sage thread: headings, key type
    "ink": "#35322F",         # body text
    "ink_soft": "#5E5852",    # secondary text
    "sage": "#A4B6AB",        # college cloth
    "sage_pale": "#D5DED8",
    "pink": "#D9B8B3",        # department cloth
    "pink_pale": "#EFE0DD",
    "blue": "#B9C6CC",        # institute cloth
    "blue_pale": "#DDE4E7",
    "rose": "#8A4F4F",        # the one primary action per view
    "rose_pale": "#F3E4E1",
    "rule": "#CFC6B9",        # stitch / hairline on twill
    "white": "#FFFFFF",
}

UNIT = {
    "college": {"cloth": C["sage"], "pale": C["sage_pale"], "name": "護理學院"},
    "dept": {"cloth": C["pink"], "pale": C["pink_pale"], "name": "護理學系"},
    "inst": {"cloth": C["blue"], "pale": C["blue_pale"], "name": "護理研究所"},
}

# 8px measurement grid
S = {1: "8px", 2: "16px", 3: "24px", 4: "32px", 5: "40px", 6: "48px", 8: "64px", 10: "80px"}

TYPE = {
    "display": "font-size:clamp(30px,7.6vw,40px);line-height:1.28;font-weight:900;letter-spacing:.01em;",
    "h2": "font-size:24px;line-height:1.4;font-weight:800;",
    "h3": "font-size:19px;line-height:1.5;font-weight:700;",
    "body": "font-size:16.5px;line-height:1.85;",
    "small": "font-size:14px;line-height:1.7;",
    "tape": "font-size:15px;line-height:1;font-weight:700;letter-spacing:.14em;",
}

TWILL_BG = (
    f"background-color:{C['twill']};"
    "background-image:repeating-linear-gradient(135deg,rgba(51,73,63,.045) 0 1px,transparent 1px 5px);"
)

SITE = "https://wwwndmc.ndmutsgh.edu.tw"


def _lum(hex_):
    h = hex_.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


TEXT_PAIRS = [
    ("thread", "twill"), ("thread", "tape"), ("ink", "twill"), ("ink", "tape"),
    ("ink_soft", "twill"), ("ink_soft", "tape"), ("white", "rose"), ("rose", "tape"),
    ("rose", "twill"), ("thread", "sage"), ("thread", "pink"), ("thread", "blue"),
    ("thread", "sage_pale"), ("thread", "pink_pale"), ("thread", "blue_pale"),
    ("ink", "rose_pale"), ("thread", "rose_pale"), ("ink_soft", "sage_pale"),
]

if __name__ == "__main__":
    bad = 0
    for fg, bg in TEXT_PAIRS:
        r = contrast(C[fg], C[bg])
        ok = r >= 4.5
        bad += not ok
        print(f"{'OK ' if ok else 'BAD'} {fg:9} on {bg:10} {r:5.2f}")
    raise SystemExit(bad)
