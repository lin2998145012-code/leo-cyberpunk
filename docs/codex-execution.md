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

| 阶段 | 内容 | 结束时 |
| --- | --- | --- |
| 0 | 画风测试：Miles 定妆照和全身候选 | **停**：导演选定 Miles 的脸和全身，同时确认画风 |
| 0.5 | 修整导演选定的定妆照和全身图，作为母版 | **停**：导演确认母版 |
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

- **生成的图里不能有任何文字**：标签、编号、视图名称、水印、签名都不行。带字的重新生成。
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
Miles: a 19-year-old wiry young man, about 168 cm, slightly hunched shoulders; narrow face, sharp chin; half-lidded tired eyes with dark under-eye circles and pale teal-grey irises; messy chin-length black hair tied into a short stubby ponytail at the nape, longer bangs with a single cyan streak in his left bangs, no shaved sides; a cheap white courier earpiece with a short microphone boom on his right ear; a thin transparent cyan AR visor across his eyes; a thigh-length deep-teal hooded rain poncho with a bright cyan reflective band along the hem and a large white Z logo printed on the back, hood down; under it a charcoal one-piece work jumpsuit with sleeves rolled up, the left leg cut off at the knee; a teal waterproof delivery bag slung across his chest; his left lower leg is a cheap scratched gunmetal prosthetic with a cracked casing and a row of five small lights; a short black rain boot on his right foot.
```

### {KEEP_MILES}
```
The character is Miles from our character references. Keep his face, tired eyes, hair and ponytail, cyan streak, earpiece, rain poncho, jumpsuit, delivery bag, prosthetic leg and colors exactly the same. Do not mirror him: the cyan streak is in his left bangs, the earpiece on his right ear, the prosthetic on his left leg. In a front view, his left side appears on the right side of the image.
```

### {ORIGINAL}
```
This is an original character and must not resemble any character in the style references: no shaved sides or shaved patterns in the hair, no jacket with a large collar, no yellow clothing, no gold chain, no tank top.
```

### {MIA}
```
Mia: a 7-year-old girl, round face, big eyes with pale teal-grey irises, short black bob haircut with straight bangs, an oversized mustard-gold knitted sweater with sleeves covering her hands, a slightly crooked golden paper crown she made herself.
```

### 2.7 Miles 的 5 个锚点（检查用）

| 锚点 | 正确 | 常见错误 |
| --- | --- | --- |
| 发型 | 及下巴的黑色乱发，后颈短小揪，**左边**刘海一缕青色挑染，**不剃发** | 剃了两侧、画了剃发图案、挑染在右边、头发太短 |
| 眼睛 | 半睁的倦眼，有黑眼圈 | 眼睛睁得很大很有神、没有黑眼圈 |
| 耳机 | **右耳**白色派单耳机，短麦克风杆 | 画到左耳、画成耳钉 |
| 雨披 | 深青色兜帽雨披，长到大腿，下摆青色反光带，**背后**白色大 Z | 画成夹克、画了大翻领、长度太短、Z 在胸前 |
| 义肢 | **左小腿**枪灰色，5 颗灯，工作服**左**裤腿在膝盖处剪掉 | 画到右腿、两条腿都正常 |

角色面向镜头时，他的左边在画面的**右侧**。左右的规则见 3.5 节：不作为淘汰标准，但从阶段 0.5 起以母版为准。另外，Miles 身上不能出现暖金色。

**和原作主角的区别**：Miles 是原创角色，只有画风和原作一样。生成的图里只要出现剃发、大翻领夹克、黄色衣服、金链子、背心中的任何一样，都算不合格。

---

## 3. 阶段 0：画风测试和 Miles 定妆

> **第 2 版。** 第 1 版的角色造型太像原作主角，已经作废（导演 2026-10-14 决定）。开始前，把第 1 版的所有文件移到 `assets/_review/stage0_v1/` 下保存，再从 c01 开始重新生成。manifest 里第 1 版的行保留，在 `notes` 里标上 `v1 作废`。

### T0.1 定妆照候选（8 张）

- 尺寸：`1024x1024`
- 风格参考：`refs/style/char_lucy_closeup.jpg`、`char_gloria_profile.jpg`、`char_dorio_action.jpg`、`light_teal_pink.jpg`
- 输出：`assets/characters/miles/portrait/miles_portrait_c01.png` … `c08.png`
- 提示词：
```
{USE_STYLE_REFS}
{ORIGINAL}
Character portrait for a model sheet: head and shoulders of a new original character, front view, looking straight at the viewer, neutral expression, the AR visor raised onto his hair so his eyes are fully visible. {SHEET}
{MILES}
{STYLE}
```

### T0.2 全身候选（6 张）

- 尺寸：`1024x1536`
- 风格参考：`refs/style/char_lucy_day.jpg`、`char_dorio_action.jpg`、`bg_station.jpg`
- 输出：`assets/characters/miles/fullbody/miles_full_c01.png` … `c06.png`
- 提示词：
```
{USE_STYLE_REFS}
{ORIGINAL}
Full-body character design of a new original character, front view, neutral standing pose, arms slightly away from the body, weight on his right leg, shoulders slightly hunched. {SHEET}
{MILES}
{STYLE}
```

### 阶段 0 结束

1. 对比图：`assets/_review/stage0_portraits.jpg`、`assets/_review/stage0_fullbody.jpg`。把候选图拼成一张，左上角标上编号（这是唯一允许出现文字的地方，编号是你后期加的）。
2. 再做一张**画风对照图** `assets/_review/stage0_style_compare.jpg`：左边放 2 张风格参考图，右边放 2 张你认为画风最接近的候选，方便导演对比。
3. REVIEW.md：每张候选写一两句客观观察，包括画风哪里像、哪里不像，**不替导演做选择**。
4. 提交、推送，然后**停下来**："阶段 0 完成，请在 `assets/selections.md` 里写下选中的定妆照和全身图编号。如果画风还不够像，请告诉我哪里不像。"

如果导演说画风不像，按导演的意见调整，重新做阶段 0。**画风没有确认之前，不要开始阶段 1。**

---

## 3.5 阶段 0.5：修整母版

### 导演的选择（2026-10-14）

| 项目 | 选中 |
| --- | --- |
| 定妆照 | `assets/characters/miles/portrait/miles_portrait_c04.png` |
| 全身图 | `assets/characters/miles/fullbody/miles_full_c05.png` |

开始前，把这两项写进 `assets/selections.md`：
```
miles_portrait: c04
miles_full: c05
```

**左右规则的更新**：导演决定，左右不再作为淘汰标准（图可以镜像使用）。但是**从这一阶段开始，所有图都以修整后的两张母版为准**：母版上挑染、耳机、义肢在哪一侧，后面的设定总图、单独视图和表情九宫格就都在同一侧。

### 为什么要修

c04 和 c05 的造型已经选定，但有几处会妨碍后面的工作：

- 整张脸被染成了紫色，这是从风格参考图的紫色灯光里学来的。设定图要用正常肤色，否则角色放进红光、白光的场景会很别扭
- 青色边缘光太强，背景有渐变。设定图需要平光
- 义肢的灯数不对（应该是 5 颗）；c05 的左裤腿是卷起来的，应该是在膝盖处剪断
- AR 目镜太厚

**修整的原则**：这是编辑，不是重画。脸、发型、表情、姿势、服装和画法都必须保持不变，只改下面列出的地方。

### T0.5.1 修整定妆照（3 个版本）

- 模型：sunburst（编辑模式）
- 输入图：`miles_portrait_c04.png`
- 风格参考（看平光下的肤色）：`refs/style/char_gloria_profile.jpg`
- 输出：`assets/characters/miles/master_fix/portrait_fix_v1..v3.png`
- 提示词：
```
Edit the input image. Keep the character, face shape, eyes, hair, ponytail, expression, pose, earpiece, outfit and drawing style exactly the same. Change only these things:
1. Skin: a warm light skin tone under flat neutral light, base color #D5906D. Keep exactly one hard-edged shadow tone, with the shadows tinted violet-indigo. Remove the overall purple cast from the face and neck.
2. Remove the strong cyan rim light along the face, hair and jacket. A very thin rim line is acceptable.
3. Background: a perfectly flat light grey, no gradient, no vignette.
4. Make the AR visor thinner: a slim transparent cyan band pushed up onto his hair.
No text.
```

### T0.5.2 修整全身图（3 个版本）

- 模型：sunburst（编辑模式）
- 输入图：`miles_full_c05.png`；第二张参考图：T0.5.1 里你自检最好的那一版（只用来对齐脸和发型）
- 输出：`assets/characters/miles/master_fix/full_fix_v1..v3.png`
- 提示词：
```
Edit the first input image. Keep the character, body proportions, hunched posture, pose, hair, rain poncho, delivery bag, jumpsuit, boots and drawing style exactly the same. The face and hair must match the second image. Change only these things:
1. Skin: a warm light skin tone under flat neutral light, base color #D5906D, with one hard-edged violet-indigo shadow tone. Remove the overall purple cast.
2. Remove the strong cyan rim light. A very thin rim line is acceptable.
3. Background: a perfectly flat light grey, no gradient. Keep only a small simple shadow under the feet.
4. Prosthetic lower leg: exactly five small round lights in one vertical row; the third light from the top is dark and broken, the other four glow white. Keep the cracks and scratches.
5. On the leg with the prosthetic, the jumpsuit leg ends just above the knee with a frayed, roughly cut edge, not rolled up.
6. Make the AR visor thinner.
No text.
```

### 自检（在 1.6 的基础上增加）

1. **和原图比，除了列出的修改，其他都没变**：脸、发型、表情、姿势、服装。变了的不合格
2. **肤色**：脸看起来是暖色的正常肤色，阴影是紫色的，但亮部不是紫色
3. 背景是纯平的浅灰
4. 全身图：义肢正好 5 颗灯，第 3 颗是暗的；裤腿是剪断的，不是卷起来的
5. 全身图的脸和发型，和修整后的定妆照对得上

每个任务最多重试 3 次。

### 阶段 0.5 结束

1. 对比图 `assets/_review/stage05_masters.jpg`：左边是原图 c04、c05，右边是修整后的各个版本，方便导演对比修了什么
2. 更新 REVIEW.md：写清楚每个版本改对了哪些、还有哪些没改对
3. 提交、推送，然后**停下来**："阶段 0.5 完成，请选定修整后的定妆照和全身图，写进 `assets/selections.md`（`miles_portrait_fix: v2`、`miles_full_fix: v1` 这样的格式）。"

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
Left two thirds: four full-body views standing side by side at exactly the same height and proportions: front view, three-quarter view of his left side, exact side profile of his left side, back view. Neutral standing pose, arms slightly away from the body; the back view shows the large white Z on the back of the poncho and the short ponytail.
Right third, top: six head studies of the same face: front, three-quarter left, profile left, three-quarter right, looking up, looking down.
Right third, bottom: close-ups of the prosthetic left lower leg, the white earpiece on his right ear, his tired eyes with dark under-eye circles, the hem of the poncho with the cyan reflective band, the AR visor.
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
| `miles_05_face_front.png` | `1024x1024` | `front head study, with the AR visor over his eyes` |
| `miles_06_face_threequarter.png` | `1024x1024` | `three-quarter left head study` |
| `miles_07_face_profile.png` | `1024x1024` | `left profile head study` |
| `miles_08_prosthetic.png` | `1792x1008` | `prosthetic leg close-up, shown twice side by side: once with the lights white and the third light broken and dark, once with all working lights glowing red` |

### T1.3 表情九宫格（2 张候选）

- 尺寸：`2048x2048`
- 参考图：`miles_portrait_master.png`、`miles_sheet_master.png`、`refs/style/char_lucy_closeup.jpg`、`refs/style/char_gloria_profile.jpg`
- 输出：`assets/characters/miles/expressions/miles_expr_grid_c01..c02.png`
- 提示词：
```
{KEEP_MILES}
{USE_STYLE_REFS}
A 3x3 grid of nine head-and-shoulders close-ups of Miles, the same face at the same slight three-quarter angle in every panel, the AR visor raised onto his hair. Each panel shows a different expression, in this order from top left to bottom right:
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
