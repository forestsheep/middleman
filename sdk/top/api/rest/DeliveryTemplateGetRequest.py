'''
Created by auto_sdk on 2016.11.11
'''
from top.api.base import RestApi
class DeliveryTemplateGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.template_ids = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.delivery.template.get'