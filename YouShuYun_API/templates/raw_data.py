#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 10:56
# @File: raw_data.py
# @Poject: Work_Project

from jinja2 import Template

data = '''
{% raw %}
His name is {{ name }}
{% endraw %}
'''

tm = Template(data)
msg = tm.render(name="Peter")

print(msg)
