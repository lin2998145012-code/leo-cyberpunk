# Higgsfield 制作流程与角色一致性方案

> 适用于《超频 OVERCLOCK》。功能信息来自 Higgsfield 官方帮助中心（2026 年 8 月版），平台更新很快，动手前请在网站上核对一遍。
> 相关文档：[导演方案](film-overclock.md)　[原片参考分析](reference-analysis.md)　[实现方案](production-plan.md)

---

## 0. 核心思路

角色一致性不是靠某一个功能解决的，而是**每道工序都要锁一次**。只要中间有一步放开，后面就会跑偏：

```
① 角色设计 → ② 角色设定包 → ③ 身份注册 → ④ 关键帧 → ⑤ 视频 → ⑥ 质检返工
  好认的长相     一套标准参考图    Element / Soul ID   每帧都带参考    首尾帧 + Element   工具排序 + 人眼确认
```

全程用 Higgsfield 生成。不过剪辑、降帧、整屏单色调色和界面文字这几步 Higgsfield 做不了，需要一个剪辑软件。免费的 DaVinci Resolve 就够用。

---

## 1. 每一步用 Higgsfield 的哪个功能

> **更新**：静态图（角色设定包、场景、道具、风格样张）改由 Codex 用 GPT Image 2.5 生成，见 [Codex 执行文档](codex-execution.md)。下表里 Nano Banana Pro 负责的步骤，都可以换成 Codex。**全片的静态图只用一个图像模型**，道理和视频一样：中途换模型会让偏差叠加。

| 工序 | 功能 | 为什么用它 |
| --- | --- | --- |
| 角色设计、设定包、关键帧 | **Nano Banana Pro**（图像） | 最多 14 张参考图，能同时保持最多 5 个角色一致，最高 4K，文字也写得准 |
| 关键帧小修 | **Nano Banana**（编辑） | 上传图片，用一句话改局部，例如"把耳钉改成银色" |
| 分镜预览 | **Popcorn**（Manual 模式） | 一次最多 8 帧连续画面，角色、光线保持一致，最多 4 张参考图。适合每段先出一版分镜，剪成动态分镜看节奏 |
| 身份注册 | **Elements** | 保存成可复用的角色，在 Kling、Seedance、Cinema Studio 里用 @ 调用，跨镜头保持身份 |
| 身份注册（待测试） | **Soul ID** | 用 20–80 张图训练身份。官方说虚构角色可以先生成肖像再训练，但 Soul 模型偏摄影风格，二次元能不能用要先测 |
| 人物镜头视频 | **Kling 3.0** | 首帧 + 尾帧 + Elements；支持多镜头；有 Impact、Bullet Time 等变速，片长 3–15 秒 |
| 动作镜头视频 | **Kling 3.0 Motion Control** | **你自己拍一段动作视频，让 Miles 照着做**。官方说会保留角色的脸和画风，适合跳跃、落地、格斗 |
| 人物镜头、空镜（本周免费） | **Wan 3.0 / Wan 3.0 Prime** | 首帧 + 尾帧，或者最多 10 张参考图加 5 段参考视频；2–30 秒。你的 Plus 账号本周在网页上不限量，用法见 [Wan 3.0 七天计划](wan3-7day-plan.md) |
| 大场景、运镜 | **Seedance 2.0 / 2.5** 或 **Cinema Studio 4.0** | 运镜控制强。Seedance 有 @character、@style 参考和 Elements；2.5 需要 Pro 或 Plus 以上套餐 |
| 视频局部修补 | **Seedance 2.5 Edit**、**Kling 3.0 Omni Edit**、**Cinema Studio 4.0 Edit Video** | 在画面上框出区域重画，例如只修一张跑偏的脸，不用整段重新生成 |
| 后期 | **DaVinci Resolve**（Higgsfield 之外） | 降帧、整屏单色、冲击帧、界面文字、剪辑、混音 |

## 2. 两条一定要先知道的平台规则

**1. 版权过滤会拦截作品名和工作室名。** Higgsfield 和 Seedance 都会检查提示词和参考图里的受保护 IP：作品名、角色名、品牌、在世艺术家的名字。所以：

- 提示词里**不写** "Studio Trigger""Edgerunners""Cyberpunk 2077" 这类名字，只描述画面特征。项目里其他文档的提示词已经按这个规则改过了。
- **不要**把原片截图上传当风格参考，这既会触发过滤，也有版权问题。风格参考用我们自己生成、已经定稿的画面。

