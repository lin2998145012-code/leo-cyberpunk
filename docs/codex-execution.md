# 执行文档：用 Codex 生成前期视觉素材

> **给 Codex 的任务说明。** 请从头到尾读完再开始。
> 项目：原创动画短片《超频 OVERCLOCK》。导演是这个仓库的主人，以下简称"导演"。
> 设定来源：[人物档案](bible/characters.md)　[世界观、场景和道具](bible/world.md)　[前期制作](preproduction.md)　[原片参考分析](reference-analysis.md)

---

## 0. 你的任务

用 GPT Image 2.5 生成这部片子的**前期视觉素材**，画风要和原作动画（导演提供的风格参考图）一致。素材做好后，导演会把它们上传到 Higgsfield 去生成视频。

做法参考的是 AIGC 创作者普遍采用的流程：

1. **先锁画风，再做角色**：用风格参考图决定画法，用人物档案决定外观。
2. **先做定妆照锁住脸**，再做**人物设定总图**：四个方向的全身图、6 个角度的头像和细节特写放在**同一张图里**生成。同一次生成里的多个视图，彼此天然一致。
3. 表情用**九宫格**一次生成 9 个。
4. 场景也用**同一张图里的多机位**来保证一致。

全部工作分 6 个阶段，**每个阶段结束都要停下来等导演确认**，不要跳过确认自己往下做。

> **⛔ 全部暂停（2026-10-15）**：导演否决了第 3 版"备忘录"造型（在衣服上写字没有赛博朋克感）。新造型确定之前，**不要执行任何阶段**。
>
> **之前的状态**：故事改成了"脑仓骑手"，Miles 改成了第 3 版"备忘录"造型（见[人物档案](bible/characters.md)）。**现在只执行阶段 0（第 3 版）。** 阶段 1 以后的任务会在第 3 版定妆之后、新剧本写好之后再更新，在那之前不要执行。

| 阶段 | 内容 | 结束时 |
| --- | --- | --- |
| 0 | 第 3 版造型：Miles 定妆照、全身和背面候选 | **停**：导演选定 Miles 的脸、全身和背面 |
| 0.5 | 修整选定的图，作为母版（第 3 版选定后再写具体要求） | **停**：导演确认母版 |
| 1 | Miles 设定总图 → 单独视图 → 表情九宫格 → 一致性检查 | **停**：导演确认 Miles |
| 2 | Mia 和配角 | **停**：导演挑选 |
| 3 | 场景和道具 | **停**：导演挑选 |
| 4 | 5 张风格样张 | **停**：导演确认画风（关卡 1） |

---

## 1. 规则（必须遵守）

### 1.1 风格参考图（重要）

- 原作动画的画面截图在 **`refs/style/`** 文件夹里，共 17 张，文件名说明了用途（`char_` 人物、`light_` 光影、`bg_` 背景、`mono_` 单色画面）。
- 这些图**只用来学画法**：线条、脸和眼睛的画法、身体比例、阴影、配色。**不能复制图里的任何角色、脸、发型、服装、标志、水印、字幕或文字。**
- 这些图里有平台水印和字幕，提示词里已经要求模型忽略。**不要修改、裁剪这些图，也不要去掉水印。**
- `refs/style/` 里的图已经在仓库中。**不要修改、删除或新增这些图**，也不要复制到 `assets/` 下面。
- **风格参考图里的人物要和我们的角色尽量不像**（性别、发型、服装都不同），这样模型只能学到画法，学不到长相。所以给 Miles 用的参考图里，**不放原作男主角的截图**。
- 阶段 0 结束后，导演选定的 Miles 定妆照就成了**我们自己的风格基准**。之后的任务优先用我们自己的图当风格参考，原作截图每次最多用 2 张。

### 1.2 生图工具

- 使用你内置的图像生成工具，模型是 **GPT Image 2.5**：
  - 只用文字生成的任务用 `gpt-image-2.5-flare`
  - **带参考图的任务**用 `gpt-image-2.5-sunburst`（本文档里几乎所有任务都带参考图）
  - 如果工具不让你选模型，就用默认模型，并在 manifest 里记下实际用的是哪个
- **每次生成最多附 4 张参考图。**
- **如果内置的图像生成工具不可用，或者不接受参考图，立即停止并告诉导演。** 不要自己改用 API 密钥，那会产生额外费用，必须由导演明确同意。
- 如果生成被内容政策拒绝，把拒绝信息原样记进 REVIEW.md 并告诉导演，不要自己想办法绕过。
- 质量统一用 `high`。

