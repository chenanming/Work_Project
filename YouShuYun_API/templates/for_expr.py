#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/20 0020 11:28
# @File: for_expr.py
# @Poject: Work_Project
import os
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR)

persons = [
	{'name': 'Andrej', 'age': 34},
	{'name': 'Mark', 'age': 17},
	{'name': 'Thomas', 'age': 44},
	{'name': 'Lucy', 'age': 14},
	{'name': 'Robert', 'age': 23},
	{'name': 'Dragomir', 'age': 54}
]

file_loader = FileSystemLoader(BASE_DIR)
env = Environment(loader=file_loader)

template = env.get_template('showpersons.txt')

output = template.render(persons=persons)
print(output)