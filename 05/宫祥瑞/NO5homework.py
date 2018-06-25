from functools import reduce

def mymap(func,*args):
    if isinstance(*args,(list,tuple,dict,str,set,bytearray,bytes)):
        for arg in zip(*args):
            yield func(*arg)
    else:
        raise TypeError("error: arg is not iterator")
def myfilter(func,args):
    if isinstance(args, (list, tuple, dict, str, set, bytearray, bytes)):
        for arg in args:
            if  func(arg) :
                yield arg
    else:
        raise TypeError("error: arg is not iterator")


def myreduce(fnc, seq):
    #reduce(func, [1, 2, 3]) = func(func(1, 2), 3)
    if isinstance(seq, (list, tuple, dict, str, set, bytearray, bytes)):
        tally = seq[0]
        for next in seq[1:]:
            tally = fnc(tally, next)
        return tally
    else:
        raise TypeError("error: arg is not iterator")

def add(x):
    return x*x
ints = list(map(add,[1,2,3,4,5,6,7,8,9]))
inta = list(mymap(add,[1,2,3,4,5,6,7,8,9]))

def fn(x):
    return x%3!=0
res =list(filter(fn,[1,2,3,4,5,6,7,8,9]))
resa =list(myfilter(fn,[1,2,3,4,5,6,7,8,9]))

def muti(x,y):
    return x*y
ret = reduce(muti, [1,3,5,7,9])
rets = myreduce(muti, [1,3,5,7,9])


print(ints,inta,res,resa,ret,rets)

# 写的不错，下次分享的时候的，可以聊聊对高阶函数的认识
