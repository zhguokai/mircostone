# -*- coding: utf-8 -*-
"""
微信抽签后台类
"""

from tornado.web import RequestHandler

from common.log.Logger import AppLogger


wxLog = AppLogger.get_loghandle(__name__)


class WxCqHandler(RequestHandler):
    """
        处理图片生成与测试
    """


    def get(self):
        # 接收参数,参数个数为0的时候，直接返回页面,后期写一个单独的图片请求类
        args = self.request.arguments
        self.render('control/wxcq/wxcq.html')


    def post(self):
        """
        用于提交数据
        :return:
        """
        wxLog.info("转向结果页面")
        userName = self.get_argument('inputName').decode("utf8")
        self.render('control/wxcq/qcjg.html', userName=userName)


__author__ = 'zhgk'
