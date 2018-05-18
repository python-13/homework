str1 = '123'
def CustomInt(str1):
    """docstring"""
    Unitdict = {'1': 1, '2': 10, '3': 100, '4': 1000, '5': 10000, '6': 100000, '7': 1000000, '8': 10000000,
                '9': 100000000}
    Strdict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    count = 0
    sum = 0
    for i in str1:
        sum += Strdict[i] * Unitdict[str(len(str1) - count)]
        count += 1
    return sum

print(CustomInt(str1))
