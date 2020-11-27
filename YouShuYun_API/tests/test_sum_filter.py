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
from jinja2 import Environment, FileSystemLoader
from YouShuYun_API.common.base_api import BaseApi
from YouShuYun_API.common.variable import is_vars

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'templates')

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

		variable = {}
		for k, v in tmp.items():
			lists = v.split(".")[1:]  # 1>>data.token
			con = res.json()
			for i in lists:
				con = con[i]
			variable[k] = con
		print(variable)
		try:
			with open("F:\chenanming\Work_Project\YouShuYun_API\config\caches.yaml", "a+", encoding='utf-8') as f:
				yaml.dump(variable, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)
			print("token缓存写入成功！")
		except:
			print("token缓存写入失败！")

		request_data = json.dumps(parameters, ensure_ascii=False)  # >>>转成json字符串
		print(request_data)
		# print(type(request_data))
		key = re.findall(r'^token$', request_data)
		print(key)



		# file_loader = FileSystemLoader(DATA_DIR)
		# env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
		# template = env.get_template('showminors.txt')
		# output = template.render(content=res.json(), parameters=parameters)
		# is_vars.set("token", output)
		# to = is_vars.get("token")
		# print(to)
