# -*- coding: utf-8 -*-

"""
定义公共接口
"""


class WeiXinConfig:
    # 应用ID
    APP_ID = 'wx36d0f120ffba09b1'
    # 应用密钥匙
    APP_SEC = "c19f328910d187fbf671d72afc25e418"
    # 访问凭证获取地址
    APP_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' \
                           + APP_ID + '&secret=' + APP_SEC
    # 访问凭证有效期(此处设为7000)
    APP_ACCESS_TOKEN_YXQ = 7000


__author__ = 'zhgk'
