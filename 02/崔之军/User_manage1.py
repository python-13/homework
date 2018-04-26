import sys
import getpass
user_data = {
    'Richard': [31, 13585996812,123456],
    'Betty': [32, 13970704984,123456],
    'James': [34, 13570013703,123456],
    'Dean': [24, 13973491230,123456],
    'Nick': [28, 13809659530,123456]
}
menu = '''
1.delete
2.update
3.list
4.find
5.exit
'''

def main():
    """docstring"""
    count = 3
    while 1:
        useranme = input('Enter user name: ').strip()
        passwd = input('Enter user password: ').strip()
        if count <= 1:
            print('Retry username or password more than three times ')
            break
        elif useranme in user_data and passwd == str(user_data[useranme][2]):
            print('\33[31mWelcome login\33[0m')
            dataOPerator()
        else:
            print('username or password is incorrect')
            count -= 1

def dataOPerator():
    """docstring"""
    while 1:
        print(menu)
        userInput = input('\33[31mEnter operation command\33[0m: ').strip()
        if userInput == 'delete':
            delUser = input('Enter user name: ').strip()
            print(delUser,'user is delete')
            user_data.pop(delUser)

        elif userInput == 'update':
            updateUser = input('\33[31mEnter user date such as user:age:tel\33[0m:').strip().split(':')
            if updateUser[0] in user_data:
                user_data[updateUser[0]] = updateUser[1:]
            else:
                print('\33[31musername is not exist\33[0m')
        elif userInput == 'list':
            userSort= input('\33[31m请输入排序方式默认按用户排序,按年龄排序请输入age\33[0m：').strip()
            print('{:<10} {:<5} {:<10} {:<10}'.format('User','Age','Tel','Password'))
            print('-'*10,'-'*5,'-'*10,'-'*10)
            #按名字排序
            if userSort == 'age':
                for i in sorted(user_data.items(), key=lambda x: x[1][0], reverse=False):
                    print('{:<10} {:<5} {:<10}'.format(i[0], *i[1]),'*'*len(str(i[1][2])))
            #按年龄排序
            else:
                for i in sorted(user_data.items(), key=lambda x: x, reverse=False):
                    print('{:<10} {:<5} {:<10}'.format(i[0], *i[1]),'{:<10}'.format('*'*len(str(i[1][2]))))

        elif userInput == 'find':
            findUser = input('Enter user:').strip()
            if findUser in user_data:
                print(findUser, '{:<2} {}'.format(*user_data[findUser]),'{}'.format('*'*len(str(user_data[findUser][2]))))
        elif userInput == 'exit':
            print('\33[31mProgram will be exit\33[0m')
            sys.exit()
        else:
            print('Enter command Incorrect')

if __name__ == '__main__':
    main()
