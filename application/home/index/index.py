# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from PIL import Image,ImageDraw,ImageFont

from application.Logger import weixinLogger


indexLog = weixinLogger.getInstance().logging


class IndexHandler(RequestHandler):
    def get(self):
        # pcon = PostDBConn()
        #sqlstr = "CREATE TABLE public.Q2test (id serial PRIMARY KEY, num integer, data varchar);"
        #pcon.exec_sql(sqlstr)


        self.render('home/yyy.html')


__author__ = 'zhgk'
