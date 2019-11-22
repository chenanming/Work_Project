#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/18 0018 16:48
# @File: search_page.py
# @Poject: Work_Project
from selenium.webdriver.common.by import By

from youshuyun.testbase.base_driver import BaseDriver


class SearchPage(BaseDriver):

	def search(self, keyword):
		# 输入关键字
		self.driver.find_element(By.ID, self.readini.get_value("search_input")).send_keys(keyword)
		return self

	def select(self, keyword):
		# 关键字，联想列表
		self.driver.find_element_by_xpath("//*[@resource-id, 'com.youshuge.happybook:id/tvTitle']//[@text=%s]").click() % (keyword)
		return self