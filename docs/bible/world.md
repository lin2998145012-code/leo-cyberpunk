# 世界观、场景和道具

> 《超频 OVERCLOCK》的世界设定。画面里出现的所有东西都要能在这里找到来由。
> 相关：[人物档案](characters.md)　[导演方案](../film-overclock.md)

> **提示词以 [Codex 执行文档](../codex-execution.md) 为准。** 这里的提示词是早期版本，画风描述比较简略，也没有用风格参考图。


---

## 1. 世界观

### Stack City（スタック・シティ）

- **一座往下长的垂直城市。** 地面早就不够用了，城市一层一层往下挖，层数越低越穷、越暗。顶层是公司大楼，见得到天空；底层终年不见天日，只有霓虹灯和广告的光。
- 城市中央是一个巨大的**天井**，几十层高架绕着天井盘旋向下（镜头 1、39）。从顶上往下看，路上流动的车灯像电路板上的电流。
- 名字来自 stack（堆叠），也是计算机里的"栈"：人在这座城市里，就像被压进栈里的数据。
- 全年都在下雨。顶层的雨是干净的，落到底层时已经混着油污和霓虹的颜色。

### ZENITH（ゼニス）

- 控制 Stack City 物流的巨型公司。旗下的 **ZENITH EXPRESS（ゼニス急便）** 是城里最大的配送平台。
- 品牌色是青色和白色。标志是一个带向上箭头的"Z"，意思是"向上"。
- 总部 **ZENITH Tower** 是全城最高的楼，片中的送达地点就是塔顶。
- 公司从不露面，只通过 App、HUD、广告和机器人和人打交道。

### OPTIMA：配送算法

- ZENITH 的派单和定价算法。每一单的配送时限由它计算，**依据是同区骑手的最快纪录**。
- 骑手评分低于 ★4.0 会被降级接单；超时会扣除本单全部报酬。
- 这就是片尾反转的原理：Miles 创下了最快纪录，OPTIMA 就把全区的时限缩短了 20%。没有人下这个命令，系统只是在正常运转。

### 超频（オーバークロック）

- ZENITH 骑手义肢里自带的固件，正式名称是"性能增强模式"。
- 启动后，神经信号被强行放大：使用者的主观时间变慢，身体反应速度大幅提高。
- **代价**：每次使用都会累积"神经负载"，超过 100% 会造成永久性神经损伤。神经负载在 HUD 上实时显示。
- 片中 Miles 从 61% 开始超频，送达时到了 89%；结尾他的手一直在抖，就是损伤。

**画面规则**（和原作刻意区分）：
- 超频时整屏染成红色单色（后期加）
- 使用者身后拖出一串漂浮的青色 HUD 数字（速度、心率、神经负载），**不画彩色残影**
- 义肢的 5 颗指示灯由白变红

### 技术和生活细节

| 项目 | 设定 |
| --- | --- |
| 交通 | 电动踏板车是骑手的标准装备；公司车队是黑色装甲车 |
| 通讯 | 手机仍然存在，但大多数信息通过 AR 目镜的 HUD 显示 |
| 义体 | 很普遍。富人的义体看不出来，穷人的义体一眼就能看出是机器 |
| 广告 | 到处都是巨幅全息广告和楼体广告，大部分是 ZENITH 的 |
| 语言 | 对白日语；界面以英文为主，配小号日文（见导演方案的"语言"一节） |

---

## 2. 视觉规则（所有场景通用）

色值和规则来自[原片参考分析](../reference-analysis.md)：

- 阴影一律带色：深靛蓝 `#17184D`、深紫、深红，**不用灰黑色**
- 夜景以深靛蓝和紫黑 `#140E1E` 为底，青色 `#29DBD5` 霓虹作边缘光
- 越往城市底层越暗、越饱和；越往顶层越亮、越苍白
- 背景可以细致，人物保持平涂
- **场景设定图里不放人物**，人物是后面合成进去的

**场景通用画风块**：
```
Painted 2D anime background art: flat shapes and soft gradients with no outlines, dense glowing signs and screens, soft bloom around light sources, deep indigo and violet shadows (never grey), saturated cyan and red neon accents, light atmospheric haze, high contrast, no characters, no text.
```

---

## 3. 场景设定

每个场景先做**一张全景**定下整体样子，再用全景当参考图，生成分镜需要的其他角度。做完的场景在 Higgsfield 里保存成 Element，之后的镜头都用它当参考。

### L1 天井（镜头 1、39）

城市中央的巨大竖井，几十层高架绕着井壁盘旋向下，没入黑暗。

| 需要的角度 | 用在哪里 |
| --- | --- |
| 垂直俯拍（正上方往下看） | 镜头 1、39（构图必须完全一致） |

```
Straight-down aerial view into a vast vertical city shaft at night: dozens of stacked
elevated highways spiral down the walls of the shaft into darkness, thousands of tiny cyan
car lights flow along them like current on a circuit board, rain falling toward the camera,
deep indigo and violet buildings with small neon signs.
[场景通用画风块]
16:9.
```

