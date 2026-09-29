"""Where every Notion page ID lives on the public site. New nodes get real node numbers once created in the CMS."""

from tokens import SITE

NODE = {
    "A": "100010/16",
    "B": "100010/1628",
    "C-2": "100010/1458",
    "C-3": "100010/1460",
    "D-1": "100180/6510",
    "D-2": "100181/6511",
    "E-1": "100010/716",
    "E-3": "100010/1463",
    "F": "100143/1861",
    "F-2": "100010/4575",
    "H-1": "100010/6333",
    "H-2": "100010/1463",
    "H-3": "100010/729",
    "K": "100010/2199",
    "L": "100010/934",
}

EXTERNAL = {
    "J": "#English-site-pending",
    "facebook": "https://www.facebook.com/",
}


def L(pid):
    """Public URL for a Notion page ID; unbuilt nodes return a visible '#待建-ID' anchor."""
    if pid in EXTERNAL:
        return EXTERNAL[pid]
    if pid in NODE:
        return f"{SITE}/unit/{NODE[pid]}"
    return f"#待建-{pid}"
