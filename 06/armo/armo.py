# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 10:31
# @Author  : armo
# @File    : armo.py
# @Software: PyCharm
# @Pyver   : 3.6.0

def sortafter(sortfn,list,group):
    '''
    :param sortfn:排序函数
    :param list: 待排序列表
    :param group: 关键词集合
    :return: 列表
    '''
    beforlist = sortfn(list)
    afterlist = []
    for i in group:
        if i in beforlist:
            #处理多个相同值
            while True:
                try:
                    beforlist.remove(i)
                    afterlist.append(i)
                except ValueError:
                    break
    return afterlist + beforlist

def sortbefor(list):
    '''
    列表排序
    :param list:
    :return:
    '''
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[j] < list[i]:
                list[j],list[i] = list[i],list[j]
    return list


l1 = [2,5,3,7,3,6,1,4,9]
l2 = [5,3,7]
l3 = sortafter(sortbefor,l1,l2)
print(l3)
# ===================================================================
number = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

def sort_priority(number, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    number.sort(key=helper)


sort_priority(number, group)

print(number)
