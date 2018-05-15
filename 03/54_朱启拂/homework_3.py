#!/usr/bin/env python3
# coding:utf-8

while True:
    num = int(input(":").strip())
    str_num = str(num)

    if len(str_num) >= 5:
        print("0 <= x <= 9999")
        exit()

    onesplace = int(num / 1 % 10)
    tensplace = int(num / 10 % 10)
    hundredsplace = int(num / 100 % 10)
    thousandsplace = int(num / 1000 % 10)

    num_key = {0: '零',
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

    yuan = '元'

    if len(str_num) == 4:
        # 1110
        if num_key[hundredsplace] != num_key[0] and num_key[tensplace] != num_key[0] and num_key[onesplace] == num_key[0]:
            print(num_key[thousandsplace] + num_list[2] + num_key[hundredsplace] +
                  num_list[1] + num_key[tensplace] + num_list[0] + yuan)
        # 110?
        elif num_key[hundredsplace] != num_key[0] and num_key[tensplace] == num_key[0]:
            # 1100
            if num_key[onesplace] == num_key[0]:
                print(num_key[thousandsplace] + num_list[2] + num_key[hundredsplace] +
                      num_list[1] + yuan)
            # 1101
            else:
                print(num_key[thousandsplace] + num_list[2] + num_key[hundredsplace] +
                      num_list[1] + num_key[0] + num_key[onesplace] + yuan)
        # 101?
        elif num_key[hundredsplace] == num_key[0] and num_key[tensplace] != num_key[0]:
            # 1010
            if num_key[onesplace] == num_key[0]:
                print(num_key[thousandsplace] + num_list[2] + num_key[0] +
                      num_key[tensplace] + num_list[0] + yuan)
            # 1011
            else:
                print(num_key[thousandsplace] + num_list[2] + num_key[0] +
                      num_key[tensplace] + num_list[0] + num_key[onesplace] + yuan)
        # 1000
        elif num_key[hundredsplace] == num_key[0] and num_key[tensplace] == num_key[0] and num_key[onesplace] == num_key[0]:
            print(num_key[thousandsplace] + num_list[2] + yuan)
        # 100? - 1001
        elif num_key[hundredsplace] == num_key[0] and num_key[tensplace] == num_key[0]:
            print(num_key[thousandsplace] + num_list[2] + num_key[0] + num_key[onesplace] + yuan)
        else:
            print(num_key[thousandsplace] + num_list[2] + num_key[hundredsplace] +
                  num_list[1] + num_key[tensplace] + num_list[0] + num_key[onesplace] + yuan)
    elif len(str_num) == 3:
        if num_key[tensplace] == num_key[0] and num_key[onesplace] == num_key[0]:
            print(num_key[hundredsplace] + num_list[1] + yuan)
        elif num_key[tensplace] == num_key[0] and num_key[onesplace] != num_key[0]:
            print(num_key[hundredsplace] + num_list[1] + num_key[tensplace] + num_key[onesplace] + yuan)
        elif num_key[tensplace] != num_key[0] and num_key[onesplace] == num_key[0]:
            print(num_key[hundredsplace] + num_list[1] + num_key[tensplace] + num_list[0] + yuan)
        else:
            print(num_key[hundredsplace] + num_list[1] + num_key[tensplace] + num_list[0] + num_key[onesplace] + yuan)
    elif len(str_num) == 2:
        if num_key[onesplace] == num_key[0]:
            print(num_key[tensplace] + num_list[0] + yuan)
        else:
            print(num_key[tensplace] + num_list[0] + num_key[onesplace] + yuan)
    else:
        print(num_key[onesplace] + yuan)
