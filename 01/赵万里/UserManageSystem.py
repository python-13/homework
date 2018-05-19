dict = {"zhao":["zhao", 20, 123456789], "liming":["liming", 19, 456978256]}


def UserManageSystem():
    print("""
    friendly reminder:
        1、input string "delete", express delete element;
        2、input string "update", express update element;
        3、input string "find", express find element;
        4、input string "list", express list element;
        5、input string "exit", express exit;
    """)

    user_input = input("User input: \n ").strip().lower()


    if user_input == "delete":
        print("primary data: {}".format(dict))
        user_name = input("please input User name: \n ").strip().lower()
        dele = dict.pop(user_name, "{} user data not existence！".format(user_name))
        print(" {}\n delete data dict: {}".format(dele, dict))


    if user_input == "update":
        UsernameAgeInfo = input(" please input name, age, contact information, use '：' split！ \n").strip().lower()
        UserName, age, info = UsernameAgeInfo.split(":")
        if dict.get(UserName):
            dict[UserName] = [UserName, age, info]
            print("{} user data update success!".format(UserName))
        else:
            print("{} user data not existence!".format(UserName))


    if user_input == "find":
        UserFindInfo = input(" please input user name: \n").strip().lower()
        print("user {} information is: {} ".format(UserFindInfo, dict.get(UserFindInfo, None)))


    if user_input == "list":
        for k,v in dict.items():
            print(" User name: {} \n  User Infomation: {}\n".format(k,v))


    if user_input == "exit":
        print("exit success!")
        return


if __name__ == "__main__":
    UserManageSystem()