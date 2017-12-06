# coding: UTF-8

import web
from base import logg
from api.testapi import TestApi


urls = (
    '/index', 'Index',
    '/testapi', 'TestApi'
)


class Index:
    def __init__(self):
        pass

    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    logg.init()
    app = web.application(urls, globals())
    app.run()
