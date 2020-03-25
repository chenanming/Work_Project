#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/3/25 0025 17:57
# @File: base_api.py
# @Poject: Work_Project

import requests
from unit.json_format import JsonData

class BaseApi:

	@classmethod
	def versed(cls, json_object):
		print(JsonData.format(json_object)) # 使用Utils的format()方法对json数据（r），格式化输出