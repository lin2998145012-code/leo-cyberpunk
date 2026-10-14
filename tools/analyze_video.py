"""分析一段视频的剪辑节奏、色彩和作画帧率。

既可以分析参考片（官方预告片），也可以检查自己生成的 AI 镜头，
把两边的数据放在一起对比。

用法:
    pip install scenedetect opencv-python-headless numpy
    python tools/analyze_video.py input.mp4 -o out/
    python tools/analyze_video.py input.mp4 -o out/ --strips 12 40   # 给第 12、40 个镜头出逐帧图

输出:
    out/report.txt         镜头时长分布、色相分布、暗部色调、色板
    out/sheet_XX.jpg       每个镜头一张缩略图（标注序号和时长）
    out/palette.png        主色板（上）和高饱和点缀色（下）
    out/strip_N.jpg        指定镜头的连续 16 帧，标注每帧相对上一帧的变化量
"""

import argparse
import os
from collections import Counter

import cv2
import numpy as np
from scenedetect import ContentDetector, detect

HUE_NAMES = ["red", "orange", "yellow", "yel-green", "green", "spring",
             "cyan", "azure", "blue", "violet", "magenta", "rose"]
# 像素变化超过这个比例，算作“换了一张画”；低于它的是压缩噪点或背景微动
NEW_DRAWING = 0.06


def read_frames(path, size):
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 24000 / 1001
    frames = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        frames.append(cv2.resize(f, size, interpolation=cv2.INTER_AREA))
    return np.array(frames), fps


