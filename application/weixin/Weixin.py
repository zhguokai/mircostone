# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
import xml.etree.ElementTree as Etr

#

from tornado.web import RequestHandler
# 引入自定义包
from application.Logger import weixinLogger
from application.weixin.msgcontroller import MsgTextController
from application.weixin.msgcontroller import MsgImgController
from application.weixin.msgcontroller import MsgVoiceController
from application.weixin.msgcontroller import MsgVideoController
from application.weixin.msgcontroller import MsgLinkController
from application.weixin.msgcontroller import MsgLocationController
from application.weixin.msgcontroller import MsgEventController


# 定义日志工具
log = weixinLogger.getInstance().logging


class AccessWeixinHandler(RequestHandler):
    """
    微信处理类
    """


    def get(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        echostr = self.get_argument("echostr")
        
        # print("weixin: %s : %s : %s" %signature %timestamp% nonce)

        token = "zgkAndHxh"
        list_wei_xin = [token,timestamp,nonce]
        list_wei_xin.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list_wei_xin)
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
        msgxml = self.request.body.decode(encoding = 'utf-8')
        log.info("接收消息体： %s" % msgxml)
        # 转换为XMLData
        msg_data = Etr.fromstring(msgxml)

        # 处理消息数据
        try:
            msgtype = msg_data.find('MsgType').text
            log.info("消息类型：%s" % msgtype)
            if msgtype == "text":
                # 调用文本消息处理
                msgcontrol = MsgTextController()
                msgcontrol.recive_text_msg(self,msg_data)
            elif msgtype == "image":
                # 处理图片
                msgcontrol = MsgImgController()
                msgcontrol.reciveImgMsg(self,msg_data)
                pass
            elif msgtype == "voice":
                # 声音消息
                msgcontrol = MsgVoiceController()
                msgcontrol.reciveVoiceMsg(self,msg_data)
                pass
            elif msgtype == "video":
                # 视图
                msgcontrol = MsgVideoController()
                msgcontrol.reciveVideoMsg(self,msg_data)
                pass
            elif msgtype == "location":
                # 地理位置
                msgcontrol = MsgLocationController()
                msgcontrol.reciveLocationMsg(self,msg_data)
                pass
            elif msgtype == "link":
                # 链接
                msgcontrol = MsgLinkController()
                msgcontrol.reciveLinkMsg(self,msg_data)
                pass
            elif msgtype == "event":
                log.info("事件类型处理")
                # 处理事件
                msgcontrol = MsgEventController()
                msgcontrol.recive_event_msg(self,msg_data)
        except BaseException as e:
            log.error("出现异常：%s" % e)


__author__ = 'zhgk'
