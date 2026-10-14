"""Preserve a generated PNG unchanged; append actual metadata and prompt provenance."""
import csv,json,shutil,sys,hashlib
from pathlib import Path
from PIL import Image
kind,number,attempt,source,status,notes=sys.argv[1:]
job=json.loads(Path('assets/_review/stage0_prompts.json').read_text())[kind]
prefix='miles_portrait' if kind=='portrait' else 'miles_full'
stem=f'{prefix}_c{int(number):02d}'
target=Path(f'assets/_review/stage0_attempts/{stem}_a{attempt}.png')
assert not target.exists(), target
target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
with Image.open(target) as im:
 im.load();assert im.format=='PNG';size=f'{im.width}x{im.height}'
notes='v2；'+notes
if size!=job['size']: notes+=f'; 实际尺寸 {size}，目标 {job["size"]}；按1.7保留原图'
refs=';'.join(job['refs'])
if status!='fail':
 candidate=Path(f'assets/characters/miles/{kind}/{stem}.png');candidate.parent.mkdir(parents=True,exist_ok=True)
 assert not candidate.exists(),candidate
 shutil.copy2(target,candidate);notes+=f'; 候选副本 {candidate}'
with Path('assets/manifest.csv').open('a',newline='') as f:
 csv.writer(f).writerow([job['task'],str(target),'not-exposed',size,'not-exposed',refs,attempt,status,notes])
log=Path('assets/_review/stage0_generation_log.json');entries=json.loads(log.read_text()) if log.exists() else []
entries.append(dict(version=2,kind=kind,candidate=int(number),attempt=int(attempt),source=source,file=str(target),size=size,self_check=status,notes=notes,prompt=job['prompt'],refs=job['refs'],sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
log.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
print(target,size,status)
