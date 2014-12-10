# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        url = "http://"+self.get_query_argument("url");
        #dicts = self.request.argrument
        #url = "http://"+self.request.argrument["url"]
        self.redirect(url.decode(encoding='utf8'))
        # templeate = Template("home/index.html")
        self.render('home/index.html')


__author__ = 'zhgk'
