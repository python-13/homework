#!/usr/bin/env python3
# coding:utf-8

num = int(input(":"))
onesplace = int(num / 1 % 10)
tensplace = int(num / 10 % 10)
hundredsplace = int(num / 100 % 10)
thousandsplace = int(num / 1000 % 10)

print(thousandsplace, hundredsplace, tensplace, onesplace)

num_key = { 0: '零',
            1: '壹',
            2: '贰',
            3: '叁',
            4: '肆',
            5: '伍',
            6: '陆',
            7: '柒',
            8: '捌',
            9: '玖'}

num_list = ['十', '佰', '仟', '万']

print(num_key[thousandsplace], num_list[2],
      num_key[hundredsplace], num_list[1],
      num_key[tensplace], num_list[0],
      num_key[onesplace], "元")
