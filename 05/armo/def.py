# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 23:27
# @Author  : armo
# @File    : def.py.py
# @Software: PyCharm
# @Pyver   : 3.6.0

from collections import Iterable

#map
def map(fn, list):
    '''
    def map every num add 1
    :param fn: func
    :param list:  list
    :return:  list
    '''
    if isinstance(list,Iterable):
        newlist = []
        for i in list:
            newlist.append(fn(i))
        return newlist
    else:
        return 'error not is Iterator'

def mapfn(x):
    '''
    nothing
    :param x:
    :return:
    '''
    x = x + 1
    return x

#reduce
def reduce(fn,list):
    '''
    def reduce sum
    :param fn:
    :param list:
    :return:
    '''
    if isinstance(list,Iterable):
        tmp = list[0]
        for i in range(len(list)-1):
            tmp = fn(tmp,list[i+1])
        return tmp
    else:
        return 'error not is Iterator'

def reducefn(x,y):
    z = x + y
    return z

#filter
def filter(fn,list):
    '''
    :return int
    :param fn:
    :param list:
    :return:
    '''
    if isinstance(list,Iterable):
        newlist = []
        for i in list:
            if fn(i):
                newlist.append(i)
        return newlist
    else:
        return 'error not is Iterator'

def filterfn(x):
    if type(x) is int:
        return True
    else:
        return False

if __name__ == '__main__':
    list = [1,2,3,4]
    list1 = [1, 2, 3, '4' ]
    l1 = map(mapfn,list)
    print(l1)
    l2 = reduce(reducefn,list)
    print(l2)
    l3 = filter(filterfn,list1)
    print(l3)