# -*- coding: utf-8 -*-
import sys
import os

from tornado import options
from tornado.ioloop import IOLoop

from app.Application import MainApplication
from common.log.Logger import AppLogger



# 定义日志工具
rootLog = AppLogger.get_loghandle(__name__)
# 增加当前路径到项目中
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    rootLog.info(u"启动系统应用开始")
    options.parse_command_line()
    app = MainApplication().create_application()
    IOLoop.instance().start()
    rootLog.info(u"启动系统应用完成")
