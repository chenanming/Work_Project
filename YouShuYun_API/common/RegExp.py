#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 18:01
# @File: RegExp.py
# @Poject: Work_Project
import re
from YouShuYun_API.common.variable import is_vars
from YouShuYun_API.utils.logger import log
from YouShuYun_API.utils.serializa import is_json_str

class RegExp(object):
	def __init__(self):
		self.re = re

	def findall(self, string):
		keys = self.re.findall(r"\{{(.*?)}\}", string)
		return keys

	def subs(self, keys, string):
		result = None
		log.info("提取变量: {}".format(keys))
		for i in keys:
			log.info("替换变量：{}".format(i))
			result = self.re.sub(r"\{{%s}}" % i, is_vars.get(i), string)
			log.info("替换结果为：{}".format(result))
		return result

	def __call__(self, exp, string):
		"""在结果中查找"""
		return self.re.findall(r'\"%s":"(.*?)"' & exp, string)[0]

regexps = RegExp()
if __name__ == "__main__":
	a = "{'data': {'loginName': 18291900215, 'password': '{{tokenn}}', 'code': None, 'description': 'encrypt'}}"
	print(regexps.findall(a))