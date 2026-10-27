# CPU-only manga pipeline: local CPU inference vs hosted image APIs (this container, as of 2026-10-27)

Scope: what is practical to install and run in **this** container: Ubuntu 24.04.5, glibc 2.39, no GPU, 4 vCPU, 15 GB RAM, ~31 GB free disk, Python 3.13.17 with system pip 24.0, uv 0.11.32, Node 22.22, and an HTTPS egress proxy. Every in-container check was run on 2026-10-27 and is labelled "(in-container check)". Prices are dated to when the page was read (2026-10-27) unless the page gave its own date.

**How to read the sources.** Many vendor pages were read through a summarising fetcher. Where a figure came only from that summary and I could not check it against a second source, I say so. Model names that appeared after my training cutoff (for example "gpt-image-2.5-flare" and "gemini-nano-banana-2.1") are reported exactly as the vendor pages gave them.

---

## 1. Local CPU inference options and realistic speeds

### Takeaway
The only fast setups on a 4-core CPU are few-step distilled models: LCM, SDXL-Turbo, Hyper-SD, SDXL-Lightning, SDXS and FLUX.2/3 Klein. Run them through OpenVINO (FastSD CPU, or OpenVINO GenAI/optimum-intel) or through stable-diffusion.cpp with GGUF weights, and use the TAESD/TAESDXL tiny decoder.
- **Published speeds** (12-core i7-12700): roughly 1–13 s per image at 512–768 px.
- **Estimate for this 4-core VM:** a few times slower. An anime SDXL checkpoint (Illustrious, NoobAI or Animagine) at 1024 px with 4–8 steps will probably take minutes per panel. This figure is my inference, not a measurement.
- **Comparison:** hosted APIs cost about $0.005–$0.07 per image and take seconds.
- **FLUX.1-class models do not fit in 15 GB RAM.** FastSD says ~30 GB for FLUX.1 schnell.

### Cited Findings

