"""Copy built-in output unchanged and record observed metadata."""
import csv,json,shutil,sys
from pathlib import Path
from PIL import Image
kind,number,attempt,source,status,notes=sys.argv[1:]
job=json.loads(Path('assets/_review/stage0_prompts.json').read_text())[kind]
prefix='miles_portrait' if kind=='portrait' else 'miles_full'
target=Path(f'assets/_review/stage0_attempts/{prefix}_c{int(number):02d}_a{attempt}.png')
target.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,target)
with Image.open(target) as im:
 im.load();size=f'{im.width}x{im.height}'
if size!=job['size']:
 notes+=f'; 实际尺寸 {size}，要求 {job["size"]}，未裁剪或缩放'
 if status=='pass':status='unsure'
refs=';'.join('refs/style/'+Path(p).name for p in job['refs'])
with Path('assets/manifest.csv').open('a',newline='') as f:
 csv.writer(f).writerow([job['task'],str(target),'builtin-default-undisclosed',size,'not-exposed',refs,attempt,status,notes])
print(target,size,status)
