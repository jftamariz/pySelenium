import requests
import json
import sys
import os
import urllib


class Api:


	def __init__(self, **kwargs):
		self.host_domain = kwargs.get("domain")
		self.s = requests.Session()
		self.token = None


	def session(self):
		return self.s

	def encoder_uri(self, string2encode):
		return urllib.quote_plus(string2encode.encode('utf-8'), safe=',:')

	def set_token(self, token):
		self.token = token

	def get_index_php(self):
		route = "index.php"

		headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

		return self.s.get(self.host_domain+route, data=None, headers=headers)


	def post_add_to_cart(self, product_id, quantity=1):

		route = "index.php?rand=1547431807327"

		headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

		datapayload = "controller=cart&add=1&ajax=true&qty={0}&id_product={1}&token={2}".format(quantity, product_id, self.token)

		return self.s.post(self.host_domain+route, data=datapayload, headers=headers)

	def get_cart(self):
		route = "index.php?controller=order"

		headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

		return self.s.get( self.host_domain+route, data=None, headers=headers)
