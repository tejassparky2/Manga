"""Render every `kind: art` panel of a chapter with Animagine XL 4.0 on CPU.

Resumable: panels whose PNG already exists are skipped.

  python tools/manga/render_panels.py story/chapter01/script.yaml output/ch01/panels
  python tools/manga/render_panels.py ... --pages 3-5 --steps 16
  python tools/manga/render_panels.py ... --redo p03_2 --seed 1234   # re-roll one panel
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from gen_panel_local import generate, load_pipeline  # noqa: E402
from layout import bucket_for, iter_panels, load_chapter, panel_id  # noqa: E402


def expand(prompt, characters):
    for name, tags in characters.items():
        prompt = prompt.replace("{" + name + "}", tags)
    return prompt


def page_filter(spec):
    if not spec:
        return lambda p: True
    lo, _, hi = spec.partition("-")
    return lambda p: int(lo) <= p <= int(hi or lo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("outdir")
    ap.add_argument("--pages", default="")
    ap.add_argument("--steps", type=int, default=16)
    ap.add_argument("--redo", default="", help="comma-separated panel ids to re-render")
    ap.add_argument("--seed", type=int, default=None, help="seed override for --redo")
    a = ap.parse_args()

    chapter = load_chapter(a.script)
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    wanted = page_filter(a.pages)
    redo = set(filter(None, a.redo.split(",")))

    jobs = []
    for page_no, i, panel, (x0, y0, x1, y1) in iter_panels(chapter):
        pid = panel_id(page_no, i)
        if panel.get("kind", "art") != "art" or not wanted(page_no):
            continue
        if redo and pid not in redo:
            continue
        if (out / f"{pid}.png").exists() and pid not in redo:
            continue
        jobs.append((pid, page_no * 100 + i, panel, bucket_for(x1 - x0, y1 - y0)))

    print(f"{len(jobs)} panels to render", flush=True)
    if not jobs:
        return
    pipe = load_pipeline()
    for n, (pid, seed, panel, (w, h)) in enumerate(jobs, start=1):
        seed = a.seed if a.seed is not None else panel.get("seed", seed)
        prompt = expand(panel["gen"], chapter["characters"])
        t = time.time()
        img = generate(pipe, prompt, width=w, height=h, steps=a.steps, seed=seed)
        img.save(out / f"{pid}.png")
        print(f"[{n}/{len(jobs)}] {pid} {w}x{h} seed={seed} {time.time() - t:.0f}s", flush=True)


if __name__ == "__main__":
    main()
