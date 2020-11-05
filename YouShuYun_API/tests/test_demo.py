#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/4 0004 11:12
# @File: test_demo.py
# @Poject: Work_Project

import pytest
import allure
from YouShuYun_API.utils.request import req
from YouShuYun_API.common.YamlData import testinfo
from YouShuYun_API.common.base_api import BaseApi


@allure.feature("单个API测试")
class TestStandAlone(BaseApi):
	@pytest.mark.parametrize('case', testinfo.device.values(), ids=testinfo.device.keys())
	def test_stand_alone_interface(self, case):
		# print(case)
		r = req.send_request(case['method'], case['path'], case.get('extract'), self.sign(**case['paramas']))
		print(r)