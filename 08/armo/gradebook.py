# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 19:15
# @Author  : armo
# @Site    : www.8i88.cn
# @File    : gradebook.py
# @Software: PyCharm
# @Pyver   : 3.6.0

class Gradebook():
    def __init__(self):
        self.gradebook = {}

    def addrecord(self,name,score1,score2):
        score = { 'English' : score1 , 'Math' : score2 }
        self.gradebook[name] = score

    def averagegrade(self,name):
        score = self.gradebook[name]
        count = 0
        sum = 0
        for i in score.values():
            sum = sum + i
            count = count + 1
        return sum/count



obj = Gradebook()
obj.addrecord('armo',56,66)
obj.addrecord('armo1',88,66)
print(obj.averagegrade('armo'))
print(obj.averagegrade('armo1'))


