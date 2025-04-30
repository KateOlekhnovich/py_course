Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
##CRM client - name, phone, email,
#client - name, phone, email
client1=["Dima", 3425335, "dima@mail.ru"]
client2=["Pasha", 4554757, "pasha@mail.ru"]


#wallet, car, do
class Wallet:
    pass

a=10
b='nd'
wallet1=Wallet()
type(a)
<class 'int'>
type(b)
<class 'str'>
type(wallet1)
<class '__main__.Wallet'>
class Dog:
    pass
class Car:
    
SyntaxError: invalid syntax

class Dog:
pass
SyntaxError: expected an indented block after class definition on line 1
calss Dog:
    
SyntaxError: invalid syntax
class Dog:
    pass

bobik=Dog()
type (bobik)
<class '__main__.Dog'>
class Car:
    pass

lada=car()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lada=car()
NameError: name 'car' is not defined. Did you mean: 'Car'?
lada=Car()
type(lada)
<class '__main__.Car'>




#wallet - id amount owner

class Wallet:
    def __init__ (self, wid, wamount,wonvner):
        pass

    
wallet1(2, 100, "vasia")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    wallet1(2, 100, "vasia")
TypeError: 'Wallet' object is not callable
wallet = Wallet(2, 100, "vasya")

class Wallet:
    def __init__ (self, wid, amount, owner):
        self.wallet_id = wid
        swlf.wallet_amount = amount
        self.wallet_owner = owner

        
wallet1 = Wallet(2,100, "Vasia")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    wallet1 = Wallet(2,100, "Vasia")
  File "<pyshell#50>", line 4, in __init__
    swlf.wallet_amount = amount
NameError: name 'swlf' is not defined. Did you mean: 'self'?
class Wallet:
    def __init__ (self, wid, amount, owner):
        self.wallet_id = wid
        self.wallet_amount = amount
        self.wallet_owner = owner

        
wallet1 = Wallet(2,100, "Vasia")

wallet1
<__main__.Wallet object at 0x0000020548E82E40>
wallet1.wallet_id
2
wallet1.wallet_owner
'Vasia'


class Dog:
    def __init__ (self, name, age)
    
