#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 16:19
# @File: get_token.py
# @Poject: Work_Project

import os
import requests
import pytest
from YouShuYun_API.api.base_api import BaseApi
from ruamel import yaml


class QiLogin(BaseApi):
	# 奇优APP

	wechat_login_url = "http://testqyapi.ad6755.com/wechat_login"
	result = {}

	def wechat_login(self):
		params = {
			"market_name": "qiyou_android",
			"union_id": "orjdyvx9ewcpOrj7eT36Ry5u-jm0",
			"device_id": "868030036658167",
			"open_id": "oT65v5rvdugSvi8IGPUkmhSEcecw",
			"device_code": "d6a964e0ce916715829e7732bedb43d7",
			"sex": "1",
			"nickname": "陈安明",
			"headimgurl": "http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJ5exQKIhibFicKPJFtTetGeUDn304rDqu4sGoFOPicMTTKCm0uvHrkrgLX6XpJ2gYXhIpn5SjdW0GwQ/132"
		}
		headers = {"content_type": "application/json; charset=UTF-8"}
		res = requests.post(self.wechat_login_url, params=params, headers=headers,
							#proxies=proxies,  # 映射指定的代理的url
							#verify=False
							).json()
		self.versed(res)
		try:
			self.result["token"] = res["data"]["token"]  # 获取登录后，response的token参数
		except:
			print("token参数获取失败！")

		return self.result, res

	def qq_login(self):
		pass

	def phone_login(self):
		pass

'''悠书云小说(快应用)'''
@pytest.mark.quicktest
class QuickLogin(BaseApi):
	caches = {}
	token = None
	_save_id_url = "http://testapi.ad6755.com/save_device_id"
	_login_url = "http://testapi.ad6755.com/checkSms"
	_user_info_url = "http://testapi.ad6755.com/get_user_info"
	headers = {
		"modelname": "MI 6",
		"appsystem": "kuaiyingyong",
		"imei": "868030036658167",
		"brandname": "xiaomi",
		"version": "3.2.1",
		"androidid": "5d20dfe6dc75c465",
		"key": "894fae147eb623e18c6564b564397808",
		"content-type": "application/x-www-form-urlencoded; charset=utf-8"
	}

	# cases, list_params = BaseApi.get_test_data("../Work_Project/YouShuYun_API/data/save_device_id.yaml")
	@classmethod
	# @pytest.mark.parametrize("cases,http,expected", list(list_params), ids=cases)
	def save_device_id(cls):
		proxies = {
			'http': 'http://127.0.0.1:8888/',
			'https': 'http://127.0.0.1:8888/',
		}
		params = {
			"Uid": "5d20dfe6dc75c465",
			"app_type": "32",  # 悠书云小说：32  言湘书城：34
			"deviceCode": "221964b5488ab8b48cea68e54cb996a9",
			"market_name": "kuaiyingyong",
			"key": "",
			"mobile": "MI 6",
			"sign": ""
		}
		params = cls.sign(params)
		# 缓存token，先定义一个空值变量token
		if cls.token == None:
			res = requests.request("POST", url=cls._save_id_url, headers=cls.headers, params=params, proxies=proxies).json()
			cls.versed(res)
			cls.token = res["data"]["token"]
		try:
			cls.caches["token"] = cls.token
			print(cls.caches)
			with open("F:\chenanming\Work_Project\YouShuYun_API\data\caches.ymal", "w", encoding='utf-8') as f:
				yaml.dump(cls.caches, f, Dumper=yaml.RoundTripDumper)
		except:
			print("token缓存写入失败！")

		return QuickLogin.token  # QuickLogin类的实例，供全局调用

	def get_user_info(self):
		params = {
			"app_type": "32",
			"market_name": "kuaiyingyong",
			"token": self.token,
			"sign": ""
		}
		params = self.sign(params)
		res = requests.request("POST", url=self._user_info_url, headers=self.headers, params=params).json()
		# print(res.request.body)
		self.versed(res)
		return res

	def phone_login(self):
		params = {
			"code": 666666,
			"app_type": "32",
			"device_id": "sagit",
			"devicecode": "b9926f8267456dd9da393dc1396b8a45",
			"mobile": 18888888888,
			"market_name": "kuaiyingyong",
			"token": QuickLogin.token
		}
		res = requests.post(self._login_url, headers=self.headers, params=params).json()
		self.versed(res)
		print(res.url)
		return res

# if __name__ == "__main__":
# 	q = QuickLogin()
# 	q.save_device_id()
# 	# q.get_user_info()
# 	# print(q.token)