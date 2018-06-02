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
    
