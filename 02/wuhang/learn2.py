#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Description: dict, input, split, strip, replace, md5
# Author: whang
# ChangDate: 2018-05-12
# Only use python3
import hashlib
user_info = {
    "Jerry": "20, 13767671234, jerry@passwd",
    "Tom": "30, 13778782345, tom@passwd",
    "Betta": "67, 18909128999, betta@passwd",
    "Schuck": "55, 18909008999, schuck@passwd",
    "Tim": "55, 18909008123, tim@passwd",
}
operate_list = ["list", "list-sort", "find", "update", "del", "exit"]


# 判断传入值是否为空
def input_not_none(content):
    if content is not "":
        return True
    else:
        return False


# 密码验证
def passwd_check(user):
    input_passwd = input("Please input passwd to verify: ")
    if input_not_none(content=input_passwd):
        get_infor = user_info[user].split(",")
        get_passwd = get_infor[2].strip()
        encrypt_passwd = hashlib.md5(get_passwd.encode("utf-8")).hexdigest()
        contrast_passwd = hashlib.md5(input_passwd.encode("utf-8")).hexdigest()
        if encrypt_passwd == contrast_passwd:
            return True
        else:
            return False


# 根据关键字排序
'''
1. 创建空字典
2. 循环从排序关键字列表中取出值，将其与user_info中保存的信息对比
3. 为避免有关键字排序重复，将其存入新的key，不存在新的key内，则打印
4. 清空字典
'''
def sort_by_key(sort_key, sort_list):
    sort_dict = {}
    for get_sort_key in sort_list:
        for get_k, get_v in user_info.items():
            cut_v = get_v.split(",")
            if sort_key == "age":
                result_sort_key = cut_v[0].strip()
                if result_sort_key == get_sort_key:
                    corresponding_infor1 = cut_v[1].strip()
                    corresponding_passwd = cut_v[2].strip()
                    if get_k not in sort_dict:
                        sort_dict[get_k] = [result_sort_key, corresponding_infor1]
                        dis_passwd = corresponding_passwd.replace(corresponding_passwd, "*" * len(corresponding_passwd))
                        print("Name: %s, Age: %s, ContactPhone:%s, Password: %s\n" % (get_k, sort_dict[get_k][0], sort_dict[get_k][1], dis_passwd))
            elif sort_key == "phone":
                result_sort_key = cut_v[1].strip()
                if result_sort_key == get_sort_key:
                    corresponding_infor1 = cut_v[0].strip()
                    corresponding_passwd = cut_v[2].strip()
                    if get_k not in sort_dict:
                        sort_dict[get_k] = [corresponding_infor1, result_sort_key]
                        dis_passwd = corresponding_passwd.replace(corresponding_passwd, "*" * len(corresponding_passwd))
                        print("Name: %s, Age: %s, ContactPhone:%s, Password: %s\n" % (get_k, sort_dict[get_k][0], sort_dict[get_k][1], dis_passwd))
            else:
                print('Not support sort by "%s"\n' % sort_key)
    sort_dict.clear()


'''
1. 创建空列表
2. 将所有可用于排序信息取出，赋值到列表中
3. 判断相应排序关键字进行跳转
'''
def list_operate(sort_key_name="name"):
    name = []
    age = []
    phone = []
    for get_name, get_content in user_info.items():
        cut_content = get_content.split(",")
        get_age = cut_content[0].strip()
        get_phone = cut_content[1].strip()
        age.append(get_age)
        phone.append(get_phone)
        name.append(get_name)
    age.sort()
    phone.sort()
    name.sort()
    if sort_key_name == "name":
        for result in name:
            result_infor = user_info[result]
            cut_result_infor1 = result_infor.split(",")
            passwd_infor = cut_result_infor1[2].strip()
            dis_passwd = passwd_infor.replace(passwd_infor, "*" * len(passwd_infor))
            print("Name: %s, Age: %s, ContactPhone:%s, Password: %s\n" % (result, cut_result_infor1[0].strip(), cut_result_infor1[1].strip(), dis_passwd))
    elif sort_key_name == "age":
        sort_by_key("age", age)
    elif sort_key_name == "phone":
        sort_by_key("phone", phone)
    else:
        print('Not support sort by "%s"\n' % sort_key_name)


def find_operate(find_name):
    if find_name in user_info:
        find_cut = user_info[find_name].split(",")
        passwd = find_cut[2].strip()
        dis_passwd = passwd.replace(passwd, "*" * len(passwd))
        print("Name: %s \nInformation: Age: %s, ContactPhone: %s, Password: %s\n" % (find_name, find_cut[0], find_cut[1], dis_passwd))
    else:
        print("Not found\n")


def update_operate(update_name):
    cut_info = update_name.split(':')
    if len(cut_info) == 3:
        if cut_info[0] in user_info:
            if passwd_check(user=cut_info[0]):
                print("Passwod verification")
                old_infor = user_info[cut_info[0]].split(",")
                old_passwd = old_infor[2].strip()
                user_info[cut_info[0]] = cut_info[1] + ", " + cut_info[2] + ", " + old_passwd
                dis_passwd = old_passwd.replace(old_passwd, "*" * len(old_passwd))
                print("Update succeed.\nNew information:\n Name: %s\n Infora: Age: %s, ContactPhone: %s, Password: %s\n" % (cut_info[0], cut_info[1], cut_info[2], dis_passwd))
            else:
                print("Password error")
        else:
            print("Name not exist\n")
    else:
        print("Input fortmat error\n")


def del_operate(del_name):
    if del_name in user_info:
        if passwd_check(user=del_name):
            print("Passwod verification")
            del user_info[del_name]
            print("Del %s succeed\n" % del_name)
        else:
            print("Password error")
    else:
        print("Name not exist\n")


def to_run(run_method, run_info=None):
    if run_method == "exit":
        print("\nExit program\n")
        exit()
    elif run_method == "list-sort":
        list_operate(sort_key_name=run_info)
    elif run_method == "find":
        find_operate(find_name=run_info)
    elif run_method == "update":
        update_operate(update_name=run_info)
    elif run_method == "del":
        del_operate(del_name=run_info)


def to_operate():
    print("You can operate to %s metohd\n\
    (***Notify: Default list sort by 'name', You can use sort by key is 'age' or 'phone', format is <list-sort> -> <sortKey>\n\
    \tif update, format is <name>:<age>:<contactPhone>***)" % operate_list)
    operate = input("Please input operate: ")
    if input_not_none(content=operate):
        if operate in operate_list and operate == "exit":
            to_run(run_method=operate)
        elif operate in operate_list and operate == "list":
            list_operate()
        elif operate in operate_list:
            operate_detail = input("Please Input operate method format: ")
            to_run(run_method=operate, run_info=operate_detail)
        else:
            print("Operate method not support\n")


if __name__ == "__main__":
    while True:
        to_operate()

