#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@version: ??
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: __init__.py.py
@time: 2017-12-05-13:03
"""

'''函数方法描述'''


def func():
	pass


'''类描述'''


class Main():
	# <editor-fold desc="self参数构造">
	def __init__(self, a1):
		self.a1 = a1

	# </editor-fold>

	# <editor-fold desc="类的解释描述">
	def __str__(self):
		return '类的解释描述'

	# </editor-fold>

	# <editor-fold desc="函数描述">
	def func_one(self):
		pass

	# </editor-fold>

	# <editor-fold desc="函数描述">
	# 静态方法 self 不是必须的了
	# 如果加了self 把它理解为一个参数就行了
	@staticmethod
	def static_foo(a1, a2):
		pass

	# </editor-fold>


if __name__ == '__main__':
	pass