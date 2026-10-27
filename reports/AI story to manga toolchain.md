# Plan Locally, Render Remotely, Letter in Code

As of late October 2026, no single tool reliably turns a written story into manga. What works is a pipeline built in stages. An LLM turns the story into a structured page-and-panel script. Character reference sheets fix what each character looks like. A hosted multimodal image model draws each panel, or each page, with no text in it. Ordinary code then lays out the pages right-to-left, letters the balloons, adds screentone and exports CBZ and PDF files.

No maintained open-source project does all of this well. The research systems built for manga, DiffSensei and StoryDiffusion, stopped updating in 2024–25 and need 24 GB-class GPUs. AI Comic Factory, the best-known open-source app, was archived in October 2025. The 2026 activity is in small, single-maintainer "agent" repos that wrap the Gemini or OpenAI image APIs.

People who actually make these comics, on Reddit, Hacker News and Japanese blogs, report the same thing: drawing is no longer the hard part. The hard parts are the storyboard, keeping rooms and props consistent, scenes where characters touch, and lettering. Consistency from reference images alone tops out at about 60–70% and starts drifting after roughly ten pages unless you train a small per-character model (a LoRA).

For this CPU-only container, use hosted APIs rather than local generation. Claude writes the script, either this Claude Code session or the Claude API. Gemini Nano Banana 2.1 (about $0.034 per image) or GPT Image 2 draws the panels. Pillow, Playwright, ImageMagick and img2pdf do layout, lettering, tone and export locally. The core Python packages are about 40 MB of downloads. Running image models locally on this CPU works, but each panel takes minutes.

On the legal side, US law does not protect raw AI images, but it does protect a human-written script and the human selection and arrangement of panels. Platforms range from outright bans (Jump+, WEBTOON contests, ComicFury) to rules that only require labelling (pixiv, Amazon KDP).

## Research code is frozen, and active tools are small repos that call image APIs

The research systems built for manga don't run without a GPU lab. **DiffSensei (CVPR 2025) is the only manga paper that released inference code, weights and dataset annotations.** Even its cut-down demo, without the multimodal LLM, needs "a single 24GB 4090". Its last commit was February 2025, and the repo still has no LICENSE file ([DiffSensei](https://github.com/jianzongwu/DiffSensei)). Most of its issues are about missing weight files, breakage from Gradio version changes, and a 2026 request to "Add LICENSE file to clarify license terms" ([DiffSensei issues](https://github.com/jianzongwu/DiffSensei/issues?q=is%3Aissue)).

