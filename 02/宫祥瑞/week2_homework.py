user = {'bob': {'age': '23', 'tel':'123456','passwd':'112233'}, 'mike': {'age':'20','tel':'789456','passwd':'112233'}, 'lisa': {'age':'25', 'tel':'456123','passwd':'112233'}}
usr = []
age = []
tel = []
passwd = []

flag = 0
flag2 = 1

def verify(src=user):
    global flag
    while True:
        if flag:
            flag = 0
            break
        name = input('please input user').strip()
        for k, v in src.items():
            if k == name:
                passwd = v.get('passwd')
                password = input('please input password').strip()
                if passwd == password:
                    flag = 1
                    print('welcome user:{} password:{} log in'.format(name,'*'*len(passwd)))
                    break
                else:
                    print('password is wrong')
                    break
        else:
            print('user name input wrong')
    return name


# print(user)
def add(src=user):
    mes = input('please input name:age:telephone:password').strip()
    lst = mes.split(':')
    src.update({lst[0]:{'age': lst[1],'tel': lst[2],'passwd':lst[3]}})
    print('add sucess user={}\tage={}\ttel={}\tpassword={}'.format(lst[0],lst[1],lst[2],'*'*len(lst[3])))

def delete(name,src=user):
    src.pop(name)
    print('{} is delete.'.format(name))


def update(name,src=user):
    mes = input('please input age:telephone:password').strip()
    lst = mes.split(':')
    src.update({name: {'age': lst[0], 'tel': lst[1],'passwd':lst[2]}})
    print('update sucess age={}\ttel={}\tpassword={}'.format( lst[0], lst[1], '*' * len(lst[2])))


def lst(src=user):
    # sorted
        type = input('please input type in user age tel').strip()
        def _list(n):
            usr[n], usr[n + 1] = usr[n + 1], usr[n]
            age[n], age[n + 1] = age[n + 1], age[n]
            tel[n], tel[n + 1] = tel[n + 1], tel[n]
            passwd[j], passwd[j + 1] = passwd[j + 1], passwd[j]
        for k, v in src.items():
            usr.append(k)
            #age,tel,passwd = *user[k]
            for k1, v1 in v.items():
                if k1 == 'age':
                    age.append(v1)
                elif k1 == 'tel':
                    tel.append(v1)
                elif k1 == 'passwd':
                    passwd.append(v1)

        for i in range(len(usr)):
            for j in range(len(usr)-i-1):
                if type == 'user'or type == '':
                    if usr[j] > usr[j+1]:
                        _list(j)
                elif type == 'age':
                    if age[j] > age[j+1]:
                        _list(j)
                elif type == 'tel':
                    if tel[j] > tel[j+1]:
                        list(j)
                else:
                    print('type wrong')
                    return -2
        for n in range(len(usr)):
            print('user={}\tage={}\ttel={}\tpassword={}'.format(usr[n],age[n],tel[n],'*'*len(passwd[n])))
        usr.clear()
        age.clear()
        tel.clear()

def find(src=user):
    usr = input('please input a name:').strip()
    for k, v in src.items():
        if k == usr:
            passwd =  v.get('passwd')
            print('age={}\ntel={}\npassword={}'.format(v.get('age'),v.get('tel'),'*' * len(passwd)))




def main():
    global user,flag2
    if flag2:
       flag2 = 0
       verify()
    opt = input("please input options in 'add delete update find list exit'").strip()
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
        lst()
        main()
    elif opt == 'exit':
        return 0
    else:
        print('error')
        main()



main()