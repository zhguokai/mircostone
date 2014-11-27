# -*- coding: utf-8 -*-

import hashlib

from tornado.web import RequestHandler


class AccessWeixinHandler(RequestHandler):
    def get(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        echostr = self.get_argument("echostr")

        #print("weixin: %s : %s : %s" %signature %timestamp% nonce)
        print("dddddddddddddd")
        token = "zgkAndHxh"

        listWeixin = list[token, timestamp, nonce]
        listWeixin.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, listWeixin)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return False


__author__ = 'zhgk'
