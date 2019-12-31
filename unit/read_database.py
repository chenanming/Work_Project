#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/12/30 0030 20:04
# @File: read_database.py
# @Poject: Work_Project

import pymysql

class DB:

	def __init__(self, host='localhsot', port='3306', user='root', passwd='root', db='', charset='utf-8'):
		# 建立连接
		self.conn = pymysql.connect(
			host="172.16.71.93",
			user="root",
			passwd="VSx6oKXPjvqQPJZ3GnIX",
			database="leshu_test",
			charset="utf-8"
		)
		# 创建游标
		self.cur = self.conn.cursor(cursor= pymysql.cursors.DictCursor)

	def __enter__(self):
		# 返回游标
		return self.cur

	def __exit__(self, exc_type, exc_val, exc_tb):
		# 提交数据库并执行
		self.conn.commit()
		# 关闭游标
		self.cur.close()
		# 关闭数据库连接
		self.conn.close()

if __name__ == '__main__':
	with DB(host="172.16.71.93",
			port="3306",
			user="root",
			passwd="VSx6oKXPjvqQPJZ3GnIX",
			db="leshu_test") as db:
		db.execute("Select * from user")