# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

from common.log.Logger import AppLogger
from common.util.encode import EncodePass
from app.view.view_path import HTML_PATH
from app.bizc.login.login_bzc import LoginBiz


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

        self.render(HTML_PATH.get("Login.login"), errmsg=None)

    def post(self):
        """
        post方法，接收用户名，密码
        :return:
        """
        loging_biz = LoginBiz()
        username = self.get_body_argument("username")
        userpass = self.get_body_argument("password")

        if username is not None and userpass is not None:
            userpass = EncodePass.encode_sha512(userpass)

            query_params = (username, userpass)
            result = loging_biz.validate_user(query_params)
            if result is not None and len(result.rows) == 1:
                self.render(HTML_PATH.get("Main.main"), userinfo=result.rows[0])
            else:
                errmsg = u"您输入的用户名或密码不正确"
                self.render(HTML_PATH.get("Login.login"), errmsg=errmsg)
        else:
            #
            errmsg = u"您输入的用户名密码不正确"
            self.render(HTML_PATH.get("Login.login"), errmsg=errmsg)


__author__ = 'zhgk'
