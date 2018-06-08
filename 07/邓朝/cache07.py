import datetime
def cache(fn):
    intcache={}
    def _cache(args):
        if intcache.get(args) is None:
            result=fn(args)
            intcache[args]=result
        else:
            result=intcache[args]
        return result
    return _cache

@cache
def fn1(x):
    if x==1 or x==2:
        return 1
    return fn1(x-1) + fn1(x-2)

while True:
    int1=input('输入位数:')
    if int1.isdigit():
        start=datetime.datetime.now().timestamp()
        print('结果:{}\n消耗时间:{}秒'.format(fn1(int(int1)),datetime.datetime.now().timestamp()-start))
    else:
        print('错误输入')
        continue
