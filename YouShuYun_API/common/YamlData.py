#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 19:49
# @File: YamlData.py
# @Poject: Work_Project
import os
from ruamel import yaml
from YouShuYun_API.config.conf import DATA_DIR

class ApiData:
	def __init__(self):
		self.info_path = os.path.join(DATA_DIR, 'testinfo.yaml')
		self.token_path = os.path.join(DATA_DIR, 'save_device_id.yaml')

	@classmethod
	def load(cls, path):
		with open(path, encoding='utf-8') as f:
			return yaml.safe_load(f)

	@property
	def info(self):
		return self.load(self.info_path)

	@property
	def device(self):
		return self.load(self.token_path)

	def test_info(self, value):
		return self.info['test_info'][value]

	def device_path(self, value):
		return self.device['tests'][value]

testinfo = ApiData()

if __name__ == "__main__":
	print(testinfo.info['test_info'])
	print(testinfo.device['tests'][])