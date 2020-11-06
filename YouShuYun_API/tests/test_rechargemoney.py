#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/30 0030 17:45
# @File: test_rechargemoney.py
# @Poject: Work_Project

import pytest
import allure
import requests
from YouShuYun_API.common.base_api import BaseApi
from YouShuYun_API.common.variable import is_vars



class TestRechargeMoney(BaseApi):
	# toke = glo.set_value("device_token")
	# print(globals())

	url = "http://testapi.ad6755.com/rechargemoney"
	host = "http://testapi.ad6755.com"
	proxies = {
		'http': 'http://127.0.0.1:8888/',
		'https': 'http://127.0.0.1:8888/',
	}
	params = {
		"app_type": 32,
		"market_name": "kuaiyingyong",
		"token": BaseApi.get_token(),
		"sign": ""
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

	# @allure.story("不同机型的,不同充值档位")
	# @pytest.mark.parametrize("modelname, brandname", [
	# 	("MIX", "xiaomi"),
	# 	("MI 6", "xiaomi"),
	# 	("OPPO Find x", "oppo"),
	# 	("VIVO NEX *", "VIVO"),
	# 	("MI 5", "XIAOMI")
	# ])
	# def test_rechargemoney(self, modelname, brandname, preparation):
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
	# 						   )
	# 	print(data.url)
	# 	# self.versed(data)
	# 	return data


	@allure.story("不同机型的,不同充值档位")
	@pytest.mark.datafile("_rechargemoney.yaml")
	def test_rechargemoney(self, parameters):
		res = requests.request(parameters["http"]['method'],
							 url=self.host + parameters["http"]['path'],
							 headers=parameters["http"]['headers'],
							 params=self.sign(parameters["http"]['params']),
							   # proxies=self.proxies,
							   # verify=False
							   )
		self.versed(res.json())
		to = is_vars.get("token")
		print(to)
		# expected = parameters["expected"]
		# print(res.url)
		# print(expected['response']['pay_model'])
		# print(self.jsonpath(res.json(), '$.data[*].price'))
		# assert self.jsonpath(res.json(), '$.data[0].pay_model') == expected['response']['pay_model']
		# assert self.jsonpath(res.json(), '$.data[*].price') == expected['response']['price']