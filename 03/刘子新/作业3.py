#!/usr/bin/env python  
# encoding: utf-8
d = {"1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}

numslist = list(input('please input your number：'))

s = []
for i in numslist:
    s += d[i]

print(type(s))

if len(s) == 3:
    s.insert(1,"佰")
    s.insert(3,"拾")
elif len(s) == 2:
    s.insert(1,"拾")
else:
    print(s)
s1 = "".join(s)

print(s1)