#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/29 0029 13:48
# @File: test_save_device_id.py
# @Poject: Work_Project
import requests
import pytest
import allure
from ruamel import yaml
from YouShuYun_API.common.base_api import BaseApi
from YouShuYun_API.utils.logger import log
import pytest_cache


cases, list_params = BaseApi.get_test_data("F:\chenanming\Work_Project\YouShuYun_API\data\save_device_id.yaml")

'''悠书云小说(快应用)'''
@pytest.mark.quicktest
class TestSaveDeviceId(BaseApi):
	caches = {}
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
	@pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
	def test_save_device_id(self, case, http, expected, preparation):
		res = requests.request(http["method"],
							   url=self.host + http["path"],
							   headers=http["headers"],
							   params=self.sign(http["params"]),
							   # proxies=self.proxies
							   )
		self.versed(res.json())
		self.token = res.json()["data"]["token"]
		try:
			self.caches["token"] = self.token
			'''获取token，并写入caches.yaml文件'''
			with open("F:\chenanming\Work_Project\YouShuYun_API\config\caches.yaml", "w", encoding='utf-8') as f:
				yaml.dump(self.caches, f, Dumper=yaml.RoundTripDumper)
			print("token缓存写入成功！")
		except:
			print("token缓存写入失败！")
		# print(expected['response']['token'])
		# print(self.jsonpath(res.json(), '$.data.token'))
		# print(type(self.jsonpath(res.json(), '$.data.token')))
		# assert self.jsonpath(res.json(), '$.' != expected["response"]["token"])