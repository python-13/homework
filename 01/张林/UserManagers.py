#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Date:2018-5-13
# Author:AreLIN
UserDict = {"AreLIN": {"age": "25", "phone": "110"},
            "Boy": {"age": "18", "phone": "120"},
            "Teacher": {"age": "18", "phone": "119"},
            "Studet": {"age": "20", "phone": "991"}
            }

UserChoseInfo = '''
************************
Please input your chose:
1. delete
2. update
3. find
4. list
5. exit
************************
'''
UserChoseList = {"1": "delete", "2": "update", "3": "find", "4": "list", "5": "exit"}

Flag = True
while Flag:
    UserChose = input(UserChoseInfo+"\n--->")
    if UserChose in UserChoseList.keys():
        if int(UserChose) == 1:
            print(UserDict)
            DeleteName = input("从上面的字典选择你要删除的用户名\n--->")
            if DeleteName in UserDict:
                del UserDict[DeleteName]
                print(UserDict)
            else:
                print("你选择的用户不存在")
                Flag = False

        elif int(UserChose) == 2:
            UpdateUser = input("用户名:年龄:联系方式\n--->")
            UpdateList = UpdateUser.split(":")
            if UpdateList[0] in UserDict.keys():
                UpdateChose = input("你所添加的用户已经存在，如果想更改请输入Yes,如果不添加请输入任意字符:\n--->")
                if UpdateChose == "Yes":
                    UserDict.update({UpdateList[0]: {"age": UpdateList[1], "Phone": UpdateList[2]}})
                else:
                    print("选择不更改原用户")
                    pass
            else:
                UserDict.update({UpdateList[0]: {"age": UpdateList[1], "Phone": UpdateList[2]}})
            print(UserDict)

        elif int(UserChose) == 3:
            FindName = input("请输入查找的用户名\n--->")
            if FindName in UserDict.keys():
                print({FindName: UserDict[FindName]})
        elif int(UserChose) == 4:
            print(UserDict)

        else:
            print("Good bye - * —")
            break

    else:
        print("You\'r chose is wrong,Please chose agin: %s" % UserChoseInfo)
