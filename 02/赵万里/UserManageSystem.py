##################
# 用户管理
# week2 homework
##################



# 用户数据
dict = {"root": ["root", 20, 123456789,123456],
        "admin": ["rdmin", 19, 123456789, 123456],
        "tencent": ["tencent", 21, 123456789, 123456]}

# 提示信息
PromptInfo = """Friendly Reminder:
    1、Input String "delete", Express delete Element;
    2、Input String "update", Express update Element;
    3、Input String "find", Express find Element;
    4、Input String "list", Express list Element;
    5、Input String "exit", Express Exit; """


# 操作功能
def OperationFunc():

    OperCommand = ["delete", "update", "find", "list", "exit"]

    # 用户输入
    UserOperation = input("\33[31mPlease User Press Prompt Information Input:\33[0m \n").strip().lower()

    if UserOperation in OperCommand[:3]:
        FindCom = input("\33[31mPlease Input Find commend; If hava Multiple parameter, Please use ':' Split:\33[0m \n")
        FindCom = FindCom.split(":")

        # 删除操作
        if UserOperation == "delete":
            if FindCom[0] in dict.keys():
                dict[FindCom[0]].pop()
                print("\33[31mDelInfor: User {} Delete Success!\33[0m".format(FindCom[0]))
                return dict

        # 更新操作
        elif UserOperation == "update":
            if FindCom[0] in dict.keys():
                dict[FindCom[0]].clear()
                dict[FindCom[0]] = FindCom
                print("\33[31mUpdateInfo: User {} Update Success!\33[0m".format(FindCom[0]))
                return dict

            print(
                "\33[31m{}Info: User {} not existence! {} Fail\33[0m".format(UserOperation, FindCom[0], UserOperation))

            # 查找用户信息
        elif UserOperation == "find":
            if FindCom[0] in dict.keys():
                print("{:<10} {:<5} {:<10} {:<10}".format("name", "age", "tel", "Password"))
                print("{} {} {} {}".format('-' * 10, '-' * 5, '-' * 10, '-' * 10))
                print("{:<10} {:<5} {:<10} ".format(*dict[FindCom[0]][:len(FindCom[0])]) + "*" * len(str(dict[FindCom[0]][-1])))

        else:
            print("\33[31mEnter command Incorrect!\33[0m")


    # 打印用户信息
    elif UserOperation == "list":

        UserInput = input("\33[31mPlease input sort mode, default use name sort:\33[0m").strip().lower()
		
		# 选择不同排序
        if UserInput == "age":
            n = 1
        elif UserInput == "tel":
            n = 2
        else:
            n = 0

        print("按照{}排序:".format(UserInput))
        print("\33[31m{:<10} {:<5} {:<10} {:<10}\33[0m".format("name", "age", "tel", "Password"))
        print("{} {} {} {}".format('-' * 10, '-' * 5, '-' * 10, '-' * 10))

        for item in sorted(dict.values(), key=lambda x: x[n]):
            print("{:<10} {:<5} {:<10} ".format(*item[:len(item)]) + "*" * len(str(item[-1])))


    elif UserOperation == "exit":
        print("\33[31mInfo: Exit success!\33[0m")
        return

    else:
        print("\33[31mEnter command Incorrect!\33[0m")




def UserManageSystem():
    print(PromptInfo)

    count = 5
    while count:
        # User Input Login Info
        LoginName = input("\33[35mPlease Input Login Name\33[0m: \n ").strip().lower()
        LoginPassword = input("\33[35mPlease Input Login Password\33[0m: \n ").strip().lower()

        # Login check
        if LoginName in dict.keys() and int(LoginPassword) == dict[LoginName][-1]:
            print("\33[31mInfo：Login Seccess!\33[0m ")
            OperationFunc()
            break
        else:
            print("\33[31mLoginError: Login Fail !\33[0m")
            count -= 1
            continue



if __name__ == "__main__":
    UserManageSystem()

# 改成持久化存储试试 