StoryDiffusion is the best-known consistency method, with 6.5k stars. It was last updated in September 2024, has 117 open issues and expects more than 20 GB of VRAM ([StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion)). Many of those issues ask for FLUX or SD3 support and got no maintainer reply ([StoryDiffusion issues](https://github.com/HVision-NKU/StoryDiffusion/issues)).

The newer manga papers publish no code. That includes MangaDiffusion, TaleDiffusion and MangaFlow, an agentic story-to-manga framework accepted at EMNLP 2026 ([MangaDiffusion](https://arxiv.org/abs/2412.19303); [TaleDiffusion](https://arxiv.org/abs/2509.04123); [MangaFlow](https://arxiv.org/abs/2605.28173)). The only way to use this tier without a GPU is to rent one. StoryDiffusion on Replicate costs about **$0.064 per run** on an L40S ([Replicate](https://replicate.com/hvision-nku/storydiffusion)).

What the research did contribute is a design. MangaFlow splits the job into six stages: planning, grounding, layout, rendering from references, composition, and text placement. A "story section memory" links each part of the story to character, scene and object references that get reused ([MangaFlow](https://arxiv.org/abs/2605.28173)). The working open-source tools of 2026 arrived at the same shape on their own. The design point that matters most is keeping text out of the image model. MangaFlow's FLUX.2 baseline, which generated pages directly, often produced unreadable bubble text, so the paper scores lettering separately ([arXiv HTML](https://arxiv.org/html/2605.28173)).

The apps show the same pattern. **AI Comic Factory was archived on 2025-10-31.** Its Hugging Face Space still runs on CPU-only hardware with 11,310 likes, because all generation happens on remote servers ([GitHub](https://github.com/jbilcke-hf/ai-comic-factory); [HF Space API](https://huggingface.co/api/spaces/jbilcke-hf/ai-comic-factory)). But its default models are dated ones such as `gpt-4-turbo` and SDXL.

The 2026 projects are small. The largest is 133 stars, and most use an LLM to plan pages and a hosted image API to draw them ([GitHub topic comic-generation](https://github.com/topics/comic-generation)). The models underneath change fast:
- The "Story to Manga" app from Show HN limited stories to 500 words and drew with Gemini 2.5 Flash Image ([HN](https://news.ycombinator.com/item?id=45214302)). Google shut that model down on 2026-10-02 ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)).
- OpenAI shut down `gpt-image-1` on 2026-10-23 ([OpenAI image guide](https://developers.openai.com/api/docs/guides/image-generation)).

Any pipeline you adopt now should make the image provider easy to swap.

| Option | What it is | Image backend | Fit for this container | Status (2026-10-27) |
|---|---|---|---|---|
| [phaethix/inkstone](https://github.com/phaethix/inkstone) | Python CLI: `.txt` novel → PDF/CBZ/PNG; tracks each character across panels; resumes after interruption | Agnes API (free key) or any OpenAI-compatible images endpoint | **Best ready-made fit**: Python ≥3.10, uv, "No GPU, no paid plan" | 12★, commit 2026-10-23 |
| [Yutarop/comic-generator](https://github.com/Yutarop/comic-generator) | Idea → 4-page manga; 1 plot call + 1 image call per page | Gemini 3 Pro Image (paid) | Good, but its `-preview` model IDs probably need updating | 16★, commit 2025-11-28 |
| [kdjfs/plot2panel](https://github.com/kdjfs/plot2panel) | Premise → checked four-panel strip | DeepSeek plans; SiliconFlow, Together or Pollinations draw | Runs on Node 22; **4 panels only** | 2★ |
| [BotTony329/mangaharness](https://github.com/BotTony329/mangaharness) | Local-first manga editor UI with an agent | Gemini or OpenAI-compatible | Runs on Node ≥18.18; it's a GUI | 4★ |
| [stockedge/manga-generator](https://github.com/stockedge/manga-generator) | Novel → script → storyboards → art → lettering → PDF | Codex's image tool, or external ComfyUI (prototypes used about 48 GB VRAM) | **Poor fit**: needs Node 24 and a GPU host | 119★ |
| [wenn-id/comicsol](https://github.com/wenn-id/comicsol) | Agent skill: plan → QA → letter → compose | Whatever image tool the agent has | Its skill installer depends on an unpublished release | 7★, 25 open issues |
| DiffSensei / StoryDiffusion | Research models | Local SDXL | **Not viable**: 20–24 GB GPU | Not updated since 2024–25 |

Commercial products exist, but nobody independent has reviewed them. LlamaGen sells a "Comic API" on plans from $18 to $200 a month ([LlamaGen pricing](https://llamagen.ai/pricing)). Anifusion offers a REST API and hosted MCP on its $9 and $24 plans and runs anime SDXL models such as Animagine and NoobAI ([Anifusion pricing](https://anifusion.ai/pricing)). Komiko's pricing page lists no API ([Komiko pricing](https://komiko.app/pricing)). A notice quoted on Reddit says Dashtoon's studio shut down on 15 August 2026 and creation moved to Frameo ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1te66s2/what_are_the_best_ai_comic_generators_in_2026/)). Every quality claim about these services comes from the vendors themselves.

## Reference sheets are enough for short stories; long ones still need a trained LoRA

The hosted image models are now the strongest and easiest option for keeping characters consistent. You attach reference images of each character to every request. Pricing differs a lot between them:

| API (model ID) | Price per ~1 MP image | Character references | Notes | Source |
|---|---|---|---|---|
| Gemini Nano Banana 2.1 (`gemini-nano-banana-2.1`) | **$0.0336**; $0.0168 in batch | 4–5 character images (see note below) | Every output has a SynthID watermark; **no free tier for image output** | [pricing](https://ai.google.dev/gemini-api/docs/pricing), [guide](https://ai.google.dev/gemini-api/docs/image-generation) |
| Gemini 3.1 Flash Image (`gemini-3.1-flash-image`) | $0.067; $0.034 in batch | 4–5 | | same |
| Gemini 3 Pro Image (`gemini-3-pro-image`, "Nano Banana Pro") | $0.134 | Disputed (see note below) | The model practitioners use most for B&W manga pages | same |
| OpenAI GPT Image 2 | $0.006 low / $0.053 medium / $0.211 high | Edits from several images (the docs' example uses 4) | `moderation="low"` available; you may need to verify your organization | [OpenAI guide](https://developers.openai.com/api/docs/guides/image-generation) |
| FLUX.2 [pro] on Together | $0.03 | Up to 10 | | [Together](https://www.together.ai/pricing), [BFL docs](https://docs.bfl.ai/kontext/kontext_image_editing) |
| NoobAI-XL community model on Replicate | ~$0.097 per run | None (load LoRAs via fal-ai/lora) | Real anime-style linework | [Replicate](https://replicate.com/delta-lock/noobai-xl), [fal](https://fal.ai/models/fal-ai/lora/api) |

The research notes read Google's flattened table two different ways. One reading gives 4 character slots to 2.1 and 3.1 Flash and 5 to Pro. The other gives 5 to 2.1 and 3.1 Flash and no character slots to Pro. Check the live docs before you hard-code the number. OpenAI's own guide says its image models "may occasionally struggle to maintain visual consistency for recurring characters" ([OpenAI guide](https://developers.openai.com/api/docs/guides/image-generation)).

Among open-weight models, the SDXL anime family is still the default for real manga linework. That means Illustrious XL, NoobAI-XL and Animagine XL 4.0. They have booru-tag control and a large ecosystem of LoRAs and ControlNets, each checkpoint is about 6.5–7 GB, and they run in 8 GB of VRAM ([InsiderLLM guide](https://insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/)).

Licences differ:
- **Animagine XL 4.0:** explicitly allows commercial use under Open RAIL++-M ([HF card](https://huggingface.co/cagliostrolab/animagine-xl-4.0)).
- **Illustrious:** OpenRAIL-M.
- **NoobAI:** its FAIPL licence is ambiguous about commercial use.

Civitai has monochrome manga LoRAs that trigger "monochrome greyscale screentones crosshatching" ([Manga Mode](https://civitai.com/models/1255751/manga-mode-illustrious)).

The newer models are mostly general-purpose editors that accept multiple reference images, and most come with licence strings attached:
- **FLUX.2 [klein] 4B:** Apache 2.0, runs in 4 steps ([HF](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B)).
- **FLUX 3 Image Klein** (released 2026-10-15): takes up to 10 references, but its licence only allows commercial outputs for businesses under $5M revenue ([HF](https://huggingface.co/black-forest-labs/flux-3-image-klein)).
- **Qwen-Image-2.1:** research-only licence ([HF](https://huggingface.co/Qwen/Qwen-Image-2.1)).
- **Anima:** a 2B anime model whose licence forbids commercial use of the model but allows commercial use of outputs ([HF](https://huggingface.co/circlestone-labs/Anima)).

None of these model cards mentions screentone or monochrome manga.

The research notes found that face-identity tools don't work on anime. InstantID, PuLID and IP-Adapter FaceID all depend on InsightFace face embeddings, which come with non-commercial licences ([InstantID](https://github.com/zengyh1900/InstantID)). One studio that produced a 120-page AI manga found that the FaceID V2 detector found **"0 faces" on anime characters** ([Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)). The same team measured the limit of reference images: they topped out at **about 60–70% consistency, and faces drifted after roughly ten pages**. They also found that three reference images blended into a blurry face, and recommend two: one face close-up and one full body. Their fix was a character LoRA trained on 15–30 images, which took 30–60 minutes per character on an RTX 4090 at about $1 of GPU time.

Reddit's most detailed advice agrees:
- "Identity should come from a character LoRA, not IP-Adapter. IP-Adapter drags the style along with the face" ([r/comfyui](https://www.reddit.com/r/comfyui/comments/1voemlz/need_help_building_a_consistent_character/)).
- A two-round LoRA training process is normal, starting from one good image.
- "anime is genuinely easier… A slightly-off anime face still reads as the same character."
- Even a good LoRA "will still only get you about 70%/80% of where you want to be", according to the author of the most-upvoted Krita comic series ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1ozuldj/proof_of_concept_for_making_comics_with_krita_ai/)).

LoRA training needs an NVIDIA GPU, so it can't be done in this container ([ai-toolkit](https://github.com/ostris/ai-toolkit)).

The cheap techniques that work without training come from the same sources:
- **Character sheets:** 2–4 full-body references plus two head shots, one facing the camera and one at a three-quarter angle ([r/comfyui](https://www.reddit.com/r/comfyui/comments/1wxixua/minimax_h3_image_generation_create_consistent/)).
- **One fixed "anchor" detail per character**, such as a scar or a red scarf ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1umhul8/comfyui_instant_storytocomic_generator_no_loras/)).
- **A "costume lock"** that lists outfit substitutions the model must not make ([Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)).
- **Only the references for characters in that panel**, because stacking unrelated references blurs which features belong to whom ([tech-insider](https://tech-insider.org/ai-comic-generator-character-consistency-2026/)).
- **Batch by character**, not by page: "drift within a run is way smaller than drift across the whole project" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1w9i3cr/whole_manhua_page_generated_locally_in_one_shot/)).
- **Edit a clean neutral image** for each expression instead of regenerating the character ([r/comfyui](https://www.reddit.com/r/comfyui/comments/1xc7os5/looking_for_workflows_for_character_expressions/)).
- **Black and white:** several creators chose it on purpose because it "keeps the style much more stable" ([r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1v5tkcl/i_spent_months_testing_whether_chatgpt_can_create/)).

Two characters in one panel is still the weak spot. Masked regional prompting reduces features bleeding between characters but doesn't eliminate it ([Easton Dev](https://eastondev.com/blog/en/posts/ai/20260828-comfyui-regional-prompting-multi-subject/)). Practitioners end up generating each figure separately and compositing them.

## People who make AI manga say the hard part is directing, not drawing

Practitioners split over whether to generate whole pages or single panels, and the split comes down to project length. The strongest case for whole pages comes from a months-long test of a 100-page ChatGPT comic: "Generating one complete comic page with one prompt turned out to be much more consistent." The real work happened earlier, in reusable character and environment sheets and a storyboard for each page ([r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1v5tkcl/i_spent_months_testing_whether_chatgpt_can_create/)). On short work, GPT Image 2 impressed Hacker News users: the author of one manga experiment found it "amazing… that GPT Image 2.0 was this good at making a coherent manga page in one shot" ([HN](https://news.ycombinator.com/item?id=48038672)).

The opposing view has more upvotes. The +32 tip on r/StableDiffusion is "do one panel at a time, and add the text in post" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1r1gsog/comic_attempts_with_anima_preview/)). One person reviewed 17 tutorials and found that whole-page generation "looks much less reliable than the thumbnails suggest", with several tutorials falling back to one panel at a time ([r/OpenAI](https://www.reddit.com/r/OpenAI/comments/1x032fq/i_analyzed_17_ai_comic_tutorials_theyre_all/)). One commenter put the trade-off plainly: with one-shot pages "you're trading away the ability to redo panel 3 without touching 1 2 and 4" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1w9i3cr/whole_manhua_page_generated_locally_in_one_shot/)).

The evidence supports a hybrid. A Zenn author concluded that static dialogue 4-koma strips are "practical" with current AI ([Zenn](https://zenn.dev/xei/articles/ai-manga-character-consistency)). Long works, action and anything you'll need to edit push toward per-panel generation.

Everyone agrees on doing the design first. Deskrex sets four checkpoints before generating any image: the script, character anchors, a YAML storyboard for each page (camera, placement, balloon positions, SFX), and then generation with QC. Its key line is "The most important thing is to finish the design before generating images" ([Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)). On Reddit, creators who have finished projects describe it as project management: "the image generator stopped being the bottleneck. The project became the bottleneck" ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1wvoiwv/the_image_generator_stopped_being_the_bottleneck/)). They keep a page manifest of character-sheet versions and approved images, and treat the novel's text as the source of truth for lettering ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1x54lx2/im_turning_my_own_middlegrade_novel_into_a/)).

The failures cluster where comics differ from single illustrations:

| Works | Fails |
|---|---|
| Static dialogue scenes, short gag strips, 4-koma ([Zenn](https://zenn.dev/xei/articles/ai-manga-character-consistency)) | Rooms, layouts and camera continuity across pages, the top complaint at +38 ([r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1v5tkcl/i_spent_months_testing_whether_chatgpt_can_create/)) |
| Character sheet attached to every prompt; new chat every 3–5 pages ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1xdcu8u/how_do_you_keep_comics_consistent/)) | Two characters touching: "a two day long argument with ChatGPT… had to manually collage them" ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1wkte8y/figured_others_would_appreciate_the_struggle/)) |
| 3D mannequins or pose apps to lock camera and height, then ControlNet or an edit model ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1vtk48r/quick_workflow_tip_use_a_3d_pose_app_to_lock_the/)) | Fights: Nano Banana Pro "doesn't know how to do fights" ([r/Bard](https://www.reddit.com/r/Bard/comments/1p34pxv/nano_banana_pro_is_insane_when_it_comes_to/)); pages read "like… a slideshow" ([r/OpenAI](https://www.reddit.com/r/OpenAI/comments/1wl1lyq/how_do_i_make_ai_manga_fights_feel_like_actual/)) |
| Lettering done outside the model, in an editor or in code ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1w8r71q/how_do_you_handle_lettering_in_your_comic_workflow/)) | Text in the image: typos such as "RULES OF HOORS?" ([HN](https://news.ycombinator.com/item?id=46066433)); fake signatures ([HN](https://news.ycombinator.com/item?id=49972442)); balloons on the wrong speaker ([r/GeminiAI](https://www.reddit.com/r/GeminiAI/comments/1rpubcj/i_made_a_manga_poc_with_gemini_and_got/)) |
| A human-written script with specific direction | LLM dialogue: "a bingo-card of all the standard AI catchphrases", output drifting to "the mean of its training data" ([HN](https://news.ycombinator.com/item?id=48038672)) |

A measured local test shows how much drift remains even with a full SDXL, ControlNet and LoRA stack. **22% of same-character pairs fell below an InsightFace "same person" threshold**, figures in contact split or fused, and bodies came out 9–10 heads tall ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1w9i3cr/whole_manhua_page_generated_locally_in_one_shot/)). Chat-based editors also ignore local fixes. Asked to narrow only the nose, ChatGPT "adjusts the entire face width" ([r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1umisjz/trying_to_make_a_consistent_comic_in_chatgpt_is/)). Readers spot the look straight away: one +13 commenter called ChatGPT's "overly loaded" rendering "a terrible watermark" ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1vcvbh1/im_experimenting_with_an_aiassisted_manga/)).

Fully automatic runs produce volume but not quality:
- A Claude-orchestrated run produced a 25-page GPT-Image-2 graphic novel in "a few hours", and nobody assessed its quality ([HN](https://news.ycombinator.com/item?id=48137188)).
- A 59-page Codex comic drew "full of mistakes and repetitions" as a top response ([r/codex](https://www.reddit.com/r/codex/comments/1t3yt5i/made_an_entire_59_page_comic_book_using_codex/)).

Realistic budgets are larger than the per-image price suggests:
- **Deskrex:** about **30 minutes per page** for single-shot Nano Banana Pro pages driven by YAML. One page took 13 generations plus inpainting. Total cost for 120 pages was about ¥3,600–11,500 ([Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)).
- **Reddit creators:** 10–20 tries for complex scenes ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1q0njk6/my_first_ai_webcomic_with_nano_banana_pro_in/)), and about two months for a 50-page comic ([r/DefendingAIArt](https://www.reddit.com/r/DefendingAIArt/comments/1wi8i8g/ai_has_let_me_publish_my_first_comic/)).

Sales so far are tiny. One self-published AI shōnen manga sold 4 copies on Lulu, and later 8 ([r/DefendingAIArt](https://www.reddit.com/r/DefendingAIArt/comments/1vp3zm5/my_ai_manga_got_8_sales_and_a_pro_ai_game/)).

## Layout, lettering, tone and export can all be done in ordinary code

The half of the pipeline that isn't image generation is where manga differs from Western comics, and it runs fine on a CPU.

**Layout conventions:**
- **Reading order:** pages start top-right, read right-to-left along each row, and end bottom-left ([GlobalComix komawari](https://globalcomix.com/news/details/254/creator-tips-and-tricks-9-basics-of-komawari)).
- **Gutters:** one Japanese production book's example uses 2 mm left/right and 5 mm top/bottom, while noting that spacing varies by artist ([gihyo.jp](https://gihyo.jp/assets/files/book/2025/978-4-297-15158-4/9784297151584-01.pdf)).
- **Bleed:** 3–5 mm ([clipstudio.net](https://www.clipstudio.net/oekaki/archives/149920)).
- **Resolution:** **600 dpi for monochrome and 350 dpi for colour or grey**.
- **Trim sizes:** B5 for magazines (182×257 mm), B6 for tankōbon, A5 for dōjinshi ([CSP Tips](https://tips.clip-studio.com/en-us/articles/8264)).
- **Page sides:** odd pages fall on the right ([MediBang](https://medibangpaint.com/en/use/2021/11/mangatutorialforbeginners07)).
- **Panels per page:** the Manga109 annotations give 103,850 frames across 10,130 two-page-spread images, which works out to roughly five panels per page ([Manga109](http://www.manga109.org/en/annotations.html)). That is a sensible default.

No manga layout generator can be installed with pip. As one r/comfyui commenter put it, "people just generate images and set them in panel by hand" ([r/comfyui](https://www.reddit.com/r/comfyui/comments/1sxb85e/is_there_a_workflow_for_creating_mangacomic_panels/)). A small engine of your own is the right tool. It represents each page as a recursive split tree, outputs panel polygons in right-to-left order, uses Shapely for slanted panels, and renders with Pillow at print resolution.

**Lettering** is less solved, but the pieces exist. No library automatically places balloons and tails. The classic approach scores candidate positions by overlap with faces, distance to the speaker and reading order, borrowed from cartographic label placement ([USPTO 8207987](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8207987)).

The manga translator projects already contain mature text-fitting code, and their licences decide which you can reuse:
- **manga-image-translator and BallonsTranslator:** GPL-3.0, so copying their code makes your code GPL ([manga-image-translator](https://github.com/zyddnys/manga-image-translator)).
- **comic-translate:** Apache-2.0 ([comic-translate](https://github.com/ogkalu2/comic-translate)).
- **koharu:** MIT/Apache, written in Rust ([koharu](https://github.com/mayocream/koharu)).

Vertical Japanese text needs care. In a test in this container, Pillow's `direction="ttb"` stacked multi-line columns left-to-right, which is backwards for Japanese. Chromium's CSS `writing-mode: vertical-rl` handles it properly, including tate-chu-yoko ([W3C](https://www.w3.org/International/articles/vertical-text/)). Reddit surfaced ComiKumi, an open-source lettering tool built for a 110-page manga published in English, German and Japanese, which keeps balloon data separate from the art and supports tate-gaki ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1w382k8/keito_no_sei_a_110page_wholesome_sliceoflife/)).

**Fonts:**
- **Shippori Antique** (SIL OFL) was "created to provide people who draw manga in Japan a beautiful antique font for free" ([Fontsource](https://fontsource.org/fonts/shippori-antique/about)).
- **Blambot's free fonts** are licensed for independent and small-press comics "even if you are making money", but not for mainstream publishers ([Blambot](https://blambot.com/pages/licenses)).
- **Wild Words**, the classic scanlation font, costs $49 per style ([Fontspring](https://fontspring.com/fonts/comicraft/wildwords)).
- Don't redistribute the fonts bundled with manga-image-translator. They include `msgothic.ttc` and `msyh.ttc`, which have proprietary or limited licences.

**Lettering conventions:**
- **Japanese:** dialogue at 10–14 pt with 125% line spacing ([CSP Tips](https://tips.clip-studio.com/en-us/articles/9582)).
- **English:** tails point at the mouth, ellipses have exactly three dots, and balloons don't cross panel borders ([Blambot grammar](https://blambot.com/pages/comic-book-grammar-tradition)).

Bad balloon craft is the quickest giveaway to cartoonists: "balloon tails that point nowhere near their supposed speaker" ([HN](https://news.ycombinator.com/item?id=48224465)).

**Screentone** needs no GPU:
- **ImageMagick:** ships 45° halftone screens (`-ordered-dither h6x6a`, `h8x8a`) ([ImageMagick](https://usage.imagemagick.org/quantize/)).
- **GEGL:** `gegl:newsprint` exposes angle and period ([GEGL](https://gegl.org/operations/gegl-newsprint.html)).
- **Manga Screen:** a popular October 2026 open-source node. It keeps lines crisp, leaves light areas as blank paper, turns dark hair and clothes solid black, and puts tone only on mid-tones. It is "a single ~260-line Python file that only uses numpy/opencv/torch" under MIT ([r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/comments/1x86cki/i_made_a_custom_node_that_turns_illustrations/)).

Generate tone at final print resolution, because downscaling halftone creates moiré.

For line art:
- **MangaLineExtraction:** MIT, 43M parameters ([HF](https://huggingface.co/p1atdev/MangaLineExtraction-hf)).
- **controlnet_aux** line-art detectors run on CPU by default ([controlnet_aux](https://github.com/huggingface/controlnet_aux)).
- **vtracer** (MIT) vectorises line art ([vtracer](https://github.com/visioncortex/vtracer)).

**Automated checks** on finished pages can use permissively licensed detectors:
- **ogkalu/comic-text-and-bubble-detector:** Apache-2.0, 43M parameters, classes `bubble`, `text_bubble` and `text_free` ([HF](https://huggingface.co/ogkalu/comic-text-and-bubble-detector)).
- **Kumiko:** detects panels and orders them with `--rtl`; it is AGPL-3.0, so run it as a separate process ([Kumiko](https://github.com/njean42/kumiko)).
- **manga-ocr:** Apache-2.0, reads Japanese text back so you can catch clipped glyphs ([manga-ocr](https://github.com/kha-white/manga-ocr)).

Magi is better at reading order, but it is licensed for academic research only ([Magi](https://github.com/ragavsachdeva/magi)).

**Export:**
- **CBZ:** a ZIP of numbered images plus `ComicInfo.xml` with `<Manga>YesAndRightToLeft</Manga>` ([ComicInfo](https://anansi-project.github.io/docs/comicinfo/documentation)).
- **PDF:** img2pdf creates lossless PDFs ([img2pdf](https://github.com/josch/img2pdf)).
- **EPUB/KEPUB/MOBI:** KCC is actively maintained (commit 2026-10-26) and builds them with `kcc-c2e -m` for right-to-left reading. It is not on PyPI, and Ubuntu's `kcc` package is a different program ([KCC](https://github.com/ciromattia/kcc)).
- **WEBTOON:** wants images "within 800x1280px", at most 2 MB each ([WEBTOON handbook](https://webtoons-static.pstatic.net/creator101/en/pdf/Creators-Resource-Handbook-Updated.pdf)).

## Copyright protects the script and the panel arrangement, not the pixels

**United States.** The US Copyright Office's January 2025 report is clear: "prompts alone do not provide sufficient human control to make users of an AI system the authors of the output." It also says "the selection and arrangement of AI-generated images with human-authored text in a comic book were protectable as a compilation." Human creative changes to AI output are protected too ([USCO Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)). The test case was *Zarya of the Dawn*. Its text and arrangement were registered, but its Midjourney images were "not the product of human authorship". A Photoshop lip edit was ruled "too minor and imperceptible" to count ([Zarya decision](https://www.copyright.gov/docs/zarya-of-the-dawn.pdf)).

**Japan.** Japan's Agency for Cultural Affairs decides case by case. "Repeated attempts, while checking the generated materials and correcting the instructions/input, may be recognized as a creative contribution." Selection alone generally doesn't count. A style counts only as an idea, and copying a style is not infringement ([Bunka-chō](https://www.bunka.go.jp/english/policy/copyright/pdf/94055801_01.pdf)).

The practical point: the parts this pipeline leaves to humans are the legally valuable ones, namely the script, the storyboard and panel arrangement, and the lettering. Keeping process records, as manga writer Takahiro Ozawa does, strengthens both authorship and non-infringement claims ([Morikatron](https://morikatron.ai/2024/09/cedec2024_ozawa/)).

**Platforms** have split into three groups.

*Bans:*
- **Shueisha:** told an author that Jump+ "cannot publish AI manga", and disqualified an AI manga that ranked No. 1 on Jump Rookie in February 2026 ([Automaton](https://automaton-media.com/en/news/shonen-jump-publisher-disqualifies-ai-generated-manga-after-it-ranked-no-1-in-rookie-contest-ranking/)).
- **WEBTOON contests** disqualify entries made with generative AI ([WEBTOON notice](https://www.webtoons.com/en/notice/detail?noticeNo=3320)).
- **ComicFury** bans AI artwork "partially or in full" ([ComicFury](https://comicfury.com/rules.php)).

*Disclosure required:*
- **Amazon KDP** requires you to declare AI-generated images "even if you applied substantial edits afterwards" ([KDP](https://kdp.amazon.com/en_US/help/topic/G200672390)).
- **pixiv** requires labels on mostly-AI works and forbids repeatedly copying a specific third party's style ([pixiv](https://www.pixiv.net/terms/?page=guideline&lang=en)).

*In between:*
- **GlobalComix** removed fully AI-generated works on 2026-03-20 but says it still allows AI within the creation process ([Graphic Policy](https://graphicpolicy.com/2026/03/24/globalcomix-updates-its-ai-content-policy-removing-fully-ai-generated-works/)). However, a support reply quoted on Reddit told one GPT-Image-2 creator that AI artwork is not permitted "regardless of whether the story… or overall creative direction are created by the artist" ([r/aicomicmakers](https://www.reddit.com/r/aicomicmakers/comments/1wnuqyu/where_are_people_publishing_aiassisted_comics/)).
- **WEBTOON Canvas:** no official AI rule was found. Users report AI works appear there and that there is no option to report them ([r/webtoons](https://www.reddit.com/r/webtoons/comments/1svcetp/lets_see_how_many_ai_canva_comics_we_can_find_by/)).

Reader communities are hostile:
- On r/webtoons, a +1,556 comment says AI art "always demotes it to slop" ([r/webtoons](https://www.reddit.com/r/webtoons/comments/1rxohiz/warning_the_manhwa_unholy_is_an_ai_slop/)).
- An AI manga topped Comic C'moA's Young Adult chart in early 2026, and readers responded with suspicion of fake reviews and calls for a separate AI category ([Unseen Japan](https://unseen-japan.com/ai-manga-japan-bestseller/)).
- An AI-written isekai novel lost its award and its planned manga adaptation ([r/books](https://www.reddit.com/r/books/comments/1q7z3va/aigenerated_isekai_novel_that_won_a_literary/)).
- Human artists are being falsely accused too. One Tapas artist said the site nearly shut them down after reports that their hand-drawn art was AI ([Tapas forum](https://forums.tapas.io/t/lack-of-ai-presence-on-tapas/90218)).

Pixiv with AI tags, Patreon, self-hosting, Lulu and AI-specific sites are where AI-assisted manga actually gets published in late 2026.

## An API-first core needs only about 40 MB of packages

The container sets the constraints. The checks below were run here on 2026-10-27:
- **CPU:** four Xeon cores with AVX-512 and AMX.
- **Python:** 3.13. Everything needed has cp313 wheels, but the system pip is Debian's externally-managed copy, so work inside a uv venv.
- **apt:** the package lists start empty.
- **GitHub:** `git clone` works, but release downloads, codeload tarballs and the GitHub API return 403. Prebuilt binaries such as stable-diffusion.cpp's releases can't be fetched.
- **Building C++:** compiling stable-diffusion.cpp from source was blocked by the session's permission classifier and will need your explicit approval.
- **Network:** Hugging Face downloads work. The API hosts for Anthropic, OpenAI, Google Gemini, BFL, Replicate, fal and Together all answered through the proxy.
- **PyTorch:** the CPU build of torch from the PyTorch index is 196 MB, against 554.6 MB plus CUDA dependencies from plain PyPI ([PyTorch CPU index](https://download.pytorch.org/whl/cpu/torch/); [PyPI torch](https://pypi.org/pypi/torch/json)).

Generating images locally on this CPU is too slow to be the default.
- **Published CPU numbers:** FastSD CPU's benchmarks come from a 12-core i7-12700. SDXL-Lightning takes 10–18 s at 768 px with 2 steps. FLUX.1-schnell takes 4.5 minutes, and **needs about 30 GB of RAM, twice what this box has** ([FastSD CPU](https://github.com/rupeshs/fastsdcpu)).
- **Full-step SDXL:** one vendor guide puts a 30-step SDXL image at 1024 px at about 13 minutes on an 8-vCPU VPS ([SSD Nodes](https://www.ssdnodes.com/learn/self-hosted-ai-image-generator)).
- **Estimate for this box (not measured):** 2–7 minutes per panel for a few-step anime SDXL model at 1024 px, so several hours for a 100-panel chapter.
- **Measured after installation (2026-10-27, this container):** Animagine XL 4.0 in diffusers, using a bf16 UNet and an fp32 VAE on 4 vCPUs with AMX.
  - **Full quality:** 832×1216, 20 Euler-a steps, CFG 5 took **205 s per panel**. The output was clean monochrome manga with screentone. One 100-panel chapter is about 5.7 hours unattended.
  - **LCM-LoRA (6 steps):** 25 s at 768×768, but the output was blurry and banded, so it is unusable with this checkpoint.
  - **Conclusion:** local generation works without any API key, but takes about 17 minutes for a 5-panel page. The hosted APIs remain faster per panel.
- **API cost for the same 100 panels:** about $1.70 with Nano Banana 2.1 in batch, $3.40 at standard price, $3 with FLUX.2 [pro] on Together, and $5.30 with GPT Image 2 at medium quality. Practitioners' 2–20× re-roll rates multiply all of these.

**The recommended setup:**
- **Orchestrator:** this Claude Code session. Claude Code has no built-in image generator, the same gap stockedge's documentation points out ([stockedge docs](https://github.com/stockedge/manga-generator/blob/main/docs/CLAUDE-CODE.md)), but it can read the story, write the script, call image APIs from Python and visually review the PNG pages.
- **Panel renderer:** Gemini Nano Banana 2.1 by default, for price and its documented character-reference slots.
- **Fallback renderer:** GPT Image 2 (medium) for complex multi-panel compositions, or for violent scenes Gemini refuses. OpenAI exposes `moderation="low"`, and Gemini has refused "blood" and "child" prompts ([r/ChatGPT](https://www.reddit.com/r/ChatGPT/comments/1umisjz/trying_to_make_a_consistent_comic_in_chatgpt_is/)).

For an unattended or batch script outside this session, use the Anthropic SDK's structured outputs to get schema-valid JSON:
- **Call:** `client.messages.parse(model="claude-opus-5-5", output_format=YourPydanticModel)` ([structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs.md)).
- **Schema limits:** no recursive schemas, and no `minimum` or `maxLength` constraints. Reference characters by `cast_id`, and enforce panel counts in Python.
- **Prior art:** AI Comic Factory's `{panel, instructions, caption}` array ([HF Space source](https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory/blob/b495b181f5ab36cb0db82c175e3294086c63995b/src/app/queries/predictNextPanels.ts)) and Veale's ComiXML, which nests scenes, panels and figures ([CEUR-WS](https://ceur-ws.org/Vol-3964/paper4.pdf)).

| Stage | Tool in this container | Licence |
|---|---|---|
| Story → page/panel script JSON (cast, settings, shot, characters, dialogue, SFX) | Claude Code session, or `anthropic` SDK with structured outputs | — |
| Character sheets (2–4 full-body + 2 head shots, anchor detail, costume lock) | `google-genai` (Nano Banana 2.1) / `openai` (GPT Image 2) | Provider terms |
| Text-free panels, rendered at panel aspect ratio, with only the in-panel references | Same SDKs; image API behind a swappable adapter | Provider terms |
| Screentone and line clean-up | ImageMagick 6 `convert -ordered-dither`, GEGL newsprint, numpy/OpenCV | IM licence / LGPL / BSD |
| Right-to-left page layout (B5/B6, 600 dpi, 2/5 mm gutters, 3–5 mm bleed) | Pillow + Shapely | MIT-CMU / BSD |
| Balloons and lettering | Pillow (English), Playwright Chromium `vertical-rl` (Japanese), drawsvg/skia-python, Shippori Antique and Comic Neue | MIT / Apache / BSD / OFL |
| QA | Claude Code reviewing the page PNGs; optional bubble detector, Kumiko `--rtl`, manga-ocr | Apache / AGPL (separate process) |
| Export | `zipfile` + ComicInfo.xml (CBZ), img2pdf (PDF), optional KCC (EPUB) | stdlib / LGPL / ISC |

These are the exact commands. Package sets were confirmed to resolve on Python 3.13 by the research. The font and KCC URLs, and the GGUF filenames, were checked on 2026-10-27. Nothing below has been run end to end.

```bash
# 0. System packages (apt lists are empty here; the session runs as root)
apt-get update
apt-get install -y fonts-noto-cjk gegl potrace 7zip
# ImageMagick 6.9.12 is preinstalled: the command is `convert`, not `magick`, e.g.
#   convert panel.png -colorspace Gray -ordered-dither h6x6a panel_tone.png

# 1. Project venv on the system Python 3.13
cd /home/user/Manga
uv venv .venv --python 3.13
source .venv/bin/activate

# 2. Core: scripting + hosted image APIs + PDF (~39 MB of wheels)
uv pip install anthropic pydantic pillow img2pdf openai google-genai fal-client replicate huggingface_hub

# 3. Layout, lettering, tone, vectorising
uv pip install shapely drawsvg skia-python uharfbuzz pyphen numpy opencv-python-headless vtracer playwright
playwright install chromium          # browser download host not yet verified through the proxy
playwright install-deps chromium     # only if Chromium reports missing system libraries

# 4. Fonts (both are SIL OFL in the Google Fonts repo)
mkdir -p fonts
curl -fsSL -o fonts/ShipporiAntique-Regular.ttf \
  https://raw.githubusercontent.com/google/fonts/main/ofl/shipporiantique/ShipporiAntique-Regular.ttf
curl -fsSL -o fonts/ComicNeue-Bold.ttf \
  https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/ComicNeue-Bold.ttf

# 5. Keys for the providers you use (Gemini has no free tier for image output)
export GEMINI_API_KEY=...        # and/or OPENAI_API_KEY=...; ANTHROPIC_API_KEY only for scripted runs outside Claude Code

# 6. OPTIONAL QA models: install CPU torch FIRST so nothing pulls CUDA wheels
uv pip install torch --index-url https://download.pytorch.org/whl/cpu
uv pip install transformers manga-ocr        # runtime on 3.13 untested
git clone https://github.com/njean42/kumiko tools/kumiko   # AGPL-3.0: call as a subprocess only

# 7. OPTIONAL e-reader export (KCC is not on PyPI; its requirements pull PySide6 on Linux)
git clone https://github.com/ciromattia/kcc tools/kcc
uv pip install -r tools/kcc/requirements.txt
python tools/kcc/kcc-c2e.py -m -p <DEVICE_PROFILE> out/pages/

# 8. OPTIONAL ready-made baseline (its own venv; it pins Pillow<13)
git clone https://github.com/phaethix/inkstone tools/inkstone
(cd tools/inkstone && uv sync --extra dev && AGNES_API_KEY=... uv run inkstone generate ../../story.txt --density B --format cbz)

# 9. OPTIONAL local CPU generation (minutes per panel)
# 9a. No compiling: FLUX.2 [klein] 4B int4 OpenVINO export (Apache-2.0, 4.6 GB, ships tokenizer files)
uv pip install openvino-genai
hf download rupeshs/flux2-klein-4b-int4-ov --local-dir models/flux2-klein-4b-int4-ov
# 9b. Anime SDXL via stable-diffusion.cpp: compiles from source, needs your approval in this session
CMAKE_ARGS="-DGGML_NATIVE=ON" uv pip install stable-diffusion-cpp-python
hf download off-grid-ai/animagine-xl-4.0-GGUF animagine-xl-4.0-Q8_0.gguf --local-dir models   # 4.18 GB
```

Disk use:
- **Core install (step 2):** about 39 MB of wheels.
- **Layout and lettering extras (step 3):** OpenCV, skia-python, Playwright and its Chromium download add more. Their size wasn't measured, but expect a few hundred MB.
- **Optional torch stack:** about 470 MB of wheels.
- **Each local model:** 4–7 GB.

With 31 GB free, keep at most two local checkpoints. The Animagine repo alone is 20.8 GB if you clone it in full ([HF API](https://huggingface.co/api/models/cagliostrolab/animagine-xl-4.0)).

The FLUX.2 klein export was chosen because it is the only one of the OpenVINO exports checked that ships the tokenizer files OpenVINO GenAI's `Text2ImagePipeline` expects. Nobody has tried loading it yet, and its quality on manga is undocumented. Animagine XL 4.0 is the licence-clean choice for authentic anime linework, but it needs the compile step.

Open questions remain:
- No CPU timing on this box has been measured.
- Whether Playwright's browser download works through the proxy is unconfirmed.
- The Gemini character-slot counts conflict between the two readings of Google's docs.
- The 2026 model IDs are reported as the vendor pages gave them.

## Conclusion

The manga-specific work is mostly in the half of the pipeline that doesn't generate images: right-to-left paneling, vertical lettering, screentone and reader-correct packaging. That half is cheap to run on a CPU, can be built entirely from permissively licensed parts, and is where human authorship earns copyright protection. So a GPU-less container is not much of a handicap for the parts that matter most. It only means renting the drawing. The design choice that matters most is architectural: keep text out of the pixels, put the image provider behind an adapter, and keep a versioned manifest of approved character sheets and locations. Two image models were shut down this month alone, and practitioners keep finding that consistency is a project-management problem before it is a model problem.

The realistic ceiling depends on length. Static, dialogue-driven stories under about ten pages can come out of this container with modest manual repair. Longer works, action-heavy chapters, and scenes where characters touch will need one of two things: per-character LoRAs trained on a rented GPU (about $1 per character), or a deliberate budget of human redraws and compositing. Where you plan to publish should be decided before production starts, not after: the same pages that qualify for KDP or pixiv with a label are disqualified from Jump+, WEBTOON contests and ComicFury.