### 1.3 尺寸

| 用途 | 尺寸 |
| --- | --- |
| 定妆照（胸像）、单独的头像 | `1024x1024` |
| 单人全身图 | `1024x1536` |
| 人物设定总图、场景多机位图 | `2560x1440` |
| 表情九宫格 | `2048x2048` |
| 场景、道具、风格样张（16:9） | `1792x1008` |

### 1.4 内容规则

- **生成的图里不能有任何文字**：标签、编号、视图名称、水印、签名都不行。带字的重新生成。唯一例外是 Miles 外套和手臂上看不清的马克笔笔迹（见 2.7）。
- **提示词里不能出现**任何现成作品名、工作室名、艺术家名或别的作品里的角色名。
- **不要改动设计。** 外形、颜色、左右位置都是导演定的。连续 3 次都生成不对，就记进 REVIEW.md 问导演，不要自己改提示词里的设计内容。
- **提示词整段复制，不要改写。** 第 2 节的固定块每次原样使用。

### 1.5 文件规则

- 在新分支 `codex/assets` 上工作，从当前分支切出来。
- 所有图片存成 PNG，放在 `assets/` 下，路径和文件名按任务写的来。
- 每生成一张图，都在 `assets/manifest.csv` 里加一行（格式见第 8 节），`refs` 一栏写清楚用了哪几张参考图。
- 每个阶段结束时更新 `assets/REVIEW.md`。
- **除了 `assets/` 目录，不要修改仓库里的其他文件。**
- 每个阶段结束时提交并推送。

### 1.6 自检

你能看图。每张图生成后先自己检查：
1. 有没有文字
2. **画风**：和风格参考图比，线条是不是一样细、一样干净？眼睛是不是窄而上挑、上睫毛线很粗？是不是只有一层硬边阴影、阴影带靛蓝或紫色？有没有出现原作里没有的柔和渐变、光泽感或 3D 感？
3. **有没有抄原作的角色**：脸、发型、服装是不是太像风格参考图里的某个角色？对照第 2.7 节的"和原作主角的区别"逐条检查，像的话重新生成。
4. 角色图：5 个锚点齐不齐（见第 2.7 节）。导演已决定左右不作为淘汰标准；从阶段 0.5 起，左右以修整后的母版为准，同一套设定图里要保持同一侧

不合格就重新生成，**每个任务最多重试 3 次**。3 次都不合格，保留最好的一张，在 REVIEW.md 里标出来。

### 1.7 执行说明（阶段 0 第 1 版之后补充）

- **左右**：正面图里，角色的左边在画面右侧。`{KEEP_MILES}` 已经写明，生成前后都按这个检查。
- **目镜**：任务里写了"目镜推到头上"的，以任务为准，覆盖 `{MILES}` 里"目镜横在眼前"的默认描述。
- **尺寸**：如果工具不让你设置尺寸，就在提示词最后加一句 `Output a square image.`（或者 `portrait` / `landscape`，按任务要求的比例），并在 manifest 里记录实际尺寸。**不要为了凑尺寸去裁剪、缩放或镜像。**
- **模型和质量**：工具不显示模型和质量时，manifest 里如实写 `not-exposed`。
- **提示词记录**：每次生成实际用的完整提示词，存进 `assets/_review/<阶段>_prompts.json`（你在第 1 版里已经这样做了，很好）。

---

## 2. 固定提示词块

任务里用 `{名字}` 引用。使用时替换成下面的原文，一个字都不要改。

### {USE_STYLE_REFS}
```
The style reference images show only the drawing style to copy: line quality, face and eye construction, body proportions, flat cel shading with one hard-edged shadow tone, and color handling. Draw exactly in that style. Do not copy any character, face, hairstyle, outfit, logo, watermark, subtitle or text from the style references, and ignore all text and logos in them.
```

### {STYLE}
```
2D anime TV series style with sharp, angular character design: slim, long-limbed proportions about 7.5 heads tall with a small head; angular jaw and cheekbones; narrow almond-shaped eyes with a heavy dark upper lash line that flicks outward, small irises with a single small highlight; a simple angular nose and a mouth drawn as one thin line. Thin, clean, even-weight dark lineart with very few interior lines. Flat colors with exactly one hard-edged shadow tone, large graphic shadow shapes cast across the face and body, shadows strongly hue-shifted toward indigo and violet (never grey). Hair drawn as solid sharp clumps with one flat highlight band. Clothes as big flat color blocks with bold graphic panels and stripes and few folds. Hard-edged colored rim light, saturated neon colors, no soft gradients on skin, no glossy or 3D rendering.
```

