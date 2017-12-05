'''
Created by auto_sdk on 2016.12.23
'''
from top.api.base import RestApi
class UserAvatarGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None

	def getapiname(self):
		return 'taobao.user.avatar.get'
