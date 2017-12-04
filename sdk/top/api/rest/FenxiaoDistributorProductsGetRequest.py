'''
Created by auto_sdk on 2017.03.06
'''
from top.api.base import RestApi
class FenxiaoDistributorProductsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.fields = None
		self.item_ids = None
		self.page_no = None
		self.page_size = None
		self.pids = None
		self.productcat_id = None
		self.start_time = None
		self.supplier_nick = None

	def getapiname(self):
		return 'taobao.fenxiao.distributor.products.get'
