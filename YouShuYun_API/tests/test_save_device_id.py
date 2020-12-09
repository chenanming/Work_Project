#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/29 0029 13:48
# @File: test_save_device_id.py
# @Poject: Work_Project
import pytest
import allure
from YouShuYun_API.common.base_api import BaseApi


# @allure.feature
class TestSaveDeviceId(BaseApi):
	def setup_class(self):
		print("打印setup")
		pass

	# @pytest.fixture(scope="class")
	# def preparation(self):
	# 	print("在数据库中准备测试数据")
	# 	test_data = "在数据库中准备测试数据"
	# 	yield test_data
	# 	print("清理测试数据")

	# @allure.story("测试save_device_id接口")
	@pytest.mark.datafile("save_device_id.yaml")
	def test_save_device_id(self, parameters):
		res = self.request(parameters)
		self.versed(res.json())

		# print(expected['response']['token'])
		# print(self.jsonpath(res.json(), '$.data.token'))
		# print(type(self.jsonpath(res.json(), '$.data.token')))
		# assert self.jsonpath(res.json(), '$.' != expected["response"]["token"])