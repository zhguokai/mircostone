# -*- coding: utf-8 -*-

"""
定义公共参数接口
"""


class WeiXinConfig:
    # 应用ID
    APP_ID = 'wx497d167c202042f1'
    # 应用密钥匙
    APP_SEC = "971b1d507404e04fb44f4da06744eb43"
    # 访问凭证获取地址
    APP_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='\
                           + APP_ID + '&secret=' + APP_SEC
    # 访问凭证有效期(此处设为7000)
    APP_ACCESS_TOKEN_YXQ = 7000

    # 获取用户信息URL
    APP_USER_URL = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN"

    APP_MENU_CREATE_URL = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN"

    APP_BASE_URL = "http://pyweb.coding.io/"


    def __init__(self):
        """

        :return:
        """


__author__ = 'zhgk'
