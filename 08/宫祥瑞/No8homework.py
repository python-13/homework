class Student:
    def __init__(self, name:str, math:int, chinese:int, english:int):
        self._name = name
        self._math = math
        self._chinese = chinese
        self._english = english


class Grdebook:
    def __init__(self):
        self._grades = dict()

    def add(self,stu:Student):
        self._grades.update({stu._name: [stu._math, stu._chinese, stu._english]})

    def average_scores(self,name):
        for k, v in self._grades.items():
            if k == name:
                return sum(v)/len(v)

    def show_scores(self,name):
        avg = self.average_scores(name)
        print('name\tmath\tchinese\tenglish\taverage')
        print('{:<5}\t'.format(name),end='')
        for i in self._grades[name]:
            print('{:<5}\t'.format(i),end='')
        print('{:<5}\t'.format(avg))

if __name__ == '__main__':
    log = """
        学生管理系统
    【1】增加学生信息
    【2】查询成绩
    【3】退出
    """
    gradebook = Grdebook()
    while True:
        print(log)
        opt = input().strip()

        if opt == '1':
            while True:
                name = str(input('Please input name:').strip())
                math = int(input('Please input math score:').strip())
                chinese = int(input('Please input chinese score:').strip())
                english = int(input('Please input english score:').strip())
                if len(name) < 20:
                    if math <= 100 and math >= 0:
                        if chinese <= 100 and chinese >= 0:
                            if english <= 100 and english >= 0:
                                break
                print('input worng')
            gradebook.add( Student(name,math,chinese,english))
            print('add name:{} math:{} chinese{} english:{} sucess'.format(name,math,chinese,english))

        elif opt == '2':
            name = input('Please input name\n').strip()
            gradebook.show_scores(str(name))

        elif opt == '3':
            print('quit')
            break

        else:
            print('key error')
            
  # 可以考虑再解耦下，编写三个类：学生类，科目类，成绩类，试试
