# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont

font = ImageFont.truetype('simsun.ttc',88)
img = Image.open("tt.jpg")
draw = ImageDraw.Draw(img)
draw.text((200,100),u'你好,世界!',(23,55,99),font = font)
draw.text((260,140),unicode('你好','utf-8'),(678,123,234),font = font)
img.save("jpeg.jpg",'JPEG')
