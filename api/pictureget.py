# coding: UTF-8
import json
import top.api
from base import logg


def getpic():
    req = top.api.PictureGetRequest("gw.api.taobao.com")
    req.set_app_info(top.appinfo("12527264", "2d62590fed388a69f21da953b3673f36"))
    req.picture_id = 1412906172843645057
    try:
        resp = req.getResponse("610050136148375340f32d627cbd0ef51692cd8097a66e7445674129")
        rtnjson = json.dumps(resp, ensure_ascii=False, indent=4)
        logg.info_response(rtnjson)
        return rtnjson
    except Exception, e:
        print e
        print type(e)
    pass
