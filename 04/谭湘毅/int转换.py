# -*- coding: utf-8 -*-
# @Time    : 2018/5/19/019 21:56
# @Author  : curetxy
# @Email   : curetxy@163.com
# @File    : int转换.py
# @Software: PyCharm

#快速的吧‘123456789’转成int型，不能直接使用int函数，别的不做限制。
def auto_int(s):
	s = s[::-1]
	num = 0
	num_temp = len(s)
	for i, v in enumerate(s, 0):
		for j in range(10):
			if v == str(j):
				num += j * (10 ** i)
		num_temp -= 1

	print(num,type(num))

num = auto_int('123456789')

# 逻辑很棒~尝试下用高阶函数来实现一下
