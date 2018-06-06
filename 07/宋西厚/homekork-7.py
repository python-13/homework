import time
import logging
from functools import wraps,lru_cache
FORMAT = '%(message)s'
logging.basicConfig(level=logging.INFO,format=FORMAT)

def timeit(fn):
    import datetime
    @wraps(fn)
    def inner(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now()-start).total_seconds()
        logging.info("func:{} timeit:{} return value:{}".format(fn.__name__,delta,ret))
        return ret
    return inner

def timeit_parame(n):
    import datetime
    def inner(fn):
        @wraps(fn)
        def dec(*args,**kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            logging.info("func:{} timeit:{} return value:{}".format(fn.__name__, delta,ret))
            return ret
        return dec
    return inner



@timeit_parame(1)
@timeit #add = timeit(add)
def add(x,y) :
    time.sleep(2)
    return x+y

add(4,6)


def cache_owe(fn):
    dic = {}
    def inner(x):
        if x in dic:
            return dic[x]
        else:
            ret = fn(x)
            dic[x] = ret
            return ret
    return inner

@cache_owe
def fn(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fn(x-1)+fn(x-2)

print(fn(500))













