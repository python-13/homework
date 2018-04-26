'''
如果输入 delete， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据， 若
存在数据则将该数据移除， 若用户数据不存在， 则提示不存在;
如果输入 update， 则让用户输入” 用户名:年龄:联系方式” 格式字符串， 并使用:分隔用户
数据， 根据用户名查找 dcit 中数据， 若存在数据则将改数据更新数据， 若用户数据不存在，
则提示不存在;
如果用户输入 find， 则让用户输入” 用户名” 格式字符串， 根据用户名查找 dict 中数据包
含输入字符串的用户信息， 并打印;
如果用户输入 list， 则打印所有用户信息;
打印用户第一个行数据为用户信息描述， 从第二行开始为用户数据;
如果用户输入 exit， 则打印退出程序， 并退出 ;



'''

users = []
while True:
    print("""
    #########################
    请输入序号选择对应的功能：
    1. 查看当前注册用户信息
    2. 更新用户信息
    3. 添加用户
    4. 删除用户
    5. 查找用户
    6. 退出程序
    7.
    #########################
    """)
    message = input("请输入你需要选择的功能: ")
    if message.isdigit() and 0 < int(message) < 7 :
        message = int(message)
        if message == 1:
            if users:
                print("信息如下")
                for i in users:
                    for key in i:
                        print("姓名: %s   年龄：%s   手机号码：%s"%(key,i[key][0],i[key][1]))
            else:
                print("无数据")
        elif message == 2:
            if users:
                name = input("请输入需要更新信息的用户名：")
                for i in users:
                    if name in i.keys():
                        message =  input("请按照提示输入数据进行更新：(年龄:联系方式)")
                        if ":" in message:
                            message = message.split(":")
                            i[name]=message
                            print("%s更新后年龄: %s 手机号码: %s" % (name, i[name][0], i[name][1]))
                        elif "：" in message:
                            message = message.split("：")
                            i[name] = message
                            print("%s更新后年龄: %s 手机号码: %s" % (name, i[name][0], i[name][1]))
                        else:
                            print("格式有误")
            else:
                print("无数据")
        elif message == 3:
            name = input("请输入添加用户的姓名：")
            age = input("请输入该用户的年龄：")
            phone = input("请输入该用户的手机号码：")
            user_message = [age,phone]
            dict_user = {name:user_message}
            users.append(dict_user)
            print("用户%s添加成功"%name)
        elif message == 4:
            if users:
                name = input("请输入需要删除信息的用户名：")
                for i,j in enumerate(users):
                    if name in j:
                        users.pop(i-1)
                        print("%s删除成功"%name)
                    else:
                        print("用户不存在")
            else:
                print("无数据")
        elif message == 5:
            if users:
                name = input("请输入你要查询的用户名：")
                for i in users:
                    if name in i:
                        print("信息如下")
                        print("姓名: %s   年龄：%s   手机号码：%s" % (name, i[name][0], i[name][1]))
            else:
                print("无数据")
        else:
            print("bye")
            break
    else:
        print("请根据提示输入相应的序号")

# 代码写的很不错，逻辑严谨，很棒，后面可以考虑下封装成函数