def label(img, text):
    for color, thick in (((0, 0, 0), 4), ((255, 255, 255), 1)):
        cv2.putText(img, text, (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, thick)


def kmeans_palette(bgr, k):
    lab = cv2.cvtColor(bgr.reshape(-1, 1, 3), cv2.COLOR_BGR2LAB).reshape(-1, 3).astype(np.float32)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.5)
    _, lbl, cent = cv2.kmeans(lab, k, None, crit, 4, cv2.KMEANS_PP_CENTERS)
    share = np.bincount(lbl.ravel(), minlength=k) / len(lbl)
    rgb = cv2.cvtColor(cent.reshape(-1, 1, 3).astype(np.uint8), cv2.COLOR_LAB2BGR).reshape(-1, 3)[:, ::-1]
    return [("#%02X%02X%02X" % tuple(rgb[i]), float(share[i])) for i in np.argsort(-share)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("-o", "--out", default="analysis_out")
    ap.add_argument("--strips", type=int, nargs="*", default=[])
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    out = []

    # 1. 镜头切分：min_scene_len=2，保留冲击帧、闪切这类极短镜头
    scenes = detect(args.video, ContentDetector(threshold=27, min_scene_len=2))
    shots = [(s.frame_num, e.frame_num) for s, e in scenes]
    frames, fps = read_frames(args.video, (480, 270))
    if not shots:
        shots = [(0, len(frames))]
    lens = np.array([(e - s) / fps for s, e in shots])
    out.append(f"镜头数 {len(shots)}  平均 {lens.mean():.2f}s  中位数 {np.median(lens):.2f}s")
    for lo, hi in [(0, .25), (.25, .5), (.5, 1), (1, 2), (2, 3), (3, 1e9)]:
        out.append(f"  {lo}-{hi if hi < 1e9 else '∞'}s: {int(((lens >= lo) & (lens < hi)).sum())}")

    # 2. 缩略图：每 20 个镜头一张
    tiles = []
    for i, (s, e) in enumerate(shots):
        t = cv2.resize(frames[min((s + e) // 2, len(frames) - 1)], (384, 216))
        label(t, f"{i + 1} {lens[i]:.2f}s")
        tiles.append(t)
    for p in range(0, len(tiles), 20):
        g = tiles[p:p + 20] + [np.zeros_like(tiles[0])] * (20 - len(tiles[p:p + 20]))
        sheet = np.vstack([np.hstack(g[r * 4:(r + 1) * 4]) for r in range(5)])
        cv2.imwrite(os.path.join(args.out, f"sheet_{p // 20 + 1:02d}.jpg"), sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])

    # 3. 作画帧率：统计镜头内“换画”的间隔（1=一拍一，2=一拍二，3=一拍三）
    gray = np.array([cv2.cvtColor(f, cv2.COLOR_BGR2GRAY) for f in frames]).astype(np.int16)
    chg = (np.abs(np.diff(gray, axis=0)) > 12).mean(axis=(1, 2))
    gaps = Counter()
    for s, e in shots:
        if e - s < 12:
            continue
        new = np.where(chg[s:e - 1] >= NEW_DRAWING)[0]
        gaps.update(np.minimum(np.diff(new), 4).tolist())
    n = sum(gaps.values()) or 1
    out.append("换画间隔（镜头运动和特效也会算进一拍一，结论要结合逐帧图看）:")
    out.append("  " + "  ".join(f"{'4+' if k == 4 else k}帧: {v / n:.0%}" for k, v in sorted(gaps.items())))

    # 4. 色彩：每 3 帧取样
    pix = frames[::3, ::2, ::2].reshape(-1, 3)
    hsv = cv2.cvtColor(pix.reshape(-1, 1, 3), cv2.COLOR_BGR2HSV).reshape(-1, 3).astype(int)
    h, sat, val = hsv[:, 0] * 2, hsv[:, 1], hsv[:, 2]
    lit = val > 20
    out.append(f"纯黑像素 {1 - lit.mean():.0%}  平均饱和度 {sat[lit].mean():.0f}/255  高饱和像素(S>150) {(sat[lit] > 150).mean():.0%}")
    vivid = lit & (sat > 90) & (val > 50)
    hist = np.histogram((h[vivid] + 15) % 360, bins=12, range=(0, 360))[0]
    hist = hist / max(hist.sum(), 1)
    out.append("色相分布: " + "  ".join(f"{nm} {x:.0%}" for nm, x in zip(HUE_NAMES, hist)))
    dark = lit & (val < 90)
    out.append(f"暗部像素中带饱和色(S>40)的比例: {(sat[dark] > 40).mean():.0%}（越高说明阴影越不是灰黑色）")

    pal = kmeans_palette(pix[lit][::5], 16)
    acc_px = pix[lit & (sat > 170) & (val > 150)]
    acc = kmeans_palette(acc_px[::2], 8) if len(acc_px) > 100 else []
    out.append("主色板: " + "  ".join(f"{c} {s:.0%}" for c, s in pal))
    out.append("点缀色: " + "  ".join(f"{c} {s:.0%}" for c, s in acc))

    img = np.full((260, 1200, 3), 30, np.uint8)
    x = 0
    for c, s in pal:
        w = int(round(s * 1200))
        img[:120, x:x + w] = [int(c[i:i + 2], 16) for i in (5, 3, 1)]
        x += w
    for j, (c, _) in enumerate(acc):
        img[140:, j * 150:(j + 1) * 150] = [int(c[i:i + 2], 16) for i in (5, 3, 1)]
        label(img[140:, j * 150:(j + 1) * 150], c)
    cv2.imwrite(os.path.join(args.out, "palette.png"), img)

    # 5. 指定镜头的逐帧图
    for shot in args.strips:
        s, e = shots[shot - 1]
        ts = []
        for k in range(16):
            i = s + k
            t = frames[i].copy() if i < e else np.zeros_like(frames[0])
            if i < e:
                label(t, f"f{k} chg={chg[i - 1] if i > 0 else 0:.3f}")
            ts.append(t)
        cv2.imwrite(os.path.join(args.out, f"strip_{shot}.jpg"),
                    np.vstack([np.hstack(ts[r * 4:(r + 1) * 4]) for r in range(4)]),
                    [cv2.IMWRITE_JPEG_QUALITY, 82])

    report = "\n".join(out)
    open(os.path.join(args.out, "report.txt"), "w", encoding="utf-8").write(report + "\n")
    print(report)


if __name__ == "__main__":
    main()