**2. 通过 MCP、Canvas、CLI 生成一律扣积分。** 你套餐里的"不限量"模型只在 higgsfield.ai 网页上不扣积分。

---

## 3. 一致性六道锁

### 锁 1：角色设计——让 AI 有东西可抓

AI 记不住"一张脸"，但能记住**几个明确的特征**。Higgsfield 的文档也建议用发色、服装细节、明显特征来做视觉锚点。所以设计阶段就给 Miles 放好 5 个锚点，每个都要做到在远景里也能认出来：

| 锚点 | 设计 | 远景能不能认出来 |
| --- | --- | --- |
| 发型 | 黑色短发，右侧剃短，左边刘海一缕青色挑染 | 能，青色挑染很显眼 |
| 疤 | 一道竖疤切断左眉 | 近景 |
| 耳钉 | 右耳三颗银色小耳钉 | 近景 |
| 颈部接口 | 左颈一个方形金属数据接口，带一颗小红灯 | 中景 |
| 义肢 | 左小腿是廉价的枪灰色义肢，外壳有裂痕，一排 5 颗指示灯，其中一颗坏了；左裤腿在膝盖处剪掉 | 能，**不对称的剪影**最好认 |

**颜色固定**（全部取自原片实测色板）：

| 部位 | 颜色 |
| --- | --- |
| 外套主色 | 深青 `#194140` |
| 外套反光条、刘海挑染 | 青 `#29DBD5` |
| 肤色 | `#D5906D` |
| 虹膜 | 灰青 `#6A9FAA` |
| 义肢 | 枪灰 `#506B61`，超频时指示灯变红 `#E83F34` |
| 裤子、头发 | 紫黑 `#140E1E` |

注意：**全身没有暖金色**。按导演规则，金色只属于妹妹 Mia。

**AR 目镜**：一条透明的青色细目镜横在眼前，HUD 的光会投在他脸上。**脸是完全露出来的**。送达之后他把目镜推到头上，那是全片第一次脸上没有系统的光。

### 锁 2：角色设定包——一套标准参考图

后面每一步都拿这套图当参考，所以它决定了一致性的上限。

**规格**（Higgsfield 文档里提到，重阴影、遮挡、裁切都会降低一致性）：
- 平光、均匀照明、浅灰纯色背景
- 不带文字、标注和水印
- 同一套服装，同一个发型
- 脸部清晰，不能被遮挡

**清单（14 张，正好是 Nano Banana Pro 的参考图上限）**：

| # | 内容 |
| --- | --- |
| 1 | 正面全身（这张是母版，其他图都从它生成） |
| 2 | 3/4 侧面全身 |
| 3 | 正侧面全身 |
| 4 | 背面全身 |
| 5 | 正面脸部特写 |
| 6 | 3/4 脸部特写 |
| 7 | 正侧脸特写（侧脸最容易跑偏，一定要有） |
| 8–12 | 表情：坚定、筋疲力尽、温柔地笑（听妹妹语音时）、震惊、强忍眼泪 |
| 13 | 义肢特写（普通状态和超频状态各半边） |
| 14 | AR 目镜推到头上的正面脸 |

**用 Nano Banana Pro 制作**：

第一步，出母版。用文生图，一次多出几张，挑一张定为 `miles_master.png`：

```
Character design, full body, front view, neutral standing pose, plain light grey background,
flat even lighting, no text.
[角色描述块]
[画风描述块]
```

第二步，从母版生成其他图。选 Multi-reference 模式，参考图 1 放母版，每次只生成一张，不要一次生成多格设定图，那样每格分辨率太低：

```
Image 1 is the character Miles. Keep his face, hair, scar, ear studs, neck port, jacket,
prosthetic leg and colors exactly the same as image 1.
Three-quarter view, full body, neutral standing pose, plain light grey background,
flat even lighting, no text.
[画风描述块]
```

把 "Three-quarter view, full body" 换成清单里的其他内容，依次生成。

第三步，检查设定包本身是否一致：用 `tools/check_consistency.py` 以母版为参考检查其余 13 张，再用人眼对照 5 个锚点，有偏的重新生成。**设定包里只要有一张偏了，后面所有镜头都会被它带偏。**

**角色描述块**（每次生成都原样复制，一个字都不改）：

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

**画风描述块**（不写任何作品名和工作室名，只描述特征，依据是原片参考分析）：

