import json
import re
file = 'classmates.json'

class ClassMate:
    def __init__(self,name,age,tel,passwd):
        self._name = name
        self._age = age
        self._tel = tel
        self._passwd = passwd

class Manage_System:
    def __init__(self):
        self._user = {}
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self,user):
        self._user = user

    def add(self,mate:ClassMate):
        if not self.user.get(mate._name):
            self.user.update({str(mate._name):{'age': str(mate._age),'tel': str(mate._tel),'passwd':str(mate._passwd)}})
            with open(file, 'w+') as f:
                json.dump(self.user,f)
            print('add sucess user={}\tage={}\ttel={}\tpassword={}'.format(mate._name,mate._age,mate._tel,'*'*len(mate._passwd)))
        else:
            print('classmate is exist')

    def update(self,mate:ClassMate):
        if  self.user.get(mate._name):
            self.user.update({str(mate._name):{'age': str(mate._age),'tel': str(mate._tel),'passwd':str(mate._passwd)}})
            with open(file, 'w+') as f:
                json.dump(self.user,f)
            print('update sucess user={}\tage={}\ttel={}\tpassword={}'.format(mate._name,mate._age,mate._tel,'*'*len(mate._passwd)))
        else:
            print('classtmate not exist')

    def delete(self):
        name = input('Please input a name').strip()
        self.user.pop(name)
        with open(file, 'w+') as f:
            json.dump(self.user, f)
        print('{} is delete.'.format(name))

    def lst(self):
        type = input('please input type in user age tel]\n').strip()
        print('{:<10} {:<5} {:<10} {:<10}'.format('User', 'Age', 'Tel', 'Password'))
        print('-' * 10, '-' * 5, '-' * 10, '-' * 10)

        if type == 'user':
            for i in sorted(self.user.items(),key= lambda x:x,reverse=False):
                print('{:<10} {:<5} {:<10}'.format(i[0], i[1]['age'], i[1]['tel']), '*' * len(str(i[1]['passwd'])))
        elif type == 'age':
            for i in sorted(self.user.items(), key=lambda x: x[1]['age'], reverse=False):
                print('{:<10} {:<5} {:<10}'.format( i[0],i[1]['age'], i[1]['tel']), '*' * len(str(i[1]['passwd'])))

        elif type == 'tel':
            for i in sorted(self.user.items(), key=lambda x: x[1]['tel'], reverse=False):
                print('{:<10} {:<5} {:<10}'.format(i[0], i[1]['age'], i[1]['tel']), '*' * len(str(i[1]['passwd'])))
        else:
            print('error')

    def find(self):
        usr = input('please input a name:\n').strip()
        for k, v in self.user.items():
            if k == usr:
                passwd =  v.get('passwd')
                print('age={}\ntel={}\npassword={}'.format(v.get('age'),v.get('tel'),'*' * len(passwd)))

def verify_msg(cls):
    def _verify(self):
        src = self.user
        use = input('please input user\n').strip()
        for k, v in src.items():
            if k == use:
                passwd = v.get('passwd')
                password = input('please input password\n').strip()
                if passwd == password:
                    print('welcome user:{} password:{} log in\n'.format(use, '*' * len(passwd)))
                    break
                else:
                    print('password is wrong\n')
                    return -1
        else:
            print('user name input wrong\n')
            return -2
        return 0
    cls.verify = _verify
    return cls

@verify_msg
class Verify_Manage_System(Manage_System):pass

pattern = '^(?P<name>[a-z]{,20}):(?P<age>[1-9]?\d):(?P<tel>[\d+]{5,11}):(?P<passwd>\w+)$'
regex = re.compile(pattern)

def msg_input():
    mes = input('please input name:age:telephone:password\n').strip()
    matcher = regex.match(mes)
    newone = None
    if matcher:
        newone = ClassMate(matcher.groupdict()['name'], matcher.groupdict()['age'], matcher.groupdict()['tel'], matcher.groupdict()['passwd'])
    return newone


if __name__=='__main__':
    manage = Verify_Manage_System()
    with open(file, 'r') as f:
        s = json.load(f)
    manage.user = s
    while True:
        flag = manage.verify()
        if not flag:
            break
    while True:
        logs = """
        please input options in list:
        [1]add
        [2]delete
        [3]update
        [4]find
        [5]list
        [6]exit
        """
        print(logs)
        opt = input().strip()
        if opt == '1' or opt == 'add':
            one = msg_input()
            if not one == None:
                manage.add(one)
        elif opt == '2' or opt=='delete':
            manage.delete()
        elif opt == '3' or opt == 'update':
            one = msg_input()
            if not one == None:
                manage.update(one)
        elif opt == '4'or opt == 'find':
           manage.find()
        elif opt == '5' or opt == 'list':
            manage.lst()
        elif opt == '6'or opt == 'exit':
            print('exit')
            break
        else:
            print('error')