# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 23:27
# @Author  : armo
# @File    : def.py.py
# @Software: PyCharm
# @Pyver   : 3.6.0

def map(fn, list):
    '''
    def map
    :param fn: func
    :param list:  list
    :return:  list
    '''
    newlist = []
    for i in list:
        newlist.append(fn(i))
    return newlist

def fn(x):
    '''
    nothing
    :param x:
    :return:
    '''
    x = x + 1
    return x

if __name__ == '__main__':
    l1 = map(fn,[1,2,3])
    print(l1)