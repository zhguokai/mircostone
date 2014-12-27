# -*- coding: utf-8 -*-
"""
连接postgresql
"""
import psycopg2

class PostDBConn():
    """
    数据库连接类
    """


    def __init__(self):
        """

        :return:
        """
        self.__conn = None;


    def __get_conn(self):
        if self.__conn is None:
            self.__conn = psycopg2.connect(database = "d44e28e299c3c4ae586ba5ee5bfcf8074",user = "uf619779d781d4780951f9a29d402290e",password = "p6ac01e007de04894a048edb11dfd5a29",host = "10.9.27.243",
                                           port = 5435)
        else:
            pass
        return self.__conn


    def __get_cursor(self):
        """
        获取游标
        :return:
        """

        return ""


    def exec_sql(self,sqlstr):
        """
       执行SQL
       :param sqlstr:
       :return:
       """
        conn = self.__get_conn()
        cursor = conn.cursor()
        # cursor = self.__get_cursor()
        result = cursor.execute(sqlstr)
        conn.commit()
        return result


if __name__ == "__main__":
    conn = PostDBConn()
    sqlstr = "CREATE TABLE public.Q2test (id serial PRIMARY KEY, num integer, data varchar);"
    result = conn.exec_sql(sqlstr)
__author__ = 'zhgk'
