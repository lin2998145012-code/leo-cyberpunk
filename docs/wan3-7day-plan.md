# Wan 3.0 免费 7 天作战计划

> 账号：Higgsfield Plus。Wan 3.0 在网页上 7 天不限量。
> 相关文档：[导演方案](film-overclock.md)　[前期制作](preproduction.md)　[Higgsfield 制作流程](higgsfield-workflow.md)　[Codex 执行文档](codex-execution.md)
>
> **更新**：静态图（设定包、场景、道具、关键帧）改由 Codex 用 GPT Image 2.5 生成。下文写着 Nano Banana Pro 的步骤，都换成 Codex 来做。

---

## 1. 先弄清楚 Wan 3.0 能做什么

Higgsfield 上的 Wan 3.0 于 2026 年 8 月上线，分 **Wan 3.0** 和 **Wan 3.0 Prime** 两个版本：Prime 生成更快，但消耗更高。按 Higgsfield 的更新日志和 API 文档：

| 项目 | 规格 |
| --- | --- |
| 时长 | 2–30 秒（最短 2 秒，正好适合短镜头） |
| 分辨率 | 480p / 720p / 1080p |
| **图生视频模式** | 首帧（必填）+ **尾帧（可选）** |
| **参考生视频模式** | 最多 **10 张参考图**、**5 段参考视频**（合计不超过 30 秒）、5 段参考音频；还能附一份文档或一个网页链接（会强制开启深度思考） |
| 其他 | 原生音频、可固定种子、可开深度思考；官方说多个角色的脸、服装和细节能在画面里保持稳定 |

这对我们意味着三件事：

1. **首尾帧模式**可以直接套用一致性方案里的"锁 5"：两张关键帧夹住一段视频。
2. **10 张参考图**装得下设定包里最重要的 10 张。
3. **参考视频**也许能代替 Kling 的 Motion Control：你拍一段动作，让 Miles 照着做，而且是免费的。这一点**官方没有明说能转移动作**，要先测。

### 免费的规则（来自 Higgsfield 帮助中心）

- **只在 higgsfield.ai 网页上免费。** 通过 MCP、Canvas、CLI 生成一律扣积分。
- **生成面板上要打开 Unlimited 开关**；关掉就会扣积分。
- 不限量走普通队列，高峰时段可能比较慢。
- **只限本人手动使用**，禁止用脚本或自动化工具批量生成。所以这 7 天都得你在网页上亲手点，我负责准备提示词、检查结果。

### 今天先确认三件事

1. 打开 **Manage Account → Subscription**，看 Active unlimited models 表：**免费的是 Wan 3.0 还是 Wan 3.0 Prime，还是两个都免费？到期时间是哪天几点？**
2. 同一个表里，**Nano Banana Pro 在不在？** 关键帧要用它。不在的话，关键帧会花积分。
3. 选 Wan 3.0 时，确认 Generate 按钮旁边有 Unlimited 开关，而且打开后显示不扣积分。

---

## 2. 核心策略

**这 7 天要把所有带人物的视频镜头都生成完。**

原因是一致性方案里有一条规则：**同一部片子尽量只用一个视频模型**，中途换模型会让角色偏差叠加。如果这周用 Wan 3.0 做了一半，剩下的过期后再换 Kling 来做，两边的 Miles 很可能不像同一个人。

具体做法：
- 每个人物镜头至少留 **3 条可用的版本**，过期后不用再补
- 先用 **720p** 反复试，定下来再出 **1080p**
- 每天收工前把当天满意的结果**全部下载**，按镜头号命名，例如 `S06_wan_take3.mp4`
- 后期（降帧、红色单色、文字、剪辑）不受这 7 天的限制，放到之后慢慢做

**两个先后顺序上的问题**：
- 视频要用关键帧和设定包，所以**前 2 天要把设定包做完**，前期素材的完整清单见[前期制作](preproduction.md)。
- 不涉及人物的镜头（城市空镜）从第 1 天就可以开始用 Wan 免费跑，不用等设定包。

---

## 3. 七天日程

| 天 | 你在 Higgsfield 上做 | 我做 |
| --- | --- | --- |
| **第 1 天** | 前期：Miles 定妆（8–16 张候选里选 1 张）、Mia 定妆、配角设定图。Wan：城市空镜（镜头 1），测试 Wan 能不能保持 2D 风格 | 检查候选图的锚点有没有画错；分析镜头 1 的风格 |
| **第 2 天** | 前期：Miles 设定包 14 张、6 个场景设定。Wan：其他空镜 | 设定包一致性检查，挑出偏了的让你重做 |
| **第 3 天** | 前期：道具设定、5 张风格样张（**关卡 1**）。Wan：试镜（**关卡 2**）、4 个测试镜头；拍你自己表演的动作视频；试 Mia 的日语语音 | 判断能不能开拍；根据测试结果写出剩下所有镜头的提示词 |
| **第 4 天** | 第一、二段（雨夜、堵死）：关键帧 → 视频，每个镜头 3 条以上 | 逐批检查一致性，标出返工镜头 |
| **第 5 天** | 第三段（超频）：动作镜头 | 同上 |
| **第 6 天** | 第四、五段（送达、生日） | 同上 |
| **第 7 天** | 返工；每个镜头补 2 条备用；**全部下载** | 列最终清单，确认没有缺镜头 |

