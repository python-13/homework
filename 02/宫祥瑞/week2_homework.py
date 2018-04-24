user = {'bob': {'age': 23, 'tel': 123456,'passwd':'112233'}, 'mike': {'age': 20, 'tel': 789456,'passwd':'112233'}, 'lisa': {'age': 25, 'tel': 456123,'passwd':'112233'}}
usr = []
age = []
tel = []
flag = 0
# print(user)
def add():
    usr = input('please input name:age:telephone:password')
    lst = usr.split(':')
    print(lst)
    user.update({lst[0]: {'age': lst[1], 'tel': lst[2], 'passwd': lst[3]}})
    # print(user)

def delete():
    usr = input('please input a name:')
    flag = user.pop(usr, 'notfind')
    if flag == 'notfind':
        print('{} is not find.'.format(usr))
    else:
        print('{}:{} is delete.'.format(usr, flag))


def update():
    usr = input('please input name:age:telephone:password')
    lst = usr.split(':')
    print(lst)
    for i in user.keys():
        # print(i)
        if lst[0] == i:
            user.update({lst[0]: {'age': lst[1], 'tel': lst[2],'passwd':lst[3]}})
    #print(user)


def lst(type):
    # sorted
    for k, v in user.items():
        usr.append(k)
        for k1, v1 in v.items():
            if k1 == 'age':
                age.append(v1)
            elif k1 == 'tel':
                tel.append(v1)

        for i in range(len(usr)):
            for j in range(len(usr)-i-1):
                if type == 'user':
                    if usr[j] > usr[j+1]:
                        usr[j],usr[j+1] = usr[j+1],usr[j]
                        age[j],age[j+1] = age[j+1],age[j]
                        tel[j],tel[j+1] = tel[j+1],tel[j]
                elif type == 'age':
                    if age[j] > age[j+1]:
                        usr[j],usr[j+1] = usr[j+1],usr[j]
                        age[j],age[j+1] = age[j+1],age[j]
                        tel[j],tel[j+1] = tel[j+1],tel[j]
                elif type == 'tel':
                    if tel[j] > tel[j+1]:
                        usr[j],usr[j+1] = usr[j+1],usr[j]
                        age[j],age[j+1] = age[j+1],age[j]
                        tel[j],tel[j+1] = tel[j+1],tel[j]
                else:
                    print('type worng')
                    return -2
    for n in range(len(usr)):
        print('user={}\tage={}\ttel={}'.format(usr[n],age[n],tel[n]))


def find():
    usr = input('please input a name:')
    for k, v in user.items():
        if k == usr:
            passwd =  v.get('passwd')
            print('age={}\ntel={}\npassword={}'.format(v.get('age'),v.get('tel'),'*' * len(passwd)))


def main():
    global flag
    while True:

        if flag:
            break
        usr = input('please input user')
        for k,v in user.items():
            if  k == usr:
                pd = v.get('passwd')
                print(pd)
                password = input('please input password')
                if pd == password:
                    flag = 1
                    break
                else:
                    print('password worng')
                    break
            else:
                print('user name input worng')




    opt = input("please input options in 'delete update find list exit'")

    if opt == 'delete':
        delete()
        main()
    elif opt == 'update':
        update()
        main()
    elif opt == 'find':
        find()
        main()
    elif opt == 'list':
        type = input('please input type in user age tel')
        lst(type)
        main()
    elif opt == 'exit':
        return 0
    else:
        print('error')
        main()



main()