'''
Created by auto_sdk on 2014.09.09
'''
from top.api.base import RestApi
class MaPackcodeCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.ma.packcode.create'
