'''
Created by auto_sdk on 2017.04.12
'''
from top.api.base import RestApi
class TmallInventoryQueryForstoreRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_list = None

	def getapiname(self):
		return 'tmall.inventory.query.forstore'
