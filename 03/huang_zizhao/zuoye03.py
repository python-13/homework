#!/usr/bin/env python
import re


a = ("零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖")
b = [ str(x) for x in range(0,10) ]
c = ('',"拾", "佰", "仟", "万")
d = (-1,-2,-3,-4,-5)
num2cn = dict(zip(b,a))
unitMap = dict(zip(d,c))
print(num2cn,unitMap)
str_ori = input("Please Input A Number: ")
if not str_ori.isdigit() :
    print("Error: Input Must Be A Number.")
    exit(9)
if int(str_ori) > 99999:
    print("Error: Number Must Less Than 99999.")
    exit(9)
    
i = -len(str_ori)
new_str = ''
while i < 0:
    if str_ori[i] == '0':
        new_str = new_str + num2cn[str_ori[i]] 
    else:
        new_str = new_str + num2cn[str_ori[i]] + unitMap[i]
    i = i + 1

new_str = new_str.strip('零')
new_str = re.sub('零{2,}','零',new_str)
print(new_str)
