'''
Created by auto_sdk on 2017.07.03
'''
from top.api.base import RestApi
class ShopRemainshowcaseGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.shop.remainshowcase.get'
