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
'''
在用户管理功能中添加密码信息:
增、 改强制验证用户密码，验证通过后，提示进行的操作信息，比如：修改xxx的密码为xxxx
当使用list 和 find操作的时候，为了保护用户隐私，将用户密码替换显示成为N(密码长度)个*
使用list时，提示用户可以对列表显示的信息进行排序，排序的字段（name, age, tel）, 根据用户输入字段进行排序（升序），默认为name排序.
'''
users = []
def list_users():
    if users:
        print("信息如下")
        for i in users:
            for key in i:
                print("姓名:{}, 密码: ******，年龄：{}，联系方式：{}".format(key,i[key][1],i[key][2]))
    else:
        print("无数据")

def update_users():
    if users:
        user_name = input("请输入你需要更新信息的用户名")
        for i in users:
            flag = False
            if i.__contains__(user_name):
                count = 0
                while True:
                    passwd = input("请输入用户密码加以验证:")
                    if passwd == i[user_name][0]:
                        print("""
                        用户{}信息如下
                        密码：{}
                        年龄：{}
                        联系方式：{}
                        """.format(user_name,i[user_name][0],i[user_name][1],i[user_name][2]))
                        while True:
                            update_message = input("请输入更新的信息:（密码，年龄，联系方式，以逗号隔开）").split(",")
                            if len(update_message) != 3:
                                print("请按提示要求填入信息")
                                continue
                            else:
                                for j in range(len(update_message)):
                                    update_message[j] = update_message[j].strip()
                                break
                        i[user_name] = update_message
                        print("""
                        用户{}更新后的信息如下
                        密码：{}
                        年龄：{}
                        联系方式：{}
                        """.format(user_name, i[user_name][0], i[user_name][1], i[user_name][2]))
                        flag = True
                        break
                    else:
                        count += 1
                        if count >= 3:
                            flag = True
                            print("连续三次错误，返回上一层")
                            break
                        print("密码错误")

            if flag:
                break
        else:
            print("用户不存在！！！")
    else:
        print("无数据")

def find_users():
    if users:
        name = input("请输入你要查询的用户名：")
        for i in users:
            if i.__contains__(name):
                print("信息如下")
                print("姓名:{}, 密码: ******，年龄：{}，联系方式：{}".format(name, i[name][1], i[name][2]))
            else:
                print("用户不存在")
    else:
        print("无数据")

def del_users():
    if users:
        user_name = input("请输入你需要删除信息的用户名")
        for i in users:
            if i.__contains__(user_name):
                users.remove(i)
                if not i.__contains__(user_name):
                    print("以删除用户{}".format(user_name))
            else:
                print("用户不存在")
    else:
        print("无数据")

def add_users():
    while True:
        message = input("请依次输入用户姓名，密码，年龄，联系方式（手机号码），以逗号隔开：").split(",")
        if len(message) != 4:
            print("请按提示要求填入信息")
            continue
        else:
            for i in range(len(message)):
                message[i] = message[i].strip()
            break
    name = message[0]
    passwd = message[1]
    age = message[2]
    tel = message[3]
    user_messgae = {name:[passwd,age,tel]}
    users.append(user_messgae)
    print("添加用户{}成功".format(name))



print("""
   #########################
   请输入序号选择对应的功能：
   1. 查看当前注册用户信息
   2. 更新用户信息
   3. 添加用户
   4. 删除用户
   5. 查找用户
   6. 退出程序
   #########################
   """)
while True:
    num = input("请输入你需要选择的功能: ")
    if num.isdigit() and 0 < int(num) < 7:
        num = int(num)
        if num == 1:
            list_users()
        elif num == 2:
            update_users()
        elif num == 3:
            add_users()
        elif num == 4:
            del_users()
        elif num == 5:
            find_users()
        else:
            print("bye")
            break
    else:
        print("输入有误请重新输入")



