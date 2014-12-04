# -*- coding: utf-8 -*-
import time


class MsgTextController:
    def __init__(self):
        pass


    def reciveTextMsg(self, requstHandler, msgData):
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

        # 根据消内容，确认回复消息
        # sendMsgConent = getSendMsg(content)
        sendMsgContent = "你在说什么？我又不认识你。。。"

        sendMsgData = {"toUser": fromUserName, "fromUser": toUserName, "msgType": msgType, "sendMsg": sendMsgContent}

        print("msg: %s" % content)

        sendMsgXML = self.sendTextMsg(sendMsgData)
        return sendMsgXML


    def sendTextMsg(self, requstHandler, sendMsgData):
        """
            发送文本消息
        """

        sendXmlStr = \
            """<xml>
                    <ToUserName><![CDATA[""" + sendMsgData["toUser"] + """]]></ToUserName>
                <FromUserName><![CDATA[""" + sendMsgData["fromUser"] + """]]></FromUserName>
                <CreateTime>""" + int(time.time()) + """</CreateTime>
                <MsgType><![CDATA[""" + sendMsgData["MsgType"] + """]]></MsgType>
                <Content><![CDATA[""" + sendMsgData["sendMsg"] + """]]></Content>
            </xml>
        ""

        """
        print(sendXmlStr)
        return sendXmlStr


__author__ = 'zhgk'
