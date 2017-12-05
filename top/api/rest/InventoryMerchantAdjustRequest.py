'''
Created by auto_sdk on 2017.04.18
'''
from top.api.base import RestApi
class InventoryMerchantAdjustRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.inventory_check = None

	def getapiname(self):
		return 'taobao.inventory.merchant.adjust'
