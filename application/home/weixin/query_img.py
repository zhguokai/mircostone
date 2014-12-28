# -*- coding: utf-8 -*-
"""

"""
from StringIO import StringIO

from tornado.web import RequestHandler
from PIL import Image,ImageFont,ImageDraw

from application.Logger import weixinLogger

imglog = weixinLogger.getInstance().logging


class QueryImgHandler(RequestHandler):
    """
    图片处理类
    """
    def get(self):
        """
        获取图片方法,用于Ajax
        :return:
        """
        arguments = self.request.arguments
        if len(arguments) > 0 and self.get_argument("type") is not None:
            # 参数不为0,额外处理生成图片
            type = self.get_argument('type')
            userName = self.get_argument('userName')
            if type == "img":
                try:
                    font = ImageFont.truetype("application/static/fonts/simsun.ttc",88)
                    img = Image.open("application/static/img/qt2.png")
                    size = img.size
                    print(size)
                    draw = ImageDraw.Draw(img)
                    draw.text((300,30),userName,(123,55,99),font = font)
                    # img.save("application/static/img/jpeg.png",'PNG')
                    # imgbytes = img.tobytes()
                    # 返回到前台
                    sio = StringIO()
                    img.save(sio,'PNG');
                    self.add_header("Content-type","image/png; charset='UTF-8'")
                    self.write(sio.getvalue())
                except Exception as e:
                    imglog.info('失败了' + e.message)
                    self.write("失败了" + e.message)


__author__ = 'zhgk'
