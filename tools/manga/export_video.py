"""Export finished pages and text-free panel art for the narrated-video session.

  python tools/manga/export_video.py story/chapter01/script.yaml output/ch01 video/ch01 --pages 1-7

Writes JPEG (quality 92) copies to <dest>/pages/page_NN.jpg and
<dest>/panels/pNN_i.jpg (generated art only; drawn screens, clocks and
phones exist only on the pages) and refreshes <dest>/manifest.json.
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import PAGE_H, PAGE_W, load_chapter, panel_id, panel_rects  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("outdir")
    ap.add_argument("dest")
    ap.add_argument("--pages", required=True, help="range such as 1-7")
    a = ap.parse_args()
    lo, _, hi = a.pages.partition("-")
    chapter = load_chapter(a.script)
    src, dest = Path(a.outdir), Path(a.dest)
    (dest / "pages").mkdir(parents=True, exist_ok=True)
    (dest / "panels").mkdir(parents=True, exist_ok=True)
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"pages": {}}
    manifest.update({"page_size": [PAGE_W, PAGE_H], "reading_order": "right-to-left",
                     "source_spec": a.script})
    for spec in chapter["pages"]:
        n = spec["page"]
        if not int(lo) <= n <= int(hi or lo):
            continue
        Image.open(src / "pages" / f"page_{n:02d}.png").convert("RGB").save(
            dest / "pages" / f"page_{n:02d}.jpg", quality=92)
        panels = []
        for i, (panel, rect) in enumerate(zip(spec["panels"], panel_rects(spec["rows"])), start=1):
            pid = panel_id(n, i)
            entry = {"id": pid, "kind": panel.get("kind", "art"), "box": list(rect)}
            art = src / "panels" / f"{pid}.png"
            if entry["kind"] == "art" and art.exists():
                Image.open(art).convert("L").save(dest / "panels" / f"{pid}.jpg", quality=92)
                entry["art"] = f"panels/{pid}.jpg"
                # the page shows a cover-crop of this uncropped render, centred on `focus`
                entry["crop_focus"] = list(panel.get("focus", (0.5, 0.5)))
            panels.append(entry)
        manifest["pages"][str(n)] = {"image": f"pages/page_{n:02d}.jpg", "panels": panels}
        print(f"exported page {n}")
    manifest["pages"] = dict(sorted(manifest["pages"].items(), key=lambda kv: int(kv[0])))
    manifest_path.write_text(json.dumps(manifest, indent=1) + "\n")


if __name__ == "__main__":
    main()
