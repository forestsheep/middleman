'''
Created by auto_sdk on 2017.04.14
'''
from top.api.base import RestApi
class LocationRelationEditRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.location_relation_list = None

	def getapiname(self):
		return 'taobao.location.relation.edit'
