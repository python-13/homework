import json

DATE  = {'ab': '12,123456789', 'cd': '34,132878763', 'zs': '65,153936589', 'ed': '34,122745238', 'tr': '12,323'}
PD = {'ab': '1223', 'cd': '345', 'ef': '456', 'zs': '567', 'ed': '21', 'tr': '2323'}
jsondate = json.dumps(DATE )
json_pd = json.dumps(PD)

def  delete():
    name = input("your name is :")
    Date = json.loads(jsondate)
    if name in Date.keys():
        Date.pop(name)
        json_date = json.dumps(Date)
        print("This user have been deleted")
        print(json_date)
    else:
        print("Sorry,this user is not in this date")

def  update():
    name = input("your name is :")
    Date = json.loads(jsondate)
    pd = json.loads(json_pd)
    if name in Date.keys():
        pwd = input("The password is :")
        if pwd == pd.get(name):
            pw = input("Please input new password ")
            pd[name] = pw
            tel = input("your telephone is :")
            age = int(input("your age is :"))
            if 10 > age > 0:
                age = '0' + str(age)
                Date[name] = age + ',' + tel
            elif 100 < age < 0:
                age = str(age)
                Date[name] = age + ',' + tel
            json_date = json.dumps(Date)
            print("{}:{}:{}".format(name, age, tel))
            print(json_date)
        else:
            print("Your password is not true")
    else:
        print("Sorry,this user is not in this date")

def ads():
    Date = json.loads(jsondate)
    pd = json.loads(json_pd)
    name = input("your name is :")
    pw = input("Please input new password ")
    age = input("your age is :")
    tel = input("your telephone is :")
    if len(age) == 1:
        age = '0' + age
        Date[name] = age + ',' + tel
    elif len(age) == 2:
        Date[name] = age + ',' + tel
    pd[name] = pw
    json_date = json.dumps(Date)
    print(json_date)
    print("The user is {},age is :{},tel is :{}".format(name, age, tel))

def find():
    name = input("your name is :")
    Date = json.loads(jsondate)
    pd = json.loads(json_pd)
    if name in Date.keys():
        pd[name] = '*' * len(pd[name])
        print("This  user's name is {} ,age is{:>3} ,telephone is {},password is {} ".format(name, Date.get(name)[:2],Date.get(name)[3:],pd[name]))
    elif name not in Date.keys():
        print("Sorry,this user is not in this date")

def list():
    Date = json.loads(jsondate)
    pd = json.loads(json_pd)
    act = input("Do you want sort this date, y or n : ")
    for name in pd.keys():
        pd[name] = '*' * len(pd[name])
    print(chr(22995) + chr(21517), chr(24180) + chr(40836), '\0' * 3, chr(30005) + chr(35805), '\0' * 8,
          chr(23494) + chr(30721))
    if act == 'y':
        sort = sorted(Date)
        for x in range(len(Date)):
            print('{}{:>5}{:>12}{:>12}'.format(sort[x], Date[sort[x]][:2], Date[sort[x]][3:], pd[sort[x]]))
    if act == 'n':
        for i in Date.keys():
            print("{}{:>5}{:>12}{:>12}".format(i, Date[i][:2], Date[i][3:], pd[i]))

def exit():
    print("It will exit this program.")

while True:
    action = input("Now,you can input delete,update,add,find,list,exit to management your date:")
    if action == "delete":
        delete()
    if  action =="update":
        update()
    if action =="add":
        ads()
    if  action=="find":
        find()
    if action=="list":
        list()
    if action=="exit":
        exit()
        break