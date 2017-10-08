# http://www.pythonchallenge.com/pc/return/good.html u:huge pas:file

from PIL import Image, ImageDraw

first = open('first.txt').read().split(',')
second = open('second.txt').read().split(',')
list_1 = [int(i) for i in first]
list_2 = [int(i) for i in second]
img = Image.new('RGB', (500, 500), 'black')
draw = ImageDraw.Draw(img)
draw.line(list_1)
draw.line(list_2)
img.show()