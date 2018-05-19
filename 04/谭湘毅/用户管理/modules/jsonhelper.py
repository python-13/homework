#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: jsonhelper.py
@time: 2018-05-18-16:11
"""

import json, os
import simplejson

from modules.Common import Common as my_Common


class jsonhelper(object):
	def __init__(self):
		pass

	#以 json 格式写入数据表文件(追加)
	def append_db_json(contant, filename):
		"""
		将信息以 json 格式写入数据表文件(追加)
		:param contant: 要写入的 json 格式内容
		:param filename: 要写入的数据表文件名
		:return: 无返回
		"""
		try:
			with open(filename, 'a+') as fa:
				fa.write(simplejson.dumps(contant, sort_keys=True))
				fa.write("\n")
		except Exception as e:
			my_Common.write_error_log(e)

	#格式写入数据表文件（覆盖）
	def write_db_json(contant, filename):
		"""
		将信息以 json 格式写入数据表文件（覆盖）
		:param contant: 写入的json数据内容
		:param filename: 要写入的文件名
		:return: 无返回结果
		"""
		try:
			with open(filename, 'w+') as fw:
				fw.write(simplejson.dumps(contant))#,sort_keys=True,indent=4))
		except Exception as e:
			my_Common.write_error_log(e)

	def write_db_simplejson(contant, filename):
		"""
		将信息以 json 格式写入数据表文件（覆盖）
		:param contant: 写入的json数据内容
		:param filename: 要写入的文件名
		:return: 无返回结果
		"""
		try:
			with open(filename, 'w+') as fw:
				fw.write(simplejson.dumps(contant, ensure_ascii=False, sort_keys=True, indent=4))
		except Exception as e:
			my_Common.write_error_log(e)

	def load_data_from_db(tabename):
		"""
		从指定的数据表中获取所有数据,通过 json 方式将数据返回
		:param tabename: 数据文件名
		:return: 返回所有结果
		"""
		try:
			with open(tabename, 'r+') as f:
				return json.load(f)
		except Exception as e:
			my_Common.write_error_log(e)


if __name__ == '__main__':
	pass
