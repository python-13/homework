#!/usr/sbin/env python

def map_(func,*iterables):
    for i in zip(*iterables):
        yield func(*i)


def reduce_(func,seq,initial=None):
    if not seq and not initial:
        raise TypeError("{func_name}() of empty sequence with no initial value.".format(
            func_name='reduce_'))
    test = getattr(seq,'__iter__',None)
    if not test:
        raise TypeError("error: arg is not iterator")
    if initial == None:
        initial = seq[0].__class__() 
    for s in seq:
        initial += s
    return initial


def filter_(func,iterable):
    test = getattr(iterable,'__iter__',None)
    if not test:
        raise TypeError("error: arg is not iterator")
    for i in iterable:
        if func(i):
            yield i

# 厉害~考虑到了惰性
