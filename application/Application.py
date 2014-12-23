# -*- coding: utf-8 -*-
#引入系统包
import os

#引入框架包
from tornado.web import Application
from tornado import options

#自定义类
from application.home.index.index import IndexHandler
from application.home.weixin.wxcq import WxCq
from application.weixin.Weixin import AccessWeixinHandler
from application.Logger import weixinLogger
#定义路径
os.path.join(os.path.dirname(__file__))
options.define("port", default=8083, help="Run server on a specific port", type=int)

#定义日志
appLog = weixinLogger.getInstance().logging

class MainApplication():

    """

    """
    def __init__(self):
        """
        初始化方法
        :return:
        """


    def createApplication(self):
        """
        :return:
        """""
        handler = [
            (r"/", IndexHandler),
            (r"/AccessWeixin", AccessWeixinHandler),
            (r"/wxcq",WxCq)


        ]
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "debug": True,
        }

        app = Application(handler, **settings)
        #加入日志
        appLog.info(options.options.port)
        app.listen(options.options.port)
        return app


__author__ = 'zhgk'