### {STYLE_BG}
```
Painted 2D anime background art: flat shapes and soft gradients with no outlines, dense glowing signs and screens, soft bloom around light sources, deep indigo and violet shadows (never grey), saturated cyan and red neon accents, light atmospheric haze, high contrast, no characters, no text.
```

### {SHEET}
```
Plain light grey background, flat even lighting, no text, no labels, no numbers, no arrows, no watermark.
```

### {MILES}
```
Miles: a 19-year-old wiry young man, about 170 cm; narrow face, sharp chin; lively narrow eyes with pale teal-grey irises and faint shadows under them, a mischievous crooked half-smile; messy black hair tied up into a small loose bun on top of his head, loose strands falling around his face, no shaved sides; a square of white medical tape on the back of his head covering a hidden data port; an oversized off-white work jacket reaching mid-thigh with the sleeves rolled up to the elbows, the whole jacket covered in handwritten black marker scribbles (illegible notes, numbers, arrows, small doodles and crossed-out lines, a few lines crossed out in red marker) and three pale cyan sticky notes stuck on it; both forearms also covered in black marker handwriting; a black marker tucked behind his ear; a fitted black high-neck shirt underneath, black cargo pants, chunky white sneakers with marker doodles.
```

### {KEEP_MILES}
```
The character is Miles from our character references. Keep his face, eyes, hair bun, the off-white jacket with its marker scribbles and sticky notes, the handwriting on his forearms, the medical tape on the back of his head, his clothes and colors exactly the same.
```

### {ORIGINAL}
```
This is an original character and must not resemble any character in the style references: no shaved sides or shaved patterns in the hair, no jacket with a large collar, no yellow clothing, no gold chain, no tank top.
```

### {LIGHT_NEUTRAL}
```
Flat neutral studio lighting: warm natural skin tone with base color #D5906D, exactly one hard-edged shadow tone tinted violet-indigo, no colored rim light, no purple or cyan cast on the skin.
```

### {MIA}
```
Mia: a 7-year-old girl, round face, big eyes with pale teal-grey irises, short black bob haircut with straight bangs, an oversized mustard-gold knitted sweater with sleeves covering her hands, a slightly crooked golden paper crown she made herself.
```

### 2.7 Miles 的 5 个锚点（检查用）

| 锚点 | 正确 | 常见错误 |
| --- | --- | --- |
| 发型 | 黑发，头顶松散的小丸子，几缕碎发垂在脸边，**不剃发** | 没有丸子、剃了两侧、扎成马尾 |
| 外套 | 宽大米白色工装外套，长到大腿中间，袖子卷到手肘，**整件写满黑色马克笔笔迹**，几行红笔划掉，3 张浅青色便利贴 | 外套是干净的、字太少、变成纯印花图案、便利贴是黄色 |
| 手臂 | 两条小臂写满黑色马克笔笔迹 | 手臂是干净的、变成纹身 |
| 后脑 | 后脑一块方形白色医用胶布 | 没有胶布、贴到脸上（只有背面图能检查） |
| 表情 | 细长灵动的眼睛，只扬起左边嘴角的坏笑 | 眼神空洞、大眼萌系、没有笑意 |

另外：Miles 身上不能出现暖金色和黄色；没有义肢、耳机、AR 目镜和雨披（第 3 版已经去掉）。

**笔迹的规则**：外套和手臂上的字是**看不清的手写笔迹和涂鸦**，不需要能读出来。这是 1.4"图里不能有文字"的唯一例外。如果模型写出了清楚可读的英文单词或句子，算不合格。

**和原作主角的区别**：Miles 是原创角色，只有画风和原作一样。生成的图里只要出现剃发、大翻领夹克、黄色衣服、金链子、背心中的任何一样，都算不合格。

---

## 3. 阶段 0：Miles 第 3 版定妆

> **第 3 版。** 第 2 版（雨披造型）已经作废（导演 2026-10-15 决定）。开始前，把第 2 版和阶段 0.5 的所有文件移到 `assets/_review/stage0_v2/` 下保存（第 1 版已经在 `stage0_v1/`），再从 c01 开始重新生成。manifest 里第 2 版的行保留，在 `notes` 里标上 `v2 作废`。`assets/selections.md` 里第 2 版的选择也标上作废。
>
> **风格参考换了**：第 2 版的脸被整体染成紫色，原因是参考图本身打着紫光。这一版只用**自然光下的原作画面**当风格参考，并且每个提示词都带上 `{LIGHT_NEUTRAL}`。

