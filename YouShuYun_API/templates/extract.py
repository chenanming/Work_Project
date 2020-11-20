#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 11:12
# @File: extract.py
# @Poject: Work_Project

from jinja2 import Template

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getAge(self):
		return self.age

	def getName(self):
		return self.name

person = Person('Peter', 34)

tm = Template("My name is {{ per.getName() }} and i am {{ per.getAge() }}")
msg = tm.render(per=person)

print(msg)