如果第 3 天发现 Wan 的一致性明显不如 Kling 3.0，就改成：**Wan 只做空镜和背景，人物镜头用 Kling 3.0（花积分）**。那样这 7 天的价值在于免费做完所有不涉及人物的镜头，以及大量试错。

**怎么把结果发给我**：直接在对话里上传图片或视频就行。我会把它们放进一致性检查工具，再告诉你哪些要返工。

---

## 4. 提示词通用部分

下面三块在每次生成时**原样复制**，不要改动。角色描述块和画风描述块与 [Higgsfield 制作流程](higgsfield-workflow.md) 里的一致。

**角色描述块**
```
Miles: a 19-year-old slim young man, narrow face, sharp chin, narrow upturned eyes with
pale teal-grey irises, a vertical scar cutting through his left eyebrow, short black hair
with the right side shaved and a single cyan streak in his left fringe, three small silver
studs in his right ear, a square metal data port on the left side of his neck with a tiny
red light, oversized deep-teal courier jacket with bright cyan reflective stripes and a high
collar, black cargo pants with the left leg cut off at the knee, left lower leg is a cheap
scratched gunmetal prosthetic with a cracked casing and a row of five small lights,
a thin transparent cyan AR visor across his eyes.
```

**画风描述块**
```
2D anime TV series style, flat cel shading with a single hard-edged shadow tone,
thin clean dark lineart of even weight, bold saturated colors, shadows tinted deep indigo
and violet (never grey), hard-edged cyan rim light, high contrast, angular expressive
character design.
```

**视频结尾块**（Wan 默认偏写实，要明确压住）
```
2D anime, flat cel shading, hand-drawn limited animation, the character stays exactly on
model, no morphing, no realistic rendering, no 3D look.
```

**Wan 参数**：草稿 720p、16:9；**关掉 Sound**（声音我们后期自己做）；种子记下来，好的结果可以复现。

---

## 5. 测试镜头提示词

### 5.1 镜头 1：城市俯瞰（第 1 天，不需要设定包）

Wan 3.0 文生视频，6 秒：

```
Straight-down aerial view into a vertical city shaft at night: stacked elevated highways
spiral down into darkness, thousands of tiny cyan lights flow along the roads like current
on a circuit board, rain falling toward the camera, deep indigo and violet buildings with
small neon signs. The camera slowly descends.
2D anime background art, flat colors, clean shapes, high contrast, no realistic rendering,
no 3D look.
```

**看什么**：画面是 2D 平涂，还是写实或 3D？如果偏写实，把 `2D anime background art, flat colors` 挪到提示词最前面再试。这个测试的结论会决定所有提示词的写法。

### 5.2 镜头 6：AR 目镜后的特写（第 3 天）

**关键帧**（Nano Banana Pro，Multi-reference；图 1 正面脸、图 2 3/4 脸、图 3 侧脸、图 4 正面全身）：

```
Images 1-4 are reference sheets of the same character, Miles. Keep his face, hair, scar,
ear studs, neck port, jacket, prosthetic leg and colors exactly as in the references.
Close-up, three-quarter view of the left side of his face, so the cyan streak and the
eyebrow scar are visible. He sits on an electric scooter in the rain, looking down at a phone
on the handlebar, listening to a voice message. His eyes are soft, a faint smile at one
corner of his mouth, the thin cyan AR visor in front of his eyes.
Night, rain, deep indigo ambient light, cyan neon rim light from the left, cyan HUD glow on
his face.
[画风描述块]
16:9.
```

**视频 A：首帧模式**（Wan 3.0 图生视频，首帧 = 上面的关键帧，3 秒）：

```
He listens to a voice message on his phone. His eyes slowly soften and one corner of his
mouth lifts slightly. Raindrops run down the visor, the cyan HUD light flickers softly on
his face. Static camera, very slight push in.
[视频结尾块]
```

**视频 B：参考图模式**（Wan 3.0 参考生视频，参考图 = 设定包 9 张 + 关键帧共 10 张，3 秒）：提示词开头加一句 `The young man is the character from the reference images.`，后面和视频 A 相同。

**看什么**：脸是不是一直像设定包？疤在左眉、挑染在左边、耳钉在右耳，有没有左右反？哪种模式更好？

### 5.3 镜头 16：低角度落地（第 3 天，测试动作）

**先拍你自己的表演**（这就是 Wan 的参考视频）：
- 手机横拍，镜头放在腰的高度，略微仰拍
- 全身入画，背景尽量简单
- 从台阶或椅子上跳下，**蹲着落地**，一只手撑地，落地后停住 1 秒
- 3 秒左右，**一镜到底不剪辑**

