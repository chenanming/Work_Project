#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 16:19
# @File: rechargemoney.py
# @Poject: Work_Project

import requests
from YouShuYun_API.api.base_api import BaseApi
from YouShuYun_API.api.get_token import QuickLogin

class Recharge(BaseApi):
	url = "http://testapi.ad6755.com/rechargemoney"
	@classmethod
	def recharge_money(cls, modelname, brandname):
		proxies = {
			'http': 'http://127.0.0.1:8888/',
			'https': 'http://127.0.0.1:8888/',
		}
		params = {
			"app_type": 32,
			"market_name": "kuaiyingyong",
			"token": QuickLogin.save_device_id(),
			"sign": ""
		}
		print(params)
		headers = {
			"modelname": modelname,
			"brandname": brandname,
			"version": "3.2.1",
			"appsystem": "kuaiyingyong",
			"imei": "868030036658167",
			"content_type": "application/x-www-form-urlencoded; charset=utf-8"
		}
		params = cls.sign(params)
		print(params)
		res = requests.request("POST", cls.url, params=params, headers=headers,
							proxies=proxies,  # 映射指定的代理的url
							verify=True).json()
		cls.versed(res)
		return res


if __name__ == "__main__":
	modelname = "MI 5"
	brandname = "miaomi"
	print(Recharge.recharge_money(modelname, brandname))