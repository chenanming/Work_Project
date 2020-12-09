#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/29 0029 17:53
# @File: base_api.py
# @Poject: Work_Project

import os
import re
import json
import hashlib
import base64
import requests
from ruamel import yaml
from jsonpath import jsonpath
from YouShuYun_API.utils.json_format import JsonData
from YouShuYun_API.utils.logger import log
from YouShuYun_API.utils.variable import is_vars

class BaseApi():
	'''
	versed:
	'''
	Base_Path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


	@classmethod
	def versed(cls, json_object):
		"""
		封装对json数据（r），格式化输出
		"""
		print(JsonData.format(json_object))

	@classmethod
	def jsonpath(cls, json_data, expr):
		return jsonpath(json_data, expr)

	@classmethod
	def load_yaml(cls, file_path, sub=None):
		"""
		封装yaml文件读取的代码，通过路径直接读取yaml文件
		"""
		file_path = os.path.join(cls.Base_Path, file_path)
		with open(file_path, 'r', encoding='utf-8') as f:
			if sub is None:
				return yaml.safe_load(f)
			else:
				return yaml.safe_load(f)[sub]

	@classmethod
	def sign(cls, body, appSecret="e9f0680f92d95ff9541e1eaff2cc18b6"):
		"""
		封装MD5方式加密（请求参数排序后，拼接参数的value+盐），生成签名
		:param body: 请求参数
		:param appSecret: 盐
		:return:
		"""
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
	def get_test_data(cls, test_data_path):
		"""封装获取yaml文件格式的，测试数据
		"""
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
	def setEnvironmentVariable(cls, parameters, res):
		"""
		提取，并设置全局的环境变量
		:param parameters: yaml文件中，需要提取成变量的所有参数
		:param res: API响应数据
		:return: 环境变量集合>>>dict
		"""
		tmp = {}
		for k, v in parameters.items():
			if k == "extract":
				for k, v in v.items():  # 1>>content.data.token
					tmp[k] = v
			else:
				pass

		for k, v in tmp.items():
			lists = v.split(".")[1:]  # 1>>data.token
			con = res.json()
			for i in lists:
				con = con[i]
			is_vars.set(k, con)

	@classmethod
	def regexps(cls, parameters):
		"""
		使用模板技术，把yml文件中的变量进行二次转化，是本框架的yml文件的技术基础
		:param parameters: 读取yaml文件的，得到的测试数据
		:return:
		"""
		# data = cls.load_yaml("config/caches.yaml")  # 从其他API响应中，读取的变量参数>>>文件
		parameters = json.dumps(parameters, ensure_ascii=False, indent=4)  # >>>编码成json字符串
		var_list = re.findall(r"\${(.*?)}", parameters)  # 查找
		parameters = parameters
		for i in var_list:
			# log.info("替换变量：{}".format(i))
			parameters = re.sub(r'\${%s}' % i, str(is_vars.get(i)), string=parameters)
		# log.info("替换结果为：{}".format(parameters))
		parameters = json.loads(parameters, encoding='utf-8')  # >>>将替换后的结果，解码为Python对象
		return parameters

	def request(self, req: dict, **kwargs):
		proxies = {
			'http': 'http://127.0.0.1:8888/',
			'https': 'http://127.0.0.1:8888/',
		}
		req = self.regexps(req)
		url = "http://testapi.ad6755.com" + req["http"]["path"]
		method = req["http"]["method"]
		headers = req["http"]["headers"]
		params = req["http"]["params"]

		res = requests.request(method=method, url=url, headers=headers, params=params, **kwargs)
		self.setEnvironmentVariable(req, res)
		return res

if __name__ == "__main__":
	api = BaseApi()
	parameters = api.load_yaml("data/save_device_id.yaml")
	data = api.request(parameters)

