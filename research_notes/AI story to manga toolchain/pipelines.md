# End-to-end "story to manga/comic" generation pipelines (open-source, research, commercial), as of 2026-10-27

Method note (applies to every repo metric below): all GitHub numbers were collected on **2026-10-27**. Star counts, license, open-issue counts and latest release come from the shields.io JSON badge API (`https://img.shields.io/github/{stars|license|issues-raw|v/release}/{owner}/{repo}.json`). Shields rounds stars above 1,000 (for example "1.4k"). "Last commit" is `git log -1` on a shallow clone of `https://github.com/{owner}/{repo}` (default branch), taken the same day. README facts come from that clone's README file. The GitHub REST/search API was not available in this session (it is repo-scoped), so repo discovery used GitHub topic pages fetched on 2026-10-27, plus repo names from the brief and from papers. "License: none" means the repo has no license GitHub can detect. For research repos that leaves reuse rights unclear.

---

## Q1. Which open-source story-to-comic/manga pipelines exist, and are they maintained?

### Takeaway
There are two tiers. The well-known research repos (StoryDiffusion, DiffSensei, SEED-Story, StoryGen, AutoStudio, ConsiStory, StoryMaker) are effectively frozen. Their last commits date from 2024 to early 2025, they have large open-issue backlogs, and all of them need a local NVIDIA GPU (roughly 16 to 37 GB VRAM). The flagship open-source end-to-end app, jbilcke-hf/ai-comic-factory, was **archived on 2025-10-31**. Its Hugging Face Space still runs. Almost all active development in 2026 is in small (under 150 stars) "agentic" pipelines. They use an LLM (Codex, Claude, Gemini, DeepSeek, Qwen) for script and panel planning, call hosted image APIs (Nano Banana / Gemini image, GPT Image, FLUX via Together or SiliconFlow, DashScope), and then add lettering, layout and PDF/CBZ export locally. They are young, have few stars, and are often single-maintainer.

### Cited Findings