```
2D anime TV series style, flat cel shading with a single hard-edged shadow tone,
thin clean dark lineart of even weight, bold saturated colors, shadows tinted deep indigo
and violet (never grey), hard-edged cyan rim light, high contrast, angular expressive
character design.
```

### 锁 3：身份注册——Elements 为主，Soul ID 做对照测试

**主方案：Elements。** 从设定包里挑最清楚的几张（正面全身、3/4 脸、侧脸、正面脸），在 Assets 里对图片选 **Create Element**，命名为 `Miles`。之后在 Kling 3.0、Seedance、Cinema Studio 里输入 @ 选择 Miles。

**对照测试：Soul ID。** 官方文档说 Soul ID 是为真人照片设计的，虚构角色要"先生成肖像再训练"，但没有说二次元风格能不能保持。所以第一周做一次测试：

1. 用设定包和 Nano Banana Pro 生成 20–30 张 Miles 的肖像和全身图（角度、表情多样，平光）
2. 在 Soul 里选 **Train new character** 训练
3. 在 Soul Cinema 里用 Soul ID 生成 8–12 张不同场景
4. 判断：**画风是不是还是 2D 平涂？** 如果被拉向写实摄影风格，就放弃 Soul ID，只用 Elements

训练好的 Soul ID 会自动出现在 Elements 里，所以两条路可以并存，不冲突。

### 锁 4：关键帧——每一帧都带着设定包

关键帧是视频的起点。关键帧一致了，视频才有可能一致。

**提示词模板**（Nano Banana Pro，Multi-reference）：

```
Images 1-4 are reference sheets of the same character, Miles. Keep his face, hair, scar,
ear studs, neck port, jacket, prosthetic leg and colors exactly as in the references.
[本镜头内容：景别、机位、动作、表情]
[本段光线块]
[画风描述块]
16:9.
```

- **参考图顺序固定**：图 1 正面脸，图 2 3/4 脸，图 3 侧脸，图 4 正面全身。全片都按这个顺序，不要换。
- **按镜头挑参考图**：侧脸镜头把侧脸设定放进去；全身镜头把全身设定放进去；义肢特写把第 13 张放进去。
- **远景要分两步做**。Higgsfield 的文档提到，脸占画面不到约 20% 时最容易跑偏。所以远景不要一步生成：先在中景里把人物生成准，再用 Nano Banana 编辑功能"把图 1 的人物放进图 2 的场景"，合成到远景里。
- **光线和身份分开处理**。整屏红色单色在后期统一加：超频段落生成时用普通的夜景光，进 Resolve 再染红。浓重的光效会让 AI 改动人物的五官，后期染色就不会。

**光线块**（对应导演方案的色彩剧本）：

| 段落 | 光线块 |
| --- | --- |
| 一、二 雨夜 / 堵死 | `night, rain, deep indigo ambient light, cyan neon rim light from the left, cyan HUD glow on his face` |
| 三 超频 | 同上（**红色在后期加**） |
| 四 公司大厅 | `pale sterile white-cyan light, low saturation, clean bright interior` |
| 五 天台 | `dark indigo night, wind, a single small warm flame lighting his face from below`（金色只出现在火苗上） |

每张关键帧生成后，都用 `tools/check_consistency.py` 和设定包比对一次，再进入视频生成。

### 锁 5：视频——首尾帧加 Element

| 镜头类型 | 做法 |
| --- | --- |
| 人物特写、情绪镜头 | Kling 3.0：首帧 + 尾帧（两张都是锁 4 做出来的关键帧）+ @Miles。动作幅度小，时长选最短，生成后再剪 |
| 动作镜头 | **Kling 3.0 Motion Control**：你用手机拍自己做这个动作，再加上 Miles 的关键帧。要求：关键帧里手和手臂露出来，人物周围留出空间；你拍的视频不能有剪辑点，构图尽量和关键帧一致。导演亲自表演，表演和一致性一起解决 |
| 连续动作 | 上一个镜头的最后一帧，当作下一个镜头的首帧 |
| 大场景、空镜 | Seedance 或 Cinema Studio 4.0，不涉及角色一致性 |

视频提示词模板：

```
@Miles [动作，一次只写一个]. [运镜，用具体的词：push in / dolly in / handheld follow / crane up].
2D anime, flat cel shading, limited animation, the character stays exactly on model.
```

