# 执行文档：用 Codex 生成前期视觉素材

> **给 Codex 的任务说明。** 请从头到尾读完再开始。
> 项目：原创动画短片《超频 OVERCLOCK》。导演是这个仓库的主人，以下简称"导演"。
> 设定来源：[人物档案](bible/characters.md)　[世界观、场景和道具](bible/world.md)　[前期制作](preproduction.md)

---

## 0. 你的任务

用 GPT Image 2.5 生成这部片子的**前期视觉素材**：角色定妆、角色设定包、配角、场景、道具和风格样张。素材生成后，导演会把它们上传到 Higgsfield，用来生成视频。

整个任务分 3 个阶段，**每个阶段结束时都要停下来，等导演确认**。不要跳过确认，自己继续往下做。

| 阶段 | 内容 | 结束时 |
| --- | --- | --- |
| 阶段 1 | 角色、配角、场景、道具的候选图 | **停**：导演挑选 |
| 阶段 2 | Miles 设定包、Mia 锁屏照片、场景的其他角度，并做一致性检查 | **停**：导演确认设定包 |
| 阶段 3 | 5 张风格样张 | **停**：导演确认画风（关卡 1） |

---

## 1. 规则（必须遵守）

### 1.1 生图工具

- 使用你内置的图像生成工具，模型是 **GPT Image 2.5**：
  - **只用文字生成的任务**（候选图、场景全景、道具）用 `gpt-image-2.5-flare`
  - **带参考图的任务**（设定包、角度图、风格样张）用 `gpt-image-2.5-sunburst`，它的编辑精度更高
  - 如果工具不让你选模型，就用默认模型，并在 manifest 里记下实际用的是哪个
- **如果内置的图像生成工具不可用，立即停止并告诉导演。** 不要自己改用 API 密钥调用 OpenAI 的接口，那会产生额外费用，必须由导演明确同意。
- 质量统一用 `high`。

### 1.2 尺寸

| 用途 | 尺寸 |
| --- | --- |
| 全身图、竖构图 | `1024x1536` |
| 脸部特写、表情 | `1024x1024` |
| 场景、风格样张、多角度设定图（16:9） | `1792x1008` |

### 1.3 内容规则

- **图里不能出现任何文字**：标签、标注、水印、签名、视图名称（比如 "FRONT"）都不行。生成出来带字的，重新生成。
- **提示词里不能出现**任何现成作品名、工作室名、艺术家名或别的作品里的角色名。版权过滤会拦截，而且这是原创作品。
- **不要改动设计。** 提示词里写的外形、颜色、左右位置都是导演定的。连续 3 次都生成不对的，在 REVIEW.md 里记下来，问导演，不要自己改提示词里的设计内容。
- **提示词整段复制，不要改写。** 第 2 节的固定块每次都原样使用。

### 1.4 文件规则

- 在一个新分支上工作：`codex/assets`，从当前分支切出来。
- 所有图片存成 PNG，放在 `assets/` 下，路径和文件名按每个任务写的来。
- 每生成一张图，都在 `assets/manifest.csv` 里加一行（格式见第 7 节）。
- 每个阶段结束时更新 `assets/REVIEW.md`（格式见第 7 节）。
- **除了 `assets/` 目录，不要修改仓库里的其他文件。**
- 每个阶段结束时提交并推送，提交信息写清楚是哪个阶段。

### 1.5 你能自己检查的事

你可以看图。每张图生成后，自己先检查一遍：
- 有没有文字
- 角色图：5 个锚点对不对，**左右有没有反**（见第 2.4 节）
- 设定图：背景是不是浅灰纯色、光线是不是均匀

不合格的直接重新生成，**每个任务最多重试 3 次**。3 次都不合格，就保留最好的一张，在 REVIEW.md 里标出来。

---

## 2. 固定提示词块

下面的块在任务里用 `{名字}` 引用。**使用时替换成下面的原文，一个字都不要改。**

### {MILES}
```
Miles: a 19-year-old slim young man, narrow face, sharp chin, narrow upturned eyes with pale teal-grey irises, a vertical scar cutting through his left eyebrow, short black hair with the right side shaved and a single cyan streak in his left fringe, three small silver studs in his right ear, a square metal data port on the left side of his neck with a tiny red light, oversized deep-teal courier jacket with bright cyan reflective stripes and a high collar, black cargo pants with the left leg cut off at the knee, left lower leg is a cheap scratched gunmetal prosthetic with a cracked casing and a row of five small lights, a thin transparent cyan AR visor across his eyes.
```

