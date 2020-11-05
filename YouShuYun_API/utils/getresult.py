#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 18:14
# @File: getresult.py
# @Poject: Work_Project
import pytest
import allure
import pytest_assume
from requests import Response
from YouShuYun_API.utils.logger import log
from YouShuYun_API.common.variable import is_vars
from YouShuYun_API.common.RegExp import regexps
from YouShuYun_API.common.base_api import

def get_result(r: Response, extract):
	'''获取response返回值'''
	for i in extract:
		value = regexps(i, extract)
		log.info("正则提取结果值：{}={}".format(i, value))
		is_vars.set(i, value)
		pytest.assume(is_vars(i))
	with allure.step("提取响应中的值"):
		for i in extract:
			allure.attach(name="提取%s" % i, body=is_vars.get(i))

if __name__ == "__main__":
	a = "{'data': {'loginName': 18291900215, 'password': '{{tokenn}}', 'code': None, 'description': 'encrypt'}}"
	print(get_result(a, "token"))
