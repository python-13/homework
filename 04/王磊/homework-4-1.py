import  json

data = {'ab': {'age': 22, 'tel': '895653425', 'passwd': '123456'},
        'cd': {'age': 28, 'tel': '383290471', 'passwd': '2323323'},
        'cf': {'age': 8, 'tel': '2465447965', 'passwd': '232323'},
        'wd': {'age': 8, 'tel': '1660809109', 'passwd': '2323232323'},
        'ee' :{'age' :33 ,'tel' :'23232323' ,'passwd' :'1212121212'}}


json_str = json.dumps(data)

def user_no_found(username):
    print("Sorry,{} is not in this date".format(username))

def passwd_error(username):
    print("{}'s password is not true".format(username))

def f_check(username):
    if username in data.keys():
        return True
    else:
        return False

def f_delete(username):
    data.pop(username)
    json_str = json.dumps(data)
    print("{} have been deleted successfully".format(username))

def f_update(username, age, tel, passwd):
    data.update({username: {'age': age, 'tel': tel, 'passwd': passwd}})
    json_str = json.dumps(data)
    print("{} have been update successfully".format(username))

def f_check_passwd(username, passwd):
    if passwd == data[username]['passwd']:
        return True
    else:
        return False

def cmds_dispatcher():
    commands ={}
    def reg(name):
        def _reg(fn):
            commands[name] = fn
            return  fn
        return _reg
    def defaultfunc():
        print("Unkown command")
    def dispatcher():
        while True:
            cmd = input("Now,you can input delete,update,add,find,list,exit to management your data:")
            if cmd.strip()  == "exit":
                return
            commands.get(cmd,defaultfunc)()
    return  reg,dispatcher

reg , dispatcher = cmds_dispatcher()


@reg('delete')
def foo1():
    username = input("your name is : ")
    if f_check(username=username) == True:
        passwd = input("your password is : ")
        if f_check_passwd(username=username, passwd=passwd):
            f_delete(username=username)
        else:
            passwd_error(username=username)
    else:
        user_no_found(username=username)

@reg( 'update')
def foo2():
    username = input("your name is :")
    if f_check(username=username) == True:
        passwd = input("your password is :")
        if f_check_passwd(username=username, passwd=passwd):
            age = int(input("you age is :"))
            tel = input("your telephone is :")
            passwd_new = input("your new password is :")
            f_update(username=username, age=age, tel=tel, passwd=passwd_new)
        else:
            passwd_error(username=username)
    else:
        user_no_found(username=username)

@reg( 'find')
def foo3():
    username = input("your name is  ")
    if f_check(username=username) == True:
        if username in data.keys():
            data[username]['passwd'] = '*' * len(data[username]['passwd'])
            print("This  user's name is {} ,age is{:>3} ,telephone is {},password is {} ".format(username,data[username]['age'],data[username]['tel'],data[username]['passwd']))
        else:
            user_no_found(username=username)

@reg( 'list')
def foo4():
    for username in data.keys():
        data[username]['passwd'] = '*' * len(data[username]['passwd'])
    act = input("Do you want sort this date, y or n : ")
    print(chr(22995) + chr(21517), chr(24180) + chr(40836), '\0' * 3, chr(30005) + chr(35805), '\0' * 3,chr(23494) + chr(30721))
    if act == 'y':
        sort = sorted(data)
        for x in range(len(sort)):
            print('{}{:>5}{:>12}{:>12}'.format(sort[x], data[sort[x]]['age'], data[sort[x]]['tel'],data[sort[x]]['passwd']))
    if act == 'n':
        for i in data.keys():
            print("{}{:>5}{:>12}{:>12}".format(i, data[i]['age'], data[i]['tel'], data[i]['passwd']))

dispatcher()
