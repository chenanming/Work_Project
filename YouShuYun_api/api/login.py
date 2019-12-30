#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 16:19
# @File: login.py
# @Poject: Work_Project

import requests
from unit.json_format import JsonData
from YouShuYun_api.api.base_api import BaseApi

class Login(BaseApi):
	wechat_login_url = "http://testqyapi.ad6755.com/wechat_login"

	def wechat_login(self):
		proxies = {'http': 'http://127.0.0.1:8080/',
				   'https': 'http://127.0.0.1:8080/',
				   }
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
							proxies=proxies,  # 映射指定的代理的url
							verify=False).json()
		self.versed(res)
		return res

	def qq_login(self):
		pass

	def phone_login(self):
		pass