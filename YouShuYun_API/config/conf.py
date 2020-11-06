#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/3 0003 16:56
# @File: conf.py
# @Poject: Work_Project
import os

# 项目目录
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 数据文件
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 日志文件
LOG_PATH = os.path.join(BASE_DIR, 'logs')

if __name__ == "__main__":
	print(DATA_DIR)