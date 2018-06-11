#!/usr/bin/env python
# coding: utf-8
import time
import json
import inspect
import functools

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def timeit(fn):
    
    @functools.wraps(fn)
    def wrapper(*a,**kw):
        start = time.time()
        result = fn(*a, **kw)
        end = time.time()
        elapse = end - start
        print("Time Elapse: ", elapse)
        return result
    return wrapper

# 实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，
# 先检测要运行的斐波那契数是否在缓存里面，如果在直接返回结果，
# 否则计算把结果存在缓存里面，再返回结果(这里需要一个while True的交互模式)。


def cache(fn):
    __cache = {}

    @functools.wraps(fn)
    def wrapper(*p, **karg):
        _ = fn.__name__, inspect.getcallargs(fn, *p, **karg)
        signature = json.dumps(_)

        if signature not in __cache.keys():
            result = fn(*p, **karg)
            __cache[signature] = result

        return __cache.get(signature)
    return wrapper

def fa(n):
    if n == 1 or n == 2:
        return 1
    return fa(n-1) + fa(n-2)


@timeit
@cache
def fa2(n):
    if n == 0 or n == 1:
        return 1
    c1 = 1
    c2 = 1
    for i in range(3,n+1):
        s = c1 + c2
        c1,c2 = s,c1
    return s


fa2(9000)
