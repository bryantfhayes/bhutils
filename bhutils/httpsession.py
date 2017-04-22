# -*- coding: utf-8 -*-
# @Author: bryanthayes
# @Date:   2017-04-20 22:35:56
# @Last Modified by:   bryanthayes
# @Last Modified time: 2017-04-20 22:56:55
import sys, requests, json

# TODO(bhayes): Add support for PUT, DELETE, UPDATE requests
class HTTPSession(object):
	def __init__(self):
		self.session = requests.Session()

	def __del__(self):
		self.session.close()

	def POST(self, root, path, data, headers=None):
		''' Issue a POST http web request given a path and data for args '''
		
		# Load headers if applicable
		if (headers == None):
			headers = {"content-type" : "application/json"}
		else:
			headers = headers

		try:
			url = root + path
			result = self.session.post(url, data=data, headers=headers).json()
			return result
		except requests.exceptions.RequestException as e:
			raise(e)

	def GET(self, root, path, data):
		''' Issue a GET http web request given a path and data payload '''
		try:
			url = root + path
			result = self.session.get(url, data=data).json()
			return result
		except requests.exceptions.RequestException as e:
			raise(e)