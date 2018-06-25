#!/usr/sbin/env python

number = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}


def sort_priority(number,group):
    s = list(filter(lambda x:x not in group, number))
    s.sort()
    g = list(group)
    g.sort()
    new_order_list = g + s
    return new_order_list


print(sort_priority(number,group))



def sort_pri(number, group):
    
    def _(x):
        return (0,x) if x in group else (1,x) 

    return sorted(number,key=_)

print(sort_pri(number, group))

# 你的还有另外一个变种的写法，尝试下试试，提示，元组排序
