#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 16:08
# @File: json_format.py
# @Poject: Work_Project

import json

class JsonData:

	@classmethod
	def format(cls, json_format):
		return json.dumps(json_format, indent=2)