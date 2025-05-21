Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
tp(1,2,3,3,4)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    tp(1,2,3,3,4)
NameError: name 'tp' is not defined
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})
    
SyntaxError: unterminated f-string literal (detected at line 6)
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
u1=User ("Kate", 41)
u1
User(Kate, 41)
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."

    
User.get_u_counter()
'User.user_counter = 0.'
u1=User ("Kate", 41)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    u1=User ("Kate", 41)
  File "<pyshell#15>", line 6, in __init__
    user_counter +=1
UnboundLocalError: cannot access local variable 'user_counter' where it is not associated with a value
u1=User ("Kate", 41


  User.get_u_counter()
         
SyntaxError: '(' was never closed
User.get_u_counter()
         
'User.user_counter = 0.'
u1
         
User(Kate, 41)
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."

    
u1=User ("Kate", 41)
u1
User(Kate, 41)
User.get_u_counter()
'User.user_counter = 1.'



class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value

        
User.get_u_counter()
'User.user_counter = 0.'
u1=User ("Kate", 41)
User.ch_u_counter(100)
User.get_u_counter()
'User.user_counter = 100.'
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value
    @staticmethod
    def name_checker(user_name):
        if len(user_name) <3:
            return user_name *4
        return user_name

    
u1=User("No", 45)
u1
User(No, 45)
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value
    @staticmethod
    def name_checker(user_name):
        if len(user_name) <3:
            return user_name *4
        return user_name

    


class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = User.name_checker(n)
        self.age = a
        User.user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}."
    @classmethod
    def ch_u_counter(cls, new_value):
        cls.user_counter = new_value
    @staticmethod
    def name_checker(user_name):
        if len(user_name) <3:
            return user_name *4
        return user_name

    


u1=User("No", 45)
u1
User(NoNoNoNo, 45)



#Export
#python data - txt, csv, xml
from abc import ABC, abstactmethod
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    from abc import ABC, abstactmethod
ImportError: cannot import name 'abstactmethod' from 'abc' (C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\abc.py). Did you mean: 'abstractmethod'?
from abc import ABC, abstractmethod
class Export(ABC):
    @abstractmethod
    def preparation (self):
        pass
    @abstractmethod
    def export_prep_data (self):
        pass

    
class ExportTXT(Export):
    def __init__ (self, data):
        self.data = data
    def preparation (self):
        pass
    def export_prep_data (self):
        pass

    

class A:
    a = 10
    def __init__ (self)
    
SyntaxError: expected ':'
class A:
    a = 1
    def __init__ (self):
        self.aa = 11
    def fun_a(self):
        retufn "fun_a"
        
SyntaxError: invalid syntax


