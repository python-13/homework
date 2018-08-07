# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 21:34
# @Author  : armo
# @Site    : www.8i88.cn
# @File    : mixin.py
# @Software: PyCharm
# @Pyver   : 3.6.0

class MixinDict:
    '''
        to dict mixin
    '''
    def todict(self):
        return sorted(self.__dict__)

class TestMixin(MixinDict):
    B = "123"
    def __init__(self):
        self.name = "test mixin"

    def testdef(self):
        self.value = "111"

A = TestMixin()
print(A.todict())
