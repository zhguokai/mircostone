# -*- coding: utf-8 -*-
"""
数据库连接配置类
"""


class MysqlConfig(object):
    """
        数据库配置信息
    """
    # IP等地址未替换
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_DBNAME = "mircostone"
    MYSQL_USER = "root"
    MYSQL_PASS = "123456"
    MYSQL_MIN_CON = 10
    MYSQL_MAX_CON = 50
    MYSQL_CHAR_SET = "utf8"
    MYSQL_COLLECTION = "utf8_general_ci"


__author__ = 'zhgk'
