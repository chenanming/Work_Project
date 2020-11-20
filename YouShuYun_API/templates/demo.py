#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/18 0018 16:08
# @File: templates.py
# @Poject: Work_Project

from ruamel import yaml
from jinja2 import Template, Environment, FileSystemLoader

import os


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def get_vars_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        vars_string = f.read()
    # 读取初始的配置文件，并转换成字典
    base_vars = yaml.safe_load(vars_string)
    # 使用当前配置参数渲染自己本身，把配置中jinja语法渲染成实际值
    vars = Template(vars_string).render(base_vars)
    return vars

def render(vars, filename):
    load = FileSystemLoader('templates')
    env = Environment(loader=load)
    template = env.get_template(filename)
    result = template.render(vars)
    print(result)

if __name__ == '__main__':
    fn = 'F:\chenanming\Work_Project\YouShuYun_API\data\demo.yaml'
    vars = get_vars_from_file(fn)
    render(yaml.safe_load(vars), 'base.html')