"""Compose lettered manga pages from a chapter spec and rendered panel art.

  python tools/manga/compose.py story/chapter01/script.yaml output/ch01 [--pages 1-5]

Reads panel art from <out>/panels, writes <out>/pages/page_NN.png and, when all
pages are composed, <out>/<name>.pdf and <out>/<name>.cbz (right-to-left).
Panels whose art is not rendered yet are drawn as grey placeholders.
"""
import argparse
import math
import random
import sys
import zipfile
from pathlib import Path

import img2pdf
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import PAGE_H, PAGE_W, load_chapter, panel_id, panel_rects  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
FONTS = ROOT / "assets" / "fonts"
CJK_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
CJK_REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
RED = (200, 16, 46)
BORDER = 5
_font_cache = {}


def font(name, size):
    key = (name, size)
    if key not in _font_cache:
        path, index = {
            "dialogue": (FONTS / "ComicNeue-Bold.ttf", 0),
            "sfx": (FONTS / "Bangers-Regular.ttf", 0),
            "sans": (CJK_BOLD, 0),
            "sans-reg": (CJK_REG, 0),
            "mono": (CJK_BOLD, 5),
        }[name]
        _font_cache[key] = ImageFont.truetype(str(path), size, index=index)
    return _font_cache[key]


# ------------------------------------------------------------------ text layout

def wrap(text, fnt, max_w):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if fnt.getlength(trial) <= max_w or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def text_block(text, fnt, max_w, spacing=1.12):
    lines = wrap(text, fnt, max_w)
    asc, desc = fnt.getmetrics()
    lh = round((asc + desc) * spacing)
    w = max(fnt.getlength(l) for l in lines)
    return lines, w, lh * len(lines), lh


def draw_lines(draw, lines, cx, top, lh, fnt, fill="black", stroke=0, stroke_fill="white"):
    for n, line in enumerate(lines):
        w = fnt.getlength(line)
        draw.text((cx - w / 2, top + n * lh), line, font=fnt, fill=fill,
                  stroke_width=stroke, stroke_fill=stroke_fill)


# ------------------------------------------------------------------ balloons

def _shape_outline(page, mask, stroke):
    """Paint a white shape with a black outline from a binary mask."""
    outline = mask.filter(ImageFilter.MaxFilter(2 * stroke + 1))
    page.paste((0, 0, 0), (0, 0), outline)
    page.paste((255, 255, 255), (0, 0), mask)


def _tail_poly(cx, cy, rx, ry, tip, width):
    ang = math.atan2(tip[1] - cy, tip[0] - cx)
    base = []
    for d in (-1, 1):
        a = ang + d * width / max(rx, ry)
        base.append((cx + rx * 0.7 * math.cos(a), cy + ry * 0.7 * math.sin(a)))
    return [base[0], tip, base[1]]


def speech(page, item, cx, cy, tip, max_w, shout=False):
    fnt = font("dialogue", item.get("size", 30))
    lines, tw, th, lh = text_block(item["say"].upper(), fnt, max_w)
    rx, ry = tw / 2 * 1.30 + 18, th / 2 * 1.38 + 16
    mask = Image.new("L", page.size, 0)
    md = ImageDraw.Draw(mask)
    if shout:
        pts = []
        n = max(14, int((rx + ry) / 14))
        for k in range(2 * n):
            a = math.pi * k / n
            r = 1.22 if k % 2 == 0 else 1.0
            pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
        md.polygon(pts, fill=255)
    else:
        md.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
    if tip is not None:
        md.polygon(_tail_poly(cx, cy, rx, ry, tip, 26), fill=255)
    _shape_outline(page, mask, 3)
    draw_lines(ImageDraw.Draw(page), lines, cx, cy - th / 2 - 2, lh, fnt)
    return rx * 2, ry * 2


def box(page, item, cx, cy, max_w, style):
    if style == "stamp":
        fnt = font("mono", item.get("size", 34))
    else:
        fnt = font("dialogue", item.get("size", 29))
    text = item["say"] if style == "stamp" else item["say"].upper()
    lines, tw, th, lh = text_block(text, fnt, max_w)
    pad = 14
    x0, y0, x1, y1 = cx - tw / 2 - pad, cy - th / 2 - pad, cx + tw / 2 + pad, cy + th / 2 + pad
    d = ImageDraw.Draw(page)
    if style == "stamp":
        d.rectangle((x0, y0, x1, y1), fill="black")
        draw_lines(d, lines, cx, y0 + pad - 4, lh, fnt, fill="white")
    elif style == "thought":
        d.rounded_rectangle((x0, y0, x1, y1), radius=18, fill="white", outline="black", width=2)
        draw_lines(d, lines, cx, y0 + pad - 2, lh, fnt)
    else:
        d.rectangle((x0, y0, x1, y1), fill="white", outline="black", width=3)
        draw_lines(d, lines, cx, y0 + pad - 2, lh, fnt)
    return x1 - x0, y1 - y0


