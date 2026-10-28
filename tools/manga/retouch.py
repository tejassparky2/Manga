"""Small, recorded hand fixes to rendered panels (no new content, only removing a mistake).

Each fix starts from the untouched render, kept as output/chNN/panels/raw/<pid>.png, so
running this again gives the same result. Each panel's script entry notes its retouch.

  python tools/manga/retouch.py            # apply every fix whose raw render exists
"""
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))


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


def _perspective(dst, src):
    """Coefficients for Image.transform(PERSPECTIVE): output point -> source point."""
    rows, rhs = [], []
    for (x, y), (u, v) in zip(dst, src):
        rows += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        rhs += [u, v]
    return np.linalg.solve(np.array(rows, float), np.array(rhs, float)).tolist()


def ch04_p09_3(im):
    """The render drew a face on Ren's page. Repaint the page with what he draws: lockers A-E
    (the same diagram as page 10), in perspective, leaving his hands and pencil untouched."""
    from compose import draw_notebook
    quad = [(395, 502), (622, 666), (445, 817), (250, 660)]          # inner frame: TL, TR, BR, BL
    cx, cy = sum(p[0] for p in quad) / 4, sum(p[1] for p in quad) / 4
    inner = [(cx + (x - cx) * 0.9, cy + (y - cy) * 0.9) for x, y in quad]
    keep = Image.new("L", im.size, 0)                                # hands and pencil stay as drawn
    kd = ImageDraw.Draw(keep)
    kd.polygon([(500, 570), (555, 562), (602, 595), (598, 662), (552, 703), (493, 688), (472, 660), (468, 624)], fill=255)
    kd.polygon([(306, 450), (348, 450), (348, 572), (318, 545)], fill=255)
    keep = keep.filter(ImageFilter.MaxFilter(9))
    area = Image.new("L", im.size, 0)
    ImageDraw.Draw(area).polygon(inner, fill=255)
    area = Image.composite(Image.new("L", im.size, 0), area, keep).filter(ImageFilter.GaussianBlur(2))
    im = Image.composite(Image.new("RGB", im.size, (241, 241, 241)), im, area)           # blank paper
    W, H = 600, 420
    art = draw_notebook(W, H, "boxes", (0.5, 0.5)).convert("L")
    lines = art.point(lambda v: 255 if v < 120 else 0)                                  # pencil strokes only
    coeffs = _perspective(inner, [(0, 0), (W, 0), (W, H), (0, H)])
    warped = lines.transform(im.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    warped = Image.composite(Image.new("L", im.size, 0), warped, keep).point(lambda v: int(v * 0.7))
    return Image.composite(Image.new("RGB", im.size, (90, 90, 90)), im, warped)


def ch04_p02_3(im):
    """A tiny girl stands inside the dark doorway (read as Saki's ghost: not canon). The doorway shades
    evenly left to right, so each row is repainted from just beside the figure."""
    px = im.load()
    for y in range(398, 476):
        for x in range(578, 612):
            px[x, y] = px[570, y]
    return im


def ch04_p03_2(im):
    """Two fake-kanji glyphs on the small lock plate of Saki's locker read as text (not canon).
    Each glyph's rows are repainted from the plain plate just beside it."""
    px = im.load()
    for x0, x1, src in ((403, 432, 398), (490, 520, 486)):
        for y in range(392, 424):
            for x in range(x0, x1):
                px[x, y] = px[src, y]
    return im


def ch05_p16_3(im):
    """The coin in Kota's notebook rendered as a shiny sphere (reads as a pearl). Repaint the page
    behind it, then draw a flat coin lying in the gutter: edge, face, rim, a glint."""
    x0, y0, x1, y1 = 343, 565, 486, 706
    # the page four ruled lines (4 x 42 px) higher, through a soft round mask the size of the sphere
    patch = im.crop((x0, y0 - 168, x1, y1 - 168))
    mask = Image.new("L", patch.size, 0)
    ImageDraw.Draw(mask).ellipse([413.5 - x0 - 70, 634.5 - y0 - 70, 413.5 - x0 + 70, 634.5 - y0 + 70], fill=255)
    im.paste(patch, (x0, y0), mask.filter(ImageFilter.GaussianBlur(3)))
    k, box = 4, (x0, y0, x1, y1)
    big = im.crop(box).resize(((x1 - x0) * k, (y1 - y0) * k), Image.LANCZOS)
    d = ImageDraw.Draw(big)
    cx, cy, rx, ry = (413 - x0) * k, (630 - y0) * k, 58 * k, 46 * k

    def ell(dx, dy, sx, sy):
        return [cx + dx - sx, cy + dy - sy, cx + dx + sx, cy + dy + sy]
    d.ellipse(ell(6 * k, 12 * k, rx, ry), fill=(206, 206, 206))                      # shadow on the page
    d.ellipse(ell(0, 7 * k, rx, ry), fill=(70, 70, 70))                             # the coin's edge
    d.ellipse(ell(0, 0, rx, ry), fill=(168, 168, 168), outline=(35, 35, 35), width=3 * k)
    d.ellipse(ell(0, 0, rx * 0.78, ry * 0.78), outline=(95, 95, 95), width=2 * k)   # raised rim
    d.arc(ell(0, 0, rx * 0.9, ry * 0.9), 200, 290, fill=(245, 245, 245), width=3 * k)  # glint
    im.paste(big.filter(ImageFilter.GaussianBlur(k * 0.6)).resize((x1 - x0, y1 - y0), Image.LANCZOS), box[:2])
    return im


def ch05_p04_3(im):
    """A photograph of a figure lies on the floor by Riku (a prop that reads as a clue: not canon).
    Each row of the floor under it is repainted by blending the floor just left and right of it."""
    quad = [(506, 739), (704, 738), (821, 868), (622, 884)]
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).polygon(quad, fill=255)
    mask = mask.filter(ImageFilter.MaxFilter(7))
    px, m = im.load(), mask.load()
    for y in range(730, 896):
        xs = [x for x in range(480, 860) if m[x, y]]
        if not xs:
            continue
        xl, xr = xs[0] - 4, min(xs[-1] + 4, im.width - 1)
        a, b = px[xl, y], px[xr, y]
        if sum(b) < 3 * 150:                              # the right edge touches his trouser leg: use the floor
            b = a
        for x in xs:
            t = (x - xl) / (xr - xl)
            px[x, y] = tuple(int(a[c] + (b[c] - a[c]) * t) for c in range(3))
    soft = im.filter(ImageFilter.GaussianBlur(1.5))
    im.paste(soft, (0, 0), mask.filter(ImageFilter.GaussianBlur(3)))
    return im


