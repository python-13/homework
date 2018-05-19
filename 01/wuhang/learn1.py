#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Description: learn dict in python how to use
# Author: whang
# QQ: 934946166
# ChangDate: 2018-05-12
# Only use python3
user_info = {
    "Jerry": "20, 137xxxx1234",
    "Tom": "30, 137xxxx2345",
}
operate_list = ["list", "find", "update", "del", "exit"]


def input_not_none(content):
    if content is not "":
        return True
    else:
        return False
        

def list_operate():
    for name, infor in user_info.items():
        information = infor.split(",")
        print("Name: %s\nInformation: Age: %s, ContactPhone:%s\n" % (name, information[0], information[1]))


def find_operate(find_name):
    if find_name in user_info:
        find_cut = user_info[find_name].split(",")
        print("Name: %s \nInformation: Age: %s, ContactPhone: %s\n" % (find_name, find_cut[0], find_cut[1]))
    else:
        print("Not found\n")


def update_operate(update_name):
    cut_info = update_name.split(':')
    if len(cut_info) == 3:
        if cut_info[0] in user_info:
            user_info[cut_info[0]] = cut_info[1] + ", " + cut_info[2]
            print("Update succeed.\nNew information:\n Name: %s\n Infora: Age: %s, ContactPhone: %s\n" % (cut_info[0], cut_info[1], cut_info[2]))
        else:
            print("Name not exist\n")
    else:
        print("Input fortmat error\n")


def del_operate(del_name):
    if del_name in user_info:
        del user_info[del_name]
        print("Del %s succeed\n" % del_name)
    else:
        print("Name not exist\n")


def to_run(run_method, run_info=None):
    if run_method == "exit":
        print("\nExit program\n")
        exit()
    elif run_method == "list":
        list_operate()
    elif run_method == "find":
        find_operate(find_name=run_info)
    elif run_method == "update":
        update_operate(update_name=run_info)
    elif run_method == "del":
        del_operate(del_name=run_info)


def to_operate():
    print("You can operate to %s metohd" % operate_list)
    operate = input("Please input operate: ")
    if input_not_none(content=operate):
        if (operate in operate_list and operate == "list") or  (operate in operate_list and operate == "exit"):
            to_run(run_method=operate)
        elif operate in operate_list:
            operate_detail = input("Please input name 'if update, format is <name>:<age>:<contactPhone>' : ")
            to_run(run_method=operate, run_info=operate_detail)
        else:
            print("Operate method not support\n")


if __name__ == "__main__":
    while True:
        to_operate()
# 完成得到很好
