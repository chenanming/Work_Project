#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/30 0030 17:45
# @File: test_rechargemoney.py
# @Poject: Work_Project

import pytest
import allure
import requests
from YouShuYun_API.api.save_device_id import QuickLogin

cases, list_params = QuickLogin.get_test_data("F:\chenanming\Work_Project\YouShuYun_API\data\rechargemoney.yaml")


class TestRecharge(QuickLogin):
	url = "http://testapi.ad6755.com/rechargemoney"
	host = "http://testapi.ad6755.com"
	proxies = {
		'http': 'http://127.0.0.1:8888/',
		'https': 'http://127.0.0.1:8888/',
	}

	params = {
		"app_type": 32,
		"market_name": "kuaiyingyong",
		"token": QuickLogin.get_token(),
		"sign": ""
	}

	def setup_class(self):
		pass

	# @allure.story("不同机型的,不同充值档位")
	# @pytest.mark.parametrize("modelname, brandname", [
	# 	("MIX", "xiaomi"),
	# 	("MI 6", "xiaomi"),
	# 	("OPPO Find x", "oppo"),
	# 	("VIVO NEX *", "VIVO"),
	# 	("MI 5", "XIAOMI")
	# ])
	# def test_rechargemoney(self, modelname, brandname):
	# 	headers = {
	# 		"modelname": modelname,
	# 		"brandname": brandname,
	# 		"version": "3.2.1",
	# 		"appsystem": "kuaiyingyong",
	# 		"imei": "868030036658167",
	# 		"content_type": "application/x-www-form-urlencoded; charset=utf-8"
	# 	}
	# 	data = requests.request("POST", url=self.url, params=self.sign(self.params), headers=headers,
	# 						   proxies=self.proxies,  # 映射指定的代理的url
	# 						   ).json()
	# 	self.versed(data)
	# 	return data

	@pytest.fixture(scope="class")
	def preparation(self):
		print("在数据库中准备测试数据")
		test_data = "在数据库中准备测试数据"
		yield test_data
		print("清理测试数据")

	@pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
	def test_rechargemoney(self, case, http, expected, preparation):
		res = requests.request(http['method'],
							 url=self.host + http['path'],
							 headers=http['headers'],
							 params=self.sign(http['params']),
							   # proxies=self.proxies,
							   # verigy=True
							   ).json()
		self.versed(res)
		return res