# -*- coding: utf-8 -*-

class MsgTextController:
    def __init__(self):
        pass

    @staticmethod
    def reciveTextMsg(msgData):
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

        print("msg: %s" % content)

    def sendTextMsg(self,msgData):
        pass
__author__ = 'zhgk'
