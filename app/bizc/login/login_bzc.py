# -*- coding: utf-8 -*-
"""
登录业务处理类，用于验证用户密码，存储Session，返回菜单等
"""


class LoginBiz(object):
    """
        登录业务处理
    """

    def __init__(self):
        """
        初始化
        :return:
        """

    def validate_user(self, params):
        """
        验证有户信息
        :param username:
        :param userpass:
        :return True Or False:
        """

        query_user_str = """
            select user_id from b_wx_users WHERE user_code=%s AND user_pass =%s
        """


__author__ = 'zhgk'
