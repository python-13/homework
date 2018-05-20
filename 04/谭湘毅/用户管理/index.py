#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: index.py
@time: 2018-05-18-15:44
"""

import os
from datetime import date, datetime

from conf import conf as  my_conf
from conf import template as my_template

from modules.Common import Common as my_Common
from modules.jsonhelper import jsonhelper as my_jsonhelper
from modules.clsUsers import clsUsers as my_clsUsers

from database.init_DB import init_DB as  my_init_DB

'''类描述'''


class Main(object):
    def __init__(self):
        pass

    def __str__(self):
        return '类的解释描述'


    def get_users(self):
        """
        显示用户的信息,用户新建、删除、解锁用户时显示用户基本信息
        :return: my_clsUsers()
        """
        username = my_Common.input_msg("请输入用户名:")
        # 创建一个用户实例
        _deluser = my_clsUsers()
        _deluser.username = username
        # 如果用户名存在,load用户信息成功
        if _deluser.load_user_info():
            # 先显示一下用户的信息
            my_Common.show_message(my_template.user_info.format(username=_deluser.username,
                                                                name=_deluser.name,
                                                                mobile=_deluser.mobile,
                                                                role=_deluser.role,
                                                                isdel="否" if _deluser.isdel == 0 else "是",
                                                                islocked="否" if _deluser.islocked == 0 else "是",
                                                                bindcard=_deluser.bindcard)
                                   , "NOTICE")
            return _deluser
        else:
            my_Common.show_message("用户名不存在!", "ERROR")
            return False


# 函数 init_database 初始化数据库
if __name__ == '__main__':

    '''类的初始化'''
    initdb = my_init_DB()#初始类的时候 自动创建 json 字典库

    today = datetime.now().strftime("%Y-%m-%d")
    weekoftoday = date.weekday(datetime.now())

    # 用户初始化
    curruser = my_clsUsers()

    # --------- 开始 主程序 --------------
    exitFlag = False
    while not exitFlag:# 根据是否登录显示不同的登录界面
        if not curruser.islogin:
            print(my_template.index_default_menu.format("欢迎您,请登录",
                                                        today,
                                                        my_Common.numtochr(weekoftoday)
                                                        )
                  )
        else:
            print(my_template.index_logined_menu.format("欢迎您: {0}".format(curruser.name),
                                                        today,
                                                        my_Common.numtochr(weekoftoday)
                                                        )
                  )

        choose = my_Common.input_msg("选择功能编号[1-3]: ", ("1", "2", "3")).strip()

        if choose == "3":#【3】退出系统
            exitFlag = True
            continue

        if choose == "1":# 1 用户登录
            # curruser.
            if (curruser.islogin):
                # 用户已登录
                # 如果用户已经登录,菜单功能2为个人中心,调用另一个菜单模板 index_user_center
                print(my_template.index_user_center.format(curruser.name,
                                                           today,
                                                           my_Common.numtochr(weekoftoday)
                                                           )
                      )

                _chooseflag = False
                while not _chooseflag:
                    _choose = input("选择功能：")
                    if _choose not in ("1", "2", "3", "4"):
                        my_Common.show_message("选择正确的功能编号!", "ERROR")
                        continue
                    else:
                        _chooseflag = True
                    if _choose == "4":  # 返回上级菜单
                        _chooseflag = True
                        continue
                    if _choose == "3":  # 注销
                        curruser.logout()
                    if _choose == "1":  # 修改密码
                        result = curruser.modify_password()
                        if not result:
                            my_Common.show_message("密码修改错误!", "ERROR")
                            _chooseflag = True
                            continue
                    if _choose == "2":  # 修改资料
                        curruser.modify_user_info()
            else:
                curruser.login()  # 登录判断
                continue

        # 4 后台管理
        if choose == "2":
            if curruser.islogin:
                if curruser.role == "admin":
                    quit_flag = False
                    while not quit_flag:
                        _show_template = my_template.index_admin
                        print(_show_template.format(username=curruser.name))
                        # _choose = input("选择操作功能: ").strip().lower()
                        _choose = my_Common.input_msg("选择功能编号[1-4]: ", ("1", "2", "3", "4")).strip()
                        if _choose not in ("1", "2", "3", "4"):
                            my_Common.show_message("选择正确的功能编号!", "ERROR")
                            continue

                        if _choose == "4":#[4]退出后台管理
                            quit_flag = True
                            continue
                        if _choose == "1": #[1]创建新用户
                            _newuser = my_clsUsers() #新对象!!!
                            _newuser.init_user_info()
                        if _choose == "2":#[2]删除用户
                            my_main = Main()
                            _user = my_main.get_users() #!!!
                            if _user:
                                confirm = my_Common.input_msg("确定要删除此用户吗(y/n)?", ("y", "n"))
                                if confirm == "y":
                                    _user.del_user()
                                    my_Common.show_message("用户删除成功!", "NOTICE")
                        if _choose == "3": #[1]解锁用户
                            my_main = Main()
                            _user = my_main.get_users()
                            if _user:
                                confirm = my_Common.input_msg("确认解锁吗(y/n)?", ("y", "n"))
                                if confirm == "y":
                                    _user.unlock_user()
                                    my_Common.show_message("用户解锁成功!", "NOTICE")
                else:
                    # 不是 admin 角色无权限
                    my_Common.show_message("权限不够!", "ERROR")
            else:
                # exitFlag = True
                my_Common.show_message("请先登录系统!", "NOTICE")
                curruser.login()
                # continue