### {MIA}
```
Mia: a 7-year-old girl, round face, big eyes with pale teal-grey irises, short black bob haircut with straight bangs, an oversized mustard-gold knitted sweater with sleeves covering her hands, a slightly crooked golden paper crown she made herself.
```

### {STYLE}
```
2D anime TV series style, flat cel shading with a single hard-edged shadow tone, thin clean dark lineart of even weight, bold saturated colors, shadows tinted deep indigo and violet (never grey), hard-edged cyan rim light, high contrast, angular expressive character design.
```

### {BG_STYLE}
```
2D anime TV series background art, flat colors, clean shapes, detailed environment, shadows tinted deep indigo and violet (never grey), high contrast, no characters, no text.
```

### {SHEET}
```
Plain light grey background, flat even lighting, no text, no labels, no watermark.
```

### {KEEP_MILES}
```
The character is Miles from the reference images. Keep his face, hair, cyan streak, eyebrow scar, ear studs, neck port, jacket, prosthetic leg and colors exactly the same as in the references. Do not mirror the character: the cyan streak and scar are on his left side, the ear studs on his right ear, the prosthetic on his left leg.
```

### 2.4 Miles 的 5 个锚点（检查用）

| 锚点 | 正确 | 常见错误 |
| --- | --- | --- |
| 青色挑染 | **左边**刘海 | 画到右边、挑染太多、整头染色 |
| 疤 | 竖疤切断**左眉** | 画到右眉、横疤、没有疤 |
| 耳钉 | **右耳**三颗银色 | 画到左耳、数量不对、金色 |
| 颈部接口 | **左颈**方形金属，一颗小红灯 | 画到右边、圆形 |
| 义肢 | **左小腿**枪灰色，5 颗灯，**左**裤腿在膝盖处剪掉 | 画到右腿、两条腿都正常、整条腿都是机械 |

注意：角色**面向镜头**时，他的左边在画面的**右侧**。检查时以角色自己的左右为准。

另外：**Miles 身上不能出现暖金色**，金色只属于 Mia。

---

## 3. 阶段 1：候选图

本阶段的任务互相独立，可以按任意顺序做。

### T1.1 Miles 定妆候选（12 张）

- 模型：flare　尺寸：`1024x1536`
- 输出：`assets/characters/miles/candidates/miles_c01.png` … `miles_c12.png`
- 提示词：
```
Character design, full body, front view, neutral standing pose, arms relaxed at his sides. {SHEET}
{MILES}
{STYLE}
```
- 12 张都用同一个提示词。想要的是**同一个设计的不同诠释**，供导演挑选。
- 自检：5 个锚点。左右错了的不算候选，重新生成补足 12 张。

### T1.2 Mia 定妆候选（6 张）

- 模型：flare　尺寸：`1024x1536`
- 输出：`assets/characters/mia/candidates/mia_c01.png` … `mia_c06.png`
- 提示词：
```
Character design, full body, front view, standing with both hands holding the edge of her paper crown, a shy smile. {SHEET}
{MIA}
{STYLE}
```

### T1.3 配角设定图（各 3 张）

模型：flare　尺寸：`1792x1008`

| 编号 | 输出 | 提示词 |
| --- | --- | --- |
| T1.3a | `assets/characters/robot/robot_c01..03.png` | `Character design sheet of a small delivery service robot: white egg-shaped body on wheels, about 80 cm tall, a round screen face showing a simple smiling face, two thin mechanical arms, a cyan Z-shaped logo on its body. Front, side and back views. {SHEET}` 后接 `{STYLE}` |
| T1.3b | `assets/characters/drone/drone_c01..03.png` | `Design sheet of a black police drone: four rotors, a single red mechanical eye with an iris that can contract, red and blue police lights on both sides. Front, side, top views and a close-up of the eye. {SHEET}` 后接 `{STYLE}` |
| T1.3c | `assets/characters/mascot/mascot_c01..03.png` | `Mascot design of a cheerful cartoon delivery rider: big head, smiling closed eyes, giving a thumbs up, wearing a brand-new deep-teal courier jacket with bright cyan reflective stripes, both legs normal and healthy. Front view and a three-quarter view. Plain light grey background, flat colors, no text.` |

### T1.4 场景全景（6 个场景，各 3 张）

- 模型：flare　尺寸：`1792x1008`
- 输出：`assets/locations/L1_shaft/L1_c01..03.png`，其他场景同理（`L2_highway`、`L3_adwall`、`L4_corridor`、`L5_lobby`、`L6_rooftop`）
- 每个场景的提示词 = 下表的描述 + 一个空格 + `{BG_STYLE}`