def sfx(page, item, cx, cy, panel_h):
    size = item.get("size", max(48, int(panel_h * 0.14)))
    fnt = font("sfx", size)
    text = item["say"]
    w, h = int(fnt.getlength(text)) + 40, int(size * 1.4) + 40
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((20, 10), text, font=fnt, fill="black",
                               stroke_width=max(4, size // 12), stroke_fill="white")
    layer = layer.rotate(item.get("angle", 8), expand=True, resample=Image.BICUBIC)
    page.paste(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)), layer)


def letter_panel(page, panel, rect):
    x0, y0, x1, y1 = rect
    pw, ph = x1 - x0, y1 - y0
    max_w = min(int(pw * 0.42), 470)
    cursor_x, cursor_y, row_h = x1 - 24, y0 + 24, 0   # auto layout: right-to-left
    for item in panel.get("text", []):
        t = item["t"]
        if t == "sfx":
            at = item.get("at", [0.28, 0.78])
            sfx(page, item, x0 + at[0] * pw, y0 + at[1] * ph, ph)
            continue
        if t == "stamp" and "at" not in item:
            box(page, item, x0 + 100, y0 + 50, max_w, "stamp")
            continue
        fnt = font("mono" if t == "stamp" else "dialogue", item.get("size", 30))
        _, tw, th, _ = text_block(item["say"].upper(), fnt, max_w)
        bw, bh = (tw * 1.30 + 36, th * 1.38 + 32) if t in ("speech", "offpanel", "shout") else (tw + 28, th + 28)
        if "at" in item:
            cx, cy = x0 + item["at"][0] * pw, y0 + item["at"][1] * ph
        else:
            if cursor_x - bw < x0 + 24 and row_h:
                cursor_x, cursor_y, row_h = x1 - 24, cursor_y + row_h + 16, 0
            cx, cy = cursor_x - bw / 2, cursor_y + bh / 2
            cursor_x -= bw + 16
            row_h = max(row_h, bh)
        cx = min(max(cx, bw / 2 + 8), PAGE_W - bw / 2 - 8)
        tail = item.get("tail")
        if t == "offpanel":
            tip = (x1 + 30, cy - 10) if tail is None else (x0 + tail[0] * pw, y0 + tail[1] * ph)
        elif t in ("speech", "shout"):
            if tail == "none":
                tip = None
            elif tail is None:
                tip = (cx + 10, cy + bh / 2 + min(70, ph * 0.12))
            else:
                tip = (x0 + tail[0] * pw, y0 + tail[1] * ph)
        if t in ("speech", "offpanel"):
            speech(page, item, cx, cy, tip, max_w)
        elif t == "shout":
            speech(page, item, cx, cy, tip, max_w, shout=True)
        elif t in ("thought", "caption", "stamp"):
            box(page, item, cx, cy, max_w, t)


# ------------------------------------------------------------------ panel art

