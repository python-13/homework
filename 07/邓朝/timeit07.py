def timeit(number):
    def _timeit(fn):
        import datetime
        def _wapper(*args,**kwargs):
            start=datetime.datetime.now().timestamp()
            for _ in range(number):
                result=fn(*args,**kwargs)
            print('函数{},执行{}次,共用时{}秒'.format(fn.__name__,number,datetime.datetime.now().timestamp()-start))
            return result
        return _wapper
    return _timeit

import time
@timeit(10)
def fn1(dalaytime:int):
    time.sleep(dalaytime)
    return

fn1(0.2)