SyntaxError: expected ':'
class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

        
bobik = Dog("bobik", 1)
bobki.age
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    bobki.age
NameError: name 'bobki' is not defined. Did you mean: 'bobik'?
bobik.age
1
class User:
    def __init__ (self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
Client1 = User ("Dima", 98393)
Client2 = User ("Nikita", 938493, "mail@mail.ru")
Client1.name
'Dima'
Client1.phone
98393


storage = []
client_storage = []
n = 4
for i in range (1, n+1)
SyntaxError: expected ':'
for i in range (1, n+1):
    print ("Client number is:", i)
    name = input ("name: ")
    phone = input ("phone: ")
    email = input ("eamil: ")
    client = Client (name, phone, email)
    client_storage.append(client)

    
Client number is: 1
name: Vasya
phone: 39393
eamil: 
Traceback (most recent call last):
  File "<pyshell#94>", line 6, in <module>
    client = Client (name, phone, email)
NameError: name 'Client' is not defined. Did you mean: 'Client1'?
for i in range (1, n+1):
    print ("Client number is:", i)
    name = input ("name: ")
    phone = input ("phone: ")
    email = input ("eamil: ")
    client = User(name, phone, email)
    client_storage.append(client)

    
Client number is: 1
name: Katya
phone: 38358
eamil: 
Client number is: 2
name: Vasya
phone: 43432-
eamil: 
Client number is: 3
name: Olga
phone: 98309527
eamil: kdfssd
Client number is: 4
name: Pasha
phone: 23242424
eamil: erhglr
def show clients(clients):
    
SyntaxError: expected '('
def show_clients(clients):
    print ("name: " user.name)
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def show_clients(clients):
    print ("name: " client.name)
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def show_clients(clients):
    for client in clients:
        print ("name: ", client.name)
        print ("phone: ", client.phone)
        print ("email: ", client.email)
        print()
    print()

    
show_clients(client_storage)
name:  Katya
phone:  38358
email:  

name:  Vasya
phone:  43432-
email:  

name:  Olga
phone:  98309527
email:  kdfssd

name:  Pasha
phone:  23242424
email:  erhglr


n = int(input ("How many clients are going to create?: ")
    for i in range (1, n+1):
    print ("Client number is:", i)
        name = input ("name: ")
        phone = input ("phone: ")
        email = input ("eamil: ")
        client = User(name, phone, email)client_storage.append(client)
        
SyntaxError: '(' was never closed
n = int(input ("How many clients are going to create?: ")
for i in range (1, n+1):
    print ("Client number is:", i)
    name = input ("name: ")
    phone = input ("phone: ")
    email = input ("eamil: ")
    client = User(name, phone, email)
    client_storage.append(client)
        
SyntaxError: '(' was never closed
n = int(input ("How many clients are going to create?: "))
for i in range (1, n+1):
    print ("Client number is:", i)
    name = input ("name: ")
    phone = input ("phone: ")
    email = input ("eamil: ")
    client = User(name, phone, email)
    client_storage.append(client)
        
SyntaxError: multiple statements found while compiling a single statement
n = int(input ("How many clients are going to create?: "))
        
How many clients are going to create?: 2
for i in range (1, n+1):
    print ("Client number is:", i)
    name = input ("name: ")
    phone = input ("phone: ")
    email = input ("eamil: ")
    client = User(name, phone, email)
    client_storage.append(client)

        
Client number is: 1
name: rjrt
phone: df
eamil: df
Client number is: 2
name: df
phone: gdf
eamil: gdf
df
        
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    df
NameError: name 'df' is not defined
class Dog:
    class_var = 0
    def __init__ (self, name, age):
        self.name = name
        self.age = age

        
Dog.class_var
0
dog1 = Dog("Dog", 1)
dog1
<__main__.Dog object at 0x0000020548E82900>
dog1.name
'Dog'
dog1.name = "DoggY"
dog1.name
'DoggY'
class Task^
SyntaxError: invalid syntax
class Task:
    counter = 1
    def __init__ (self, name):
        self.task_id = Task.counter
        self.task_name = name
        self.task_status = False

        
class Task:
    counter = 1
    def __init__ (self, name):
        self.task_id = Task.counter
        Task.counter += 1
        self.task_name = name
        self.task_status = False

        
t1 = Task("go")
t1 = Task("run")
t2 = Task("run")
t1 = Task("go")
print (t1.task_id, t1.task_name, t1.task_status)
4 go False
print (t2.task_id, t2.task_name, t2.task_status)
3 run False
Task.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'counter': 5, '__init__': <function Task.__init__ at 0x0000020548FA18A0>, '__static_attributes__': ('task_id', 'task_name', 'task_status'), '__dict__': <attribute '__dict__' of 'Task' objects>, '__weakref__': <attribute '__weakref__' of 'Task' objects>, '__doc__': None})



class f:
    """ Документация"""
    a = 9
    def __init__(self):
        pass

    
help (f)
Help on class f in module __main__:

class f(builtins.object)
 |  Документация
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  a = 9

f.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__doc__': 'Документация', 'a': 9, '__init__': <function f.__init__ at 0x0000020548FA2520>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'f' objects>, '__weakref__': <attribute '__weakref__' of 'f' objects>})


class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")

        
barsik = Cat ("Barsik", 5)

barsik.hello()
Hello! My name is Barsik, and I'm 5 years old!
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
        
SyntaxError: unexpected indent
class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
    def say (self, msg):
        print (f"{self.name} says {msg}")

        
barsik = Cat ("Barsik", 5)
barsik.say("HIIIII")
Barsik says HIIIII
class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
    def say (self, msg):
        print (f"{self.name} says {msg}")
    def grow(self):
        self.grow +=1

        
barsik = Cat ("Barsik", 5)
barsik.hello
<bound method Cat.hello of <__main__.Cat object at 0x0000020548E830E0>>
barsik.hello()
Hello! My name is Barsik, and I'm 5 years old!
barsik.grow
<bound method Cat.grow of <__main__.Cat object at 0x0000020548E830E0>>
barsik.grow()
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    barsik.grow()
  File "<pyshell#178>", line 10, in grow
    self.grow +=1
TypeError: unsupported operand type(s) for +=: 'method' and 'int'
barsik.grow()
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    barsik.grow()

  File "<pyshell#178>", line 10, in grow
    self.grow +=1
TypeError: unsupported operand type(s) for +=: 'method' and 'int'
class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
    def say (self, msg):
        print (f"{self.name} says {msg}")
    def grow(self):
        self.age +=1

        

barsik = Cat ("Barsik", 5)
barsik.grow()
barsik.hello()
Hello! My name is Barsik, and I'm 6 years old!
class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
    def say (self, msg):
        print (f"{self.name} says {msg}")
    def grow(self):
        self.age +=1
    def __repr__(self):
        return f"cat info. \n name:{self.name}, \n age:{self.age}"

    
barsik = Cat ("Barsik", 5)
barsik
cat info. 
 name:Barsik, 
 age:5
class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
    def say (self, msg):
        print (f"{self.name} says {msg}")
    def grow(self):
        self.age +=1
    def __repr__(self):
        return f"cat info. \nname:{self.name}, \nage:{self.age}"
    def __str__(self):
        return f"{self.name} |  {self.age}"

    
barsik = Cat ("Barsik", 5)
print(barsik)
Barsik |  5

barsik
cat info. 
name:Barsik, 
age:5
def = Dog:
    
SyntaxError: invalid syntax
def Dog():
    pass
Dog.__bases__
SyntaxError: invalid syntax
Dog.__bases__
(<class 'object'>,)
# swimming cat

class SwimCat (Cat):
    def swim(self):
        print("I can swim!")

        
sadik = SwimCat("Sadic", 2)
sadik
cat info. 
name:Sadic, 
age:2
sadik.grow()
sadik.hello()
Hello! My name is Sadic, and I'm 3 years old!
Hello! My name is Sadic, and I'm 3 years old!
SyntaxError: unterminated string literal (detected at line 1)

class SwimCat (Cat):
    def swim(self):
        print("I can swim!")
    def __str__(self):
        return f"Swimming cat {self.name} |  {self.age}"

    
sadik = SwimCat("Sadic", 2)
sadik
cat info. 
name:Sadic, 
age:2
print (sadik)
Swimming cat Sadic |  2
class SwimCat (Cat):
    def __init__ (self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def swim(self):
        print("I can swim!")
    def __str__(self):
        return f"Swimming cat {self.name} |  {self.age}"

    
sadik = SwimCat("Sadic", 2, "red")
sadik.__dict__
{'name': 'Sadic', 'age': 2, 'color': 'red'}
class SwimCat (Cat):
    def __init__ (self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def swim(self):
        print("I can swim!")
    def __str__(self):
        return f"Swimming cat {self.name} |  {self.age}"
    def hello(self):
        super().hello()
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old, and my color {self.color}!")

        
sadik = SwimCat("Sadic", 2, "red")

sadik.hello()
Hello! My name is Sadic, and I'm 2 years old!
Hello! My name is Sadic, and I'm 2 years old, and my color red!


class SwimCat (Cat):
    def __init__ (self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def swim(self):
        print("I can swim!")
    def __str__(self):
        return f"Swimming cat {self.name} |  {self.age}"
    def hello(self):
        super().hello()
        print (f"My color is {self.color}!")

        
sadik = SwimCat("Sadic", 2, "red")
sadik.hello()

Hello! My name is Sadic, and I'm 2 years old!
My color is red!




class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.name}, and I'm {self.age} years old!")
    def __str__(self):
        return f"{self.name} |  {self.age}"

    
c1 = Cat("Maks", 1)
c1.name = "Pupsik"
ca
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    ca
NameError: name 'ca' is not defined. Did you mean: 'a'?
c1
<__main__.Cat object at 0x0000020548E83620>
class Cat:
    def __init__ (self, name, age):
        self.__name = name
        self.age = age
    def hello(self):
        print (f"Hello! My name is {self.__name}, and I'm {self.age} years old!")
   
    def __repr__(self):
...         return f"cat info. \nname:{self.__name}, \nage:{self.age}"
...     def __str__(self):
...         return f"{self.__name} |  {self.age}"
... 
...     
>>> c1 = Cat("Maks", 1)
... 
>>> c1.name = "Pupsik"
>>> c1
cat info. 
name:Maks, 
age:1
>>> class Cat:
...     def __init__ (self, name, age):
...         self.__name = name
...         self.age = age
...     def hello(self):
...         print (f"Hello! My name is {self.__name}, and I'm {self.age} years old!")
...    
...     def __repr__(self):
...         return f"cat info. \nname:{self.__name}, \nage:{self.age}"
...     def __str__(self):
...         return f"{self.__name} |  {self.age}"
...     def chane_name (self, name):
...         self.__name = name
... 
...         
>>> c1 = Cat("Maks", 1)
>>> c1.name = "fsh"
>>> c1
cat info. 
name:Maks, 
age:1
>>> c1.__name = "dhshjh"
>>> 
>>> c1
cat info. 
name:Maks, 
age:1
