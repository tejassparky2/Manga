"""Draw layout sketches for panels the model cannot compose from text alone.

render_panels.py repaints a panel from its sketch (`sketch:` in the script), so
the sketch fixes what text prompts kept getting wrong: the room's shape, the
size of the metal door, how many students stand in it. Shapes and tones only;
the model draws the people and the detail.

  python tools/manga/sketches.py          # writes story/chapterNN/sketches/*.png
"""
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

GAKURAN, SKIN, HAIR, WHITE = (28, 28, 28), (205, 205, 205), (18, 18, 18), (235, 235, 235)


def concrete(w, h, base, seed, grain=14):
    rnd = random.Random(seed)
    noise = Image.new("L", (w // 4, h // 4))
    noise.putdata([max(0, min(255, base + rnd.randint(-grain, grain))) for _ in range(noise.width * noise.height)])
    return noise.resize((w, h), Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.5)).convert("RGB")


def light_pool(img, cx, cy, rx, ry, gain=40):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=gain)
    mask = mask.filter(ImageFilter.GaussianBlur(min(rx, ry) // 2))
    return Image.composite(Image.new("RGB", img.size, (255, 255, 255)), img, mask)


def vignette(img, strength=150):
    w, h = img.size
    mask = Image.new("L", (w, h), strength)
    ImageDraw.Draw(mask).ellipse([w * 0.08, h * 0.05, w * 0.92, h * 0.95], fill=0)
    mask = mask.filter(ImageFilter.GaussianBlur(min(w, h) // 6))
    return Image.composite(Image.new("RGB", (w, h), (10, 10, 10)), img, mask)


def metal_door(d, x0, y0, x1, y1, frame=18, bands=3, double=True):
    """A heavy riveted steel door: dark frame, banded slab, rivet rows, centre seam."""
    d.rectangle([x0 - frame, y0 - frame, x1 + frame, y1], fill=(34, 34, 34))
    d.rectangle([x0, y0, x1, y1], fill=(140, 140, 140))
    d.rectangle([x0, y0, x0 + (x1 - x0) // 9, y1], fill=(158, 158, 158))  # light catching one edge
    band_h = max(8, (y1 - y0) // 22)
    step = max(10, (x1 - x0) // 18)
    for k in range(1, bands + 1):
        y = y0 + (y1 - y0) * k // (bands + 1)
        d.rectangle([x0, y - band_h // 2, x1, y + band_h // 2], fill=(98, 98, 98))
        for x in range(x0 + step // 2, x1, step):
            r = max(2, band_h // 4)
            d.ellipse([x - r, y - r, x + r, y + r], fill=(196, 196, 196), outline=(40, 40, 40))
    if double:
        cx = (x0 + x1) // 2
        d.rectangle([cx - 3, y0, cx + 3, y1], fill=(22, 22, 22))
    for y in (y0 + (y1 - y0) // 7, y1 - (y1 - y0) // 7):  # hinge blocks on the frame
        d.rectangle([x0 - frame - 6, y - band_h, x0 - 4, y + band_h], fill=(64, 64, 64))
        d.rectangle([x1 + 4, y - band_h, x1 + frame + 6, y + band_h], fill=(64, 64, 64))


def student(d, x, y, s, girl, rnd):
    """A small high-angle figure standing with its feet at (x, y), about 110*s px tall."""
    d.ellipse([x - 22 * s, y - 6 * s, x + 22 * s, y + 6 * s], fill=(60, 60, 60))  # shadow
    head = 15 * s
    top = y - 110 * s
    if girl:
        d.rectangle([x - 9 * s, y - 34 * s, x - 3 * s, y], fill=SKIN)  # legs
        d.rectangle([x + 3 * s, y - 34 * s, x + 9 * s, y], fill=SKIN)
        d.polygon([(x - 13 * s, y - 62 * s), (x + 13 * s, y - 62 * s), (x + 20 * s, y - 32 * s),
                   (x - 20 * s, y - 32 * s)], fill=GAKURAN)  # skirt
        d.rounded_rectangle([x - 16 * s, top + 28 * s, x + 16 * s, y - 58 * s], 6 * s, fill=GAKURAN)
        d.polygon([(x - 16 * s, top + 30 * s), (x + 16 * s, top + 30 * s), (x, top + 46 * s)], fill=WHITE)  # collar
        d.ellipse([x - head * 1.15, top - 2 * s, x + head * 1.15, top + 2 * head + 8 * s], fill=HAIR)  # long hair
    else:
        d.rectangle([x - 11 * s, y - 46 * s, x - 2 * s, y], fill=GAKURAN)  # trousers
        d.rectangle([x + 2 * s, y - 46 * s, x + 11 * s, y], fill=GAKURAN)
        d.rounded_rectangle([x - 18 * s, top + 26 * s, x + 18 * s, y - 40 * s], 6 * s, fill=GAKURAN)
        d.ellipse([x - head, top, x + head, top + 2 * head], fill=HAIR)
    face = rnd.choice((-1, 0, 1))  # which way the student is looking
    fx = x + face * head * 0.45
    d.ellipse([fx - head * 0.55, top + head * 0.8, fx + head * 0.55, top + head * 1.9], fill=SKIN)


def chamber_wide(w=1152, h=896, seed=1501):
    """Ch1 p15_1: the whole chamber from above. Concrete box, the huge metal door
    and the dark screen on the back wall, twenty students scattered on the floor."""
    rnd = random.Random(seed)
    img = concrete(w, h, 150, seed)
    d = ImageDraw.Draw(img)
    back_y, side = int(h * 0.34), int(w * 0.12)
    wall = concrete(w, h, 78, seed + 1)
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rectangle([side, 0, w - side, back_y], fill=255)
    img.paste(wall, (0, 0), mask)
    sides = concrete(w, h, 60, seed + 2)
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.polygon([(0, 0), (side, 0), (side, back_y), (0, int(h * 0.6))], fill=255)
    md.polygon([(w, 0), (w - side, 0), (w - side, back_y), (w, int(h * 0.6))], fill=255)
    img.paste(sides, (0, 0), mask)
    d = ImageDraw.Draw(img)
    d.line([(side, back_y), (w - side, back_y)], fill=(40, 40, 40), width=4)
    d.line([(side, back_y), (0, int(h * 0.6))], fill=(40, 40, 40), width=4)
    d.line([(w - side, back_y), (w, int(h * 0.6))], fill=(40, 40, 40), width=4)
    metal_door(d, int(w * 0.19), int(back_y * 0.12), int(w * 0.42), back_y)
    sx0, sy0, sx1, sy1 = int(w * 0.55), int(back_y * 0.18), int(w * 0.84), int(back_y * 0.78)
    d.rectangle([sx0 - 8, sy0 - 8, sx1 + 8, sy1 + 8], fill=(48, 48, 48))
    d.rectangle([sx0, sy0, sx1, sy1], fill=(12, 12, 12))
    img = light_pool(img, w // 2, int(h * 0.68), int(w * 0.42), int(h * 0.3), gain=55)
    d = ImageDraw.Draw(img)
    rows = [(back_y + 70, 5), (back_y + 190, 5), (back_y + 330, 5), (h - 50, 5)]  # 4 x 5 = 20 students
    figures = []
    for y, n in rows:
        t = (y - back_y) / (h - back_y)
        half = (w / 2 - side) + t * side * 1.6
        for k in range(n):
            x = w / 2 - half * 0.86 + (2 * half * 0.86) * (k + 0.5) / n + rnd.uniform(-30, 30)
            figures.append((y + rnd.uniform(-18, 18), x, 0.6 + t * 0.75))
    girls = set(rnd.sample(range(20), 9))
    for idx, (y, x, s) in enumerate(sorted(figures)):
        student(d, x, y, s, idx in girls, rnd)
    return vignette(img, 120)


def door_push(w=1344, h=768, seed=1604):
    """Ch1 p16_4: Gō and Riku, from behind, shoulders against the huge metal door,
    which fills the panel and dwarfs them."""
    img = concrete(w, h, 88, seed)
    d = ImageDraw.Draw(img)
    floor_y = int(h * 0.86)
    d.rectangle([0, floor_y, w, h], fill=(112, 112, 112))
    metal_door(d, int(w * 0.2), int(h * 0.05), int(w * 0.8), floor_y, frame=30, bands=3)
    img = light_pool(img, w // 2, int(h * 0.2), int(w * 0.3), int(h * 0.25), gain=35)
    d = ImageDraw.Draw(img)
    for x, s, broad in ((w * 0.43, 1.0, True), (w * 0.58, 0.92, False)):
        base = h - 14
        top = base - 360 * s
        d.ellipse([x - 70 * s, base - 12, x + 70 * s, base + 10], fill=(70, 70, 70))  # shadow
        d.polygon([(x - 34 * s, base - 170 * s), (x - 6 * s, base - 170 * s), (x - 14 * s, base), (x - 40 * s, base)],
                  fill=GAKURAN)  # legs braced apart
        d.polygon([(x + 6 * s, base - 170 * s), (x + 34 * s, base - 170 * s), (x + 46 * s, base), (x + 18 * s, base)],
                  fill=GAKURAN)
        sh = 62 * s if broad else 50 * s
        d.polygon([(x - sh, top + 70 * s), (x + sh, top + 70 * s), (x + 40 * s, base - 160 * s),
                   (x - 40 * s, base - 160 * s)], fill=GAKURAN)  # back of the jacket
        for side in (-1, 1):  # arms up, palms flat on the door
            hx = x + side * (sh + 30 * s)
            d.line([(x + side * sh * 0.8, top + 80 * s), (hx, top + 10 * s)], fill=GAKURAN, width=int(30 * s))
            d.ellipse([hx - 13 * s, top - 6 * s, hx + 13 * s, top + 22 * s], fill=SKIN)
        r = 30 * s if broad else 33 * s
        d.ellipse([x - r, top - 4 * s, x + r, top + 2 * r - 4 * s], fill=(40, 40, 40) if broad else HAIR)
    return vignette(img, 140)


def frozen_class(w=1536, h=640, seed=2004):
    """Ch1 p20_4 and p21_2: the class standing frozen in two loose rows, facing the
    viewer (and Momo), in the dark concrete chamber with light on their faces.
    The sealed door stays out of frame."""
    rnd = random.Random(seed)
    k = h / 640
    n = max(4, round(7 * w / 1536 / k))
    img = concrete(w, h, 62, seed)
    d = ImageDraw.Draw(img)
    d.rectangle([0, int(h * 0.72), w, h], fill=(92, 92, 92))
    img = light_pool(img, w // 2, int(h * 0.62), int(w * 0.45), int(h * 0.4), gain=45)
    d = ImageDraw.Draw(img)
    figures = [(h * 0.8, w * (i + 0.5) / n + rnd.uniform(-25, 25) * k, 2.6 * k) for i in range(n)]
    figures += [(h + 40 * k, w * (i + 1) / n + rnd.uniform(-25, 25) * k, 3.4 * k) for i in range(n - 1)]
    for idx, (y, x, s) in enumerate(figures):
        student(d, x, y, s, idx % 3 == 1, rnd)
    return vignette(img, 120)


def old_key(length, angle=0, tone=(200, 200, 200)):
    """An old metal key on a transparent layer: ring bow, shaft, toothed bit."""
    L = int(length)
    layer = Image.new("RGBA", (L + 20, L // 2 + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cy, r, shaft = layer.height // 2, L // 7, max(6, L // 22)
    edge = (60, 60, 60, 255)
    d.ellipse([10, cy - r, 10 + 2 * r, cy + r], fill=tone + (255,), outline=edge, width=3)
    d.ellipse([10 + r // 2, cy - r // 2, 10 + r * 3 // 2, cy + r // 2], fill=(0, 0, 0, 0), outline=edge, width=3)
    d.rectangle([10 + 2 * r - 4, cy - shaft, L, cy + shaft], fill=tone + (255,), outline=edge, width=2)
    for k, depth in enumerate((3.2, 2.2, 3.0)):  # the bit's teeth
        x = L - (k + 1) * L // 12
        d.rectangle([x, cy + shaft - 2, x + L // 16, cy + shaft * depth], fill=tone + (255,), outline=edge, width=2)
    d.line([(10 + 2 * r, cy - shaft // 2), (L - 6, cy - shaft // 2)], fill=(245, 245, 245, 255), width=2)  # shine
    return layer.rotate(angle, expand=True, resample=Image.BICUBIC)


def key_case(w=1152, h=896, seed=2301):
    """Ch1 p23_1: the exit key on a pedestal behind glass under a spotlight, the
    empty token containers in a ring around it, in the dark chamber."""
    img = concrete(w, h, 46, seed)
    d = ImageDraw.Draw(img)
    beam = Image.new("L", (w, h), 0)
    ImageDraw.Draw(beam).polygon([(w * 0.44, 0), (w * 0.56, 0), (w * 0.68, h * 0.78), (w * 0.32, h * 0.78)], fill=70)
    img = Image.composite(Image.new("RGB", (w, h), (255, 255, 255)), img, beam.filter(ImageFilter.GaussianBlur(30)))
    img = light_pool(img, w // 2, int(h * 0.8), int(w * 0.3), int(h * 0.09), gain=90)
    d = ImageDraw.Draw(img)
    px0, px1, ptop, pbot = int(w * 0.33), int(w * 0.67), int(h * 0.56), int(h * 0.8)
    d.rectangle([px0, ptop, px1, pbot], fill=(120, 120, 120), outline=(30, 30, 30), width=3)  # pedestal
    d.polygon([(px0, ptop), (px1, ptop), (px1 - 14, ptop - 18), (px0 + 14, ptop - 18)], fill=(170, 170, 170))
    gx0, gx1, gtop = px0 + 18, px1 - 18, int(h * 0.22)
    glass = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glass)
    gd.rectangle([gx0, gtop, gx1, ptop - 18], fill=(220, 220, 220, 40), outline=(235, 235, 235, 255), width=3)
    gd.line([(gx0 + 20, gtop + 30), (gx0 + 60, gtop + 120)], fill=(255, 255, 255, 160), width=6)  # reflection
    img = Image.alpha_composite(img.convert("RGBA"), glass)
    key = old_key((gx1 - gx0) * 0.9, angle=0)
    img.alpha_composite(key, (int((gx0 + gx1 - key.width) / 2), int(ptop - 18 - key.height * 0.8)))
    img = img.convert("RGB")
    d = ImageDraw.Draw(img)
    for k in range(10):  # empty transparent token containers on the floor, either side
        t = k / 9
        if abs(t - 0.5) < 0.2:
            continue
        x = w * (0.08 + 0.84 * t)
        y = h * (0.84 + 0.1 * (1 - abs(2 * t - 1)))
        cw, ch = w * 0.045, h * 0.17
        d.rectangle([x - cw, y - ch, x + cw, y], outline=(200, 200, 200), width=3)
        d.ellipse([x - cw, y - ch - cw * 0.35, x + cw, y - ch + cw * 0.35], outline=(220, 220, 220), width=3)
        d.ellipse([x - cw, y - cw * 0.35, x + cw, y + cw * 0.35], outline=(150, 150, 150), width=3)
    return vignette(img, 160)


def key_title(w=832, h=1216, seed=2011):
    """Ch2 p01_1 (title splash): the exit key on a pedestal behind glass, one
    spotlight from above, dark room. The top third stays clear for the title."""
    img = concrete(w, h, 40, seed)
    beam = Image.new("L", (w, h), 0)
    ImageDraw.Draw(beam).polygon([(w * 0.38, 0), (w * 0.62, 0), (w * 0.86, h * 0.9), (w * 0.14, h * 0.9)], fill=60)
    img = Image.composite(Image.new("RGB", (w, h), (255, 255, 255)), img, beam.filter(ImageFilter.GaussianBlur(40)))
    img = light_pool(img, w // 2, int(h * 0.88), int(w * 0.4), int(h * 0.06), gain=90)
    d = ImageDraw.Draw(img)
    px0, px1, ptop, pbot = int(w * 0.25), int(w * 0.75), int(h * 0.6), int(h * 0.88)
    d.rectangle([px0, ptop, px1, pbot], fill=(70, 70, 70), outline=(20, 20, 20), width=3)
    d.polygon([(px0, ptop), (px1, ptop), (px1 - 16, ptop - 22), (px0 + 16, ptop - 22)], fill=(150, 150, 150))
    gx0, gx1, gtop = px0 + 20, px1 - 20, int(h * 0.34)
    glass = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glass)
    gd.rectangle([gx0, gtop, gx1, ptop - 22], fill=(220, 220, 220, 36), outline=(235, 235, 235, 255), width=3)
    gd.line([(gx0 + 24, gtop + 30), (gx0 + 70, gtop + 150)], fill=(255, 255, 255, 150), width=7)
    img = Image.alpha_composite(img.convert("RGBA"), glass)
    key = old_key((gx1 - gx0) * 0.85)
    img.alpha_composite(key, (int((w - key.width) / 2), int(ptop - 22 - key.height * 0.8)))
    return vignette(img.convert("RGB"), 150)


def key_closeup(w=896, h=1152, seed=2302):
    """Ch1 p23_2: close-up of the old metal key lying on the pedestal, glass
    reflections in front, black background."""
    img = Image.new("RGB", (w, h), (14, 14, 14))
    d = ImageDraw.Draw(img)
    top = int(h * 0.62)
    d.polygon([(0, top), (w, top), (w, h), (0, h)], fill=(105, 105, 105))
    img = light_pool(img, w // 2, int(h * 0.68), int(w * 0.4), int(h * 0.12), gain=110)
    img = img.convert("RGBA")
    key = old_key(w * 0.82, angle=-6)
    img.alpha_composite(key, (int((w - key.width) / 2), int(top + h * 0.11 - key.height / 2)))
    glare = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glare)
    for x, wd in ((w * 0.18, 26), (w * 0.27, 9), (w * 0.72, 18)):
        gd.line([(x, 0), (x + w * 0.25, h)], fill=(255, 255, 255, 46), width=wd)
    img = Image.alpha_composite(img, glare.filter(ImageFilter.GaussianBlur(3)))
    return vignette(img.convert("RGB"), 120)


def finger(d, x0, y0, x1, y1, width, fill=SKIN):
    d.line([(x0, y0), (x1, y1)], fill=fill, width=int(width))
    r = width / 2
    d.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill=fill)


def coin_in_palm(w=832, h=1216, seed=3132):
    """Ch3 p13_2: hands only. A girl's open palm, one coin lying flat on it, and a
    boy's hand in a black sleeve letting go of it from above. White background."""
    img = Image.new("RGB", (w, h), (238, 238, 238))
    d = ImageDraw.Draw(img)
    cx, cy = w * 0.47, h * 0.68
    d.polygon([(cx - 120, cy + 120), (cx + 130, cy + 120), (cx + 150, h), (cx - 150, h)], fill=(214, 214, 214))  # wrist
    d.rectangle([cx - 170, h * 0.93, cx + 170, h], fill=GAKURAN)  # her sleeve cuff
    for k, (dx, length) in enumerate(((-100, 190), (-35, 230), (30, 220), (92, 170))):
        finger(d, cx + dx, cy - 90, cx + dx * 1.15, cy - 90 - length, 62)
    finger(d, cx - 140, cy + 20, cx - 270, cy - 90, 70)  # thumb
    d.ellipse([cx - 165, cy - 150, cx + 165, cy + 170], fill=SKIN, outline=(150, 150, 150), width=3)  # palm
    d.ellipse([cx - 75, cy - 45, cx + 75, cy + 45], fill=(150, 150, 150), outline=(70, 70, 70), width=4)  # the coin
    d.ellipse([cx - 58, cy - 33, cx + 58, cy + 33], outline=(110, 110, 110), width=3)
    d.polygon([(w, 0), (w, h * 0.22), (w * 0.78, h * 0.4), (w * 0.6, h * 0.3), (w * 0.72, 0)], fill=GAKURAN)  # his sleeve
    d.ellipse([w * 0.55, h * 0.3, w * 0.8, h * 0.47], fill=(196, 196, 196))  # his hand
    finger(d, w * 0.6, h * 0.42, cx + 30, cy - 70, 44, fill=(196, 196, 196))  # index finger to the coin
    finger(d, w * 0.66, h * 0.45, cx + 70, cy - 30, 44, fill=(196, 196, 196))  # thumb
    return img.filter(ImageFilter.GaussianBlur(1))


def empty_hands(w=832, h=1216, seed=3142):
    """Ch3 p14_2: the class in the bare white room, front row holding out empty
    open hands, the rest behind them."""
    rnd = random.Random(seed)
    img = Image.new("RGB", (w, h), (232, 232, 232))
    d = ImageDraw.Draw(img)
    d.rectangle([0, h * 0.62, w, h], fill=(210, 210, 210))  # floor
    rows = [(h * 0.47, 0.55, 5), (h * 0.68, 0.75, 4), (h * 0.99, 1.0, 3)]
    for row, (base, s, n) in enumerate(rows):
        for k in range(n):
            x = w * (k + 0.5) / n + rnd.uniform(-20, 20)
            girl = (k + row) % 2 == 1
            head = 40 * s
            top = base - 380 * s
            d.rounded_rectangle([x - 72 * s, top + 2 * head - 10 * s, x + 72 * s, base], 26 * s, fill=GAKURAN)
            if girl:
                d.polygon([(x - 62 * s, top + 2 * head), (x + 62 * s, top + 2 * head), (x, top + 2 * head + 80 * s)],
                          fill=WHITE)  # sailor collar
                d.ellipse([x - head * 1.2, top - 8 * s, x + head * 1.2, top + 2 * head + 50 * s], fill=HAIR)
            d.ellipse([x - head * 0.8, top + head * 0.45, x + head * 0.8, top + head * 2.1], fill=SKIN)  # face
            d.ellipse([x - head, top - 6 * s, x + head, top + head * 0.9], fill=HAIR)  # fringe
            if row == len(rows) - 1:  # front row: both hands out, palms up, empty
                for side in (-1, 1):
                    hx, hy = x + side * 52 * s, base - 170 * s
                    d.ellipse([hx - 38 * s, hy - 26 * s, hx + 38 * s, hy + 26 * s], fill=SKIN, outline=(120, 120, 120))
                    for f in range(4):
                        fx = hx - 27 * s + f * 18 * s
                        finger(d, fx, hy - 10 * s, fx + side * 4 * s, hy - 52 * s, 13 * s)
    return vignette(img, 60)


SKETCHES = {
    "chapter01": {"p15_1.png": chamber_wide, "p16_4.png": door_push, "p20_4.png": frozen_class,
                  "p21_2.png": lambda: frozen_class(1152, 896, seed=2102), "p23_1.png": key_case, "p23_2.png": key_closeup},
    "chapter02": {"p01_1.png": key_title, "p10_1.png": lambda: chamber_wide(seed=2101)},  # same chamber as Ch1 p15_1
    "chapter03": {"p13_2.png": coin_in_palm, "p14_2.png": empty_hands},
}


if __name__ == "__main__":
    story = Path(sys.argv[1] if len(sys.argv) > 1 else "story")
    for chapter, sketches in SKETCHES.items():
        out = story / chapter / "sketches"
        out.mkdir(parents=True, exist_ok=True)
        for name, draw in sketches.items():
            draw().save(out / name)
            print("wrote", out / name)