def fit(img, w, h, focus=(0.5, 0.5)):
    sw, sh = img.size
    scale = max(w / sw, h / sh)
    nw, nh = math.ceil(sw * scale), math.ceil(sh * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    left = int((nw - w) * focus[0])
    top = int((nh - h) * focus[1])
    return img.crop((left, top, left + w, top + h))


def tone(w, h, step=10, r=1.6, bg=235):
    """A simple dot screentone tile."""
    img = Image.new("L", (w, h), bg)
    d = ImageDraw.Draw(img)
    for y in range(0, h, step):
        off = step // 2 if (y // step) % 2 else 0
        for x in range(-step, w, step):
            d.ellipse((x + off - r, y - r, x + off + r, y + r), fill=80)
    return img.convert("RGB")


def screen_base(w, h):
    img = Image.new("RGB", (w, h), (12, 12, 14))
    d = ImageDraw.Draw(img)
    for y in range(0, h, 4):
        d.line((0, y, w, y), fill=(22, 22, 26))
    glow = Image.new("L", (w, h), 0)
    ImageDraw.Draw(glow).ellipse((-w * 0.2, -h * 0.2, w * 1.2, h * 1.2), fill=60)
    glow = glow.filter(ImageFilter.GaussianBlur(min(w, h) // 6))
    img.paste((70, 70, 78), (0, 0), glow)
    return img


def draw_screen(w, h, lines):
    img = screen_base(w, h)
    d = ImageDraw.Draw(img)
    max_w = w * 0.86

    def layout(scale):
        rows = []   # (text, size, red)
        for l in lines:
            s = int(min(h * (0.16 if l.get("big") else 0.095), w * (0.09 if l.get("big") else 0.075)) * scale)
            for t in wrap(l["s"], font("sans", s), max_w):   # long lines wrap instead of overflowing
                rows.append((t, s, l.get("red")))
        gap = int(h * 0.04 * scale)
        return rows, sum(r[1] for r in rows) + gap * (len(rows) - 1), gap

    scale = 1.0
    rows, total, gap = layout(scale)
    while (total > h * 0.86 or any(font("sans", r[1]).getlength(r[0]) > max_w for r in rows)) and scale > 0.3:
        scale -= 0.05
        rows, total, gap = layout(scale)
    y = (h - total) / 2
    for t, s, red in rows:
        f = font("sans", s)
        d.text(((w - f.getlength(t)) / 2, y - s * 0.12), t, font=f, fill=RED if red else (238, 238, 238))
        y += s + gap
    return img


def draw_rules(w, h, lines):
    img = screen_base(w, h)
    d = ImageDraw.Draw(img)
    pad = int(w * 0.08)

    def layout(size):
        f, fh = font("sans", size), font("sans", int(size * 1.1))
        blocks, total = [], 0
        for l in lines:
            label, _, body = l["s"].partition(": ")
            wrapped, _, th, lh = text_block(body, f, w - 2 * pad)
            blocks.append((label + ":", wrapped, lh, th))
            total += int(size * 1.5) + th + int(size * 1.3)
        return f, fh, blocks, total - int(size * 1.3)

    size = int(w * 0.06)
    while layout(size)[3] > h - 2 * pad:
        size -= 2
    f, fh, blocks, total = layout(size)
    y = (h - total) / 2
    for label, wrapped, lh, th in blocks:
        d.text((pad, y), label, font=fh, fill=RED)
        y += int(size * 1.5)
        for n, line in enumerate(wrapped):
            d.text((pad, y + n * lh), line, font=f, fill=(238, 238, 238))
        y += th + int(size * 1.3)
    return img


def draw_timer(w, h, time):
    img = screen_base(w, h)
    d = ImageDraw.Draw(img)
    f = font("mono", int(min(h * 0.62, w * 0.3)))
    tw = f.getlength(time)
    asc, desc = f.getmetrics()
    d.text(((w - tw) / 2, (h - asc - desc) / 2), time, font=f, fill=RED)
    return img


def blurred_text(w, h, size, seed, n_chars=None):
    rnd = random.Random(seed)
    img = Image.new("L", (w, h), 0)
    s = "".join(rnd.choice("ABCDEFGHJKLMNPRSTUVWXYZ0123456789 -") for _ in range(n_chars or w // (size // 2)))
    ImageDraw.Draw(img).text((0, 0), s, font=font("sans-reg", size), fill=200)
    return img.filter(ImageFilter.GaussianBlur(size * 0.35))


RECORDS = [  # recovered canon only (story_bible.md 3.10)
    ("KURODA REN", "2007-04-12", "A"),
    ("TACHIBANA YUI", "2007-06-03", "O"),
    ("SAKURAI HARUTO", "2007-01-25", "B"),
    ("KANZAKI RIKU", "2006-11-14", "A"),
    ("SHIBATA GŌ", "2007-02-20", "O"),
]


def draw_grid(w, h):
    img = screen_base(w, h)
    d = ImageDraw.Draw(img)
    s = int(h * 0.05)
    f, fh = font("sans", s), font("sans", int(s * 0.7))
    cols = [0.04, 0.32, 0.50, 0.59, 0.75]
    heads = ["NAME", "BIRTHDAY", "BLOOD", "MEDICAL", "EMERGENCY CONTACT"]
    y = int(h * 0.06)
    for c, t in zip(cols, heads):
        d.text((w * c, y), t, font=fh, fill=RED)
    y += int(s * 1.6)
    row_h = int(s * 1.45)
    for n, rec in enumerate(RECORDS):
        for c, t in zip(cols, rec):
            d.text((w * c, y), t, font=f, fill=(238, 238, 238))
        for c, cw, k in ((cols[3], 0.13, 1), (cols[4], 0.2, 2)):
            img.paste((150, 150, 150), (int(w * c), y + 4), blurred_text(int(w * cw), s, s - 4, n * 10 + k))
        y += row_h
    # remaining records: out of focus, unreadable (not recovered)
    while y + row_h < h - 8:
        img.paste((110, 110, 110), (int(w * 0.04), y + 4), blurred_text(int(w * 0.92), s, s, y))
        y += row_h
    return img


def draw_card(w, h):
    img = screen_base(w, h)
    d = ImageDraw.Draw(img)
    s = int(min(h * 0.075, w * 0.06))
    f, fl = font("sans", s), font("sans", int(s * 0.62))
    name, bday, blood = RECORDS[0]
    x, y = int(w * 0.08), int(h * 0.1)
    for label, value in (("NAME", name), ("BIRTHDAY", bday), ("BLOOD TYPE", blood)):
        d.text((x, y), label, font=fl, fill=RED)
        d.text((x, y + int(s * 0.75)), value, font=f, fill=(238, 238, 238))
        y += int(s * 2.1)
    for n, label in enumerate(("MEDICAL", "EMERGENCY CONTACT")):
        d.text((x, y), label, font=fl, fill=RED)
        img.paste((150, 150, 150), (x, y + int(s * 0.8)), blurred_text(int(w * 0.8), s, s - 6, 99 + n))
        y += int(s * 2.1)
    return img


def draw_clock(w, h, hhmmss):
    ss = 2
    W, H = w * ss, h * ss
    img = tone(W, H, step=14, r=2.2, bg=225)
    d = ImageDraw.Draw(img)
    cx, cy, R = W / 2, H / 2, min(W, H) * 0.42
    d.ellipse((cx - R - 14, cy - R - 14, cx + R + 14, cy + R + 14), fill="black")
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill="white")
    for k in range(60):
        a = math.pi * 2 * k / 60
        r1 = R * (0.84 if k % 5 == 0 else 0.92)
        d.line((cx + r1 * math.sin(a), cy - r1 * math.cos(a), cx + R * 0.97 * math.sin(a), cy - R * 0.97 * math.cos(a)),
               fill="black", width=10 if k % 5 == 0 else 3)
    hh, mm, sec = (int(v) for v in hhmmss.split(":"))
    for frac, length, width in (((hh % 12 + mm / 60) / 12, 0.5, 22), ((mm + sec / 60) / 60, 0.75, 14), (sec / 60, 0.85, 5)):
        a = 2 * math.pi * frac
        d.line((cx, cy, cx + R * length * math.sin(a), cy - R * length * math.cos(a)), fill="black", width=width)
    d.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), fill="black")
    return img.resize((w, h), Image.LANCZOS)


def draw_phone(w, h, mode):
    ss = 2
    W, H = w * ss, h * ss
    img = tone(W, H, step=12, r=2.6, bg=70)
    d = ImageDraw.Draw(img)
    ph = H * 0.92
    pw = min(ph * 0.5, W * 0.62)
    x0, y0 = (W - pw) / 2, (H - ph) / 2
    d.rounded_rectangle((x0, y0, x0 + pw, y0 + ph), radius=pw * 0.12, fill="black")
    sx0, sy0, sx1, sy1 = x0 + pw * 0.05, y0 + ph * 0.035, x0 + pw * 0.95, y0 + ph * 0.965
    d.rounded_rectangle((sx0, sy0, sx1, sy1), radius=pw * 0.09, fill=(245, 245, 245))
    sw = sx1 - sx0
    fs = font("sans", int(sw * 0.065))
    fb = font("sans", int(sw * 0.085))
    if mode == "market":
        d.text((sx0 + sw * 0.07, sy0 + sw * 0.05), "12:16", font=fs, fill="black")
        d.text((sx0 + sw * 0.07, sy0 + sw * 0.22), "MARKET UPDATE", font=fb, fill="black")
        rnd = random.Random(1217)
        cx0, cy0, cx1, cy1 = sx0 + sw * 0.07, sy0 + sw * 0.45, sx1 - sw * 0.07, sy0 + sw * 1.15
        d.rectangle((cx0, cy0, cx1, cy1), outline=(170, 170, 170), width=3)
        pts, v = [], 0.5
        n = 60
        for k in range(n):
            v = min(0.9, max(0.1, v + rnd.uniform(-0.06, 0.06)))
            pts.append((cx0 + (cx1 - cx0) * k / (n - 1) * 0.7, cy1 - (cy1 - cy0) * v))
        d.line(pts, fill="black", width=5)
        d.line((pts[-1][0], cy0, pts[-1][0], cy1), fill=(120, 120, 120), width=3)
        by = cy1 + sw * 0.12
        d.rounded_rectangle((sx0 + sw * 0.07, by, sx1 - sw * 0.07, by + sw * 0.22), radius=18, fill=(40, 40, 40))
        t = "CONNECTION LOST"
        d.text((sx0 + (sw - fb.getlength(t)) / 2, by + sw * 0.055), t, font=fb, fill="white")
    else:
        t1 = "No Service"
        d.text((sx0 + sw * 0.07, sy0 + sw * 0.05), t1, font=fs, fill="black")
        cy = (sy0 + sy1) / 2
        bx = sx0 + sw * 0.3
        for k in range(4):
            bh = sw * 0.08 * (k + 1)
            d.rectangle((bx + k * sw * 0.11, cy - bh, bx + k * sw * 0.11 + sw * 0.07, cy), outline="black", width=4)
        d.line((bx - sw * 0.04, cy - sw * 0.36, bx + sw * 0.46, cy + sw * 0.04), fill="black", width=8)
        t2 = "No signal"
        d.text((sx0 + (sw - fb.getlength(t2)) / 2, cy + sw * 0.15), t2, font=fb, fill="black")
    return img.resize((w, h), Image.LANCZOS)


def draw_title(page, rect, chapter):
    x0, y0, x1, y1 = rect
    d = ImageDraw.Draw(page)
    f = font("sfx", 150)
    for n, line in enumerate(("DEAD MAN'S", "ALGORITHM")):
        tw = f.getlength(line)
        d.text(((x0 + x1 - tw) / 2, y0 + 90 + n * 150), line, font=f, fill="black", stroke_width=10, stroke_fill="white")
    f2 = font("sfx", 64)
    t = f"CHAPTER {chapter['chapter']}  —  {chapter['title'].upper()}"
    d.text(((x0 + x1 - f2.getlength(t)) / 2, y0 + 420), t, font=f2, fill="white", stroke_width=6, stroke_fill="black")


def draw_streak(img, spec):
    """One glowing streak from (x0, y0) to its head at (x1, y1), in panel fractions.

    An optional fifth value scales the trail width and head size (a near fireball).
    """
    w, h = img.size
    x0, y0, x1, y1 = spec[0] * w, spec[1] * h, spec[2] * w, spec[3] * h
    k_size = spec[4] if len(spec) > 4 else 1.0
    glow = Image.new("L", (w, h), 0)
    core = Image.new("L", (w, h), 0)
    gd, cd = ImageDraw.Draw(glow), ImageDraw.Draw(core)
    n = 40
    for k in range(n):
        t0, t1 = k / n, (k + 1) / n
        seg = (x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0, x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1)
        gd.line(seg, fill=int(255 * t1), width=int((4 + 18 * t1) * k_size))
        cd.line(seg, fill=int(255 * t1), width=int((1 + 5 * t1) * k_size))
    r = max(6, int(min(w, h) * 0.012 * k_size))
    gd.ellipse((x1 - 3 * r, y1 - 3 * r, x1 + 3 * r, y1 + 3 * r), fill=255)
    cd.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), fill=255)
    shade = glow.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(6)).point(lambda v: v * 0.55)
    img.paste((30, 30, 30), (0, 0), shade)   # dark edge so the streak reads on a light sky
    img.paste((255, 255, 255), (0, 0), glow.filter(ImageFilter.GaussianBlur(10 * k_size)))
    img.paste((255, 255, 255), (0, 0), core)
    return img


