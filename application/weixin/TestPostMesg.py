# -*- coding: utf-8 -*-
import urllib2



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

req = urllib2.Request("http://localhost:8080/AccessWeixin", data=data.encode(encoding='utf-8'))
req.add_header("Content-type", "text/xml; charset='UTF-8'")
res = urllib2.urlopen(req)
print(res)
__author__ = 'zhgk'
