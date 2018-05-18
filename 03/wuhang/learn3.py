#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description: conversion
# Author: whang
# QQ: 934946166
# ChangeDate: 2018-05-16


conversion_num = {"0": "零", "1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌", "9": "玖"}
conversion_embellish = ("整", "元", "拾", "佰", "仟", "万", "拾", "佰", "仟", "亿")


'''
1. 尝试是否可以将输入的内容转换为int类型
2. 循环将每次取出一个字符，并从conversion_num中对应到中文转换
3. 不能超过亿单位，首字母不能为0
4. 出现0并且在末位时，添加"元"修饰
5. 出现0并且非在末位时，添加单位修饰("拾", "佰", "仟", "万", "拾", "佰", "仟", "亿")，并记录0的出现
6. 循环到末位且0统计变量有增加，则在中间添加"零"修饰，并正确追加末位数字转换返回
7. 1-9数字正常转换及单位修饰追加
'''
def conversion_func():
    input_content = input("Please input conversion quantity of money: ")
    try:
        # try, int(input_content) to content variable
        content = int(input_content)
        conversion = {"assmebly": ""}
        unit_start = 1
        zero_count = 1
        unit_decrease = len(input_content)
        for money_number in input_content:
            if unit_start == 1 and int(money_number) == 0 and len(input_content) <= 9:
                print("WARN: Please don't start with 0, and don't exceed a hundred mill unit")
            else:
                if unit_start > 1 and int(money_number) == 0:
                    if unit_start == len(input_content) and unit_decrease == 1:
                        conversion["assmebly"] = conversion["assmebly"] + conversion_embellish[unit_decrease]
                    elif unit_start != len(input_content):
                        conversion["assmebly"] = conversion["assmebly"] + conversion_embellish[unit_decrease]
                        unit_decrease -= 1
                        unit_start += 1
                        zero_count += 1
                    elif unit_start == len(input_content):
                        conversion["assmebly"] = conversion["assmebly"] + conversion_num[money_number] + conversion_embellish[unit_decrease]
                        unit_decrease -= 1
                        unit_start += 1
                elif unit_start == len(input_content) and zero_count != 1:
                    conversion["assmebly"] = conversion["assmebly"] + conversion_num["0"] + conversion_num[money_number] + conversion_embellish[unit_decrease]
                else:
                    conversion["assmebly"] = conversion["assmebly"] + conversion_num[money_number] + conversion_embellish[unit_decrease]
                    unit_decrease -= 1
                    unit_start += 1
                    zero_count = 1
        conversion["assmebly"] = conversion["assmebly"] + conversion_embellish[0]
        return conversion["assmebly"]
    except ValueError:
        print("ERROR: Input type error, Only support integer")
    except:
        print("ERROR: Unknown error, Please by fortmat to input")


if __name__ == "__main__":
    result = conversion_func()
    if result != None:
        print(result)


# 暂有bug，请勿批改
