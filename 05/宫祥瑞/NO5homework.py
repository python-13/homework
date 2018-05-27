from functools import reduce

def mymap(func,*args):
    if isinstance(*args,(list,tuple,dict,str,set,bytearray,bytes)):
        for arg in zip(*args):
            yield func(*arg)
def myfilter(func,args):
    if isinstance(args, (list, tuple, dict, str, set, bytearray, bytes)):
        for arg in args:
            if  func(arg) :
                yield arg
    else:
        raise TypeError("error: arg is not iterator")


def myreduce(func, *args):
    """ 
    reduce(func, [1, 2, 3]) = func(func(1, 2), 3)
    待解决 思路 递归
    """



def add(x):
    return x*x
ints = list(map(add,[1,2,3,4,5,6,7,8,9]))
inta = list(mymap(add,[1,2,3,4,5,6,7,8,9]))


def fn(x):
    return x%3!=0

res =list(filter(fn,[1,2,3,4,5,6,7,8,9]))
res1 =list(myfilter(fn,[1,2,3,4,5,6,7,8,9]))
def muti(x,y):
    return x*y
ret = reduce(muti, [1,3,5,7,9])
#ret1 = myreduce(fn1, [1,3,5,7,9])


print(ints,inta,res,res1,ret)