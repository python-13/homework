from functools import wraps
import time
import datetime
def timeit(fn):
    @wraps(fn)
    def wrappper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret

    return wrappper


@timeit
def add(x, y):
    return x + y


print(add(4, 5))
