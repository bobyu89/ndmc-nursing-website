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

DEPT_NODE = {
    "A": "100180/6510",
    "B": "100010/1628",
    "B-3": "100180/6798",
    "C-2-2": "100010/1471",
    "E": "100010/4575",
    "F-1-1": "100010/1492",
    "F-1-3": "100010/3642",
    "I-1": "100180/6796",
    "J": "100180/6681",
    "J-1": "100180/6798",
    "J-2": "100180/6810",
    "K": "100180/6799",
}

INST_NODE = {
    "A": "100181/6511",
    "B": "100010/1628",
    "B-4": "100181/6802",
    "D-2": "100181/6802",
    "G": "100181/6533",
    "G-1": "100181/6533",
    "G-2": "100181/6794",
}

# English sites: no live nodes yet (an orphan uniten/100010/843 exists in the CMS).
EN_NODE, EN_DEPT_NODE, EN_INST_NODE = {}, {}, {}

EXTERNAL = {
    "facebook": "https://www.facebook.com/",
}


def L(pid):
    """Public URL for a Notion page ID. College IDs are bare ("C-1"); department and institute IDs
    carry a prefix ("dept:C-1", "inst:F-1"). Unbuilt nodes return a visible '#待建-ID' anchor."""
    if pid == "J":
        return L("en:A")
    if pid in EXTERNAL:
        return EXTERNAL[pid]
    site, _, key = pid.rpartition(":")
    table = {"": NODE, "dept": DEPT_NODE, "inst": INST_NODE,
             "en": EN_NODE, "en_dept": EN_DEPT_NODE, "en_inst": EN_INST_NODE}[site]
    if key in table:
        return f"{SITE}/unit/{table[key]}"
    return f"#待建-{pid.replace(':', '-')}"
