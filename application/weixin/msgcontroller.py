# -*- coding: utf-8 -*-
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from application.Logger import weixinLogger
from application.weixin.userinfo import UserInfo
from application.weixin.WxConfig import WeiXinConfig

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


    def recive_text_msg(self,requesthandler,msg_data):
        """
            处理文本消息
        :param msg_data:
        :return:
        """
        # 消息类型
        msg_type = msg_data.find('MsgType').text
        # 公众账号
        to_user_name = msg_data.find('ToUserName').text
        # 来源用户名称
        from_user_name = msg_data.find('FromUserName').text
        # 消创建时间
        # create_time = msg_data.find('CreateTime').text

        # 消息内容
        msg_content = msg_data.find('Content').text
        log.info("存储消息：%s" % msg_content)
        log.info("用户：%s" % from_user_name)

        user = UserInfo.get_userinfo_openid(from_user_name)

        log.info("用户 %s 发来了消息: %s" % (user["nickname"],msg_content))

        """
        根据content去数据库中查询要回复的内容，如果存在，将查询的信息直接回复
        否则回复:你在说什么
        """


        # 根据消内容，确认回复消息
        if msg_content == "1":
            send_msg_content = "老婆：我想你了"
        elif msg_content == "2":
            send_msg_content = "老婆：我恨你不理我"
        elif msg_content == "3":
            send_msg_content = "老婆：我错了，不要烦弃俺"
        elif msg_content == "4":
            send_msg_content = "老婆：我爱你哟"
        elif msg_content == "5":
            send_msg_content = "老婆：我真的不知道ing"
        elif msg_content == "6":
            url = WeiXinConfig.APP_BASE_URL + "wxcq"
            send_msg_content = "<a href='" + url + "'>算一挂</a>"
        else:
            send_msg_content = "你在说什么？我听不懂ing...\n"\
                               "1:我想你\n"\
                               "2:我恨你\n"\
                               "3:我烦你\n"\
                               "4:我爱你\n"\
                               "5:我不知道\n"\
                               "<a href='pyweb.coding.io'>参观一下吧</a>\n"
        # sendMsgConent = getSendMsg(content)


        sendmsg_data = { "toUser":from_user_name,"fromUser":to_user_name,"msgType":msg_type,
                         "sendMsg":send_msg_content }


        # 调用回复文本消息方法
        self.send_text_msg(requesthandler,sendmsg_data)
        return True


    def send_text_msg(self,requesthandler,sendmsg_data):
        """
            发送文本消息
        """

        send_xml_str =\
            """<xml>
                    <ToUserName><![CDATA[""" + sendmsg_data["toUser"] + """]]></ToUserName>
                <FromUserName><![CDATA[""" + sendmsg_data["fromUser"] + """]]></FromUserName>
                <CreateTime>""" + str(int(time.time())) + """</CreateTime>
                <MsgType><![CDATA[""" + sendmsg_data["msgType"] + """]]></MsgType>
                <Content><![CDATA[""" + sendmsg_data["sendMsg"] + """]]></Content>
                </xml>
            """

        # 设置返回消息头
        requesthandler.set_header("Content-type","text/xml; charset='UTF-8'")
        requesthandler.write(send_xml_str)
        return True


class MsgImgController:
    """
    图片消息处理
    """


    def __init__(self):
        pass


    def reciveImgMsg(self,requesthandler,msg_data):
        """
        处理图片消息
        :param requesthandler:
        :param msg_data:
        :return:
        """
        pass


class MsgVoiceController:
    """
    声音消息处理
    """


    def __init__(self):
        pass


    def reciveVoiceMsg(self,requesthandler,msg_data):
        pass


class MsgVideoController:
    """
    视频消息处理
    """


    def __init__(self):
        pass


    def reciveVideoMsg(self,requesthandler,msg_data):
        pass


class MsgLocationController:
    """
    位置消息处理
    """


    def __init__(self):
        pass


    def reciveLocationMsg(self,requesthandler,msg_data):
        pass


class MsgLinkController:
    """
    链接消息处理
    """


    def __init__(self):
        pass


    def reciveLinkMsg(self,requesthandler,msg_data):
        pass


class MsgEventController:
    """
    事件消息处理
    """


    def __init__(self):
        pass


    def recive_event_msg(self,requesthandler,msg_data):

        log.info("开始解析接收者")
        # 公众账号
        to_user_name = msg_data.find('ToUserName').text
        log.info("开始解析发送者")
        # 来源用户名称
        from_user_name = msg_data.find('FromUserName').text
        # 消创建时间
        log.info("开始解析创建时间")
        #create_time = msg_data.find('CreateTime').text
        # 消息类型
        log.info("开始解析消息类型")
        msg_type = msg_data.find('MsgType').text
        # 消息ID
        # log.info("开始解析消息ID ")
        # msgid = msg_data.find('MsgId').text
        # 消息内容
        log.info("开始解析事件内容")
        eventtype = msg_data.find("Event").text
        # 定义返回消息变量
        send_msg_content = ""
        if eventtype == "subscribe":
            log.info("订阅事件")
            # 订阅事件
            send_msg_content = "欢迎关注竹韵科技\n"\
                               "1:我想你\n"\
                               "2:我恨你\n"\
                               "3:我烦你\n"\
                               "4:我爱你\n"\
                               "5:我不知道\n"\
                               "<a href='pyweb.coding.io'>访问主页</a>\n"

        elif eventtype == "unsubscribe":
            log.info("取消订阅事件")
            # 取消订阅事件
            send_msg_content = "非常抱歉，您取消了对我的关注！"
        elif eventtype == "SCAN":
            log.info("打描事件")
            # 扫描订阅事件
            send_msg_content = "欢迎关注竹韵科技—扫描\n"\
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

        sendmsg_data = { "toUser":from_user_name,"fromUser":to_user_name,"msgType":msg_type,
                         "sendMsg":send_msg_content }
        self.send_event_msg(requesthandler,sendmsg_data)


    def send_event_msg(self,requesthandler,sendmsg_data):
        send_xml_str =\
            """<xml>
                <ToUserName><![CDATA[""" + sendmsg_data["toUser"] + """]]></ToUserName>
                <FromUserName><![CDATA[""" + sendmsg_data["fromUser"] + """]]></FromUserName>
                <CreateTime>""" + str(int(time.time())) + """</CreateTime>
                <MsgType><![CDATA[""" + sendmsg_data["msgType"] + """]]></MsgType>
                <Content><![CDATA[""" + sendmsg_data["sendMsg"] + """]]></Content>
                </xml>
            """

        # 设置返回消息头
        log.info("发送订阅消息:"+send_xml_str)
        requesthandler.set_header("Content-type","text/xml; charset='UTF-8'")
        requesthandler.write(send_xml_str)
        return True


__author__ = 'zhgk'
