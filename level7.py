#current level 7: http://www.pythonchallenge.com/pc/def/oxygen.html
import re
from PIL import Image, ImageFilter
im=Image.open('oxygen.png')

#this loop only find y where grey is
y=0
while True:
    r, g, b, a = im.getpixel((0,y))
    if r==g==b:
        break
    y+=1

message = ''.join([chr(im.getpixel((x, y))[0]) for x in range(0, im.size[0], 7)])# grey is 0-255
out = re.findall('\d+', message)
print(message)
print(''.join(chr(int(i)) for i in out))