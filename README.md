# Manga

Toolchain for turning a written story into manga pages, in a CPU-only Linux container.

- **Research:** [`reports/AI story to manga toolchain.md`](reports/AI%20story%20to%20manga%20toolchain.md), with the source notes in `research_notes/`.
- **Install:** `./setup.sh` installs apt packages, a Python 3.13 venv in `.venv`, CPU PyTorch and diffusers, the Animagine XL 4.0 model (about 7 GB, in `models/`), and the research MCP servers.

## Pipeline

1. **Script.** Claude turns the story into pages, panels, shots, characters, dialogue and SFX.
2. **Panels.** Panels are drawn without text by one of:
   - a hosted API: `google-genai`, `openai`, `fal-client` or `replicate`, which needs your API key;
   - locally on CPU: `tools/gen_panel_local.py`, at about 205 s per 832×1216 panel and no key needed.
3. **Pages.** Right-to-left layout, balloons and lettering are done with Pillow, skia-python or drawsvg. Vertical Japanese text uses Playwright with the pre-installed Chromium and CSS `writing-mode: vertical-rl`.
4. **Tone.** Screentone uses ImageMagick (`convert … -ordered-dither h6x6a`) or GEGL. Line-art vectorising uses vtracer or potrace.
5. **Export.** PDF uses img2pdf. CBZ is a zip of the page images plus `ComicInfo.xml` with `<Manga>YesAndRightToLeft</Manga>`.

## Fonts (`assets/fonts`, SIL Open Font License)

| Font | Use |
|---|---|
| Shippori Antique | Japanese dialogue |
| Comic Neue | English dialogue |
| Bangers | SFX |

Noto CJK comes from apt.

## Research helpers

- **`.mcp.json`:** registers two MCP servers.
  - `chrome-devtools` drives headless Chromium.
  - `reddit` uses [mcp-reddit](https://github.com/adhikasp/mcp-reddit) through Reddit's official OAuth API.
- **`tools/reddit_tool.py`:** adds Reddit search and comment-tree reading, which mcp-reddit lacks.
