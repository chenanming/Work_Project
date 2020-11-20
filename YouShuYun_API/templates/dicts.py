#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 10:53
# @File: dicts.py
# @Poject: Work_Project

from jinja2 import Template

response = {
  "code": 1,
  "msg": "成功",
  "data": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdGVzdGFwaS5hZDY3NTUuY29tL3NhdmVfZGV2aWNlX2lkIiwiaWF0IjoxNjA1ODQyMDc2LCJleHAiOjE2MDU5Mjg0NzYsIm5iZiI6MTYwNTg0MjA3NiwianRpIjoiN0xxWHgyMlNhYThLdWs1TyIsInN1YiI6MTU1Nn0.PWw_i5hmetJZ23It-LFx9NL0wfcja3f1W8B7F4MAvS0",
    "is_new": 0,
    "exp": "2020-11-26 11:14:36"
  }
}


tm = Template("token: {{ content.data.token }}")
# tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")
msg = tm.render(content=response)

print(msg)