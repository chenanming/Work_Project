#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 13:23
# @File: test_sum_filter.py
# @Poject: Work_Project

import os
import re
import json
import pytest
import requests
from ruamel import yaml
from YouShuYun_API.common.base_api import BaseApi
from YouShuYun_API.utils.logger import log

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'templates')
print(DATA_DIR)

class TestSaveDeviceId(BaseApi):
	host = "http://testapi.ad6755.com"

	@pytest.mark.datafile("save_device_id.yaml")
	def test_save_device_id(self, parameters):
		res = requests.request(parameters["http"]["method"],
							   url=self.host + parameters["http"]["path"],
							   headers=parameters["http"]["headers"],
							   params=self.sign(parameters["http"]["params"]),
							   # proxies=self.proxies
							   )
		self.versed(res.json())
		"""
		print(content)
		data_list = []
		for k, v in parameters.items():
			if k == "extract":
				for k, v in v.items(): # 1>>content.data.token
					data_list.append(v)

		var = {}
		for data in data_list:
			list = data.split(".")[1:]
			# print(list)
			con = content
			for i in list:
				con = con[i]
			var[data] = con

		extrat = {}
		for k, v in parameters.items():
			if k == "extract":
				for k, v in v.items():
					extrat[k] = var[v]
		print(extrat)
		"""

		tmp = {}
		for k, v in parameters.items():
			if k == "extract":
				for k, v in v.items():  # 1>>content.data.token
					tmp[k] = v
			else:
				pass

		variable = {}
		for k, v in tmp.items():
			lists = v.split(".")[1:]  # 1>>data.token
			con = res.json()
			for i in lists:
				con = con[i]
			variable[k] = con

		file_path = "F:\chenanming\Work_Project\YouShuYun_API\config\caches.yaml"
		if len(variable) != 0:
			try:
				with open(file_path, 'r', encoding='utf-8') as f:
					contents = yaml.safe_load(f)
					for i in contents:
						pass
				with open(file_path, "w", encoding='utf-8') as nf:
					yaml.dump(variable, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True, default_flow_style=False)
			except:
				print("token缓存写入失败！")

		# data = self.load_yaml("F:\chenanming\Work_Project\YouShuYun_API\config\caches.yaml")
		# print(type(data))

		req_yaml_data = json.dumps(parameters, ensure_ascii=False, indent=4)  # >>>编码成json字符串
		var_list = re.findall(r"\{{(.*?)}\}", req_yaml_data)
		req = req_yaml_data
		for i in var_list:
			log.info("替换变量：{}".format(i))
			req = re.sub(r'\{{%s}}' % i, str(variable[i]), string=req)
		log.info("替换结果为：{}".format(req))
		new_parameters = json.loads(req, encoding='utf-8')  # >>>将替换后的结果，解码为Python对象
		self.versed(new_parameters)