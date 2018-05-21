# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 12:20
# @Author  : armo
# @File    : User.py
# @Software: PyCharm
# @Pyver   : 3.6.0


import json,re,os


class userinfo:
    def __init__(self):
        self.filename = os.path.dirname(os.path.abspath(__file__)) + "/user.json"

    def create(self):
        try:
            info = input("输入用户信息:\n")  # 姓名,年龄,电话,以冒号分隔
            rr = re.search("([^:]*):(\d{1,2}):(\d{11})", info).group().split(":")
            if os.path.getsize(self.filename) != 0:
                with open(self.filename,'r') as f:
                    userdata = json.loads(json.load(f))
            else:
                userdata = {}
            if rr[0] in userdata.keys():
                print("用户名已存在!")
            else:
                userdata[rr[0]] = {
                    "age": rr[1],
                    "phone": rr[2],
                }
                with open(self.filename, 'w') as fw:
                    json.dump(json.dumps(userdata),fw)
                print("新增成功!")
        except:
            print("输入错误，请重新")
            self.create()

    def retrieve(self):
        willRname = input("输入要查询的用户名:\n")
        with open(self.filename,'r') as f:
            info = json.loads(json.load(f))
            try:
                if info[willRname]:
                    print("""姓名: %s,年龄: %s,电话: %s""" %(willRname,info[willRname]['age'],info[willRname]['phone']))
                    return
            except:
                print( "此人失踪")
                return

    def update(self):
        try:
            info = input("修改后信息:\n") # 姓名,年龄,电话,以冒号分隔
            rr = re.search("([^:]*):(\d{1,2}):(\d{11})", info).group().split(":")
            with open(self.filename,'r') as f:
                userdata = json.loads(json.load(f))
            userdata[rr[0]] = {
                "age": rr[1],
                "phone": rr[2],
            }
            with open(self.filename, 'w') as fw:
                json.dump(json.dumps(userdata),fw)
            print("更新成功!")
        except:
            print("输入错误，请重新输入")
            self.update()

    def delete(self):
        willDname = input("输入要删除的用户名:\n")
        with open(self.filename, 'r') as f:
            info = json.loads(json.load(f))
            try:
                del info[willDname]
                with open(self.filename, 'w') as fw:
                    json.dump(json.dumps(info), fw)
                print("删除成功!")
                return
            except:
                print("此人失踪")
                return

if __name__ == '__main__':
    tododic = { '1':'create' , '2':'retrieve' , '3':'update' , '4':'delete'}
    while True:
        print("""功能列表:\n\t1:新增用户\n\t2:查询用户\n\t3:修改用户\n\t4:删除用户""")
        todo = input("请输入选项:")
        try:
            if tododic[todo] == 'create':
                obj = userinfo()
                obj.create()
            if tododic[todo] == 'retrieve':
                obj = userinfo()
                obj.retrieve()
            if tododic[todo] == 'update':
                obj = userinfo()
                obj.update()
            if tododic[todo] == 'delete':
                obj = userinfo()
                obj.delete()
        except:
            print("输入错误!")
            continue
   # 再试下面向对象的方式