def ch05_p20_2(im):
    """The lone figure in front (Ren, from behind) came out with a bob: Aoi's silhouette. Repaint
    the background behind the head, then draw Ren's short, messy hair over a visible nape."""
    import math
    px = im.load()
    for y in range(768, 889):                                       # background, row by row
        a, b = px[628, y], px[742, y]
        for x in range(630, 741):
            t = (x - 628) / (742 - 628)
            px[x, y] = tuple(int(a[c] + (b[c] - a[c]) * t) for c in range(3))
    k, box = 4, (620, 760, 750, 900)
    big = im.crop(box).resize(((box[2] - box[0]) * k, (box[3] - box[1]) * k), Image.LANCZOS)
    d = ImageDraw.Draw(big)

    def P(x, y):
        return ((x - box[0]) * k, (y - box[1]) * k)
    import random
    rnd = random.Random(2002)
    d.rectangle([*P(675, 868), *P(695, 892)], fill=(62, 62, 61))     # a little nape above the collar
    cx, cy, rx, ry = 685, 840, 33, 35
    d.ellipse([*P(cx - rx, cy - ry), *P(cx + rx, cy + ry)], fill=(18, 18, 18))
    for i in range(11):                                             # soft clumps round the crown and sides
        a = math.pi * (0.95 + 1.1 * i / 10) + rnd.uniform(-0.1, 0.1)
        rr = rnd.uniform(9, 13)
        x, y = cx + (rx + 1) * math.cos(a), cy + (ry + 1) * math.sin(a)
        d.ellipse([*P(x - rr, y - rr), *P(x + rr, y + rr)], fill=(18, 18, 18))
    for a, ln in ((3.6, 10), (4.3, 12), (5.0, 11), (5.7, 9)):      # a few wisps sticking out
        x, y = cx + (rx + 8) * math.cos(a), cy + (ry + 8) * math.sin(a)
        d.polygon([P(x - 4 * math.sin(a), y + 4 * math.cos(a)), P(x + 4 * math.sin(a), y - 4 * math.cos(a)),
                   P(x + ln * math.cos(a), y + ln * math.sin(a))], fill=(18, 18, 18))
    for dx, ln in ((-16, 8), (-6, 12), (4, 10), (15, 7)):           # uneven strands over the nape
        d.polygon([P(cx + dx - 6, 868), P(cx + dx + 6, 868), P(cx + dx + 2, 868 + ln)], fill=(18, 18, 18))
    im.paste(big.filter(ImageFilter.GaussianBlur(k * 1.8)).resize((box[2] - box[0], box[3] - box[1]), Image.LANCZOS),
             box[:2])
    return im


RETOUCH = {"ch04/p01_1": ch04_p01_1, "ch04/p19_1": ch04_p19_1, "ch04/p09_3": ch04_p09_3, "ch04/p02_3": ch04_p02_3, "ch04/p03_2": ch04_p03_2, "ch05/p16_3": ch05_p16_3, "ch05/p04_3": ch05_p04_3, "ch05/p20_2": ch05_p20_2}


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
