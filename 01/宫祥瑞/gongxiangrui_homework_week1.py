user = {'bob': {'age': 23, 'tel': 123456}, 'mike': {'age': 20, 'tel': 789456}, 'lisa': {'age': 25, 'tel': 456123}}
lst1 = []

# print(user)
def delete():
    usr = input('please input a name:')
    flag = user.pop(usr, 'notfind')
    if flag == 'notfind':
        print('{} is not find.'.format(usr))
    else:
        print('{}:{} is delete.'.format(usr, flag))


def update():
    usr = input('please input name:age:telephone')
    lst = usr.split(':')
    print(lst)
    for i in user.keys():
        # print(i)
        if lst[0] == i:
            user.update({lst[0]: {'age': lst[1], 'tel': lst[2]}})
    print(user)


def lst():
    # sorted
    def sort(src):
        for k, v in src.items():
            lst1.append(k)
            if isinstance(v, (dict, set)):
                sort(v)
            else:
                lst1.append(v)

    sort(user)

    for i in range(len(lst1)):
        if i%5 == 0:
            print()
            print('{:<6}'.format('name'), end='')

        print('{:<6}'.format(lst1[i]),end='')
    print()

def find():
    usr = input('please input a name:')
    val = user.get(usr, 'not find')
    print('{}'.format(val))


def main():
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
        lst()
        main()
    elif opt == 'exit':
        return 0
    else:
        print('error')
        return -2


main()