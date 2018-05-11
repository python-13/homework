#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 金额大小写转换.py
@time: 2018-05-09-15:32
"""

#定义大小写
dic_mony = {"0": "零", "1": "壹", "2": "贰",
			"3": "叁", "4": "肆", "5": "伍",
			"6": "陆", "7": "柒", "8": "捌",
			"9": "玖"}

#定义单位
dic_unit = {0: "", 1: "拾", 2: "佰", 3: "仟", 4: "万",
			5: "拾", 6: "佰", 7: "仟", 8: "亿"}

while True:
	num = input('请输入整数数字 Q 退出 ： ')
	listnum = list(num)
	lennum = len(listnum) - 1  # 反过来 千 百 十
	mid = []
	if num == 'q' or num == 'Q':
		break
	else:
		for item in listnum:
			# print(dic_mony[item])
			# print(dic_unit[lennum])
			mid.append(dic_mony[item])
			mid.append(dic_unit[lennum])
			lennum = lennum - 1 #继续递减
		print(mid)
		print('{}元'.format(''.join(mid)))