两条规则：
- **同一段落只用一个视频模型。** Higgsfield 自己的文档也提到，中途换模型会让偏差叠加。建议用镜头 6 同时测 Kling 3.0 和 Seedance，选出来以后，一、二、四、五段都用它。
- **先用 720p 草稿反复试，满意了再出最终分辨率。** 积分消耗主要由分辨率和时长决定，Generate 按钮上会显示具体消耗。

### 锁 6：质检和返工

**工具检查**：把同一段落的镜头放进一个文件夹，运行：

```bash
python tools/check_consistency.py --ref refs/miles/ --shots shots/seq1/ -o seq1_report.csv
```

报告按"最不像参考图"排序，并标出明显偏离同批镜头的帧，作为"返工候选"。

**人眼检查**：逐个镜头对照 5 个锚点——挑染在左边、疤在左眉、耳钉在右耳、接口在左颈、义肢在左腿。**左右反了是最常见的错误**，工具查不出来，只能靠人眼。

**返工路线**：

| 问题 | 怎么修 |
| --- | --- |
| 关键帧不像 | Nano Banana 编辑局部，或者换参考图组合重新生成 |
| 视频里某几帧脸跑偏 | Seedance 2.5 Edit / Kling 3.0 Omni Edit / Cinema Studio Edit Video 框选脸部重画 |
| 整段越来越不像 | 补一张尾帧锁住结尾，缩短时长，重新生成 |
| 锚点左右反了 | 关键帧阶段改好；视频已经生成的话，局部重画 |

---

## 4. 一致性检查工具在原片上的验证结果

在用到我们自己的镜头之前，我先拿原片预告检验了这个工具：从正式预告里截了 8 个角色共 24 个镜头，看 CCIP 模型能不能分清"同一个角色"和"不同角色"。CCIP 是专门为二次元角色训练的身份比对模型。

| 测试 | 结果 |
| --- | --- |
| 同一角色的 33 对，判为同一人 | 82% |
| 不同角色的 220 对，判为不同人 | 88% |
| 用 David 的 3 张图做参考，检查 15 帧混合画面 | **其他角色的 9 帧全部排在 David 的 6 帧前面**，排序完全正确；但最接近的一对分数只差 0.162 对 0.167 |

出错的情况都集中在三类画面上：

- 画面上叠了大字（角色名卡）
- 整屏偏色（全品红、全粉）
- 截图里没有脸（只截到手和头发）

所以使用规则是：

1. **用来排序，不用来判对错。** 工具负责找出最可疑的镜头，最后一定要人眼确认。
2. **在后期调色之前检查。** 红色单色段落检查染红之前的原始素材。
3. **检查的画面不要叠字幕和界面。**

---

## 5. 第一周测试计划

Higgsfield 文档里推荐的一致性测试方法是：同一个角色生成 8–12 张不同角度、光线、服装的图，重点看侧脸、仰角、俯角和远景，这几种最先崩。我们按这个思路选测试镜头：

| 测试 | 镜头 | 考验什么 |
| --- | --- | --- |
| A | 设定包 14 张 | 设定包本身是否一致（工具 + 人眼） |
| B | Soul ID 对照 | Soul ID 能不能保持 2D 画风 |
| C | 镜头 6：AR 目镜后的特写，HUD 青光打在脸上 | 带光效的近景；同时比较 Kling 3.0 和 Seedance |
| D | 镜头 16：低角度全身落地 | 仰角 + 全身 + Motion Control（你自己演） |
| E | 镜头 21：鱼眼俯拍跳楼 | 最难的远景 + 俯角，测试"先中景、再合成"的做法 |
| F | 镜头 36：摘下目镜的正脸 | 全片最重要的角色镜头 |

**通过标准**：
- 工具报告里没有"返工候选"
- 5 个锚点全部正确，没有左右反
- 把 C–F 四个镜头和设定包摆在一起，给一个没看过的人看，他能认出是同一个人

四个镜头都通过，再开始量产。

---

## 6. 账号情况

- **套餐：Plus。** 能用 Seedance 2.5（需要 Pro 或 Plus 以上）。
- **Wan 3.0 本周在网页上不限量。** 这 7 天怎么安排，见 [Wan 3.0 七天计划](wan3-7day-plan.md)。
- **MCP 接入（可选）**：Higgsfield 有官方 MCP 接口（`https://mcp.higgsfield.ai/mcp`），接上后我可以直接生成。但通过 MCP 生成一律扣积分，不享受不限量，所以这周免费的 Wan 3.0 要在网页上手动生成。
