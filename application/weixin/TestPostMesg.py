# -*- coding: utf-8 -*-
import urllib.request
import urllib.request


data = """
<xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName>
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[this is a test]]></Content>
 <MsgId>1234567890123456</MsgId>
 </xml>
"""

req = urllib.request.Request("http://localhost:8080/AccessWeixin", data=data.encode(encoding='utf-8'), method='POST')

# "Content-type", "text/xml; charset=\"UTF-8\""
req.add_header("Content-type", "text/xml; charset='UTF-8'")
res = urllib.request.urlopen(req)

__author__ = 'zhgk'
