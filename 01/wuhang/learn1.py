#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Description: learn dict in python how to use
# Author: whang
# QQ: 934946166
# ChangDate: 2018-05-12
# Only use python3
user_info = {
    "Jerry": "Age: 20, Contact Phone: 137xxxx1234",
    "Tom": "Age: 30, Contact Phone: 137xxxx2345",
}
operate_list = ["list", "find", "update", "del", "exit"]


def input_not_none(content):
    if content is not "":
        return True
    else:
        return False
        

def list_operate():
    for name, infor in user_info.items():
        print("Name: %s\nInformation: %s\n" % (name, infor))


def find_operate(find_name):
    if find_name in user_info:
        print("Name: ", find_name, "\nInformation:", user_info[find_name], "\n")
    else:
        print("Not found\n")


def update_operate(update_name):
    cut_info = update_name.split(':')
    if len(cut_info) == 3:
        if cut_info[0] in user_info:
            user_info[cut_info[0]] = "Age: " + cut_info[1] + " Contact Phone: " + cut_info[2]
            print("Update succeed.\nNew information:\n Name: %s\n %s\n" % (cut_info[0], user_info[cut_info[0]]))
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
