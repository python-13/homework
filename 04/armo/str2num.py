# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 18:49
# @Author  : armo
# @File    : str2num.py
# @Software: PyCharm
# @Pyver   : 3.6.0


numdic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
numstr = input("输入数字:")
j = 1
num = 0
for i in numstr[::-1]:
    num = num + numdic[i] * j
    j = j * 10



print(num)
print(type(num))

# 可以，尝试下封装成函数，然后在用面向对象的方式再试试
