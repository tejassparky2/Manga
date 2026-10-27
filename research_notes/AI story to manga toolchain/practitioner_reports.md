# Practitioner Reports: Making Manga/Comics with AI (as of 2026-10-27)

> **Access limits that shape these notes (read first):**
> - **Reddit was unreachable.** Direct fetches of reddit.com/old.reddit.com redirect to a login wall (HTTP 302 to `/login/?reason=lor2`), the web-search tool refuses `reddit.com` as a domain, and an attempt to use a third-party Reddit mirror was blocked by the session's permission policy. **No Reddit thread is quoted or paraphrased here.** Claims of the form "people on r/StableDiffusion say…" are absent on purpose. Where a vendor blog asserts what "Reddit users" do, I treat it as unverified.
> - **The GitHub API was gated** in this session. GitHub pages were read through plain web fetches only (AI Comic Factory issue list, Krita AI Diffusion discussions, story-to-manga README).
> - **What substitutes for Reddit:** Hacker News (full threads via the Algolia API), Tapas creator forums (Discourse JSON), Civitai workflow pages (public API), Japanese practitioner logs (note.com, Zenn, a 120-page production write-up), primary legal documents (copyright.gov, bunka.go.jp), official platform rules, and news coverage.
> - Items dated before 2025 are labeled **[BACKGROUND]**.

## 1. Workflows experienced users recommend, from story to finished pages

### Takeaway
Hands-on practitioners from 2025–2026 converge on a staged pipeline:
1. **Script and storyboard designed first, by a human or with an LLM's help.**
2. **Character "anchors"** (reference sheets, or a character LoRA for long works).
3. **Composition control per panel** (a hand sketch, 3D mannequins or ControlNet pose/scribble/depth).
4. **Generation or cleanup panel by panel**, not whole pages in one shot, except for short gag or 4-koma strips.
5. **Manual repair, then lettering in Clip Studio Paint or Photoshop.**

One-shot page generators (GPT-Image-2, Nano Banana Pro) are now good enough for quick drafts and short strips. Nearly every serious account still budgets a manual pass and does its own lettering.

### Cited Findings