def render_panel(panel, w, h, art_dir, pid):
    kind = panel.get("kind", "art")
    if kind == "art":
        path = art_dir / f"{panel.get('reuse', pid)}.png"   # reuse: show another panel's art
        if not path.exists():
            img = Image.new("RGB", (w, h), (200, 200, 200))
            ImageDraw.Draw(img).text((20, 20), f"{pid} not rendered yet", font=font("sans", 28), fill="black")
            return img
        img = Image.open(path).convert("L").convert("RGB")
        img = fit(img, w, h, tuple(panel.get("focus", (0.5, 0.5))))
        return draw_streak(img, panel["streak"]) if panel.get("streak") else img
    if kind == "black":
        return Image.new("RGB", (w, h), "black")
    if kind == "white":
        return Image.new("RGB", (w, h), "white")
    if kind == "screen":
        return draw_screen(w, h, panel["lines"])
    if kind == "rules":
        return draw_rules(w, h, panel["lines"])
    if kind == "timer":
        return draw_timer(w, h, panel["time"])
    if kind == "grid":
        return draw_grid(w, h)
    if kind == "card":
        return draw_card(w, h)
    if kind == "clock":
        return draw_clock(w, h, panel["time"])
    if kind == "phone":
        return draw_phone(w, h, panel["mode"])
    raise ValueError(f"unknown panel kind {kind}")


