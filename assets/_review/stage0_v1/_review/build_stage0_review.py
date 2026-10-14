"""Build review collages only; original references and generations remain unchanged."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[2]
out=root/'assets/_review'
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',24)
def panel(canvas,path,box,label):
    x,y,w,h=box
    with Image.open(root/path) as original:
        thumb=ImageOps.contain(original.convert('RGB'),(w,h-40))
    canvas.paste(thumb,(x+(w-thumb.width)//2,y+40+(h-40-thumb.height)//2))
    ImageDraw.Draw(canvas).text((x+12,y+7),label,font=font,fill='#ffffff')
canvas=Image.new('RGB',(1500,660),'#24242c')
for i in range(3):
    panel(canvas,f'assets/_review/stage0_attempts/miles_portrait_c01_a{i+1}.png',(i*500,0,500,660),f'c01 / a{i+1} - FAIL')
canvas.save(out/'stage0_portraits.jpg',quality=95)
canvas=Image.new('RGB',(1600,1000),'#24242c')
items=[('refs/style/char_david_smile.jpg','STYLE REF 1'),('assets/_review/stage0_attempts/miles_portrait_c01_a2.png','c01 / a2 - FAIL'),('refs/style/char_lucy_closeup.jpg','STYLE REF 2'),('assets/_review/stage0_attempts/miles_portrait_c01_a3.png','c01 / a3 - FAIL')]
for i,(path,label) in enumerate(items):
    panel(canvas,path,((i%2)*800,(i//2)*500,800,500),label)
canvas.save(out/'stage0_style_compare.jpg',quality=95)
print('Built review collages; no cropping or watermark removal.')
