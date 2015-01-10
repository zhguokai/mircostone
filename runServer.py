# -*- coding: utf-8 -*-
from tornado import options
from tornado.ioloop import IOLoop

from app.Application import MainApplication
from common.log.Logger import AppLogger



# 定义日志工具
rootLog = AppLogger.get_loghandle(__name__)

if __name__ == "__main__":
    rootLog.info(u"启动系统应用开始")
    options.parse_command_line()
    app = MainApplication().create_application()
    IOLoop.instance().start()
    rootLog.info(u"启动系统应用完成")
