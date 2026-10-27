#!/usr/bin/env bash
# Installs the story-to-manga toolchain in a CPU-only Linux container.
# See "reports/AI story to manga toolchain.md" for why each piece was chosen.
set -euo pipefail
cd "$(dirname "$0")"

# System packages: CJK fonts, screentone/vector tools, archive tool, EGL for skia-python
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
  fonts-noto-cjk imagemagick gegl potrace 7zip libegl1 libgl1

# Python venv (system Python 3.13)
uv venv .venv --python 3.13
. .venv/bin/activate

# Core: LLM scripting, hosted image APIs, page assembly and PDF export
uv pip install anthropic pydantic pillow img2pdf pyyaml \
  openai google-genai fal-client replicate huggingface_hub

# Layout, lettering, screentone and line-art helpers
uv pip install shapely drawsvg skia-python uharfbuzz pyphen numpy \
  opencv-python-headless vtracer playwright
# Python Playwright uses the pre-installed Chromium via executable_path;
# do not run `playwright install`.

# Local CPU image generation (CPU-only torch wheel, no CUDA downloads)
uv pip install torch --index-url https://download.pytorch.org/whl/cpu
uv pip install diffusers transformers accelerate safetensors peft

# Animagine XL 4.0 (CreativeML Open RAIL++-M), diffusers layout, ~7 GB
if [ ! -f models/animagine-xl-4.0/unet/diffusion_pytorch_model.safetensors ]; then
  hf download cagliostrolab/animagine-xl-4.0 --exclude "*.safetensors" --local-dir models/animagine-xl-4.0
  hf download cagliostrolab/animagine-xl-4.0 \
    unet/diffusion_pytorch_model.safetensors text_encoder/model.safetensors \
    text_encoder_2/model.safetensors vae/diffusion_pytorch_model.safetensors \
    --local-dir models/animagine-xl-4.0
fi

# Research helpers: Chrome DevTools MCP and Reddit MCP (official Reddit OAuth API)
npm install -g chrome-devtools-mcp@1.12.0
uv tool install --force --python 3.12 --with httpx git+https://github.com/adhikasp/mcp-reddit.git

echo "Done. Activate with: source .venv/bin/activate"
