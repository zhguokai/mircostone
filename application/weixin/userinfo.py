# -*- coding: utf-8 -*-
"""
获取用户信息
"""
import json
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# 引入凭证获取工具
from application.weixin.AccessToken import AccessToken
from application.weixin.WxConfig import WeiXinConfig
from application.Logger import AppLogger

# 定义日志
log = AppLogger.get_loghandle(__name__)


class UserInfo:
    """
    用于处理用户相关信息
    """


    def __init__(self):
        log.info("%s 初始化" % self.__class__)


    @staticmethod
    def get_userinfo_openid(openid):
        """
        取得用户信息
        :param openid:
        :return:{
                "subscribe": 1,
                "openid": "o6_bmjrPTlm6_2sgVt7hMZOPfL2M",
                "nickname": "Band",
                "sex": 1,
                "language": "zh_CN",
                "city": "广州",
                "province": "广东",
                "country": "中国",
                "headimgurl":"http://wx.qlogo.cn/mmopen
                    /g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4e
                    Msv84eavHiaiceqxibJxCfHe/0",
                "subscribe_time": 1382694957,
                "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL"
            }
        """
        url = WeiXinConfig.APP_USER_URL
        url = url.replace("=ACCESS_TOKEN","=" + AccessToken.getinstance().getaccestoken())
        url = url.replace("=OPENID","=" + openid)
        log.info("获取用户信息URL: %s" % url)

        result_response = urllib.urlopen(url)
        result_data = result_response.read().decode()
        userinfo_dict = json.loads(result_data,encoding = 'utf-8')
        log.info("用户信息:%s" % userinfo_dict)
        if "errcode" in userinfo_dict:
            log.error("获取用户出错，错误码：%s  错误消息:%s"
                      % (userinfo_dict["errcode"],userinfo_dict["errmsg"]))
        return userinfo_dict


if __name__ == "__main__":

    UserInfo.get_userinfo_openid('zhangsan')

__author__ = 'zhgk'
