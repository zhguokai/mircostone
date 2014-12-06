# -*- coding: utf-8 -*-
import  urllib2
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
                                                       +AccessToken.getinstance().getaccestoken())
        dataStr = """
        {
            "button":[
                {
                    "type":"click",
                    "name":"签到",
                    "key":"V1001_TODAY_MUSIC"
                },
                {
                    "name":"报工",
                    "sub_button":[
                        {
                            "type":"view",
                            "name":"搜索",
                            "url":"http://www.soso.com/"
                        },
                        {
                            "type":"view",
                            "name":"视频",
                            "url":"http://v.qq.com/"
                        },
                        {
                            "type":"click",
                            "name":"赞一下我们",
                            "key":"V1001_GOOD"
                        }]
                },{
                    "name":"打码",
                    "sub_button":[
                        {
                            "type":"view",
                            "name":"V2"
                        },
                        {
                            "type":"view",
                            "name":"V2"
                        },
                        {
                            "type":"view",
                            "name":"V2"
                        }
                    ]
                }
            ]
        }
        """
        req = urllib2.Request(url,data=dataStr.encode(encoding='utf-8'))
        req.add_header("Content-type", "text/json; charset='UTF-8'")
        res = urllib2.urlopen(req)
        print(res)


if __name__ == "__main__":
    m =MenuTool()
    m.createMenu()



__author__ = 'zhgk'

