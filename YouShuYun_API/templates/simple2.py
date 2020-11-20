#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 10:25
# @File: simple2.py
# @Poject: Work_Project

from jinja2 import Template

name = "Pater"
age = 32

tm = Template("My name is {{ name }} and I am {{ age }}")
msg = tm.render(name=name, age=age)

print(msg)