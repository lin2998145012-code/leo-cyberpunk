"""检查生成的镜头里，角色和参考图是不是同一个人。

用 CCIP（专门为二次元角色训练的"是不是同一个角色"模型）给每个镜头打分：
分数是镜头里的角色和参考图之间的差异，越小越像。

用原片预告验证过（见 docs/higgsfield-workflow.md 第 6 节）：
- 适合做相对排序：找出一批镜头里"最不像"的那几个，优先返工
- 不适合用固定阈值判对错：整屏单色、画面压了大字、截图里没有脸时会误判
所以报告按分数排序，把明显偏离同批镜头的标出来，最后要人眼确认。

用法:
    python -m venv venv && . venv/bin/activate
    pip install --no-deps dghs-imgutils
    pip install hbutils pillow "numpy<2" scikit-learn huggingface-hub tqdm \
        opencv-contrib-python-headless pandas scipy "emoji>=2.5.0,<2.12" pilmoji \
        "shapely!=2.0.7" pyclipper deprecation hfutils filelock piexif pyrfc6266 \
        urlobject tokenizers onnxruntime
    python tools/check_consistency.py --ref refs/linchi/ --shots shots/ -o report.csv

    --ref    角色参考图文件夹（角色设定包里的正面、侧面、表情等，平光、无文字）
    --shots  要检查的图片或视频文件夹；视频每个取 3 帧（开头、中间、结尾）
"""

import argparse
import csv
import os

import cv2
import numpy as np
from PIL import Image
from imgutils.detect import detect_person
from imgutils.metrics import ccip_difference, ccip_extract_feature

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}
VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv"}


def largest_person(img):
    """裁出画面里最大的那个人；检测不到就用整张图。"""
    dets = detect_person(img)
    if not dets:
        return img
    (x0, y0, x1, y1), _, _ = max(dets, key=lambda d: (d[0][2] - d[0][0]) * (d[0][3] - d[0][1]))
    return img.crop((x0, y0, x1, y1))


def video_frames(path):
    cap = cv2.VideoCapture(path)
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    for label, idx in (("start", 0), ("mid", n // 2), ("end", max(n - 2, 0))):
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, f = cap.read()
        if ok:
            yield label, Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))


def samples(folder):
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        ext = os.path.splitext(name)[1].lower()
        if ext in IMAGE_EXT:
            yield name, "-", Image.open(path).convert("RGB")
        elif ext in VIDEO_EXT:
            for label, img in video_frames(path):
                yield name, label, img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True)
    ap.add_argument("--shots", required=True)
    ap.add_argument("-o", "--out", default="consistency_report.csv")
    args = ap.parse_args()

    refs = [ccip_extract_feature(largest_person(img)) for _, _, img in samples(args.ref)]
    if not refs:
        raise SystemExit(f"{args.ref} 里没有参考图")

    rows = []
    for name, frame, img in samples(args.shots):
        feat = ccip_extract_feature(largest_person(img))
        d = [ccip_difference(feat, r) for r in refs]
        rows.append({"file": name, "frame": frame, "closest": min(d), "mean": float(np.mean(d))})
    if not rows:
        raise SystemExit(f"{args.shots} 里没有可检查的图片或视频")

    # 偏离标准：比这批镜头的中位数高出 1.5 倍四分位距
    means = np.array([r["mean"] for r in rows])
    q1, med, q3 = np.percentile(means, [25, 50, 75])
    limit = q3 + 1.5 * (q3 - q1)
    rows.sort(key=lambda r: -r["mean"])
    for r in rows:
        r["flag"] = "返工候选" if r["mean"] > limit else ""

    with open(args.out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["file", "frame", "mean", "closest", "flag"])
        w.writeheader()
        for r in rows:
            w.writerow({**r, "mean": f"{r['mean']:.3f}", "closest": f"{r['closest']:.3f}"})

    print(f"参考图 {len(refs)} 张，检查 {len(rows)} 帧，中位差异 {med:.3f}，偏离线 {limit:.3f}")
    print("最不像参考图的 10 帧（差异越大越不像）：")
    for r in rows[:10]:
        print(f"  {r['mean']:.3f}  {r['file']} [{r['frame']}] {r['flag']}")
    print(f"完整报告: {args.out}")


if __name__ == "__main__":
    main()
