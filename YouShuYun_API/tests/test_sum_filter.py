#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 13:23
# @File: test_sum_filter.py
# @Poject: Work_Project

import os
import pytest
import requests
from YouShuYun_API.common.base_api import BaseApi

Base_Path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class TestSaveDeviceId(BaseApi):
	host = "http://testapi.ad6755.com"

	@pytest.mark.datafile("save_device_id.yaml")
	def test_save_device_id(self, parameters):
		parameters = self.regexps(parameters)
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
			# variable[k] = con
			variable = is_vars.set(k, con)
		"""

		variable = self.setEnvironmentVariable(parameters, res)

		file_path = os.path.join(Base_Path, 'config/caches.yaml')
		# print(file_path)
		# if len(variable) != 0:
		# 	try:
		# 		with open(file_path, "a+", encoding='utf-8') as nf:
		# 			yaml.dump(variable, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True)
		# 	except:
		# 		print("token缓存写入失败！")
