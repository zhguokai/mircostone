# -*- coding: utf-8 -*-
import logging
import datetime
import os


class weixinLogger:
    """
        日志类
    """
    __instance = None

    def __init__(self):
        """
            初始化日志
        """
        filepath = os.path.join(os.path.dirname(__file__))
        # 定义日志文件名称
        filename = filepath+"/../" + datetime.datetime.now().strftime('%Y-%m-%d') + ".log"
        # 定义日志显示格式
        formatter = logging.Formatter("%(asctime)s  - %(levelname)s - %(message)s")
        # 定义显示类型
        filehandler = logging.FileHandler(filename, mode='a', encoding='utf-8', delay=True)
        # 定义日志显示格式
        filehandler.setFormatter(formatter)
        # 创建日志类
        logg = logging.Logger("")
        # 设置日志显示级别
        logg.setLevel(logging.INFO)
        # 增加文件句柄
        logg.addHandler(filehandler)
        #
        self.logging = logg

    @staticmethod
    def getInstance():
        """
            单例模式返回
        """
        if weixinLogger.__instance is None:
            weixinLogger.__instance = weixinLogger()
        else:
            pass
        return weixinLogger.__instance


if __name__ == "__main__":
    wlog = weixinLogger.getInstance().logging
    wlog.info("hello %s" %wlog)

__author__ = 'zhgk'
