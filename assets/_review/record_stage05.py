"""Copy untouched edit output and record provenance; candidate promotion is separate."""
from pathlib import Path
import sys,json,csv,hashlib,shutil
from PIL import Image
kind,version,attempt,source,status,notes=sys.argv[1:]
job=json.loads(Path('assets/_review/stage05_prompts.json').read_text())[kind]
prefix='portrait' if kind=='portrait' else 'full'
target=Path(f'assets/_review/stage05_attempts/{prefix}_fix_v{version}_a{attempt}.png')
assert not target.exists()
target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
with Image.open(target) as im:
 im.load();assert im.format=='PNG';size=f'{im.width}x{im.height}'
entry=dict(kind=kind,version=int(version),attempt=int(attempt),source=source,file=str(target),size=size,self_check=status,notes=notes,prompt=job['prompt'],refs=job['refs'],sha256=hashlib.sha256(target.read_bytes()).hexdigest())
p=Path('assets/_review/stage05_generation_log.json');entries=json.loads(p.read_text()) if p.exists() else [];entries.append(entry);p.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
with Path('assets/manifest.csv').open('a',newline='') as f:
 csv.writer(f,lineterminator="\n").writerow([job['task'],str(target),'not-exposed',size,'not-exposed',';'.join(job['refs']),attempt,status,f'stage0.5 v{version}; '+notes])
print(str(target),size,status)
