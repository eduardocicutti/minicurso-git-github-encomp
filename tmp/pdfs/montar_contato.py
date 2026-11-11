from pathlib import Path
from PIL import Image, ImageDraw
import math
files=sorted(Path('tmp/pdfs/rendered').glob('pagina-*.png'))
w,h=330,470
sheet=Image.new('RGB',(w*4,h*math.ceil(len(files)/4)),(220,225,232))
d=ImageDraw.Draw(sheet)
for i,p in enumerate(files):
    im=Image.open(p).convert('RGB')
    im.thumbnail((w-20,h-30))
    x=i%4*w+(w-im.width)//2
    y=i//4*h+22
    sheet.paste(im,(x,y))
    d.text((i%4*w+8,i//4*h+5),p.stem,fill=(20,30,50))
sheet.save('tmp/pdfs/contato.png')
