#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/29 0029 17:53
# @File: base_api.py
# @Poject: Work_Project

import json
import base64
import requests
import hashlib
import logging
from ruamel import yaml
from jsonpath import jsonpath
from YouShuYun_API.utils.json_format import JsonData
from YouShuYun_API.utils.commlib import ReadTestYaml

class BaseApi():
	'''
	versed:
	jsonpath:
	load_yaml:
	send:
	sign:
	get_test_data:
	'''

	@classmethod
	# 封装对json数据（r），格式化输出
	def versed(cls, json_object):
		print(JsonData.format(json_object))

	@classmethod
	def jsonpath(cls, json_data, expr):
		return jsonpath(json_data, expr)

	@classmethod
	# 封装yaml文件读取的代码，通过路径直接读取yaml文件
	def load_yaml(cls, file_path):
		with open(file_path, 'r', encoding='utf-8') as f:
			return yaml.safe_load(f)

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
	# 封装MD5方式加密（请求参数排序后，拼接参数的value+盐），生成签名
	def sign(cls, body, appSecret="e9f0680f92d95ff9541e1eaff2cc18b6"):
		lists = []
		for k, v in sorted(body.items()):
			if k[1] != "" and k[0] != "sign":
				lists.append("".join(str(v)))
		# print(isinstance(body, Iterable))
		result = "".join(lists) + appSecret  # 拼接待签名字符串

		def jiamimd5(params):
			m = hashlib.md5()
			m.update(result.encode('UTF-8'))
			return m.hexdigest()

		sign = jiamimd5(result)  # 调用jiamimd5()加密生成签名，并赋值给变量"sign"
		body["sign"] = sign
		lists.clear()
		return body

	@classmethod
	# 封装获取yaml文件格式的，测试数据
	def get_test_data(cls, test_data_path):
		case = []  # 存储测试用例名称
		http = []  # 存储请对象
		expected = []  # 存储预期结果
		print(test_data_path)
		with open(test_data_path, 'r', encoding='utf-8') as f:
			dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
			test = dat['tests']
			for td in test:
				case.append(td.get('case', ''))
				http.append(td.get('http', {}))
				expected.append(td.get('expected', {}))
		paramesters = zip(case, http, expected)
		return case, paramesters

	@classmethod
	def get_token(cls):
		token = cls.load_yaml("F:\chenanming\Work_Project\YouShuYun_API\data\caches.yaml")
		return token['token']

# if __name__ == "__main__":
# 	body = {
#     "code": 1,
#     "msg": "成功！",
#     "data": {
#         "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdGVzdGFwaS5hZDY3NTUuY29tL3NhdmVfZGV2aWNlX2lkIiwiaWF0IjoxNjAzMzQzNDk2LCJleHAiOjE2MDM0Mjk4OTYsIm5iZiI6MTYwMzM0MzQ5NiwianRpIjoiMnhOZ2o2dm9SczJXWHdGWiIsInN1YiI6MTU1Mn0._1b-m6jUICFmvG4iS4MMymgaLZqzY_vffI6q60YhBLA",
#         "is_new": 0,
#         "exp": "2020-10-28 13:11:36"
#     }
# }
# 	token = BaseApi.jsonpath(body, '$.data.token')
# 	msg = BaseApi.jsonpath(body, '$.[msg]')
# 	print(token)
# 	print(msg)
# 	assert token != None
# 	assert msg == "成功！"