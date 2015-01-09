# -*- coding: utf-8 -*-
"""
密码加密算法，使用SHA512盐值加密
"""
from Crypto.Hash import SHA512


class EncodePass(object):
    """
    对密码进行加密
    """

    def __init__(self):
        """
        初始化
        :return:
        """

    @staticmethod
    def encode_sha512(source_str):
        """
        对传入的字符串加密
        :param source_str:要加密的字符串
        :return target_str:加密后的字符串
        """
        sha512 = SHA512.new()
        sha512.update(source_str)
        target_str = sha512.hexdigest()
        return target_str


__author__ = 'zhgk'
