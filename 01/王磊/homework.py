Date = {'ab': '12,123456789', 'cd': '34,132878763', 'zs': '65,153936589', 'ed': '34,122745238','tr':'12,323'}


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
        print("This  user's name is {} ,age is{:>3} ,telephone is {} ".format(name, Date.get(name)[:2],Date.get(name)[3:]))
        if name not in Date.keys():
            print("Sorry,this user is not in this date")

    if action == 'list':
        print(chr(22995) + chr(21517), chr(24180) + chr(40836), '\0' * 3, chr(30005) + chr(35805))
        for i in Date.keys():
                print("{}{:>5}{:>12}".format(i, Date[i][:2], Date[i][3:]))

    if action == 'exit':
        print("It will exit this program.")
        break
