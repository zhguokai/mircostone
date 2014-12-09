# -*- coding: utf-8 -*-
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from application.weixin.WxConfig import WeiXinConfig
from application.weixin.AccessToken import AccessToken


class MenuTool:
    """
    自定义菜单接口
    """


    def createMenu(self):
        url = WeiXinConfig.APP_MENU_CREATE_URL.replace("=ACCESS_TOKEN","="
                                                       + AccessToken.getinstance().getaccestoken())
        dataStr = """
{
    "button": [
        {
            "name": "签到",
            "sub_button": [
                {
                    "type": "click",
                    "name": "早上",
                    "key": "Z001"
                },
                {
                    "type": "click",
                    "name": "晚上",
                    "key": "Z003"
                },
                {
                    "type": "click",
                    "name": "中午",
                    "key": "Z002"
                },
                {
                    "type": "click",
                    "name": "下午",
                    "key": "Z004"
                },
                {
                    "type": "click",
                    "name": "后半夜",
                    "key": "Z006"
                }
            ]
        },
        {
            "name": "报工",
            "sub_button": [
                {
                    "type": "view",
                    "name": "本人报工",
                    "url": "http://www.soso.com/"
                },
                {
                    "type": "view",
                    "name": "代报工",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "审批报工",
                    "key": "V1001_GOOD"
                },
                {
                    "type": "click",
                    "name": "提交工时",
                    "key": "V1002_GOOD"
                },
                {
                    "type": "click",
                    "name": "提交请假",
                    "key": "V1003_GOOD"
                }
            ]
        },
        {
            "name": "请假",
            "sub_button": [
                {
                    "type": "click",
                    "name": "事假",
                    "key": "J_001"
                },
                {
                    "type": "click",
                    "name": "痌假",
                    "key": "J_002"
                },
                {
                    "type": "click",
                    "name": "产假",
                    "key": "J_003"
                },
                {
                    "type": "click",
                    "name": "带薪假",
                    "key": "J_004"
                },
                {
                    "type": "click",
                    "name": "年假",
                    "key": "J_005"
                }
            ]
        }
    ]
}
        """
        req = urllib2.Request(url,data = dataStr.encode(encoding = 'utf-8'))
        req.add_header("Content-type","text/json; charset='UTF-8'")
        res = urllib2.urlopen(req)
        print(res)


if __name__ == "__main__":
    m = MenuTool()
    m.createMenu()

__author__ = 'zhgk'

