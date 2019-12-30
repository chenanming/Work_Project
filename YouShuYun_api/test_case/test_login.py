#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 17:28
# @File: test_login.py
# @Poject: Work_Project

from YouShuYun_api.api.login import Login

class TestLogin:
	login = Login()
	def setup_class(self):
		pass

	def test_wechat_login(self):
		res = self.login.wechat_login()
		assert res['code'] == 1

	def test_qq_login(self):
		pass