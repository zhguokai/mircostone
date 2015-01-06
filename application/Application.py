# -*- coding: utf-8 -*-
# 引入系统包
import os

# 引入框架包
from tornado.web import Application
from tornado import options

# 自定义类
from application.Logger import AppLogger
from application.home.index.index import IndexHandler
from application.home.weixin.wxcq import WxCqHandler
from application.weixin.Weixin import AccessWeixinHandler
from application.home.weixin.query_img import QueryImgHandler
# 定义路径
os.path.join(os.path.dirname(__file__))
options.define("port",default = 8083,help = "Run server on a specific port",type = int)
# 定义日志
applog = AppLogger.get_loghandle(__name__)


class MainApplication():
    """
        应用程序启动入口
    """


    def __init__(self):
        """
        初始化方法,
        :return:
        """


    @staticmethod
    def create_application():
        """
        静态方法启动应用实例
        :return:
        """

        handler = [
            (r"/",IndexHandler),
            (r"/AccessWeixin",AccessWeixinHandler),
            (r"/wxcq",WxCqHandler),
            (r"/wxcq/queryImg",QueryImgHandler)

        ]
        settings = {
            "static_path":os.path.join(os.path.dirname(__file__),"static"),
            "template_path":os.path.join(os.path.dirname(__file__),"templates"),
            "debug":True,
        }

        app = Application(handler,**settings)
        # 加入日志
        applog.info(u"应用启动，临听端口: %s" % options.options.port)
        app.listen(options.options.port)
        return app


__author__ = 'zhgk'
