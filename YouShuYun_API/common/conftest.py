#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/10/21 0021 11:40
# @File: conftest.py
# @Poject: Work_Project

import os
import pytest
import json
from ruamel import yaml

def pytest_generate_tests(metafunc: "Metafunc") -> None:
	ids = []
	markers = metafunc.definition.own_markers
	for marker in markers:
		if marker.name == 'datefile':
			test_data_path = os.path.join(metafunc.config.rootdir, marker.args[0])
			with open(test_data_path) as f:
				ext = os.path.splitext(test_data_path[-1])
				if ext in ['.yml', '.yaml']:
					test_data = yaml.safe_load(f)
				elif ext == '.json':
					test_data = json.load(f)
				else:
					raise TypeError('datafile must be yaml or json, root must be tests')

	if "parameters" in metafunc.fixturenames:
		for data in test_data['tests']:
			ids.append(data['case'])
		metafunc.parametrize('parameters', test_data['tests'], ids=ids, scope="function")