class A:
    a = 1
    def __init__ (self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__ (self):
        self.bb = 22
    def fun_a(self):
        return "fun_b"

    
class C(B):
    a = 3
    def __init__ (self):
        self.cc = 33
    def fun_a(self):
        return "fun_c"

    
c_inst = C()
c_inst.cc
33
c_inst.c
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    c_inst.c
AttributeError: 'C' object has no attribute 'c'. Did you mean: 'cc'?
class C(B):
    b = 3
    def __init__ (self):
        self.cc = 33
    def fun_a(self):
        return "fun_c"

    
c_inst = C()
c_inst.c
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    c_inst.c
AttributeError: 'C' object has no attribute 'c'. Did you mean: 'cc'?
class C(B):
    c = 3
    def __init__ (self):
        self.cc = 33
    def fun_a(self):
        return "fun_c"

    
c_inst = C()

c_inst.c
3
c_inst.a
1
c_inst.fun_a
<bound method C.fun_a of <__main__.C object at 0x00000161FF586BA0>>
class B(A):
    b = 2
    def __init__ (self):
        self.bb = 22
    def fun_b(self):
        return "fun_b"


    

class C(B):
    a = 3
    def __init__ (self):
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.c
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    c_inst.c
AttributeError: 'C' object has no attribute 'c'. Did you mean: 'cc'?
    
c_inst = C()


    
c_inst = C()



c_inst.c
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    c_inst.c
AttributeError: 'C' object has no attribute 'c'. Did you mean: 'cc'?
class A:
    a = 1
    def __init__ (self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__ (self):
        super().__init__()
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__ (self):
        super().__init__()
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.c
3
c_inst.a
1
c_inst.b
2
c_inst.cc
33
c_inst.bb
22
c_inst.aa
11


C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
B.mro
<built-in method mro of type object at 0x00000161FF22B290>
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
A.mro()
[<class '__main__.A'>, <class 'object'>]



class A:
    a = 1
    var = 100
    def __init__ (self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B:
    b = 2
    var = 333
    def __init__ (self):
        super().__init__()
        self.bb = 22
    def fun_b(self):
        return "fun_b"

















        
        return "fun_b"

    


KeyboardInterrupt
class B:
    b = 2
    var = 333
    def __init__ (self):
        super().__init__()
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(A, B):
   pass

c_inst= C()
c_inst.a
1
c_inst.b
2
c_inst.var
100
C.mro()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


class A:
    def start(self)
    
SyntaxError: expected ':'
class A:
    def start(self):
        print("A - start")
    def job(self):
        self.start()

        
class B(A):
    def start(self):
        print("B - start")

        
B.mro
<built-in method mro of type object at 0x00000161FF229F30>
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
class A:
    def str(self):
        return "A - str"

    
class B(A):
    def str(self):
        return "B - str"

    
bb = B()
bb
<__main__.B object at 0x00000161FF586E40>
bb.str()
'B - str'
try:
    1/0
except: #если была ошибка
    print(0)
else: # если в try не было ошибок
    print("OK")
finally: #срабатывает всегда
    print("BUM!")

    
0
BUM!

class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter +=1
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
def user_input():
    n,a = input("name "), int(input("age ")
    if len(n) < 2:
                              
SyntaxError: '(' was never closed
def user_input():
    n,a = input("name "), int(input("age "))
    if len(n) < 2:
        pass #вызвать исключение Ошибка Длина имени
    if a < 0:
        pass #вызвать исключение Ошибка возраст отриц
    return User (n, a)

class UserNameError (Exception):
    def __init__(self, u_name, message = "Имя пользователя меньше двух символов - запрещено!"):
        self.u_name = u_name
        self.message = message

        
raise UserNameError
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    raise UserNameError
TypeError: UserNameError.__init__() missing 1 required positional argument: 'u_name'
raise UserNameError ("A")
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    raise UserNameError ("A")
UserNameError: A
class UserNameError (Exception):
    def __init__(self, u_name, message = "Имя пользователя меньше двух символов - запрещено!"):
        self.u_name = u_name
        self.message = message
    def __repr__(self):
        return self.message + "---->" + self.message

    
class UserAgeError (Exception):
    def __init__(self, u_age, message = "Отрицательный возраст - запрещено!"):
        self.u_age = u_age
        self.message = message
    def __repr__(self):
        return self.message + "---->" + self.message

    
def user_input():
    n,a = input("name "), int(input("age "))
    if len(n) < 2:
        raise UserNameError
    if a < 0:
        raise UserAgeError
    return User (n, a)

user_input("A", 5)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    user_input("A", 5)
TypeError: user_input() takes 0 positional arguments but 2 were given
class UserAgeError (Exception):
    def __init__(self, u_age, message = "Отрицательный возраст - запрещено!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return self.message + "---->" + self.message

    
try:
    user)input()
    
SyntaxError: unmatched ')'
class UserAgeError (Exception):
    def __init__(self, u_age, message = "Отрицательный возраст - запрещено!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return self.message + "---->" + self.message

    



#последний вариант
    
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

class UserNameError(Exception):
    def __init__(self, u_name, message="имя пользователя меньше 2-ух симоволов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __str__(self):
        return self.u_name + "-->" + self.message

class UserAgeError(Exception):
    def __init__(self, u_age, message="возраст пользователя не может быть меньше нуля!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return f"{self.u_age} --> {self.message}"

def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        raise UserNameError(n)
    if a < 0:
        raise UserAgeError(a)
    return User(n, a)

try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")
    
SyntaxError: invalid syntax
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
class UserNameError(Exception):
    def __init__(self, u_name, message="имя пользователя меньше 2-ух симоволов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __str__(self):
        return self.u_name + "-->" + self.message


class UserAgeError(Exception):
    def __init__(self, u_age, message="возраст пользователя не может быть меньше нуля!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return f"{self.u_age} --> {self.message}"

    
def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        raise UserNameError(n)
    if a < 0:
        raise UserAgeError(a)
    return User(n, a)

try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")

    
name 
age 
Чтото не так...

try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")

    
name K
age 5
K-->имя пользователя меньше 2-ух симоволов запрещено!
try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")

    
name Kate
age -5
-5 --> возраст пользователя не может быть меньше нуля!






#OUEUE

class Que:
    def __init__(self):
        self.__que = []
    def put (self, number)
    
SyntaxError: expected ':'
class Que:
    def __init__(self):
        self.__que = []
    def put (self, number):
        self.__que.append(number)
        print(""значение успешно добавлено")
              
SyntaxError: unterminated string literal (detected at line 6)
class Que:
    def __init__(self):
        self.__que = []
        print("Очередь создана")
    def put (self, number):
        self.__que.append(number)
        print("Значение успешно добавлено")
        print("Текущее значение очереди: , self.__que")
    def get(self):
        if len(self.__que) < 1:
            raise EmtyError
        del self.__que[0]
        print("Значение успешно удалено")
        print("Текущее значение очереди: , self.__que")

        
class EmptyQueError(Exception):
    """Очередь пуста"""
    pass
q1 = Que()
SyntaxError: invalid syntax
class EmptyQueError(Exception):
    """Очередь пуста"""
    pass

q1 = Que()
Очередь создана
for i in range(5):
    q1.put(i)

    
Значение успешно добавлено
Текущее значение очереди: , self.__que
Значение успешно добавлено
Текущее значение очереди: , self.__que
Значение успешно добавлено
Текущее значение очереди: , self.__que
Значение успешно добавлено
Текущее значение очереди: , self.__que
Значение успешно добавлено
Текущее значение очереди: , self.__que
for i in range(6):
    q1.get()

    
Значение успешно удалено
Текущее значение очереди: , self.__que
Значение успешно удалено
Текущее значение очереди: , self.__que
Значение успешно удалено
Текущее значение очереди: , self.__que
Значение успешно удалено
Текущее значение очереди: , self.__que
Значение успешно удалено
Текущее значение очереди: , self.__que
Traceback (most recent call last):
  File "<pyshell#278>", line 2, in <module>
    q1.get()
  File "<pyshell#266>", line 11, in get
    raise EmtyError
NameError: name 'EmtyError' is not defined. Did you mean: 'EOFError'?
class Que:
    def __init__(self):
        self.__que = []
        print("Очередь создана")
    def put (self, number):
        self.__que.append(number)
...         print("Значение успешно добавлено")
...         print("Текущее значение очереди: " , self.__que)
...     def get(self):
...         if len(self.__que) < 1:
...             raise EmtyError
...         del self.__que[0]
...         print("Значение успешно удалено")
...         print("Текущее значение очереди: " , self.__que)
... 
...         
>>> q1 = Que()
Очередь создана
>>> for i in range(5):
...     q1.put(i)
... 
...     
Значение успешно добавлено
Текущее значение очереди:  [0]
Значение успешно добавлено
Текущее значение очереди:  [0, 1]
Значение успешно добавлено
Текущее значение очереди:  [0, 1, 2]
Значение успешно добавлено
Текущее значение очереди:  [0, 1, 2, 3]
Значение успешно добавлено
Текущее значение очереди:  [0, 1, 2, 3, 4]
>>> for i in range(6):
...     q1.get()
... 
...     
Значение успешно удалено
Текущее значение очереди:  [1, 2, 3, 4]
Значение успешно удалено
Текущее значение очереди:  [2, 3, 4]
Значение успешно удалено
Текущее значение очереди:  [3, 4]
Значение успешно удалено
Текущее значение очереди:  [4]
Значение успешно удалено
Текущее значение очереди:  []
Traceback (most recent call last):
  File "<pyshell#285>", line 2, in <module>
    q1.get()
  File "<pyshell#280>", line 11, in get
    raise EmtyError
NameError: name 'EmtyError' is not defined. Did you mean: 'EOFError'?
