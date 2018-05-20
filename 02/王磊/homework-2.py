Date = {'ab': '12,123456789', 'cd': '34,132878763', 'zs': '65,153936589', 'ed': '34,122745238','tr':'12,323'}
pd  = {'ab': '1223', 'cd': '345', 'ef': '456', 'zs': '567','ed':'21','tr':'2323'}

while True:
    action = input("Now,you can input delete,update,find,list,exit to management your date:")
    if action == 'delete':
        name = input("your name is :")
        if name in Date.keys():
          Date.pop(name)
          print("Now date is {}".format(Date))
          print("This user have been deleted")
        else:
             print("Sorry,this user is not in this date")

    if action == 'update':
        name = input("your name is :")
        if name in Date.keys():
            pwd = input("The password is :")
            if pwd == pd.get(name):
                pw = input("Please input new password ")
                pd[name] = pw
            else:
                print("Your password is not true")
            tel = input("your telephone is :")
            age = int(input("your age is :"))
            if age < 0 or age > 100:
                print("age is out of range")
            elif 10 > age > 0:
                age = '0' + str(age)
            else:
                age = str(age)
            Date[name] = age + ',' + tel
            print("{}:{}:{}".format(name, age, tel))
            print("Now date is {}".format(Date))
        else:
            print("Sorry,this user is not in this date")

    if action == 'find':
        name = input("your name is :")
        if name in Date.keys():
            pd[name] = '*'*len(pd[name])
            print("This  user's name is {} ,age is{:>3} ,telephone is {},password is {} ".format(name, Date.get(name)[:2],Date.get(name)[3:],pd[name]))
        elif name not in Date.keys():
            print("Sorry,this user is not in this date")

    if action == 'list':
        act = input("Do you want sort this date, y or n : ")
        for name in pd.keys():
            pd[name] = '*' * len(pd[name])
        print(chr(22995) + chr(21517), chr(24180) + chr(40836), '\0' * 3, chr(30005) + chr(35805), '\0' * 8,chr(23494) + chr(30721))
        if  act == 'y':
            sort = sorted(Date)
            for x in range(len(Date)):
                print('{}{:>5}{:>12}{:>12}'.format(sort[x], Date[sort[x]][:2], Date[sort[x]][3:], pd[sort[x]]))
        if act == 'n':
            for i in Date.keys():
                print("{}{:>5}{:>12}{:>12}".format(i, Date[i][:2], Date[i][3:], pd[i]))

    if action == 'exit':
        print("It will exit this program.")
        break
