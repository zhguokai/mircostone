# -*- coding: utf-8 -*
import time

import urllib
import json
#
from app.weixin.WxConfig import WeiXinConfig
from common.log.Logger import AppLogger
#
"""
获取微信授权凭证
"""
# 定义日志属性类
acLog = AppLogger.get_loghandle(__name__)


class AccessToken:
    # 定义单实例变量
    __instance = None


    def __init__(self):
        # 访问凭证
        self.accToken = None
        self.accTokeGetTime = None


    def getaccestoken(self):
        # print("AccessToke: %s " % self.accTokeGetTime)
        """
        获取微信访问凭证
        需要URl
        :return: self.accToken
        """

        if (self.accToken is None) or (time.time() - self.accTokeGetTime > WeiXinConfig.APP_ACCESS_TOKEN_YXQ):
            self.accToken = ""
            try:
                result_response = urllib.urlopen(WeiXinConfig.APP_ACCESS_TOKEN_URL)
                result_data = result_response.read().decode()
                result_dict = json.loads(result_data, encoding='utf-8')
                """
                {"access_token":"ACCESS_TOKEN","expires_in":7200}
                {"errcode":40013,"errmsg":"invalid appid"}
                """
                # print(result_dict["access_token"])
                if "errcode" in result_dict:
                    print("errcode: %s errmsg: %s" % (result_dict["errcode"], result_dict["errmsg"]))
                else:
                    self.accToken = result_dict["access_token"]
                    self.accTokeGetTime = time.time()
            except BaseException as e:
                print("连接错误: %s" % e)


        else:
            """
            判断当前Token时间是否失效
            """
            pass
        return self.accToken


    @staticmethod
    def getinstance():
        if AccessToken.__instance is None:
            AccessToken.__instance = AccessToken()
        else:
            pass

        return AccessToken.__instance


if __name__ == "__main__":
    """
    测试方法
    """
    acLog.info("AccessToken-" "测试")
    ace = AccessToken.getinstance()

    # t1 = time.time()
    print(ace.getaccestoken())
    # time.sleep(10)
    # print(time.time() - t1)
    # print(ace.getaccestoken())

__author__ = 'zhgk'