**Hacker News: practitioner workflow descriptions**
- HN commenter *elpocko*, 2025-04-26, on how comic panels get made: "You can train LoRAs on your characters for consistency. It takes seconds to generate a panel for a comic; you make a sketch, then generate hundreds of candidates, pick the best one, maybe correct flaws in Photoshop, and it's still faster and cheaper than drawing it yourself from scratch." They list img2img, ControlNet, OpenPose and InstantID as control methods. — [HN comment](https://news.ycombinator.com/item?id=43807878)
- **"Ask HN: Gen model to 1) design characters 2) make a consistent comic with them?" (2026-05-27).** The poster, working from RPG campaign notes, said the models they tried "are not consistent at all. They dont store the character design, so each panel is different in style." — [HN thread](https://news.ycombinator.com/item?id=48301635)
  - *wmf* replied: "I've seen people doing this with GPT Image 2." — [HN](https://news.ycombinator.com/item?id=48301908)
  - *vunderba* (hosted models): "build out a baseline style using text-to-image and then always add those images as 'style reference' images in future prompts e.g. 'Create a four-panel comic of bla bla bla. Use the attached images strictly as stylistic references only'." — [HN](https://news.ycombinator.com/item?id=48302016)
  - *vunderba* (self-hosting, 2026-05-30): "Really strong character consistency is usu. done by fine-tuning a custom character LoRA… you could probably get by using ControlNets… `revision` or `reference_only`… As a first step look through some of the Illustrious and/or Anima models." Recommended frontends were ComfyUI and Automatic1111, preferring "the NeoForge variant." — [HN](https://news.ycombinator.com/item?id=48337657)
  - *vunderba* on LoRA training (2026-06-01): OneTrainer "used to be the 'industry standard'," and many people use Civitai's online trainer. "more images is not necessarily better, rather the most important thing is that you caption/tag the images well." — [HN](https://news.ycombinator.com/item?id=48358079)
- *vunderba*, 2025-11-13, describing their comic pipeline: "I take advantage of this by sticking a Mistral 7b LLM in-between that takes a given prompt as an input and creates 4 variations of it before sending them all out." For style, they find Nano Banana works better "by providing a minimum of two images. The first image is intended to be transformed, and the second image is used as 'stylistic aesthetic reference'." — [HN comment](https://news.ycombinator.com/item?id=45921921)
- **Fully agentic LLM-to-comic runs.** HN user *bilater* (2026-05-14) had Claude orchestrate the whole run:
  1. Research 30 years of graphic novels.
  2. Pick a story and art style.
  3. Write the script.
  4. Break it into per-page image prompts.
  5. Call a Codex subagent to render with GPT-Image-2.

  "a few hours later I got a 25-page PDF of the graphic novel." Quality was not assessed in the thread. — [HN comment](https://news.ycombinator.com/item?id=48137188)
- **"Creating an animated manga with GPT Image 2.0 and Claude Code" (2026-05-06).** The author (*__grob*) said "it was (and still is) amazing to me that GPT Image 2.0 was this good at making a coherent manga page in one shot." They conceded "I did not give much creative direction at all… thus the AI catchphrases." A reviewer (*vunderba*) called the script "a bingo-card of all the standard AI catchphrases" and said that without specificity models gravitate "to the figurative 'mean of its training data'." — [HN thread](https://news.ycombinator.com/item?id=48038672); [blog post](https://groverburger.xyz/notes/2026-04-27-mangamotion/)

**Japanese practitioner logs (2025–2026)**
- **あやおい, note.com, 2025-12-24: two-page manga with AI in a hand-drawn workflow.** — [note.com log](https://note.com/ayaoi03072026/n/n70d5eb079619)
  - Name (storyboard) drawn in Clip Studio Paint's commercial manga template.
  - Character LoRAs trained from one standing reference plus face-less body images from several angles (about 3,000 steps). One character's reference image was generated with GPT.
  - Rough sketches drawn by hand, with 3D mannequins for crowds and backgrounds.
  - Cleanup in **Krita AI Diffusion**: sketch halved in size, live mode, then generation mode. The same settings were reused for one character across a page.
  - Crowd mannequins converted to manga-style pedestrians with **nano banana**. Wildcard prompts produced varied mob characters.
  - 3D backgrounds converted with Clip Studio's LT conversion, or rendered via nano banana/Wisk/GPT, then binarized in Clip Studio.
  - Screentone, speed lines and effects added by hand.
  - Key advice: 「AIの方が早い／手描きの方が早い」を瞬時に見極めて頭を切り替える ("instantly judge whether AI or hand-drawing is faster and switch"). Also: keep the hand-drawn workflow intact and use AI wherever it fits.
- **Itaru Tomita (Deskrex), 2026-07-17: a 120-page AI manga produced in stages (8 → 16 → 32 → 120 pages).** — [Deskrex article](https://media.deskrex.ai/ai-manga-workflow-2026/) (author's company sells AI research tools; figures are self-reported)
  - Four gates before any image generation:
    1. Script: the protagonist's change, back-calculated from key scenes (iterated with Claude Sonnet 4.6).
    2. Character assets: three face anchors (front, three-quarter, side) plus a sheet.
    3. Storyboard: one **YAML file per page** with camera, placement, balloon positions and SFX.
    4. Generation and QC.
  - For strict consistency: ComfyUI with a character LoRA, ControlNet OpenPose, Face Detailer and an upscaler.
  - Parts-based compositing: characters, backgrounds and props generated separately; SAM for layout coordinates; rembg (isnet-anime) for cutouts; PIL to composite.
  - Lettering is semi-manual in Clip Studio or Photoshop.
  - The author also calls "Nano Banana Pro + YAML" single-shot pages (about 30 min/page) the mainstream SFW option.
  - Key line: 「AI漫画の作り方で最も重要なのは、いきなり画像を生成するのではなく、設計を先に済ませることです。」("The most important thing is to finish the design before generating images.")
- **Mimi (zenn.dev/xei), 2026-02-15: 4-koma built panel by panel.** — [Zenn article](https://zenn.dev/xei/articles/ai-manga-character-consistency)
  - Each panel generated separately from a reference image; for two characters, alternating single-character cuts.
  - Reference backgrounds removed with rembg and replaced with white.
  - Page assembled in PIL (2×2 grid, right-to-left reading order, programmatic balloons).
  - Conclusion: 「静的な会話シーンの4コマ漫画なら、今のAIでも十分に実用レベル。」("For static dialogue 4-koma, current AI is practical.")
- **copainter blog (vendor), published 2025-09-30, updated 2026-10.** — [copainter blog](https://blog.copainter.ai/how-to-make-manga/)
  - Recommended split: humans do plot and name (storyboard); AI does lineart from roughs, coloring from flat colors, and backgrounds; humans finish with balloons, tones and effect lines.
  - Character preparation comes first: a reference image, three-view sheet and expression set.
  - The post explicitly rejects "having AI draw a whole episode."

**ComfyUI and Civitai workflows**
- **Mittoshura's "Comic Creator – TEXT to SEQUENCE Workflow" for ComfyUI** (Illustrious base; v1.0 2025-08-21, v1.1 2025-10-04; about 2,330 downloads of v1.1). It generates "up to 8 images at once, split into 3 sections" with LoRA and wildcard support and a "Built-In Comic Page Assembler." — [Civitai](https://civitai.com/models/1884978)
- **The same author's "Dynamic Multi-Character Workflow"** (Illustrious; v1.5 2025-10-29 through v1.7 2026-08-14) handles multiple characters per panel with regional prompts and color-based masks, giving each character its own LoRA. v1.7 "Completely revamped the ControlNet section" and added Photopea mask painting. — [Civitai](https://civitai.com/models/1669611)

**Earlier workflow threads [BACKGROUND]**
- **Krita AI Diffusion GitHub discussion #1410 (Nov–Dec 2024).** User *freecoderwaifu* suggested:
  - Lay out panels manually or in Clip Studio EX, or use a comic-layout extension for A1111/Forge.
  - Sketch each panel roughly, then use Scribble ControlNet panel by panel.
  - Retouch artifacts by hand and do a refine pass or two.
  - Alternatively, pose free 3D models and use Depth or Pose ControlNet.

  Another participant: "i am trying the same thing right now and i am getting somewhere and no where at the same time." — [GitHub discussion](https://github.com/Acly/krita-ai-diffusion/discussions/1410)
- **Takahiro Ozawa (manga writer) at CEDEC 2024 (2024-08-23).** — [Morikatron summary](https://morikatron.ai/2024/09/cedec2024_ozawa/)
  - Uses generative AI for idea generation, as a story "sparring partner" (a custom "new-serialization framework" GPT), for mass-producing character-design drafts (main character drafts for 『南緯六◯度線の約束』 came from Midjourney 4, then were reworked), and for backgrounds.
  - Background outputs were traced and corrected by human staff, mainly to replace garbled text and fix period details.
  - Background techniques he described: build a 3D skeleton and render it with Adobe Firefly, or extract lines with Sketch Edge and clean them with Copainter.
  - He archives generation settings to show he did not intentionally reproduce existing works.

**Turnkey "story → manga" apps**
- **Story to Manga (open source, Show HN 2025-09-11).**
  1. A Gemini text model extracts characters, settings and arcs.
  2. It generates character reference sheets.
  3. It splits the story into panels with dialogue.
  4. Gemini 2.5 Flash Image ("Nano Banana") renders panels using the sheets.

  Limits: stories capped at 500 words; complex plots and many characters are advised against. The author: "The hard part—and what makes it actually usable—is keeping characters consistent across panels." — [HN Show](https://news.ycombinator.com/item?id=45214302); [GitHub README](https://github.com/victorhuangwq/story-to-manga)

### Inferences
- The recommended workflow has two speeds:
  - **Fast lane:** an LLM writes the script and a YAML/shot list; a multimodal image model (GPT-Image-2 or Nano Banana Pro) renders pages or panels from reference images; humans fix and letter.
  - **Control lane:** a local SDXL-family model (Illustrious/NoobAI/Anima) with a character LoRA, ControlNet pose/scribble/depth, regional prompts and detailers, often driven from Krita AI Diffusion or ComfyUI.
- Serious long-form projects (Deskrex at 120 pages) end up in the control lane because reference-only consistency degrades over many pages.
- "Design before generating" is the most repeated piece of advice: name/storyboard, character anchors and per-page YAML.

### Gaps
- **No Reddit evidence** (see access note). I could not verify any r/StableDiffusion, r/comfyui, r/aiArt, r/AIArtCreators, r/comics, r/manga, r/webtoons, r/MachineLearning or r/LocalLLaMA workflow posts. A writer must not attribute specific claims to those subreddits from these notes.
- I did not watch YouTube tutorials (video content is not fetchable as text). No YouTube claims are included.
- I found no independent (non-vendor, non-self-reported) measurement of end-to-end workflow quality.

## 2. Tools and models praised or criticized, and the most common failure modes

### Takeaway
- **2026 hosted models:** GPT-Image-2 and Nano Banana Pro / Nano Banana 2 are praised for one-shot multi-panel coherence. They are still criticized for typos in balloons, false signatures, and messy official demos.
- **Local stack:** Illustrious-family SDXL models with character LoRAs remain the default for strict consistency and manga linework.
- **Reference-only consistency** works for short static scenes. It degrades over long works, with multiple characters in one panel, and in dynamic action.
- **Most-cited failures:** character and face drift; costume drift; two characters blending; hands, extra limbs and phantom arms; garbled or misattributed text; extreme close-ups; one-point-perspective wide panels; style "sameyness" or catchphrase writing when the model gets little direction.

### Cited Findings

**GPT-Image-2 (ChatGPT Images 2.0)**
- *vunderba*, 2026-04-22: "I was quite impressed with how faithful it adhered to the prompts given that multi-panel stuff has to maintain a sense of continuity." — [HN](https://news.ycombinator.com/item?id=47857651)
- *vunderba*, 2026-05-18: "You still have to do some manual work if you want to create something like a comic and make sure each panel is internally consistent with the world. Heck, even OpenAI's own cookbook demonstration of the dog comic was a complete mess." Also: "most people fall into the Fiverr camp… even one-shotting with the latest models, gpt-image-2 or nb2 can get you there." — [HN](https://news.ycombinator.com/item?id=48181603)
- *vunderba*, 2026-09-08 (ChatGPT Images 2.5 thread): "their 4-panel comic strip using gpt-image-2 was an absolute mess too." — [HN](https://news.ycombinator.com/item?id=49615339)
- *Legend2440*, 2026-06-30 (Nano Banana 2 Lite thread): "ChatGPT detail is a lot better though. You can do stuff like complex 6-panel comics that Nano Banana can't match." — [HN](https://news.ycombinator.com/item?id=48737312)

**Nano Banana family (Gemini image)**
- *vunderba*, 2025-11-27, on a Nano Banana Pro comic: "Definitely still needs a 'human in the loop.'… it's still got plenty of messy typos." Examples quoted: "RULES OF HOORS?" and "Updste #2". — [HN](https://news.ycombinator.com/item?id=46066433)
- *vunderba*, 2025-11-13, endorsing an article: "Nano Banana is terrible at style transfer even with prompt engineering." The workaround is to supply a second image as the style reference. — [HN](https://news.ycombinator.com/item?id=45921921)
- *hubraumhugo*, 2026-02-26: "Previous nano banana frequently made speech attribution errors, the new one [Nano Banana 2] seems a lot more consistent." — [HN](https://news.ycombinator.com/item?id=47169346)
- *gwern*, 2026-10-06: false signatures are "a perennial problem with my own generated comics with both Nano Banana Pro and ChatGPT (all generations). I often have to put in an extra edit to erase the false signature." — [HN](https://news.ycombinator.com/item?id=49972442)
- The あやおい log found nano banana useful for converting 3D mannequins and 3D backgrounds into manga-style crowds and scenes, when given a detailed prompt to keep positions and perspective. — [note.com](https://note.com/ayaoi03072026/n/n70d5eb079619)

**Local SDXL family (Illustrious / NoobAI / Anima) with LoRAs**
- vunderba recommends starting from "Illustrious and/or Anima models" and training a character LoRA for strong consistency. — [HN](https://news.ycombinator.com/item?id=48337657)
- Civitai's most-downloaded comic workflows found here are built on **Illustrious**. — [Civitai 1884978](https://civitai.com/models/1884978); [Civitai 1669611](https://civitai.com/models/1669611)
- Deskrex trained its LoRA on **Anima Base v1.0** on a RunPod RTX 4090. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
  - Also tested: Seedream v5 Pro, GPT-Image-2, Nano Banana Pro, Seedream v4.5 and Qwen.
  - Reported per-image API prices: Qwen $0.028; Seedream v4.5 $0.05; Seedream v5 Pro $0.054; GPT-Image-2 $0.058; Nano Banana Pro edit-ultra $0.15.
  - Choose one base family early because "LoRAs are not interchangeable across architectures."
  - LoRA training was effectively impossible on Apple Silicon as of July 2026.

**Reference-image methods: limits**
- Deskrex reports that reference images alone plateaued at about 60–70% consistency, with faces drifting after about 10 pages (eye angle, nose and jaw). Fix: a character LoRA trained on 15–30 images. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
  - Three reference images averaged into a blurry face; use two (one face close-up, one full body).
  - IP-Adapter Plus Face, FaceID V2, InstantID and Cosmos Reference were tested and judged insufficient.
  - FaceID V2's InsightFace detector found "0 faces" on anime faces.
- Zenn's 4-koma comparison (Flux Schnell, Flux Kontext Pro, FLUX.2 Pro, P-Image-Edit) — [Zenn](https://zenn.dev/xei/articles/ai-manga-character-consistency):
  - Text-only prompting fails: 「テキストだけでキャラを固定するのは現状ほぼ不可能」.
  - P-Image-Edit kept the anime character best, at about $0.04/page.
  - Kontext Pro was close and gave the best backgrounds.
  - FLUX.2 Pro drifted semi-realistic and dropped the logo and cat ears.
  - Limits: two characters in the same panel mix together, intense action poses break down, and the reference image's background bleeds into the output.
  - It did **not** test Nano Banana, GPT-image, Qwen-Image-Edit or Seedream.
- General editing-model comparisons, not manga-specific: one pose-transfer test found Flux Kontext preserves facial features more reliably than Qwen Edit 2509. — [MyAIForce](https://myaiforce.com/flux-kontext-pose-transfer/) (single tester; low confidence)

**Failure modes and fixes (Deskrex and あやおい)**
- *Costume drift:* "bass player" produced an invented band T-shirt and denim. Fix: a "costume lock" listing forbidden alternatives. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
- *Phantom arms:* fixed with a face-only reference, "visible arm count = 1" in the prompt, and negative prompts. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
- *Masks ignored by API editors:* one API edit ignored 8 of 12 masked areas. Fix: ComfyUI with FLUX.1 Fill treats masks as hard constraints. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
- *Unreliable automatic lettering:* fully automatic balloons and SFX have a high failure rate, so lettering stays semi-manual. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
- *Extreme close-ups* (feet, eyes or ears only) were hard to generate; *wide horizontal panels* came out in one-point perspective with the character mid-road; some panels were simply hand-drawn instead. — [note.com](https://note.com/ayaoi03072026/n/n70d5eb079619)

**Failure modes reported by app builders and critics**
- *MangaMe* builder (Show HN, 2025-07-03; GPT-4o image): "The hardest part has been getting the AI to keep characters looking the same across different panels as I only require one selfie… and sometimes the text in speech bubbles still gets jumbled." — [HN](https://news.ycombinator.com/item?id=44460087)
- *Glimora* AI comic generator (Show HN, 2025-07-02): commenter *jug* said "the generated comics have typos and seem to make little sense." — [HN](https://news.ycombinator.com/item?id=44446201)
- *crooked-v*, 2025-04-26: "The level of actual creative control isn't great, even for what should be an easy case of one character in profile against a blank background… you're wrestling the systems involved to try and produce consistent output." — [HN](https://news.ycombinator.com/item?id=43807336)
- *egypturnash*, 2026-05-21, critiquing the lettering of a suspected-AI comic: "used 'comic book' fonts but has zero idea of how word balloons actually work. Piss-poor internal margins, balloon tails that point nowhere near their supposed speaker." — [HN](https://news.ycombinator.com/item?id=48224465)
- **Expressions:** the NeurIPS 2025 Creative AI Track paper "Panel-by-Panel Souls" (Zhang, Huang, Huang, Rekimoto; arXiv 2025-11-20) says text-to-image models "struggle to produce the nuanced facial expressions that manga narratives need," which the authors attribute to the ambiguity of language. Their workflow is landmark-based face detection with manual framing, then LivePortrait expression transfer driven by performative video input. — [arXiv](https://arxiv.org/abs/2511.16038)
- AI Comic Factory (jbilcke-hf; now archived) has open issues titled "Bubbles" (2024-09-07) and "Creating more than just 4koma" (2023-12-01). Its issue list shows layout and balloons as long-standing asks. — [GitHub issues](https://github.com/jbilcke-hf/ai-comic-factory/issues?q=is%3Aissue+sort%3Acomments-desc) [BACKGROUND]

### Inferences
- In practice "consistency" splits into four separate problems: identity (face), costume, style, and multi-character separation. Each has a different fix:
  - Identity: a LoRA, or two clean references on a white background.
  - Costume: a costume lock in the prompt.
  - Style: a style-reference image.
  - Multi-character separation: regional masks, or compositing separately generated characters.
- Hosted multimodal models now win on convenience and one-shot layout. Local LoRA stacks still win on long-run identity stability and hard-mask control.
- Text in images is the most persistent weakness across every model family discussed. Practitioners treat lettering as a human step regardless of model.

### Gaps
- I found no controlled, independent manga-specific benchmark comparing Illustrious/NoobAI vs FLUX vs GPT-Image-2 vs Nano Banana Pro. Evidence here is anecdotal (HN) or from single-author tests (Zenn, Deskrex).
- I found no practitioner reports specific to Pony-family models for manga in 2025–2026; the Pony comparison asked for in the brief is unaddressed.
- A HN comment about "Gempix2" (2025-11-08) reads like promotional spam and was excluded.

## 3. Notable case studies and what creators said about process and effort

### Takeaway
- **Earlier landmarks [BACKGROUND]:** *Zarya of the Dawn* (2022–23) and *Cyberpunk: Peach John* (2023) established that prompt-and-select workflows involve heavy iteration ("hundreds or thousands" of prompts; "lottery"-like generation) and still need human selection, arrangement and editing.
- **2025–2026:** the story has shifted to commercial charts and contests in Japan, where openly AI-generated manga reached No. 1 on Comic C'moA's rankings, while Shueisha disqualified an AI manga from Jump Rookie and an award-winning Young Jump entry faced AI accusations.

### Cited Findings

**Zarya of the Dawn (Kris Kashtanova; USCO letter 2023-02-21) [BACKGROUND]** — [Copyright Office decision](https://www.copyright.gov/docs/zarya-of-the-dawn.pdf)
- The Office concluded Kashtanova "is the author of the Work's text as well as the selection, coordination, and arrangement of the Work's written and visual elements." However, "the images in the Work that were generated by the Midjourney technology are not the product of human authorship," and it reissued the registration on that basis.
- Kashtanova's counsel described the process: "hundreds or thousands of descriptive prompts," and each final image was "painstakingly shaped… over hundreds of iterations." After writing the text, "every image in the final Work was cropped, framed, and placed." Tools: "Midjourney service, Photoshop, and Comic Life 3."
- A Photoshop edit to Zarya's lips was held "too minor and imperceptible to supply the necessary creativity for copyright protection."

**Cyberpunk: Peach John (Rootport; Shinchosha, released 2023-03-09) [BACKGROUND]** — [AFP via Tech Xplore, 2023-03-06](https://techxplore.com/news/2023-03-machine-magic-art-menace-japan.html)
- Rootport said he has "absolutely zero" drawing talent.
- He used Midjourney with prompts like "pink hair," "Asian boy," "stadium jacket," and picked the best frames.
- The book is over 100 full-color pages, made in about six weeks; AFP said a skilled artist would take about a year.
- He said it "was a fun process, it reminded me of playing the lottery."
- AFP noted the same character's face sometimes "look[s] markedly different from panel to panel."
- AFP coverage summarized in search results says he avoided hand-heavy scenes as a "significant compromise." I did not fetch that article's text, so this is search-snippet level. — [Gulf News/AFP](https://gulfnews.com/amp/story/world%2Fasia%2Fmachine-magic-or-art-menace--japans-first-ai-manga-cyberpunk-peach-john-hits-the-shelves-1.1678188836451)
- Rootport's blog Q&A reportedly says nearly 9,000 images were generated. This is also search-snippet level and was not fetched. — [Rootport blog](https://rootport.hateblo.jp/entry/2023/09/08/141446)

**妻よ、僕の恋人になってくれませんか？ / My Dear Wife, Will You Be My Lover? (mamaya; STUDIO ZOON; Comic C'moA; released 2025-12-28)** — [Unseen Japan, 2026-01-08](https://unseen-japan.com/ai-manga-japan-bestseller/)
- The synopsis states "This work was produced using AI-generated images."
- It reached No. 1 in Comic C'moA's Young Adult rankings at the start of 2026 and stayed in the top five.
- mamaya had previously worked as an editor on hit series.
- Users questioned five-star reviews from accounts with no history. Critics cited "cut-and-paste AI images," cramped panels and "face manga" compositions. Several readers demanded a separate category for AI manga.
- No tools or process details were disclosed.

**NTR Kaeshi (Fukashigi-chan; Jump Rookie)** — [Automaton West, 2026-02-20](https://automaton-media.com/en/news/shonen-jump-publisher-disqualifies-ai-generated-manga-after-it-ranked-no-1-in-rookie-contest-ranking/)
- It topped the monthly Jump Rookie ranking (over 15,700 views by 2026-02-01) and was disqualified as of 2026-02-11.
- The author posted that Jump Rookie staff emailed: 「ジャンプ＋ではAI漫画は掲載できない」 ("Jump+ cannot publish AI manga"). The series was ended.

**Mikuni no Hane Hanezamsama (Morinaga Burubon)** — [Tokyo Weekender, 2025-11-28](https://www.tokyoweekender.com/entertainment/anime-and-manga/award-winning-manga-accused-of-being-ai-generated/)
- Won three prizes at Young Jump's 36th Rookie Awards (¥430,000).
- Then accused of AI use: inconsistent designs, proportion errors, "overly glossy lines," pasted-looking backgrounds, and a viral image of a female character with a beard.
- Shueisha had issued no statement. The award's rules "do not explicitly prohibit the use of AI."

**Shueisha's Manga Million (launched 2026-08-06)**
- Fans suspected AI translation despite a human-translation promise. — [Tokyo Weekender](https://www.tokyoweekender.com/entertainment/anime-and-manga/manga-million-shueisha-ai-translation-controversy/) (search-snippet level; not fetched)

**Dashtoon (India) [mostly BACKGROUND]**
- TechCrunch (2023-11-02) described a storyboard-first Dashtoon Studio, with AI-generated storyboards and dialogue planned later. — [TechCrunch](https://techcrunch.com/2023/11/02/dashtoon/)
- A Microsoft case study reports "80k+ monthly active users… content created by 200+ MAU creators… 50k+ images being created every day." The date is unclear and these are company-sourced figures. — [Microsoft](https://www.microsoft.com/en-in/aifirstmovers/dashtoon)
- I found no 2025–2026 creator first-person accounts for Dashtoon.

**Hobbyist case studies (Japan)**
- The あやおい two-page log (2025-12-24) said AI removed the step they least enjoy: 「下書きという工程が一番気乗りしない作業なんですよね…」 ("drafting is the step I'm least motivated to do"). They reported no time savings because they documented while drawing. — [note.com](https://note.com/ayaoi03072026/n/n70d5eb079619)
- The Deskrex 120-page project is described under Q1, Q2 and Q5. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)

### Inferences
- Commercial success, as in the C'moA ranking, has not settled acceptance. Each 2025–2026 Japanese case triggered calls to label or segregate AI manga. Contest gatekeepers (Jump+) are the strictest point in the pipeline.
- Creators who publish process details (Kashtanova's counsel, Rootport, あやおい, Deskrex) all describe heavy iteration and human selection or repair. None describe true one-prompt-per-page production for long-form work.

### Gaps
- I did not find first-person process statements from mamaya/STUDIO ZOON, from the NTR Kaeshi author beyond the one post, or from Morinaga Burubon.
- I did not find any 2025–2026 English-language published graphic novel with a detailed AI process write-up comparable to Zarya.
- Kashtanova's post-2023 comic work was not researched beyond its mention in the Part 2 report (Rose Enigma registration, 2023-03-21). — [Part 2 PDF](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)

## 4. Legal, platform and community context

### Takeaway
- **US:** prompts alone don't make you an author. Human text, creative selection, coordination and arrangement, perceptible human input, and creative modifications are protectable; raw AI images are not.
- **Japan:** copyrightability is case-by-case and turns on "creative contribution" (detailed expressive instructions, iterative correction, creative selection, human additions). Style alone is an idea.
- **Platforms split:** Jump+, WEBTOON contests, ComicFury and Tapas (by community account) ban AI art. pixiv and Amazon KDP require labeling or disclosure. GlobalComix (March 2026) removed fully AI works but allows AI-assisted ones. WEBTOON Canvas has no clearly documented AI rule.
- **Community reception** among comic creators remains predominantly hostile, with boycotts and reporting campaigns.

### Cited Findings

**United States** — [Part 2: Copyrightability (Jan 2025)](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)
- Released 2025-01-29. — [Sidley summary](https://datamatters.sidley.com/2025/02/07/u-s-copyright-office-issues-report-on-artificial-intelligence-and-copyrightability/)
- On prompts: "prompts alone do not provide sufficient human control to make users of an AI system the authors of the output. Prompts essentially function as instructions that convey unprotectible ideas."
- On human contributions: "Human authors are entitled to copyright in their works of authorship that are perceptible in AI-generated outputs, as well as the creative selection, coordination, or arrangement of material in the outputs, or creative modifications of the outputs."
- On comics: "the selection and arrangement of AI-generated images with human-authored text in a comic book were protectable as a compilation."
- On editing tools that allow selection and placement of elements: whether they meet the Feist standard is "a case-by-case determination." Also, "the inclusion of elements of AI-generated content in a larger human-authored work does not affect the copyrightability of the larger human-authored work as a whole."
- On expressive inputs (e.g., your own drawing as input): copyright "would cover the perceptible human expression" and "may also cover the selection, coordination, and arrangement of the human-authored and AI-generated material, even though it would not extend to the AI-generated elements standing alone."
- It cites the March 2023 AI Registration Guidance (88 Fed. Reg. 16190) and the Zarya decision.

**Japan** — [Agency for Cultural Affairs, "General Understanding on AI and Copyright in Japan" overview (May 2024)](https://www.bunka.go.jp/english/policy/copyright/pdf/94055801_01.pdf) [BACKGROUND, still current guidance]
- Copyrightability "will be determined on a case-by-case basis."
- Factors:
  - "Detailed instructions that specifically indicate what constitutes creative expression" count. "lengthy instructions (i.e., prompts) that merely suggest an idea do not."
  - "A large number of attempts alone does not affect the assessment," but "Repeated attempts, while checking the generated materials and correcting the instructions/input, may be recognized as a creative contribution."
  - "The mere act of selection itself does not influence the determination," though some choices may be creative.
  - Human "additions or corrections… that can be considered creative expressions are generally considered to be copyrighted works."
- On style: output "which applies the 'creator's style'… does not infringe copyright if the style merely encompasses an idea." Article 30-4's training exception "may not apply to AI training which 'picks off' a specific creator's style" in certain situations.

**Platform policies**
- **Shueisha Jump+ / Jump Rookie:** staff said Jump+ cannot publish AI manga, and the 2026 No. 1 entry was disqualified. — [Automaton, 2026-02-20](https://automaton-media.com/en/news/shonen-jump-publisher-disqualifies-ai-generated-manga-after-it-ranked-no-1-in-rookie-contest-ranking/)
- **WEBTOON contests:** the 2025 "Webcomic Legends" contest rules say entries "Must not be created using any form of generative artificial intelligence" and "Submissions that are found to have used generative AI will be disqualified." — [WEBTOON notice 3320](https://www.webtoons.com/en/notice/detail?noticeNo=3320)
- **WEBTOON Canvas:** I could not locate official text.
  - Third-party guides (commercial, partly conflicting) say Canvas terms and guidelines contain no AI-specific clause or uploader AI field as of mid/late 2026. — [TaleAtelier](https://taleatelier.com/webtoon-creator); [ComicPad](https://www.comicpad.app/webtoon-creator); [Comistitch](https://comistitch.com/blog/webtoon-canvas-vs-originals/) (low confidence)
  - WEBTOON launched an opt-in AI *translation* beta for Canvas in spring 2026. — [K-Comics Beat, 2026-03-26](https://kcomicsbeat.com/2026/03/26/webtoon-pushes-to-expand-indie-creators-reach-on-canvas-introduces-ai-powered-translation-program/) (search-snippet level)
- **Amazon KDP:** "We require you to inform us of AI-generated content (text, images, or translations) when you publish." "AI-generated images include cover and interior images and artwork." Content stays AI-generated "even if you applied substantial edits afterwards." AI-assisted content need not be disclosed. — [KDP Content Guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390)
- **ComicFury:** "We do not allow webcomics whose artwork was created using generative AI software (partially or in full)." — [ComicFury rules](https://comicfury.com/rules.php)
- **pixiv** (guidelines revised 2026-03-18) — [pixiv Guidelines](https://www.pixiv.net/terms/?page=guideline&lang=en)
  - "AI-generated" means "work in which all or most of the production process is carried out by AI" and "must be labeled as such."
  - For manga, labeling covers works where all or most of "the story, writing, placement, drawing" is AI. Work using AI as "secondary content" is exempt.
  - pixiv may auto-label unlabeled works.
  - Prohibited: "Repeatedly posting works/information that copy the artistic style of a specific third party."
  - Earlier 2023 pixiv news posts on AI in Requests and FANBOX appeared in search results but were not fetched. — [pixiv news 8710](https://www.pixiv.net/info.php?id=8710&lang=en)
- **Tapas:** I did not find official policy text.
  - Forum users state AI art is against the rules (e.g., "posting ai generated works on tapas is against the site's rules," 2023-06-16). — [Tapas forum](https://forums.tapas.io/t/do-you-use-ai-generated-images-in-your-comic/76858)
  - A reported AI series' pages were replaced with "will return soon with a new art style" after community reports (2023-11-20). — [Tapas forum](https://forums.tapas.io/t/ai-generated-art-okay-on-tapas/79626) [BACKGROUND]
  - In 2025 users still describe "very low tolerance of AI." A hand-drawing artist said "I had tapas almost shut me down cause people reported my art as AI." — [Tapas forum, 2025-05-30/31](https://forums.tapas.io/t/lack-of-ai-presence-on-tapas/90218)
- **GlobalComix:** a policy update (2026-03-20) removed fully AI-generated works but "doesn't prevent the use of AI within the creation process." — [Graphic Policy, 2026-03-24](https://graphicpolicy.com/2026/03/24/globalcomix-updates-its-ai-content-policy-removing-fully-ai-generated-works/); [GlobalComix AI policy](https://globalcomix.com/ai-policy) (search-snippet level; not fetched)
- **San Diego Comic-Con** banned AI-created material from its Art Show (January 2026). — [Animation Magazine](https://www.animationmagazine.net/2026/01/san-diego-comic-con-bans-ai-from-art-show) (search-snippet level; not fetched)

**Community reception**
- **Korea [BACKGROUND]:** from 2023-05-02 about 60 "AI Webtoon Boycott" comics flooded Naver Webtoon's amateur section; more than 200 cartoonists pledged participation. Naver banned AI works from its webtoon competition. — [Korea JoongAng Daily, 2023-06-10](https://www.koreajoongangdaily.com/business/creators-boycott-aigenerated-webtoons-on-naver/11866608)
- **Korea (2025):** the WEBTOON Creators Union reportedly said Naver's contract permits using works as research and AI-training data. This is via an Anime Feminist roundup of ANN and is search-snippet level. — [Anime Feminist, Nov 2025](https://www.animefeminist.com/weekly-round-up-5-11-november-2025/)
- **Japan, Piccoma (2026-05-01):** Piccoma previewed an AI-generated "ANIME" category from manga. *Maria†Holic* creator Minari Endou said webtoon creators' rights are "weak" and they can't veto such decisions. X users talked of "cut[ting] ties," calling it "synthesizing stolen goods." — [K-Comics Beat](https://kcomicsbeat.com/2026/05/01/piccoma-angers-manga-authors-and-readers-with-ai-animations/)
- **Tapas creator forum, 2025–2026:**
  - An illustrator: "Several big fields of illustration, writing etc. are 100% down… Some clients ask for sketches, don´t pay and then use my sketches with AI." — [Tapas forum, 2025-08-25](https://forums.tapas.io/t/a-personal-thought-about-generative-ai-and-its-effects-on-my-creative-process/91861)
  - On a user's AI-"enhanced" art: "If you didn't mention it, I won't be able to tell" (*kyupol*). Another found the AI version "more amateurish… abuse the airbrush tool" (*Oriflamme*). — [Tapas forum, 2025-07-02](https://forums.tapas.io/t/can-i-use-ai-to-enhance-my-own-original-artwork/90862)
- **Hacker News (split):**
  - Matthew Inman's "A cartoonist's review of AI art" (The Oatmeal, Oct 2025) drew pushback, e.g., "the 'no heart' take is just too harsh" (*DrSiemer*). Others agreed: "No decisions were made by a thinking, feeling human. There is no 'why'" (*nicbou*). — [HN thread, 2025-10-07](https://news.ycombinator.com/item?id=45507228)
  - Reaction to blog comics made with Nano Banana Pro: "it was clearly slop pictures from the first one." — [HN, 2026-03-03](https://news.ycombinator.com/item?id=47233655)
- **Academic:** an ACM paper, "AI in Webtoon Creation: Challenges, Perceptions, and Design Implications," reportedly finds readers react strongly to binary AI tags and proposes granular disclosure (e.g., AI-assisted backgrounds labeled separately). The ACM page returned HTTP 403, so this is from search-result description only. — [ACM DL](https://dl.acm.org/doi/full/10.1145/3772318.3790343)

### Inferences
- For a creator seeking copyright in the US or Japan, the defensible core is the human-authored script/text, the paneling and arrangement (selection, coordination and arrangement), and human-drawn or creatively modified elements. Keeping process records (as Ozawa does) supports both authorship and non-infringement arguments. Pure prompt-to-page output is weakest.
- Platform choice is now a design constraint:
  - Contests (Jump+, WEBTOON) and ComicFury/Tapas are effectively closed to generative-AI art.
  - KDP and pixiv permit it with disclosure or labeling. KDP's rule treats even heavily edited AI images as "AI-generated."
- Detection is mostly community-driven (reports, visual tells like hands, beards, glossy lines). False accusations against human artists are a documented side effect (Tapas, 2025).

### Gaps
- I could not verify official text for WEBTOON Canvas or Tapas AI rules; claims rely on forums and third-party guides.
- MangaPlus/Shueisha's general policy beyond Jump+/Jump Rookie and the Young Jump award was not found.
- Kodansha, Kadokawa and Shogakukan contest rules on AI were not researched.
- South Korea's AI Basic Act disclosure duty (reported effective 2026-01-22 by a commercial blog) was not verified against primary law.
- The ACM webtoon paper could not be read (HTTP 403).

## 5. Keeping human control: where human editing matters most, and time per page

### Takeaway
Practitioners concentrate human effort on:
1. Story, script and name/storyboard (paneling, camera, balloon placement).
2. Character design approval and "locks."
3. Expressions and acting.
4. Fixing hands, limbs and continuity.
5. Lettering (balloons, tails, SFX).

Reported times range from roughly 30 minutes per page (one-shot hosted model plus fixes, single self-reported case) to 1–1.5 hours per page (vendor case with AI lineart and coloring from human roughs). Hand-drawn pages are commonly several hours or more.

### Cited Findings

**Where human control matters**
- **Paneling and storyboard:** Deskrex makes storyboarding a gate before generation, with per-page YAML specifying camera, placement and balloons. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
  - copainter assigns the name/storyboard to humans (1–2 hours) and explicitly rejects having AI draw a whole episode. — [copainter](https://blog.copainter.ai/how-to-make-manga/)
  - The US Copyright Office's recognition of "selection, coordination, and arrangement" as protectable also makes paneling the legally most valuable human step. — [Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)
- **Expressions:** the Rekimoto lab paper argues text prompts are too ambiguous for manga expressions. It proposes performance-driven expression transfer with manual framing. — [arXiv 2511.16038](https://arxiv.org/abs/2511.16038)
- **Lettering:**
  - Deskrex: fully automatic lettering has a high failure rate, so it uses templates plus manual placement in Clip Studio or Photoshop.
  - copainter: "garbled text" is fixed by lettering in an editor afterwards.
  - Model-rendered text produces typos and false signatures. — [HN vunderba](https://news.ycombinator.com/item?id=46066433); [HN gwern](https://news.ycombinator.com/item?id=49972442)
  - Bad balloon craft is an instant "AI tell" to experienced cartoonists. — [HN egypturnash](https://news.ycombinator.com/item?id=48224465)
- **Creative direction:** without specific direction, outputs regress to "the figurative 'mean of its training data'." — [HN vunderba, 2026-05-06](https://news.ycombinator.com/item?id=48039446)
- **Process advice:** あやおい advises keeping the hand-drawn workflow intact and switching between AI and hand-drawing based on which is faster per panel. — [note.com](https://note.com/ayaoi03072026/n/n70d5eb079619)
  - Ozawa: whatever the AI outputs, the human mangaka judges it and chooses whether to incorporate it, and "選択には責任が伴う" (choice carries responsibility). — [Morikatron, CEDEC2024](https://morikatron.ai/2024/09/cedec2024_ozawa/) [BACKGROUND]
- **Rule of thumb:** Deskrex uses "90% automated + 10% manual" and rejects full automation. — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)

**Time estimates (all self-reported or vendor; none independently verified)**
- **Deskrex (2026-07)** — [Deskrex](https://media.deskrex.ai/ai-manga-workflow-2026/)
  - Single-shot Nano Banana Pro + YAML: about 30 min/page; one cited page took 13 generations plus inpainting and Photoshop.
  - Manual finishing: 5–10 min/page.
  - LoRA training: 30–60 min per character on an RTX 4090 (about $1 of GPU time; about $4–5 per character including reference generation).
  - Estimated money cost for 120 pages: about ¥3,600–11,500.
- **copainter (vendor) case (2025-08):** 4 pages in about 5 hours vs. an estimated 12+ hours manually. — [copainter](https://blog.copainter.ai/how-to-make-manga/)
  - Lineart 30–50 min/page with AI (vs. 2+ hours manual).
  - Coloring 20–30 min/page (vs. 1+ hour).
  - Finishing 15–30 min/page.
  - Character setup 1–2 hours the first time.
  - Manual fixes were mainly logos, text, background effects, fingers and character consistency.
- **Rootport [BACKGROUND]:** 100+ full-color pages in about six weeks (2023). — [AFP/Tech Xplore](https://techxplore.com/news/2023-03-machine-magic-art-menace-japan.html)
- **Agentic run (2026-05):** a 25-page GPT-Image-2 graphic novel in "a few hours," fully autonomous with no human art direction; quality unassessed. — [HN bilater](https://news.ycombinator.com/item?id=48137188)
- **Hand-drawn baseline anecdote (2025-06-01):** a Tapas artist said a single illustration with three people takes 8 hours. — [Tapas forum](https://forums.tapas.io/t/lack-of-ai-presence-on-tapas/90218)
- **Vendor-blog figures (low confidence):** traditional pages at 4–10 or 7–16 hours each, lettering 1–3 hours per page, LoRA setup 2–4 hours. — [aimagicx](https://www.aimagicx.com/blog/ai-comic-manga-generator-guide-2026); [comicpad](https://www.comicpad.app/how-to-create-a-comic)

### Inferences
- Time savings come mostly from lineart, coloring and backgrounds. The human-heavy steps (story, paneling, expressions, lettering, QC) don't compress much. That is consistent with copainter's "about 75% theoretically automatable" claim, Deskrex's 90/10 rule, and the legal value of arrangement.
- Per-page time in practice ranges from about 0.5 hours (short static scenes, hosted one-shot, tolerant of imperfections) to about 1.5 hours or more (AI-assisted lineart and coloring from human roughs). Fixing failure cases (hands, multi-character panels, action) can erase the gains. あやおい drew some panels by hand for this reason.

### Gaps
- I found no non-vendor, multi-creator survey of hours per page for AI-assisted manga.
- I found no data on how much time the lettering stage takes specifically in AI workflows.
- Reddit time-per-page reports (common in r/StableDiffusion and r/comfyui threads) could not be accessed.
