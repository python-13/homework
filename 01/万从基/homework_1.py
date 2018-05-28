# 第一次作业
# 用户管理
# 如果输入 delete， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据， 若
# 存在数据则将该数据移除， 若用户数据不存在， 则提示不存在
# 如果输入 update， 则让用户输入” 用户名: 年龄: 联系方式” 格式字符串， 并使用: 分隔用户
# 数据， 根据用户名查找 dcit 中数据， 若存在数据则将改数据更新数据， 若用户数据不存在，
# 则提示不存在
# 如果用户输入 find， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据包
# 含输入字符串的用户信息， 并打印
# 如果用户输入 list， 则打印所有用户信息
# 打印用户第一个行数据为用户信息描述， 从第二行开始为用户数据
# 如果用户输入 exit， 则打印退出程序， 并退出

user = {'tom':[30,110], 'jerry':[29,120]}

command = input('Please input a command(delete, update, find, list, exit):')
if command == 'find':
    username = input('Please input username:')
    if username in user.keys():
        print('age: {}, phone: {}'.format(user[username][0],user[username][1]))
    else:
        print(username + " is not exist!")
elif command == 'update':
    infor = input('Please input your info(username:age:phone):') 
    username = infor.strip(':')[0]
    age = infor.strip(':')[1]
    phone = infor.strip(':')[2]
    if username in user.keys():
        user[username] = [age,phone]
    else:
        print(username + " is not exist!")
elif command == 'list':
    [print('username: {}\nage: {}, phone: {}'.format(k,v[0],v[1])) for k,v in user.items()]
elif command == 'delete':
    username = input('Please input username:')
    if username in user.keys():
        user.pop(username)
        print('user ' + username + ' is delete!')
    else:
        print(username + " is not exist!")
elif command == 'exit':
    exit()
else:
    print('Error input!!')