### T0.1 定妆照候选（8 张）

- 尺寸：`1024x1024`
- 风格参考：`refs/style/char_gloria_profile.jpg`、`char_lucy_day.jpg`、`char_dorio_action.jpg`
- 输出：`assets/characters/miles/portrait/miles_portrait_c01.png` … `c08.png`
- 提示词：
```
{USE_STYLE_REFS}
{ORIGINAL}
Character portrait for a model sheet: head and shoulders of a new original character, front view, looking straight at the viewer with a mischievous crooked half-smile, only the left corner of his mouth rises. The top of the jacket and the marker scribbles on it are visible. {SHEET}
{LIGHT_NEUTRAL}
{MILES}
{STYLE}
```

### T0.2 正面全身候选（6 张）

- 尺寸：`1024x1536`
- 风格参考：`refs/style/char_lucy_day.jpg`、`char_dorio_action.jpg`、`char_gloria_profile.jpg`
- 输出：`assets/characters/miles/fullbody/miles_full_c01.png` … `c06.png`
- 提示词：
```
{USE_STYLE_REFS}
{ORIGINAL}
Full-body character design of a new original character, front view, relaxed standing pose with one hand in his pocket, the jacket hanging open, a mischievous crooked half-smile. The marker scribbles on the jacket and on his forearms are clearly visible. {SHEET}
{LIGHT_NEUTRAL}
{MILES}
{STYLE}
```

### T0.3 背面全身候选（4 张）

后脑的胶布和外套背面只有背面图能看见，所以这一版提前做背面。

- 尺寸：`1024x1536`
- 风格参考：同 T0.2
- 输出：`assets/characters/miles/fullbody/miles_back_c01.png` … `c04.png`
- 提示词：
```
{USE_STYLE_REFS}
{ORIGINAL}
Full-body character design of a new original character, back view, standing, head turned slightly so the square of white medical tape on the back of his head and his hair bun are clearly visible. The back of the jacket is covered in handwritten marker scribbles. {SHEET}
{LIGHT_NEUTRAL}
{MILES}
{STYLE}
```

### 阶段 0 结束

1. 对比图：`assets/_review/stage0_portraits.jpg`、`assets/_review/stage0_fullbody.jpg`、`assets/_review/stage0_back.jpg`。候选图拼在一起，左上角标上编号（编号是你后期加的）。
2. 画风对照图 `assets/_review/stage0_style_compare.jpg`：左边放 2 张风格参考图，右边放 2 张你认为画风最接近的候选。
3. REVIEW.md：每张候选写一两句客观观察，**特别写清楚**：笔迹是不是看不清的手写（没有可读的英文）、肤色是不是正常（没有整体发紫）、像不像原作的某个角色。**不替导演做选择。**
4. 提交、推送，然后**停下来**："阶段 0（第 3 版）完成，请选定定妆照、正面全身和背面的编号。"

**画风和造型没有确认之前，不要开始后面的阶段。**

---

## 3.5 阶段 0.5：修整母版

第 3 版选定以后，导演和 Claude 会根据选中的图再写具体的修整要求。**在那之前不要执行。**

---

## 4. 阶段 1：Miles 设定总图

**开始前**：读 `assets/selections.md`，把阶段 0.5 选中的**修整版**定妆照复制成 `assets/characters/miles/miles_portrait_master.png`，修整版全身图复制成 `assets/characters/miles/miles_full_master.png`。**选定之后不再重新生成这两张。**

### T1.1 人物设定总图（3 张候选）

- 尺寸：`2560x1440`
- 参考图：`miles_portrait_master.png`、`miles_full_master.png`、`refs/style/char_lucy_day.jpg`、`refs/style/char_dorio_action.jpg`
- 输出：`assets/characters/miles/sheet/miles_sheet_c01..c03.png`
- 提示词：
```
{KEEP_MILES}
{USE_STYLE_REFS}
{ORIGINAL}
A professional character model sheet of Miles in one image. Layout:
Left two thirds: four full-body views standing side by side at exactly the same height and proportions: front view, three-quarter view of his left side, exact side profile of his left side, back view. Neutral standing pose, arms slightly away from the body; the back view shows the medical tape on the back of his head, the hair bun and the scribbles on the back of the jacket.
Right third, top: six head studies of the same face: front, three-quarter left, profile left, three-quarter right, looking up, looking down.
Right third, bottom: close-ups of the medical tape on the back of his head, his forearm covered in marker handwriting, a patch of the jacket with scribbles and a sticky note, the black marker, his eyes.
Along the bottom edge: a row of plain color swatches of his colors.
{SHEET}
{MILES}
{STYLE}
```

