user_dict = {'liang':{'age':'18','phone':'111111'},
             'bing':{'age':'20','phone':'222222'},
             'wen':{'age':'22','phone':'333333'}
                }
print("Enter 'delete' delete user; \n"
      "Enter 'update' to update the user; \n"
      "Enter 'find' find user; \n"
      "Enter 'list' to print all users; \n"
      "Enter 'exit' to exit the program")

while True:
    print('Please enter your options: ')
    operating = input()
    if operating == 'delete':
        key = input('Please enter the username to delete: ')
        if user_dict.get(key):
            user_dict.pop(key)
            print('User {} deleted successfully'.format(key))
        else:
            print('The user does not exist!')
            continue

    elif operating == 'update':
        print("Please enter 'username:age:contact':")
        user_info = input()
        if user_dict.get(user_info.split(':')[0]):
            user_list = user_info.split(':')
            temp = {user_list[0]:{'age':user_list[1], 'contact':user_list[2]}}
            user_dict.update(temp)
            print("'{}' user information update completed!".format(user_list[0]))

        else:
            print('The user does not exist!')
            continue

    elif operating == 'find':
        print('Please enter user name: ')
        username = input()
        if user_dict.get(username):
            print('username: {}'.format(username))
            print('userinfo: {}'.format(user_dict[username]))
        else:
            print('The user does not exist!')

    elif operating == 'list':
        for key in user_dict:
            print('username:', key)
            print('userinfo: ', user_dict[key])

    elif operating == 'exit':
        break
