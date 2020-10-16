#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/30 0030 17:45
# @File: test_rechargemoney.py
# @Poject: Work_Project

import pytest, allure
from YouShuYun_API.api.rechargemoney import Recharge

class TestRecharge:
	rec = Recharge()
	def setup_class(self):
		pass

	@allure.story("不同机型的,不同充值档位")
	@pytest.mark.parametrize("modelname, brandname", [
		("MIX", "xiaomi"),
		("MI 6", "xiaomi"),
		("OPPO Find x", "oppo"),
		("VIVO NEX *", "VIVO"),
		("MI 5", "XIAOMI")
	])
	def test_01(self, modelname, brandname):
		data = self.rec.recharge_money(modelname, brandname)
		print(data)
		#assert data['data'][0]['price'] != 0