'''
Created by auto_sdk on 2016.04.13
'''
from top.api.base import RestApi
class FenxiaoProductSkuDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_id = None
		self.properties = None

	def getapiname(self):
		return 'taobao.fenxiao.product.sku.delete'
