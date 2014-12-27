# -*- coding: utf-8 -*-
from tornado.web import RequestHandler

from application.db.connect.postgresql_conn import PostDBConn
from PIL import Image,ImageDraw,ImageFont

class IndexHandler(RequestHandler):
    def get(self):
        # url = "http://"+self.get_query_argument("url");
        #dicts = self.request.argrument
        #url = "http://"+self.request.argrument["url"]
        #self.redirect(url.decode(encoding='utf8'))
        # templeate = Template("home/index.html")
        pcon = PostDBConn()
        sqlstr = "CREATE TABLE public.Q2test (id serial PRIMARY KEY, num integer, data varchar);"
        pcon.exec_sql(sqlstr)
        self.render('home/yyy.html')


__author__ = 'zhgk'

if __name__=="main":
    font = ImageFont.truetype('simsun.ttc',88)
    img = Image.open("bg_02.jpg")
    draw = ImageDraw.Draw(img)
    draw.text((200,100),u'你好,世界!',(23,55,99),font = font)
    draw.text((260,140),unicode('你好','utf-8'),(678,123,234),font = font)
    img.save("jpeg.jpg",'JPEG')
