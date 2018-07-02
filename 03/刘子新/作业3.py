#!/usr/bin/env python  
# encoding: utf-8

d = {"1":"壹","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}

numslist = list(input('please enter an integer：'))

if len(numslist) >= 5:
    
    print(' your number should be less than 10000')
    
else:   
    s = []

    for i in numslist:
    
    s += d[i]
    
    if len(s) == 4:
        s.insert(1,"仟")
        s.insert(3,"佰")
        s.insert(5,"拾")
        s.append('元')

    elif len(s) == 3:
        s.insert(1,"佰")
        s.insert(3,"拾")
        s.append("元")

    elif len(s) == 2:
        s.insert(1,"拾")
        s.append("元")         
    
    else:
        print(s)
        
    s1 = "".join(s)

    print(s1)

