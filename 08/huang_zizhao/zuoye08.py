#!/usr/bin/env python
# coding: utf-8

# 本周作业：
# 编写一个学生管理系统类---Gradebook:
# 要求能动态的添加学生-name 和学生成绩grades(一个学生可以有个多科的科目成绩)，并
# 且根据学生名字能算出学生的平均成绩：
# 提示：可以预先初始化一个字典，用实例字典存储相应的信息

import functools

class GradeBook:

    def __init__(self):
        self._grades = {}

    def add(self,name,subject,grade):
        self._grades[name][subject] = grade

    def get_average(self,name):
        if name in self._grades.keys():
            grades = self._grades.values()
            num = len(num)
            if num !=0:
                return sum(grades) // num
            else:
                print("Not Found Any Subjects Of {name}".format(name=name))
        else:
            print("Not Found This Student {name}".format(name=name))

        return -1


class Student:

    def __init__(self, name):
        self._name = name
        self._subjects = dict()

    def add_subject(self, subject, grade):
        self._subjects[subject] = grade

    def get_average(self):
        values = self._subjects.values()
        num = len(values)
        sum = functools.reduce(lambda x,y: x+y, values, 0)
        return sum / num if num !=0 else 0

    # Not work in set and dict
    def __hash__(self):
        return self._name.__hash__()
    
    def __str__(self):
        return str({self_name: self._subjects})
    

class GradeBook2:
    def __init__(self):
        self._students = dict()
        
    def add_student(self, *students):
        for student in students:
            if student._name not in self._students.keys():
                self._students[student._name] = student
            
    def get_student_average(self, student_name):
        if student_name in self._students.keys():
            return self._students[student_name].get_average()
        else:
            print("Can Not Found This Student.")
    
    def add_subject(self, student, subject, grade):
        if student._name in self._students.keys():
            student.add_subject(subject, grade)
        else:
            print("Please Add Student First.")
            
    def __str__(self):
        return str(self._students)

