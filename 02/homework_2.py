user_dict = {'liang':{'age':'18','tel':'111111','passwd':'123123'},
             'bing':{'age':'20','tel':'222222','passwd':'123123'},
             'wen':{'age':'22','tel':'333333','passwd':'123123'}
                }
def user_help():
    print("Enter 'delete' delete user; \n"
          "Enter 'update' to update the user; \n"
          "Enter 'find' find user; \n"
          "Enter 'list' to print all users; \n"
          "Enter 'exit' to exit the program; \n"
          "Enter 'help' for help")

def user_delete():
    key = input('Please enter the username to delete: ')
    if user_dict.get(key):
        user_dict.pop(key)
        print('User {} deleted successfully!'.format(key))
    else:
        print('The user does not exist!')

def user_update():
    print("Please enter 'username:age:tel:password':")
    user_info = input()
    user_list = user_info.split(':')
    if user_dict.get(user_list[0]):
        print('User already exists, modify user information? Y/N')
        flag = input()
        if flag == 'Y' or flag == 'y':
            temp = {user_list[0]: {'age': user_list[1], 'tel': user_list[2], 'passwd': user_list[3]}}
            user_dict.update(temp)
            print("'{}' user information update completed!".format(user_list[0]))
        else:
            return
    else:
        temp = {user_list[0]: {'age': user_list[1], 'tel': user_list[2], 'passwd': user_list[3]}}
        user_dict.update(temp)
        print("'{}' user information update completed!".format(user_list[0]))

def user_print():
    print('User information can be sorted by (name, age, tel fields),The default sort field is name')
    user_list = list(user_dict.items())
    user_list.sort(key=lambda x: x[0])
    for i in user_list:
        print('username:', i[0])
        temp = i[1].copy()
        temp['passwd'] = len(temp['passwd']) * '*'
        print('userinfo: ', temp)

    flag = input('If you need to sort, please enter the sort field(age、tel), otherwise press the Enter key directly: ')
    if flag == 'age' or flag == 'tel':
        user_list.sort(key=lambda x: x[1][flag])
        for i in user_list:
            print('username:', i[0])
            temp = i[1].copy()
            temp['passwd'] = len(temp['passwd']) * '*'
            print('userinfo: ', temp)
    else:
        return

def user_find():
    print('Please enter user name: ')
    username = input()
    if user_dict.get(username):
        print('username: {}'.format(username))
        temp = user_dict[username].copy()
        temp['passwd'] = len(temp['passwd']) * '*'
        print('userinfo: {}'.format(temp))
    else:
        print('The user does not exist!')

def user_auth():
    times = 5
    while True:
        username = input('Please enter the username:')
        if user_dict.get(username):
            if times:
                password = input('Please enter the password:')
                if password == user_dict[username]['passwd']:
                    print('The authentication is successful, please follow the prompts to continue your operation.')
                    return True
                else:
                    times -= 1
                    if times:
                        print('The password is wrong, you have {} chances, please re-enter:'.format(times))
                    else:
                        print('Too many password errors, the program exits')
                        break
        else:
            times -= 1
            if times:
                print('The user does not exist! please enter again')
            else:
                print('Too many errors, the program exits!')
                break

def main():
    if user_auth():
        print('Please enter the username and password as prompted:')
        user_help()
        while True:
            print('Please enter your options: ')
            operating = input()
            if operating == 'delete':
                user_delete()

            elif operating == 'update':
                user_update()

            elif operating == 'find':
                user_find()

            elif operating == 'list':
                user_print()

            elif operating == 'help':
                user_help()

            elif operating == 'exit':
                break

if __name__ == "__main__":
    main()
