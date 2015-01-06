# -*- coding: utf-8 -*-
import logging
import datetime
import os


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

        filepath = os.path.join(os.path.dirname(__file__))
        # 定义日志文件名称
        filename = filepath + "/../" + datetime.datetime.now().strftime('%Y-%m-%d') + ".log"
        # 定义日志显示格式
        formatter = logging.Formatter("%(asctime)s  - %(levelname)s - %(message)s")
        # 定义显示类型
        filehandler = logging.FileHandler(filename,mode = 'a',encoding = 'utf-8',delay = True)
        # 定义日志显示格式
        filehandler.setFormatter(formatter)
        # 创建日志类
        logg = logging.Logger("logger")
        # 设置日志显示级别
        logg.setLevel(logging.INFO)
        # 增加文件句柄
        logg.addHandler(filehandler)
        # 定义日志句柄
        self.__loghandle = logg


    @staticmethod
    def get_loghandle(classname):
        """
        单例形式返回日志句柄
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


if __name__ == "__main__":
    wlog = AppLogger.get_loghandle("AppLogger")
    wlog.info("hello %s" % wlog)
    elog = AppLogger.get_loghandle("AppLogger")
    elog.info("hello %s" % elog)
__author__ = 'zhgk'
