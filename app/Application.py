# -*- coding: utf-8 -*-
# 引入系统包
import os
# 定义路径
os.path.join(os.path.dirname(__file__))

# 引入框架包
from tornado.web import Application
from tornado import options

from app.control.login.login import LoginHandler
from app.control.weixin.wxcq import WxCqHandler
from app.weixin.Weixin import AccessWeixinHandler
from app.control.weixin.query_img import QueryImgHandler
from static import static_path
from templates import templates_path
from common.log.Logger import AppLogger
# 定义日志
applog = AppLogger.get_loghandle(__name__)
options.define("port", default=8083, help="Run server on a specific port", type=int)


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
            (r"/", LoginHandler),
            (r"/AccessWeixin", AccessWeixinHandler),
            (r"/wxcq", WxCqHandler),
            (r"/wxcq/queryImg", QueryImgHandler)
        ]
        settings = {
            "static_path": static_path,
            "template_path": templates_path,
            "debug": True,
        }

        app = Application(handler, **settings)
        # 加入日志
        applog.info(u"应用启动，临听端口: %s" % options.options.port)
        app.listen(options.options.port)
        return app


__author__ = 'zhgk'
