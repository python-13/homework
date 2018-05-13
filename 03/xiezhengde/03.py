"""
第三次作业
将阿拉伯数字表示的一串整数(小于1万)转换成标准的中文货币表达式，单位为元:比如“1234”转化为"壹仟贰佰叁拾肆元",
“1001”转化成为"壹仟零壹元",
数字的中文对应：零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖","拾", "佰", "仟", "万"，请试着实验一下。
"""
dc = {0:"零",1:"壹",2:"贰",3:"叁",4:"肆",5:"伍",6:"陆",7:"柒",8:"捌",9:"玖"}
ls = []

print("input(0-9999)")
num = input(">>>").strip()
if num.isdigit():
    num=str(int(num))
    for i in num:
        ls.append(dc[int(i)])

    if len(num) == 4:
        print("{}仟{}佰{}拾{}元".format(ls[0],ls[1],ls[2],ls[3]))
    elif len(num) == 3:
        print("{}佰{}拾{}元".format(ls[0],ls[1],ls[2]))
    elif len(num) == 2:
        print("{}拾{}元".format(ls[0],ls[1]))
    else:
        print("{}元".format(ls[0]))
else:
    print("input Error!Enter（0-9999)")
    
# 逻辑上有点问题,测试下1000试试，看下是不是和预期的相符，在改改
