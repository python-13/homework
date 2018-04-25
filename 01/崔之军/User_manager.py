import sys
user_data = {
    'Richard': [31, 13585996812],
    'Betty': [32, 13970704984],
    'James': [34, 13570013703],
    'Dean': [24, 13973491230],
    'Nick': [28, 13809659530]
}

while 1:
    userInput = input('\33[31mEnter operation command\33[0m: ').strip()
    if userInput == 'delete':
        delUser = input('Enter user name: ').strip()
        user_data.pop(delUser)
    elif userInput == 'update':
        updateUser = input('\33[31mEnter user date such as user:age:tel\33[0m:').strip().split(':')
        if updateUser[0] in user_data:
            user_data[updateUser[0]] = updateUser[1:]
        else:
            print('\33[31musername is not exist\33[0m')
    elif userInput == 'list':
        print('{:<10} {:<10} {}'.format('User','Age','Tel'))
        print('-'*32)
        for key in user_data:
            print('{:<10}{:<10} {}'.format(key,*user_data[key]))
    elif userInput == 'find':
        findUser = input('Enter user:').strip()
        if findUser in user_data:
            print(findUser, '{:<10} {}'.format(*user_data[findUser]))
    elif userInput == 'exit':
        print('\33[31mProgram will be exit\33[0m')
        sys.exit()
    else:
        print('Enter command Incorrect')