### 阶段 1 中途确认

做完 T1.1 先停下来，把 3 张候选给导演挑，导演把选中的编号写进 `assets/selections.md`（`miles_sheet: c02`）。选中的复制成 `assets/characters/miles/miles_sheet_master.png`。

### T1.2 单独视图（从设定总图里重画成大图）

设定总图上每个视图都太小，所以要单独重画成大图。**设计以设定总图为准。**

- 参考图：`miles_sheet_master.png`、`miles_portrait_master.png`、`miles_full_master.png`
- 输出：`assets/characters/miles/pack/`
- 提示词 = `{KEEP_MILES}` + `Redraw only the ` + 下表的视图 + ` from the model sheet as a single large image, with exactly the same design, proportions and colors.` + `{SHEET}` + `{STYLE}`

| 文件名 | 尺寸 | 视图 |
| --- | --- | --- |
| `miles_01_front_full.png` | `1024x1536` | `front full-body view` |
| `miles_02_threequarter_full.png` | `1024x1536` | `three-quarter full-body view of his left side` |
| `miles_03_side_full.png` | `1024x1536` | `side profile full-body view of his left side` |
| `miles_04_back_full.png` | `1024x1536` | `back full-body view` |
| `miles_05_face_front.png` | `1024x1024` | `front head study` |
| `miles_06_face_threequarter.png` | `1024x1024` | `three-quarter left head study` |
| `miles_07_face_profile.png` | `1024x1024` | `left profile head study` |
| `miles_08_details.png` | `1792x1008` | `detail close-ups side by side: the medical tape on the back of his head, his forearm covered in marker handwriting, a patch of the jacket with scribbles and a sticky note` |

### T1.3 表情九宫格（2 张候选）

- 尺寸：`2048x2048`
- 参考图：`miles_portrait_master.png`、`miles_sheet_master.png`、`refs/style/char_lucy_closeup.jpg`、`refs/style/char_gloria_profile.jpg`
- 输出：`assets/characters/miles/expressions/miles_expr_grid_c01..c02.png`
- 提示词：
```
{KEEP_MILES}
{USE_STYLE_REFS}
A 3x3 grid of nine head-and-shoulders close-ups of Miles, the same face at the same slight three-quarter angle in every panel. Each panel shows a different expression, in this order from top left to bottom right:
1 neutral; 2 determined, jaw set, eyes narrowed; 3 exhausted and out of breath, sweat on his face; 4 tender smile, only the left corner of his mouth rises; 5 shocked, eyes wide; 6 holding back tears, lips pressed together; 7 gritted teeth in pain; 8 smug crooked smile, only the left corner of his mouth rises; 9 empty, hollow stare.
Thin gutters between the panels. {SHEET}
{STYLE}
```

### T1.4 一致性检查

1. 按 `tools/check_consistency.py` 文件开头的说明建虚拟环境、装依赖。第一次运行会从 HuggingFace 下载模型。
2. 建好 `assets/characters/miles/master_ref/`，放入 `miles_portrait_master.png` 和 `miles_full_master.png` 两张，然后运行：
```bash
python tools/check_consistency.py --ref assets/characters/miles/master_ref/ --shots assets/characters/miles/pack/ -o assets/_review/miles_pack_consistency.csv
```
3. 标为"返工候选"的图，加上你自检时锚点不对的图，重新生成，每张最多 2 次，然后再跑一遍检查。
4. 把报告的前 5 行和锚点检查结果写进 REVIEW.md。工具只负责排序，最后由人眼判断；两者冲突时，两种结论都写下来。

如果你的运行环境下载不了模型，就跳过这一步，在 REVIEW.md 里说明。

### 阶段 1 结束

1. 对比图：`assets/_review/stage1_miles.jpg`，包括设定总图、8 张单独视图和表情九宫格
2. 更新 REVIEW.md，提交、推送
3. **停下来**："阶段 1 完成，请确认 Miles 的设定总图、单独视图和表情九宫格，并在 `assets/selections.md` 里写下选中的表情九宫格。"

---

## 5. 阶段 2：Mia 和配角

> **暂停**：阶段 2–4 是按旧剧本（外卖骑手）写的，要等新剧本写好后更新。在那之前不要执行。

