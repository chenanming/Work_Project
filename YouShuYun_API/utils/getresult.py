#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 18:14
# @File: getresult.py
# @Poject: Work_Project
import pytest
import allure
from requests import Response
from YouShuYun_API.utils.logger import log
from YouShuYun_API.common.variable import is_vars
from YouShuYun_API.common.RegExp import regexps

def get_result(r: Response, extract):
	'''获取response返回值'''
	for i in extract:
		value = regexps(i, extract)
		log.info("正则提取结果值：{}={}".format(i, value))
		is_vars.set(i, value)
		# pytest.assume(is_vars(i))
	with allure.step("提取响应中的值"):
		for i in extract:
			allure.attach(name="提取%s" % i, body=is_vars.get(i))

if __name__ == "__main__":
	resp = {
  "code": 1,
  "msg": "\u6210\u529f\uff01",
  "data": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdGVzdGFwaS5hZDY3NTUuY29tL3NhdmVfZGV2aWNlX2lkIiwiaWF0IjoxNjA1Njc5NTcwLCJleHAiOjE2MDU3NjU5NzAsIm5iZiI6MTYwNTY3OTU3MCwianRpIjoiN1hncmJoRG1IZjZNUXdXdSIsInN1YiI6MTU1Mn0.YF5RDl0-m2Zo49jWZ7rfWuITyNatLUcP1JGiGzBWt6k",
    "is_new": 0,
    "exp": "2020-11-24 14:06:10"
  }
}
	a = {
  "tests": {
    "method": "POST",
    "path": "/save_device_id",
    "headers": {
      "modelname": "Mi 6",
      "brandname": "Xiaomi",
      "appsystem": "kuaiyingyong",
      "version": "3.2.1",
      "androidid": "5d20dfe6dc75c465",
      "imei": "868030036658167"
    },
    "params": {
      "Uid": "5d20dfe6dc75c465",
      "app_type": 32,
      "deviceCode": "221964b5488ab8b48cea68e54cb996a9",
      "market_name": "kuaiyingyong",
      "mobile": "MI 6"
    },
    "extract": {
      "token": "conten.data.token"
    }
  }
}
	print(get_result(resp, a))
