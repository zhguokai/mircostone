# -*- coding: utf-8 -*-

import hashlib
import xml.etree.ElementTree as Etr

#

from tornado.web import RequestHandler

from application.weixin.msgTextController import MsgTextController


class AccessWeixinHandler(RequestHandler):
    def get(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        echostr = self.get_argument("echostr")
        
        # print("weixin: %s : %s : %s" %signature %timestamp% nonce)

        token = "zgkAndHxh"
        listWeixin = [token, timestamp, nonce]
        listWeixin.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, listWeixin)
        hashcode = sha1.hexdigest()
        
        if hashcode == signature:
            self.write(echostr)
        else:
            self.write('False')
    
    def post(self):
        """
        接收用户请求
        :return:
        """""
        # 消息体
        msgXml = self.request.body.decode(encoding='utf-8')
        # 转换为XMLData
        msgData = Etr.fromstring(msgXml)

        # 处理消息数据
        try:

            msgType = msgData.find('MsgType').text
            if msgType == "text":
                #调用文本消息处理
               msgControl = MsgTextController()
               sendMsg = msgControl.reciveTextMsg(msgData)
               print(sendMsg)
               self.set_header("Content-type", "text/xml; charset='UTF-8'")
               print("GGGGGGGGGGGGGGGGGGGGGG")
               self.write(sendMsg)

        except AttributeError as ae:
            print(ae)


__author__ = 'zhgk'
