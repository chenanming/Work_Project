#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/29 0029 13:48
# @File: test_save_device_id.py
# @Poject: Work_Project
import requests
import pytest
import allure
from YouShuYun_API.common.base_api import BaseApi


cases, list_params = BaseApi.get_test_data("F:\chenanming\Work_Project\YouShuYun_API\data\save_device_id.yaml")

'''悠书云小说(快应用)'''
@pytest.mark.quicktest
class TestSaveDeviceId(BaseApi):
	host = "http://testapi.ad6755.com"
	proxies = {
		'http': 'http://127.0.0.1:8888/',
		'https': 'http://127.0.0.1:8888/',
	}

	def setup_class(self):
		print("打印setup")
		pass

	@pytest.fixture(scope="class")
	def preparation(self):
		print("在数据库中准备测试数据")
		test_data = "在数据库中准备测试数据"
		yield test_data
		print("清理测试数据")

	@allure.story("测试save_device_id接口")
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
		self.setEnvironmentVariable(parameters, res)  # setEnvironmentVariable(): 提取yaml中所有需求提取成变量的参数

		# print(expected['response']['token'])
		# print(self.jsonpath(res.json(), '$.data.token'))
		# print(type(self.jsonpath(res.json(), '$.data.token')))
		# assert self.jsonpath(res.json(), '$.' != expected["response"]["token"])