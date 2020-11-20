#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 13:23
# @File: test_sum_filter.py
# @Poject: Work_Project

import os
import pytest
import requests
from jinja2 import Environment, FileSystemLoader
from YouShuYun_API.common.base_api import BaseApi

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'templates')

class TestSaveDeviceId(BaseApi):
	host = "http://testapi.ad6755.com"

	@pytest.mark.datafile("save_device_id.yaml")
	def test_save_device_id(self, parameters):
		print(parameters)
		res = requests.request(parameters["http"]["method"],
							   url=self.host + parameters["http"]["path"],
							   headers=parameters["http"]["headers"],
							   params=self.sign(parameters["http"]["params"]),
							   # proxies=self.proxies
							   )
		self.versed(res.json())

		file_loader = FileSystemLoader(DATA_DIR)
		env = Environment(loader=file_loader)
		print(DATA_DIR)

		template= env.get_template('showminors.txt')

		output = template.render(content=res.json())
		print(output)