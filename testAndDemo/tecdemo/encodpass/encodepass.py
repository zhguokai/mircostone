# -*- coding: utf-8 -*-
"""
测试密码加密算法，使用SHA512盐值加密
"""
from hashlib import sha512

sh = sha512()
sh.update("sysadmin".encode(encoding='utf8'))
print(sh.hexdigest())

__author__ = 'zhgk'
