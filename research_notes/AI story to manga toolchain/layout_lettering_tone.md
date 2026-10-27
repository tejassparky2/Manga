# Manga page assembly: panel layout, lettering, SFX, screentone, line art, export (as of 2026-10-27)

Scope: the non-illustration half of a story-to-manga pipeline. The input is generated panel images plus a script (dialogue, captions, SFX). The output is finished manga pages and reader files. The emphasis is on open-source tools that can be scripted and that run on the target container: Linux (Ubuntu 24.04.5), no GPU, 4 vCPU, 15 GB RAM, Python 3.13, Node 22.

Method notes:
- **Repo activity.** "Last commit" dates come from shallow `git clone` runs on 2026-10-27, and licenses come from each repo's LICENSE file. The GitHub REST API was blocked in this session.
- **Package data.** PyPI, npm, Hugging Face and Launchpad data comes from their public JSON APIs, queried on 2026-10-27.
- **Local tests.** Items marked **[local test]** were run in this container on 2026-10-27.

---

## Q1. Automatic panel layout: research, code, programmatic approaches, and the manga layout rules they must respect

### Takeaway
No maintained open-source manga layout generator exists that you can pip-install. Research systems (Cao et al. 2012, MangaDiffusion 2024, DiffSensei 2024/25, MangaFlow 2026) either release no layout code or need a 24 GB+ GPU. The practical route is a small rule-based layout engine you write yourself (template grids plus recursive splits) that emits panel polygons, rendered with Pillow, Cairo/Skia, SVG, or HTML/CSS through headless Chromium. Manga109 or Kumiko can supply real panel statistics for validation. The engine needs to encode these conventions:
- right-to-left (RTL) reading order;
- top/bottom gutters wider than left/right gutters (one worked example uses 2 mm left/right and 5 mm top/bottom);
- 3–5 mm bleed;
- dialogue kept inside the inner "basic frame";
- 600 dpi for monochrome, 350 dpi for colour or grey;
- trim sizes of B5 (magazine), B6 (tankōbon) and A5 (dōjinshi), or 5×7.5 in for US editions.

### Cited Findings

