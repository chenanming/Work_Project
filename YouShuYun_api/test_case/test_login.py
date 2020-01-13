#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/9 0009 17:28
# @File: test_login.py
# @Poject: Work_Project

from unittest import TestCase
from YouShuYun_api.api.login import QiLogin, QuickLogin


class TestQiyouLogin:
	# 奇优APP登录接口

	login = QiLogin()
	def setup_class(self):
		pass

	def test_wechat_login(self):
		res = self.login.wechat_login()
		assert res[0]['code'] == 1

	def test_qq_login(self):
		pass


class TestYouLogin:
	# 悠书云阅读APP登录接口
	pass



class TestQuickLogin:
	# 悠书云小说（快应用）登录接口

	login = QuickLogin()
	def setup_class(self):
		pass

	def test_save_device(self):
		token = self.login.save_device_id()
		assert token != None

	def test_get_user_info(self):
		res = self.login.get_user_info()
		assert res['code'] == 1


	def test_phone_loging(self):
		res = self.login.phone_login()
		assert res['code'] == 1