def compose_page(page_spec, art_dir, chapter):
    page = Image.new("RGB", (PAGE_W, PAGE_H), "white")
    d = ImageDraw.Draw(page)
    rects = panel_rects(page_spec["rows"])
    for i, (panel, rect) in enumerate(zip(page_spec["panels"], rects), start=1):
        x0, y0, x1, y1 = rect
        img = render_panel(panel, x1 - x0, y1 - y0, art_dir, panel_id(page_spec["page"], i))
        page.paste(img, (x0, y0))
        if panel.get("overlay_timer"):
            tw, th = int((x1 - x0) * 0.42), int((y1 - y0) * 0.12)
            ox, oy = x0 + ((x1 - x0) - tw) // 2, y0 + int((y1 - y0) * 0.05)
            page.paste(draw_timer(tw, th, panel["overlay_timer"]), (ox, oy))
            d.rectangle((ox, oy, ox + tw, oy + th), outline="black", width=4)
        if panel.get("kind") != "white":
            d.rectangle(rect, outline="black", width=BORDER)
        if panel.get("title"):
            draw_title(page, rect, chapter)
    for panel, rect in zip(page_spec["panels"], rects):
        letter_panel(page, panel, rect)
    f = font("sans-reg", 24)
    num = str(page_spec["page"])
    d.text(((PAGE_W - f.getlength(num)) / 2, PAGE_H - 62), num, font=f, fill="black")
    return page


