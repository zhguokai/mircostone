# -*- coding: utf-8 -*-
from datetime import datetime
from logging import Logger
from logging import Formatter
from logging import FileHandler
from logging import INFO

from common import logfile_path


class AppLogger(object):
    """
        日志类
    """

    # 定义SysLogger实例
    __instance = None

    def __init__(self):
        """
            初始化日志工具
        """

        # 定义日志文件名称
        filename = logfile_path + datetime.now().strftime('%Y-%m-%d') + ".log"
        # 定义日志显示格式
        formatter = Formatter("%(asctime)s  - %(levelname)s - %(message)s")
        # 定义显示类型
        filehandler = FileHandler(filename, mode='a', encoding='utf-8', delay=True)
        # 定义日志显示格式
        filehandler.setFormatter(formatter)
        # 创建日志类
        logg = Logger("logger")
        # 设置日志显示级别
        logg.setLevel(INFO)
        # 增加文件句柄
        logg.addHandler(filehandler)
        # 定义日志句柄
        self.__loghandle = logg

    @staticmethod
    def get_loghandle(classname):
        """
        单例形式返回日志句柄
        :rtype : object
        :return: logHandle
        """
        if AppLogger.__instance is None:
            # SysLogger未初始化时，进行初始化
            AppLogger.__instance = AppLogger()
            AppLogger.__instance.__loghandle.info(u"%s 获取初始日志句柄" % classname)
        else:
            # 如果已经初始化，则什么都不做
            AppLogger.__instance.__loghandle.info(u"%s 获取日志句柄" % classname)

        # 返回日志句柄
        return AppLogger.__instance.__loghandle


__author__ = 'zhgk'
