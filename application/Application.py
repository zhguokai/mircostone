# -*- coding: utf-8 -*-
import os

from tornado.web import Application
import tornado.options

from application.home.index.index import IndexHandler
from application.weixin.Weixin import AccessWeixinHandler


tornado.options.define("port", default=80, help="Run server on a specific port", type=int)
os.path.join(os.path.dirname(__file__))


class MainApplication():
    """

    """

    def createApplication(self):
        """
        :return:
        """""
        handler = [
            (r"/.*", IndexHandler),
            (r"/AccessWeixin.*", AccessWeixinHandler)

        ]
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "debug": True,
        }

        app = Application(handler, **settings)
        print(tornado.options.options.port)
        app.listen(tornado.options.options.port)
        return app


__author__ = 'zhgk'
