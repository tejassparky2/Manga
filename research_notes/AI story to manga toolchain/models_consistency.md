# Image Models and Character-Consistency Techniques for Manga-Style Art (state as of 2026-10-27)

Research date: 2026-10-27. All prices/versions are "as retrieved on or shortly before 2026-10-27" unless otherwise dated. Items marked **[UNVERIFIED]** come only from third-party/aggregator sources or could not be checked against a primary page. Items marked **[OLDER]** are 2024–mid-2025 information that may be superseded.

Target container for the toolchain: Linux, NO GPU, 4 vCPU, 15 GB RAM, ~31 GB free disk. CPU-feasibility notes are given per model.

---

## Q1. Open-weight models for manga/anime art (SDXL anime family, FLUX family, Qwen-Image family, HiDream, SD3.5, 2025–2026 newcomers): quality for monochrome manga, licenses, sizes, VRAM, CPU feasibility

### Takeaway
For pure anime/manga line art, SDXL derivatives (Illustrious XL → NoobAI-XL, Animagine XL 4.0) remain the community default in 2026 because of tag-based control, Danbooru character/artist knowledge, ~6.5 GB checkpoints, 8 GB VRAM, and a deep LoRA/ControlNet ecosystem (including many monochrome/screentone LoRAs); the strongest 2026 open-weight newcomers are general-purpose multi-reference editors (FLUX 3 Image Klein, Qwen-Image-2.1, FLUX.2 klein) and an anime-specific 2B model (Anima), but the best of these carry non-commercial or revenue-capped licenses. Only Animagine XL 4.0 (Open RAIL++-M), Illustrious XL (OpenRAIL-M), FLUX.2 [klein] 4B (Apache 2.0), Qwen-Image/Qwen-Image-Edit-2509/2511 (Apache 2.0) and Z-Image-Turbo (Apache 2.0) are clearly commercial-friendly. On a 4-vCPU/15 GB-RAM box, only SDXL-class models with few-step distillation (minutes per image) and possibly small (2–6B) models via quantized stable-diffusion.cpp are realistic; 20B-class Qwen-Image and 32B FLUX.2 [dev] are not.

### Cited Findings

**SDXL anime family (2024–2025 releases, still dominant in 2026)**
- 2026 guides say SDXL models built on Illustrious or NoobAI still lead for pure anime, citing deeper ecosystem, purpose-built models and lower VRAM than FLUX — [InsiderLLM 2026 guide](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/); [LocalAIMaster: Illustrious vs NoobAI](https://localaimaster.com/blog/best-local-anime-image-model)
- **NoobAI-XL (v-pred or eps)**: SDXL fine-tune built on Illustrious v0.1, trained on Danbooru + e621 (~13M images), 6.46 GB pruned fp16, min 8 GB VRAM, "final release"; v-pred needs Euler/DDIM (not Karras); recommended Euler/DDIM, 25–40 steps, CFG 5–7 — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)
- NoobAI-XL license on Hugging Face: `fair-ai-public-license-1.0-sd` (FAIPL-1.0-SD) — [HF Laxhar/noobai-XL-1.1](https://huggingface.co/Laxhar/noobai-XL-1.1); [HF Laxhar/noobai-XL-Vpred-1.0](https://huggingface.co/Laxhar/noobai-XL-Vpred-1.0). Laxhar README asks derivatives to "remain open source" (share-alike) and adds harmful-use restrictions — [HF Laxhar Vpred-0.5 README](https://huggingface.co/Laxhar/noobai-XL-Vpred-0.5/blob/806c6d1255df328c58bb16e4a9f7ecda6015545e/README.md?code=true). A 2026 guide summary describes NoobAI's licence as non-commercial — [LocalAIMaster](https://localaimaster.com/blog/best-local-anime-image-model) **[UNVERIFIED — conflicts with FAIPL text; a Civitai community article argues NoobAI's extra restrictions are likely unenforceable](https://civitai.com/articles/18619)**. Treat NoobAI commercial status as ambiguous.
- **Illustrious XL v2.0**: SDXL, 6.5 GB, min 8 GB VRAM, data through Aug 2024, native up to 1536×1536; Euler a, 28–35 steps, CFG 5.5–7, Clip Skip 2 — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/). License tag `creativeml-openrail-m` — [HF OnomaAIResearch/Illustrious-XL-v2.0](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0). Official v2.0 base suits LoRAs/control; merges (WAI-Illustrious v16, Hassaku, NoobAI) add built-in style — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)
- **Animagine XL 4.0**: retrained from SDXL 1.0 on 8,401,464 anime images, knowledge cutoff 2025-01-07; released 2025-01-24, "Opt" 2025-02-13; "3B params", F16; CFG 4–7 (5 rec.), 25–28 steps (28 rec.), Euler a, e.g. 832×1216; license **CreativeML Open RAIL++-M, commercial use permitted** — [HF cagliostrolab/animagine-xl-4.0](https://huggingface.co/cagliostrolab/animagine-xl-4.0). File ~6.5 GB, 8 GB VRAM — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)
- **Pony Diffusion V6 XL**: 6.9 GB + 335 MB VAE, 2.6M training images (~50/50 SFW/NSFW), score tags, Euler a 25 steps CFG 7. **Pony V7** uses AuraFlow (7B params); V6 LoRAs incompatible; tooling immature — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)

