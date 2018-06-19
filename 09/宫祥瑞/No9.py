
class To_dictMixin:
    def to_dict(self):
        property = self.__dict__
        return property

class Students:
    def __init__(self,name:str,age:int,score:int):
        self.name = name
        self.age = age
        self.score =score


class Dict_students(To_dictMixin,Students):pass


bob = Dict_students('bob',18,80)
lisa  = Dict_students('lisa',22,75)
print(bob.to_dict())
print(lisa.to_dict())