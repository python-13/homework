class DictMixin:
    def to_dict(self):
        return self.__dict__


class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def to_dict(self):
        print('old')


class Test2(DictMixin, Test):
    def __init__(self):
        super().__init__()


test = Test2()
print(test.to_dict())
