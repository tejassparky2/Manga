"""Tiny image server for a rented GPU (e.g. a RunPod pod with an RTX 4090).

Runs the same model and settings as tools/gen_panel_local.py, so panels made
on the GPU match the ones made on CPU. The manga renderer calls it with
`render_panels.py --remote https://<pod-id>-8000.proxy.runpod.net --token <TOKEN>`.

  pip install diffusers transformers accelerate safetensors huggingface_hub
  TOKEN=<shared secret> python gpu_server.py          # listens on :8000
"""
import io
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock

import torch
from diffusers import EulerAncestralDiscreteScheduler, StableDiffusionXLPipeline
from huggingface_hub import snapshot_download

TOKEN = os.environ["TOKEN"]
MODEL = snapshot_download(
    "cagliostrolab/animagine-xl-4.0",
    allow_patterns=["model_index.json", "scheduler/*", "tokenizer*/*", "text_encoder*/*", "unet/*", "vae/*"],
    ignore_patterns=["*.bin"],
)
pipe = StableDiffusionXLPipeline.from_pretrained(MODEL, torch_dtype=torch.float16).to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.vae.to(torch.float32)  # SDXL VAE is unstable in half precision
lock = Lock()


def generate(req):
    with torch.no_grad():
        latents = pipe(req["prompt"], negative_prompt=req["negative"], width=req["width"], height=req["height"],
                       num_inference_steps=req["steps"], guidance_scale=req["cfg"], output_type="latent",
                       generator=torch.Generator().manual_seed(req["seed"])).images
        latents = latents.to(torch.float32) / pipe.vae.config.scaling_factor
        return pipe.image_processor.postprocess(pipe.vae.decode(latents).sample)[0]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200 if self.path == "/health" else 404)
        self.end_headers()

    def do_POST(self):
        if self.path != "/generate" or self.headers.get("X-Token") != TOKEN:
            self.send_response(403)
            self.end_headers()
            return
        req = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        with lock:
            img = generate(req)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        self.send_response(200)
        self.send_header("Content-Type", "image/png")
        self.end_headers()
        self.wfile.write(buf.getvalue())


if __name__ == "__main__":
    print("ready on :8000", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