| 场景 | 描述 |
| --- | --- |
| L1 天井 | `Straight-down aerial view into a vast vertical city shaft at night: dozens of stacked elevated highways spiral down the walls of the shaft into darkness, thousands of tiny cyan car lights flow along them like current on a circuit board, rain falling toward the camera, deep indigo and violet buildings with small neon signs.` |
| L2 高架 | `An elevated highway suspended between skyscrapers at night, completely jammed: a convoy of black armored corporate vehicles blocks all lanes, police drones with red and blue lights hover above, rain, wet car roofs reflecting cyan and red neon, deep indigo ambient light. Wide front view.` |
| L3 广告墙 | `A skyscraper facade next to an elevated highway at night, the entire wall is a giant illuminated advertisement showing a cheerful cartoon delivery rider mascot giving a thumbs up, the space left blank where the slogan will go. Rain, cyan and white light from the ad, deep indigo surroundings.` |
| L4 走廊 | `A long, spotless corridor at the top of a corporate tower: white walls, glossy floor, thin cyan light strips along the ceiling, a glass door at the far end. Pale sterile white-cyan light, low saturation, perfectly symmetrical one-point perspective.` |
| L5 大厅 | `An empty, spotless white delivery lobby at the top of a corporate tower: a package scanner on the wall with a blank cyan screen, a glossy white floor, soft elevator-lobby atmosphere, a small cyan Z-shaped logo on the wall. Pale sterile white-cyan light, low saturation, clean and silent. Wide fixed shot.` |
| L6 天台 | `The edge of a skyscraper rooftop at night, the whole vertical city glowing far below, strong wind, a low metal railing, dark indigo sky, distant cyan and red city lights. Lonely, quiet atmosphere. Extreme wide shot.` |

自检：**画面里不能有人物**；场景 L3 的广告上不能有文字。

### T1.5 道具设定图（6 件，各 2 张）

- 模型：flare　尺寸：`1792x1008`
- 输出：`assets/props/<道具>/<道具>_c01..02.png`
- 提示词模板：
```
Prop design sheet of {道具描述}, multiple orthographic views (front, side, back, top). {SHEET} Consistent proportions.
2D anime TV series style, flat cel shading with a single hard-edged shadow tone, thin clean dark lineart of even weight.
```

| 文件夹 | {道具描述} |
| --- | --- |
| `scooter` | `an old courier electric scooter, deep teal body, a phone mount on the handlebar, a dented mudguard` |
| `deliverybox` | `a square backpack-style courier delivery box, deep teal with a cyan Z-shaped logo, worn corners and scratches, shoulder straps` |
| `phone` | `a cheap smartphone with a crack across the top right corner of a blank black screen` |
| `cupcake` | `a squashed cupcake with white frosting and one small strawberry, inside a clear plastic box` |
| `lighter` | `a cheap transparent plastic lighter with visible fuel inside and a flint wheel` |
| `package` | `a small white cardboard parcel box with a blank white label` |

### 阶段 1 结束

1. 为每一组候选图做一张**对比图**：把同一组的图拼成一张，每张图左上角标上编号（比如 `c03`），存到 `assets/_review/stage1_<组名>.jpg`。这是唯一允许出现文字的地方：编号是你后期加上去的，不是生成的。
2. 更新 `assets/REVIEW.md`：每组候选图写一两句客观观察（比如"c04 的耳钉画到了左耳""c07 线条最干净"），**不要替导演做选择**。
3. 提交、推送。
4. **停下来**，告诉导演："阶段 1 完成，请在 `assets/selections.md` 里写下每组选中的编号。"

`assets/selections.md` 由导演填写，格式：
```
miles: c07
mia: c02
robot: c01
drone: c03
mascot: c02
L1: c02
L2: c01
...
scooter: c01
...
```

---

## 4. 阶段 2：设定包和角度图

**开始前**：读 `assets/selections.md`。把每组选中的图复制一份，命名为 `<名字>_master.png`，放在同一个角色、场景或道具文件夹下，例如 `assets/characters/miles/miles_master.png`。**母版一旦选定就不要重新生成。**

### T2.1 Miles 设定包（13 张，加上母版共 14 张）

- 模型：sunburst
- 参考图：`miles_master.png`。从第 06 张开始，再加上已经生成的 `miles_05_face_front.png`，一共两张参考图
- 输出：`assets/characters/miles/pack/`
- 每张的提示词 = `{KEEP_MILES}` + 下表的内容 + `{SHEET}` + `{STYLE}`

