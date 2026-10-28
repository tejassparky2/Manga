"""Small, recorded hand fixes to rendered panels (no new content, only removing a mistake).

Each fix starts from the untouched render, kept as output/chNN/panels/raw/<pid>.png, so
running this again gives the same result. Each panel's script entry notes its retouch.

  python tools/manga/retouch.py            # apply every fix whose raw render exists
"""
import shutil
from pathlib import Path

from PIL import Image, ImageDraw


def ch04_p01_1(im):
    """A tiny figure stands inside the doorway; "Nobody moved first." Shift empty doorway over it."""
    im.paste(im.crop((372, 612, 404, 704)), (406, 612))
    return im


def ch04_p19_1(im):
    """The lone figure has a spiky crown (reads as Haruto). Repaint a smooth, slicked-back head (Riku)."""
    k, box = 4, (588, 364, 634, 404)
    big = im.crop(box).resize(((box[2] - box[0]) * k, (box[3] - box[1]) * k), Image.NEAREST)
    d = ImageDraw.Draw(big)
    px = im.load()
    for y in range(box[3] - box[1]):                     # background, row by row, from beside the figure
        d.rectangle([0, y * k, big.width, (y + 1) * k], fill=px[578, box[1] + y])
    cx, top, bot = (610.5 - box[0]) * k, (382 - box[1]) * k, (406 - box[1]) * k
    d.ellipse([cx - 9.5 * k, top, cx + 9.5 * k, bot], fill=(16, 16, 16))
    d.rectangle([cx - 5 * k, (399 - box[1]) * k, cx + 5 * k, big.height], fill=(16, 16, 16))
    im.paste(big.resize((box[2] - box[0], box[3] - box[1]), Image.LANCZOS), box[:2])
    return im


RETOUCH = {"ch04/p01_1": ch04_p01_1, "ch04/p19_1": ch04_p19_1}


def main(root=Path("output")):
    for key, fix in RETOUCH.items():
        ch, pid = key.split("/")
        panel, raw = root / ch / "panels" / f"{pid}.png", root / ch / "panels" / "raw" / f"{pid}.png"
        if not raw.exists():
            if not panel.exists():
                continue
            raw.parent.mkdir(exist_ok=True)
            shutil.copy(panel, raw)
        fix(Image.open(raw).convert("RGB")).save(panel)
        print("retouched", key)


if __name__ == "__main__":
    main()
