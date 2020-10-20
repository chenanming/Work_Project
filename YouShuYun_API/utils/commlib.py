#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/19 0019 17:48
# @File: commlib.py
# @Poject: Work_Project

from ruamel import yaml

'''读取.ymal文件，获取测试参数'''
class ReadTestYaml:
	def get_test_data(self, test_data_path):
		case = []
		http = []
		expected = []
		with open(test_data_path, 'r', encoding='utf-8') as f:
			data = yaml.load(f.read(), Loader=yaml.Loader)
			test = data['tests']
			print(test)
			for td in test:
				case.append(td.get(''))
				http.append(td.get('headers', {}))
				expected.append(td.get('exepted', {}))
				print(td)
				print(case)
				print(type(case))
				print(type(http))
				print(type(expected))
		paramesters = zip(case, http, expected)
		return case, expected

if __name__ == "__main__":
	a = ReadTestYaml()
	a.get_test_data("F:\chenanming\Work_Project\YouShuYun_API\data\save_device_id.yaml")