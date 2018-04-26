#!/usr/bin/env python3
# coding:utf-8
# 2018/04/24 15:55
# qifu.zhu

import json
import hashlib
import getpass

#passwd = 123
data = {'朱启拂': {'age': 22, 'qq': '895653425', 'passwd': '202cb962ac59075b964b07152d234b70'},
        '小智': {'age': 28, 'qq': '383290471', 'passwd': '202cb962ac59075b964b07152d234b70'},
        '密斯李': {'age': 8, 'qq': '2465447965', 'passwd': '202cb962ac59075b964b07152d234b70'},
        '豌豆': {'age': 8, 'qq': '1660809109', 'passwd': '202cb962ac59075b964b07152d234b70'}}

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
请按 用户名:年龄:QQ号码:密码 格式输入信息 如:
     朱启拂:22:895653425:123
"""


def user_no_found(user_name):
    print("{0} 用户信息不存在!".format(user_name))


def passwd_error(user_name):
    print("{0} 用户密码错误!".format(user_name))


def f_check(user_name):
    if user_name in data.keys():
        return True
    else:
        return False


def f_delete(user_name):
    data.pop(user_name)
    print("{0} 用户信息删除成功!".format(user_name))


def f_update(user_name, age, qq, passwd):
    hl = hashlib.md5()
    hl.update(passwd.encode(encoding='utf-8'))
    passwd = hl.hexdigest()
    data.update({user_name: {'age': age, 'qq': qq, 'passwd': passwd}})
    print("{0} 用户信息更新成功!".format(user_name))


def f_check_passwd(user_name, passwd):
    hl = hashlib.md5()
    hl.update(passwd.encode(encoding='utf-8'))
    if hl.hexdigest() == data[user_name]['passwd']:
        return True
    else:
        return False


def main():
    while True:
        print(menu)
        select = input(": ")
        if select == '1':
            user_name = input("请输入用户名: ")
            if f_check(user_name=user_name) == True:
                passwd = getpass.getpass("请输入密码: ")
                if f_check_passwd(user_name=user_name, passwd=passwd):
                    f_delete(user_name=user_name)
                else:
                    passwd_error(user_name=user_name)
            else:
                user_no_found(user_name=user_name)
        elif select == '2':
            print(info_update)
            info = input(": ")
            info_list = info.split(":")
            user_name = info_list[0]
            age = info_list[1]
            qq = info_list[2]
            passwd_new = info_list[3]
            if f_check(user_name=user_name) == True:
                passwd = getpass.getpass("请输入密码: ")
                if f_check_passwd(user_name=user_name, passwd=passwd):
                    f_update(user_name=user_name, age=age, qq=qq, passwd=passwd_new)
                else:
                    passwd_error(user_name=user_name)
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
            #print(json.dumps(data, indent=4, ensure_ascii=False))
            for i in data.items():
                print(i)
            tag = input("按哪一列排序(name、age、qq): ")
            data_list = list(data.items())
            if tag == 'name':
                data_list.sort(key=lambda x: x[0])
                for i in data_list:
                    print(i)
            elif tag == 'age' or tag == 'qq':
                data_list.sort(key=lambda x: x[1][tag])
                for i in data_list:
                    print(i)
            else:
                print("无效的列名!")
        elif select == '5':
            print('退出程序!')
            break


if __name__ == '__main__':
    main()
# 代码不错，除了注释，还是尽量不要用中文