从这一阶段开始，**风格参考优先用我们自己的图**：`miles_sheet_master.png` 和 `miles_portrait_master.png`，原作截图最多加 1 张。

### T2.1 Mia 定妆照（6 张候选）

- 尺寸：`1024x1024`
- 参考图：`miles_portrait_master.png`（只学画风，**不是**要画 Miles）、`refs/style/char_lucy_closeup.jpg`
- 输出：`assets/characters/mia/portrait/mia_portrait_c01..c06.png`
- 提示词：
```
{USE_STYLE_REFS}
The reference images are style references only; draw a new character. Character portrait: head and shoulders of a 7-year-old girl, front view, a bright smile. {SHEET}
{MIA}
{STYLE}
Child proportions: a larger head and rounder face than an adult, while keeping the same line and shading style.
```

**停下来**，等导演选定 Mia 的定妆照，复制成 `assets/characters/mia/mia_portrait_master.png`。

### T2.2 Mia 设定图（2 张候选）

- 尺寸：`2560x1440`
- 参考图：`mia_portrait_master.png`、`miles_sheet_master.png`（只学版式和画风）
- 输出：`assets/characters/mia/sheet/mia_sheet_c01..c02.png`
- 提示词：
```
The girl is Mia from the portrait reference. Keep her face, hair, sweater, paper crown and colors exactly the same. Use the layout and drawing style of the model sheet reference, but draw only Mia.
A character model sheet of Mia in one image: left half, three full-body views at the same height: front, side, back. Right half, top: three head studies: front, three-quarter, profile. Right half, bottom: four small head close-ups with expressions: laughing, pouting, sleepy, excited.
{SHEET}
{MIA}
{STYLE}
```

### T2.3 Mia 锁屏照片（3 张）

- 尺寸：`1024x1536`
- 参考图：`mia_portrait_master.png`、Mia 选中的设定图
- 输出：`assets/characters/mia/mia_photo_v1..v3.png`
- 提示词：
```
The girl is Mia from the references. Keep her face, hair, sweater, paper crown and colors exactly the same.
A phone photo of Mia at home, smiling at the camera with both hands raised, showing off her paper crown. Warm golden indoor light, slightly overexposed edges like a phone beauty filter, a cozy small room in the background, no text.
{MIA}
{STYLE}
```

### T2.4 配角设定图（各 3 张候选）

- 尺寸：`1792x1008`
- 参考图：`miles_sheet_master.png`（只学画风）、`refs/style/char_fullbody_station.jpg`
- 输出：`assets/characters/<robot|drone|mascot>/<名字>_c01..c03.png`
- 提示词 = `{USE_STYLE_REFS}` + 下表内容 + `{SHEET}` + `{STYLE}`

| 名字 | 内容 |
| --- | --- |
| `robot` | `Design sheet of a small delivery service robot: white egg-shaped body on wheels, about 80 cm tall, a round screen face showing a simple smiling face, two thin mechanical arms, a cyan Z-shaped logo on its body. Front, side and back views.` |
| `drone` | `Design sheet of a black police drone: four rotors, a single red mechanical eye with an iris that can contract, red and blue police lights on both sides. Front, side, top views and a close-up of the eye.` |
| `mascot` | `Mascot design of a cheerful cartoon delivery rider: big head, smiling closed eyes, giving a thumbs up, wearing a brand-new deep-teal hooded rain poncho with a cyan reflective band and a white Z logo, both legs normal and healthy. Front view and a three-quarter view. Simpler and rounder than the main characters, like an advertising mascot.` |

### 阶段 2 结束

对比图 `assets/_review/stage2_cast.jpg`，更新 REVIEW.md，提交、推送，**停下来**等导演挑选。

---

## 6. 阶段 3：场景和道具

### T3.1 场景全景（6 个场景，各 3 张候选）

- 尺寸：`1792x1008`
- 输出：`assets/locations/<场景>/<场景>_c01..c03.png`
- 提示词 = `{USE_STYLE_REFS}` + 场景描述 + `{STYLE_BG}`
- 每个场景用的风格参考：

