#!/usr/bin/env python3

# An API Wrapper Library for boostack.

# Copyright 2022 GNU Public License v2

import subprocess,json,urllib.parse

class bookstack_api(object):
	tokenid=""
	tokensecret=""
	bookstack_host=""
	protocol="https"
	port=80
	def __init__(self,myhost="localhost",mytokenid="",mytokensecret=""):
		self.tokenid=mytokenid
		self.tokensecret=mytokensecret
		self.bookstack_host=myhost
	def set_token(self,mytokenid,mytokensecret):
		self.tokenid=mytokenid
		self.tokensecret=mytokensecret
	def get_token(self):
		return self.token+":"+self.tokensecret
	def set_bookstack_host(self,myhost):
		self.bookstack_host=myhost
	def get_bookstack_host(self):
		return self.bookstack_host
	def set_protocol(self,myprotocol):
		self.protocol=myprotocol
	def get_protocol(self):
		return self.protocol
	def set_port(self,myport):
		self.port=myport
	def get_port(self):
		return self.port
	def call_get_api(self,apicall):
		return json.loads((subprocess.getoutput("curl -sk --request GET --url "+self.protocol+"://"+self.bookstack_host+":"+str(self.port)+"/api/"+apicall+" --header 'Authorization: Token "+self.tokenid+":"+self.tokensecret+"'")))
	def call_post_api(self,apicall,parameters):
		curlcommand="curl -sk --request POST --url '"+self.protocol+"://"+self.bookstack_host+":"+str(self.port)+"/api/"+apicall+"?"
		for param in parameters:
			#print(param)
			curlcommand=curlcommand+urllib.parse.quote(param)+"="+urllib.parse.quote(parameters[param])+"&"
		curlcommand=curlcommand.rstrip("&")+"'"
		curlcommand=curlcommand+" --header 'Authorization: Token "+self.tokenid+":"+self.tokensecret+"'"
		#print(curlcommand)
		x=subprocess.getoutput(curlcommand)
		#print(x)
		try:
			return json.loads(x)
		except:
			return "Too big"
	def call_post_json_api(self,apicall,jsonfile):
		#return json.loads(subprocess.getoutput
		print("curl -sk --request POST --url '"+self.protocol+"://"+self.bookstack_host+":"+str(self.port)+"/api/"+apicall+"' -H 'Content-Type:application/json' --data "+'"$(cat '+jsonfile+')"'+" --header 'Authorization: Token "+self.tokenid+":"+self.tokensecret+"'")


