#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 16:19
# @File: home.py
# @Poject: Work_Project

import requests
import pytest
from unit.json_format import JsonData
from YouShuYun_API.api.base_api import BaseApi
from YouShuYun_API.api.login import QuickLogin

class Recharge(BaseApi):
	url = "http://testapi.ad6755.com/rechargemoney"


	def recharge_price(self, modelname, brandname):
		# 充值档位
		proxies = {
			'http': 'http://127.0.0.1:8888/',
			'https': 'http://127.0.0.1:8888/',
		}
		params = {
			"app_type": 32,
			"market_name": "kuaiyingyong",
			"token": QuickLogin.token
		}
		headers = {
			"modelname": modelname,
			"brandname": brandname,
			"version": "3.1.5",
			"appsystem": "kuaiyingyong",
			"imei": "868030036658167",
			"content_type": "application/x-www-form-urlencoded; charset=utf-8"
		}
		res = requests.post(self.url, params=params, headers=headers,
							proxies=proxies,  # 映射指定的代理的url
							verify=False).json()
		self.versed(res)
		return res