| 场景文件夹 | 风格参考 | 描述 |
| --- | --- | --- |
| `L1_shaft` | `bg_city_window`、`light_club_purple` | `Straight-down aerial view into a vast vertical city shaft at night: dozens of stacked elevated highways spiral down the walls of the shaft into darkness, thousands of tiny cyan car lights flow along them like current on a circuit board, rain falling toward the camera, deep indigo and violet buildings with small neon signs.` |
| `L2_highway` | `bg_city_window`、`bg_station` | `An elevated highway suspended between skyscrapers at night, completely jammed: a convoy of black armored corporate vehicles blocks all lanes, police drones with red and blue lights hover above, rain, wet car roofs reflecting cyan and red neon, deep indigo ambient light. Wide front view.` |
| `L3_adwall` | `bg_city_window`、`light_club_purple` | `A skyscraper facade next to an elevated highway at night, the entire wall is a giant illuminated advertisement showing a cheerful cartoon delivery rider mascot giving a thumbs up, the slogan area left blank. Rain, cyan and white light from the ad, deep indigo surroundings.` |
| `L4_corridor` | `bg_corp_hall`、`char_gloria_profile` | `A long, spotless corridor at the top of a corporate tower: white walls, glossy floor, thin cyan light strips along the ceiling, a glass door at the far end. Pale sterile white-cyan light, low saturation, perfectly symmetrical one-point perspective.` |
| `L5_lobby` | `bg_corp_hall`、`char_gloria_profile` | `An empty, spotless white delivery lobby at the top of a corporate tower: a package scanner on the wall with a blank cyan screen, a glossy white floor, a small cyan Z-shaped logo on the wall. Pale sterile white-cyan light, low saturation, clean and silent. Wide fixed shot.` |
| `L6_rooftop` | `bg_city_window`、`light_rimsilhouette` | `The edge of a skyscraper rooftop at night, the whole vertical city glowing far below, strong wind, a low metal railing, dark indigo sky, distant cyan and red city lights. Lonely, quiet atmosphere. Extreme wide shot.` |

风格参考文件都在 `refs/style/` 下，后缀是 `.jpg`。

**停下来**，等导演选定每个场景的全景，复制成 `<场景>_master.png`。

### T3.2 场景多机位图（需要多个角度的 4 个场景）

在同一张图里生成同一个场景的多个角度，保证一致。

- 尺寸：`2560x1440`
- 参考图：该场景的 `<场景>_master.png`
- 输出：`assets/locations/<场景>/<场景>_angles.png`
- 提示词 = `A 2x2 grid showing the same location as the reference image from four camera angles, with the same design, lighting and colors in all four panels: ` + 下表的四个角度 + `. Thin gutters between panels.` + `{STYLE_BG}`

| 场景 | 四个角度 |
| --- | --- |
| `L2_highway` | `1 wide front view; 2 side view along the jam; 3 low angle from just above a car roof; 4 high angle looking down on the convoy` |
| `L3_adwall` | `1 extreme high-angle fisheye view from the highway edge straight down the 100-story drop beside the facade; 2 medium view of the facade with the mascot's face and thumbs up; 3 low angle looking up the facade; 4 side view of the facade from the highway` |
| `L5_lobby` | `1 wide fixed shot; 2 close-up of the package scanner; 3 reverse angle toward the corridor door; 4 low angle across the glossy floor` |
| `L6_rooftop` | `1 extreme wide shot; 2 medium shot of the railing; 3 close view of the railing with the city lights far below strongly out of focus; 4 looking straight down from the edge` |

然后把镜头需要的角度单独重画成 `1792x1008` 的大图，命名为 `<场景>_<角度编号>.png`，比如 `L3_adwall_1.png`。提示词：`Redraw only panel [编号] of the reference grid as a single large image, with exactly the same design, lighting and colors.` + `{STYLE_BG}`。

### T3.3 道具设定图（6 件，各 2 张候选）

- 尺寸：`1792x1008`
- 参考图：`miles_sheet_master.png`（只学画风）
- 输出：`assets/props/<道具>/<道具>_c01..c02.png`
- 提示词：
```
{USE_STYLE_REFS}
Prop design sheet of {道具描述}, multiple orthographic views (front, side, back, top), consistent proportions. {SHEET}
{STYLE}
```

| 文件夹 | {道具描述} |
| --- | --- |
| `scooter` | `an old courier electric scooter, deep teal body, a phone mount on the handlebar, a dented mudguard` |
| `deliverybag` | `a teal waterproof courier delivery bag worn slung across the chest, a cyan Z-shaped logo, a roll-top closure, worn edges and scratches` |
| `phone` | `a cheap smartphone with a crack across the top right corner of a blank black screen` |
| `cupcake` | `a squashed cupcake with white frosting and one small strawberry, inside a clear plastic box` |
| `lighter` | `a cheap transparent plastic lighter with visible fuel inside and a flint wheel` |
| `package` | `a small white cardboard parcel box with a blank white label` |

