# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import main

from testAndDemo.tecdemo.db.mysql_conn import MySqlDBConn


class MyTestCase(TestCase):
    def test_something(self):
        qqstr = """
            SELECT * FROM b_wx_users WHERE user_code = %s;
        """
        params = ("sysadmin",)
        rest = MySqlDBConn.execute_query_sql(qqstr, params)
        print(rest)
        self.assertEqual(rest is True, True)


if __name__ == '__main__':
    main()

__author__ = 'zhgk'
