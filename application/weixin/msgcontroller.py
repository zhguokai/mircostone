# -*- coding: utf-8 -*-
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from application.Logger import weixinLogger
from application.weixin.userinfo import UserInfo
from application.weixin.menu import MenuTool

# 定义日志工具
log = weixinLogger.getInstance().logging


class MsgTextController:
    """
    文本消处理
    """


    def __init__(self):
        """

        :return:
        """


    def reciveTextMsg(self,requstHandler,msgData):
        """
            处理文本消息
        :param msgData:
        :return:
        """
        # 消息类型
        msgType = msgData.find('MsgType').text
        # 公众账号
        toUserName = msgData.find('ToUserName').text
        # 来源用户名称
        fromUserName = msgData.find('FromUserName').text
        # 消创建时间
        createTime = msgData.find('CreateTime').text
        # 消息类型
        msgType = msgData.find('MsgType').text
        # 消息ID
        msgid = msgData.find('MsgId').text
        # 消息内容
        content = msgData.find('Content').text
        log.info("存储消息：%s" % content)
        log.info("用户：%s" % fromUserName)

        user = UserInfo.get_userinfo_openid(fromUserName)

        log.info("用户 %s 发来了消息: %s" % (user["nickname"],content))

        """
        根据content去数据库中查询要回复的内容，如果存在，将查询的信息直接回复
        否则回复:你在说什么
        """


        # 根据消内容，确认回复消息
        if content == "1":
            sendMsgContent = "老婆：我想你了"
        elif content == "2":
            sendMsgContent = "老婆：我恨你不理我"
        elif content == "3":
            sendMsgContent = "老婆：我错了，不要烦弃俺"
        elif content == "4":
            sendMsgContent = "老婆：我爱你哟"
        elif content == "5":
            sendMsgContent = "老婆：我真的不知道ing"
        elif content=="6":
            sendMsgContent="<a href='http://pyweb.coding.io?url=hzbei.taobao.com'>点击进行淘宝店</a>"
        elif content == "CM881212":
            m = MenuTool()
            m.createMenu()
            sendMsgContent = "目录创建完成"

        else:
            sendMsgContent = "你在说什么？我听不懂ing...\n"\
                             "1:我想你\n"\
                             "2:我恨你\n"\
                             "3:我烦你\n"\
                             "4:我爱你\n"\
                             "5:我不知道\n"\
                             "<a href='pyweb.coding.io'>访问主页</a>\n"
        # sendMsgConent = getSendMsg(content)


        sendMsgData = { "toUser":fromUserName,"fromUser":toUserName,"msgType":msgType,
                        "sendMsg":sendMsgContent }


        # 调用回复文本消息方法
        self.sendTextMsg(requstHandler,sendMsgData)
        return True


    def sendTextMsg(self,requstHandler,sendMsgData):
        """
            发送文本消息
        """

        sendXmlStr =\
            """<xml>
                    <ToUserName><![CDATA[""" + sendMsgData["toUser"] + """]]></ToUserName>
                <FromUserName><![CDATA[""" + sendMsgData["fromUser"] + """]]></FromUserName>
                <CreateTime>""" + str(int(time.time())) + """</CreateTime>
                <MsgType><![CDATA[""" + sendMsgData["msgType"] + """]]></MsgType>
                <Content><![CDATA[""" + sendMsgData["sendMsg"] + """]]></Content>
                </xml>
            """

        # 设置返回消息头
        requstHandler.set_header("Content-type","text/xml; charset='UTF-8'")
        requstHandler.write(sendXmlStr)
        return True


class MsgImgController:
    """
    图片消息处理
    """


    def __init__(self):
        pass


    def reciveImgMsg(self,requstHandler,msgData):
        """
        处理图片消息
        :param requstHandler:
        :param msgData:
        :return:
        """
        pass


class MsgVoiceController:
    """
    声音消息处理
    """


    def __init__(self):
        pass


    def reciveVoiceMsg(self,requstHandler,msgData):
        pass


class MsgVideoController:
    """
    视频消息处理
    """


    def __init__(self):
        pass


    def reciveVideoMsg(self,requstHandler,msgData):
        pass


class MsgLocationController:
    """
    位置消息处理
    """


    def __init__(self):
        pass


    def reciveLocationMsg(self,requstHandler,msgData):
        pass


class MsgLinkController:
    """
    链接消息处理
    """


    def __init__(self):
        pass


    def reciveLinkMsg(self,requstHandler,msgData):
        pass


class MsgEventController:
    """
    事件消息处理
    """


    def __init__(self):
        pass


    def reciveEventMsg(self,requstHandler,msgData):

        # 消息类型
        msgType = msgData.find('MsgType').text
        # 公众账号
        toUserName = msgData.find('ToUserName').text
        # 来源用户名称
        fromUserName = msgData.find('FromUserName').text
        # 消创建时间
        createTime = msgData.find('CreateTime').text
        # 消息类型
        msgType = msgData.find('MsgType').text
        # 消息ID
        msgid = msgData.find('MsgId').text
        # 消息内容

        eventtype = msgData.find("Event").text
        if eventtype == "subscribe":
            log.info("订阅事件")
            # 订阅事件
            sendMsgContent = "欢迎关注竹韵科技\n"\
                             "1:我想你\n"\
                             "2:我恨你\n"\
                             "3:我烦你\n"\
                             "4:我爱你\n"\
                             "5:我不知道\n"\
                             "<a href='pyweb.coding.io'>访问主页</a>\n"

        elif eventtype == "unsubscribe":
            log.info("取消订阅事件")
            # 取消订阅事件
            sendMsgContent = "非常抱歉，您取消了对我的关注！"
        elif eventtype == "SCAN":
            log.info("打描事件")
            # 扫描订阅事件
            sendMsgContent = "欢迎关注竹韵科技—扫描\n"\
                             "1:我想你\n"\
                             "2:我恨你\n"\
                             "3:我烦你\n"\
                             "4:我爱你\n"\
                             "5:我不知道\n"\
                             "<a href='pyweb.coding.io'>访问主页</a>\n"

        elif eventtype == "LOCATION":
            # 上报地理位置事件
            pass
        elif eventtype == "CLICK":
            # 自定义菜单事件
            pass
        elif eventtype == "VIEW":
            # 点击菜单跳转链接事件
            pass

        sendMsgData = { "toUser":fromUserName,"fromUser":toUserName,"msgType":msgType,
                        "sendMsg":sendMsgContent }
        self.sendEventMsg(requstHandler,sendMsgData)


    def sendEventMsg(self,requstHandler,sendMsgData):
        sendXmlStr =\
            """<xml>
                <ToUserName><![CDATA[""" + sendMsgData["toUser"] + """]]></ToUserName>
                <FromUserName><![CDATA[""" + sendMsgData["fromUser"] + """]]></FromUserName>
                <CreateTime>""" + str(int(time.time())) + """</CreateTime>
                <MsgType><![CDATA[""" + sendMsgData["msgType"] + """]]></MsgType>
                <Content><![CDATA[""" + sendMsgData["sendMsg"] + """]]></Content>
                </xml>
            """

        # 设置返回消息头
        requstHandler.set_header("Content-type","text/xml; charset='UTF-8'")
        requstHandler.write(sendXmlStr)
        return True


__author__ = 'zhgk'
