# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        # templeate = Template("home/index.html")
        self.render('home/index.html')


__author__ = 'zhgk'
