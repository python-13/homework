#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: init_DB.py
@time: 2018-05-18-17:11
"""

'''类描述'''

import os
from datetime import date, datetime

from conf import conf as  my_conf

from modules.Common import Common as my_Common
from modules.jsonhelper import jsonhelper as my_jsonhelper


class init_DB(object):

	def __init__(self):
		# pass
		self.init_database()

	'''定义用户字典'''
	_user_dic = {
		"test": {'password': '1', 'name': '测试', 'mobile': '1381005956',
				 'islocked': 0, 'role': 'user', 'isdel': 0, 'islocked': 0},
		"admin": {'password': '1', 'name': '谭湘毅', 'mobile': '1381005956',
				  'islocked': 0, 'role': 'admin', 'isdel': 0, 'islocked': 0}
	}

	'''函数 用户数据写入方法，写入json文件'''
	def init_db_users(self):
		_db_file = os.path.join(my_conf.DATABASE['dbpath'], 'users.db')
		for k, v in self._user_dic.items():
			temppasswd = self._user_dic[k]['password']
			encryptpasswd = my_Common.encrypt(temppasswd)
			self._user_dic[k]['password'] = encryptpasswd
		my_jsonhelper.write_db_simplejson(self._user_dic, _db_file)
		print("Table create successfull".format(_db_file))

	'''定义一个数据库统一初始化函数'''
	def init_database(self):
		#获取数据文件列表
		tables = list(my_conf.DATABASE['tables'].values())
		#数据表存放路径
		database = my_conf.DATABASE['dbpath']

		for _table in tables:
			if not os.path.exists(os.path.join(database, '{0}.db'.format(_table))):
				if hasattr(self, 'init_db_{0}'.format(_table)): #调用创建表的方法
					init_func = getattr(init_DB, 'init_db_{0}'.format(_table))
					init_func(self)
				else:
					my_Common.write_error_log(
						"Table create Error...." + os.path.join(database, '{0}.db'.format(_table)))
			else:
				my_Common.show_message(os.path.join(database, '{0}.db'.format(_table),
													'表已经存在，数据初始化已完成'), "INFORMATION")


if __name__ == '__main__':
	my = init_DB()
	my.init_database()
