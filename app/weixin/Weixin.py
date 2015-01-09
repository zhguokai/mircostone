# -*- coding: utf-8 -*-
import hashlib
import xml.etree.ElementTree as Etr

#

from tornado.web import RequestHandler
# 引入自定义包
from common.log.Logger import AppLogger
from app.weixin.msgcontroller import MsgTextController
from app.weixin.msgcontroller import MsgImgController
from app.weixin.msgcontroller import MsgVoiceController
from app.weixin.msgcontroller import MsgVideoController
from app.weixin.msgcontroller import MsgLinkController
from app.weixin.msgcontroller import MsgLocationController
from app.weixin.msgcontroller import MsgEventController


# 定义日志工具
acelog = AppLogger.get_loghandle(__name__)


class AccessWeixinHandler(RequestHandler):
    """
    微信处理类
    """


    def data_received(self, chunk):
        """
        暂不做操作
        :param chunk:
        :return:
        """


    def get(self):
        acelog.info(u"接收微信请求认证")
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        echostr = self.get_argument("echostr")

        # print("weixin: %s : %s : %s" %signature %timestamp% nonce)

        token = "zgkAndHxh"
        list_wei_xin = [token, timestamp, nonce]
        list_wei_xin.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list_wei_xin)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            self.write(echostr)
            acelog.info(u"微信认证成功")
        else:
            self.write('False')
            acelog.info(u"微信认证失败")


    def post(self):
        """
        接收用户请求
        :return:
        """""

        # 消息体
        msgxml = self.request.body.decode(encoding='utf-8')
        acelog.info("接收消息体： %s" % msgxml)
        # 转换为XMLData
        msg_data = Etr.fromstring(msgxml)

        # 处理消息数据
        try:
            msgtype = msg_data.find('MsgType').text
            acelog.info("消息类型：%s" % msgtype)
            if msgtype == "text":
                # 调用文本消息处理
                msgcontrol = MsgTextController()
                msgcontrol.recive_text_msg(self, msg_data)
            elif msgtype == "image":
                # 处理图片
                msgcontrol = MsgImgController()
                msgcontrol.reciveImgMsg(self, msg_data)
                pass
            elif msgtype == "voice":
                # 声音消息
                msgcontrol = MsgVoiceController()
                msgcontrol.reciveVoiceMsg(self, msg_data)
                pass
            elif msgtype == "video":
                # 视图
                msgcontrol = MsgVideoController()
                msgcontrol.reciveVideoMsg(self, msg_data)
                pass
            elif msgtype == "location":
                # 地理位置
                msgcontrol = MsgLocationController()
                msgcontrol.reciveLocationMsg(self, msg_data)
                pass
            elif msgtype == "link":
                # 链接
                msgcontrol = MsgLinkController()
                msgcontrol.reciveLinkMsg(self, msg_data)
                pass
            elif msgtype == "event":
                acelog.info("事件类型处理")
                # 处理事件
                msgcontrol = MsgEventController()
                msgcontrol.recive_event_msg(self, msg_data)
        except BaseException as e:
            acelog.error("出现异常：%s" % e)


__author__ = 'zhgk'
