#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: clsUsers.py
@time: 2018-05-18-16:44
"""

import os
from datetime import date, datetime

from conf import conf as  my_conf
from conf import template as my_template

from modules.Common import Common as my_Common
from modules.jsonhelper import jsonhelper as my_jsonhelper

'''类描述'''


class clsUsers(object):
    # 用户数据库
    # /Users/davetan/Desktop/mypython/python90day/z基础部分知识点/shoping/database/users.db
    __database = "{0}.db".format(os.path.join(my_conf.DATABASE['dbpath'],
                                              my_conf.DATABASE["tables"]["users"]))

    def __init__(self):
        # print(self.__database)
        self.username = ""  # 登录名
        self.password = ""  # 登录密码
        self.bindcard = ""  # 绑定卡
        self.islogin = False  # 登录状态
        self.name = ""  # 姓名
        self.mobile = ""  # 手机
        self.islocked = 0  # 是否锁定
        self.role = "user"  # 账户权限
        self.trycount = 0  # 登录尝试次数
        self.isdel = 0  # 用户删除标识
        # 随机验证码逻辑有误
        self.code = my_Common.verification_code(1)  # 随机验证码

        # 将json字符串一次性读入json字典中
        self.dict_user = {}

        self.db_load()

    def __str__(self):
        return '类的解释描述'

    def db_load(self):
        # 返回json字符串 导出为字典
        # print(self.__database)
        self.dict_user = my_jsonhelper.load_data_from_db(self.__database)

    # print(self.dict_user)

    def login(self):
        """
        用户登录过程函数，输入用户名和密码后调用内部方法 _user_login进行登录验证
        :return:
        """
        # 如果大于最大尝试次数
        while self.trycount <= my_conf.ERROR_MAX_COUNT:
            if (self.trycount == my_conf.ERROR_MAX_COUNT - 1):
                my_Common.show_message('请注意再输入一次系统将锁定当前用户', "NOTICE")

            self.username = input("用户名: ")
            password = input("密  码: ")
            self.code = '1'  # my_Common.verification_code(1) #随机验证码
            # my_Common.show_message("验证码：{0}".format(self.code), "INFORMATION")
            check_code = '1'  # input("请输入验证码:")

            '''
            验证码
            '''
            if check_code != self.code:
                my_Common.show_message("验证码错误！", "ERROR")
                continue

            '''
            用户名不存在  类中 @property 的方法
            '''
            if not self.user_exists:
                my_Common.show_message("用户名/密码错误！", "ERROR")
                continue

            # 调用用户登录方法进行登录,登录成功后更新对象self
            self._user_login(password, check_code)

            # 用户锁定就直接退出
            if self.islocked:
                my_Common.show_message("该用户已被锁定,请联系系统管理员！", "ERROR")
                self.trycount = 0
                break

            # 登录成功 退出登录
            if self.islogin:
                break
            else:
                my_Common.show_message("用户名密码错误", "NOTICE")

        # else:
        if self.trycount > my_conf.ERROR_MAX_COUNT:
            # 失败后锁定
            self.islocked = 1

            # 更新用户信息
            self.dict_user[self.username]["islocked"] = self.islocked
            self.update_user()
            my_Common.show_message("输入错误次数过多,请联系系统管理员!", "ERROR")

    # 将用户的登录尝试次数恢复初始值 0
    # self.trycount = 0

    def update_user(self):
        """
        用户数据更新方法,用户修改信息、用户账户锁定、解锁等操作之后更新数据库文件
        :return:
        """
        try:
            '''
            _password = my_Common.encrypt(self.password)
            self.dict_user[self.username]["password"] = _password
            self.dict_user[self.username]["islocked"] = self.islocked
            self.dict_user[self.username]["name"] = self.name
            self.dict_user[self.username]["mobile"] = self.mobile
            self.dict_user[self.username]["bindcard"] = self.bindcard
            self.dict_user[self.username]["isdel"] = self.isdel
            self.dict_user[self.username]["role"] = self.role
            '''
            # 写入数据库文件
            my_jsonhelper.write_db_simplejson(self.dict_user, self.__database)
            return True
        except Exception as e:
            my_Common.write_error_log(e)
            return False

    @property
    def user_exists(self):
        # self.dict_user.keys()
        if self.username in list(self.dict_user.keys()):
            return True
        else:
            return False

    def _user_login(self, password, code):
        """
        用户登录验证模块,对用户对象进行判断,登录成功后返回一个新的用户对象
        :return:
        """
        # 对输入的密码加密
        _password = my_Common.encrypt(password)

        for user, details in self.dict_user.items():
            # 找到用户名
            if user == self.username and not details["isdel"]:
                # 是否被锁定
                if details["islocked"] == 0:
                    # 账户未锁定,验证密码
                    if details["password"] == _password and code == self.code:
                        # 对用户对象进行赋值
                        self.islogin = True
                        # self.bindcard = details["bindcard"]
                        self.name = details["name"]
                        self.mobile = details["mobile"]
                        self.role = details["role"]
                        self.isdel = details["isdel"]
                        self.islocked = details["islocked"]
                        self.password = password
                        break
                    else:
                        # 密码错误,失败1次
                        self.trycount += 1
                else:
                    # 账户锁定了
                    self.islocked = 1

    def logout(self):
        """
        注销当前用户,将系统属性置空
        :return:
        """
        self.islogin = False
        self.bindcard = ""
        self.mobile = ""
        self.name = ""
        self.password = ""
        self.username = ""
        my_Common.show_message("注销成功", "NOTICE")

    def modify_password(self):
        """
        个人中心 - 修改密码
        :return:
        """
        _not_null_flag = False
        try:
            while not _not_null_flag:
                _new_password = input("输入新密码: ").strip()
                _confirm_password = input("再次输入确认密码:").strip()
                if not _new_password or not _confirm_password:
                    my_Common.show_message("密码不能为空,请重新输入!", "ERROR")
                    continue
                if _new_password != _confirm_password:
                    my_Common.show_message("两次输入密码不一致,请重新输入!", "NOTICE")
                    continue
                _not_null_flag = True
            self.password = _new_password
            _password = my_Common.encrypt(self.password)
            self.dict_user[self.username]["password"] = _password
            self.update_user()
            my_Common.show_message("密码修改成功!", "INFORMATIOM")
            return True
        except Exception as e:
            my_Common.write_error_log(e)
            return False


    def modify_user_info(self):
        """
        打印用户信息
        :return: 用户信息字符串
        """
        if self.islocked == 1:
            currstatus = "账户锁定"
        else:
            currstatus = "账户正常"
        frmuser = my_template.user_info.format(
            username=self.username,
            name=self.name,
            mobile=self.mobile,
            bindcard=self.bindcard,
            role=self.role,
            islocked="是" if self.islocked == 1 else "否",
            isdel="是" if self.isdel == 1 else "否"
        )
        # 打印用户信息
        my_Common.show_message(frmuser, "NOTICE")
    
        # 开始修改
        my_Common.show_message("请输入新的资料,若不更新直接回车：", "NOTICE")
        # 三元运算
        new_name = input("姓名({0}); ".format(self.name))
        new_mobile = input("手机({0}): ".format(self.mobile))
        self.name = self.name if len(new_name) == 0 else new_name
        self.mobile = self.mobile if len(new_mobile) == 0 else new_mobile

        # 更新用户资料库变量
        self.dict_user[self.username]["name"] = self.name
        self.dict_user[self.username]["mobile"] = self.mobile

        if self.update_user():
            my_Common.show_message("信息更新成功!", "NOTICE")
        else:
            my_Common.show_message("更新失败,查看日志!", "ERROR")


    def init_user_info(self):
        """
        创建用户，完善用户资料信息
        :return:
        """
        is_null_flag = True
        while is_null_flag:
            self.username = input("登录用户名(小写字母）:").strip().lower()
            if not self.username:
                my_Common.show_message("用户名不能为空", "ERROR")
                continue
            elif self.user_exists:
                my_Common.show_message("该用户名已存在", "ERROR")
                continue
            else:
                is_null_flag = False
                continue

        self.name = my_Common.input_msg("姓名:")
        self.password = my_Common.input_msg("密码:")
        self.mobile = my_Common.input_msg("手机:")
        self.role = my_Common.input_msg("用户权限(user/admin):", ("admin", "user"))
        self.create_user()
        my_Common.show_message("用户创建成功!", "NOTICE")


    def create_user(self):
        """
        新创建一个用户,将用户数据同步写入到数据库文件
        :return:
        """
        self.dict_user[self.username] = dict(password=my_Common.encrypt(self.password),
                                             name=self.name,
                                             mobile=self.mobile,
                                             # bindcard=self.bindcard,
                                             role=self.role,
                                             islocked=0,
                                             isdel=0,
                                             )
        my_jsonhelper.write_db_simplejson(self.dict_user, self.__database)


    def del_user(self):
        """
        删除用户,逻辑删除
        :return:
        """
        self.dict_user[self.username]["isdel"] = 1
        self.update_user()

    def unlock_user(self):
        self.dict_user[self.username]["islocked"] = 0
        self.update_user()

    def load_user_info(self):
        """
        根据用户名获取用户信息
        :return: 用户对象
        """
        if self.user_exists:
            user_detail = self.dict_user[self.username]
            self.name = user_detail["name"]
            # self.bindcard = user_detail["bindcard"]
            self.islocked = user_detail["islocked"]
            self.role = user_detail["role"]
            self.isdel = user_detail["isdel"]
            self.mobile = user_detail["mobile"]
            return True
        else:
            return False



if __name__ == '__main__':
    pass