def export(pages_dir, out_dir, name, chapter):
    pages = sorted(pages_dir.glob("page_*.png"))
    pdf = out_dir / f"{name}.pdf"
    pdf.write_bytes(img2pdf.convert([str(p) for p in pages]))
    info = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<ComicInfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n'
        "  <Series>DEAD MAN'S ALGORITHM</Series>\n"
        f"  <Number>{chapter['chapter']}</Number>\n"
        f"  <Title>{chapter['title']}</Title>\n"
        f"  <PageCount>{len(pages)}</PageCount>\n"
        "  <BlackAndWhite>Yes</BlackAndWhite>\n"
        "  <Manga>YesAndRightToLeft</Manga>\n"
        "</ComicInfo>\n"
    )
    cbz = out_dir / f"{name}.cbz"
    with zipfile.ZipFile(cbz, "w", zipfile.ZIP_STORED) as z:
        for p in pages:
            z.write(p, p.name)
        z.writestr("ComicInfo.xml", info)
    return pdf, cbz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("outdir")
    ap.add_argument("--pages", default="")
    ap.add_argument("--name", default="DEAD_MANS_ALGORITHM_ch01")
    a = ap.parse_args()
    chapter = load_chapter(a.script)
    out = Path(a.outdir)
    pages_dir = out / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    lo, _, hi = a.pages.partition("-")
    for spec in chapter["pages"]:
        n = spec["page"]
        if a.pages and not (int(lo) <= n <= int(hi or lo)):
            continue
        compose_page(spec, out / "panels", chapter).save(pages_dir / f"page_{n:02d}.png", optimize=True)
        print(f"page {n} done")
    if len(list(pages_dir.glob("page_*.png"))) == len(chapter["pages"]):
        pdf, cbz = export(pages_dir, out, a.name, chapter)
        print(f"exported {pdf.name}, {cbz.name}")


if __name__ == "__main__":
    main()
