#!/usr/bin/env python3
# coding:utf-8
# 2018/04/24 15:55
# qifu.zhu

import json

data = {'朱启拂': {'age': 22, 'qq': '895653425'},
        '小智': {'age': 28, 'qq': '383290471'},
        '密斯李': {'age': 8, 'qq': '2465447965'},
        '豌豆': {'age': 8, 'qq': '1660809109'}}

menu = """
###############################
请输入序号选择对应功能:
1. delete
2. update
3. find
4. list
5. exit
###############################
"""

info_update = """
请按 用户名:年龄:QQ号码 格式输入信息 如:
     朱启拂:22:895653425
"""


def user_no_found(user_name):
    print("{0} 用户信息不存在!".format(user_name))


def f_check(user_name):
    if user_name in data.keys():
        return True
    else:
        return False


def f_delete(user_name):
    data.pop(user_name)
    print("{0} 用户信息删除成功!".format(user_name))


def f_update(user_name, age, qq):
    data.update({user_name: {'age': age, 'qq': qq}})
    print("{0} 用户信息更新成功!".format(user_name))


def main():
    while True:
        print(menu)
        select = input(": ")
        if select == '1':
            user_name = input("请输入用户名: ")
            if f_check(user_name=user_name) == True:
                f_delete(user_name=user_name)
            else:
                user_no_found(user_name=user_name)
        elif select == '2':
            print(info_update)
            info = input(": ")
            info_list = info.split(":")
            user_name = info_list[0]
            age = info_list[1]
            qq = info_list[2]
            if f_check(user_name=user_name) == True:
                f_update(user_name=user_name, age=age, qq=qq)
            else:
                user_no_found(user_name=user_name)
        elif select == '3':
            user_name = input("请输入用户名: ")
            if f_check(user_name=user_name) == True:
                if user_name in data.keys():
                    print(json.dumps(data[user_name], indent=4, ensure_ascii=False))
            else:
                user_no_found(user_name=user_name)
        elif select == '4':
            print(json.dumps(data, indent=4, ensure_ascii=False))
        elif select == '5':
            print('退出程序!')
            break


if __name__ == '__main__':
    main()