**Monochrome manga / screentone add-ons (SDXL/Illustrious LoRAs on Civitai)**
- *Manga Mode [Illustrious]*: triggers "m4ng4" and "monochrome greyscale screentones crosshatching", Clip Skip 2, published 2025-02-15 — [Civitai](https://civitai.com/models/1255751/manga-mode-illustrious)
- *manga | Illustrious Style LoRA*: aimed at manga page layouts; strength 1.0, CFG 4–8, 20–30 steps, Euler a; example prompt uses speech-bubble and 4koma tags — [Civitai](https://civitai.com/models/1745962/manga-or-illustrious-style-lora)
- *monochrome/greyscale | Illustrious Style LoRA* (hatching/sketch) — [Civitai](https://civitai.com/models/1633019/monochromegreyscale-or-illustrious-style-lora); *Stylish Monochrome* — [Civitai](https://civitai.com/models/962873/stylish-monochrome); *Monochrome Comic for IllustriousXL 2.0* — [Civitai](https://civitai.com/models/1281848/monochrome-comic); *monochrome/traditional media* — [Civitai](https://civitai.com/models/1599901/monochrometraditional-media-or-illustrious-style-lora?modelVersionId=1810512)
- *SDXL LoRA for Classic Black & White Manga Style* (trigger "m4ng41nk"): trained for clean ink line art, varied line weights, screentone dot shading, dramatic hatching — [Civitai](https://civitai.com/models/2664796/sdxl-lora-for-classic-black-and-white-manga-style?modelVersionId=2992297)
- LineAniRedmond (SDXL manga-style lineart LoRA) and a cross-platform lineart LoRA that works on SD3.5, Flux, SDXL, Pony (weight 0.5–1.0) — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)
- NoobAI also has a dedicated "manga line" ControlNet (see Q4) — [HF Laxhar NoobAI-SDXL-controlnet collection](https://huggingface.co/collections/Laxhar/noobai-sdxl-controlnet)

**Anima (2025–2026 anime newcomer)**
- 2B-parameter text-to-image model from CircleStone Labs (with Comfy Org) built on NVIDIA Cosmos-Predict2-2B-Text2Image; text encoder Qwen3 0.6B base; Qwen-Image VAE; trained on "several million anime images and about 800k non-anime artistic images", no synthetic data, anime cutoff Sept 2025; 512²–1536²; 30–50 steps CFG 4–5 (Turbo: CFG 1, 8–12 steps); Danbooru tags + natural language, artists via "@name"; "natively supported in ComfyUI"; weak at realism and long text — [HF circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)
- License: CircleStone Labs Non-Commercial License for model and derivatives (plus NVIDIA Open Model License inheritance); **outputs may be used commercially**; hosting behind paid API/platform not allowed without a commercial license — [HF Anima README](https://huggingface.co/circlestone-labs/Anima/blob/main/README.md)
- Hands-on report: ~7 GB VRAM — [lilting.ch](https://lilting.ch/en/articles/anima-2b-anime-image-generation) **[UNVERIFIED single source]**. Supported by stable-diffusion.cpp (CPU-capable) — [GitHub leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp). A 2026 guide covers Anima character-LoRA training on 12 GB VRAM — [note.com/sepiablue](https://note.com/sepiablue/n/nf6cb2520d2a2?hl=en)

**FLUX family (Black Forest Labs)**
- FLUX.1 base is 12B; ≥12 GB VRAM for comfortable anime use, 16 GB+ with GGUF Q8 recommended; anime FLUX finetunes (AnimePro FLUX on Schnell, AnimEasy 4-bit) are "early" — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)
- **FLUX.1 Kontext [dev]**: 12B rectified-flow transformer; "character, style and object reference without any finetuning"; multi-turn edits "with minimal visual drift"; FLUX.1 [dev] Non-Commercial License (card also says outputs can be used commercially); paper 2025-06-17 — [HF FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev) **[OLDER, mid-2025]**
- **FLUX.2 [dev]**: 32B flow-matching model for generation and multi-image editing, FLUX Non-Commercial License, released Nov 2025 — [HF FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev); ~90 GB VRAM unquantized per a third-party summary — [innFactory](https://innfactory.ai/en/ai-models/flux/) **[UNVERIFIED]**
- **FLUX.2 [klein] 4B**: 4B rectified-flow transformer; T2I + editing + multi-reference editing; 4 steps, guidance 1.0; "under a second"; ~13 GB VRAM (RTX 3090/4070+); **Apache 2.0** — [HF FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B). Klein family released 2026-01-15; klein 9B is FLUX Non-Commercial, 19.6 GB VRAM — [BFL FLUX.2 overview](https://docs.bfl.ml/flux_2/flux2_overview); [VentureBeat](https://venturebeat.com/technology/black-forest-labs-launches-open-source-flux-2-klein-to-generate-ai-images-in)
- **FLUX 3 Image Klein** (newest, 2026-10-15): "5.6B open weights model" (Hub metadata says 6B); text encoder Qwen3-VL-4B-Instruct; T2I + single-reference editing + multi-reference generation with **up to 10 reference images**; bounding-box layout prompts; distilled checkpoint 16 steps/no guidance, Base 50 steps guidance 3.5; VRAM at 1024² on B200: 31 GB BF16, 26 GB FP8, 25 GB NVFP4 (prompt upsampler extra 18.8 GB download); diffusers modular pipeline (install from main); **FLUX Kommunity License v1.0**: non-commercial, plus commercial *output* for "Qualifying Users" with < US$5M revenue — [HF flux-3-image-klein](https://huggingface.co/black-forest-labs/flux-3-image-klein). Release date and "~8 GB VRAM in quantized builds" — [VentureBeat](https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses); [AlphaSignal](https://alphasignal.ai/news/black-forest-labs-flux-3-klein-runs-image-generation-on-8gb-gpus) **[8 GB figure UNVERIFIED vs. HF card's 25–31 GB]**. FLUX 3 Dev announced, no release date as of Oct 2026 — [Layer3Labs](https://www.layer3labs.io/guides/flux-3-image-explained) **[UNVERIFIED]**

**Qwen-Image family (Alibaba)**
- Original Qwen-Image (Aug 2025) and Qwen-Image-2512 were Apache 2.0 — [CellCog](https://cellcog.ai/blog/qwen-image-2-1/); [Elegant Software Solutions](https://www.elegantsoftwaresolutions.com/blog/qwen-image-2-1-release-guide) **[secondary]**
- **Qwen-Image-Edit-2511**: Apache 2.0; improved identity preservation and multi-person group-photo consistency — [HF Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511); 20B params BF16 — [aiindigo](https://aiindigo.com/tool/qwen-image-edit-2511) **[secondary]**. Earlier Edit-2509 optimized for 1–3 input images — [ComfyUI docs](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511)
- **Qwen-Image-2.1** (weights 2026-09-20): unified generation + editing; 7B visual DiT (32 single-stream layers); up to **10 reference images**; native RGBA; local edits via circles/painted annotations/masks; identity preservation; examples at 2048×2048 with 40 steps; `QwenImage21Pipeline` (diffusers main); **Qwen Research License (research/evaluation only)**; no anime/manga mention on card — [HF Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1). Text encoder Qwen3-VL 8B, ~15B total with encoder; release date — [DataNorth](https://datanorth.ai/news/qwen-releases-qwen-image-2-1); [CometAPI community](https://community.cometapi.com/t/qwen-image-2-1-has-open-weights-but-shipping-it-commercially-needs-a-separate-license/1149) **[secondary]**

**Other open-weight models**
- **Z-Image-Turbo** (Alibaba Tongyi-MAI): 6B, Apache 2.0, late Nov 2025; ~16 GB BF16, 8 GB FP8, ~6 GB GGUF; anime quality not covered in sources — [AlphaSignal](https://alphasignal.ai/news/alibaba-s-z-image-turbo-tops-open-weight-rankings-on-a-16gb-gpu); [Tech Insider](https://tech-insider.org/z-image-turbo-local-setup-2026/); [runaihome](https://runaihome.com/blog/z-image-turbo-16gb-vram-home-lab-image-gen-2026/) **[secondary]**
- **SD 3.5**: Stability Community License — free for research/non-commercial and for commercial use by orgs under US$1M annual revenue — [Stability AI license](https://stability.ai/license); [Stability SD3.5 announcement](https://stability.ai/news/introducing-stable-diffusion-3-5). No notable anime finetune ecosystem found (only a cross-platform lineart LoRA) — [InsiderLLM](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)
- **HiDream-I1**: transformer weights MIT-licensed, "commercial-friendly" — [d-central.tech model DB](https://d-central.tech/local-image-generation-models/) **[secondary; check HF card]**
- **HunyuanImage 3.0 Instruct** (Tencent, Jan 2026) and **Bria Fibo 2.0** (Oct 2026) rank #4 and #1 on the AA open-weights editing board — [Artificial Analysis open-weights editing](https://artificialanalysis.ai/image/leaderboard/editing/open-weights)

**CPU-only feasibility (relevant to 4 vCPU / 15 GB RAM / no GPU)**
- stable-diffusion.cpp (latest news entry 2026-10-16) runs on CPU (AVX/AVX2/AVX512) and supports SD1.x/SDXL, SD3.5, FLUX.1, FLUX.2 dev/klein, FLUX.3 Image Klein, Qwen Image 2.1, Qwen Image Edit series, FLUX.1-Kontext-dev, Z-Image, Anima, HiDream-O1-Image, "Ideogram4", Chroma, etc.; GGUF quantization; LoRA, PhotoMaker, IP-Adapter (SD1.5 & SDXL), **ControlNet (SD1.5 only)**, TAESD, ESRGAN — [GitHub stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)
- FastSD CPU benchmarks on an Intel i7-12700 (12 cores/20 threads): SDXL-Turbo 512², 1 step: 10 s (PyTorch) / 5.6 s (OpenVINO) / 2.5 s (OpenVINO+TAESD); SDXL-Lightning 768², 2 steps: 18 / 12 / 10 s; Hyper-SD SDXL 768², 1 step: 19 / 13 / 6.3 s; FLUX.1-schnell int4 512², 3 steps: 4 min 30 s; FLUX at 512² needs ~30 GB RAM; SDXL OpenVINO min 11 GB RAM (~9 GB with TAESD); Z-Image-Turbo Q4_K via sd.cpp ~7–8 GB RAM total — [LocalAIMaster, 2026-09-27](https://localaimaster.com/blog/image-generation-without-gpu); [GitHub rupeshs/fastsdcpu](https://github.com/rupeshs/fastsdcpu)
- Full SDXL at 1024×1024, 30 steps, Euler on an 8-vCPU VPS: ~780 s (~13 min) per image ("10–20 minutes"); SDXL CPU needs ~16 GB RAM, SD1.5 ~8 GB; SD1.5 512² takes 1–2 min — [SSD Nodes guide](https://www.ssdnodes.com/learn/self-hosted-ai-image-generator) **[order-of-magnitude vendor estimate]**
- A stable-diffusion.cpp paper reports 59.3 s end-to-end on a Xeon CPU for a Q3_K model (model/resolution unspecified) — [EmergentMind summary](https://www.emergentmind.com/topics/stable-diffusion-cpp) **[UNVERIFIED context]**

### Inferences
- Best open-weight quality for B&W manga today = Illustrious/NoobAI-family checkpoint (or Animagine XL 4.0 if commercial-license clarity matters) + a monochrome/screentone LoRA ("monochrome, greyscale, screentones" tags) + optional NoobAI "manga line"/lineart ControlNet. None of the 2026 general models (FLUX 3 Klein, Qwen-Image-2.1) document manga/screentone ability; they'd need LoRAs or reference-style inputs.
- License-clean commercial local stack: Animagine XL 4.0 or Illustrious XL (OpenRAIL), FLUX.2 [klein] 4B (Apache) for reference-based editing, Qwen-Image-Edit-2511 (Apache, but ~20B—GPU only). Anima/FLUX 3 Klein permit commercial *outputs* (Anima for anyone; FLUX 3 Klein for <$5M revenue) but not commercial redistribution/hosting.
- On the target container (4 vCPU, i.e. roughly 1/3–1/5 of the i7-12700's threads): extrapolating from the 8-vCPU 13-min figure, full-step SDXL/Illustrious at 1024² would take ~25–40 min/image — impractical. With few-step distillation (SDXL-Lightning/Hyper-SD/DMD2-style LoRAs, 2–8 steps) plus OpenVINO or sd.cpp and TAESD, roughly 1–5 min per 768–1024² image is plausible. SDXL fits in 15 GB RAM only tightly (needs ~11–16 GB). These are extrapolations, not measurements.
- Anima (2B) and FLUX.2 klein 4B / Z-Image-Turbo Q4 GGUF (~7–8 GB RAM) are the most CPU-plausible "modern" models in RAM terms, but each image is likely multiple minutes on 4 vCPU. Qwen-Image(-Edit) 20B, FLUX.2 dev 32B, and FLUX.1 12B (≥30 GB RAM at 512²) are effectively infeasible within 15 GB RAM. FLUX 3 Klein (5.6B + 4B VL encoder) might fit at Q4 but is unbenchmarked on CPU.
- Disk: each SDXL checkpoint ~6.5 GB; with 31 GB free, plan for at most ~2–3 checkpoints plus LoRAs/ControlNets (~2.5 GB each for SDXL ControlNets is typical, unverified here).

### Gaps
- No primary source for NoobAI-XL's exact commercial terms (HF card body did not render); conflicting secondary claims.
- No license found for Pony V7 / AuraFlow; no HF-card verification for HiDream-I1 license.
- No measured CPU timings for Anima, FLUX.2 klein 4B, FLUX 3 Klein, or Illustrious/NoobAI on a 4-vCPU machine; all CPU numbers above are from 8–20-thread machines or estimates.
- No source evaluates FLUX 3 Klein, Qwen-Image-2.1, or Z-Image specifically on monochrome manga/screentone output.
- Exact file sizes for FLUX 3 Klein / Qwen-Image-2.1 weights not stated on cards.

---

## Q2. Character consistency techniques (LoRA training, IP-Adapter/FaceID, InstantID, PhotoMaker, PuLID, reference-only, StoryDiffusion, DiffSensei, OmniGen2, Kontext, ACE++, UNO, InfiniteYou, in-context editing models) — and what works for anime/manga faces vs photoreal

### Takeaway
For anime/manga, a per-character LoRA on an Illustrious/NoobAI/Anima base (≈15–50 curated images, ~1,500–3,000 steps, 8–24 GB NVIDIA GPU) remains the most reliable way to lock face, hair and outfit across hundreds of panels; zero-shot alternatives are now strong but mostly photoreal-oriented (InstantID/PuLID/PhotoMaker/FaceID depend on InsightFace face embeddings with non-commercial model licenses), while 2025–2026 in-context multi-reference editors (FLUX.1 Kontext, Qwen-Image-Edit-2511, FLUX 3 Klein / Qwen-Image-2.1 with up to 10 references, OmniGen2) and commercial APIs give good training-free consistency. Manga-specific research (DiffSensei, MangaFlow, SyntheticManga, AnimeAdapter) exists but has limited usable releases. None of the training approaches are viable CPU-only.

### Cited Findings

**Character LoRA training**
- Dataset: at least 10 images, ideally ~20–50 — [note.com 2026 Illustrious LoRA guide](https://note.com/reocoffee/n/n9744ca3ad878?hl=en); 20–40 images of the target character — [digitalcreativeai](https://www.digitalcreativeai.net/en/post/original-character-lora-illustrious-character-training); AI Toolkit Illustrious example used 15 images, quality > quantity, vary pose/angle/background, caption what is *not* the character's defining trait — [comfyui.nomadoor AI Toolkit SDXL guide](https://comfyui.nomadoor.net/en/notes/ai-toolkit-sdxl-lora-training/)
- Resolution ≥1024² for SDXL/Pony/Illustrious; WD14 tagging with `wd-eva02-large-tagger-v3` for anime; kohya folder name `10_name` = repeats — [Tech Tactician kohya tutorial](https://techtactician.com/how-to-train-stable-diffusion-lora-models/); [digitalcreativeai](https://www.digitalcreativeai.net/en/post/original-character-lora-illustrious-character-training)
- Hyperparameters (2026 guide): rank 16–32, alpha = rank, U-Net LR 1e-4, text encoders frozen initially — [Airmore LoRA guide 2026](https://airmore.ai/lora-training-guide.html); typical 1,500–3,000 steps; another claims Illustrious converges ~3,000; a 2025 example used rank 8/alpha 1/1,600 steps; SeaArt suggests rank 64 and higher LR (conflicting) — [SeaArt guide](https://www.seaart.ai/articleDetail/cvdakg5e878c73a5mbrg); [vancurious kohya guide](https://vancurious.ca/generative-AI-Kohya) **[community; numbers conflict]**
- ostris **ai-toolkit** (MIT): LoRA training for FLUX.1-dev, FLUX.2-dev, FLUX.2-klein base 4B/9B, Qwen-Image (incl. 2512, 2.1, 2.1-Turbo), Z-Image/Turbo, SDXL, SD1.5, Chroma, HiDream I1, plus edit models FLUX.1-Kontext-dev, Qwen-Image-Edit 2509/2511, HiDream E1; requires "Nvidia GPU with enough ram"; example configs like `train_lora_flux_24gb.yaml`; CPU training not mentioned — [GitHub ostris/ai-toolkit](https://github.com/ostris/ai-toolkit)
- Anima character LoRA guide targets 12 GB VRAM — [note.com/sepiablue](https://note.com/sepiablue/n/nf6cb2520d2a2?hl=en)

**Adapter / zero-shot identity methods (SD/SDXL era)**
- NoobAI-trained IP-Adapter (kataragi/Noob_ipadapter): load through ControlNet slot with CLIP-ViT-H preprocessor; also an Animagine XL 3.1 variant — [HF kataragi/Noob_ipadapter](https://huggingface.co/kataragi/Noob_ipadapter)
- ComfyUI IPAdapter Plus lists SDXL ViT-H, face, and FaceID models; FaceID requires insightface — [GitHub ComfyUI_IPAdapter_plus (mirror)](https://github.com/erikluo/ComfyUI_IPAdapter_plus)
- Community guidance: IP-Adapter FaceID-Plus / InstantID for SDXL, PhotoMaker if many face photos, plus OpenPose ControlNet — [Digital Zoom Studio, Feb 2026](https://digitalzoomstudio.net/2026/02/stable-diffusion-character-consistency/)
- InstantID code Apache 2.0 but face models (antelopev2) and checkpoints "for non-commercial research purposes only" per insightface license; PuLID also uses InsightFace antelopev2 — [GitHub InstantID (mirror)](https://github.com/zengyh1900/InstantID); [Replicate fofr/pulid-base readme](https://replicate.com/fofr/pulid-base/readme)
- MediaPipe can detect faces but cannot replace InstantID/FaceID identity embeddings — [comfy.icu MediaPipe FaceMesh node](https://comfy.icu/node/Inference_Core_MediaPipe-FaceMeshPreprocessor)
- **AnimeAdapter** (arXiv 2605.20237, May/June 2026): lightweight SD appearance adapter for anime characters from one reference; semantic-selective local attention + pose-aware conditioning; positions itself against IP-Adapter's loss of fine-grained detail; compatible with ControlNet/LoRAs; **code/weights "will be released upon acceptance"** — [arXiv abs](https://arxiv.org/abs/2605.20237); [search summary of v1](https://arxiv.org/html/2605.20237v1)

**Training-free sequence/story methods**
- **StoryDiffusion** (consistent self-attention, ByteDance/Nankai): plug-in for SD1.5/SDXL models; needs ≥3 prompts (5–6 recommended); low-VRAM script tested on 24 GB A10 + 30 GB RAM — [GitHub HVision-NKU/StoryDiffusion](https://github.com/hvision-nku/storydiffusion); [HF Space README](https://huggingface.co/spaces/lixiang6/demo/blob/main/README.md) **[OLDER, 2024]**. License not confirmed.
- **DiffSensei** (CVPR 2025): diffusion generator + multimodal LLM as character identity adapter; masked cross-attention for character placement per panel; MangaZero dataset 43,264 pages / 427,147 panels / 48 series — [arXiv 2412.07589](https://arxiv.org/abs/2412.07589v1); [The Decoder](https://the-decoder.com/diffsensei-ai-pioneers-hinton-lecun-and-bengio-star-in-fictional-manga-created-by-new-ai-system/). Without character references output looks generic — [The Decoder](https://the-decoder.com/diffsensei-ai-pioneers-hinton-lecun-and-bengio-star-in-fictional-manga-created-by-new-ai-system/) **[OLDER]**
- **Manga Generation via Layout-controllable Diffusion** (Manga109Story dataset) — [arXiv 2412.19303](https://arxiv.org/abs/2412.19303) **[OLDER]**
- **MangaFlow** (EMNLP 2026 Main; v2 2026-09-14): agentic story→manga pipeline (planning, grounding, layout, reference-conditioned rendering, composition, text placement); a "story section memory" links section text to character/scene/object references reused across panels; meta-benchmark for layout/consistency/quality; backbone model and code not stated on abstract — [arXiv 2605.28173](https://arxiv.org/abs/2605.28173)
- **SyntheticManga** (CVPR 2026 Findings): training-free, layout-aware multi-character manga generation with "phased diffusion", evaluated on ConsiStory+ — [CVF open access PDF](https://openaccess.thecvf.com/content/CVPR2026F/papers/Peng_SyntheticManga_Training-Free_Manga_Generation_with_Phased_Diffusion_CVPRF_2026_paper.pdf) **[details only from search snippet; PDF returned 403]**
- TaleDiffusion (multi-character story generation with dialogue rendering) — [arXiv 2509.04123](https://arxiv.org/pdf/2509.04123) **[not read in detail]**

**Unified / in-context reference models (open)**
- **OmniGen2** OmniContext benchmark (8 task categories; images include animation stills; GPT-4.1 judge). Single-subject table (later arXiv version): OmniGen2 8.68 subject-consistency / 8.19 overall; UNO 6.48 / 6.60; InfiniteYou 5.15 / 6.05. An earlier version reported OmniGen2 7.18 overall vs UNO 4.71 — [arXiv 2506.18871](https://arxiv.org/html/2506.18871); [CVPR 2026 paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_OmniGen2_Towards_Instruction-Aligned_Multimodal_Generation_CVPR_2026_paper.pdf)
- **UNO** (ByteDance, FLUX.1-based): code Apache 2.0, weights CC BY-NC 4.0, FLUX.1-dev terms apply — [ComfyUI Wiki](https://comfyui-wiki.com/ja/news/2025-04-09-bytedance-uno-ai-image); [HF Space README](https://huggingface.co/spaces/altarcomputing/UNO-FLUX/blame/main/README.md) **[OLDER]**
- **FLUX.1 Kontext [dev]**: character/style/object reference without finetuning, multi-turn editing with minimal drift (non-commercial weights) — [HF](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)
- **Qwen-Image-Edit-2511** (Apache 2.0): identity preservation in imaginative portrait edits, multi-person consistency — [HF](https://huggingface.co/Qwen/Qwen-Image-Edit-2511); [HackerNoon "stops face drift"](https://hackernoon.com/the-image-editor-that-finally-stops-face-drift-inside-qwen-image-edit-2511)
- **FLUX 3 Image Klein** and **Qwen-Image-2.1**: up to 10 reference images each — [HF FLUX 3 Klein](https://huggingface.co/black-forest-labs/flux-3-image-klein); [HF Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)

**Commercial-API consistency (details in Q3)**
- Gemini: up to 4 character images for consistency (Nano Banana 2.1 / 3.1 Flash), up to 5 for Pro; multi-turn chaining recommended — [Google Gemini image-generation docs](https://ai.google.dev/gemini-api/docs/image-generation)
- OpenAI GPT Image 2.5 docs admit the model "may occasionally struggle to maintain visual consistency for recurring characters or brand elements" — [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- Practical comic advice: pass only references of characters actually in the panel; stacking unrelated character refs blurs attribute binding — [tech-insider comic guide](https://tech-insider.org/ai-comic-generator-character-consistency-2026/) **[secondary]**; open-source manga generator feeds the previous page image back to keep characters consistent — [GitHub Yutarop/comic-generator](https://github.com/Yutarop/comic-generator)

### Inferences
- Anime vs photoreal: InstantID, PuLID, PhotoMaker, IP-Adapter FaceID, InfiniteYou all hinge on face-recognition embeddings (InsightFace) trained on real faces; anime faces (large eyes, simplified features) are likely to be poorly detected/embedded, and the InsightFace weights are non-commercial — so these are the wrong tool for manga. Anime-appropriate zero-shot options are CLIP-image-based IP-Adapter (esp. the NoobAI-trained one), in-context editors (Kontext, Qwen-Image-Edit, FLUX 3 Klein), and commercial multi-reference APIs; the robust option remains a character LoRA (identity encoded in tag space, works with ControlNet and regional prompting).
- Recommended hybrid for a manga pipeline: (1) design model sheet (front/side/back, expressions) with an API or local model; (2) train a LoRA per main character on that sheet (needs a rented GPU — not possible on the CPU container); (3) generate panels with LoRA + pose ControlNet; (4) optionally fix drift with an in-context editor using the model sheet as reference.
- CPU container: LoRA *inference* works in stable-diffusion.cpp on CPU; LoRA *training* and StoryDiffusion/DiffSensei/OmniGen2 (GPU-scale VRAM) do not.

### Gaps
- No quantitative head-to-head of IP-Adapter vs Kontext vs Qwen-Image-Edit vs LoRA on anime/manga characters found.
- No source confirms whether InsightFace fails specifically on anime faces (inferred, not measured).
- ACE++ and InfiniteYou licenses and anime performance not found; PhotoMaker anime performance not found.
- DiffSensei repo license, VRAM, and current maintenance status not verified; MangaFlow backbone and code release unknown; SyntheticManga numbers not read.
- No published training time per LoRA on specific GPUs found in the sources read.

---

## Q3. Commercial APIs with reference-image / multi-image character consistency: pricing, limits, endpoints, SDKs, policies, commercial terms

### Takeaway
As of late Oct 2026 the main reference-capable APIs are OpenAI GPT Image 2 / 2.5 (token-priced; ~$0.005–$0.21 per 1024² image), Google Gemini "Nano Banana" 2.1 / 2 / 2 Lite / Pro ($0.0336–$0.24 per image; up to 4–5 character refs), BFL FLUX (Kontext pro $0.04 / max $0.08; FLUX 3 Klein ~$0.009), ByteDance Seedream 4.5/5.0 (~$0.018–$0.045, up to 10–14 refs, mostly third-party-verified), Ideogram (character reference surcharge on 3.0; new 4.5 pricing), Runway Gen-4 Image with References ($0.02–$0.08) and Recraft ($0.04 raster). Midjourney still has no official API (V8.2 replaced --cref/--oref with an "Edit Model"). Gemini 2.5 Flash Image (original Nano Banana) and gpt-image-1 have been shut down.

### Cited Findings

**OpenAI (GPT Image)**
- Current models: `gpt-image-2.5-sunburst` (editing precision) and `gpt-image-2.5-flare` (fast everyday); quality levels low/medium/high/xhigh/max; endpoints `/v1/images/generations`, `/v1/images/edits`, and Responses API `image_generation` tool; Python `client.images.generate`, `client.images.edit`, `client.responses.create(tools=[{"type":"image_generation"}])`; `moderation` = `auto` (standard) or `low`; edit example passes 4 reference images; GPT Image 2 sizes up to 3840 px edge, multiples of 16, ≤3:1 ratio — [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- Token prices (per 1M): GPT Image 2.5 (both) and gpt-image-2: image input $8, image output $30, text input $5, cached image input $2; gpt-image-1.5: $8 / $32; gpt-image-1-mini: $2.50 / $8; batch ~50% (e.g. gpt-image-2 $4 / $15) — [OpenAI pricing](https://developers.openai.com/api/docs/pricing)
- Per-image (1024×1024 low/medium/high): gpt-image-2 $0.006 / $0.053 / $0.211 (portrait/landscape $0.005 / $0.041 / $0.165); gpt-image-1.5 $0.009 / $0.034 / $0.133; gpt-image-1-mini $0.005 / $0.011 / $0.036; `gpt-image-1` "was shut down on October 23, 2026"; for gpt-image-2 input_fidelity is fixed high (more input tokens with references) — [OpenAI image guide, cost section](https://developers.openai.com/api/docs/guides/image-generation)
- GPT Image 2.5 per-image estimate $0.005–$0.211 (max 1024² $0.211); gpt-image-1.5, gpt-image-1-mini and `chatgpt-image-latest` retire 2026-12-01; DALL·E 2/3 removed 2026-05-12 — [CostGoat, updated 2026-10-20](https://costgoat.com/pricing/openai-images) **[third-party estimates]**

**Google Gemini ("Nano Banana")**
- Models/IDs: Nano Banana 2.1 `gemini-nano-banana-2.1` (primary); Nano Banana 2 `gemini-3.1-flash-image`; Nano Banana 2 Lite `gemini-3.1-flash-lite-image`; Nano Banana Pro `gemini-3-pro-image`; Nano Banana `gemini-2.5-flash-image` (legacy). References: up to 10 object images (2.1, 3.1 Flash), 14 (Flash Lite), 6 (Pro); **up to 4 character images for consistency (2.1, 3.1 Flash), 5 (Pro)**; style refs up to 3 (Pro). 1K/2K/4K. All outputs carry **SynthID** watermark. Multi-turn via `previous_interaction_id`; Python `google-genai`: `client.interactions.create(...)`. Flash Lite "not optimized for multiple reference inputs or multi-turn" — [Gemini image-generation docs](https://ai.google.dev/gemini-api/docs/image-generation) (table flattened; mapping per fetch tool)
- Prices per output image (standard / batch): Nano Banana 2.1 $0.0336 (1K), $0.0504 (2K), $0.113 (4K) / half in batch; Nano Banana 2 (3.1 Flash) $0.045 (0.5K), $0.067 (1K), $0.101 (2K), $0.151 (4K) / batch $0.022–$0.076; Nano Banana 2 Lite $0.0336 (1K) / $0.0168; Nano Banana Pro $0.134 (1K/2K), $0.24 (4K) / batch $0.067 / $0.12; Gemini 2.5 Flash Image $0.039, "deprecated and will be shut down on October 2, 2026" — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)

**Black Forest Labs (FLUX API)**
- FLUX.1 Kontext [pro] $0.04/image, Kontext [max] $0.08/image (1 credit = $0.01) — [BFL pricing docs (EU mirror)](https://docs.eu.bfl.ai/quick_start/pricing); [bfl.ai/pricing](https://bfl.ai/pricing) (per search; values did not render on fetch) **[OLDER model, mid-2025]**
- FLUX 3 Image / FLUX 3 Image Klein priced per image by resolution (768², 1K, 1.5K, 2K, 4K); FLUX.2 pro/max/flex/klein priced per megapixel; FLUX.2 [dev] local only — [BFL pricing docs](https://docs.bfl.ml/quick_start/pricing) (numbers did not render)
- FLUX 3 Image Klein API ≈ $0.009 per 1K image — [VentureBeat](https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses); AA lists $9 per 1,000 images; FLUX.2 [klein] 9B $17/1k; FLUX.2 [dev] $24/1k (hosted by partners) — [Artificial Analysis](https://artificialanalysis.ai/image/leaderboard/editing/open-weights)
- Self-hosting license tiers (prices not public): Builder (FLUX 3 Klein/FLUX.2 klein, 10K images/month), Platform and Professional (100K images/month), Enterprise — [bfl.ai/pricing](https://bfl.ai/pricing)

**ByteDance Seedream (BytePlus ModelArk)** — all **[third-party, official BytePlus page not retrieved]**
- Seedream 4.5 (`seedream-4-5-251128`) $0.04/image; Seedream 5.0 (`seedream-5-0-260128`) $0.035/image — [APIYI docs](https://docs.apiyi.com/en/api-capabilities/seedream-image); OpenRouter $0.04/image for 4.5 — [OpenRouter](https://openrouter.ai/bytedance-seed/seedream-4.5/pricing)
- Seedream 5.0 Pro ~$0.045 per output up to 2.36 MP (first reference free, +$0.003 per extra), up to 10 references — [The Rundown](https://www.therundown.ai/tools/seedream-5-0-pro); conflicting $0.075 — [kie.ai](https://kie.ai/blog/what-is-seedream-5) and $0.12 — [EvoLink](https://evolink.ai/seedream-5-0-pro); 5.0 Lite $0.035, up to 14 references — [Apiyi blog](https://help.apiyi.com/en/seedream-5-0-lite-api-guide-cheaper-than-4-5-en.html); Flash $0.018 — [GlobalGPT](https://www.glbgpt.com/hub/how-to-use-seedream-5-0-flash)

**Ideogram**
- Ideogram 3.0 API: $0.03 / $0.06 / $0.09 (Turbo/Default/Quality), with Character Reference $0.10 / $0.15 / $0.20 — [eesel.ai](https://www.eesel.ai/blog/ideogram-pricing); [checkthat.ai](https://checkthat.ai/brands/ideogram/pricing) **[third-party]**
- Ideogram 4.5 (newest): from $0.008/image (very low quality) to $0.06 medium, references priced same as prompt-only — [GlobalGPT review, checked 2026-10-21](https://www.glbgpt.com/hub/ideogram-4-5-review) **[UNVERIFIED]**
- Official API page lists models 4.5/4.0/3.0 and a default rate limit of **10 in-flight requests**; price table did not render — [Ideogram pricing (API tab)](http://ideogram.ai/pricing/?pricing_tab=api)

**Midjourney**
- No official public API as of Aug 2026; third-party "Midjourney APIs" are unofficial wrappers and automation violates ToS — [Unifically](https://unifically.com/blogs/midjourney-api) **[secondary]**
- V8.2 default since 2026-07-24; new **Edit Model replaces Omni Reference, Character Reference and Retexture**; up to four reference images via `--edit` — [Midjourney docs: Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version) (via search snippet; direct fetch 403); [blakecrosley guide](https://blakecrosley.com/guides/midjourney); Omni Reference remains a V7 feature; `--cref` is legacy V6/Niji 6 — [clipdance](https://clipdance.ai/blog/midjourney-v8-character-consistency) **[secondary]**

**Runway**
- Gen-4 Image API (with References): `gen4_image` 5 credits (720p) / 8 credits (1080p); `gen4_image_turbo` 2 credits; API credit = $0.01 → $0.05 / $0.08 / $0.02 per image — [Runway API pricing docs](https://docs.dev.runwayml.com/guides/pricing); launch announcement (May 2025) — [Runway news](https://runwayml.com/news/introducing-runway-api-for-gen-4-images)

**Recraft**
- V3 raster $0.04/image, vector $0.08/image; API units $1 = 1,000 units — [Recraft API pricing](https://www.recraft.ai/docs/api-reference/pricing); V4.1 Flash raster $0.007/image — [usagepricing tracker, 2026-10-05](https://www.usagepricing.com/blueprint/activity/recraft-2026-10-05-v41-flash-api-model) **[UNVERIFIED]**

**Microsoft MAI-Image**
- MAI-Image-2.6-Preview #1 on AA Image Editing (Elo 1,284, 13,492 samples) — [Artificial Analysis on X](https://x.com/ArtificialAnlys/status/2092284543705456991?lang=en); MAI-Image-2.7-Preview reportedly has no API — [OrcaRouter](https://www.orcarouter.ai/blog/mai-image-2-7-preview-vs-gpt-image-2-5) **[UNVERIFIED]**

### Inferences
- Cheapest viable reference-based "panel renderer" APIs for a CPU-only container: Nano Banana 2.1 ($0.0336 at 1K, $0.0168 batch, 4 character refs), FLUX 3 Klein API (~$0.009), Seedream 5.0 Flash/Lite ($0.018–$0.035), gpt-image-2 low/medium ($0.005–$0.053). For a 20-page chapter at ~5 panels/page plus ~2× retries (~200 images) this is roughly $2–$11 at those tiers (arithmetic from the cited prices).
- Monochrome manga look must be requested via prompt/style references on these APIs; none of the docs read advertise manga/screentone support specifically.
- Nano Banana outputs carry SynthID watermarks; OpenAI provides `moderation: low`. Both are hosted with content filters — fan-service/violence-heavy manga may be blocked.

### Gaps
- Exact GPT Image 2.5 per-image prices by quality (only token rates are official); rate limits for OpenAI and Gemini image models not retrieved.
- Official BytePlus Seedream prices, Leonardo API pricing/character-reference features, and Ideogram official price table could not be retrieved.
- Commercial-use/output-ownership terms for each provider's ToS were not read in this pass (OpenAI, Google, BFL, Ideogram, Runway, Recraft, ByteDance).
- No public rate-limit figures except Ideogram (10 in-flight).

---

## Q4. Pose/composition control for panels; two distinct characters in one panel without attribute bleeding

### Takeaway
For SDXL anime bases, use Illustrious/NoobAI-specific ControlNets (NoobAI official set includes lineart-anime, **manga line**, depth, normal, softedge, tile + openpose), since generic SDXL ControlNets often fail on Illustrious; for multi-character panels, regional prompting (Attention Couple / masked conditioning) plus per-character LoRAs reduces but does not eliminate bleeding, and a robust workaround is to generate characters separately and composite/inpaint. Newer models add native layout control (FLUX 3 Klein bounding boxes, Qwen-Image-2.1 masked/annotated local edits); on CPU, stable-diffusion.cpp supports ControlNet only for SD1.5.

### Cited Findings
- NoobAI SDXL ControlNets (Eugeoter, curated by Laxhar): lineart anime, lineart realistic, **manga line**, depth, depth_midas, normal, softedge, tile, plus Laxhar openpose; designed for the epsilon-prediction variant — [HF Laxhar NoobAI-SDXL-controlnet collection](https://huggingface.co/collections/Laxhar/noobai-sdxl-controlnet); [X post on release](https://x.com/studiomasakaki/status/1858868389013545370)
- Illustrious-specific openpose: `deepsea001/controlnet-openpose-illustrious-xl` (notes many such checkpoints are experimental) — [HF](https://huggingface.co/deepsea001/controlnet-openpose-illustrious-xl); NoobAI openpose works on Illustrious-based WAI checkpoint with a pose editor — [user report on X](https://x.com/A2yanagid/status/1899044285108129939)
- Generic SDXL lineart ControlNet did not work with Illustrious; Krita AI Diffusion added Illustrious/NoobAI ControlNet support — [GitHub Acly/krita-ai-diffusion #1418](https://github.com/Acly/krita-ai-diffusion/issues/1418); "it might be necessary to use a proprietary ControlNet" for Illustrious/NoobAI — [note.com/kazuya_bros](https://note.com/kazuya_bros/n/n84fa6fe9360b?hl=en)
- Regional prompting: Attention Couple (laksjdjf port) takes base mask + per-region conditioning/masks; masks must cover the whole canvas — [comfy.icu Attention Couple](https://comfy.icu/node/AttentionCouple-cgem156); [comfy.icu Load Attention couple](https://comfy.icu/node/Attention-couple); prompt-syntax couple in comfyui-prompt-control — [comfy.icu AttentionCouplePPM](https://comfy.icu/node/AttentionCouplePPM); region masks must match image or latent (8× smaller) size — [comfy.icu Define Region](https://comfy.icu/node/ETN_DefineRegion)
- Limits: masks do not strictly confine content; characters can spill and blend at edges — [note.com/higana_yogana](https://note.com/higana_yogana/n/n4d22434a49f2?hl=en); lowering background strength reduces but doesn't remove bleed — [Easton Dev, 2026-08-28](https://eastondev.com/blog/en/posts/ai/20260828-comfyui-regional-prompting-multi-subject/)
- FLUX 3 Image Klein supports bounding-box layout prompts — [HF](https://huggingface.co/black-forest-labs/flux-3-image-klein); Qwen-Image-2.1 supports local edits via circles, painted annotations, or masks — [HF](https://huggingface.co/Qwen/Qwen-Image-2.1)
- DiffSensei uses masked cross-attention to place characters per panel layout — [arXiv 2412.07589](https://arxiv.org/abs/2412.07589v1); MangaFlow makes layout and references explicit editable intermediates — [arXiv 2605.28173](https://arxiv.org/abs/2605.28173)
- API side: pass only the references for characters in that panel to avoid attribute-binding blur — [tech-insider](https://tech-insider.org/ai-comic-generator-character-consistency-2026/) **[secondary]**
- stable-diffusion.cpp: ControlNet supported for SD1.5 only; IP-Adapter for SD1.5 and SDXL; PhotoMaker supported — [GitHub](https://github.com/leejet/stable-diffusion.cpp)

### Inferences
- Practical multi-character recipe (local): OpenPose of both figures (pose editor) + Attention Couple with left/right masks, each region carrying its own character LoRA trigger and outfit tags, then inpaint each face with only that character's LoRA (ADetailer-style; sd.cpp lists ADetailer). Alternatively, render each character alone and composite in panel layout (also simpler on CPU).
- On the CPU container, pose ControlNet for SDXL is not available in stable-diffusion.cpp; would require diffusers/ComfyUI on CPU (much slower) or using SD1.5 anime models with ControlNet.

### Gaps
- No quantitative measurement of bleeding reduction for Attention Couple vs. alternatives (one guide's 91% vs 68% figures lack a source — [Apatero](https://apatero.com/blog/regional-prompter-comfyui-complete-guide-2025) — not used).
- No source on whether a ControlNet Union model exists for NoobAI/Illustrious; v-pred-compatible ControlNets not confirmed.
- File sizes of NoobAI ControlNets not retrieved.

---

## Q5. Benchmarks / head-to-head comparisons relevant to anime/manga style or character consistency

### Takeaway
No public leaderboard isolates anime/manga style or cross-panel character consistency; general Artificial Analysis (AA) arenas show OpenAI GPT Image 2/2.5 leading text-to-image, Microsoft MAI-Image-2.6-Preview leading image editing, and Bria Fibo 2.0 / Qwen-Image-2.1 / FLUX 3 Klein leading open-weight editing (Oct 2026). Academic consistency benchmarks (OmniContext, ConsiStory+, DiffSensei's MangaZero, MangaFlow's meta-benchmark) exist but are not anime-specific leaderboards.

### Cited Findings
- **AA-Image-T2I v2.1**: GPT Image 2.5 Sunburst (max) 1222, GPT Image 2.5 Flare (max) 1207, GPT Image 2 (high) 1186, Nano Banana 2.1 1176, MAI-Image-2.6 1166 — [AA T2I leaderboard](https://artificialanalysis.ai/image/leaderboard/text-to-image) (via search snippet; scores not comparable across versions)
- Earlier AA T2I arena snapshot: GPT Image 2 (high) 1369, Reve 2.1 1324, Nano Banana 2 1317, GPT Image 1.5 (high) 1312, MAI-Image-2.5 1307 — [AA T2I open-weights view](https://artificialanalysis.ai/image/leaderboard/text-to-image?open-weights=true) (search snippet); GPT Image 2 (high) debuted at #1 — [AA on X](https://x.com/ArtificialAnlys/status/2047184062012706980)
- AA expanded T2I arena categories "from UI/UX Design to Live-Action Film, and from Physics to Text Rendering" — [AA on X](https://x.com/ArtificialAnlys/status/2085774161138635016); editing arena rebuilt into 17 task leaderboards incl. "Identity-Preserving Edits" — [AA on X](https://x.com/ArtificialAnlys/status/2095245450899239072); [AlphaSignal](https://alphasignal.ai/news/artificial-analysis-rebuilds-its-image-editing-arena-across-17-specialized)
- Image editing overall: MAI-Image-2.6-Preview #1 (Elo 1,284, 13,492 samples), only 25 pts above #5; GPT Image 2 (high) #4 at 1,259 but leads Object-Level Edit and Composition & Framing — [AA on X](https://x.com/ArtificialAnlys/status/2092284543705456991?lang=en); [Superpower Daily](https://superpowerdaily.com/posts/artificial-analysis-rebuilds-image-editing-arena-with-different-leaders-by-task)
- **AA-Image-Editing v2.1 open weights** (Elo, release, API $/1k images): 1 Bria Fibo 2.0 1088 (Oct 2026, $32); 2 Qwen-Image-2.1 1081 (Sep 2026, no API); 3 FLUX 3 Image Klein 1072 (Oct 2026, $9); 4 HunyuanImage 3.0 Instruct 1063 (Jan 2026); 5 FLUX.2 [dev] Turbo (fal) 1019; 6 FLUX.2 [klein] 9B 1015 ($17); 7 FLUX.2 [dev] Flash 1012 ($5); 8 FLUX.2 [dev] 1000 (anchor, $24); 9 Qwen Image Edit Plus 2511 991 ($60); 10 Qwen Image Edit Plus 2509 965 ($30) — [AA open-weights editing](https://artificialanalysis.ai/image/leaderboard/editing/open-weights)
- Open-weights T2I leader reported as Qwen-Image-2.1 (Elo 1035) in one snapshot, Ideogram 4.0 (Quality) (1211) in another — [AA T2I open-weights](https://artificialanalysis.ai/image/leaderboard/text-to-image?open-weights=true) **[conflicting cached snapshots]**; stable-diffusion.cpp also lists "Ideogram4" as a supported model — [GitHub](https://github.com/leejet/stable-diffusion.cpp) **[implies open weights; UNVERIFIED]**
- OmniContext (OmniGen2): subject consistency on single-subject tasks — OmniGen2 8.68, UNO 6.48, InfiniteYou 5.15 (overall 8.19 / 6.60 / 6.05); includes animation stills — [arXiv 2506.18871](https://arxiv.org/html/2506.18871)
- DiffSensei reports gains over baselines in quality, character consistency and layout fit on MangaZero — [CVPR 2025 poster](https://cvpr.thecvf.com/virtual/2025/poster/35070); [arXiv](https://arxiv.org/pdf/2412.07589)
- MangaFlow reports improved layout adherence and cross-panel consistency vs direct generation baselines (no numbers on abstract) — [arXiv 2605.28173](https://arxiv.org/abs/2605.28173); SyntheticManga reports on ConsiStory+ — [CVF](https://openaccess.thecvf.com/content/CVPR2026F/papers/Peng_SyntheticManga_Training-Free_Manga_Generation_with_Phased_Diffusion_CVPRF_2026_paper.pdf) (snippet only)

### Inferences
- For a manga pipeline, general leaderboards are a weak proxy: GPT Image 2/2.5 and Nano Banana lead generic quality, but anime-tag fidelity and screentone style are better served by SDXL anime checkpoints that do not appear on AA boards at all.
- For identity-preserving reference editing (the core of panel-to-panel consistency), the AA open-weights editing board suggests FLUX 3 Klein and Qwen-Image-2.1 are the strongest open models as of Oct 2026, both with 10-reference input, but both have restricted licenses; FLUX.2 klein 4B (Apache) was not in the top-10 table shown.

### Gaps
- No anime- or manga-specific leaderboard or community blind test found; AA's category list (as read) does not confirm an "Anime" category.
- AA leaderboard scores came from cached/snippet views with inconsistent dates; live values should be re-checked.
- No published benchmark comparing commercial APIs on multi-panel character consistency.
