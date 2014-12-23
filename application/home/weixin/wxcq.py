# -*- coding: utf-8 -*-
"""
微信抽签后台类
"""
from tornado.web import RequestHandler

from application.Logger import weixinLogger
wxLog = weixinLogger.getInstance().logging
class WxCq(RequestHandler):
    """

    """


    def get(self):
        """
        用于处理转向页面
        :return:
        """
        self.render('home/wxcq/wxcq.html')


    def post(self):
        """
        用于提交数据
        :return:
        """
        wxLog.info("转向结果页面")
        self.render('home/wxcq/qcjg.html')


__author__ = 'zhgk'
