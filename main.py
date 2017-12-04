# coding: UTF-8

import web
from api.testapi import TestApi

urls = (
    '/index', 'index',
    '/testapi', 'TestApi'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
