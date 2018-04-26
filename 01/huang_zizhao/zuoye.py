#!/usr/bin/env python
import readline

user_dict=dict()
user_dict = {
    "hzz": { 'userName': 'hzz', 'age': 27, 'tel': '123' },
    "lhr": { 'userName': 'lhr', 'age': 25, 'tel': '456' },
    "hzy": { 'userName': 'hzy', 'age': 27, 'tel': '789' },
}

def input_(p):
    return input(p).strip(' ')


def acquire():
    userNamePatten = input_("Pls Input UserName: ")
    users = user_dict.keys()
    user_match = [ u for u in users if userNamePatten in u ]
    for userName in user_match:
        string = "UserName: {:<15s} Age: {:<3} Tel: {t:<11s}".format(user_dict.get(userName).get('userName'),
            user_dict.get(userName).get('age'), t=user_dict.get(userName).get('tel'))
        print(string)
    print()


def remove():
    userName = input_("Pls Input UserName: ")
    if user_dict.get(userName) is None:
        print("Warning: {u:<15s} Not Exist.".format(u=userName))
        return None
    else:
        userInfo = user_dict.pop(userName)
        print("Delete User: {u:<15s}".format(u=userName))
        return userInfo


def update_():
    info = input_("Pls Input User Info: ")
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


def show():
    print("{:<20s}{:<8s}{:<18s}".format("UserName","Age","Tel"))
    for info in user_dict.values():
        userName = info.get('userName')
        age = info.get('age')
        tel = info.get('tel')
        print("{:<20}{:<8}{:<18}".format(userName, age, tel))
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
    
