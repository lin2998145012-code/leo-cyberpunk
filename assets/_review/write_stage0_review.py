from pathlib import Path
import csv,json,hashlib
p=Path('assets/_review');logs=json.loads((p/'stage0_generation_log.json').read_text());policy=json.loads((p/'stage0_policy.json').read_text())
portraits=sorted(Path('assets/characters/miles/portrait').glob('*.png'));full=sorted(Path('assets/characters/miles/fullbody').glob('*.png'))
lines=['# 素材审查记录','','## 阶段 0 第 2 版（2026-10-14）','','执行依据：`claude/gifted-faraday-1hwuw1` 的 `1f66197`，已同步到 `codex/assets`。第 1 版已作废，原文件按 assets 内相对路径归档至 `assets/_review/stage0_v1/`；manifest 保留旧行并添加 `v1 作废`，旧路径指向归档文件。更早的 T1.* 记录与未跟踪素材维持原状。','','### 导演本轮补充','','“不要纠结左右，这个有镜像的，无所谓”：从收到这条指示后，不再因耳机、挑染或义肢的左右而淘汰、重试。原始 PNG 未镜像。c03 的一次左右重试发生在此指示之前。','','### 进度与工具边界','',f'- 定妆候选 {len(portraits)}/8；全身候选 {len(full)}/6；共调用内置生图工具 {len(logs)} 次。', '- 模型与质量参数均未公开，manifest 如实标为 `not-exposed`；未调用 API 密钥。', '- 固定块原样展开，仅按 §1.7 在末尾添加方形/竖构图请求。实际提示词见 `stage0_prompts.json`，逐次来源、提示词、引用与哈希见 `stage0_generation_log.json`。', '- 定妆图实际 1254×1254，全身图实际 1024×1536；未裁剪、缩放或镜像原图。对比图只做缩略排版与编号，完整参考图未裁剪、未去水印。','', '### 定妆候选的共同观察','','八张均见倦眼、黑眼圈、长发小揪、白色耳机与抬起的目镜，未见剃发、大翻领夹克、黄色服装、金链子、背心或文字。细线、窄眼与大块紫色硬边阴影接近参考；目镜普遍偏厚，灰底和部分色块有轻微渐变，脸部紫色环境光比平光设定更重，尚需导演判断画风。自检记 `unsure`，不声称所有严格画风要求已通过。胸像无法确认雨披长度、背后 Z 或义肢。','']
for path in portraits:
 n=int(path.stem[-2:]);d=[x for x in logs if x['kind']=='portrait' and x['candidate']==n][-1]
 lines.append(f'- c{n:02}（第 {d["attempt"]} 次）：'+d['notes'].split('；',1)[1].split('; 候选副本')[0])
lines+=['','### 全身候选','']
for path in full:
 n=int(path.stem[-2:]);sha=hashlib.sha256(path.read_bytes()).hexdigest();d=next(x for x in logs if x['kind']=='fullbody' and x['candidate']==n and x['sha256']==sha)
 lines.append(f'- c{n:02}（第 {d["attempt"]} 次，{d["self_check"]}）：'+d['notes'].split('；',1)[1].split('; 候选副本')[0])
lines+=['','全身正面图不能验证背后 Z；看不见的特征不算已确认。','', '### 返工记录','']
for d in logs:
 if d['self_check']=='fail':lines.append(f'- {d["kind"]} c{d["candidate"]:02} / a{d["attempt"]}：{d["notes"]}')
lines+=['','### 需要导演决定的问题','']
lines+=['已按 §1.4 报告灯数问题；没有收到放宽灯数的答复，也没有修改设计或提示词。复核 §1.6 后，按“3 次都不合格，保留最好的一张，在 REVIEW.md 里标出来”继续做齐不同编号。c01、c02、c04、c05 均保留 fail，不因收录为候选而视作通过；c03、c06 可辨 5 颗灯，仍有各自的细节偏差。', '', '阶段 0 第 2 版候选与对比板已齐，等待导演验收画风和选择编号。建议先看定妆 c02/c04，以及全身 c03/c06；其余选项也完整保留。请在 assets/selections.md 中记录选中的定妆照与全身图编号，若选中存在灯数偏差的图，另行决定修复方式。未进入阶段 1。', '', '### 对比板', '', '- 定妆：[stage0_portraits.jpg](_review/stage0_portraits.jpg)', '- 全身：[stage0_fullbody.jpg](_review/stage0_fullbody.jpg)', '- 参考与候选：[stage0_style_compare.jpg](_review/stage0_style_compare.jpg)', '- 原图与生成尝试对应：[stage0_candidate_index.json](_review/stage0_candidate_index.json)']
Path('assets/REVIEW.md').write_text('\n'.join(lines)+'\n')
print('Updated review.')