| 文件名 | 尺寸 | 内容 |
| --- | --- | --- |
| `miles_01_front_full.png` | — | **直接复制母版，不生成** |
| `miles_02_threequarter_full.png` | `1024x1536` | `Three-quarter view from his left side, full body, neutral standing pose.` |
| `miles_03_side_full.png` | `1024x1536` | `Exact side profile view of his left side, full body, neutral standing pose.` |
| `miles_04_back_full.png` | `1024x1536` | `Back view, full body, neutral standing pose, the delivery box on his back.` |
| `miles_05_face_front.png` | `1024x1024` | `Close-up of his face, front view, neutral expression, AR visor over his eyes.` |
| `miles_06_face_threequarter.png` | `1024x1024` | `Close-up of his face, three-quarter view from his left side, neutral expression.` |
| `miles_07_face_profile.png` | `1024x1024` | `Close-up of his face, exact side profile of his left side, neutral expression.` |
| `miles_08_expr_determined.png` | `1024x1024` | `Close-up of his face, front view, determined expression, jaw set, eyes narrowed.` |
| `miles_09_expr_exhausted.png` | `1024x1024` | `Close-up of his face, front view, exhausted and out of breath, sweat on his face.` |
| `miles_10_expr_tender.png` | `1024x1024` | `Close-up of his face, three-quarter view, a tender, soft smile, only the left corner of his mouth rises.` |
| `miles_11_expr_shocked.png` | `1024x1024` | `Close-up of his face, front view, shocked, eyes wide.` |
| `miles_12_expr_holdingtears.png` | `1024x1024` | `Close-up of his face, front view, holding back tears, eyes wet, lips pressed together.` |
| `miles_13_prosthetic.png` | `1792x1008` | `Close-up design sheet of his left lower leg prosthetic only: cheap scratched gunmetal casing with cracks, a row of five small lights. Two versions side by side: left version with the lights white and the third light broken and dark, right version with all working lights glowing red.` |
| `miles_14_visor_up.png` | `1024x1024` | `Close-up of his face, front view, the AR visor pushed up onto his hair, a crooked tired smile, only the left corner of his mouth rises.` |

### T2.2 设定包一致性检查

1. 按 `tools/check_consistency.py` 文件开头的说明，建一个虚拟环境并安装依赖。第一次运行时，它会从 HuggingFace 下载模型。
2. 运行：
```bash
python tools/check_consistency.py --ref assets/characters/miles/master_ref/ --shots assets/characters/miles/pack/ -o assets/_review/miles_pack_consistency.csv
```
   运行前先建好 `assets/characters/miles/master_ref/`，里面只放 `miles_master.png` 一张图。
3. 报告里被标为"返工候选"的图，加上你自检时锚点不对的图，**重新生成，每张最多 2 次**。重新生成后再跑一遍检查。
4. 把最终报告的前 5 行和你的锚点检查结果写进 REVIEW.md。
5. **检查工具只负责排序，最后要靠人眼判断。** 工具和你的判断冲突时，两种结论都写下来。

如果你的运行环境下载不了模型，就跳过第 1–3 步，在 REVIEW.md 里说明，导演会另找人跑。

### T2.3 Mia 锁屏照片

- 模型：sunburst　参考图：`mia_master.png`　尺寸：`1024x1536`
- 输出：`assets/characters/mia/mia_photo_lockscreen.png`，生成 3 张：`_v1..v3`
- 提示词：
```
The girl is Mia from the reference image. Keep her face, hair, sweater, paper crown and colors exactly the same.
A phone photo of Mia at home, smiling at the camera with both hands raised, showing off her paper crown. Warm golden indoor light, slightly overexposed edges like a phone beauty filter, cozy small room in the background, no text.
{MIA}
2D anime TV series style, flat cel shading with a single hard-edged shadow tone, thin clean dark lineart of even weight, warm golden palette.
```

### T2.4 场景的其他角度

- 模型：sunburst　参考图：该场景的 `<场景>_master.png`　尺寸：`1792x1008`
- 每张的提示词 = `Same location as the reference image, same design, lighting and colors.` + 下表的内容 + `{BG_STYLE}`
- 输出：放在对应的场景文件夹下

| 文件名 | 内容 |
| --- | --- |
| `L2_side.png` | `Side view along the jammed highway, cars receding into the distance.` |
| `L2_roof_low.png` | `Low angle from just above the roof of one jammed car, rain splashing, the convoy behind.` |
| `L3_fisheye_down.png` | `Extreme high-angle fisheye view from the edge of the highway looking straight down the 100-story drop beside the advertisement facade.` |
| `L3_facade_mid.png` | `Medium view of the advertisement facade, the mascot's face and thumbs up filling the frame, slogan area blank.` |
| `L5_scanner.png` | `Close-up of the package scanner on the wall, blank cyan screen.` |
| `L6_railing_bg.png` | `Close view of the rooftop railing with the city lights far below, strongly out of focus, for use as a close-up background.` |

