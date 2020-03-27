#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/3/25 0025 17:47
# @File: gettoken.py
# @Poject: Work_Project

import requests
from TestQuick_API.api.base_api import BaseApi

class Login(BaseApi):
	def gettoken(self, ProjectName=None):
		if ProjectName == 'YouShuYun_APP':
			headers = {
				"modelname": "MI 6",
				"appsystem": "android",
				"brandname": "xiaomi",
				"version": "3.1.5",
				"appversion": "78",
				"content-type": "application/x-www-form-urlencoded; charset=utf-8"
			}
		elif ProjectName == 'QuickAPP_yxsc':
			headers = {
				"modelname": "MI 6",
				"appsystem": "kuaiyingyong",
				"imei": "868030036658167",
				"brandname": "xiaomi",
				"version": "3.1.3",
				"androidid": "5d20dfe6dc75c465",
				"key": "894fae147eb623e18c6564b564397808",
				"content-type": "application/x-www-form-urlencoded; charset=utf-8"
			}
			params = {
				"Uid": "5d20dfe6dc75c465",
				"only_code": "5d20dfe6dc75c465",
				"app_type": "32",  # 悠书云小说：32  言湘书城：34
				"deviceCode": "221964b5488ab8b48cea68e54cb996a9",
				"market_name": "kuaiyingyong"
			}

		elif ProjectName == 'QuickAPP_ysy':
			headers = {
				"modelname": "MI 6",
				"appsystem": "kuaiyingyong",
				"imei": "868030036658167",
				"brandname": "xiaomi",
				"version": "3.1.3",
				"androidid": "5d20dfe6dc75c465",
				"key": "894fae147eb623e18c6564b564397808",
				"content-type": "application/x-www-form-urlencoded; charset=utf-8"
			}
		else:
			print("请输如项目名：")

