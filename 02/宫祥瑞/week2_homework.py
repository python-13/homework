user = {'bob': {'age': '23', 'tel':'123456','passwd':'112233'}, 'mike': {'age':'20','tel':'789456','passwd':'112233'}, 'lisa': {'age':'25', 'tel':'456123','passwd':'112233'}}
usr = []
age = []
tel = []
passwd = []

flag = 0
flag1 = 1
flag2 = 1

def verify():
    global flag
    while True:
        if flag:
            flag = 0
            break
        name = input('please input user')
        for k, v in user.items():
            if k == name:
                passwd = v.get('passwd')
                password = input('please input password')
                if passwd == password:
                    flag = 1
                    break
                else:
                    print('password is wrong')
                    break
        else:
            print('user name input wrong')
    return name


# print(user)
def add():
    mes = input('please input name:age:telephone:password')
    lst = mes.split(':')
    #print(lst)
    user.update({lst[0]:{'age': lst[1],'tel': lst[2],'passwd':lst[3]}})
    print('add sucess user={}\tage={}\ttel={}\tpassword={}'.format(lst[0],lst[1],lst[2],'*'*len(lst[3])))

def delete(name):

    user.pop(name)
    print('{} is delete.'.format(name))


def update(name):

    mes = input('please input age:telephone:password')
    lst = mes.split(':')
    user.update({name: {'age': lst[0], 'tel': lst[1],'passwd':lst[2]}})
    print('update sucess age={}\ttel={}\tpassword={}'.format( lst[0], lst[1], '*' * len(lst[2])))

#list重大漏洞待解决
def lst(type):
    # sorted
    global flag1
    if flag1:
        flag1 = 0
        for k, v in user.items():
            usr.append(k)
            for k1, v1 in v.items():
                if k1 == 'age':
                    age.append(v1)
                elif k1 == 'tel':
                    tel.append(v1)
                elif k1 == 'passwd':
                    passwd.append(v1)

        for i in range(len(usr)):
            for j in range(len(usr)-i-1):
                if type == 'user':
                    if usr[j] > usr[j+1]:
                        usr[j],usr[j+1] = usr[j+1],usr[j]
                        age[j],age[j+1] = age[j+1],age[j]
                        tel[j],tel[j+1] = tel[j+1],tel[j]
                        passwd[j],passwd[j+1] = passwd[j+1],passwd[j]
                elif type == 'age':
                    if age[j] > age[j+1]:
                        usr[j],usr[j+1] = usr[j+1],usr[j]
                        age[j],age[j+1] = age[j+1],age[j]
                        tel[j],tel[j+1] = tel[j+1],tel[j]
                        passwd[j], passwd[j + 1] = passwd[j + 1], passwd[j]
                elif type == 'tel':
                    if tel[j] > tel[j+1]:
                        usr[j],usr[j+1] = usr[j+1],usr[j]
                        age[j],age[j+1] = age[j+1],age[j]
                        tel[j],tel[j+1] = tel[j+1],tel[j]
                        passwd[j], passwd[j + 1] = passwd[j + 1], passwd[j]
                else:
                    print('type wrong')
                    return -2
    for n in range(len(usr)):
        print('user={}\tage={}\ttel={}\tpassword={}'.format(usr[n],age[n],tel[n],'*'*len(passwd[n])))


def find():
    usr = input('please input a name:')
    for k, v in user.items():
        if k == usr:
            passwd =  v.get('passwd')
            print('age={}\ntel={}\npassword={}'.format(v.get('age'),v.get('tel'),'*' * len(passwd)))




def main():
    global flag2
    if flag2:
       flag2 = 0
       verify()
    opt = input("please input options in 'add delete update find list exit'")
    if opt == 'add':
        add()
        main()
    elif opt == 'delete':
        name = verify()
        delete(name)
        main()
    elif opt == 'update':
        name = verify()
        update(name)
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