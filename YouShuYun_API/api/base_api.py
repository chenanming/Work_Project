#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/29 0029 17:53
# @File: base_api.py
# @Poject: Work_Project

import json
import base64
import requests
from YouShuYun_API.utils.json_format import JsonData
from YouShuYun_API.utils.create_sign import JiaMi

class BaseApi:

	@classmethod
	def versed(cls, json_object):
		print(JsonData.format(json_object))  # 使用Utils的format()方法对json数据（r），格式化输出

	json_data = None
	def jsonpath(cls, expr):
		return JsonData.jsonpath(cls.json_data, expr)

	def send(self, req: dict):
		if "http" == req["schema"]:
			res = requests.request(req["method"], req["url"], header=req["headers"])
			return json.loads(base64.decode(res.content))
		elif "dubbo" == req["schema"]:
			pass
		elif "websocket" == req["schema"]:
			pass
		else:
			pass

	@classmethod
	def sign(cls, body):
		return JiaMi.sign_body(body)

# if __name__ == "__main__":
# 	body = {
# 		"app_type": "32",  # 悠书云小说：32  言湘书城：34
# 		"deviceCode": "221964b5488ab8b48cea68e54cb996a9",
# 		"Uid": "5d20dfe6dc75c465",
# 		"market_name": "kuaiyingyong",
# 		"key": "",
# 		"mobile": "MI 6",
# 		"sign": ""
# 	}
# 	print(BaseApi.sign(body))