"""Write the readable PAGE/PANEL manga script from a chapter spec.

  python tools/manga/script_md.py story/chapter01/script.yaml story/chapter01/script.md
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import load_chapter  # noqa: E402

KIND_NOTE = {
    "clock": "Drawn element (not generated art)",
    "phone": "Drawn element (not generated art)",
    "screen": "System screen. Text exactly as below.",
    "rules": "System screen. Text exactly as below.",
    "timer": "System screen.",
    "grid": "System screen. Only the five recovered records are readable.",
    "card": "System screen.",
}
LABEL = {"speech": "", "offpanel": " (off-panel)", "shout": " (shout)", "thought": " (thought)"}


def mark(item):
    return "" if item.get("canon") else " †"


def main(src, dst):
    ch = load_chapter(src)
    out = [
        f"# DEAD MAN'S ALGORITHM — Chapter {ch['chapter']}: {ch['title']}",
        "",
        "Reconstruction draft 1, generated from `script.yaml`.",
        "",
        "**Legend**",
        "- Unmarked dialogue and screen text is **CONFIRMED CANON**: verbatim from `story_bible.md`.",
        "- **†** marks new dialogue or captions written for this draft: **PROPOSAL — NOT CANON**.",
        "- Artist directions are separate from lettered text.",
        "- Right-to-left reading order is a PROPOSAL.",
        "",
        "**Character visual designs used for the art (PROPOSAL — NOT CANON)**",
        "",
        "The bible confirms only Aoi's glasses, Haruto's blond or light hair, Gō's strength and Momo's design.",
        "",
    ]
    for name, tags in ch["characters"].items():
        out.append(f"- {name}: {tags}")
    scene = None
    for page in ch["pages"]:
        if page.get("scene") != scene:
            scene = page.get("scene")
            out += ["", "---", "", f"## Scene {scene}"]
        out += ["", f"### PAGE {page['page']}"]
        if page.get("note"):
            out.append(f"*Page note: {page['note']}*")
        for i, panel in enumerate(page["panels"], start=1):
            out += ["", f"**PANEL {i} — {panel['shot']}**", f"- Art: {panel['art']}"]
            kind = panel.get("kind", "art")
            if kind in KIND_NOTE:
                out.append(f"- {KIND_NOTE[kind]}")
            for line in panel.get("lines", []):
                out.append(f"  - SCREEN: `{line['s']}`{mark(line)}")
            if kind == "timer":
                out.append(f"  - SCREEN: `{panel['time']}`")
            if panel.get("overlay_timer"):
                out.append(f"  - SCREEN (overlay): `{panel['overlay_timer']}`")
            for item in panel.get("text", []):
                t = item["t"]
                if t == "sfx":
                    out.append(f"- SFX: {item['say']}")
                elif t == "stamp":
                    out.append(f"- CAPTION (time stamp): {item['say']}{mark(item)}")
                elif t == "caption":
                    out.append(f"- CAPTION: \"{item['say']}\"{mark(item)}")
                else:
                    out.append(f"- {item['who']}{LABEL[t]}: \"{item['say']}\"{mark(item)}")
            if panel.get("clue"):
                out.append(f"- Visual clue: {panel['clue']}")
            if panel.get("note"):
                out.append(f"- Continuity note: {panel['note']}")
    Path(dst).write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main(*sys.argv[1:3])
