# -*- coding: utf-8 -*- 
#数据库连接类
import sys
from pymongo import MongoClient
from pymongo import connection
from pymongo import collection

class dbCon:
    """
    数据库连接类
    """
    def __init__(self):
        #创建Client
        self.client = MongoClient(host= 'localhost', port=27017, max_pool_size= 100)
        self.db = self.client.bm
    def findObject(self, collectionName, key):
        """
        查询单条记录
        """
        result = self.db[collectionName].find_one(key)
        return result
    def closeClient(self):
        """
        关闭Client
        """
        self.client.close()


