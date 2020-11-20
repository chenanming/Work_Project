#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/21 0021 11:40
# @File: conftest.py
# @Poject: Work_Project
import os
import json
import pytest
from ruamel import yaml

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def pytest_generate_tests(metafunc):
    ids = []
    markers = metafunc.definition.own_markers
    for marker in markers:
        if marker.name == 'datafile':  # 读取外数据
            test_data_path = os.path.join(DATA_DIR, marker.args[0])  # 拼接测试数据路径
            with open(test_data_path, encoding='utf-8') as f:
                ext = os.path.splitext(test_data_path)[-1]
                if ext in ['.yaml', '.yml']:
                    test_data = yaml.safe_load(f)
                elif ext == '.json':
                    test_data = json.load(f)
                else:
                    raise TypeError('datafile must be yaml or json，root must be tests')
    if "parameters" in metafunc.fixturenames:   # 用外部数据进行参数化
        for data in test_data['tests']:  # 用test_data中的case作为测试用例名称
            ids.append(data['case'])
        # 用test_data这个列表对parameters进行参数化。
        metafunc.parametrize("parameters", test_data['tests'], ids=ids, scope="function")