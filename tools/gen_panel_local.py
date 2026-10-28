"""Generate one manga panel on CPU with Animagine XL 4.0 (no API key needed).

Measured on this container (4 vCPU Xeon with AMX, bf16): 832x1216, 20 steps,
CFG 5 took ~205 s per panel.

  python tools/gen_panel_local.py "1girl, short black hair, school uniform, rooftop, wind" -o output/p1.png
"""
import argparse
import time
from pathlib import Path

import torch
from diffusers import EulerAncestralDiscreteScheduler, StableDiffusionXLPipeline

MODEL = Path(__file__).resolve().parent.parent / "models" / "animagine-xl-4.0"
# CLIP reads only 77 tokens, so the style tags lead and the quality tags trail.
STYLE = "monochrome, greyscale, manga"
QUALITY = "screentone, masterpiece, high score, absurdres"
NEGATIVE = ("lowres, bad anatomy, bad hands, text, speech bubble, error, worst quality, low quality, "
            "jpeg artifacts, signature, watermark, blurry, color")


def full_prompt(prompt):
    return f"{STYLE}, {prompt}, {QUALITY}"


def load_pipeline():
    pipe = StableDiffusionXLPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16)
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.vae.to(torch.float32)  # SDXL VAE is unstable in half precision
    return pipe


def generate(pipe, prompt, width=832, height=1216, steps=20, cfg=5.0, seed=0, negative=NEGATIVE):
    with torch.no_grad():
        latents = pipe(full_prompt(prompt), negative_prompt=negative, width=width, height=height,
                       num_inference_steps=steps, guidance_scale=cfg, output_type="latent",
                       generator=torch.Generator().manual_seed(seed)).images
        latents = latents.to(torch.float32) / pipe.vae.config.scaling_factor
        return pipe.image_processor.postprocess(pipe.vae.decode(latents).sample)[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", help="Danbooru-style tags describing the panel")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--width", type=int, default=832)
    ap.add_argument("--height", type=int, default=1216)
    ap.add_argument("--steps", type=int, default=20)
    ap.add_argument("--cfg", type=float, default=5.0)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()

    pipe = load_pipeline()
    t = time.time()
    img = generate(pipe, a.prompt, a.width, a.height, a.steps, a.cfg, a.seed)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    img.save(a.out)
    print(f"saved {a.out} in {time.time() - t:.0f}s")


if __name__ == "__main__":
    main()