### 阶段 3 结束

对比图 `assets/_review/stage3_locations.jpg`、`assets/_review/stage3_props.jpg`，更新 REVIEW.md，提交、推送，**停下来**等导演挑选。

---

## 7. 阶段 4：风格样张（关卡 1）

每个段落一张，把色彩剧本变成画面。

- 尺寸：`1792x1008`，每张 3 个版本：`_v1..v3`
- 参考图（4 张）：`miles_sheet_master.png`、`miles_portrait_master.png`、对应场景的 master、下表的光影参考
- 输出：`assets/style_frames/`
- 提示词 = `{KEEP_MILES}` + `{USE_STYLE_REFS}` + 下表的画面 + `The whole figure takes on the color of the ambient light.` + `{STYLE}`

| 文件名 | 光影参考 | 画面 |
| --- | --- | --- |
| `SF1_rain_night` | `light_teal_pink` | `Medium shot: Miles rides an electric scooter through the jammed elevated highway in the rain, looking down at a phone on the handlebar. Night, rain, deep indigo ambient light, cyan neon rim light from the left, cyan HUD glow on his face.` |
| `SF2_jam` | `light_rimsilhouette` | `Wide shot: Miles stops at the edge of the jammed highway, the black convoy and police drones ahead, he looks down at his prosthetic leg. Night, rain, deep indigo ambient light, red and blue police lights mixing with cyan neon.` |
| `SF3_overclock` | `char_dorio_action` | `Low-angle full shot: Miles crouches on a car roof after landing, rain drops frozen in the air around him, a trail of floating cyan HUD numbers behind him. Night, rain, deep indigo ambient light, cyan neon rim light from the left.` |
| `SF4_lobby` | `char_gloria_profile` | `Wide fixed shot: Miles kneels exhausted in the spotless white delivery lobby while a small white service robot takes a parcel from him. Pale sterile white-cyan light, low saturation.` |
| `SF5_rooftop` | `light_rimsilhouette` | `Medium close-up: Miles sits at the rooftop edge, a single small lighter flame lit in his trembling hand, the city glowing far below. Dark indigo night; the warm flame lighting his face from below is the only warm color in the frame.` |

**SF3 的红色预览**：成片里这一段是整屏红色单色，在后期统一加。为了让导演提前看到效果，给每个 SF3 版本额外做一张预览：用 Python 把图转成亮度图，再从暗到亮映射到 `#140E1E` → `#B02324` → `#E83F34` → `#EDF5ED`，高饱和的青色像素（HUD 数字）不映射。存成 `SF3_overclock_v1_redpreview.png`，其他版本依此类推。可以和原作的 `refs/style/mono_red_fight.jpg` 对比一下。

### 阶段 4 结束

对比图 `assets/_review/stage4_style_frames.jpg`，旁边放上对应的原作光影参考图，方便导演对比。更新 REVIEW.md，提交、推送，然后**停下来**："阶段 4 完成，请确认风格样张。确认后，就可以把素材上传到 Higgsfield 了。"

---

## 8. 记录文件的格式

### assets/manifest.csv

```
task,file,model,size,quality,refs,attempt,self_check,notes
T0.1,assets/characters/miles/portrait/miles_portrait_c01.png,gpt-image-2.5-sunburst,1024x1024,high,char_lucy_closeup;char_gloria_profile;char_dorio_action;light_teal_pink,1,pass,
```

`self_check` 填 `pass`、`fail` 或 `unsure`；`notes` 写不合格的原因或需要导演注意的地方。

### assets/selections.md（导演填写）

```
miles_portrait: c03
miles_full: c02
miles_sheet: c01
miles_expr_grid: c02
mia_portrait: c04
...
```

### assets/REVIEW.md

每个阶段一节：每张候选的客观观察，画风像在哪里、不像在哪里，以及需要导演决定的问题。不替导演做选择。

---

## 9. 之后的事（不属于 Codex 的任务）

导演确认风格样张之后：
1. **只把我们自己生成的素材上传到 Higgsfield**。`refs/style/` 里的原作截图不上传：Higgsfield 的版权过滤会拦截，而且没有必要，因为画风已经体现在我们自己的素材里了。
2. 在 Higgsfield 上创建 Element `Miles`，用 Wan 3.0 做试镜（关卡 2）
3. 生成镜头的关键帧和视频，见 [Wan 3.0 七天计划](wan3-7day-plan.md)
