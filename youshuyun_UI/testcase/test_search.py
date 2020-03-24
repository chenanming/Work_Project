#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/18 0018 17:14
# @File: test_search.py
# @Poject: Work_Project

from YouShuYun_UI.testpage.home_page import HomePage

class TestSearch:
	def setup(self):
		self.homepage = HomePage()

	def test_search(self):
		self.homepage.goto_search().search("超级特种兵").select(1)