**关键帧**（Nano Banana Pro，参考图 1 正面全身、2 3/4 全身、3 正侧面全身、4 义肢特写）：

```
Images 1-4 are reference sheets of the same character, Miles. Keep his face, hair, scar,
ear studs, neck port, jacket, prosthetic leg and colors exactly as in the references.
Low-angle full shot. He has just landed in a crouch on the roof of a car in a traffic jam,
one hand on the roof, his prosthetic left leg bent under him, the roof dented around his
feet, rain splashing outward. He looks up past the camera, determined.
Night, rain, deep indigo ambient light, cyan neon rim light from the left.
[画风描述块]
16:9.
```

注意：这个镜头最后是**全红画面**，但生成时用普通夜景光，红色在后期加。

**视频 A：首帧模式**（2 秒）：
```
He lands in a crouch on the car roof, the metal dents under his weight, rain splashes
outward, then he holds still for a moment. Low angle, static camera.
[视频结尾块]
```

**视频 B：参考视频模式**（参考图 = 设定包里的全身图和义肢特写，参考视频 1 = 你的表演）：
```
The young man from the reference images performs the movement from video 1: he lands in a
crouch on the roof of a car in a traffic jam at night, the roof dents, rain splashes outward,
then he holds still for a moment. Low angle, static camera.
[视频结尾块]
```

**看什么**：视频 B 是不是照着你的动作做的？如果是，第三段所有动作镜头都用这个方法，全部免费；如果不是，动作镜头改用 Kling 3.0 Motion Control（花积分）。

### 5.4 镜头 21：鱼眼俯拍跳楼（第 3 天，最难的远景）

远景里脸太小，容易跑偏，所以分三步：

**① 背景**（Nano Banana Pro，文生图）：
```
Extreme high-angle fisheye view looking straight down a 100-story canyon between cyberpunk
skyscrapers at night. A jammed elevated highway crosses the bottom of the frame, tiny car
lights far below, rain, small neon signs, deep indigo and violet, cyan accents.
2D anime background art, flat colors, clean shapes, high contrast. 16:9.
```

**② 人物**（Nano Banana Pro，Multi-reference；参考图用设定包的全身图）：中景的 Miles 在半空起跳，从上方俯拍，平光、浅灰背景。

**③ 合成**（Nano Banana 编辑；图 1 = 人物，图 2 = 背景）：
```
Place the character from image 1 into image 2, small in the upper center of the frame,
mid-leap from the edge of the highway toward a building facade, seen from above.
Keep his design exactly the same as image 1 and match the lighting and fisheye
perspective of image 2.
```

**视频**（Wan 3.0 首帧模式，2 秒）：
```
He leaps across the gap between the highway and the building, rain streaking past,
the camera tilts down slightly to follow him, strong fisheye perspective.
[视频结尾块]
```

### 5.5 镜头 36：摘下目镜（第 3 天，最重要的角色镜头）

做两张关键帧，用**首尾帧模式**把动作夹住。

**首帧**（Nano Banana Pro，图 1 正面脸、图 2 3/4 脸、图 3 推起目镜的正脸、图 4 筋疲力尽的表情）：
```
Images 1-4 are reference sheets of the same character, Miles. Keep his face, hair, scar,
ear studs, neck port, jacket and colors exactly as in the references.
Close-up, front view. He kneels in a spotless white lobby, exhausted and out of breath,
sweat on his face, the thin cyan AR visor still over his eyes.
Pale sterile white-cyan light, low saturation, clean bright interior.
[画风描述块]
16:9.
```

**尾帧**：同一个提示词，把最后一句动作改成 `the AR visor pushed up onto his hair, a crooked tired smile`。用首帧当参考图 5，保证构图一致。

**视频**（Wan 3.0 首尾帧模式，2–3 秒）：
```
He pushes the AR visor up onto his hair, breathes out heavily, and a crooked tired smile
spreads across his face. Static camera.
[视频结尾块]
```

**看什么**：这个镜头是全片第一次没有 HUD 光的正脸，**一定要和设定包一模一样**。如果首尾帧中间变脸，就把时长缩到 2 秒再试。

---

## 6. 第 3 天结束时的判断标准

把 4 个测试镜头（6、16、21、36）的所有版本都发给我。我用 `tools/check_consistency.py` 检查之后，我们一起按下面的标准决定：

| 结果 | 决定 |
| --- | --- |
| 4 个镜头都和设定包一致，锚点没有左右反 | **Wan 3.0 当主力**，这 7 天做完所有人物镜头 |
| 特写可以，动作或远景不行 | 特写和情绪镜头用 Wan，动作镜头改用 Kling 3.0 Motion Control |
| 都不行 | Wan 只做空镜和背景，人物镜头改用 Kling 3.0 |

不管哪种结果，城市空镜和背景镜头（1、7、39、41）都用 Wan 免费做完。
