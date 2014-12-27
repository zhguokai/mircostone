# -*- coding: utf-8 -*-
from tornado.web import RequestHandler

from PIL import Image,ImageDraw,ImageFont

from application.db.connect.postgresql_conn import PostDBConn
from application.Logger import weixinLogger

indexLog = weixinLogger.getInstance().logging


class IndexHandler(RequestHandler):
    def get(self):
        # url = "http://"+self.get_query_argument("url");
        # dicts = self.request.argrument
        #url = "http://"+self.request.argrument["url"]
        #self.redirect(url.decode(encoding='utf8'))
        # templeate = Template("home/index.html")
        pcon = PostDBConn()
        sqlstr = "CREATE TABLE public.Q2test (id serial PRIMARY KEY, num integer, data varchar);"
        #pcon.exec_sql(sqlstr)
        try:
            font = ImageFont.truetype('simsun.ttc',88)
            img = Image.open("qt2.png")
            draw = ImageDraw.Draw(img)
            draw.text((200,100),u'你好,世界!',(23,55,99),font = font)
            draw.text((260,140),unicode('你好','utf-8'),(678,123,234),font = font)
            img.save("jpeg.png",'PNG')
            indexLog.info("成功了")
        except Exception as e:
            indexLog.info(e.message)

        self.render('home/yyy.html')


__author__ = 'zhgk'
