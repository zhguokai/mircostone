import tornado.options
from tornado.ioloop import IOLoop

from application.Application import MainApplication


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = MainApplication().createApplication()
    IOLoop.instance().start()
