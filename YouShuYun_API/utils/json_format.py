#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/7/23 0023 08:58
# @File: json_format.py
# @Poject: Work_Project

import json

class JsonData:

	@classmethod
	def format(cls, json_format):
		return json.dumps(json_format, indent=2, ensure_ascii=False)