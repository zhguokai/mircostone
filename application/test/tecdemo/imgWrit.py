# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont,ImageFile
import PIL


font = ImageFont.truetype('../simsun.ttc',88)
PIL.ImageFile.LOAD_TRUNCATED_IMAGES = True
img = Image.open("../DSC_1498.JPG")
draw = ImageDraw.Draw(img)
draw.text((200,100),u'你好,世界!',(23,55,99),font = font)
draw.text((260,140),unicode('你好','utf-8'),(678,123,234),font = font)
img.save("../jpesg.jpg",'JPEG')
