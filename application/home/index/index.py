# -*- coding: utf-8 -*-
from tornado.web import RequestHandler

from application.db.connect.postgresql_conn import PostDBConn


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
