# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

from application.Logger import AppLogger


indexLog = AppLogger.get_loghandle(__name__)


class IndexHandler(RequestHandler):
    """
    首页处理类
    """


    def get(self):
        """
        什么操作都不做，单纯的转向首页
        :return:
        """

        self.render('home/index.html')


__author__ = 'zhgk'
