# -*- coding: utf-8 -*
import time

import urllib.request
import urllib.response
import urllib.error
import json
#
from application.weixin.WxConfig import WeiXinConfig
#
"""
获取微信授权凭证
"""


class AccessToken:
    # 定义单实例变量
    instance = None

    def __init__(self):
        # 访问凭证
        self.accToken = None
        self.accTokeGetTime = None

    def getaccestoken(self):
        print("AccessToke: %s " % self.accTokeGetTime)
        """
        获取微信访问凭证
        需要URl
        :return: self.accToken
        """
        if (self.accToken is None) or (time.time() - self.accTokeGetTime > WeiXinConfig.APP_ACCESS_TOKEN_YXQ):
            self.accToken = ""
            try:
                result_response = urllib.request.urlopen(WeiXinConfig.APP_ACCESS_TOKEN_URL)
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
            except urllib.error.ContentTooShortError as cex:
                print("连接错误: ")
                print(cex.content)
            except urllib.error.HTTPError as httpex:
                print("HTTP协议错误")
                print(httpex.code)
            except urllib.error.URLError as uex:
                print("URL 错误")
                print(uex.reason)

        else:
            """
            判断当前Token时间是否失效
            """
            pass
        return self.accToken

    @staticmethod
    def getinstance():
        if AccessToken.instance is None:
            AccessToken.instance = AccessToken()
        else:
            pass

        return AccessToken.instance


if __name__ == "__main__":
    """
    测试方法
    """
    # ace = AccessToken.getinstance()
    # t1 = time.time()
    # print(ace.getaccestoken())
    # time.sleep(10)
    # print(time.time() - t1)
    # print(ace.getaccestoken())

__author__ = 'zhgk'
