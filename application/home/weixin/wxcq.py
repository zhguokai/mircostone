# -*- coding: utf-8 -*-
"""
微信抽签后台类
"""

from StringIO import StringIO

from PIL import ImageFont,ImageDraw,Image
from tornado.web import RequestHandler

from application.Logger import weixinLogger


wxLog = weixinLogger.getInstance().logging


class WxCq(RequestHandler):
    """
        处理图片生成与测试
    """


    def get(self):

        # 接收参数,参数个数为0的时候，直接返回页面,后期写一个单独的图片请求类
        args = self.request.arguments
        if len(args) > 0:
            #参数不为0,额外处理生成图片
            type = self.get_argument('type')
            userName = self.get_argument('userName')
            if type == "img":
                try:
                    font = ImageFont.truetype("application/static/fonts/simsun.ttc",88)
                    img = Image.open("application/static/img/qt2.png")
                    size = img.size
                    print(size)
                    draw = ImageDraw.Draw(img)
                    draw.text((200,20),userName,(123,55,99),font = font)
                    # img.save("application/static/img/jpeg.png",'PNG')
                    # imgbytes = img.tobytes()
                    #返回到前台
                    sio = StringIO()
                    img.save(sio,'PNG');
                    self.add_header("Content-type","image/png; charset='UTF-8'")
                    self.write(sio.getvalue())
                except Exception as e:
                    wxLog.info('失败了' + e.message)
                    self.write("失败了" + e.message)
        else:
            self.render('home/wxcq/wxcq.html')


    def post(self):
        """
        用于提交数据
        :return:
        """
        wxLog.info("转向结果页面")
        userName = self.get_argument('inputName').decode("utf8")
        self.render('home/wxcq/qcjg.html',userName = userName)


__author__ = 'zhgk'
