"""Page geometry shared by the panel renderer and the page composer.

Rows are listed top to bottom; cells within a row are listed right to left
(manga reading order), so the first cell of a row is its rightmost panel.
"""
from pathlib import Path

import yaml

PAGE_W, PAGE_H = 1600, 2264          # ~B5 proportions (1:1.415)
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 80, 90, 100
HGAP, VGAP = 24, 32                  # gutters between panels / rows

# SDXL resolutions near 1 megapixel
BUCKETS = [(1024, 1024), (1152, 896), (896, 1152), (1216, 832), (832, 1216),
           (1344, 768), (768, 1344), (1536, 640), (640, 1536)]


def load_chapter(path):
    return yaml.safe_load(Path(path).read_text())


def panel_rects(rows):
    """Return [(x0, y0, x1, y1), ...] in reading order for a page's rows."""
    content_w = PAGE_W - 2 * MARGIN_X
    content_h = PAGE_H - MARGIN_TOP - MARGIN_BOTTOM
    total_h = sum(r[0] for r in rows)
    avail_h = content_h - VGAP * (len(rows) - 1)
    rects, y = [], MARGIN_TOP
    for height_weight, cells in rows:
        h = round(avail_h * height_weight / total_h)
        avail_w = content_w - HGAP * (len(cells) - 1)
        x_right = PAGE_W - MARGIN_X
        for w_weight in cells:
            w = round(avail_w * w_weight / sum(cells))
            rects.append((x_right - w, y, x_right, y + h))
            x_right -= w + HGAP
        y += h + VGAP
    return rects


def bucket_for(w, h):
    import math
    target = math.log(w / h)
    return min(BUCKETS, key=lambda b: abs(math.log(b[0] / b[1]) - target))


def iter_panels(chapter):
    """Yield (page_no, index, panel, rect) for every panel in reading order."""
    for page in chapter["pages"]:
        for i, (panel, rect) in enumerate(zip(page["panels"], panel_rects(page["rows"])), start=1):
            yield page["page"], i, panel, rect


def panel_id(page_no, index):
    return f"p{page_no:02d}_{index}"