#### A. Topic-page discovery (fetched 2026-10-27)
- The GitHub topic `comic-generation` has 13 public repos. The top ones by stars: stockedge/manga-generator (119★), wanshuiyin/ARIS-Movie-Director (74★), lhfer/codex-novel-to-comic-studio (25★), Yutarop/comic-generator (16★), XBastille/AIComicX (13★), rolfie-han/hanxiaoyu-visual-story-comic (13★) — [GitHub topic comic-generation](https://github.com/topics/comic-generation)
- The topic `comic-generator` has 22 public repos, including RemiPelloux/agent-mangaka-forge, RobinaMirbahar/Comic-Studio-Ai, phaethix/inkstone, CallmeTruong/Comic_Studio, BotTony329/mangaharness, kdjfs/plot2panel, GL-Wen/huiman-ark, williamjxj/LianHuanAI and Saeyeon-developer/agent-comic-kit — [GitHub topic comic-generator](https://github.com/topics/comic-generator)
- The topic `manga-generator` has 6 repos. The top one is Agions/kineo at 133★ — [GitHub topic manga-generator](https://github.com/topics/manga-generator)
- The topic `manga-generation` has only 3 repos: FURUYAN1234/nano-banana-pro, koesan/Manga-Panel-LayoutGAN and StaryMoon/DiffSensei-Unofficial — [GitHub topic manga-generation](https://github.com/topics/manga-generation)
- The topic `story-visualization` has 8 repos, mostly old (for example CPCStoryVisualization-Pytorch, last updated 2021) — [GitHub topic story-visualization](https://github.com/topics/story-visualization)
- Hugging Face Spaces search for "comic", sorted by likes: jbilcke-hf/ai-comic-factory ♥11,310 is far ahead of the next ones, makem/ai-comic-factory ♥147 and Mistral-AI-Game-Jam/ai-interactive-comic-book ♥85. One Space is named `jbilcke-hf/image-server_USED-BY-COMIC-FACTORY_NOW-DECOMISSIONED`. Searching "manga" mostly returns translation and OCR Spaces; the top generator, Minecraft3193092/ai-manga-factory, has ♥12 — [HF Spaces API (comic)](https://huggingface.co/api/spaces?search=comic&sort=likes&direction=-1&limit=25); [HF Spaces API (manga)](https://huggingface.co/api/spaces?search=manga&sort=likes&direction=-1&limit=20)

#### B. Research / model repos (all need a local GPU; data as of 2026-10-27)

| Repo | What it does | Base models | VRAM (from README) | License | Last commit | ★ / open issues | Source |
|---|---|---|---|---|---|---|---|
| HVision-NKU/StoryDiffusion | "Consistent self-attention" for character-consistent image sequences; ships `Comic_Generation.ipynb` and a Gradio comic demo | Plug-in for any SD1.5/SDXL model | Low-VRAM version tested on a 24 GB A10 with 30 GB RAM; "expected to work well with >20 G" | Apache-2.0 | 2024-09-26 | 6.5k / 117 | [repo](https://github.com/HVision-NKU/StoryDiffusion) |
| jianzongwu/DiffSensei (CVPR 2025) | Customized **manga** generation: an MLLM adapts character features to panel captions, with layout control and the MangaZero dataset | SDXL + IP-Adapter; MLLM stage trained from SEED-X-17B | Version without the MLLM "can be run on a single 24GB 4090" | No LICENSE file in repo (HF model card says MIT) | 2025-02-05 | 928 / 27 | [repo](https://github.com/jianzongwu/DiffSensei), [HF model](https://huggingface.co/api/models/jianzongwu/DiffSensei) |
| ali-vilab/MangaNinjia ("MangaNinja") | **Reference-guided line-art colorization**; not story-to-manga | SD1.5 + CLIP ViT-L + ControlNet lineart | A community Windows port says 6 GB VRAM | README badge says CC BY-NC 4.0; HF model card says apache-2.0 (**conflict**) | 2025-03-02 | 750 / 19 | [repo](https://github.com/ali-vilab/MangaNinjia), [HF model](https://huggingface.co/api/models/Johanan0528/MangaNinjia) |
| UCSC-VLAA/story-adapter | Training-free iterative story visualization; has a `--style comic` option | SDXL (RealVisXL_V4.0) + IP-Adapter; optional ControlNet/OpenPose | Not stated | MIT | 2026-04-03 | 959 / 0 | [repo](https://github.com/UCSC-VLAA/story-adapter) |
| haoningwu3639/StoryGen ("Intelligent Grimm") | Open-ended story visualization with the StorySalon dataset | SD1.5 | Not stated (multi-GPU training) | MIT | 2024-12-02 | 269 / 7 | [repo](https://github.com/haoningwu3639/StoryGen) |
| donahowe/AutoStudio | Multi-turn interactive image generation (LLM agents + layout) | SD1.5 and SDXL versions; Grounding-DINO + EfficientSAM | Not stated | none | 2025-04-13 | 452 / 9 | [repo](https://github.com/donahowe/AutoStudio) |
| TencentARC/SEED-Story | MLLM that generates multimodal long stories (text + consistent images) | SEED-X MLLM; needs SDXL base, Llama-2-7b-hf and Qwen-VL-Chat | "NVIDIA GPU + CUDA" | Apache-2.0 except third-party components | 2024-10-11 | 884 / 5 | [repo](https://github.com/TencentARC/SEED-Story) |
| NVlabs/consistory | Training-free consistent subject generation | SDXL ("Add FLUX support" is still an open TODO) | Has a `--cache_cpu_offloading` flag | NVIDIA custom (not identifiable by GitHub) | 2024-11-04 | 427 / 10 | [repo](https://github.com/NVlabs/consistory) |
| RedAIGC/StoryMaker | Consistent multi-character (face + clothing) generation | SDXL + InsightFace | Not stated | none in repo; HF model says apache-2.0 | 2024-12-02 | 721 / 19 | [repo](https://github.com/RedAIGC/StoryMaker), [HF model](https://huggingface.co/api/models/RED-AIGC/StoryMaker) |
| byliutao/1Prompt1Story | Single-prompt consistent story images | Diffusers (pins transformers 4.46.3, gradio 4.44.1) | Not stated | MIT | 2025-10-20 | 322 / 14 | [repo](https://github.com/byliutao/1Prompt1Story) |
| daviddinkevich/Story2Board | Training-free storyboard generation from natural language | FLUX.1-dev | Not stated | MIT | 2025-08-22 | 287 / 9 | [repo](https://github.com/daviddinkevich/Story2Board) |
| Murray-Wang/CharaConsist | Consistent characters on DiT | FLUX.1-dev | 37 GB on 1 GPU; 26 GB with model CPU offload; 3 GB with sequential CPU offload | none | 2025-07-22 | 166 / 11 | [repo](https://github.com/Murray-Wang/CharaConsist) |
| bytedance/UNO | Subject-driven (multi-reference) generation; bundled in ComfyUI story nodes | FLUX.1-dev | fp8 peak about 16 GB; 40 s to 1 min per image on an RTX 3090 | Apache-2.0 (code) | 2025-09-12 | 1.4k / 27 | [repo](https://github.com/bytedance/UNO) |
| Tencent/InstantCharacter | Character customization | FLUX-based (offload demo) | Offload inference "under 22GB VRAM" | Custom license | 2025-05-14 | 1k / 32 | [repo](https://github.com/Tencent/InstantCharacter) |
| smthemex/ComfyUI_StoryDiffusion | ComfyUI node pack bundling StoryDiffusion, UNO, DreamO, InstantCharacter, OmniConsistency, PuLID, StoryMaker, ConsiStory, Bagel, Qwen-Image(-Edit) GGUF | Several (SDXL, FLUX, Qwen-Image) | Says to use fp8 / GGUF Q4 when VRAM is under 24 GB | Apache-2.0 | 2025-10-11 | 518 / 75 (release v1) | [repo](https://github.com/smthemex/ComfyUI_StoryDiffusion) |
| AILab-CVC/TaleCrafter | Story visualization | n/a | n/a | none | 2024-03-22 | 268 / 4 — **repo contains only README/assets/docs, no code** | [repo](https://github.com/AILab-CVC/TaleCrafter) |
| aim-uofa/MovieDreamer | Long-story visual generation | n/a | n/a | none | 2024-08-10 | 326 / 5 — **repo contains only README + assets, no code** | [repo](https://github.com/aim-uofa/MovieDreamer) |
| Aria-Zhangjl/StoryWeaver | Story visualization, with the TBC_Bench benchmark | (code folder present) | n/a | none | 2026-07-18 | 228 / 3 | [repo](https://github.com/Aria-Zhangjl/StoryWeaver) |
| qinghew/CharacterFactory | Generates consistent new characters | Diffusion (details not checked) | n/a | Apache-2.0 | 2026-02-09 | 222 / 3 | [repo](https://github.com/qinghew/CharacterFactory) |
| donahowe/Theatergen | Multi-turn consistent generation | SD + IP-Adapter | n/a | none | 2024-09-26 | 70 / 6 | [repo](https://github.com/donahowe/Theatergen) |
| JoHnneyWang/OneActor | Consistent subject generation | Diffusers | n/a | none | 2024-12-23 | 17 / 4 | [repo](https://github.com/JoHnneyWang/OneActor) |
| StaryMoon/DiffSensei-Unofficial | Unofficial PyTorch reproduction of DiffSensei | torch ≥2.1 | n/a | MIT | 2026-07-02 | 0 / 2 (v0.2.0); README lists "Public checkpoints" as still to do | [repo](https://github.com/StaryMoon/DiffSensei-Unofficial) |
| koesan/Manga-Panel-LayoutGAN | **Layout component only**: LayoutGAN++ predicts manga panel positions on a page | LayoutGAN++ | Not stated | MIT | 2025-10-14 | 4 / 0 | [repo](https://github.com/koesan/Manga-Panel-LayoutGAN) |

#### C. End-to-end apps and agentic pipelines (orchestration plus hosted model APIs; data as of 2026-10-27)

| Repo | Input → output | LLM / image models (per README) | Local GPU? | Stack / runtime | License | Last commit | ★ / issues / release | Source |
|---|---|---|---|---|---|---|---|---|
| jbilcke-hf/ai-comic-factory | Prompt → multi-panel comic page (layouts, captions) | LLM_ENGINE options: HF Inference API/Endpoint (default `HuggingFaceH4/zephyr-7b-beta`), OpenAI (`gpt-4-turbo`), Groq (`mixtral-8x7b-32768`), Anthropic (`claude-3-opus-20240229`). RENDERING_ENGINE options: HF Inference API/Endpoint (SDXL base 1.0 + refiner), Replicate (`stabilityai/sdxl`), VideoChain, OpenAI | No (all remote) | Next.js 14.2.7; `.nvmrc` = v24.6.0; Dockerfile; scripts dev/build/start | Apache-2.0 | 2025-10-30; **archived 2025-10-31 (read-only)** | 1.4k★, 322 forks, 7 open issues, 2 open PRs | [GitHub page](https://github.com/jbilcke-hf/ai-comic-factory), [README](https://github.com/jbilcke-hf/ai-comic-factory) |
| HF Space jbilcke-hf/ai-comic-factory | Same app, hosted | Same | Space hardware = `cpu-basic` (inference is remote) | Docker SDK | — | lastModified 2025-10-30; stage RUNNING on 2026-10-27 | ♥11,310 | [HF API](https://huggingface.co/api/spaces/jbilcke-hf/ai-comic-factory) |
| stockedge/manga-generator | Novel/source text → script → storyboards → artwork → lettering (bubbles placed separately from art) → reviewed pages → PDF | Codex path: Codex's built-in image generation, visual inspection and subagents. Claude Code path: Claude orchestrates and reviews, **external ComfyUI + Qwen-Image-Edit-2511 FP8** generates images | Codex path: no. ComfyUI path: yes (earlier prototypes "used 48GB VRAM", about 100 GB disk, RunPod suggested) | **Node.js 24**, Chrome/Edge, Japanese fonts, Python with reportlab/pypdf/Pillow, Poppler; `npm ci` | MIT | 2026-10-26 | 119★ / 1 / v0.1.0 | [repo](https://github.com/stockedge/manga-generator), [README.en](https://github.com/stockedge/manga-generator/blob/main/README.en.md), [docs/CLAUDE-CODE.md](https://github.com/stockedge/manga-generator/blob/main/docs/CLAUDE-CODE.md), [docs/COMFYUI.md](https://github.com/stockedge/manga-generator/blob/main/docs/COMFYUI.md) |
| Agions/kineo | Script → AI manga and animated short dramas (multi-agent desktop app) | README claims 13 providers, for example DeepSeek-V4/R1, "Qwen 3.8-Max", "OpenAI GPT-5.6 Sol", "Doubao Seedream 5.0" (model names **unverified**) | No (APIs); uses VideoToolbox/NVENC for video encoding | Tauri + Rust + pnpm (`pnpm install`, `pnpm tauri dev`); keys stored in the system Keyring | MIT | 2026-10-27 | 133★ / 0 / v0.0.2 | [repo](https://github.com/Agions/kineo) |
| wanshuiyin/ARIS-Movie-Director | Loose story → image-based "movie"/comic (`comic.json`) with cross-model auditing | Codex image generation (GPT-5.5) plus a Google-family reviewer (the Gemini CLI is deprecated; ships a shim to Antigravity `agy`) | No | `pip install -r requirements.txt`; codex CLI; headless Chrome | MIT | 2026-10-17 | 74★ / 0 | [repo](https://github.com/wanshuiyin/ARIS-Movie-Director) |
| lhfer/codex-novel-to-comic-studio | EPUB/TXT novel → manga, exported to PDF and CBZ (Codex skill) | Codex | No | Codex skill | MIT | 2026-05-19 | 25★ / 0 | [repo](https://github.com/lhfer/codex-novel-to-comic-studio), [topic page](https://github.com/topics/comic-generation) |
| FURUYAN1234/nano-banana-pro ("Super FURU AI 4-koma System") | Topic + character references → 4-koma (Gemini) or 4- to 8-panel (OpenAI) manga page, with AI quality review | Gemini (4-koma only) and OpenAI (the README's example uses "GPT Image 2.5") | No (browser app; demo on GitHub Pages) | Web app | Custom "source available, free to use" license | 2026-10-27 | 19★ / 0 / v7.2.0 | [repo](https://github.com/FURUYAN1234/nano-banana-pro) |
| Yutarop/comic-generator | One-line idea → full manga (4 pages) | `gemini-3-pro-preview` (plot, 1 call) + `gemini-3-pro-image-preview` (1 call per page) | No | Python ≥3.12, `uv sync`, `google-genai>=1.52.0` | MIT | 2025-11-28 | 16★ / 0 | [repo](https://github.com/Yutarop/comic-generator) |
| RobinaMirbahar/Comic-Studio-Ai | Story or uploaded character → multi-agent comic (built for the "Gemini Live Agent Challenge") | Gemini; `nano-banana-pro-preview`, `gemini-3.1-flash-image-preview` | No | FastAPI, Dockerfile, Cloud Run | Apache-2.0 | 2026-10-27 | 16★ / 0 | [repo](https://github.com/RobinaMirbahar/Comic-Studio-Ai) |
| RemiPelloux/agent-mangaka-forge | Agent skill pack for manga pages with persistent character image memory | Agent-provided | No | Skills + `requirements.txt` | MIT | 2026-04-29 | 16★ / 0 | [repo](https://github.com/RemiPelloux/agent-mangaka-forge) |
| rolfie-han/hanxiaoyu-visual-story-comic | Agent Skills package for consistent multi-page comics (Claude Code, Gemini CLI, etc.) | Agent-provided | No | Skill | MIT | 2026-08-26 | 13★ / 0 / v1.1.1 | [repo](https://github.com/rolfie-han/hanxiaoyu-visual-story-comic) |
| phaethix/inkstone | Local `.txt` novel → comic pages (PDF/CBZ/PNG), with a cross-panel character ledger and resumable state | Agnes API: `agnes-3.0-flash` (scripting), `agnes-image-2.5-flash` (t2i/i2i). Or `PROVIDER=openai_compat` (any OpenAI-style `/images/generations` gateway) | **No: "No GPU, no paid plan: just one free API key"** | Python ≥3.10, uv; offline pytest suite; optional web UI | MIT | 2026-10-23 | 12★ / 0 | [repo](https://github.com/phaethix/inkstone) |
| CallmeTruong/Comic_Studio | Story → LangGraph agent → panels → manga-style layout + editable speech bubbles | OpenAI-compatible chat/vision endpoint (planning, QA) + **local SD 1.5** checkpoint (default `comicBabes_v2.safetensors`) + optional LoRA | **Yes**: "CPU mode is only practical for small tests" | Python + npm frontend | none | 2026-09-14 | 9★ / 0 | [repo](https://github.com/CallmeTruong/Comic_Studio) |
| wenn-id/comicsol ("Comic Sol") | Prompt/story → editable comic project → panel plan → (external) art → QA → lettering → page composition → PDF | **Not an image generator.** Uses the active agent's image tool, an external adapter/API, local ComfyUI, or a hand-off to another agent | No | Python ≥3.11, Pillow 13.0.0; CLI, MCP, Codex plugin, Agent Skills | MIT | 2026-10-23 | 7★ / **25 open issues** | [repo](https://github.com/wenn-id/comicsol) |
| BotTony329/mangaharness ("Kumanga") | Local-first AI manga editor: reusable characters, panels, natural-language agent | Image: Google Gemini (reference-image aware) or any OpenAI-compatible REST endpoint. Agent: OpenAI-, Anthropic- or Gemini-compatible | No | Next.js 15, Node ≥18.18 | MIT (per README) | 2026-10-02 | 4★ / 0 / v0.1.1 | [repo](https://github.com/BotTony329/mangaharness) |
| eust-w/ltseries | Self-hosted studio: script → assets → storyboards → video series | Alibaba Cloud Model Studio / DashScope (Qwen LLM by default; image and video) | No (bundles no weights) | Go 1.24+, Node 22.12+, **Docker (MongoDB)**, FFmpeg; `docker compose up -d --build` | MIT | 2026-10-25 | 4★ / 0 | [repo](https://github.com/eust-w/ltseries) |
| williamjxj/LianHuanAI | Story → Chinese lianhuanhua-style comics | LLM: DeepSeek/Kimi/MiniMax. Image backends: comfyui (default, local) / runninghub / zhipu / tongyi / minimax / replicate / dry_run | Default ComfyUI backend needs a local GPU; the cloud backends do not | Python | none | 2026-08-26 | 4★ / 0 | [repo](https://github.com/williamjxj/LianHuanAI) |
| kdjfs/plot2panel | One premise → validated **four-panel** comic (fixed 4 panels) | Planner: DeepSeek (`deepseek-v4-pro` default). Images: SiliconFlow (default), Together (`FLUX.1-schnell`), Pollinations (no key), or mock | No | Next.js; Node ≥20.9; pnpm 10 | MIT | 2026-08-18 | 2★ / 0 / v0.1.0 | [repo](https://github.com/kdjfs/plot2panel) |
| Saeyeon-developer/agent-comic-kit | Claude Code/Codex skill + CLI: character consistency, storyboards, SNS formats | GPT Image (Gemini/NovelAI backends are planned) | No | `git clone … ~/.claude/skills/agent-comic-kit`; `pip install pillow pyyaml`; Python ≥3.11 | Apache-2.0 | 2026-10-05 | 2★ / 0 | [repo](https://github.com/Saeyeon-developer/agent-comic-kit) |
| GL-Wen/huiman-ark | Frontend-only AI comic studio: story → storyboards, character sheets, images | Defaults: gateway `https://api.antmoo.cc`, text `claude-opus-5-5`, image `gpt-image-2`; all overridable | No | **Node ≥22.18.0**; `pnpm install --frozen-lockfile` | MIT | 2026-10-25 | 1★ / 0 | [repo](https://github.com/GL-Wen/huiman-ark) |
| backblaze-b2-samples/comic-storyboard-b2 | Sample app: character-consistent comics with frames stored in Backblaze B2 plus a provenance manifest | n/a | No | TS sample | none | 2026-09-02 | 1★ / 2 | [repo](https://github.com/backblaze-b2-samples/comic-storyboard-b2), [topic page](https://github.com/topics/comic-generator) |
| XBastille/AIComicX | Story → comics | n/a | n/a | n/a | not identifiable by GitHub | 2025-12-07 | 13★; README says **"PROJECT ARCHIVED (UNFINISHED)"** | [repo](https://github.com/XBastille/AIComicX) |

### Inferences
- No maintained open-source project combines research-grade consistency (DiffSensei-style MLLM identity control or StoryDiffusion-style attention sharing) with a working end-to-end story → paginated-manga UX. The research code is frozen and needs a GPU. The maintained apps rely on proprietary image APIs (Nano Banana, GPT Image) for consistency.
- The 2026 trend is "agent skill" packaging (Codex/Claude Code/Gemini CLI skills such as stockedge, comicsol, agent-comic-kit, hanxiaoyu, agent-mangaka-forge, codex-novel-to-comic-studio). The coding agent does script planning and visual QA, and image generation is delegated. These are maintained but have tiny user bases (≤119★). Expect rough edges.
- Several projects deliberately do lettering and speech bubbles outside the image model (stockedge, inkstone, comicsol, Comic_Studio). That reflects a known weakness: image models render dialogue text poorly. This matches MangaFlow's finding on a FLUX.2 baseline (see Q2).

### Gaps
- GitHub search API was unavailable, so repos without topic tags may be missed. In particular, Chinese-language and less-tagged repos may be under-covered.
- I did not verify VRAM for Story-Adapter, StoryGen, AutoStudio, 1Prompt1Story, Story2Board, StoryMaker or ConsiStory; their READMEs give no numbers.
- Model names quoted from 2026 READMEs (for example "GPT-5.6 Sol", "Qwen 3.8-Max", "gpt-image-2", "GPT Image 2.5", "deepseek-v4-pro", "agnes-image-2.5-flash") were not checked against provider docs. Only the Gemini image model IDs were cross-checked (see Q3).
- I did not verify the Agnes API (agnes-ai.com) free-tier terms. The homepage returned only its title ("Free Omni-Modal AI API…").

---

## Q2. Which academic papers (2024–2026) target manga/comic generation specifically, and which released usable code/weights?

### Takeaway
Only a handful of papers target **manga/comic pages** specifically, meaning panel layout plus character consistency plus dialogue. **DiffSensei (CVPR 2025)** is the only one with released inference code, weights and dataset annotations. MangaDiffusion (Dec 2024), TaleDiffusion (Sep 2025) and MangaFlow (EMNLP 2026; an agentic story→manga framework with layout, references and lettering) list **no code link** on their arXiv pages. The broader "story visualization" literature (StoryDiffusion, StoryGen, SEED-Story, Story-Adapter, StoryMaker, UNO, CharaConsist, Story2Board) has released code but produces image sequences, not paginated manga with bubbles. ViStoryBench (CVPR 2026) is the main 2025–2026 benchmark.

### Cited Findings
- **DiffSensei** (arXiv 2412.07589; CVPR 2025) bridges multimodal LLMs and diffusion for customized manga generation and introduces the **MangaZero** dataset — [arXiv](https://arxiv.org/abs/2412.07589); [CVF open access PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_DiffSensei_Bridging_Multi-Modal_LLMs_and_Diffusion_Models_for_Customized_Manga_CVPR_2025_paper.pdf)
  - Release timeline: checkpoint, dataset and inference code 2024-12-10; a Gradio demo without the MLLM (lower memory) 2024-12-13; reference training code 2025-02-05. Because of licensing, the dataset ships as MangaDex URLs plus annotations rather than images — [DiffSensei README](https://github.com/jianzongwu/DiffSensei)
  - HF weights `jianzongwu/DiffSensei`: card license MIT, not gated, lastModified 2024-12-11 — [HF API](https://huggingface.co/api/models/jianzongwu/DiffSensei)
- **MangaDiffusion**, "Manga Generation via Layout-controllable Diffusion" (Chen et al., arXiv 2412.19303, 2024-12-26): generates multi-panel manga from plain text, controls panel count and layout, and builds the Manga109Story dataset. **No code, weights or dataset link** on the abs page — [arXiv](https://arxiv.org/abs/2412.19303)
- **TaleDiffusion** (Banerjee, Lladós, Pal, Dutta; arXiv 2509.04123; v1 2025-09-04, v2 2026-04-11): an LLM produces per-frame descriptions and dialogues; bounded attention handles per-box masks; identity-consistent self-attention keeps characters stable; **speech bubbles are assigned to characters in post-processing using CLIPSeg**. No venue and no code link on the abs page — [arXiv](https://arxiv.org/abs/2509.04123)
- **MangaFlow**, "An End-to-End Agentic Framework for Controllable Story to Manga Generation" (Wang, Xie, Chen, Xiu, Nakayama; arXiv 2605.28173; v1 2026-05-27, v2 2026-09-14; **EMNLP 2026 Main** per the arXiv comments). Its stages are planning → grounding → layout construction → reference-conditioned rendering → composition → text placement. A "story section memory" links sections to characters, scenes and objects, and the paper adds a meta-benchmark. **No code or project URL** on the abs page — [arXiv abs](https://arxiv.org/abs/2605.28173)
  - A search snippet of the paper says the "Direct-FLUX.2" baseline often produces unreadable text, so bubble readability is evaluated separately — [arXiv HTML (via search result)](https://arxiv.org/html/2605.28173) (snippet only; I did not read the full text)
- **ViStoryBench** (arXiv 2505.24862; accepted to CVPR 2026 on 2026/02/21): 80 story segments and 344 characters. Metrics cover character consistency (e.g. CIDS), style (CSD), prompt adherence, aesthetics and copy-paste artifacts. It evaluates image-story methods **uno, seedstory, storygen, storydiffusion, storyadapter, theatergen**; video methods movieagent, animdirector, vlogger, mmstoryagent; closed models gemini and gpt4o; and business tools moki, morphic_studio, bairimeng_ai, shenbimaliang, xunfeihuiying and doubao. arXiv v4 (2025-12-19) added NanoBanana-Pro. Repo has 173★ — [vistorybench GitHub](https://github.com/vistorybench/vistorybench); [arXiv HTML v4](https://arxiv.org/html/2505.24862v4); [CVPR 2026 poster](https://cvpr.thecvf.com/virtual/2026/poster/39308)
  - The CVPR 2026 supplementary notes that a simple copy-paste baseline scores best on several metrics, so the authors argue metrics must be read together — [CVPR 2026 supplemental (search snippet)](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Zhuang_ViStoryBench_Comprehensive_Benchmark_CVPR_2026_supplemental.pdf)
- **StoryDiffusion** (arXiv 2405.01434): code released (Apache-2.0); weights are any SD1.5/SDXL model — [repo](https://github.com/HVision-NKU/StoryDiffusion)
- **SEED-Story**: weights `TencentARC/SEED-Story` on HF (license "other", lastModified 2024-08-26) — [HF API](https://huggingface.co/api/models/TencentARC/SEED-Story); [repo](https://github.com/TencentARC/SEED-Story)
- **StoryGen**: weights `haoningwu/StoryGen` (MIT, lastModified 2025-06-26) — [HF API](https://huggingface.co/api/models/haoningwu/StoryGen)
- **StoryMaker**: weights `RED-AIGC/StoryMaker` (apache-2.0, lastModified 2024-11-09); technical report arXiv 2409.12576 — [HF API](https://huggingface.co/api/models/RED-AIGC/StoryMaker); [repo README](https://github.com/RedAIGC/StoryMaker)
- **MangaNinja** (colorization, not generation from story): weights `Johanan0528/MangaNinjia` (card: apache-2.0, but the README badge says CC BY-NC 4.0). The HF demo Space `fffiloni/MangaNinja-demo` was in **RUNTIME_ERROR** on 2026-10-27 — [HF model API](https://huggingface.co/api/models/Johanan0528/MangaNinjia); [HF Space API](https://huggingface.co/api/spaces/fffiloni/MangaNinja-demo); [repo](https://github.com/ali-vilab/MangaNinjia)
- **Announced but no code in repo:** TaleCrafter (AILab-CVC) and MovieDreamer (aim-uofa) contain only README and assets — [TaleCrafter](https://github.com/AILab-CVC/TaleCrafter); [MovieDreamer](https://github.com/aim-uofa/MovieDreamer)

### Inferences
- For a usable research-grade manga generator with released weights, DiffSensei is effectively the only option. It needs a 24 GB-class GPU even without the MLLM, and has unresolved install issues (Q5).
- MangaFlow's decomposition (plan → layout → reference-conditioned render → compose → letter) is the same architecture the 2026 open-source agentic tools use with commercial image APIs. It is a reasonable design template even without its code.

### Gaps
- I did not open the PDF/HTML full texts of MangaDiffusion, TaleDiffusion or MangaFlow. A code link might appear inside the paper; the abs pages show none.
- I did not identify which LLM or image models MangaFlow uses; the abs page doesn't say.
- I did not systematically search SIGGRAPH/ICCV/ECCV/NeurIPS 2025–2026 proceedings for comic layout or speech-balloon placement papers. A search for "comic generation multimodal LLM 2026 code" returned nothing relevant.
- I did not verify venues for Story2Board, CharaConsist, 1Prompt1Story, StoryWeaver, MangaNinja or UNO.

---

## Q3. Which commercial/hosted products do story-to-manga? Pricing, API, quality, terms

### Takeaway
LlamaGen.ai and Anifusion are the most clearly positioned story/script → comic/manga products with published pricing and an API. LlamaGen has a "Comic API"; Anifusion has a REST API plus hosted MCP on paid plans. Komiko offers idea → comic with credit ("Zap") pricing and no API mentioned. Dashtoon is now mainly a reader plus creator platform inside the Dashverse group. Several sites could not be read (ComicsMaker.ai, Lore Machine, aicomicfactory.app), so their pricing is unverified. The DIY route used by most 2026 open-source pipelines is a direct Gemini or OpenAI image API. Gemini image models have **no free API tier** and cost about $0.034 to $0.134 per 1K image (official pricing, updated 2026-10-27).

### Cited Findings
- **LlamaGen.ai** (pricing page fetched 2026-10-27): "The AI Comic Agent & Intelligent Canvas"
  - Plans: Free (1 custom character, 4 panels per page); Standard $18/mo (15,000 credits, up to 20 panels per prompt); Pro $30/mo (45,000 credits, 40 panels); Unlimited $96/mo (135,000 credits, 64 panels); Production Unlimited $200/mo (270,000 credits). Introductory prices are $14/$24/$58/$120. Credit-pack figures on the page are internally inconsistent.
  - A "Comic API" exists (docs link; details not shown). The guessed URL `llamagen.ai/api` returned 404.
  - Commercial terms: "If you have subscribed at any point, you are free to use your images in just about any way you want"; companies with more than US$500k gross annual revenue must buy Pro or Unlimited.
  - Models named: OpenAI, Claude, Gemini, Grok, Nano Banana, FLUX-pro, gpt-image-1, CyaniModel; GPT-4o for free-tier story generation.
  - Source: [LlamaGen pricing](https://llamagen.ai/pricing)
  - LlamaGen's own "best AI manga generators 2026" article recommends LlamaGen, "Jenova Manga Creator", ComicsAI, OpenArt, SD+ComfyUI and Canva/Clip Studio. This is **vendor content, not an independent review** — [LlamaGen article](https://llamagen.ai/de/articles/best-ai-manga-generators-2026)
- **Anifusion** (pricing page fetched 2026-10-27): "Turn stories into manga pages with layouts, characters, speech bubbles, and editing tools", with a "Script to beats" tool, panel grid planner and LoRA training.
  - Plans: Free $0 (100 credits); Creator $9/mo (2,000 credits); Pro $24/mo (10,000 credits). Credit packs run $15 (2,000) to $120 (30,000). An image costs 5 to 100 credits depending on the model.
  - **REST API + hosted MCP on Creator/Pro.** Commercial use is included on Creator/Pro (not listed for Free), "subject to Anifusion's terms".
  - Models: anime SDXL family (AnimagineXL 3.x/4.0, SDXL, WAI Illustrious, NoobAI XL, Pony Diffusion V6 XL, etc.).
  - Source: [Anifusion pricing](https://anifusion.ai/pricing)
- **Komiko (KomikoAI)** (pricing page fetched 2026-10-27): AI Comic Generator ("Enter an idea and generate a comic in seconds"), Comics Canvas and OC Maker.
  - Plans: Free (500-Zap signup bonus + 80 daily); Starter $9.99/mo (5,000 Zaps); Plus $19.99/mo (15,000); Premium $49.99/mo (50,000); Enterprise custom.
  - No API mentioned. Commercial terms not on the pricing page.
  - Models listed include Gemini, NoobAI XL, GPT-4o, Nano Banana 2, Qwen Image Edit and Midjourney, plus many video models.
  - Source: [Komiko pricing](https://komiko.app/pricing)
- **Dashtoon**: the homepage reads "Read and create your own comics, manga and manhwa online", with a Studio section. The `/studio/plans` page rendered only the title "Frameo Pro - Canvas", so studio pricing is unverified — [Dashtoon](https://dashtoon.com/); [Dashtoon studio plans](https://dashtoon.com/studio/plans)
  - Search summaries say Dashtoon raised a US$13M Series A led by Peak XV in Aug 2025, and that parent Dashverse also runs DashReels and Frameo.AI. These are secondary summaries — [Preqin profile](https://www.preqin.com/data/profile/asset/dashtoon/570983); [Dealroom](https://app.dealroom.co/companies/dashverse)
- **Lore Machine**: MIT Technology Review (2024-03-05) describes it as bundling several generative models into a one-click text-to-comic workflow — [MIT Tech Review](https://www.technologyreview.com/2024/03/05/1089458/generative-ai-turn-my-story-into-comic-images-lore-machine/). The official site rendered only its title, so its current (2026) status and pricing are unverified — [loremachine.world](https://www.loremachine.world/). 2026 feature claims come only from aggregator listings (e.g. [stork.ai](https://www.stork.ai/en/lore-machine)) and are unverified.
- **ComicsMaker.ai**: the pricing page rendered only its title ("Generate Comics with AI | AI Comic Strip Maker"), so all details are unverified — [ComicsMaker pricing](https://www.comicsmaker.ai/pricing)
- **AI Comic Factory hosted site**: the README names `aicomicfactory.app` as the official website — [README](https://github.com/jbilcke-hf/ai-comic-factory). The domain did not resolve from this session (DNS ENOTFOUND), so its status is unverified. The free HF Space is RUNNING — [HF API](https://huggingface.co/api/spaces/jbilcke-hf/ai-comic-factory)
- **Gemini API image models** (official pricing, "Last updated 2026-10-27 UTC"; paid tier; **free tier "Not available" for all image models**):
  - `gemini-3-pro-image` (Nano Banana Pro): $0.134 per 1K/2K image, $0.24 per 4K.
  - `gemini-3.1-flash-image` (Nano Banana 2): $0.067 per 1K.
  - `gemini-3.1-flash-lite-image`: $0.0336 per 1K.
  - `gemini-nano-banana-2.1`: $0.0336 per 1K.
  - Batch API pricing is about half.
  - `gemini-2.5-flash-image` is **deprecated, with shutdown on 2026-10-02**.
  - Source: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- **Nano Banana Pro for comics** (vendor/tutorial sources; treat as marketing): ComfyUI docs describe enhanced text rendering and character consistency. Tutorials report about 4 panels per generated strip and blending of up to 5 reference faces. Lettering and page assembly are usually done in a separate editor — [ComfyUI docs](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-pro/workflow); [Anifusion blog](https://anifusion.ai/blog/mastering-nano-banana-pro-comic-manga-generation/); [nerdschalk](https://nerdschalk.com/how-to-make-professional-comics-with-gemini-nano-banana-pro/)
- **StoryDiffusion on Replicate** (`hvision-nku/storydiffusion`): Nvidia L40S, about $0.064 per run (about 15 runs per $1), typically about 66 s. Needs at least 3 prompts (5 to 6 recommended) — [Replicate](https://replicate.com/hvision-nku/storydiffusion); packaged by [camenduru/StoryDiffusion-replicate](https://github.com/camenduru/StoryDiffusion-replicate) (23★)

### Inferences
- For API-driven automation, LlamaGen (Comic API) and Anifusion (REST + MCP) are the only commercial products whose own pricing pages confirm an API. Neither page documented endpoints, so integration effort is unknown.
- Per-page costs for a DIY Gemini pipeline: one Nano Banana Pro call per page (as in Yutarop/comic-generator) costs about $0.134 per page at 1K/2K, before LLM costs. This is an inference from the official price list plus that repo's call counts.

### Gaps
- OpenAI image pricing (gpt-image-1/2) could not be fetched (HTTP 403), so it is unverified.
- I did not check Neural Frames. My understanding is that it is an AI music-video/animation tool rather than a comic generator, but that is unverified.
- I did not fetch Midjourney or ChatGPT terms. Ownership and commercial-use terms for LlamaGen, Anifusion and Komiko were read only from their pricing pages, not the full ToS.
- I found no independent, non-vendor user reviews of output quality for any commercial product in this pass; quality claims are vendor-sourced.
- Jenova Manga Creator appeared only in a vendor article and is unverified.

---

## Q4. For each open-source option: local GPU or hosted APIs? Exact install steps from README

### Takeaway
Every research repo needs a local CUDA GPU, usually 16 to 37 GB. The only no-GPU ways to use them are hosted copies: StoryDiffusion on Replicate (about $0.064 per run) or its HF ZeroGPU Space. Most 2026 apps are API-only: ai-comic-factory, inkstone, plot2panel, Kumanga/mangaharness, Yutarop/comic-generator, Comic-Studio-Ai, huiman-ark, and the agent-skill packs. Their install steps are short (`uv sync`, `pnpm install`, `npm install`).

### Cited Findings

**Research repos (GPU required). Install steps as written in the READMEs:**
- StoryDiffusion: `conda create --name storydiffusion python=3.10` → `pip install -U pip` → `pip install -r requirements.txt` → `python gradio_app_sdxl_specific_id_low_vram.py`. Tested on a 24 GB A10 with 30 GB RAM; ">20 G" expected — [README](https://github.com/HVision-NKU/StoryDiffusion)
  - Hosted alternatives: HF Space `YupengZhou/StoryDiffusion` (RUNNING on `zero-a10g`, ♥620, lastModified 2025-08-28) — [HF API](https://huggingface.co/api/spaces/YupengZhou/StoryDiffusion); Replicate — [Replicate](https://replicate.com/hvision-nku/storydiffusion)
- DiffSensei: `conda create -n diffsensei python=3.11` → `pip install -r requirements.txt` → `pip install gradio-image-prompter` → download the HF checkpoint into `checkpoints/` → run `scripts.demo.gradio_wo_mllm` (24 GB 4090) or the full Gradio demo with the MLLM — [README](https://github.com/jianzongwu/DiffSensei)
- MangaNinja: `git clone https://github.com/ali-vilab/MangaNinjia.git`, install, download SD1.5, clip-vit-large-patch14, control_v11p_sd15_lineart and the MangaNinjia weights, set paths in `configs/inference.yaml`. A Windows port with a 6 GB VRAM auto-installer exists (sdbds) — [README](https://github.com/ali-vilab/MangaNinjia)
- Story-Adapter: `conda create -n StoryAdapter python=3.10` → `pip install -r requirements.txt` → download the IP-Adapter SDXL image encoder and `ip-adapter_sdxl.bin` → `python run.py --base_model_path …/RealVisXL_V4.0 … --style comic` — [README](https://github.com/UCSC-VLAA/story-adapter)
- SEED-Story: NVIDIA GPU + CUDA; `pip install -r requirements.txt`; download SEED-Story-George, Detokenizer-George, SDXL base, Llama-2-7b-hf and Qwen-VL-Chat — [README](https://github.com/TencentARC/SEED-Story)
- CharaConsist: `conda create --name characonsist python=3.9` → `pip install -r requirements.txt`; FLUX.1-dev; `init_mode` 0/1/2/3 = 37 GB / 26 GB / ≤20 GB across ≥2 GPUs / 3 GB with sequential CPU offload — [README](https://github.com/Murray-Wang/CharaConsist)
- Story2Board: `conda create -n story2board python=3.12` → `pip install -r requirements.txt`; FLUX.1-dev — [README](https://github.com/daviddinkevich/Story2Board)
- 1Prompt1Story: `conda create --name 1p1s python=3.10`; `pip install transformers==4.46.3`; `pip install opencv-python scipy gradio==4.44.1 sympy==1.13.1` — [README](https://github.com/byliutao/1Prompt1Story)
- UNO: FLUX.1-dev + xflux text encoders + CLIP + UNO weights; `--offload --name flux-dev-fp8` gives a peak of about 16 GB — [README](https://github.com/bytedance/UNO)

**API-only / orchestration apps. Install steps as written in the READMEs:**
- ai-comic-factory:
  - No `npm` commands in the README. It says the project "isn't a monolithic Space that can be duplicated and ran immediately" and is configured through `.env` / `.env.local` (LLM_ENGINE, RENDERING_ENGINE and the AUTH_* keys) — [GitHub page](https://github.com/jbilcke-hf/ai-comic-factory)
  - `package.json` scripts are `dev/build/lint/start`; `.nvmrc` = v24.6.0; a Dockerfile exists — [repo](https://github.com/jbilcke-hf/ai-comic-factory)
  - Example Replicate config: `RENDERING_ENGINE="REPLICATE"`, `RENDERING_REPLICATE_API_MODEL="stabilityai/sdxl"`, `AUTH_REPLICATE_API_TOKEN=…`; OpenAI LLM: `LLM_ENGINE="OPENAI"`, `LLM_OPENAI_API_MODEL="gpt-4-turbo"` — [README](https://github.com/jbilcke-hf/ai-comic-factory)
- inkstone (Python 3.10+, uv, Agnes key):
  - Install: `uv sync --extra dev`, set `AGNES_API_KEY`, then `uv run python examples/first_panel.py`; the offline test is `uv run pytest`.
  - Usage: `uv run inkstone plan --book examples/scene1.txt` (offline estimate); `uv run inkstone generate examples/scene1.txt --density B`; `--format cbz`; web UI via `AGNES_API_KEY=sk-xxx uv run python web/server.py`.
  - `PROVIDER=openai_compat` with `OPENAI_COMPAT_*` reroutes to another gateway; `INKSTONE_PAGE_SIZE` defaults to 1024x1536.
  - Source: [README](https://github.com/phaethix/inkstone)
- plot2panel (Node ≥20.9, pnpm 10):
  - Install: `git clone https://github.com/kdjfs/plot2panel.git` → `cd plot2panel` → `pnpm install` → `pnpm dev`.
  - Env: `DEEPSEEK_API_KEY` (required); `IMAGE_PROVIDER=siliconflow|together|pollinations|mock`; `TOGETHER_IMAGE_MODEL` defaults to `black-forest-labs/FLUX.1-schnell`.
  - Source: [README](https://github.com/kdjfs/plot2panel)
- mangaharness/Kumanga (Node ≥18.18): `git clone https://github.com/BotTony329/mangaharness.git` → `cd mangaharness` → `npm install` → `cp .env.example .env.local` (optional) → `npm run dev` (http://localhost:3000). AI keys are entered in the in-app "AI Settings", and "the editor works without any AI key" — [README](https://github.com/BotTony329/mangaharness)
- Yutarop/comic-generator (Python ≥3.12): `uv sync`, then a `.env` with Gemini access to `gemini-3-pro-image-preview` and `gemini-3-pro-preview`. Per comic: 1 plot call plus 4 page-image calls — [README](https://github.com/Yutarop/comic-generator)
- huiman-ark (Node ≥22.18.0): `pnpm install --frozen-lockfile`; env `AI_TEXT_MODEL=claude-opus-5-5`, `AI_IMAGE_MODEL=gpt-image-2`; default base URL `https://api.antmoo.cc` — [README](https://github.com/GL-Wen/huiman-ark)
- agent-comic-kit: `git clone https://github.com/Saeyeon-developer/agent-comic-kit ~/.claude/skills/agent-comic-kit` → `pip install pillow pyyaml` — [README](https://github.com/Saeyeon-developer/agent-comic-kit)
- comicsol: Python 3.11+ with Pillow 13.0.0. `comic-sol skill-install --target codex|claude|antigravity|zcode` requires `v2.0.0rc6`, which the README says "is not yet published" — [README](https://github.com/wenn-id/comicsol)
- stockedge/manga-generator: Node.js 24, Chrome/Edge, Japanese fonts, Poppler; `npm ci`; `python -m pip install reportlab pypdf Pillow` (path set in `MANGA_PYTHON`); run with `node cli/auto.mjs start original.txt --renderer "ComfyUI+Qwen-Image-Edit-2511-FP8"`. The docs state that a Claude subscription alone does **not** include a GPU or external image generation — [docs/CLAUDE-CODE.md](https://github.com/stockedge/manga-generator/blob/main/docs/CLAUDE-CODE.md); [README.en](https://github.com/stockedge/manga-generator/blob/main/README.en.md)
- ltseries: `docker compose up -d --build`, or Go 1.24+ / Node 22.12+ / Docker (MongoDB) / FFmpeg plus a DashScope key — [README](https://github.com/eust-w/ltseries)
- CallmeTruong/Comic_Studio: `python -m pip install -r requirements.txt`; `npm install`; put an SD1.5 checkpoint in `models/base/`; needs an OpenAI-compatible chat/vision endpoint; NVIDIA GPU recommended — [README](https://github.com/CallmeTruong/Comic_Studio)

### Inferences
- In API-only apps, image generation is remote and only planning, lettering and layout run locally. Hardware needs are therefore trivial, and cost and consistency depend on the chosen image API.
- Several apps hard-code preview or older model IDs (`gemini-3-pro-image-preview`, `gpt-4-turbo`, `claude-3-opus-20240229`, `mixtral-8x7b-32768`). Given Google's deprecation of `gemini-2.5-flash-image` (shutdown 2026-10-02 per the [Gemini pricing page](https://ai.google.dev/gemini-api/docs/pricing)), expect some defaults to need updating to current IDs such as `gemini-3-pro-image` or `gemini-3.1-flash-image`. I did not test this.

### Gaps
- I did not test whether `npm install && npm run dev` actually builds ai-comic-factory on Node 22. The README has no explicit commands and `.nvmrc` pins Node 24.6.0.
- I did not verify whether HF ZeroGPU Spaces (StoryDiffusion) can be driven programmatically from a container via `gradio_client`, or what the quota is for a free HF account.

---

## Q5. What do GitHub issues reveal about real-world failure modes?

### Takeaway
The dominant failure modes are: broken installs and missing-weight paths (DiffSensei, StoryDiffusion); dependency and version drift (Gradio, huggingface_hub, pydantic); requests for models the frozen code doesn't support (FLUX/SD3 for StoryDiffusion); character consistency that holds for faces but drifts for clothing or the reference image; external-API rate limits and outages (ai-comic-factory with DALL·E 3 and HF Inference); and outright abandonment (ai-comic-factory archived, AIComicX archived unfinished, MangaNinja HF demo in runtime error, research repos with 100+ open issues and no maintainer replies).

### Cited Findings
- **ai-comic-factory** (12 issues total, 7 open; repo archived):
  - Local and Windows setup failures: #1 "How to run this on windows?" (2023-08-30), #10 "[Help] I am unable to run it successfully" (2023-11-13), #13 (2024-02-21), #20 "Trying to run locally" (2024-10-04).
  - Provider failures: #11 incorrect content type for Inference Endpoints; #16 "Too many requests with Dalle3 as rendering engine"; #21 "Possible Rendering API Issue" (2024-12-02).
  - Requests: #19 "Bubbles"; #12 "Creating more than just 4koma".
  - Source: [issues](https://github.com/jbilcke-hf/ai-comic-factory/issues?q=is%3Aissue)
  - The HF Space list includes a Space named `jbilcke-hf/image-server_USED-BY-COMIC-FACTORY_NOW-DECOMISSIONED` — [HF Spaces API](https://huggingface.co/api/spaces?search=comic&sort=likes&direction=-1&limit=25)
- **StoryDiffusion** (117 open issues; first page covers #149 to #177):
  - Consistency failures: #177 results don't look like the reference (2025-09-08); #157 face stable but clothing not; #161 guiding from a reference image.
  - Dependency errors: #164 `split_torch_state_dict_into_shards` import error from huggingface_hub; #171 PydanticSchemaGenerationError; #156 tensor broadcast error.
  - Model-support requests left unanswered: FLUX/SD3/DiT (#158, #166, #176), SD1.5 (#167), Kolors (#154).
  - Missing training code and dataset (#169) and video model update (#153); multi-character usage confusion (#174); prompt-count errors (#168, "needs at least 2, got 0").
  - Source: [issues](https://github.com/HVision-NKU/StoryDiffusion/issues)
- **DiffSensei** (44 issues total):
  - Missing weight files: #23 and #25 "no file named diffusion_pytorch_model.bin found in …image_generator/unet".
  - #30 FileNotFoundError for MangaZero `train.json`; #27 download error; #28 "Notes for first run".
  - Gradio breakage: #29, #31 "TypeError: argument of type 'bool' is not iterable (Gradio version?)", #32 can't open demo page.
  - #21 "Hardware Requirements?"; #42 "LlamaForCausalLM has no generate()"; #51 "Add LICENSE file to clarify license terms" (2026-05-16).
  - About ten spam or off-topic "story" posts (2025–2026) with no maintainer triage.
  - Source: [issues](https://github.com/jianzongwu/DiffSensei/issues?q=is%3Aissue)
- **MangaNinja**: HF demo Space in RUNTIME_ERROR as of 2026-10-27 — [HF API](https://huggingface.co/api/spaces/fffiloni/MangaNinja-demo)
- **AIComicX**: README banner "⚠️ PROJECT ARCHIVED (UNFINISHED) … has been discontinued in an incomplete state" — [repo](https://github.com/XBastille/AIComicX)
- **ComfyUI_StoryDiffusion**: 75 open issues as of 2026-10-27 — [repo](https://github.com/smthemex/ComfyUI_StoryDiffusion)
- **comicsol**: 25 open issues on a 7★ repo (2026-10-27); README says skill-install depends on an unpublished `v2.0.0rc6` and that projects beyond 4 pages or 12 panels require an explicit scope decision — [repo](https://github.com/wenn-id/comicsol)
- **ARIS-Movie-Director**: README (2026-07 note) says the legacy `gemini` CLI is deprecated upstream ("dies with `IneligibleTierError`") and ships a shim to Antigravity. This is upstream-API churn breaking agentic pipelines — [README](https://github.com/wanshuiyin/ARIS-Movie-Director)
- **inkstone** documents its own limits: consistency is "medium by design: the honest ceiling of a free, no-GPU model"; IP-Adapter/InsightFace-grade consistency "need a local GPU running SDXL/Flux"; free-tier 429/503s are handled with retries and resume — [README](https://github.com/phaethix/inkstone)
- **CallmeTruong/Comic_Studio** README: SD 1.5 "does not … understand complex actions perfectly"; diffusion at 80 steps is the slowest stage — [README](https://github.com/CallmeTruong/Comic_Studio)

### Inferences
- Pinned, unmaintained research environments (Python 3.9–3.11, Gradio 4.x, older transformers and huggingface_hub) are a frequent cause of failure. Even with a GPU, expect to pin versions manually. None of these repos documents Python 3.13 support.
- Issue trackers rarely show "consistency" complaints for the API-based apps, but those apps are too new and small to have meaningful issue histories (most show 0 open issues). The absence of issues is not evidence of quality.

### Gaps
- I read only issue titles and list metadata, not bodies or comments. Root causes and fixes (e.g. for DiffSensei #23/#25) are unverified.
- I did not review issue trackers for Story-Adapter, SEED-Story, ConsiStory, StoryMaker or the ComfyUI pack beyond their counts.

---

## Q6 (objective). Which are realistically usable in the target CPU-only Linux container (4 vCPU, 15 GB RAM, ~31 GB disk, Python 3.13, Node 22, internet via proxy)?

### Takeaway
Only API-driven pipelines are realistic. The best fits are **phaethix/inkstone** (Python, uv, no GPU by design, free Agnes key or any OpenAI-compatible image gateway), **kdjfs/plot2panel** (Node ≥20.9 + pnpm; DeepSeek + SiliconFlow/Together/Pollinations; 4 panels only), **BotTony329/mangaharness (Kumanga)** (Node ≥18.18; Gemini or OpenAI-compatible), **Yutarop/comic-generator** (Python ≥3.12 + google-genai; Nano Banana Pro, paid), and the archived but simple **ai-comic-factory** (Next.js; HF/OpenAI/Replicate). Agent-skill packs (agent-comic-kit, comicsol, hanxiaoyu, agent-mangaka-forge) also fit, provided the agent session has an image-generation tool or an external image API. Every research repo (DiffSensei, StoryDiffusion, Story-Adapter, SEED-Story, etc.) is impractical locally. Use them only via hosted endpoints (StoryDiffusion on Replicate or the HF ZeroGPU Space).

### Cited Findings
- inkstone states "No GPU, no paid plan: just one free API key", requires Python 3.10+ and uv, and its dependencies are light (Pillow ≥12.3,<13) — [README](https://github.com/phaethix/inkstone); `requires-python = ">=3.10"` in [pyproject](https://github.com/phaethix/inkstone/blob/main/pyproject.toml)
- plot2panel requires Node.js 20.9+ and pnpm 10, a DeepSeek key, and an image-provider key "unless you intentionally choose Pollinations or the local placeholder" — [README](https://github.com/kdjfs/plot2panel)
- mangaharness requires Node.js 18.18+; the editor works without an AI key, and AI uses Gemini or an OpenAI-compatible endpoint — [README](https://github.com/BotTony329/mangaharness)
- Yutarop/comic-generator requires Python ≥3.12 and google-genai ≥1.52.0 — [pyproject](https://github.com/Yutarop/comic-generator/blob/main/pyproject.toml); [README](https://github.com/Yutarop/comic-generator)
- ai-comic-factory's own HF Space runs on `cpu-basic` hardware, which shows the app needs no local GPU — [HF API](https://huggingface.co/api/spaces/jbilcke-hf/ai-comic-factory). Its `.nvmrc` pins Node v24.6.0 and it uses Next 14.2.7 — [repo](https://github.com/jbilcke-hf/ai-comic-factory)
- **Version mismatches with the container:**
  - stockedge/manga-generator requires **Node.js 24** (the container has 22) and, for the Claude Code path, an external ComfyUI GPU host (about 48 GB VRAM used in prototypes) — [docs/CLAUDE-CODE.md](https://github.com/stockedge/manga-generator/blob/main/docs/CLAUDE-CODE.md); [docs/COMFYUI.md](https://github.com/stockedge/manga-generator/blob/main/docs/COMFYUI.md)
  - huiman-ark requires Node **≥22.18.0** — [package.json](https://github.com/GL-Wen/huiman-ark/blob/main/package.json)
  - ltseries needs Docker (MongoDB), Go 1.24+ and FFmpeg — [README](https://github.com/eust-w/ltseries)
- **GPU-bound (not viable on CPU):**
  - DiffSensei: 24 GB even without the MLLM — [README](https://github.com/jianzongwu/DiffSensei)
  - StoryDiffusion: more than 20 GB — [README](https://github.com/HVision-NKU/StoryDiffusion)
  - SEED-Story: NVIDIA GPU + CUDA — [README](https://github.com/TencentARC/SEED-Story)
  - UNO: about 16 GB with fp8 — [README](https://github.com/bytedance/UNO)
  - InstantCharacter: under 22 GB with offload — [README](https://github.com/Tencent/InstantCharacter)
  - CharaConsist: 3 to 37 GB **GPU** — [README](https://github.com/Murray-Wang/CharaConsist)
  - CallmeTruong/Comic_Studio: "CPU mode is only practical for small tests" — [README](https://github.com/CallmeTruong/Comic_Studio)
- Hosted GPU fallback for research models: StoryDiffusion on Replicate, L40S, about $0.064 and about 66 s per run — [Replicate](https://replicate.com/hvision-nku/storydiffusion); HF Space on `zero-a10g` — [HF API](https://huggingface.co/api/spaces/YupengZhou/StoryDiffusion)
- Cost reference for Gemini-based pipelines: no free API tier for image models; Nano Banana Pro is $0.134 per 1K/2K image and Nano Banana 2 is $0.067 per 1K (2026-10-27) — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)

### Inferences
- Recommended shortlist for a CPU container:
  1. **inkstone**: lowest cost, txt → PDF/CBZ, honest about medium consistency; uv installs via pip.
  2. **Yutarop/comic-generator, or a similar thin Gemini script**: best consistency per the Nano Banana Pro claims, but paid; model IDs may need updating from `-preview`.
  3. **plot2panel**: polished but limited to 4-panel strips.
  4. **mangaharness/Kumanga**: an editor UI with agent features.
  5. **ai-comic-factory**: archived; its default model IDs are dated.
- A Claude Code agent with skill packs (agent-comic-kit, comicsol) also needs some image API reachable from the container, because Claude Code itself has no image-generation tool. stockedge's docs make the same point for Claude.
- Python 3.13 is untested by any repo here. Only lower bounds are declared: inkstone ≥3.10, comicsol ≥3.11, Yutarop ≥3.12, agent-comic-kit ≥3.11. Pure-Python plus Pillow stacks are likely fine. comicsol pins Pillow==13.0.0 and inkstone Pillow<13; I did not verify wheel availability for 3.13.
- Disk (31 GB) and RAM (15 GB) cannot hold FLUX.1-dev or SDXL plus an MLLM for CPU inference at useful speed. Even CharaConsist's 3 GB mode is a GPU sequential-offload mode.

### Gaps
- I installed or ran none of these in the target container; all feasibility statements come from READMEs and declared requirements.
- I did not verify the Agnes free tier (rate limits, commercial-use terms, availability from the proxy). The site returned only its title.
- I did not verify proxy reachability of third-party APIs (generativelanguage.googleapis.com, api.deepseek.com, SiliconFlow, Together, Replicate, api.antmoo.cc). Note that `aicomicfactory.app` failed DNS resolution in this session.
