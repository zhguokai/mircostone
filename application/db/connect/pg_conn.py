# -*- coding: utf-8 -*-
"""
PostGreSQL数据库的连接类
"""

import psycopg2

from application.db import dbconfig
from application.Logger import AppLogger

dblog = AppLogger.get_loghandle(__name__)
class PgDBConn:
    """
    postgresql的连接类
    """


    def __init__(self):
        """
        初始化方法,定义私有变量
        :return:
        """
        self.__dbhost = dbconfig.POSTGRESQL_DB_HOST
        self.__dbport = dbconfig.POSTGRESQL_DB_PORT
        self.__dbname = dbconfig.POSTGRESQL_DB_NAME
        self.__dbuser = dbconfig.POSTGRESQL_DB_USER
        self.__dbpass = dbconfig.POSTGRESQL_DB_PASS
        self.__conn = None


    def __create_conn(self):
        """
        取得数据库连接
        :return:
        """
        try:
            self.__conn = psycopg2.connect(database = self.__dbname,user = self.__dbuser,
                              password = self.__dbpass,host = self.__dbhost,port = self.__dbport)
            return self.__conn
        except Exception as E:
            log.error(e)


__author__ = 'zhgk'
