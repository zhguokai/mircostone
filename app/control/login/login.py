# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

from common.log.Logger import AppLogger
from common.util.encode import EncodePass

loginLog = AppLogger.get_loghandle(__name__)


class LoginHandler(RequestHandler):
    """
    登录类，访问域名端口时，执行Get方法，转向登录页面
    """

    def data_received(self, chunk):
        pass

    def get(self):
        """
        什么操作都不做，单纯的转向首页
        :return:
        """

        self.render('app/login/login.html')

    def post(self):
        """
        post方法，接收用户名，密码
        :return:
        """
        username = self.get_argument("usernmae")
        userpass = self.get_argument("userpass")

        if username is not None and userpass is not None:
            userpass = EncodePass.encode_sha512(userpass)


__author__ = 'zhgk'
