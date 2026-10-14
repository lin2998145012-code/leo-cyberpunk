"""Review-only thumbnails; leave all input PNGs untouched."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[2]
canvas=Image.new('RGB',(2400,1700),'#24242c')
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',26)
def panel(path,col,row,label):
 x,y=col*600,row*850
 ImageDraw.Draw(canvas).text((x+15,y+12),label,font=font,fill='white')
 if not (root/path).exists():
  ImageDraw.Draw(canvas).text((x+120,y+400),'PENDING',font=font,fill='#999999');return
 with Image.open(root/path) as im:thumb=ImageOps.contain(im.convert('RGB'),(580,790))
 canvas.paste(thumb,(x+(600-thumb.width)//2,y+50+(790-thumb.height)//2))
panel('assets/characters/miles/portrait/miles_portrait_c04.png',0,0,'Original portrait c04')
panel('assets/characters/miles/fullbody/miles_full_c05.png',0,1,'Original full c05')
for v in range(1,4):
 panel(f'assets/characters/miles/master_fix/portrait_fix_v{v}.png',v,0,f'Portrait fix v{v}')
 panel(f'assets/characters/miles/master_fix/full_fix_v{v}.png',v,1,f'Full fix v{v}')
canvas.save(root/'assets/_review/stage05_masters.jpg',quality=95)
print('Built stage05 comparison board.')
