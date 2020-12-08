#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 17:53
# @File: variable.py
# @Poject: Work_Project

class Variable(object):
	'''全局变量'''
	def __init__(self):
		super().__init__()

	def set(self, key, value):
		setattr(self, key, value)

	def get(self, key):
		return getattr(self, key)

	def has(self, key):
		return hasattr(self, key)

is_vars = Variable()

if __name__ == "__main__":
	is_vars.set("token", "sdlkfjldksjf")
	print(is_vars.get("token"))