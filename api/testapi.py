#coding:UTF-8
import web

class TestApi:
    def __init__(self):
        pass

    def GET(self):
        data = web.input()
        return str(data)

    def POST(self):
        jsonString = web.data()
        rtnString = 'normal'
        try:
            rtnString = "我收到了测试消息"
        except Exception as err:
            rtnString = err.toString()
        return rtnString