**Environment facts (in-container checks, 2026-10-27)**
- The CPU is "Intel(R) Xeon(R) Processor @ 2.10GHz" (model 207), with 4 cores, 1 thread per core, a KVM hypervisor and 260 MiB L3. Its flags include `avx512f/bw/vl/vnni/bf16/fp16`, `avx_vnni`, `amx_bf16`, `amx_int8` and `amx_tile`. That means bf16/int8 AMX acceleration paths in OpenVINO, ggml and PyTorch are usable in principle. — (in-container check: `lscpu`, `/proc/cpuinfo`)
- The build toolchain is present: cmake, gcc/g++ 13.3.0, make and ninja. — (in-container check)
- **GitHub through the proxy:**
  - `git ls-remote`/clone over HTTPS works for public repos, and so does `raw.githubusercontent.com`.
  - `github.com/<repo>/releases/latest` pages, `codeload.github.com` tarballs and the GitHub REST/GraphQL API return **HTTP 403**: "GitHub access to this repository is not enabled for this session. Use add_repo to request access."
  - So **prebuilt release binaries (for example sd.cpp's) may not be downloadable** unless the repo is attached with `add_repo`.
  - — (in-container check against https://github.com/leejet/stable-diffusion.cpp/releases/latest)
- **Building third-party C++ in this session needs permission.** My attempt to `git clone` and `cmake --build` stable-diffusion.cpp in the scratchpad was **denied by the session's auto-mode permission classifier** ("Code from External"), so no local benchmark could be run. Any plan that compiles sd.cpp, including `pip install stable-diffusion-cpp-python`, which builds from an sdist, will need the user's explicit permission in this environment. — (in-container check)
- **Hugging Face downloads work.** Model API, `resolve/` and the Xet CDN (`us.aws.cdn.hf.co`) are all reachable; a 1 MB range request on an SDXL file returned HTTP 206. — (in-container check against https://huggingface.co/stabilityai/sdxl-turbo)

**stable-diffusion.cpp (ggml, GGUF)**
- Supported image families: SD1.x/2.x/SDXL, SD3/3.5, FLUX.1 and FLUX.2, Chroma, Qwen-Image and Z-Image. Image-edit models include FLUX.1-Kontext-dev and Qwen Image Edit. — [sd.cpp README](https://github.com/leejet/stable-diffusion.cpp)
- CPU backend: "CPU (AVX, AVX2 and AVX512 support for x86 architectures)". The project also has LoRA ("same as stable-diffusion-webui"), "Control Net support with SD 1.5", PhotoMaker, "Latent Consistency Models support (LCM/LCM-LoRA)", and "Faster and memory efficient latent decoding with TAESD". — [sd.cpp README](https://github.com/leejet/stable-diffusion.cpp)
- In late 2026 the docs folder lists per-model guides for many newer models, including flux2, flux3, z_image, qwen_image_2.1, ideogram4, anima, iris, lcm, taesd, lora, photo_maker, ip_adapter and edit. — [sd.cpp README (raw)](https://raw.githubusercontent.com/leejet/stable-diffusion.cpp/master/README.md)
- Quantization: `--type` accepts `q8_0`, `q4_0`/`q4_1` and others. Memory for SD1.x txt2img at 512×512 is ~2.8 GB (f32), ~2.3 GB (f16), ~2.1 GB (q8_0) and ~2.0 GB (q4_0). With flash attention it is ~1.9 GB (f16) and ~1.6 GB (q8_0). Conversion uses `sd-cli -M convert ... --type q8_0`. — [sd.cpp quantization_and_gguf.md](https://raw.githubusercontent.com/leejet/stable-diffusion.cpp/master/docs/quantization_and_gguf.md)
- Performance knobs: `--flash-attn` saves memory (e.g. "SD2 768x768 ~1400mb"); `--vae-tiling` cuts VAE memory; batched CFG is on by default for UNet models. **The performance doc gives no CPU seconds-per-image figures.** — [sd.cpp performance.md](https://raw.githubusercontent.com/leejet/stable-diffusion.cpp/master/docs/performance.md)
- A CPU-only build is a plain cmake build. An optional `-DGGML_OPENBLAS=ON` build is also documented. — [sd.cpp build.md](https://raw.githubusercontent.com/leejet/stable-diffusion.cpp/master/docs/build.md)
- Python binding: `pip install stable-diffusion-cpp-python` "will also build `stable-diffusion.cpp` from source". Cmake options go through `CMAKE_ARGS` or `-C cmake.args=...`. It supports Python 3.8+. — [stable-diffusion-cpp-python README](https://raw.githubusercontent.com/william-murray1204/stable-diffusion-cpp-python/main/README.md)
- PyPI has **stable-diffusion-cpp-python 0.4.7 (uploaded 2026-05-12) as a 20.6 MB sdist only, with no wheels**, so it always compiles. — [PyPI JSON](https://pypi.org/pypi/stable-diffusion-cpp-python/json) (in-container check)

**FastSD CPU (rupeshs/fastsdcpu; OpenVINO + PyTorch)**
- Linux install: clone, then `chmod +x install.sh; ./install.sh`, then `./start.sh` (GUI) or `./start-webui.sh`. The README asks for "Python 3.10 and uv". — [FastSD CPU README](https://github.com/rupeshs/fastsdcpu)
- Supported models: LCM, LCM-LoRA (SD1.5/SDXL/SSD-1B), OpenVINO LCM models, SDXS-512, SD Turbo/SDXL Turbo, Hyper-SD (1-step), SDXL-Lightning (2-step), FLUX.1-schnell OpenVINO int4, Iris 3B Turbo, FLUX.3 Image Klein OpenVINO (2–4 steps; t2i and edit), FLUX.2-klein-4B OpenVINO (edit), and GGUF Flux 2 Klein. **The README names no dedicated anime model.** — [FastSD CPU README](https://github.com/rupeshs/fastsdcpu)

Published FastSD CPU benchmarks. All are from the README, on a Core i7-12700 (12 cores / 20 threads, desktop).

| Model | Resolution, steps | PyTorch | OpenVINO | OpenVINO + tiny decoder |
|---|---|---|---|---|
| SDXS-512-0.9 | 512, 1 step | 4.8 s | 3.8 s | **0.82 s** (TAESD) |
| SD Turbo | 512, 1 step | 7.8 s | 5 s | 1.7 s |
| SDXL Turbo | 512, 1 step | 10 s | 5.6 s | 2.5 s (TAESDXL) |
| Hyper-SD (SDXL) | 768, 1 step | 19 s | 13 s | 6.3 s |
| SDXL-Lightning | 768, 2 steps | 18 s | 12 s | 10 s |
| FLUX.1-schnell | 512, 3 steps | – | **4 min 30 s** | – |
| Iris 3B Turbo | 1024, 4 steps | – | ~90 s | – |
| FLUX.3 Image Klein | 512, 4 steps | – | ~36 s t2i; ~72 s with 1 reference image (edit) | – |

Source: [FastSD CPU README](https://github.com/rupeshs/fastsdcpu)

- FastSD CPU RAM minimums:
  - LCM 2 GB; LCM-LoRA 4 GB; OpenVINO (Flux2) 8 GB; Iris 3B at 1024 8.4 GB.
  - The tiny decoder saves ~2 GB, so OpenVINO mode needs ~9 GB with it on.
  - FLUX.1 schnell at 512 needs "around 30GB system RAM", which is **over this box's 15 GB**.
  - FLUX.3 Image Klein at 512 needs ~8–9 GB.
  - — [FastSD CPU README](https://github.com/rupeshs/fastsdcpu)

**OpenVINO GenAI / optimum-intel**
- The Python API is `ov_genai.Text2ImagePipeline(model_path, "CPU").generate(prompt)`. There are also `Image2ImagePipeline` (with `strength`) and `InpaintingPipeline`, plus LoRA adapters and `get_performance_metrics()`. Export example: `optimum-cli export openvino --model stabilityai/stable-diffusion-xl-base-1.0 --weight-format int4 --trust-remote-code <out_dir>`. The page publishes **no speed numbers**. — [OpenVINO GenAI image generation](https://openvinotoolkit.github.io/openvino.genai/docs/use-cases/image-generation/)
- Supported image architectures:
  - LCM, SD 1.x/2.x and SDXL (all with t2i/i2i/inpaint and LoRA). SDXL examples include `stabilityai/sdxl-turbo`.
  - SD3 (no LoRA), Flux (incl. FLUX.1-schnell), FLUX.2 [klein] (t2i/i2i, LoRA), Qwen-Image / Qwen-Image-2.1 and Z-Image / Z-Image-Turbo.
  - — [OpenVINO GenAI supported models](https://openvinotoolkit.github.io/openvino.genai/docs/supported-models/)
- Older Intel data (Sapphire Rapids r7iz.metal-16xl, SD v1.5, 20 steps, published 2023-03-28):
  - Diffusers fp32 baseline: 32.3 s/image.
  - OpenVINO with dynamic shapes: 16.7 s. With static shape at 512×512: **4.7 s**.
  - IPEX bf16/AMX: 5.4 s; with DPMSolver: 5.05 s.
  - System tuning with 32 cores: 11.8 s.
  - — [HF blog: Accelerating Stable Diffusion Inference on Intel CPUs](https://huggingface.co/blog/stable-diffusion-inference-intel)

**Diffusers / ComfyUI on CPU (generic)**
- An SSD Nodes guide charts "8 vCPU VPS, no GPU" at **~780 s per SDXL 1024×1024, 30-step image** (labelled "typical, July 2026"). It suggests ~16 GB RAM for SDXL and ~8 GB for SD1.5 on CPU. The CPU, software stack and method are not stated, so treat this as order-of-magnitude only. — [SSD Nodes self-hosted AI image generator](https://www.ssdnodes.com/learn/self-hosted-ai-image-generator)
- I found **no first-party ComfyUI `--cpu` benchmark** and no published stable-diffusion.cpp SDXL CPU timing. Search results said so explicitly. — [search summary; localaimaster notes no published CPU timings for Z-Image-Turbo](https://localaimaster.com/blog/image-generation-without-gpu)

**Anime/manga-capable checkpoints and CPU-ready formats (HF Hub API, in-container check 2026-10-27)**

Base checkpoints:

| Repo | Main file | Licence (HF metadata) |
|---|---|---|
| `OnomaAIResearch/Illustrious-XL-v2.0` | single 6.94 GB `.safetensors` | creativeml-openrail-m; not gated |
| `Laxhar/noobai-XL-1.1` | 7.11 GB single file, plus diffusers folders (repo 14.0 GB) | "other"; not gated |
| `cagliostrolab/animagine-xl-4.0` | 6.94 GB `-opt` single file (repo 20.8 GB) | openrail++ |

— [HF API: Illustrious-XL-v2.0](https://huggingface.co/api/models/OnomaAIResearch/Illustrious-XL-v2.0), [HF API: noobai-XL-1.1](https://huggingface.co/api/models/Laxhar/noobai-XL-1.1), [HF API: animagine-xl-4.0](https://huggingface.co/api/models/cagliostrolab/animagine-xl-4.0)

GGUF builds (usable with sd.cpp):

| Repo | Files and sizes | Downloads |
|---|---|---|
| `off-grid-ai/animagine-xl-4.0-GGUF` | Q8_0 4.18 GB, Q4_K 2.8 GB | 5,032 |
| `off-grid-ai/illustrious-xl-v2.0-GGUF` | Q8_0 4.18 GB, Q4_K 2.8 GB | 4,026 |
| `btaskel/noobai-XL-Vpred-1.0-GGUF` | Q8_0 2.76 GB, Q4_K_S 1.49 GB (these look like UNet-only files) | – |
| `BigDannyPt/Illustrious-GGUF-Collection` | collection | 37,011 |

— [HF model search "illustrious gguf"](https://huggingface.co/api/models?search=illustrious%20gguf), [HF API: animagine GGUF](https://huggingface.co/api/models/off-grid-ai/animagine-xl-4.0-GGUF)

OpenVINO builds:
- Anime-specific exports exist but have low adoption:
  - `HelloSun/animagine-xl-4.0-Lightning-OpenVINO-INT4` (6.2 GB repo, 140 downloads)
  - `None1145/noobai-XL-Vpred-0.65s-openvino`
  - `HelloSun/animemixv10_lcm-OpenVINO-INT4` (SD1.5 LCM anime)
  - `hsuwill000/LCM-anything-v5-openvino`
  - — [HF search "animagine openvino"](https://huggingface.co/api/models?search=animagine%20openvino), [HF search "anime openvino"](https://huggingface.co/api/models?search=anime%20openvino)
- FastSD's generic OpenVINO models (each about 4.8 GB repo, int8): `rupeshs/sdxl-turbo-openvino-int8`, `rupeshs/hyper-sd-sdxl-1-step-openvino-int8`, `rupeshs/SDXL-Lightning-2steps-openvino-int8`. Also `rupeshs/LCM-dreamshaper-v7-openvino-int8` (3.1 GB), `rupeshs/flux2-klein-4b-int4-ov` (4.6 GB) and `rupeshs/flux3-image-klein-int4-ov`. — [HF API: rupeshs models](https://huggingface.co/api/models?author=rupeshs)
- Of these OpenVINO repos, **only `rupeshs/flux2-klein-4b-int4-ov` contains `openvino_tokenizer` files**. The SDXL and LCM exports do not. — (in-container check of HF siblings lists)
- Few-step add-ons: `latent-consistency/lcm-lora-sdxl` (0.39 GB LoRA) and `ByteDance/SDXL-Lightning` (UNet/LoRA variants for 1, 2, 4 and 8 steps; full checkpoints 6.94 GB each). — [HF API: lcm-lora-sdxl](https://huggingface.co/api/models/latent-consistency/lcm-lora-sdxl), [HF API: SDXL-Lightning](https://huggingface.co/api/models/ByteDance/SDXL-Lightning)

### Inferences
- **Speed on this box (estimates, not measurements).** The i7-12700 numbers come from a 12-core/20-thread desktop. This VM has 4 cores, but they have AVX-512 and AMX, which recent OpenVINO and ggml can use.
  - On compute-bound steps, expect roughly 2–4× the i7-12700 latency.
  - SDXL-class at 768 px with 1–2 steps via OpenVINO + TAESDXL: probably ~20–60 s per image.
  - SDXL 1024 px: the SSD Nodes figure (~26 s/step on 8 vCPU, unknown stack) suggests something like 20–50 s per UNet step here. A 4–8-step Lightning/LCM/Hyper anime render would then take roughly 2–7 minutes per panel, plus text encoders and VAE.
  - A 20-page chapter at ~5 panels per page is ~100 panels, which works out to several hours of CPU time.
  - **Someone should measure this with a 1-image smoke test before committing.**
- **What fits in RAM.** SDXL anime checkpoints (6.9 GB fp16) fit in 15 GB, especially as Q8_0/Q4_K GGUF (2.8–4.2 GB) or int8 OpenVINO. FLUX.1 does not fit (~30 GB). FLUX.2-klein-4B / FLUX.3 Klein int4 (~8–9 GB) fits and is the only local option with reference-image editing for character consistency, at ~1–2+ minutes per edit here (extrapolated from ~72 s on the i7-12700).
- **Which local engine.**
  - **stable-diffusion.cpp** is the simplest way to run *arbitrary* Illustrious/NoobAI/Animagine checkpoints plus LoRAs on CPU with low RAM: single-file safetensors or GGUF, and LCM/TAESD support. Because of GitHub release and permission limits, the install path here is a source build through PyPI or `git clone` + cmake, and it needs user approval.
  - **OpenVINO/FastSD** has the best published CPU numbers. But anime SDXL models must be exported with optimum-intel, which needs torch, or taken from rare third-party exports. Most SDXL OpenVINO exports lack tokenizer IRs, so they target optimum-intel pipelines rather than GenAI's `Text2ImagePipeline` (unverified).
- **Image quality caveat.** Distilled 1–2-step models and LCM-LoRA on top of anime checkpoints are known to lose detail. Keep this to drafts or thumbnails. This is general knowledge and was not verified in these sources.

### Gaps
- No published benchmark exists for any of these engines on a ~4-core server CPU. ComfyUI `--cpu` and diffusers SDXL CPU per-step figures come only from a vendor blog with an unspecified stack. A local smoke test was blocked by the permission classifier.
- ONNX Runtime for SD on CPU: onnxruntime 1.31.1 ships cp313 wheels (see section 2), but I found no current CPU SD benchmark or maintained anime ONNX checkpoints.
- I did not verify whether `HelloSun/animagine-xl-4.0-Lightning-OpenVINO-INT4` loads in OpenVINO GenAI or optimum-intel 2.2, or whether its quality is acceptable.
- ComfyUI's Python 3.13 compatibility and current release were not checked (GitHub release pages are blocked).

---

## 2. Python 3.13 compatibility and installing CPU-only torch

### Takeaway
Python 3.13 works. As of 2026-10-27 the whole stack has cp313 manylinux_2_28 wheels (glibc 2.39 here satisfies manylinux_2_28): torch 2.14.1 (CPU build), diffusers, transformers, onnxruntime, openvino, openvino-genai, pillow and the API SDKs. A 3.12 venv is not required, but uv can fetch 3.12 if a tool such as FastSD CPU insists. Two rules:
- Install torch from `https://download.pytorch.org/whl/cpu`. That gives a 196 MB CPU wheel. Plain PyPI gives a 554.6 MB wheel plus CUDA 13 dependencies.
- Pin `transformers<5.6` when using optimum-intel.

### Cited Findings
- **torch on PyPI.** Latest is **2.14.1 (uploaded 2026-09-30)**, `requires_python >=3.10`, and it has a `torch-2.14.1-cp313-cp313-manylinux_2_28_x86_64.whl` of **554.6 MB**. — [PyPI JSON: torch](https://pypi.org/pypi/torch/json) (in-container check)
- **The PyPI torch wheel pulls CUDA on Linux.** Its `requires_dist` includes `cuda-toolkit[cublas,cudart,...]==13.0.3; platform_system == "Linux"`, `nvidia-cudnn-cu13==9.24.0.43`, `nvidia-nccl-cu13`, `nvidia-nvshmem-cu13` and others. `nvidia-cudnn-cu13` alone is ~614 MB. — [PyPI JSON: torch 2.14.1](https://pypi.org/pypi/torch/2.14.1/json), [PyPI JSON: nvidia-cudnn-cu13](https://pypi.org/pypi/nvidia-cudnn-cu13/json) (in-container check)
- **CPU torch index.** It lists `torch-2.14.1+cpu-cp313-cp313-manylinux_2_28_x86_64.whl`, as well as cp312, cp314 and cp314t builds and 2.13.x/2.14.0. The cp313 CPU wheel's Content-Length is **196,253,851 bytes (~196 MB)**. — [download.pytorch.org/whl/cpu/torch/](https://download.pytorch.org/whl/cpu/torch/) (in-container check)
- PyTorch's install selector is at the Get Started page (last updated 2026-07-27). The page's install command is JS-rendered and could not be extracted, so the CPU index URL above was verified directly. — [PyTorch Get Started](https://pytorch.org/get-started/locally/)
- **Other cp313 wheels and versions** (PyPI, 2026-10-27, in-container checks):

| Package | Version (upload date) | requires_python | cp313 wheel size |
|---|---|---|---|
| [onnxruntime](https://pypi.org/pypi/onnxruntime/json) | 1.31.1 (2026-10-26) | >=3.11 | 23.8 MB (also cp313t) |
| [openvino](https://pypi.org/pypi/openvino/json) | 2026.4.1 (2026-10-01) | – | 59.1 MB |
| [openvino-genai](https://pypi.org/pypi/openvino-genai/json) | 2026.4.1.0 | – | 6.7 MB |
| [pillow](https://pypi.org/pypi/pillow/json) | 13.0.0 (2026-10-16) | >=3.11 | 7.1 MB |
| diffusers | 0.42.1 | – | – |
| transformers | 5.21.0 | – | – |
| accelerate | 1.15.0 | – | – |
| optimum-intel | 2.2.0 | – | – |
| huggingface_hub | 2.3.0 | – | – |

  The resolver also used `openvino-tokenizers` 2026.4.1.0 (a `py3-none-manylinux_2_28` wheel, 1.9 MB).
- **Full resolution under uv for both Python versions.** `uv pip compile` (no install) resolved this set for both **Python 3.13 and 3.12** on `x86_64-manylinux_2_28`: torch (CPU index), diffusers, transformers, accelerate, safetensors, sentencepiece, peft, optimum-intel[openvino], openvino-genai and onnxruntime. Results were torch 2.14.1+cpu, diffusers 0.42.1, transformers 5.21.0, tokenizers 0.23.3, sentencepiece 0.2.2, numpy 2.5.4, openvino 2026.4.1 and onnxruntime 1.31.1. **The approximate total wheel download is ~470 MB.** — (in-container check; index [pypi.org/simple](https://pypi.org/simple) + [download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu))
- **The optimum-intel resolver trap.** optimum-intel 2.2.0 requires `transformers<5.6,>=4.51` and `optimum~=2.3.0`. With transformers left unpinned, uv backtracked to **optimum-intel 1.15.0 (uploaded 2024-02-16)**. Pinning `optimum-intel[openvino]>=2.2` plus `transformers<5.6` resolves to optimum-intel 2.2.0, transformers 5.5.4, diffusers 0.39.0, nncf 3.4.0, torch 2.14.1+cpu and torchvision 0.29.1+cpu. — [PyPI JSON: optimum-intel 2.2.0](https://pypi.org/pypi/optimum-intel/2.2.0/json), [PyPI JSON: optimum-intel 1.15.0](https://pypi.org/pypi/optimum-intel/1.15.0/json) (in-container check)
- **uv and Python 3.12.** uv 0.11.32 is installed at `/root/.local/bin/uv`. It downloads Python from `releases.astral.sh`, which is reachable through the proxy (HTTP 200/206 for `cpython-3.12.13+20260718-x86_64-unknown-linux-gnu-install_only_stripped.tar.gz`). So `uv venv --python 3.12` works here without touching GitHub. — [releases.astral.sh python-build-standalone 3.12.13](https://releases.astral.sh/github/python-build-standalone/releases/download/20260718/cpython-3.12.13%2B20260718-x86_64-unknown-linux-gnu-install_only_stripped.tar.gz) (in-container check)
- **Proxy bypass list.** The proxy's NO_PROXY includes `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` and `api.anthropic.com`, so these connect directly. — (in-container check: `$HTTPS_PROXY/__agentproxy/status`)
- System pip is 24.0 from Debian (`/usr/lib/python3/dist-packages/pip`), and system Pillow 12.3.0 is already present. — (in-container check)
- FastSD CPU's README asks for "Python 3.10 and uv" on Linux. — [FastSD CPU README](https://github.com/rupeshs/fastsdcpu)

### Inferences
- Use a **uv-managed venv on the system Python 3.13**: `uv venv .venv --python 3.13`. This avoids Ubuntu's externally-managed system pip, and every wheel needed exists for cp313.
- Use Python 3.12 only for FastSD CPU's own `install.sh`, or if a niche package without cp313 wheels turns up.
- Always pass `--index-url https://download.pytorch.org/whl/cpu`, or `--extra-index-url` plus `--index-strategy unsafe-best-match` in uv, so torch resolves to the `+cpu` build. Otherwise ~2+ GB of CUDA wheels arrive.

### Gaps
- I did not test runtime behaviour on 3.13, such as import-time errors in diffusers or optimum-intel. Only wheel availability and dependency resolution were verified.
- Some transitive packages (e.g. `multiprocess`) were not individually checked for cp313-specific wheels. They resolved, and are pure-python or universal.

---

## 3. Hosted image APIs callable from Python

### Takeaway
For manga panels with recurring characters:
- **Gemini image models** are the best documented for multi-reference consistency: up to 14 inputs, including up to 5 "character" images on Nano Banana 2 / 2.1. Prices run ~$0.034–$0.067 per 1K image, half that in batch.
- **FLUX.2** (BFL, also on Together, fal and Replicate) takes up to 10 references at ~$0.03 per image on Together.
- **OpenAI GPT Image 2** takes multi-image edits at $0.006 (low) to $0.211 (high) per 1024² image.
- **Anime-specific checkpoints** (Illustrious, NoobAI, Animagine) are only clearly available as community models on **Replicate**, or via **fal-ai/lora**, which takes any HF/URL base model.

All the main hosts are reachable from this container.

### Cited Findings

**Reachability (in-container check, 2026-10-27).** Through the proxy, HTTPS reached `api.anthropic.com`, `api.openai.com`, `generativelanguage.googleapis.com`, `api.bfl.ai`, `api.replicate.com`, `fal.run`, `queue.fal.run`, `api.together.xyz`, `router.huggingface.co`, `api.stability.ai`, `api.ideogram.ai`, `api.novita.ai`, `api.runware.ai` and `civitai.com`. They answered with application-level codes (200/302/307/404/421), not proxy 403s. — (in-container `curl` check)

**SDK packages and env vars** (PyPI, 2026-10-27, from package metadata and README):

| Package | Version (date) | Python | Auth env var | Call shown in README |
|---|---|---|---|---|
| [openai](https://pypi.org/pypi/openai/json) | 3.40.0 (2026-10-27) | >=3.10 | `OPENAI_API_KEY` | `client.images.generate` / `client.images.edit` (per [OpenAI image guide](https://developers.openai.com/api/docs/guides/image-generation)) |
| [google-genai](https://pypi.org/pypi/google-genai/json) | 2.33.0 (2026-10-23) | >=3.10 | `GEMINI_API_KEY` or `GOOGLE_API_KEY` | `client.models.generate_content`, `client.interactions.create` (the image-gen guide's examples use `client.interactions.create`) |
| [fal-client](https://pypi.org/pypi/fal-client/json) | 1.0.3 (2026-09-21) | – | `FAL_KEY` | `fal_client.run` / `run_async` / queue status classes |
| [replicate](https://pypi.org/pypi/replicate/json) | 1.0.7 (2025-05-27) | – | `REPLICATE_API_TOKEN` | `replicate.run` |
| [together](https://pypi.org/pypi/together/json) | 3.0.0 (2026-10-22) | – | `TOGETHER_API_KEY` | – |
| [runware](https://pypi.org/pypi/runware/json) | 0.5.24 (2026-06-30) | – | `RUNWARE_API_KEY` | `imageInference` |
| [huggingface_hub](https://pypi.org/pypi/huggingface_hub/json) | 2.3.0 (2026-10-23) | – | `HF_TOKEN` | – |
| [anthropic](https://pypi.org/pypi/anthropic/json) | 2.3.0 (2026-10-23) | >=3.10 | `ANTHROPIC_API_KEY` | – |

BFL has no official SDK in these notes. Its REST API uses header `x-key` and env var `BFL_API_KEY` ([BFL Kontext docs](https://docs.bfl.ai/kontext/kontext_image_editing)).

**Google Gemini API (Nano Banana family)**

Prices, from the [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) page (which says "Last updated 2026-10-27 UTC"):

| Model | Model ID | Standard price per image | Batch price |
|---|---|---|---|
| Nano Banana 2.1 | `gemini-nano-banana-2.1` | 1K $0.0336, 2K $0.0504, 4K $0.113 | 1K $0.0168 |
| Gemini 3.1 Flash Image (Nano Banana 2) | `gemini-3.1-flash-image` | 0.5K $0.045, 1K $0.067, 2K $0.101, 4K $0.151 | 1K $0.034 |
| Gemini 3.1 Flash Lite Image | `gemini-3.1-flash-lite-image` | 1K only, $0.0336 | – |
| Gemini 3 Pro Image (Nano Banana Pro) | `gemini-3-pro-image` | 1K/2K $0.134, 4K $0.24 | – |
| Gemini 2.5 Flash Image | `gemini-2.5-flash-image` | $0.039 | – |

- `gemini-2.5-flash-image` is marked deprecated with **shutdown October 2, 2026**.
- **No free tier for image output** on any of these models.

Reference images and other details, from the [Gemini image generation guide](https://ai.google.dev/gemini-api/docs/image-generation):
- Up to **14 mixed reference images** per request.
- Nano Banana 2.1 and 3.1 Flash Image: up to 10 object images plus **up to 5 character images**.
- Flash Lite: 14 object + 4 character.
- Pro: 6 object + 3 style, with **no character-consistency images**.
- Every output carries a SynthID watermark, and use is subject to Google's Prohibited Use Policy.
- Pro supports interleaved text+illustration (e.g. illustrated stories) and multi-turn editing.

Rate limits, from [Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) (last updated 2026-10-26 UTC):
- RPM/RPD/IPM for image models are shown only in AI Studio.
- There is a spend-based cap per rolling 10 minutes: Free N/A; Tier 1 $10 (needs linked billing); Tier 2 $50 ($100 paid + 3 days); Tier 3 $200 ($1,000 paid + 30 days).

**OpenAI Images**

Per-image output prices, from the [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation):

| Model | Quality | 1024×1024 | 1024×1536 |
|---|---|---|---|
| GPT Image 2 | low | $0.006 | $0.005 |
| GPT Image 2 | medium | $0.053 | $0.041 |
| GPT Image 2 | high | $0.211 | $0.165 |
| GPT Image 1.5 | low / medium / high | $0.009 / $0.034 / $0.133 | – |
| GPT Image 1 Mini | low / medium / high | $0.005 / $0.011 / $0.036 | – |

- The guide says **`gpt-image-1` was shut down October 23, 2026**.

Token pricing, from [OpenAI pricing](https://developers.openai.com/api/docs/pricing):
- Image tokens cost $8/M input and $30/M output for gpt-image-2 and the 2.5 models; gpt-image-1.5 output is $32/M.
- The page lists `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare` at the same per-token rates as gpt-image-2, with batch at half price.
- Data residency adds a 10% uplift for models released on or after 2026-03-05.

Features and limits, from the [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation):
- `client.images.edit` accepts **multiple reference images** (the example uses 4; no maximum stated). gpt-image-2 always processes inputs at high fidelity.
- `moderation` takes `auto` (default) or `low` ("less restrictive filtering"). Blocked requests raise `moderation_blocked` with categories and stage (input/output).
- **API Organization Verification** may be required.
- Sizes: 1024², 1536×1024, 1024×1536, or custom multiples of 16 within a 1:3–3:1 aspect ratio and up to 3840 px per edge.

**Black Forest Labs (FLUX) direct API**
- `POST https://api.bfl.ai/v1/flux-kontext-pro`, header `x-key`, env `BFL_API_KEY`. It takes one `input_image` (≤20 MB / 20 MP), `safety_tolerance` from 0 (strict) to 6 (permissive) with default 2, jpeg/png output and aspect ratios from 3:7 to 7:3 at ~1 MP. You poll `polling_url`, and result URLs are valid for 10 minutes.
- The docs call **FLUX.2** "multi-reference support (up to 10 images)", with output up to 4 MP, and recommend it over Kontext, which they describe as previous-generation.
- — [BFL Kontext docs](https://docs.bfl.ai/kontext/kontext_image_editing)
- **Per-model prices were not captured.** The docs say "1 credit = $0.01", but the dollar figures did not render. The bfl.ai calculator shows a default "$0.048 per image" without naming the model. Its model list includes FLUX 3 Image, FLUX 3 Image Klein, FLUX.2 [flex/pro/max/klein 4B/9B]. — [BFL pricing docs](https://docs.bfl.ai/quick_start/pricing), [bfl.ai/pricing](https://bfl.ai/pricing)

**Together AI**

Prices from [Together pricing](https://www.together.ai/pricing), which gives no dates:

| Model | Price |
|---|---|
| GPT Image 2 | $0.053/image |
| GPT Image 1.5 | $0.034/image |
| Nano Banana 2 | $0.05/image |
| Nano Banana Pro | $0.134/image |
| Gemini Flash Image 2.5 | $0.039/image |
| FLUX.2 [pro] / [flex] | $0.03/image |
| FLUX.2 [dev] | $0.0154/image |
| FLUX.2 [max] | $0.070/MP |
| FLUX.1 Kontext [pro] / [max] | $0.04 / $0.08 per MP |
| Qwen Image | $0.0058/MP |
| Seedream 4.0 | $0.03/MP |
| Ideogram 4.0 | $0.06/image |
| **SD XL** | **$0.0019/MP** |

No custom checkpoints are mentioned.

**fal.ai**
- Prices (no dates on the page): Nano Banana 2 $0.08/image, Nano Banana Pro $0.15, Nano Banana $0.0398, Z-Image Turbo $0.005/MP, FLUX.1 [schnell] $0.003/MP. "GPT Image 2" is listed as "$1 per units" with no clear basis. — [fal pricing](https://fal.ai/pricing)
- The **`fal-ai/lora`** endpoint takes `model_name` = "URL or HuggingFace ID of the base model". In principle that lets an Illustrious, NoobAI or Animagine HF repo serve as the base. It also takes `loras`, `ip_adapter`, `controlnets`, a single embedding, and schedulers including LCM/TCD/Euler A. Auth is `FAL_KEY`. Its price is not on the page. — [fal-ai/lora API](https://fal.ai/models/fal-ai/lora/api)

**Replicate**
- Most public models are billed per second of hardware: CPU $0.0001/s, T4 $0.000225/s, L40S $0.000975/s, H100 $0.001525/s ($5.49/h). Official models are billed per output: FLUX 1.1 Pro $0.04, FLUX Dev $0.025, FLUX Schnell $3.00 per 1,000 images, Ideogram v3 Quality $0.09. — [Replicate pricing](https://replicate.com/pricing)
- Community anime model **`delta-lock/noobai-xl`** ("Models fine-tuned from NoobAI-XL/Illustrious-XL series") runs on an H100 at about **$0.097 per run (~10 runs per $1)**. — [Replicate: delta-lock/noobai-xl](https://replicate.com/delta-lock/noobai-xl)
  - Typical prediction time conflicts between sources: "within 64 seconds" on the fetched page versus "within 8 seconds" in a search snippet of the same page.
  - Other Illustrious/NoobAI community models exist, e.g. `aisha-ai-official/fasercore-illustrious-v1` and `aisha-ai-official/noobai-real-sdxl-v0.1`. — [Replicate: fasercore-illustrious](https://replicate.com/aisha-ai-official/fasercore-illustrious-v1/readme), [Replicate: noobai-real-sdxl](https://replicate.com/aisha-ai-official/noobai-real-sdxl-v0.1/examples)

**Runware**
- Prices: FLUX 3 Image Klein $0.003 (512², 16 steps), FLUX 3 Image $0.041 (0.75K), Ideogram 4.5 $0.008 (very low), Qwen-Image-2.1-Turbo $0.014133, Seedream 5.0 Flash $0.01926. The page says pricing "varies across thousands of parameters". — [Runware pricing](https://www.runware.ai/pricing)
- The SDK is `runware` (`RUNWARE_API_KEY`, `imageInference`). — [PyPI: runware](https://pypi.org/pypi/runware/json)
- Whether Runware accepts arbitrary Civitai/AIR model IDs (e.g. Illustrious finetunes) is **unverified**: the docs URL returned 404.

**Stability AI**
- 1 credit = $0.01, with 25 free credits for new accounts. Generation: Stable Image Ultra $0.08, SD 3.5 Large $0.065, Large Turbo $0.04, Medium $0.035, Flash $0.025, Stable Image Core $0.03, SDXL 1.0 from $0.009. Control/style: Structure, Sketch and Style Guide $0.05 each; Style Transfer $0.08. Inpaint $0.05, Outpaint $0.04. Creative upscale costs 60 credits. No date on the page. — [Stability pricing](https://docs.stability.ai/pricing)

**Hugging Face Inference Providers**
- Billing is pass-through ("no markup"). Free users get **no** monthly credits and must buy credits. PRO users get $2.00/month, and Team/Enterprise orgs get $2.00 per seat. Calls route via `router.huggingface.co` with `HF_TOKEN` and `InferenceClient`. hf-inference itself "focuses mostly on CPU inference" as of July 2025. — [HF Inference Providers pricing](https://huggingface.co/docs/inference-providers/pricing)

**Ideogram and Novita**
- **Ideogram:** API prices did not render ("Loading current prices"). The page lists models Ideogram 4.5, 4.0, 3.0 and Vector. Character consistency is mentioned only for app subscription plans. — [Ideogram API pricing](http://ideogram.ai/pricing/?pricing_tab=api)
- Ideogram prices seen on resellers: Ideogram 4.5 $0.008 at very-low quality on Runware ([Runware pricing](https://www.runware.ai/pricing)); Ideogram 4.0 $0.06 on Together ([Together pricing](https://www.together.ai/pricing)); Ideogram v3 Quality $0.09 on Replicate ([Replicate pricing](https://replicate.com/pricing)).
- **Novita:** the pricing page showed no image prices in this capture. — [Novita pricing](https://novita.ai/pricing)

### Inferences
- **Cost for ~100 panels per chapter at ~1 MP:**
  - Gemini Nano Banana 2.1 batch: ~$1.70. Standard: ~$3.40.
  - FLUX.2 [pro] on Together: ~$3.
  - GPT Image 2 medium: ~$5.30.
  - Anime-checkpoint SDXL on Replicate H100: ~$10 at $0.097 per run.
  - Raw SDXL on Together: ~$0.19 at $0.0019/MP, but with no anime checkpoint.
  - Re-rolls for consistency multiply these figures.
- **Character consistency:** the best documented hosted levers are Gemini's character-reference slots (≤5) and FLUX.2's 10-image multi-reference. Pass a per-character reference sheet on every panel call.
- **Text in balloons:** generate panels without text and letter them in Pillow. All models' text rendering is unreliable for Japanese/English balloons; this is general knowledge, not verified here.
- **Violence and other fiction content:** OpenAI exposes `moderation="low"` and BFL exposes `safety_tolerance` up to 6. Gemini publishes no tunable image-safety knob in the captured docs. Expect occasional `moderation_blocked` or refusals on violent scenes and build retry/rephrase logic.

### Gaps
- Per-image prices for BFL direct, Ideogram direct and Novita were not captured because those pages render dynamically.
- Rate limits: OpenAI image RPM/IPM, BFL concurrency, fal/Replicate/Together limits and Gemini per-model IPM were not found in the captured content.
- Whether Runware or Novita host Illustrious, NoobAI or Animagine (Civitai AIR IDs) is unverified. Whether fal-ai/lora works with a Civitai URL and what it costs is also unverified.
- Detailed content-policy text for violence in fiction was not fetched for Google, Together, fal, Replicate, Stability or Ideogram.

---

## 4. Using Claude to turn a story into a structured panel script (JSON)

### Takeaway
Call Claude through `anthropic` 2.3.0 (Python ≥3.10) with **structured outputs**: `client.messages.parse(..., output_format=<PydanticModel>)` or `output_config={"format": {"type": "json_schema", ...}}`. This returns a schema-valid pages → panels → shot/description/characters/dialogue/SFX JSON.
- Current IDs: `claude-opus-5-5` (the default recommendation), `claude-sonnet-5-5`, `claude-haiku-5-5` and `claude-fable-5-1`.
- **The schema must avoid recursion and numeric/length constraints.** Enforce counts in code instead.
- There is **no standard comic-script JSON schema**. The best prior art is Veale's ComiXML (scenes → panels → figures, backdrops, balloons, captions) and AI Comic Factory's `{panel, instructions, caption}` array.

### Cited Findings
- **Current models** ([Anthropic models overview](https://platform.claude.com/docs/en/about-claude/models/overview.md)):

| Model | API ID | Price per MTok (input / output) | Default effort |
|---|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | $10 / $50 | high |
| Claude Opus 5.5 | `claude-opus-5-5` | $4 / $20 | medium |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | $2 / $10 | high |
| Claude Haiku 5.5 | `claude-haiku-5-5` | from $0.10 / $0.50 | medium |

  - All have 1M context and 128K max output. Batch is 50% off.
  - The page says: "start with Claude Opus 5.5 for most workloads". The Claude API ID for each is the pinned dateless ID shown.
- **Install and auth.** `pip install anthropic` (v2.3.0, uploaded 2026-10-23, `requires_python >=3.10`). Auth uses `ANTHROPIC_API_KEY`. — [PyPI JSON: anthropic](https://pypi.org/pypi/anthropic/json) (in-container check)
- **Structured outputs** are GA on the Claude API, including `claude-opus-5-5`, `claude-sonnet-5-5` and `claude-haiku-5-5`. Request with `output_config: {format: {type: "json_schema", schema: {...}}}`, or in Python with `client.messages.parse(model=..., output_format=PydanticModel)`, which returns `response.parsed_output`. The old top-level `output_format` request parameter is deprecated and no beta header is needed. — [Structured outputs docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs.md)
- **Schema limits.** Supported: `enum`, `const`, `anyOf`, `allOf` (no `$ref` inside), local `$ref`/`$defs`, `required`, `additionalProperties: false`, and some string formats. **Not supported: recursive schemas, `minimum`/`maximum`, `minLength`/`maxLength`, array constraints beyond `minItems` 0 or 1.** Complexity limits: 20 strict tools, 24 optional params, 16 union-typed params. "Schema is too complex for compilation" returns a 400, with a 180 s compile timeout. `strict: true` on tools guarantees schema-valid tool inputs. — [Structured outputs docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs.md)
- **Opus 5.5 API behaviour**, from the claude-api skill reference cached 2026-10-06 and consistent with the models overview's "Adaptive (always on)" thinking:
  - Thinking cannot be disabled.
  - Forced `tool_choice` `any`/`tool` returns 400, so use `auto` + `strict`, or structured outputs.
  - Assistant prefill returns 400.
  - Use streaming for large `max_tokens`.
  - — [Anthropic models overview](https://platform.claude.com/docs/en/about-claude/models/overview.md)
- **Prior art for comic-script schemas:**
  - Tony Veale, "Flipping The Script: Complementary Modes of Story Generation in Comics", Text2Story'25 workshop, Lucca, 10 April 2025. It describes the **ComiXML** schema: a comic is composed of "scenes, panels, and panel elements (figures, backdrops, balloons, speech, captions)". Characters are defined with gender and skin/hair/lip tones, and each panel can place up to three figures against a backdrop. The paper contrasts plot → text → visuals with the "Marvel method", where the plot is visualised first and then an LLM writes dialogue to fit. — [CEUR-WS Vol-3964 paper4](https://ceur-ws.org/Vol-3964/paper4.pdf)
  - **AI Comic Factory** (open-source, HF Space) asks the LLM for "a VALID JSON array" typed `Array<{ panel: number; instructions: string; caption: string; }>`. It asks for drawing instructions that state each character's gender, age, origin, clothes, colours, location and lighting, plus 2–3 sentence captions. It uses a `[{` prefill, which is not possible on current Claude models. — [ai-comic-factory predictNextPanels.ts](https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory/blob/b495b181f5ab36cb0db82c175e3294086c63995b/src/app/queries/predictNextPanels.ts)
  - LlamaGen's guide suggests having an LLM produce a beat list and then a script table with panel / camera / dialogue / caption / continuity columns. This is a vendor blog, so it is weak evidence. — [LlamaGen comic script format](https://llamagen.ai/pt-pt/blogs/comic-script-format-for-novel-writers)

### Inferences
- **A practical schema** (my synthesis, fits within the limits above):
  - Top level: `{title, reading_direction: enum["rtl","ltr"], cast: [ {id, name, visual_description, outfit, reference_prompt} ], settings: [ {id, description} ], pages: [ {page_number, layout_hint: enum[...], panels: [ ... ] } ]}`.
  - Each panel: `{panel_id, shot: enum["extreme_wide","wide","medium","close_up","extreme_close_up","over_the_shoulder","pov","insert"], angle: enum[...], size: enum["splash","large","medium","small"], setting_id, description, characters: [ {cast_id, expression, pose, position: enum["left","center","right","background"]} ], dialogue: [ {speaker_cast_id, text, balloon: enum["speech","thought","shout","whisper","narration","caption"]} ], sfx: [ {text, romanized, style} ], image_prompt}`.
  - Use `cast_id` references instead of nesting to stay non-recursive. Check panel counts and dialogue length in Python after parsing.
- **Model choice:** run a two-pass pipeline, script first and then per-panel image prompts. `claude-opus-5-5` (the docs' default) or `claude-sonnet-5-5` for the cheaper screenplay pass. The Batch API halves cost when latency doesn't matter.

### Gaps
- I found no widely adopted, published JSON schema standard for comic or manga scripts; the prior art above uses XML or ad-hoc arrays.
- Anthropic per-tier rate limits were not fetched.

---

## 5. Recommended minimal install set (exact commands, approximate sizes)

### Takeaway
Use **API-first**. The core pipeline (Claude scripting + hosted images + Pillow lettering + PDF/CBZ) is ~39 MB of wheels in a uv venv on the system Python 3.13. Add the optional local CPU path (OpenVINO, or torch CPU + diffusers) only if offline generation is required. That path is ~470 MB of wheels plus 3–7 GB per SDXL-class model, and it will be slow.

### Cited Findings
- **Core set.** `anthropic pydantic pillow img2pdf openai google-genai fal-client replicate huggingface_hub` resolves on Python 3.13 (and 3.12) to 54 packages:
  - Pinned versions include anthropic 2.3.0, openai 3.40.0, google-genai 2.33.0, fal-client 1.0.3, replicate 1.0.7, huggingface-hub 2.3.0, pillow 13.0.0, img2pdf 0.6.3 (which pulls pikepdf 10.17.0) and pydantic 2.14.1.
  - **Approximate total wheel download: ~39 MB.** The largest are pillow 7.1 MB, lxml 5.2 MB and cryptography 5.0 MB.
  - — (in-container `uv pip compile` plus PyPI JSON sizes)
- **Local OpenVINO/torch set.** Approximately ~472 MB of wheels: torch+cpu 196 MB, openvino 59 MB, pyarrow 54 MB, scipy 35 MB, onnxruntime 24 MB, numpy 17 MB, transformers 13 MB, pandas 12 MB, onnx 9 MB, diffusers 6 MB, openvino-genai 7 MB. — (in-container check; sizes from [PyPI](https://pypi.org/) and [download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu/torch/))
- **Model download sizes:**
  - SDXL anime checkpoints: 6.94–7.11 GB each in fp16 single-file form, or 2.8–4.18 GB as Q4_K/Q8_0 GGUF.
  - OpenVINO int8 SDXL-Turbo/Lightning/Hyper repos: ~4.8 GB each.
  - FLUX.2-klein-4B int4 OV: 4.6 GB. LCM-LoRA SDXL: 0.39 GB.
  - — (in-container HF API checks; links in section 1)
- **apt.** Package lists are empty in this container, so `apt-get update` is needed first; `archive.ubuntu.com` is reachable. 119 font files are already installed. — (in-container check)
- **Builds need permission.** Building sd.cpp from source, including `pip install stable-diffusion-cpp-python` (sdist only, 20.6 MB), was blocked by the session permission classifier. — (in-container check)

### Inferences
Suggested commands. Package sets and versions were verified by resolution only; nothing was installed.

```bash
# 0) Project venv on system Python 3.13 (no system-pip changes)
cd /home/user/Manga && uv venv .venv --python 3.13 && source .venv/bin/activate

# 1) Core pipeline: LLM scripting + hosted image APIs + lettering + PDF (~39 MB of wheels)
uv pip install anthropic pydantic pillow img2pdf openai google-genai fal-client replicate huggingface_hub
#    (optional) together runware   # other hosted providers
#    CBZ export: Python stdlib zipfile; no package needed (CBZ = ZIP of page images; unverified format note)

# 2) Fonts for lettering (Japanese/English balloons) — sizes unverified
sudo apt-get update && sudo apt-get install -y fonts-noto-cjk

# 3a) OPTIONAL local CPU path via OpenVINO (+ optimum-intel to export anime SDXL checkpoints)
uv pip install "optimum-intel[openvino]>=2.2" "transformers<5.6" diffusers openvino-genai \
  torch --index-url https://pypi.org/simple --extra-index-url https://download.pytorch.org/whl/cpu \
  --index-strategy unsafe-best-match
#    export:  optimum-cli export openvino --model cagliostrolab/animagine-xl-4.0 --weight-format int8 animagine_ov

# 3b) OPTIONAL plain diffusers on CPU torch (no CUDA bloat: 196 MB torch instead of ~555 MB + CUDA wheels)
uv pip install torch --index-url https://download.pytorch.org/whl/cpu
uv pip install diffusers transformers accelerate safetensors peft

# 3c) OPTIONAL stable-diffusion.cpp (needs user permission to compile; ~20.6 MB sdist, builds with cmake/gcc)
CMAKE_ARGS="-DGGML_NATIVE=ON" uv pip install stable-diffusion-cpp-python
#    weights: e.g. off-grid-ai/illustrious-xl-v2.0-GGUF (Q4_K 2.8 GB) or the 6.94 GB safetensors
```

- **Disk budget.** One SDXL anime model, an OpenVINO export of it and the venv come to roughly 15 GB, which fits in the 31 GB free. Two or more full checkpoints plus exports will get tight.
- **Default if the user has API keys:** core set (1) plus fonts (2). Use Gemini Nano Banana 2.1 or 3.1 Flash Image with character reference images, or FLUX.2 via Together/BFL, for the panels. Use Claude for the script, and Pillow for panel layout, balloons, and PDF/CBZ assembly via img2pdf and zipfile.

### Gaps
- Installed sizes on disk for apt `fonts-noto-cjk` and the full venvs were not measured, because nothing was installed.
- I did not verify which `ComicInfo.xml` fields CBZ readers expect.
- No end-to-end smoke test was run, either local generation or API calls without keys.