### 阶段 2 结束

1. 对比图：`assets/_review/stage2_miles_pack.jpg`（14 张拼在一起）和 `assets/_review/stage2_locations.jpg`
2. 更新 REVIEW.md，写进一致性检查的结果
3. 提交、推送
4. **停下来**，告诉导演："阶段 2 完成，请确认 Miles 设定包。"

---

## 5. 阶段 3：风格样张（关卡 1）

每个段落一张，把色彩剧本变成画面。这 5 张定下来，就等于定下了整部片子的样子。

- 模型：sunburst　尺寸：`1792x1008`　每张生成 3 个版本：`_v1..v3`
- 参考图：Miles 设定包的 `miles_01`、`miles_05`、`miles_06`，加上对应的场景母版
- 输出：`assets/style_frames/`
- 每张的提示词 = `{KEEP_MILES}` + 下表的画面和光线 + `{STYLE}`

| 文件名 | 画面和光线 |
| --- | --- |
| `SF1_rain_night` | `Medium shot: Miles rides an electric scooter through the jammed elevated highway in the rain, looking down at a phone on the handlebar. Night, rain, deep indigo ambient light, cyan neon rim light from the left, cyan HUD glow on his face.` |
| `SF2_jam` | `Wide shot: Miles stops at the edge of the jammed highway, the black convoy and police drones ahead, he looks down at his prosthetic leg. Night, rain, deep indigo ambient light, red and blue police lights mixing with cyan neon.` |
| `SF3_overclock` | `Low-angle full shot: Miles crouches on a car roof after landing, rain drops frozen in the air around him, a trail of floating cyan HUD numbers behind him. Night, rain, deep indigo ambient light, cyan neon rim light from the left.` |
| `SF4_lobby` | `Wide fixed shot: Miles kneels exhausted in the spotless white delivery lobby while a small white service robot takes a parcel from him. Pale sterile white-cyan light, low saturation.` |
| `SF5_rooftop` | `Medium close-up: Miles sits at the rooftop edge, a single small lighter flame lit in his trembling hand, the city glowing far below. Dark indigo night, the warm flame lighting his face from below is the only warm color in the frame.` |

`SF3_overclock` 生成时用普通夜景光，因为成片里这一段是**整屏红色单色**，在后期统一加。为了让导演提前看到效果，再额外为每个 SF3 版本做一张预览：用 Python 把图转成亮度图，再映射到这组颜色上（从暗到亮）：

`#140E1E` → `#B02324` → `#E83F34` → `#EDF5ED`

青色的 HUD 数字保持原色不映射（可以把高饱和的青色像素蒙版出来，跳过映射）。预览存成 `SF3_overclock_v1_redpreview.png`，依此类推。

### 阶段 3 结束

1. 对比图：`assets/_review/stage3_style_frames.jpg`
2. 更新 REVIEW.md
3. 提交、推送
4. **停下来**，告诉导演："阶段 3 完成，请确认风格样张。确认后，这些素材就可以上传到 Higgsfield 了。"

---

## 6. 这份文档之后的事（不属于 Codex 的任务）

导演确认风格样张之后：
1. 把 Miles 设定包上传到 Higgsfield，创建 Element `Miles`
2. 用 Wan 3.0 做试镜（关卡 2）
3. 开始生成镜头的关键帧和视频，见 [Wan 3.0 七天计划](wan3-7day-plan.md)

镜头关键帧会另外写一份执行文档。

---

## 7. 记录文件的格式

### assets/manifest.csv

每生成一张图加一行：

```
task,file,model,size,quality,refs,attempt,self_check,notes
T1.1,assets/characters/miles/candidates/miles_c01.png,gpt-image-2.5-flare,1024x1536,high,,1,pass,
T2.1,assets/characters/miles/pack/miles_03_side_full.png,gpt-image-2.5-sunburst,1024x1536,high,miles_master.png,2,pass,第 1 次义肢画到了右腿
```

- `self_check`：`pass`、`fail` 或 `unsure`
- `notes`：不合格的原因，或者需要导演注意的地方

### assets/REVIEW.md

```
# 素材审查记录

## 阶段 1（日期）
### Miles 候选
- c01：……
- c04：耳钉画到了左耳，已重新生成
### 需要导演决定的问题
- ……
```

只写客观观察和问题，不替导演做选择。
