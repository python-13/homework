# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 17:21
# @Author  : armo
# @File    : NumToChinese.py
# @Software: PyCharm
# @Pyver   : 3.6.0

import re
# 前置0将数字补齐5位数,直接转换为汉字，并添加单位
def Num2Chinese(num):
    numstr = str(num)
    strlen = len(numstr)
    numdict = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍','6':'陆','7':'柒','8':'捌','9':'玖','0':'零' ,'10':'拾','100':'佰','1000':'仟','10000':'万'}
    if strlen == 1:
        return numdict[numstr]
    else:
        chstr = ""
        for i in numstr:
            chstr += numdict[i]
        while len(chstr) != 5:
            chstr = numdict['0'] + chstr
        unitstr = chstr[0] + numdict['10000'] + chstr[1] + numdict['1000'] + chstr[2] + numdict['100'] + chstr[3] + numdict['10'] + chstr[4]
        return unitstr

# 处理各种0情况
def del0(unitstr):
    # 删除前置0
    while unitstr[0] == '零':
        unitstr = unitstr[2:]
    # 删除后置0
    if unitstr[-1] == '零':
        unitstr = unitstr[:-1]
        while unitstr[-2] == '零':
            unitstr = unitstr[:-2]
    # 替换字符串中间 "[零][拾佰仟万]" 和 "[零]"
    rr = re.compile("[零][拾佰仟万]")
    rrresult = rr.findall(unitstr)
    for i in  rrresult:
        unitstr = unitstr.replace(i,"零")
    while unitstr.find("零零") != -1:
        unitstr =unitstr.replace("零零", "零")
    return unitstr

if __name__ == '__main__':
    while True:
        num = input("请输入1-5位数:\n")
        if int(num) < 10:
            unitstr = Num2Chinese(num)
            print("结果: %s元" %unitstr)
        elif len(num) < 6:
            unitstr = Num2Chinese(num)
            result = del0(unitstr)
            print("结果: %s元" %result)
        else:
            print("输入错误!\n")
            continue