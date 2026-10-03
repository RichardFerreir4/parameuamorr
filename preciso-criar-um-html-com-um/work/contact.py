from PIL import Image, ImageDraw
import os, glob
fs=glob.glob(r'D:\pdc\*.jpeg')
out=Image.new('RGB',(660,((len(fs)+2)//3)*210),'white')
d=ImageDraw.Draw(out)
for i,f in enumerate(fs):
 im=Image.open(f); im.thumbnail((210,165))
 x=(i%3)*220; y=(i//3)*210
 out.paste(im,(x,y)); d.text((x,y+170),os.path.basename(f)[:31],fill='black')
out.save(r'C:\Users\Richard\Documents\Codex\2026-10-02\preciso-criar-um-html-com-um\work\contact.jpg')
