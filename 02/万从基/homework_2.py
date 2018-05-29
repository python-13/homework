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

# 第二次作业：
# 在用户管理功能中添加密码信息:
# 增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
# 当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
# 使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）, 根据用户输入字段进行排序（升序），默认为name排序.

user = {'tom':{'age':30,'phone':110,'passwd':'gdsagsa'}, 'jerry':{'age':29,'phone':120,'passwd':'gdsagsvcxzb'}}
while True:
    command = input('Please input a command(delete, update, find, list, exit):')
    if command == 'find':
        username = input('Please input username:')
        if username in user.keys():
            print('age: {}, phone: {}'.format(user[username]['age'],user[username]['phone']))
        else:
            print(username + " is not exist!")
    elif command == 'update':
        infor = input('Please input your info(username:age:phone):').strip().split(':')
        username = infor[0]
        age = infor[1]
        phone = infor[2]
        if username in user.keys():
            user[username]['age'] = age
            print('Update Succeed!')
        else:
            print(username + " is not exist!")
    elif command == 'list':
        [print('username: {}\nage: {}, phone: {}, password: {}'.format(k,v['age'],v['phone'],['*' for i in range(len(v['passwd']))])) for k,v in user.items()]
    elif command == 'delete':
        username = input('Please input username:')
        if username in user.keys():
            user.pop(username)
            print('user ' + username + ' is delete!')
        else:
            print(username + " is not exist!")
    elif command == 'exit':
        print('Exiting...')
        break
    else:
        print('Error input!!')

