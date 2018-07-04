#/usr/bin/env python

#本周作业：（6.19--6.24）
#写个mixin 类，并在这个类里面实现一个to_dict 的方法：这个方法是把对象的属性序列化
#成字典的形式。其他类通过继承这个mixin 来继承这个方法。注意：写之前，需要了解mixin
#是什么，它和子类继承有什么区别。

class TestMixin:

    def to_dict(self):
        return self.__dict__

class A(TestMixin):
    def __init__(self, name):
        self._name = name

