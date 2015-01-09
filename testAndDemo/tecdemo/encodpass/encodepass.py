# -*- coding: utf-8 -*-
"""
测试密码加密算法，使用SHA512盐值加密
"""
from Crypto.Hash import SHA512

sh = SHA512.new()
sh.update("sysadmin")
print(sh.hexdigest())

__author__ = 'zhgk'
