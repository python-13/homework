# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 11:45
# @Author  : armo
# @File    : decorator.py
# @Software: PyCharm
# @Pyver   : 3.6.0

import datetime,time
import inspect

def timeit(fn):
    def _timeit(*args, **kwargs):
        befor = datetime.datetime.now()
        tmpfn = fn(*args,**kwargs)
        time = (datetime.datetime.now() - befor).total_seconds()
        print(time)
        return tmpfn
    return _timeit


def cache(fn):
    cache_key = {}
    def _cache(*args,**kwargs):
        params_dick = {}
        # args
        dick_args_key = inspect.signature(fn).parameters
        params_list = [ i for i in dick_args_key.keys()]
        for i,v in enumerate(args):
            params_dick[params_list[i]] = v
        # kwargs
        params_dick.update(kwargs)
        # default args
        for k,v in dick_args_key.items():
            if k not in params_dick.keys():
                params_dick[k] = v.default

        key = tuple(sorted(params_dick.items()))
        if key not in cache_key.keys():
            cache_key[key] = fn(*args,**kwargs)

        # tmpfn = fn(*args,**kwargs)
        return cache_key[key]
    return _cache

@timeit
@cache
def add(x,y):
    time.sleep(2)
    return x + y

@timeit
@cache
def fibonacci(a,b,num=30):
    time.sleep(4)
    fibonacci_list = [a,b]
    for i in range(0,num):
        a ,b = b ,a+b
        fibonacci_list.append(b)
    return fibonacci_list

print(fibonacci(1,1))
print(fibonacci(1,1))