**Research on layout generation**
- **Cao, Chan & Lau, "Automatic Stylistic Manga Layout" (ACM TOG / SIGGRAPH Asia 2012).** Three parametric style models cover layout structure, panel importance and panel shape. A generative probabilistic framework produces an initial layout, then an optimisation refines the layout and artwork geometry together. In a user study, novices made more manga-like layouts with it than with a commercial manual tool. — [SIGGRAPH History](https://history.siggraph.org/?p=207969); [author PDF](https://www.cs.cityu.edu.hk/~rynson/papers/siga12a.pdf); [project page](https://www.cs.cityu.edu.hk/~rynson/projects/manga/MangaDesigner.html). No code release was found (unverified).
- **Yang et al., "Automatic Comic Generation with Stylistic Multi-page Layouts and Emotion-driven Text Balloon Generation" (arXiv 2101.11111, Jan 2021).** It allocates images across pages, builds layouts from image importance and inter-image relations, varies balloon shape and word size by detected emotion, and places balloons next to speakers found by speaker detection. No code is linked. — [arXiv](https://arxiv.org/abs/2101.11111)
- **Chen et al., "Manga Generation via Layout-controllable Diffusion" (MangaDiffusion, arXiv 2412.19303, 26 Dec 2024).** Introduces the Manga109Story dataset (about 21,142 pages derived from Manga109, with GPT-4o panel captions) and an "inter-panel" transformer that generates whole pages with a controlled number of panels. The arXiv page gives no code or data URL. — [arXiv](https://arxiv.org/abs/2412.19303)
- **"How Panel Layouts Define Manga" (arXiv 2412.19141).** An analysis paper on Manga109 showing that panel layouts strongly reflect the identity of individual works. — [ResearchGate](https://www.researchgate.net/publication/387512302_How_Panel_Layouts_Define_Manga_Insights_from_Visual_Ablation_Experiments) (via search snippet)
- **MangaFlow (arXiv 2605.28173).** v1 was submitted 27 May 2026 and v2 on 14 Sep 2026; it is listed as EMNLP 2026 Main. It is an agentic story-to-manga framework with planning, grounding, layout construction, reference-conditioned rendering, composition and text placement stages. Layout and lettering are editable intermediate controls, and the paper adds the MangaGen-MetaBench benchmark. The page gives no code URL. — [arXiv](https://arxiv.org/abs/2605.28173)
- **DiffSensei (jianzongwu/DiffSensei).** Last commit 2025-02-05, no LICENSE file in the repo. The lower-memory "without MLLM" variant still needs "a single 24GB 4090 GPU". The MangaZero dataset ships only MangaDex URLs plus annotations "for license issues". — [GitHub](https://github.com/jianzongwu/DiffSensei); [MangaZero on HF](https://huggingface.co/datasets/jianzongwu/MangaZero)

**Code that does page or panel composition**
- **StoryDiffusion** (Apache-2.0, last commit 2024-09-26). `utils/utils.py` has plain Pillow helpers: `get_comic(images, types="4panel")`, `get_comic_4panel`, `get_comic_classical`, `add_caption`, `distribute_images(group_sizes=(4,3,2))`, and a bundled `fonts/Inkfree.ttf`. These are simple LTR grid and caption composers and can be reused. — [GitHub](https://github.com/HVision-NKU/StoryDiffusion)
- **AI Comic Factory** (jbilcke-hf, Apache-2.0 per `LICENCE.md`, last commit 2025-10-30). Page layouts are Tailwind CSS grids in `src/app/layouts/index.tsx`, for example `grid-cols-2 grid-rows-2` and `grid-cols-5 grid-rows-2` with `col-span`/`row-span`. Speech bubbles are a React `Bubble` component in `src/app/interface/panel/bubble/`. — [GitHub](https://github.com/jbilcke-hf/ai-comic-factory)
- **comfyui-panelforge ("Pixstri ComfyUI Comics")**. ComfyUI nodes in a Page → Row → Frame hierarchy that compose images into comic layouts. No LICENSE file; last commit 2025-04-29. — [GitHub](https://github.com/lisaks/comfyui-panelforge)
- **Krita 5.3 / 6.0** (released 5 Feb 2026). Adds a "Comic Panel Editing tool" to "split and merge vector objects quickly, making it easy to set up panel layouts for comics". This is GUI-oriented. — [Krita 5.3 release notes](https://krita.org/en/release-notes/krita-5-3-release-notes/)
- **gramener/comicgen** (MIT, npm 1.9.9, npm last modified 2024-03-02, repo last commit 2024-04-07). An API for adding pre-drawn comic characters to web pages, not a manga layout tool. — [GitHub](https://github.com/gramener/comicgen); [npm](https://www.npmjs.com/package/comicgen)
- **LaTeX.** No CTAN package draws comic panels or balloons. The closest is the new **graphicnovel** class (v0.5.0, announced 2026-10-12, LPPL 1.3c), which formats scripts only and "does not draw panels or generate finished comic artwork". — [CTAN graphicnovel](https://ctan.org/pkg/graphicnovel)
- **Typst.** A Dec 2025 gap analysis (Typst v0.14.2) says Typst "struggles even with basic vertical typesetting" (issues #5908 and #7399). The community package **basho 0.1.0** adds tategaki with tate-chu-yoko, ruby, kinsoku shori and multi-column RTL. The Python binding `typst` is 0.15.0 (2026-06-16, abi3 wheels, Apache-2.0). — [gap analysis mirror](https://scriptagc.wasmer.app/https_gap_zhtyp_art); [basho](https://typst.app/universe/package/basho); [typst on PyPI](https://pypi.org/project/typst/); [typst-py](https://github.com/messense/typst-py)

**Rendering primitives (versions from PyPI on 2026-10-27)**

| Package | Version / date | License | Wheel / install notes |
|---|---|---|---|
| [Pillow](https://pypi.org/project/pillow/) | 13.0.0 (2026-10-16) | MIT-CMU | cp313 manylinux wheel |
| [pycairo](https://pypi.org/project/pycairo/) | 1.29.2 | LGPL-2.1 OR MPL-1.1 | No cp313 Linux wheel; builds from sdist and needs `libcairo2-dev` (apt 1.18.0 available here) |
| [skia-python](https://pypi.org/project/skia-python/) | 144.1 | BSD | cp313 wheel |
| [drawsvg](https://pypi.org/project/drawsvg/) | 2.4.2 (2026-08-12) | MIT | Pure Python |
| [svgwrite](https://pypi.org/project/svgwrite/) | 1.4.3 (2022, stale) | MIT | Pure Python |
| [cairosvg](https://pypi.org/project/cairosvg/) | 2.9.1 | LGPL-3.0+ | — |
| [reportlab](https://pypi.org/project/reportlab/) | 5.1.0 (2026-10-22) | BSD | — |
| [weasyprint](https://pypi.org/project/weasyprint/) | 70.0 | BSD | — |
| [playwright](https://pypi.org/project/playwright/) | 1.64.1 | Apache-2.0 | Also on npm 1.64.1 |
| [puppeteer](https://www.npmjs.com/package/puppeteer) | npm 25.16.0 | Apache-2.0 | — |
| [shapely](https://pypi.org/project/shapely/) | 2.2.0 | BSD-3 | Useful for panel polygons and balloon clipping |

**Manga layout conventions**
- **Reading order.** A page starts at the top-right panel, moves right to left along a row, then drops to the next row, ending bottom-left. Within a panel, the rightmost balloon is read first, and stacked balloons top-first. These are consistent secondary sources only. — [Buffalo Library "How to Read Manga" PDF](https://www.BuffaloLib.org/sites/default/files/getgraphic/resources/HowtoReadManga.pdf); [Google Arts & Culture "Grammar of Manga"](https://artsandculture.google.com/story/EAWB4YvyVDqJJQ); [GlobalComix komawari basics](https://globalcomix.com/news/details/254/creator-tips-and-tricks-9-basics-of-komawari)
- **Gutters.** In a Clip Studio Paint "frame border divide" example, a Japanese book (gihyo.jp, 2025) sets 左右の間隔 (left/right gap) to **2.0** and 上下の間隔 (top/bottom gap) to **5.0**, noting that "左右と上下の間隔は、作家によって違います" (the spacing varies by artist). — [gihyo.jp sample PDF](https://gihyo.jp/assets/files/book/2025/978-4-297-15158-4/9784297151584-01.pdf) **[local pdftotext check]**
- **Bleed.** 裁ち落とし幅 (bleed width) is usually **3 mm or 5 mm**. Use 5 mm if the printer is undecided. — [gihyo.jp PDF](https://gihyo.jp/assets/files/book/2025/978-4-297-15158-4/9784297151584-01.pdf). Clip Studio's official column gives 塗り足し (bleed allowance) as "3mm～5mm". — [clipstudio.net column](https://www.clipstudio.net/oekaki/archives/149920)
- **Resolution.** "モノクロ（白黒）原稿は 600dpi / カラー、グレー原稿は 350dpi" (600 dpi for black-and-white manuscripts; 350 dpi for colour or grey). — [gihyo.jp PDF](https://gihyo.jp/assets/files/book/2025/978-4-297-15158-4/9784297151584-01.pdf). MediBang says a minimum of 600 dpi for print. — [MediBang tutorial 07](https://medibangpaint.com/en/use/2021/11/mangatutorialforbeginners07). A Clip Studio Tips guide gives 600–1200 dpi for monochrome, 300–600 dpi for colour, and around 150 dpi / ~4000 px wide for web. — [CSP Tips 8264](https://tips.clip-studio.com/en-us/articles/8264)
- **Trim and manuscript sizes:**
  - Magazine pages: B5 finished size (182×257 mm), drawn on A4. — [CSP Tips 8264](https://tips.clip-studio.com/en-us/articles/8264)
  - Tankōbon: B6 finished size, drawn on A5. Japanese B6 is 128×182 mm, A5 is 148×210 mm, and bunkoban is A6 (105×148 mm). — [CSP Tips 8264](https://tips.clip-studio.com/en-us/articles/8264); [Wikipedia Tankōbon](https://en.wikipedia.org/wiki/Tank%C5%8Dbon)
  - Dōjinshi: A5 finished size, drawn on B5. — [CSP Tips 8264](https://tips.clip-studio.com/en-us/articles/8264)
  - US "Tokyopop trim": about 5×7.5 in (13×19 cm). — [Wikipedia Tankōbon](https://en.wikipedia.org/wiki/Tank%C5%8Dbon)
  - Wikipedia gives B5 as 176×250 mm (ISO B5), while Japanese sources use JIS B5 at 182×257 mm. Use JIS B sizes for Japanese print.
- **B4 submission manuscript (secondary source).** Paper 257×364 mm, "finished frame" 220×310 mm, 基本枠 (basic frame) 180×270 mm. — [uptogo.com.tw](https://uptogo.com.tw/?p=1695294) (secondary; sources disagree on frame definitions)
- **Safe area and binding:**
  - Dialogue and faces go inside the inner "safe area" line; the binding margin is hidden when bound. — [MediBang tutorial 07](https://medibangpaint.com/en/use/2021/11/mangatutorialforbeginners07)
  - On right-bound books, don't bleed into the binding side (ノド); bleed the outer edge instead. — [clipstudio.net column](https://www.clipstudio.net/oekaki/archives/149920)
  - "In the basic Japanese manga format, odd-numbered pages go to the right, and even-numbered pages go to the left." — [MediBang tutorial 07](https://medibangpaint.com/en/use/2021/11/mangatutorialforbeginners07)
- **Cover spine width.** Roughly 1 mm per 10 pages (about 2 mm for 20 pages, 4 mm for 40). — [clipstudio.net column](https://www.clipstudio.net/oekaki/archives/149920)
- **Panel density (Manga109 annotation stats v2026.05.21).** 10,130 annotated images, 103,850 frames and 159,598 text boxes. Images are stored "in double-page spread manner". — [Manga109 annotations](http://www.manga109.org/en/annotations.html)

### Inferences
- **Panel count.** From the Manga109 numbers, 103,850 frames ÷ 10,130 spreads ≈ 10.3 frames per spread, so about 5 panels per page. Ranges of 3–7 per page with a 4–6 default are reasonable. This is computed here, not stated by Manga109.
- **Build vs. borrow.** A home-grown engine is easier than adopting research code. Represent a page as a recursive split tree (horizontal strips, each split vertically), and assign panels in RTL order: right-to-left within a strip, strips top to bottom. Apply gutters of about 2 mm (left/right) and 5 mm (top/bottom) at trim scale. Clip full-bleed panels to trim + 3–5 mm. Use Shapely for polygon maths and slanted panels. For an RTL Japanese edition, StoryDiffusion's and AI Comic Factory's grid code would need to be mirrored.
- **Recommended stack on this container.** Either:
  - Pillow (raster) + drawsvg/skia-python (vector balloons), rendered at 600 dpi B5/B6; or
  - HTML/CSS Grid + `writing-mode: vertical-rl`, rendered by Playwright headless Chromium to PNG/PDF.

  Both run CPU-only. The HTML route gets the most mature vertical Japanese text for free (see Q2).

### Gaps
- No primary industry standard for gutter widths or panels per page was found; the 2 mm / 5 mm values are one book's worked example.
- No released code was found for Cao 2012, MangaDiffusion or MangaFlow.
- No open, maintained "layout dataset" with RTL page templates was found beyond Manga109's frame boxes (academic licence, see Q4) and MangaZero's URL-only release.

---

## Q2. Speech bubbles and lettering: balloon and tail tools, fonts and licences, vertical Japanese text, text fitting, and reusable lettering code

### Takeaway
- **Balloon placement.** There is no drop-in Python library for "place balloon + tail automatically". The reusable pieces are:
  - (a) the text-fitting renderers inside the translator projects: manga-image-translator and BallonsTranslator (GPL-3.0), comic-translate (Apache-2.0), and koharu (MIT/Apache, Rust);
  - (b) small SVG/canvas bubble generators (splargdotcom/speechbubble, MIT);
  - (c) classic label-placement research (cartographic labelling plus a layout-quality score).
- **Vertical Japanese text.** Chromium CSS `writing-mode: vertical-rl` is the most robust option. Pillow `direction="ttb"` works per column but stacks multiple lines left-to-right **[local test]**, so each column must be placed right-to-left by hand.
- **Fonts.** Safe free options: **Shippori Antique** (OFL, made for manga dialogue) for Japanese, and Blambot's free comic fonts (free for indie or small-press comics even when sold, not for mainstream publishers or software embedding) for English. Wild Words (Comicraft) is paid.

### Cited Findings

**Balloon placement research and code**
- **"An Automated Procedure for Word Balloon Placement in Cinema Comics".** Places each balloon relative to its speaker while keeping dialogue reading order, using a cartographic labelling algorithm, then refines positions with a balloon-layout quality measure. — [ResearchGate](https://www.researchgate.net/publication/220845577_An_Automated_Procedure_for_Word_Balloon_Placement_in_Cinema_Comics)
- **Related patent.** Uses EPFLP (Extended Point-Feature Label Placement) plus a QLayout score that rewards balloons being far apart from one another and near their reference points. — [USPTO 8207987](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8207987)
- **Earlier speaker-aware systems** (Preu et al., Hong et al. script-face mapping, Wang et al. speech recognition) are summarised in [arXiv 2101.11111](https://arxiv.org/pdf/2101.11111).
- **splargdotcom/speechbubble** (MIT, last commit 2026-10-06). Browser-based; generates bubbles "as procedural SVG"; tails join the body cleanly and can be dragged to the speaker; supports speech, thought and shout styles. — [GitHub](https://github.com/splargdotcom/speechbubble)
- **longweekendlabs/speech-bubble-editor** (MIT, last commit 2026-09-27). Desktop app for Windows x64, Linux x64 and macOS. Has 19 balloon styles (speech, cloud, starburst, twin/triple, caption…), draggable tails that stay pointed at the speaker, 12 bundled fonts "plus Japanese-capable fonts for manga work", and a comic-page maker. — [GitHub](https://github.com/longweekendlabs/speech-bubble-editor)
- **sunmockyang/speech-bubbles.** A JS canvas library for dynamic bubbles with tail and source point. No LICENSE file; last commit 2017-01-23 (stale). — [GitHub](https://github.com/sunmockyang/speech-bubbles)

**Reusable lettering/render code in translator projects (all CPU-capable)**
- **manga-image-translator** (zyddnys; GPL-3.0; last commit 2026-10-11; active)
  - Renderer: `manga_translator/rendering/text_render.py` uses `freetype-py`, OpenCV and `hyphen` (PyHyphen). It has a CJK horizontal↔vertical punctuation map (`CJK_H2V`), `put_text_vertical`, `calc_vertical`, glyph stroking via `freetype.Stroker`, and a `ballon_extractor.py`. There is also a "Rendering with Gimp" path.
  - Packaging: `pip-modules/mit-renderer/pyproject.toml` declares the renderer sub-package as **MIT**, while the repo LICENSE is GPL-3.0. This is a conflict; treat the code as GPL-3.0 unless clarified.
  - Install: `pip install -r requirements.txt` on Python 3.13 builds `pydensecrf` from a Py3.13 branch (needs `build-essential`). A CPU Docker web server image `zyddnys/manga-image-translator:main` exists.
  - Bundled fonts: `fonts/` contains `anime_ace.ttf`, `anime_ace_3.ttf`, `msgothic.ttc`, `msyh.ttc` and `NotoSansMonoCJK-VF.ttf.ttc`.
  - Source: [GitHub](https://github.com/zyddnys/manga-image-translator)
- **BallonsTranslator** (dmMaze; GPL-3.0; last commit 2026-10-23; active)
  - Headless CLI: `python -m ballontranslator --headless --exec_dirs "[DIR_1],[DIR_2]"`, with settings from `config/config.json` and `--ldpi` to fix font scale.
  - Text engine: Qt-based (`ballontranslator/ui/text_engine/...`).
  - Font recognition: optional, via YuzuMarker.FontDetection (MIT).
  - The README says it "heavily depends on manga-image-translator".
  - Linux install script available.
  - Source: [GitHub](https://github.com/dmMaze/BallonsTranslator); [YuzuMarker.FontDetection](https://github.com/JeffersonQin/YuzuMarker.FontDetection)
- **comic-translate** (ogkalu2; **Apache-2.0**; last commit 2026-09-10)
  - `modules/rendering/render.py` uses Pillow plus PySide6 `QTextDocument`, with `vertical_layout.py` and `hyphen_textwrap.py` (a modified CPython textwrap that inserts hyphens). Functions include `draw_text(..., init_font_size=40, min_font_size=10, outline=True)` and `pyside_word_wrap`.
  - Also has a webtoon batch renderer.
  - Install via `uv` with Python 3.12 in the README.
  - Source: [GitHub](https://github.com/ogkalu2/comic-translate)
- **koharu** (MIT OR Apache-2.0; Rust; last commit 2026-10-27; very active)
  - "Multilingual text shaping and layout with automatic fitting, font fallback, vertical CJK, and right-to-left text".
  - The `koharu-renderer` crate depends on `harfrust`, `skrifa`, `hypher` (hyphenation), `icu_segmenter` and `fontique`.
  - CPU inference is supported but "substantially slower", and the editor canvas needs WebGPU.
  - Source: [GitHub](https://github.com/mayocream/koharu) (badge points to koharu-rs/koharu); [typesetting guide](https://koharu.rs/guides/typesetting)

**Vertical Japanese text and fitting primitives**
- **Pillow.**
  - `ImageDraw.text`, `multiline_text`, `textbbox` and `textlength` accept `direction="ttb"`, `features=[...]` (OpenType) and `language` (BCP 47, since 6.0). All require libraqm.
  - Pillow wheels since 8.2.0 include a modified libraqm that loads FriBiDi at runtime.
  - There is no automatic wrap or fit-to-box helper.
  - Docs show 13.0.0. — [ImageDraw docs](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html); [build docs](https://pillow.readthedocs.io/en/stable/installation/building-from-source.html)
  - **[local test]** Pillow 12.3.0 here reports raqm 0.10.5, FriBiDi 1.0.13 and HarfBuzz 14.2.1. Vertical layout works: `ー` turns vertical and `…` becomes `⋮`. However, `multiline_text(direction="ttb")` placed the 2nd line **to the right** of the 1st (wrong for Japanese), and `！？` stacked rather than sitting side by side as tate-chu-yoko. The only system CJK fonts present were IPAGothic; `fonts-noto-cjk` 20230817 is installable via apt ([Launchpad](https://launchpad.net/ubuntu/+source/fonts-noto-cjk)).
- **CSS.** "The basics of vertical writing are supported by all major browser engines" (`writing-mode: vertical-rl`, `text-orientation`, `text-combine-upright` for tate-chu-yoko). — [W3C i18n: vertical text](https://www.w3.org/International/articles/vertical-text/)
- **Shaping and hyphenation:**
  - **uharfbuzz** 0.57.0 (Apache-2.0, abi3 wheels) for shaping. — [PyPI](https://pypi.org/project/uharfbuzz/)
  - **freetype-py** 2.5.1 (BSD, last release 2024-08-29) for glyph rendering. — [PyPI](https://pypi.org/project/freetype-py/)
  - **Pyphen** 0.18.1 (GPL-2+/LGPL-2.1+/MPL-1.1 tri-licence, pure Python, repo active 2026-10-27). — [PyPI](https://pypi.org/project/pyphen/); [GitHub](https://github.com/Kozea/Pyphen)
  - **PyHyphen** 4.0.4 (Apache-2.0, last release 2024-07-30, sdist only, so it compiles on install). — [PyPI](https://pypi.org/project/PyHyphen/)
- **Inkscape.** Ubuntu 24.04 ships 1.2.2 ([Launchpad](https://launchpad.net/ubuntu/+source/inkscape)).
  - Vertical text uses `writing-mode` (Inkscape has long written `tb-rl`) plus a "Text orientation: Upright" option. An older book notes "a number of deficiencies" for Japanese tategaki.
  - CLI export: `inkscape --export-filename=out.png -w … in.svg`, plus `--export-pdf-version`.
  - Sources: [W3C list post](https://lists.w3.org/Archives/Public/www-svg/2015Jul/0053.html); [Inkscape forum](https://inkscape.org/forums/questions/vertical-text); [O'Reilly](https://www.oreilly.com/library/view/the-book-of/9781593271817/ch15s03.html); [Debian 12 man page](https://dokk.org/manpages/debian/12/inkscape/inkscape.1.en)
- **Krita 5.3/6.0** (5 Feb 2026). Rewritten text tool: on-canvas editing, auto-wrapped text, text in shape (SVG 2), text on path, full OpenType features, and a glyph palette for CJK variants. The release notes do **not** mention vertical writing mode. Ubuntu 24.04 apt still ships Krita 5.2.2 ([Launchpad](https://launchpad.net/ubuntu/+source/krita)). — [Krita 5.3 notes](https://krita.org/en/release-notes/krita-5-3-release-notes/); [Krita Artists vertical wrap thread](https://krita-artists.org/t/about-the-issue-of-vertical-text-line-wrapping/94589)
- **Commercial / no Linux:**
  - **Clip Studio Paint** (Celsys, Ver. 5) supports Windows 10/11, macOS 14/15/26, iPadOS, iOS, Android 13+, Galaxy and Chromebook. **No Linux.** — [CSP system requirements](https://www.clipstudio.net/en/dl/system/)
  - **MediBang Paint** lists Mac, Windows, Android and iOS, with no Linux. — [AlternativeTo](https://alternativeto.net/software/medibang-paint) (secondary)

**Fonts and licences**
- **Blambot** (Nate Piekos), official licence page:
  - $0.00 fonts: "Anyone can use these typefaces for non-profit use in print, or flattened into web graphics."
  - Fonts marked "Non-profit/Indie Comics Use" are free for "independent/small press comic creators" in print, flattened web graphics and merchandise, "even if you are making money with your project".
  - Mainstream publishers (Marvel, DC, Image, IDW, Dark Horse, etc.) need a commercial licence.
  - The free clause "does not apply to any other 'indie' use or industry other than comic book creation".
  - An Embedding licence ("including the typeface software in third party software or an app") is separate and requires that fonts not be accessible to end users.
  - The page says nothing about AI.
  - Source: [Blambot licenses](https://blambot.com/pages/licenses)
- **Anime Ace (Blambot).** A distribution notice calls it freeware for independent comic creation and non-profit use, with no redistribution. — [online-fonts.com](https://online-fonts.com/fonts/anime-ace). This **conflicts** with 1001fonts ("free for personal use", not commercial) — [1001fonts](https://www.1001fonts.com/anime-ace-font.html) — and with Dafont ("personal use only"). Blambot's own page is authoritative.
- **Comicraft Wildwords** (the classic manga-translation dialogue face). $49 per style, or $139 for the 4-font family. No free or indie tier was found. — [Fontspring](https://fontspring.com/fonts/comicraft/wildwords); [MyFonts](https://myfonts.com/fonts/comicraft/wild-words)
- **Shippori Antique** (FONTDASU). **SIL OFL 1.1**, "created to provide people who draw manga in Japan a beautiful antique font for free". Antique Mincho-style kana with old sans Latin. On Google Fonts; B1 variant also OFL. — [Fontsource](https://fontsource.org/fonts/shippori-antique/about); [Google Fonts](https://fonts.google.com/specimen/Shippori%2BAntique/about)
- **源暎アンチック / GenEi Antique** (おたもん / okoneya). A "漫画向けフリーフォント" (free font for manga) for dialogue, with manga-specific ！/？ variants and a vertical-setting sample. The info page lists v4 / Ver 4.1 (2018-03-13) but also mentions Ver 5.0+ features. **The licence is not stated on that page.** — [okoneya.jp](https://okoneya.jp/font/genei-antique.html)
- **Japanese magazine norms (Clip Studio official tips):**
  - Dialogue size "10-14pt is commonly used"; some editors specify Q (1 Q = 0.25 mm).
  - Line spacing standard 125% (some magazines 130%); ruby lines about 150%.
  - The example font is "I-OTF Antics StdB" (commercial).
  - Source: [CSP Tips 9582](https://tips.clip-studio.com/en-us/articles/9582)

**Lettering conventions (English) from Blambot's "Comic Book Grammar & Tradition"**
- Tails point at the speaker's mouth.
- Bold italic marks emphasis.
- Ellipses are exactly 3 dots; use double dashes, not em/en dashes.
- Avoid hyphenation where possible; one space after end punctuation.
- Crossbar "I" only for the pronoun "I" and acronyms.
- Balloon types: burst for screaming, dashed outline for whispers, wavy for distress; radio balloons are italic and spiky.
- Thought balloons have small circular tails pointed at the head.
- Off-panel speech: the tail butts against the panel border.
- Avoid balloons crossing borders, and avoid tangents.
- Joined balloons mean the same thought.
- Spell out numbers; sound effects are usually unpunctuated.
- Source: [Blambot grammar](https://blambot.com/pages/comic-book-grammar-tradition)

**Sound effects (SFX) handling in localisation**
- Common options:
  - keep the Japanese SFX and add a small translation nearby;
  - replace or overlay it;
  - add glossaries or footnotes;
  - some scanlations tag translated sounds "*SFX".
- Sources: [1stopasia blog](https://www.1stopasia.com/blog/sound-effects-and-visual-language-translating-the-untranslatable-in-manga/); [Kanzenshuu forum](https://www.kanzenshuu.com/forum/viewtopic.php?p=117440)
- Manga109 has a public "Comic Onomatopoeia (COO)" annotation set: quadrilateral boxes plus katakana text such as `ドド~・~・・ン`, licensed CC BY 4.0 (LICENSE_COO). — [manga109/public-annotations](https://github.com/manga109/public-annotations)

### Inferences
- **Licence-safe code reuse.** Borrow fitting and vertical-layout logic from **comic-translate** (Apache-2.0; needs PySide6, likely fine headless with `QT_QPA_PLATFORM=offscreen`, which is unverified) or **koharu-renderer** (MIT/Apache, Rust). Copying from manga-image-translator or BallonsTranslator makes the derivative GPL-3.0.
- **Don't redistribute bundled fonts.** manga-image-translator's `msgothic.ttc`, `msyh.ttc` and `anime_ace*.ttf` are proprietary or limited-licence fonts.
- **Minimal own algorithm:**
  1. Get the speaker's face/head box from Magi or the detector (Q4).
  2. Pick candidate balloon positions in reading order: upper-right first for Japanese, upper-left for English.
  3. Score by overlap with faces/characters, distance to the speaker, and order consistency (the EPFLP/QLayout idea).
  4. Size the ellipse to text by binary search on font size, with min font clamped to about 10–14 pt-equivalent at print size.
  5. Draw the tail as a tapered triangle aimed at the mouth.
- **English edition fonts.** Comic-style all-caps fonts (Blambot free or Comic Neue), no hyphenation, bold italic for emphasis.
- **Japanese edition fonts.** Shippori Antique, vertical columns progressing right-to-left, 125% leading.

### Gaps
- GenEi Antique licence terms (download page not fetched).
- Scribus 1.6.1 (apt) vertical CJK support was not checked.
- Krita 5.3 vertical text support is unconfirmed by the release notes.
- WeasyPrint's `writing-mode` support was not checked.
- Comic Neue / Bangers licences were not verified this session.
- No maintained Python library for automatic balloon + tail placement was found.

---

## Q3. Screentone, halftone, inking and line-art conversion, and AI models that output monochrome manga

### Takeaway
- **Classical, CPU, scriptable halftoning is mature.** Three good options:
  - ImageMagick `-ordered-dither h6x6a/h8x8a/c7x7b` (verified locally);
  - the GEGL `gegl:newsprint` op through the `gegl` CLI, with angle, period and pattern control;
  - Krita's screentone generator and halftone filter (GUI).
- **Learned screentone research is mostly GPU or abandoned.** ScreenVAE has no official code found. Sketch2Manga (2024) runs as ComfyUI on SD1.5 + ControlNet.
- **Line-art extraction runs on CPU.** Anime2Sketch, MangaLineExtraction ("erika", 43M params, HF port) and controlnet_aux lineart/lineart_anime/TEED/Anyline all accept CPU (slowly). Vectorise with vtracer (MIT) or potrace (GPL).

### Cited Findings

**Classical halftone / screentone**
- **ImageMagick ordered-dither maps:**
  - 45° screens `h4x4a`, `h6x6a`, `h8x8a`; orthogonal `h4x4o`, `h6x6o`, `h8x8o`, `h16x16o`; circles `c7x7b`/`c7x7w`.
  - Greyscale output needs `-colorspace Gray` first, e.g. `magick in.png -colorspace Gray -ordered-dither h8x8o out.gif`.
  - Rotated screens are not built in: rotate a tile with `-distort SRT`, though rotated tiles "do not tile very well".
  - Levels syntax: `o8x8,13`.
  - Source: [ImageMagick Usage: quantize](https://usage.imagemagick.org/quantize/)
  - **[local test]** IM 6.9.12-98 (Ubuntu apt) lists `h4x4a…h16x16o`, `c5x5b` and `c7x7*`, and `-ordered-dither h6x6a` on a gradient gives a pure 2-colour PNG.
- **GEGL `gegl:newsprint`** (digital halftoning):
  - colour model black, RG, RGB or CMYK; per-ink `pattern`;
  - `period` (default 12 px); `angle` (default black 75°);
  - `aa-samples` (default 16), `turbulence`, `blocksize`, `angleboost`, `black-pullout`.
  - Source: [GEGL op page](https://gegl.org/operations/gegl-newsprint.html)
  - CLI form: `gegl -o output.png -- op property=value`. — [GEGL CLI](https://gegl.org/commandline.html)
  - Ubuntu 24.04 apt has gegl 0.4.48 and GIMP 2.10.36. — [Launchpad gegl](https://launchpad.net/ubuntu/+source/gegl); [Launchpad gimp](https://launchpad.net/ubuntu/+source/gimp)
  - GEGL licence files: COPYING (GPL-3) + COPYING.LESSER (LGPL-3). — [GNOME/gegl](https://github.com/GNOME/gegl)
- **Krita:**
  - Screentone fill-layer generator (since 4.4) for "dots and lines, similar to traditional screentone". — [Krita docs](https://docs.krita.org/en/reference_manual/layers_and_masks/fill_layer_generators/screentone.html)
  - A newer halftone filter takes its screen from fill-layer generators. — [Krita filters docs](https://docs.krita.org/reference_manual/filters/artistic.html); [MR 409](https://invent.kde.org/graphics/krita/-/merge_requests/409)
  - Used as a filter mask it recomputes in real time and can be slow on large canvases. — [Krita Artists](https://krita-artists.org/t/screentone-quality-of-krita-4-4-x/24159?page=4)
- **Python halftone / dither tools:**
  - **philgyford/python-halftone**: greyscale or CMYK dots, `angles`, `sample`, `scale`. **No LICENSE file** in the repo; last commit 2021-12-21. — [GitHub](https://github.com/philgyford/python-halftone)
  - **didder** (Go CLI): "extensive, fast, and accurate command-line image dithering tool… designed to work well for… pipeline scripting", Bayer and other ordered dithers. GPL-3.0; last commit 2026-02-03. — [GitHub](https://github.com/makew0rld/didder)
- **Japanese tone terms.** In CSP, 線数 (line count) is the halftone dot pitch (網点の間隔); 濃度 is density in %; the "standard" patterns are circle or line; 砂目 (sand-grain) tone uses noise. — [gihyo.jp PDF](https://gihyo.jp/assets/files/book/2025/978-4-297-15158-4/9784297151584-01.pdf) **[local pdftotext]**

**Learned screentone research**
- **ScreenVAE** ("Manga Filling Style Conversion with Screentone VAE", Xie, Li, Wong, ACM TOG 2020): no official code found; `github.com/msxie92/ScreenVAE` failed to clone. — [Semantic Scholar](https://www.semanticscholar.org/paper/Manga-filling-style-conversion-with-screentone-Xie-Li/90744aa25664e8878fd8d451f582f482af8c7424)
- **MangaRestoration** (msxie92, "Exploiting Aliasing for Manga Restoration"): custom CUHK licence allowing academic, research and commercial use, with written notice to the author for commercial use. Last commit 2021-07-19. — [GitHub](https://github.com/msxie92/MangaRestoration)
- **Sketch2Manga** (Lin et al., arXiv 2403.08266, 2024). Diffusion turns a sketch into a colour illustration, then intensity-guided screening produces screentoned manga. — [arXiv](https://arxiv.org/abs/2403.08266)
  - Community implementation **dmMaze/sketch2manga**: ComfyUI workflow + Gradio. It needs an SD1.5 colourisation checkpoint, `control_v11p_sd15_lineart`, and finetuned `mangatone` VAE + diffusion weights. No LICENSE file in the repo; last commit 2025-03-31. — [GitHub](https://github.com/dmMaze/sketch2manga)
  - The weights (`dreMaz/sketch2manga`) are MIT on HF. — [HF](https://huggingface.co/dreMaz/sketch2manga)
- **kktsubota/manga-character-screentone** ("Synthesis of Screentone Patterns of Manga Characters"): BSD-2, "I only provide a demo script now", last commit 2023-07-30. — [GitHub](https://github.com/kktsubota/manga-character-screentone)
- **Other papers:** "Screentone-Preserved Manga Retargeting" ([arXiv 2203.03396](https://arxiv.org/pdf/2203.03396)), "Screentone-Aware Manga Super-Resolution" ([arXiv 2305.08325](https://arxiv.org/pdf/2305.08325)), "Deep Comic Screening via Tone-aware Semantic Layer Analysis" ([PDF](https://www.sfu.edu.hk/filemanager/en/content_2095/Deep%20Comic%20Screening%20via%20Tone-aware%20Semantic%20Layer%20Analysis.pdf)).

**Line-art extraction (all PyTorch; CPU possible)**

| Tool | Licence / activity | Weights | Usage / notes |
|---|---|---|---|
| [Anime2Sketch](https://github.com/Mukosame/Anime2Sketch) | MIT; last commit 2026-10-18 | Google Drive, plus an "artifact-free" variant | Requirements: "CPU or NVIDIA GPU + CUDA CuDNN". `python3 test.py --dataroot in/ --load_size 512 --output_dir out/` |
| [MangaLineExtraction_PyTorch](https://github.com/ljsabc/MangaLineExtraction_PyTorch) (paper "Deep Extraction of Manga Structural Lines") | MIT; last commit 2025-01-10 | `erika.pth` (GitHub release / Dropbox) | HF port [p1atdev/MangaLineExtraction-hf](https://huggingface.co/p1atdev/MangaLineExtraction-hf): MIT, ~43.1M params |
| [informative-drawings](https://github.com/carolineec/informative-drawings) | MIT; last commit 2024-08-31 | Google Drive | `python test.py --name anime_style` |
| [controlnet_aux](https://github.com/huggingface/controlnet_aux) (`pip install controlnet-aux`, 0.0.10, 2025-05-08) | Apache-2.0; repo last commit 2025-05-08 (slowing) | Annotator weights from `lllyasviel/Annotators` (HF licence "other") | `LineartDetector`, `LineartAnimeDetector`, `TEEDdetector`, `AnylineDetector`; "use cpu by default" |
| [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) | Apache-2.0; last commit 2026-10-11 | — | Exposes "Manga Lineart" (`lineart_anime_denoise`), Anime Lineart, Standard Lineart, TEED and AnyLine. [Anyline](https://github.com/TheMistoAI/ComfyUI-Anyline) is MIT; MistoLine weights are openrail++ |
| sketchKeras | Apache-2.0; last commit 2017-05-04 (stale) | — | — |

**Vectorising line art**
- **vtracer** 0.6.15: MIT, cp313 wheel, repo active 2026-10-22. — [PyPI](https://pypi.org/project/vtracer/); [GitHub](https://github.com/visioncortex/vtracer)
- **potrace** 1.16 (apt, GPL). — [Launchpad](https://launchpad.net/ubuntu/+source/potrace)
- **potracer** (pure-Python port, GPLv2+, 2022). — [PyPI](https://pypi.org/project/potracer/)

**Models that output monochrome manga directly (GPU-class)**
- **drawatoon-v1** (fumeisama): a PixArt-Sigma fine-tune that "can generate pretty decent black-and-white manga art". About 763M params; no licence in the card metadata; modified 2025-04-11. — [HF](https://huggingface.co/fumeisama/drawatoon-v1) (claim via Reddit mirror)
- **Community LoRAs.** Monochrome manga LoRAs exist on CivitAI. One tester found that SDXL manga LoRAs at low denoise kept colour and that stacking a character LoRA pushed output toward pale greyscale. — [civarchive](https://civarchive.com/models/760255); [lilting.ch test](https://lilting.ch/en/articles/manga-bw-workflow-test-draft)

### Inferences
- **Recommended CPU pipeline for "colour/grey panel → manga page":**
  1. Extract line art (MangaLineExtraction or Anime2Sketch at 512–1024 px on CPU, likely seconds to tens of seconds per panel; not benchmarked).
  2. Posterise the original luminance into 3–4 tone levels.
  3. Fill each level with a fixed screen: ImageMagick `h6x6a`/`h8x8a`, or a numpy-generated dot screen at a chosen pitch and 45°, stored as 1-bit at 600 dpi.
  4. Composite the lines on top as pure black.
  5. Optionally vectorise lines with vtracer.

  This mimics a 線数/濃度 tone workflow and avoids GPU models.
- **Screen frequency.** Generate tone at final print resolution. Halftoning before downscaling causes moiré; ImageMagick notes rotated tiles don't tile cleanly, which argues for generating rotated dot screens analytically.
- **GPU models are optional.** Sketch2Manga, drawatoon and DiffSensei are optional upstream generators and impractical on this 4-vCPU box. They belong to the image-generation research track.

### Gaps
- No official ScreenVAE code.
- No CPU timing benchmarks were found for any line-art model.
- Typical Japanese screentone line counts (e.g. 50–70 lines/inch) were not verified from a primary source.
- Licences of the `lllyasviel/Annotators` weights ("other") were not inspected.
- The Krita screentone/halftone features run inside Krita. Whether Krita's CLI/Python can apply them headless was not verified.

---

## Q4. Manga understanding and analysis tools for validation or layout learning

### Takeaway
- **Detectors.** Magi v1/v2/v3 detect panels, text, characters and tails, output reading order and transcripts, and v3 adds OCR. They are **academic-research-only**, and the README examples use `.cuda()`.
- **Commercially usable alternative.** The Apache-2.0 **ogkalu/comic-text-and-bubble-detector** (RT-DETR-v2, 43M params) handles balloon and text QA. **Kumiko** (AGPL-3.0, OpenCV only, has `--rtl`) handles panel extraction and order.
- **Data.** Manga109 is the reference dataset (academic only); Manga109-s (87 volumes) is approved for commercial use.

### Cited Findings
- **Magi (ragavsachdeva/magi).** Last commit 2025-06-27. Usage examples: `AutoModel.from_pretrained("ragavsachdeva/magi"|"magiv2", trust_remote_code=True).cuda()`; v3 uses `AutoModelForCausalLM` with float16. Licence: "The provided models and datasets are available for academic research purposes only." — [GitHub](https://github.com/ragavsachdeva/magi)
  - HF metadata: magi v1 about 516M params (modified 2025-04-09); magiv2 (modified 2025-03-07); magiv3 about 833M params (modified 2026-07-21). No licence field in the cards. — [magi](https://huggingface.co/ragavsachdeva/magi); [magiv2](https://huggingface.co/ragavsachdeva/magiv2); [magiv3](https://huggingface.co/ragavsachdeva/magiv3)
  - Magiv3 (ICCV 2025, "From Panels to Prose") detects characters, texts, panels and tails in one model, plus character clustering, text–character matching and OCR. It has poor text detection and no OCR on Chinese/Korean comics. — [ICCV 2025 supplemental](https://openaccess.thecvf.com/content/ICCV2025/supplemental/Sachdeva_From_Panels_to_ICCV_2025_supplemental.pdf)
  - A third-party review says boxes are output already in reading order. — [Moonlight review](https://www.themoonlight.io/es/review/from-panels-to-prose-generating-literary-narratives-from-comics)
  - Magi v1 (CVPR 2024) sorts text boxes into reading order to produce transcripts. — [CVPR 2024](https://cvpr.thecvf.com/virtual/2024/poster/31457)
- **ogkalu/comic-text-and-bubble-detector.** Apache-2.0. RT-DETR-v2 r50vd fine-tuned on about 11k manga/webtoon/manhua/Western images at 640 px. Classes: `bubble`, `text_bubble`, `text_free`. About 42.9M params; modified 2026-05-15. — [HF](https://huggingface.co/ogkalu/comic-text-and-bubble-detector)
- **comic-text-detector** (dmMaze). GPL-3.0; last commit 2023-08-13 (stale). — [GitHub](https://github.com/dmMaze/comic-text-detector)
- **manga-ocr** (kha-white). Apache-2.0; last commit 2026-07-19; `pip install manga-ocr` (0.1.16); GPU optional. — [GitHub](https://github.com/kha-white/manga-ocr); [PyPI](https://pypi.org/project/manga-ocr/)
- **mokuro** (GPL-3.0, 0.2.5) uses manga-ocr to build HTML overlays. — [PyPI](https://pypi.org/project/mokuro/)
- **Kumiko** (njean42). **AGPL-3.0**; last commit 2024-12-22. Only dependency is `python3-opencv`. Outputs panel JSON for a page or a whole book; "Add the `--rtl` option to have them sorted in right-to-left reading order (e.g. mangas)". — [GitHub](https://github.com/njean42/kumiko)
- **Manga109.** 109 volumes, 21,142 pages, 1970s–2010s, UTokyo Aizawa-Yamasaki-Matsui Lab. "Limited to academic, non-commercial purposes"; **"87 of the 109 volumes have been newly approved for commercial use… Manga109-s"**.
  - Annotations: face, body, text (with content) and frame boxes in per-volume XML; latest annotation version v2026.05.21.
  - Sources: [Manga109](http://www.manga109.org/en/download.html); [annotations](http://www.manga109.org/en/annotations.html)
  - Public extra annotations: COO onomatopoeia (CC BY 4.0), Manga109Dialog (speaker links), MangaUB. — [public-annotations](https://github.com/manga109/public-annotations)
  - `manga109api` (MIT, 0.3.1, 2020) is a Python parser. — [GitHub](https://github.com/manga109/manga109api)
- **Panel and text detectors** used for Manga109 splits: DASS_Det_Inference (Apache-2.0, active 2026-10-03). — [GitHub](https://github.com/barisbatuhan/DASS_Det_Inference)

### Inferences
- **QA loop for generated pages:**
  1. Run Kumiko `--rtl` (or Magi in research use) on each rendered page and check that detected panel order matches script order.
  2. Run the Apache-2.0 bubble detector and check that every script line landed in a `text_bubble` and no text leaks outside (`text_free` should only be captions/SFX).
  3. Optionally OCR back with manga-ocr (Japanese) to catch clipped glyphs.

  All of this runs on CPU. Magi v1 at about 516M params should run on CPU in float32 if `.cuda()` is dropped (untested).
- **Learning layout priors.** Training on Manga109 frame boxes is fine for research. A shipped commercial product should use Manga109-s or the CC-BY COO annotations.

### Gaps
- Exact Manga109-s licence text and application process (site returns a TLS host-name mismatch over HTTPS; the HTTP page was used).
- Magi CPU runtime is not benchmarked.
- comic-text-detector CPU/ONNX status is not confirmed.

---

## Q5. Export formats (CBZ/CBR, PDF, EPUB fixed layout, webtoon strips) and command-line builders

### Takeaway
- **CBZ** (zip of numbered images plus `ComicInfo.xml` with `<Manga>YesAndRightToLeft</Manga>`) and **PDF** (img2pdf, lossless) are trivial to script.
- **Fixed-layout EPUB** for RTL manga needs `rendition:layout=pre-paginated` and `page-progression-direction="rtl"`, which KCC generates.
- **KCC** (`kcc-c2e -m` for manga RTL, `-w` for webtoon) is the actively maintained (2026-10-26) ISC-licensed CLI that converts image folders to EPUB/KEPUB/MOBI/CBZ/PDF.
- **Webtoon.** Vertical strips should be sliced to ≤800×1280 px per image for WEBTOON Canvas (SmartStitch console or Pillow).

### Cited Findings
- **Comic archive types.** CBZ = ZIP, CBR = RAR, CB7 = 7z, CBT = TAR (.cba = ACE). The first image is typically the cover; extra metadata can live as embedded XML. — [Wikipedia: Comic book archive](https://en.wikipedia.org/wiki/Comic_book_archive)
- **ComicInfo.xml (Anansi Project).**
  - `Manga` = `YesAndRightToLeft` defines RTL reading.
  - `Pages/ComicPageInfo` has `Image`, `Type` (FrontCover, InnerCover, Story, BackCover, Delete…), `DoublePage`, `ImageWidth`/`ImageHeight`.
  - `LanguageISO` is recommended as a BCP 47 tag; `BlackAndWhite`; `Format` (e.g. "Digital", "Web").
  - Schema v2.0 is the latest final; v2.1 is a draft.
  - Source: [ComicInfo docs](https://anansi-project.github.io/docs/comicinfo/documentation)
- **EPUB 3.3:**
  - `page-progression-direction` "sets the global direction in which the content flows. Allowed values are `ltr`, `rtl` and `default`".
  - `rendition:layout` `pre-paginated` means reading systems "produce exactly one page per spine itemref".
  - `rendition:spread` controls synthetic spreads; `page-spread-right` (alias `rendition:page-spread-right`) marks a spread's right page.
  - Source: [W3C EPUB 3.3](https://www.w3.org/TR/epub-33/)
- **KCC – Kindle Comic Converter** (ciromattia/kcc; ISC; last commit 2026-10-26)
  - Inputs: image folders, CBZ/EPUB, PDF. Outputs: MOBI/AZW3, EPUB, KEPUB, CBZ, PDF, folders.
  - CLI: `kcc-c2e [options] input` with `-p PROFILE`, `-m/--manga-style` ("right-to-left reading and splitting"), `-w/--webtoon`, `-u/--upscale`, `-s/--stretch`, `-c` cropping, `--forcecolor`.
  - "RTL mode only affects splitting order for CBZ output. Your cbz reader itself sets the page turn direction."
  - Calibre "doesn't properly support fixed layout EPUB/MOBI".
  - Installs: Linux, Docker, flatpak and AppImage via the wiki, or `pip install -r requirements.txt` from source. Note that `KindleComicConverter` does not resolve on PyPI.
  - Source: [GitHub](https://github.com/ciromattia/kcc); [install wiki](https://github.com/ciromattia/kcc/wiki/Installation); PyPI 404 checked 2026-10-27
  - Caution: Ubuntu's apt package **`kcc` (2.3+really-0.1) is a different program**, not Kindle Comic Converter. Its identity as the Japanese "Kanji Code Converter" is from memory and unverified. — [Launchpad kcc](https://launchpad.net/ubuntu/+source/kcc)
- **img2pdf.** Lossless JPEG/PNG → PDF. LGPL-3.0; pip 0.6.3 (2025-11-05), apt 0.5.1; repo active 2026-07-01. — [PyPI](https://pypi.org/project/img2pdf/); [GitHub](https://github.com/josch/img2pdf)
- **comictagger.** ComicInfo/CBZ tagging. Apache-2.0; repo active 2026-09-06, but **PyPI is stale (1.5.5 from 2022-11-26)**. — [GitHub](https://github.com/comictagger/comictagger); [PyPI](https://pypi.org/project/comictagger/)
- **ebooklib.** EPUB writer; **AGPL-3.0**; 0.20 (2025-10-26). — [PyPI](https://pypi.org/project/ebooklib/)
- **Node EPUB writers:** epub-gen-memory (MIT, 1.1.2) and jszip (MIT/GPL-3.0, 3.10.2) for hand-rolled EPUB/CBZ. — [npm epub-gen-memory](https://www.npmjs.com/package/epub-gen-memory); [npm jszip](https://www.npmjs.com/package/jszip)
- **Calibre.** Calibre 7.6.0 is in Ubuntu 24.04 apt, but see KCC's caution on fixed layout. — [Launchpad calibre](https://launchpad.net/ubuntu/+source/calibre)
- **Webtoon.**
  - WEBTOON's Creators Resource Handbook says to upload "within 800x1280px". Limits: 2 MB max per image, up to 20 MB / 100 images per episode, JPG/JPEG/PNG. Oversized images are auto-sliced and reduced. — [WEBTOON handbook PDF](https://webtoons-static.pstatic.net/creator101/en/pdf/Creators-Resource-Handbook-Updated.pdf)
  - A third-party page claims about 16,000 px per slice (conflicts with the handbook). — [imageonline.io](https://imageonline.io/webtoon-layout-generator/)
- **SmartStitch** (MechTechnology). MIT; last commit 2026-05-07. Stitches and slices webtoon strips; console version runs "on any platform with Python" 3.10+; flags include `--input_folder/-i`, output type `-t`, and a rough output height. — [GitHub](https://github.com/MechTechnology/SmartStitch)
- **Archivers.** 7zip 23.01 is in Ubuntu 24.04 apt; `zip` is already installed in the container. — [Launchpad 7zip](https://launchpad.net/ubuntu/+source/7zip)

### Inferences
- **Recommended outputs:**
  - (1) `pages/0001.png…` at print resolution;
  - (2) a CBZ built with Python `zipfile`: images in zero-padded order + `ComicInfo.xml` (`Manga=YesAndRightToLeft`, `BlackAndWhite=Yes`, `LanguageISO`);
  - (3) a print PDF via img2pdf at the trim size plus bleed;
  - (4) e-reader EPUB/KEPUB via `kcc-c2e -m -p <profile>`;
  - (5) for webtoon, a Pillow vertical concatenation sliced into 800×1280 chunks.
- **Avoid CBR.** RAR creation requires the proprietary `rar` tool (general knowledge, not verified this session).

### Gaps
- KCC's current EPUB output was not inspected for RTL spine attributes.
- No primary source was found on RAR creation licensing.
- WEBTOON's live help-centre wording (hard cap vs. recommendation) was not checked.

---

## Q6. Consolidated per-tool inventory: licence, Linux install, headless/CPU, maintenance (checked 2026-10-27)

### Takeaway
Everything needed to assemble pages is available CPU-only on Ubuntu 24.04 via pip or apt:
- **Layout and letters:** Pillow (with raqm), drawsvg/skia-python, Playwright/Chromium for CSS vertical text.
- **Tone and lines:** ImageMagick, GEGL, vtracer, controlnet_aux, MangaLineExtraction, Anime2Sketch.
- **Packaging:** img2pdf, zip, KCC.
- **QA:** the Apache bubble detector, Kumiko, manga-ocr.

Licence traps:
- GPL/AGPL code: manga-image-translator, BallonsTranslator, comic-text-detector, Kumiko (AGPL), ebooklib (AGPL), mokuro, didder, potrace.
- Research-only models and data: Magi, full Manga109.
- Repos with no licence: DiffSensei, dmMaze/sketch2manga, python-halftone, comfyui-panelforge.
- Fonts: proprietary fonts bundled in manga-image-translator.

GPU or desktop-only, not usable here: DiffSensei (24 GB GPU), Sketch2Manga (SD1.5 GPU), koharu's editor (needs WebGPU), Clip Studio Paint and MediBang (no Linux).

### Cited Findings

| Tool | Role | Licence | Linux install | Headless / CPU | Last activity |
|---|---|---|---|---|---|
| [Pillow](https://pypi.org/project/pillow/) | raster compose, text (ttb via raqm) | MIT-CMU | pip (cp313 wheel) | yes / yes | 13.0.0, 2026-10-16 |
| [drawsvg](https://pypi.org/project/drawsvg/) | SVG panels/balloons | MIT | pip | yes / yes | 2.4.2, 2026-08-12 |
| [skia-python](https://pypi.org/project/skia-python/) | vector raster | BSD | pip (cp313) | yes / yes | 144.1, 2026-10-20 |
| [pycairo](https://pypi.org/project/pycairo/) | vector raster | LGPL-2.1/MPL-1.1 | pip sdist + `libcairo2-dev` | yes / yes | 1.29.2, 2026-10-04 |
| [Playwright](https://pypi.org/project/playwright/) | HTML/CSS → PNG/PDF (vertical-rl) | Apache-2.0 | pip/npm + `playwright install chromium` | yes / yes | 1.64.1, 2026-10-22 |
| [typst (py)](https://pypi.org/project/typst/) + [basho](https://typst.app/universe/package/basho) | typeset pages | Apache-2.0 (typst-py) | pip (abi3) | yes / yes | 0.15.0, 2026-06-16; basho 0.1.0 |
| [uharfbuzz](https://pypi.org/project/uharfbuzz/) / [freetype-py](https://pypi.org/project/freetype-py/) | shaping / glyphs | Apache-2.0 / BSD | pip | yes / yes | 0.57.0 2026-10-23 / 2.5.1 2024-08-29 |
| [Pyphen](https://github.com/Kozea/Pyphen) | hyphenation | GPL/LGPL/MPL tri | pip (pure) | yes / yes | 0.18.1; repo 2026-10-27 |
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) | detect/OCR/inpaint/render (vertical CJK) | GPL-3.0 | pip -r / Docker (CPU image) | yes / yes (slow) | 2026-10-11 |
| [BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) | lettering app, headless batch | GPL-3.0 | install.sh / python | `--headless` / yes | 2026-10-23 |
| [comic-translate](https://github.com/ogkalu2/comic-translate) | lettering app, render code | Apache-2.0 | uv + requirements (Py3.12 in docs) | Qt app; render needs PySide6 | 2026-09-10 |
| [koharu](https://github.com/mayocream/koharu) | Rust translator/typesetter | MIT/Apache-2.0 | release builds (Linux) | CPU slow; editor needs WebGPU | 2026-10-27 |
| [speechbubble](https://github.com/splargdotcom/speechbubble) | SVG bubble generator (browser) | MIT | static web | browser | 2026-10-06 |
| [speech-bubble-editor](https://github.com/longweekendlabs/speech-bubble-editor) | desktop bubble/page tool | MIT | Linux x64 release | GUI | 2026-09-27 |
| [StoryDiffusion utils](https://github.com/HVision-NKU/StoryDiffusion) | Pillow comic grid/caption helpers | Apache-2.0 | git | yes / yes (helpers only) | 2024-09-26 |
| [AI Comic Factory](https://github.com/jbilcke-hf/ai-comic-factory) | CSS-grid layouts, bubble component | Apache-2.0 | Node/Next.js | browser | 2025-10-30 |
| [ImageMagick](https://usage.imagemagick.org/quantize/) | halftone (`-ordered-dither h*`), compositing | ImageMagick License | apt (6.9.12-98 installed) | yes / yes | repo active 2026-10-27 |
| [GEGL](https://gegl.org/operations/gegl-newsprint.html) | `gegl:newsprint` halftone CLI | LGPL-3/GPL-3 | apt gegl 0.4.48 | yes / yes | repo active 2026-10-24 |
| [Krita](https://krita.org/en/release-notes/krita-5-3-release-notes/) | screentone generator, halftone filter, text, panel tool | GPL (KDE) | apt 5.2.2; 5.3/6.0 via upstream builds | GUI (CLI export unverified) | 5.3.0 released 2026-02-05; 5.3.2 bugfix |
| [Inkscape](https://launchpad.net/ubuntu/+source/inkscape) | SVG lettering, CLI export | GPL | apt 1.2.2 | CLI export yes | — |
| [didder](https://github.com/makew0rld/didder) | dithering CLI | GPL-3.0 | Go binary | yes / yes | 2026-02-03 |
| [python-halftone](https://github.com/philgyford/python-halftone) | dot halftone | **no licence file** | git | yes / yes | 2021-12-21 |
| [Anime2Sketch](https://github.com/Mukosame/Anime2Sketch) | line art | MIT | git + pip -r; weights GDrive | yes / yes | 2026-10-18 |
| [MangaLineExtraction](https://github.com/ljsabc/MangaLineExtraction_PyTorch) | manga structural lines | MIT | git / HF port | yes / yes | 2025-01-10 |
| [informative-drawings](https://github.com/carolineec/informative-drawings) | line drawings | MIT | git; weights GDrive | yes / yes | 2024-08-31 |
| [controlnet_aux](https://github.com/huggingface/controlnet_aux) | lineart/anime/TEED/Anyline | Apache-2.0 (weights vary) | pip `controlnet-aux` | yes / CPU default | 2025-05-08 |
| [vtracer](https://github.com/visioncortex/vtracer) | raster→SVG | MIT | pip (cp313) | yes / yes | 2026-10-22 |
| [potrace](https://launchpad.net/ubuntu/+source/potrace) | bitmap→vector | GPL | apt 1.16 | yes / yes | — |
| [dmMaze/sketch2manga](https://github.com/dmMaze/sketch2manga) | diffusion screentoning | no licence file (weights MIT) | ComfyUI node | **GPU** practical | 2025-03-31 |
| [DiffSensei](https://github.com/jianzongwu/DiffSensei) | layout-conditioned manga gen | no licence file | git | **24 GB GPU** | 2025-02-05 |
| [Magi v1–v3](https://github.com/ragavsachdeva/magi) | panels/text/chars/tails/order/OCR | **academic research only** | HF transformers | examples `.cuda()`; CPU untested | repo 2025-06-27; v3 weights 2026-07-21 |
| [comic-text-and-bubble-detector](https://huggingface.co/ogkalu/comic-text-and-bubble-detector) | bubble/text QA | Apache-2.0 | HF (RT-DETR-v2) | yes / yes (43M params) | 2026-05-15 |
| [Kumiko](https://github.com/njean42/kumiko) | panel detection, `--rtl` order | **AGPL-3.0** | git + apt `python3-opencv` | yes / yes | 2024-12-22 |
| [manga-ocr](https://github.com/kha-white/manga-ocr) | JP OCR for QA | Apache-2.0 | pip | yes / yes | 2026-07-19 |
| [Manga109 / -s](http://www.manga109.org/en/download.html) | dataset | academic only / 87 vols commercial | request access | — | annotations v2026.05.21 |
| [KCC](https://github.com/ciromattia/kcc) | EPUB/KEPUB/MOBI/CBZ/PDF builder | ISC | source / Docker / AppImage / flatpak | CLI `kcc-c2e` / yes | 2026-10-26 |
| [img2pdf](https://github.com/josch/img2pdf) | lossless PDF | LGPL-3.0 | pip 0.6.3 / apt 0.5.1 | yes / yes | 2026-07-01 |
| [comictagger](https://github.com/comictagger/comictagger) | ComicInfo tagging | Apache-2.0 | GitHub (PyPI stale 2022) | CLI / yes | 2026-09-06 |
| [SmartStitch](https://github.com/MechTechnology/SmartStitch) | webtoon stitch/slice | MIT | git, Python 3.10+ console | yes / yes | 2026-05-07 |
| [Clip Studio Paint](https://www.clipstudio.net/en/dl/system/) | pro manga suite | commercial | **no Linux** | GUI | Ver. 5 |
| [MediBang Paint](https://alternativeto.net/software/medibang-paint) | manga paint app | freemium, proprietary | **no Linux** listed | GUI | — |

### Inferences
- **Minimal install set for this container:**
  - pip: `pillow drawsvg skia-python shapely uharfbuzz pyphen img2pdf vtracer opencv-python-headless playwright manga-ocr controlnet-aux`, plus `torch` CPU wheels (2.14.1 has cp313 manylinux wheels per [PyPI](https://pypi.org/project/torch/)) and `onnxruntime` 1.31.1 (cp313, [PyPI](https://pypi.org/project/onnxruntime/)).
  - apt: `fonts-noto-cjk potrace gegl 7zip` (ImageMagick already present).
  - Fonts: Shippori Antique from Google Fonts.
  - From git: Kumiko (if AGPL is acceptable) and KCC.

  All are CPU-capable. Model weights (Anime2Sketch, MangaLineExtraction, bubble detector) download from Google Drive, Dropbox or HF.
- **Prefer Apache/MIT/BSD components** so the assembly code stays permissively licensed. Keep GPL tools (ImageMagick is fine, GEGL/potrace/didder run as CLIs) as separate processes rather than linked or copied code.

### Gaps
- Krita headless scripting for screentone/halftone (`krita --export` / Python without GUI) was not verified.
- Scribus 1.6.1 suitability (vertical CJK, scripting) was not assessed.
- No CPU benchmarks were run for any ML component.
- Inkscape 1.2.2 (apt) vs current upstream vertical-text behaviour was not compared.
