#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 16:19
# @File: rechargemoney.py
# @Poject: Work_Project

import requests
from YouShuYun_API.api.base_api import BaseApi
from YouShuYun_API.api.get_token import QuickLogin
from collections import Iterable

class Recharge(QuickLogin):
	url = "http://testapi.ad6755.com/rechargemoney"
	def recharge_money(self, modelname, brandname):
		proxies = {
			'http': 'http://127.0.0.1:8888/',
			'https': 'http://127.0.0.1:8888/',
		}
		params = {
			"app_type": 32,
			"market_name": "kuaiyingyong",
			"token": self.get_token(),
			"sign": ""
		}
		headers = {
			"modelname": modelname,
			"brandname": brandname,
			"version": "3.2.1",
			"appsystem": "kuaiyingyong",
			"imei": "868030036658167",
			"content_type": "application/x-www-form-urlencoded; charset=utf-8"
		}
		print(params)
		params = self.sign(params)
		res = requests.request("POST", url=self.url, params=params, headers=headers,
							# proxies=proxies,  # 映射指定的代理的url
							# verify=False
							   ).json()
		self.versed(res)
		return res


# if __name__ == "__main__":
# 	modelname = "MI 6"
# 	brandname = "Xiaomi"
# 	res = Recharge()
# 	res.recharge_money(modelname, brandname)