#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/16 0016 13:50
# @File: create_sign.py
# @Poject: Work_Project

import hashlib
from collections import Iterable

class JiaMi:
	'''MD5() 加密请求参数，生成签名'''
	@classmethod
	def sign_body(cls, body, appSecret="e9f0680f92d95ff9541e1eaff2cc18b6"):

		lists = []
		for k, v in sorted(body.items()):
			if k[1] != "" and k[0] != "sign":
				lists.append("".join(str(v)))
		# print(isinstance(body, Iterable))
		result = "".join(lists) + appSecret  # 拼接待签名字符串

		def jiamimd5(params):
			m = hashlib.md5()
			m.update(result.encode('UTF-8'))
			return m.hexdigest()

		sign = jiamimd5(result)  # 调用jiamimd5()加密生成签名，并赋值给变量"sign"
		body["sign"] = sign
		lists.clear()
		return body