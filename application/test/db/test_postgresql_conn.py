# -*- coding: utf-8 -*-
__author__ = 'zhgk'

import unittest

from application.db.connect.postgresql_conn import PostDBConn


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        初始化工作
        :return:
        """
        self.tclass = PostDBConn()


    def tearDown(self):
        """
        清理工作
        :return:
        """


    def test_get_conn(self):
        sqlstr = "CREATE TABLE public.qtest (id serial PRIMARY KEY, num integer, data varchar);"
        self.assertEqual(self.tclass.exec_sql(sqlstr) is None,True)


if __name__ == '__main__':
    unittest.main()
