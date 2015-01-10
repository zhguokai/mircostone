# -*- coding: utf-8 -*-
__author__ = 'zhgk'

import unittest

from common.util.encode import EncodePass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        passstr = "system"
        newstr = EncodePass.encode_sha512(passstr)
        print(newstr)
        self.assertEqual(len(newstr) == 128, True)


if __name__ == '__main__':
    unittest.main()
