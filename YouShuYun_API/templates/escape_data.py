#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 11:04
# @File: escape_data.py
# @Poject: Work_Project

from jinja2 import Template, escape

data = '<a>Today is a sunny day</a>'

tm = Template("{{ data | e }}")
msg	= tm.render(data=data)

print(msg)
print(escape(data))
