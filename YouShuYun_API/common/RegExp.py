#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 18:01
# @File: RegExp.py
# @Poject: Work_Project
import re
import json
from YouShuYun_API.common.variable import is_vars
from YouShuYun_API.utils.logger import log
from YouShuYun_API.utils.serializa import is_json_str

class RegExp(object):
	def __init__(self):
		self.re = re

	def findall(self, string):  # 传递json类型的字符串的参数
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
	a = {
    "case": "验证tong获取",
    "http": {
        "method": "POST",
        "path": "/save_device_id",
        "token": "{{token}}",
        "headers": {
            "modelname": "Mi 6",
            "brandname": "Xiaomi",
            "appsystem": "kuaiyingyong",
            "version": "3.2.1",
            "androidid": "5d20dfe6dc75c465",
            "imei": "868030036658167",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "params": {
            "Uid": "5d20dfe6dc75c465",
            "app_type": 32,
            "deviceCode": "93c2137932882c0308905681fd72c0c9",
            "market_name": "kuaiyingyong",
            "mobile": "MI 6",
            "sign": "d39e7dd120c026829bd0434fc630697d"
        }
    },
    "extract": {
        "token": "content.data.token",
        "msg": "content.msg"
    },
    "expected": {
        "response": {
            "code": [
                1
            ]
        }
    }
}
	print(regexps.findall(a))