### L2 堵死的高架（镜头 3、7、15–18）

一条悬在两栋楼之间的高架，被 ZENITH 的黑色装甲车队完全堵死，车顶上全是雨水的反光。

| 需要的角度 | 用在哪里 |
| --- | --- |
| 正面远景，车队封路 | 镜头 7 |
| 侧面，车流 | 镜头 3、18 |
| 低角度，车顶 | 镜头 15、16 |

```
An elevated highway suspended between skyscrapers at night, completely jammed: a convoy of
black armored corporate vehicles blocks all lanes, police drones with red and blue lights
hover above, rain, wet car roofs reflecting cyan and red neon, deep indigo ambient light.
Wide front view.
[场景通用画风块]
16:9.
```

### L3 ZENITH 广告墙（镜头 21、23）

高架旁边的一栋大楼，整面外墙是 ZENITH 的巨幅广告，画着吉祥物「ゼンくん」。

| 需要的角度 | 用在哪里 |
| --- | --- |
| 从高架边缘往下看的鱼眼俯拍，一百层的落差 | 镜头 21 |
| 外墙中景，能看到吉祥物广告 | 镜头 23 |

```
A skyscraper facade next to an elevated highway at night, the entire wall is a giant
illuminated advertisement showing a cheerful cartoon delivery rider mascot giving a thumbs
up, the space left blank where the slogan will go. Rain, cyan and white light from the ad,
deep indigo surroundings.
[场景通用画风块]
16:9.
```

### L4 塔顶走廊（镜头 32）

ZENITH Tower 顶层的走廊，从这里开始，红色从画面里褪去，变成无菌室一样的青白色。

```
A long, spotless corridor at the top of a corporate tower: white walls, glossy floor,
thin cyan light strips along the ceiling, a glass door at the far end. Pale sterile
white-cyan light, low saturation, perfectly symmetrical one-point perspective.
[场景通用画风块]
16:9.
```

### L5 白色大厅（镜头 33–38）

走廊尽头的配送大厅，空无一人，一尘不染，墙上有扫描仪。

| 需要的角度 | 用在哪里 |
| --- | --- |
| 全景，固定机位 | 镜头 34 |
| 扫描仪特写 | 镜头 33 |

```
An empty, spotless white delivery lobby at the top of a corporate tower: a package
scanner on the wall with a cyan screen, a glossy white floor, soft elevator-lobby
atmosphere, a small cyan Z-shaped logo on the wall. Pale sterile white-cyan light,
low saturation, clean and silent. Wide fixed shot.
[场景通用画风块]
16:9.
```

### L6 塔顶天台（镜头 41–48）

ZENITH Tower 的天台边缘，脚下是整座 Stack City。风很大，是全片最安静的地方。

| 需要的角度 | 用在哪里 |
| --- | --- |
| 大远景：天台边缘，脚下是城市 | 镜头 41 |
| 近景的背景：天台边缘的栏杆和远处的城市灯光（虚化） | 镜头 42–48 |

```
The edge of a skyscraper rooftop at night, the whole vertical city glowing far below,
strong wind, a low metal railing, dark indigo sky, distant cyan and red city lights.
Lonely, quiet atmosphere. Extreme wide shot.
[场景通用画风块]
16:9.
```

---

## 4. 道具设定

每件道具做一张多角度设定图（正面、侧面、背面、俯视），平光、浅灰背景、不带文字。参考 Higgsfield 短片教程里手表设定图的做法。

| 道具 | 设计 | 用在哪里 |
| --- | --- | --- |
| **电动车** | ZENITH 配发的旧款电动踏板车，车身深青色，车把上有手机支架，挡泥板有凹痕 | 镜头 3、5、15 |
| **配送箱** | 方形背包式，深青色，有青色 ZENITH 标志，边角磨损 | 全片 |
| **手机** | 廉价款，屏幕右上角有一道裂痕，界面在后期加 | 镜头 2、5、11、38、45 |
| **小蛋糕** | 压扁了的纸杯蛋糕，白色奶油上有一颗小草莓，装在透明塑料盒里 | 镜头 43 |
| **打火机** | 透明塑料的廉价打火机，看得见里面的燃料，砂轮式 | 镜头 43–47 |
| **包裹** | 白色小方盒，贴着标签；标签文字在后期加 | 镜头 33、37 |

**道具设定图提示词模板**：
```
Prop design sheet of [道具描述], multiple orthographic views (front, side, back, top),
plain light grey background, flat even lighting, no text, consistent proportions.
2D anime TV series style, flat cel shading with a single hard-edged shadow tone,
thin clean dark lineart of even weight.
```

例如配送箱：
```
Prop design sheet of a square backpack-style courier delivery box, deep teal with a cyan
Z-shaped logo, worn corners and scratches, shoulder straps, multiple orthographic views
(front, side, back, top), plain light grey background, flat even lighting, no text,
consistent proportions.
2D anime TV series style, flat cel shading with a single hard-edged shadow tone,
thin clean dark lineart of even weight.
```
