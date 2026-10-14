"""Compose review boards; never crop, resize or mirror source files in place."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[2];out=root/'assets/_review'
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',28)
def panel(canvas,path,box,label):
 x,y,w,h=box
 if (root/path).exists():
  with Image.open(root/path) as im:thumb=ImageOps.contain(im.convert('RGB'),(w-16,h-48))
  canvas.paste(thumb,(x+(w-thumb.width)//2,y+42+(h-48-thumb.height)//2))
 ImageDraw.Draw(canvas).text((x+12,y+7),label,font=font,fill='white')
canvas=Image.new('RGB',(2200,1200),'#24242c')
for i in range(8):panel(canvas,f'assets/characters/miles/portrait/miles_portrait_c{i+1:02}.png',((i%4)*550,(i//4)*600,550,600),f'v2 portrait c{i+1:02}')
canvas.save(out/'stage0_portraits.jpg',quality=95)
paths=sorted((root/'assets/characters/miles/fullbody').glob('*.png'))
canvas=Image.new('RGB',(1800,1960),'#24242c')
for i in range(6):
 path=f'assets/characters/miles/fullbody/miles_full_c{i+1:02}.png';label=f'v2 full c{i+1:02}' if (root/path).exists() else f'c{i+1:02} - PENDING'
 panel(canvas,path,((i%3)*600,(i//3)*980,600,980),label)
canvas.save(out/'stage0_fullbody.jpg',quality=95)
canvas=Image.new('RGB',(1800,1100),'#24242c')
items=[('refs/style/char_lucy_closeup.jpg','STYLE REF 1'),('assets/characters/miles/portrait/miles_portrait_c02.png','v2 portrait c02'),('refs/style/char_gloria_profile.jpg','STYLE REF 2'),('assets/characters/miles/portrait/miles_portrait_c04.png','v2 portrait c04')]
for i,(path,label) in enumerate(items):panel(canvas,path,((i%2)*900,(i//2)*550,900,550),label)
canvas.save(out/'stage0_style_compare.jpg',quality=95)
print(f'Built 8-portrait board, {len(paths)}-of-6 fullbody board, and style comparison.')
