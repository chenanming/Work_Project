#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/29 0029 17:53
# @File: base_api.py
# @Poject: Work_Project

import json
import base64
import hashlib
import requests
from unit.json_format import JsonData
from YouShuYun_API.utils.utils import Utils

class BaseApi:
	@classmethod
	def versed(cls, json_object):
		print(JsonData.format(json_object ))  # 使用Utils的format()方法对json数据（r），格式化输出

	json_data = None
	def jsonpath(self, expr):
		return Utils.jsonpath(self.json_data, expr)

	def send(self, data: dict):
		if "http" == data["schema"]:
			res = requests.request(data["method"], data["url"], header=data["headers"])
			return json.loads(base64.decode(res.content))
		elif "dubbo" == data["schema"]:
			pass
		elif "websocket" == data["schema"]:
			pass
		else:
			pass

	'''MD5() 加密请求参数，生成签名'''
	@classmethod
	def sign_body(cls, body, appkey="e9f0680f92d95ff9541e1eaff2cc18b6"):
		def jiamimd5(params):
			m = hashlib.md5()
			m.update(result.encode('UTF-8'))
			return m.hexdigest()

		list = []
		for k, v in sorted(body.items()):
			if k[1] != "" and k[0] != "sign":
				list.append("".join(v))
		sort = "".join(list)  # 拼接待签名字符串
		result = sort+appkey
		sign = jiamimd5(result)  # 调用jiamimd5()加密生成签名，并赋值给变量"sign"
		body["sign"] = sign
		return body

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
# 	print(BaseApi.sign_body(body))