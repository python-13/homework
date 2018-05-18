import math
str1 = '123'
def CustomInt(str1):
    """docstring"""
    Strdict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    count = 1
    sum = 0
    for i in str1:
        sum += Strdict[i] * pow(10,len(str1)-count)
        count += 1
    return sum

print(CustomInt(str1))
