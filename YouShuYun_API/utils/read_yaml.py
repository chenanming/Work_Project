#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/20 0020 17:12
# @File: read_yaml.py
# @Poject: Work_Project

from ruamel import yaml

class ReadYaml:
	def get_token_cache(self, cachePath="F:\chenanming\Work_Project\YouShuYun_API\data\caches.yaml"):
		with open(cachePath, 'r') as f:
			token_cache = yaml.safe_load(f)
			# print(data['token'])
			return token_cache["token"]

if __name__ == '__main__':
	a = ReadYaml()
	a.get_token_cache()