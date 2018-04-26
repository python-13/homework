#!/usr/bin/env python
import readline
import getpass

user_dict=dict()
user_dict = {
    "admin": { 'userName': 'admin', 'age': 28, 'tel': '123', 'password': '123456' },
    "hzz": { 'userName': 'hzz', 'age': 27, 'tel': '123', 'password': '123456' },
    "lhr": { 'userName': 'lhr', 'age': 25, 'tel': '456', 'password': '123456' },
    "hzy": { 'userName': 'hzy', 'age': 27, 'tel': '789', 'password': '123456' },
}
global login_status
login_status = False
def input_(p):
    return input(p).strip(' ')

def login(func):

    def wrapper():
        userName = input_("Login: ")
        passwd = getpass.getpass("Password: ")
        if user_dict.get(userName) is not None:
            if passwd == user_dict.get(userName).get('password'):
                login_status = True
            else:
                print("Warning: {u} Login Failed.".format(u=userName))
                return help_()
        else:
            print("Warning: {u} Not Exist.".format(u=userName))
            return help_()
        return func()
    return wrapper 
        

def acquire():
    userNamePattern = input_("Pls Input UserName Pattern: ")
    users = user_dict.keys()
    user_match = [ u for u in users if userNamePattern in u ]
    for userName in user_match:
        string = "UserName: {:<15s} Age: {:<3} Tel: {:<11s} Password: {:<10}".format(user_dict.get(userName).get('userName'),
            user_dict.get(userName).get('age'), user_dict.get(userName).get('tel'), 
            '*' * len(user_dict.get(userName).get('password')))
        print(string)
    print()

@login
def remove():
    userName = input_("Pls Input UserName Which To Be Remove: ")
    if user_dict.get(userName) is None:
        print("Warning: {u:<15s} Not Exist.".format(u=userName))
        return None
    else:
        userInfo = user_dict.pop(userName)
        print("Delete User: {u:<15s}".format(u=userName))
        return userInfo

@login
def update_():
    info = input_("Update User, Pls Input User Info: ")
    info_ = info.split(':')
    userName = info_[0]
    if userName == 0: 
        return None
    if user_dict.get(userName) is None:
        print("Warning: {u:<15s} Not Exist.".format(u=userName))
        return None
    key_ = ["username",'age','tel']
    tmp = zip(key_, info_)
    user_dict.setdefault(info_[0],{}).update(tmp)
    string = "User {u} Info Updated : Age:{a} Tel:{t}".format(u=userName,
        a=user_dict.get(userName).get('age'), 
        t=user_dict.get(userName).get('tel'))
    print(string)


def show():
    field = input("Sorted By Which filed userName, age , tel, or password: ")
    print("{:<20s}{:<8s}{:<18s}{:<20}".format("UserName","Age","Tel","Password"))
    for info in sorted(user_dict.values(),key=lambda x: x[field]):
        userName = info.get('userName')
        age = info.get('age')
        tel = info.get('tel')
        password = info.get('password')
        print("{:<20}{:<8}{:<18}{:<20}".format(userName, age, tel, '*' * len(password)))
    return


def help_():
    prom_1 = "{d: <10s}{msg:<45}{d: >10s}\n".format(d='|', msg="1.Input delete: Remove User Info")
    prom_2 = "{d: <10s}{msg:<45}{d: >10s}\n".format(d='|', msg="2.Input update: Insert or Update User Info")
    prom_3 = "{d: <10s}{msg:<45}{d: >10s}\n".format(d='|', msg="3.Input find:   Get User Info")
    prom_4 = "{d: <10s}{msg:<45}{d: >10s}\n".format(d='|', msg="4.Input list:   List User Info")
    prom_5 = "{d: <10s}{msg:<45}{d: >10s}\n".format(d='|', msg="5.Input exit:   Exit")
    prom_6 = "{d: <10s}{msg:<45}{d: >10s}".format(d='|', msg="6.Input help:   Print This Menu")
    prompt = prom_1 + prom_2 + prom_3 + prom_4 + prom_5 + prom_6
    print('='*65)
    print(prompt)
    print('='*65)
 

opt = {
    "exit": exit,
    "delete": remove,
    "update": update_,
    "list": show,
    "find": acquire,
    "help": help_,
}


if __name__ == '__main__':
    help_()
    while True:     
        operation = input_("What You Want To Do: ")
        func = opt.get(operation)
        if func is None:
            help_()
        else:
            func()
    
