#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/7/23 0023 08:58
# @File: json_format.py
# @Poject: Work_Project

import json
from jsonpath import jsonpath

class JsonData:

	@classmethod
	def format(cls, json_format):
		return json.dumps(json_format, indent=2)

	@classmethod
	def jsonpath(cls, json_object, expr):
		return jsonpath(json_object, expr)