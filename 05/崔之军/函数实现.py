from collections import Iterable


# map函数实现

def square(x):
    """docstring"""
    return x * x


def cusmap(func, *args):
    lst = []
    if isinstance(args, Iterable):
        for i in list(*args):
            lst.append(func(int(i)))
        return lst
    else:
        print('error not is Iterator')
        return


print(cusmap(square, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# reduce函数实现

def fn(x, y):
    """docstring"""
    return x + y


def reduce(func, *args):
    """docstring"""
    ret = 0
    list1 = list(*args)
    length = len(list1) - 1
    for i in list1[::2]:
        if list1.index(i) != length:
            value = list1[list1.index(i) + 1]
        else:
            value = 0
        ret += fn(i, value)
    return ret


ret = reduce(fn, [1, 2, 3, 4, 6])
print(ret)

#  filter 函数实现
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_odd(n):
    return n % 2 == 1

def cumfilter(func,*args):
    """docstring"""
    ret = []
    for i in list(*args):
        if is_odd(i):
            ret.append(i)
    return ret

print(cumfilter(is_odd,lst))
