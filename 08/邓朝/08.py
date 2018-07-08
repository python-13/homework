class Student:
    def __init__(self, name: str):
        self.name = name
        self.grade = {}


class StudentBook:
    def __init__(self):
        self.book = {}

    def addstudent(self, name: str):
        if self.book.get(name) is None:
            self.book[name] = Student(name)
        else:
            pass

    def addgrade(self, name: str, sub: str, res: int):
        if self.book.get(name):
            self.book[name].grade[sub] = res
        else:
            self.book[name] = Student(name)
            self.book[name].grade[sub] = res

    def show(self, name: str):
        return (name, self.book[name].grade)

    def showall(self):
        return [(k, v.grade) for k, v in self.book.items()]

    def avg(self, name: str):
        if self.book.get(name) is None:
            print('Out of the catalog')
        else:
            return sum(self.book[name].grade.values()) // len(self.book[name].grade.keys())


book = StudentBook()
book.addgrade('deng', 'eng', 60)
book.addgrade('deng', 'math', 70)
book.addstudent('deng3')
book.addgrade('deng3', 'eng', 90)
book.addgrade('deng4', 'eng', 20)
book.addgrade('deng4', 'math', 77)
book.addgrade('deng4', 'chi', 35)
print(book.showall())
print(book.show('deng4'))
print('avg', book.avg('deng4'))
