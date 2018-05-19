#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: conf.py
@time: 2018-05-18-15:52
"""

'''类描述'''

import os

# BASE_DIR = '/Users/davetan/Desktop/mypython/python90day/作业1/用户管理'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件存放路径
LOG_PATH = os.path.join(BASE_DIR, "logs")

'''
json 数据存放的地方
'''

DATABASE = dict(enginner='file',
				dbpath=os.path.join(BASE_DIR,'database'),
				tables={'users':'users'}
				)

# 用户登录失败最大次数
ERROR_MAX_COUNT = 3