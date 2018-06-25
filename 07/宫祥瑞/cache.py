import time
import inspect
from functools import wraps
import datetime

def my_cache(duration):
    def _cache(fn):
        local_cache = {}

        @wraps(fn)
        def wrapper(*args,**kwargs):
            #过期的key
            expire_keys = []
            for k,(_,stamp) in local_cache.items():
                now =datetime.datetime.now().timestamp()
                if now - stamp >duration:
                    expire_keys.append(k)
            for k in expire_keys:
                local_cache.pop(k)

            #参数处理，构建key
            sig = inspect.signature(fn)
            params = sig.parameters

            param_names = [key for key in params.keys()]
            params_dict = {}

            for i,v in enumerate(args):
                k = param_names[i]
                params_dict[k] = v

            params_dict.update(kwargs)

            for k,v in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = v.default

            key = tuple(sorted(params_dict.items()))

            if key not in local_cache.keys():
                local_cache[key] = (fn(*args,**kwargs),
                datetime.datetime.now().timestamp())

            return local_cache[key][0]

        return wrapper
    return _cache

@my_cache(10)
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(100))
print([fib(x) for x in range(60)])