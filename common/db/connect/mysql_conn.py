# -*- coding: utf-8 -*-
"""
mysql数据库连接类
用于测试数据连接
"""
from pymysql import connect

from common.log.Logger import AppLogger
from common.db.dbconfig import MysqlConfig


dblog = AppLogger.get_loghandle(__name__)


class MySqlDBConn(object):
    """
    处理Mysql连接
    """

    __instance = None

    def __init__(self):
        """
        初始化方法
        :return:
        """
        self.__setttings = {
            "user": MysqlConfig.MYSQL_USER,
            "password": MysqlConfig.MYSQL_PASS,
            "host": MysqlConfig.MYSQL_HOST,
            "port": MysqlConfig.MYSQL_PORT,
            "database": MysqlConfig.MYSQL_DBNAME,
        }
        self.__con = self.__get_conn()

    def __get_conn(self):
        """
        获取连接
        :return:
        """
        con = None
        try:
            con = connect(**self.__setttings)
            dblog.info(u"获取数据库连接")
        except BaseException as e:
            dblog.error(u"数据库连接获取失败:错误码： %s 错误消息：%s " % e.args)
        return con

    @staticmethod
    def execute_query_sql(query_sql_str, query_params):
        """
        执行查询方法
        :param sqlstr:
        :return:
        """
        try:
            dblog.info(u"执行SQL: %s" % query_sql_str)
            conn = MySqlDBConn.get_exechandle()
            up_cursor = conn.cursor()
            up_cursor.execute(query_sql_str, query_params)
            query_result = up_cursor._result
            return query_result
        except BaseException as e:
            dblog.error(u"查询数据库异常： %s" % e.args[0])
            return None

    @staticmethod
    def execute_update_sql(update_sql):
        """
        执行更新SQL
        :param update_sql:
        :return:执行结果
        """

        try:
            dblog.info(u"执行SQL: %s" % update_sql)
            conn = MySqlDBConn.get_exechandle()
            up_cursor = conn.cursor(buffered=True)
            up_cursor.execute(update_sql)
            conn.commit()
            up_cursor.close()
            return True
        except BaseException as e:
            dblog.error(u"操作数据库异常： %s" % e.args[0])
            return False

    @staticmethod
    def get_exechandle():
        if MySqlDBConn.__instance is None:
            MySqlDBConn.__instance = MySqlDBConn()

        elif MySqlDBConn.__instance.__con is None:
            MySqlDBConn.__instance = MySqlDBConn()
        else:
            """
            """
        return MySqlDBConn.__instance.__con


__author__ = 'zhgk'
