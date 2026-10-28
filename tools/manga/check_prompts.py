"""Check every art prompt and its negative fit CLIP's 77-token window.

Tokens past 77 are silently dropped, so a tag at the end of a long prompt (the
quality tags, a late negative) would do nothing. Also lists missing sketches.

  python tools/manga/check_prompts.py story/chapter04/script.yaml
"""
import sys
from pathlib import Path

from transformers import CLIPTokenizer

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_panel_local import MODEL, full_prompt  # noqa: E402
from layout import iter_panels, load_chapter, panel_id  # noqa: E402
from render_panels import expand, negatives_for  # noqa: E402

LIMIT = 77


def main():
    tok = CLIPTokenizer.from_pretrained(MODEL, subfolder="tokenizer")
    bad = 0
    for script in sys.argv[1:]:
        chapter = load_chapter(script)
        for page_no, i, panel, _ in iter_panels(chapter):
            if panel.get("kind", "art") != "art" or panel.get("reuse"):
                continue
            pid = panel_id(page_no, i)
            n_pos = len(tok(full_prompt(expand(panel["gen"], chapter["characters"]))).input_ids) - 2
            n_neg = len(tok(negatives_for(chapter, page_no, panel)).input_ids) - 2
            missing = panel.get("sketch") and not (Path(script).parent / panel["sketch"]).exists()
            if n_pos > LIMIT or n_neg > LIMIT or missing:
                bad += 1
                print(f"{script} {pid}: prompt {n_pos}, negative {n_neg}" + (", sketch missing" if missing else ""))
    print("all prompts fit" if not bad else f"{bad} panel(s) to fix")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
