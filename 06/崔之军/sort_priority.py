number = [4, 7, 3, 5, 2, 6, 0, 1, 8, 9]
group = {3, 2, 5, 7}
def sort_priority(number1,group1):
    ret= [x for x in group1]
    for x in group:
       number1.remove(x)
    number1.sort()
    ret.extend(number1)
    global number
    number = ret
    return number
sort_priority(number,group)
print(number)