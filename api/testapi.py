# coding:UTF-8
import web
import top.api
import json
from base import logg
import pictureget


class TestApi:
    def __init__(self):
        pass

    def GET(self):
        data = web.input()
        logg.info(data)
        return pictureget.getpic()
        # req = top.api.PictureGetRequest("gw.api.taobao.com")
        # req.set_app_info(top.appinfo("12527264", "2d62590fed388a69f21da953b3673f36"))
        # req.picture_id = 1412906172843645057
        # try:
        #     resp = req.getResponse("610050136148375340f32d627cbd0ef51692cd8097a66e7445674129")
        #     rtnjson = json.dumps(resp, ensure_ascii=False, indent=4)
        #     return rtnjson
        # except Exception, e:
        #     print e
        #     print type(e)

        # req = top.api.PictureUploadRequest("gw.api.taobao.com")
        # req.set_app_info(top.appinfo("12527264", "2d62590fed388a69f21da953b3673f36"))

        # req.picture_category_id = 1412916179972488430
        # req.img = top.api.FileItem('p1.png', open('p1.png'))
        # req.image_input_title = "t1"
        # req.title = "mypic"
        # # req.picture_id = 10000
        # req.client_type = "client:computer"
        # req.is_https = "true"
        # try:
        #     resp = req.getResponse("610050136148375340f32d627cbd0ef51692cd8097a66e7445674129")
        #     print resp
        # except Exception, e:
        #     print type(e)
        #     print e
        # pass


    def POST(self):
        jsonString = web.data()
        rtnString = 'normal'
        try:
            rtnString = "我收到了测试消息"
        except Exception as err:
            rtnString = err.toString()
        return rtnString