# -*- coding: utf-8 -*-
__author__ = 'zhgk'

import unittest

from application.TestAndDemo.demo.db.mysql_conn import MySqlDBConn


class MyTestCase(unittest.TestCase):
    def test_something(self):
        str = """
        INSERT INTO `mircostone`.`b_wx_users` (`user_id`, `user_code`, `user_name`, `user_pass`,
        `user_email`, `user_phone`, `user_type`, `user_address`) VALUES ('1', 'wetert', 'sdgdg',
         'sdg', 'sdg', 'sdg', 'sdg', 'sdg');

        """
        rest = MySqlDBConn.execute_update_sql(str)
        print(rest)
        self.assertEqual(rest is True, True)


if __name__ == '__main__':
    unittest.main()
