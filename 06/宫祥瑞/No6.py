number = [8,3,3,1,2,5,4,7,6]
group = {2,3,5,7}

def sort_priority(number,group):
    s = list(filter(lambda x: x in group, number))
    d = list(filter(lambda x: x not in group, number))
    s.sort()
    d.sort()
    return s+d
num = sort_priority(number,group)
print(number)
print(num)