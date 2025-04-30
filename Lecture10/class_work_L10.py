Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
di
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    di
NameError: name 'di' is not defined. Did you mean: 'dir'?
try:
    print(di)
except NameError:
    print ("mistake")
    raise

mistake
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print(di)
NameError: name 'di' is not defined. Did you mean: 'dir'?

#Car (vin, model, body_type)

class Car:
    def __init__(self, vin, vol, body_type):
        self.vin = vin
        self.vol = vol
        self.body_type = body_type
    def __repr__(self):
        return f"Car ({self.vin}, {self.vol}, {self.body_type})"

    
lada1 = Car("12323", 1.67, "sedan")

lada1.__dict__
{'vin': '12323', 'vol': 1.67, 'body_type': 'sedan'}
di = lada1.__dict__
type(di)
<class 'dict'>
di.get
<built-in method get of dict object at 0x0000016E4464EC80>
di.get("vin")
'12323'
lada2=Car("132421", 1.9. "hatchback")
SyntaxError: invalid syntax
lada2=Car("132421", 1.9., "hatchback")
SyntaxError: invalid syntax
lada2=Car("132421", 1.9, "hatchback")
li = [lada1, lada2]
for car_inst in li:
    print (car_inst.vin)
    print (car_inst.vol)

    
12323
1.67
132421
1.9

for car_inst in li:
    for k, v in car_inst.__dict__.itens():
        print()
        print (k, ":", v)

        
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    for k, v in car_inst.__dict__.itens():
AttributeError: 'dict' object has no attribute 'itens'. Did you mean: 'items'?
for car_inst in li:
    for k, v in car_inst.__dict__.items():
        print()
        print (k, ":", v)'
        
SyntaxError: unterminated string literal (detected at line 4)
for car_inst in li:
    for k, v in car_inst.__dict__.items():
        print()
        print (k, ":", v)

        

vin : 12323

vol : 1.67

body_type : sedan

vin : 132421

vol : 1.9

body_type : hatchback



class Car:
    def __init__(blblbl, vin, vol, body_type):
        blblbl.vin = vin
        blblbl.vol = vol
        blblbl.body_type = body_type
    def __repr__(blblbl):
        return f"Car ({blblbl.vin}, {blblbl.vol}, {blblbl.body_type})"

    
lada3 = Car("2352", 2.0, "sedan")
lada3
Car (2352, 2.0, sedan)
lada3.body_type = "coupe"
lada3
Car (2352, 2.0, coupe)
lada2.new_var = 123
lada
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    lada
NameError: name 'lada' is not defined. Did you mean: 'lada1'?
lada3
Car (2352, 2.0, coupe)
lada2.__dict__
{'vin': '132421', 'vol': 1.9, 'body_type': 'hatchback', 'new_var': 123}
Car.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 4, '__init__': <function Car.__init__ at 0x0000016E46AFE520>, '__repr__': <function Car.__repr__ at 0x0000016E46AFE5C0>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
Car.__bases__
(<class 'object'>,)
class Car:
    def __init__(self, vin, vol, body_type):
        self.vin = vin
        self.vol = vol
        self.body_type = body_type
    def __repr__(self):
        return f"Car ({self.vin}, {self.vol}, {self.body_type})"
    def move(self):
        print("move")
    def turn(self, direc):
        print("turn", direc)
    def stop(self):
        print("stop")

        
class SportCar(Car):
    def __init__ (self):
        super().__init__(vin, vol, body_type, speed_limit = 270, max_speed=300)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f" SportCar {
KeyboardInterrupt
class SportCar(Car):
    def __init__ (self):
        super().__init__(vin, vol, body_type, speed_limit = 270, max_speed=300)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f"SportCar ({self.speed_limit}, {self.max_speed})"
    def race(self):
        print (f" race with {self.max_speed} km\h")

        
reno1 = SportCar("458035", 2.0, "coupe")
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    reno1 = SportCar("458035", 2.0, "coupe")
TypeError: SportCar.__init__() takes 1 positional argument but 4 were given
class SportCar(Car):
    def __init__ (self, vin, vol, body_type, speed_limit = 270, max_speed=300):
        super().__init__(vin, vol, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f"SportCar ({self.speed_limit}, {self.max_speed})"
    def race(self):
        print (f" race with {self.max_speed} km\h")

        
reno1 = SportCar("458035", 2.0, "coupe")
reno1
SportCar (270, 300)
class SportCar(Car):
    def __init__ (self, vin, vol, body_type, speed_limit = 270, max_speed=300):
        super().__init__(vin, vol, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        return super().__repr__() + "\n" f"SportCar ({self.speed_limit}, {self.max_speed})"
    def race(self):
        print (f" race with {self.max_speed} km\h")

        
reno1 = SportCar("458035", 2.0, "coupe")
reno1
Car (458035, 2.0, coupe)
SportCar (270, 300)



class Dog:
    def say(self, msg):
        print (msg)

        

class Cat:
    def say(self, msg):
        print (msg)

        

class Bird:
    def say(self, msg):
        print (msg)

        
d,c,b = Dog(), Cat(), Bird()
d.say ("dog"), c.say("cat"), b.say("kria")
dog
cat
kria
(None, None, None)




#Stack


class Stack:
    def __init__(self):
        self.__stack = []
        print ("Has been created")
    def push (self, value):
        self.__stack.append(value)
        print (value, "has been added")

        
class Stack:
    def __init__(self):
        self.__stack = []
        print ("Has been created")
    def push (self, value):
        self.__stack.append(value)
        self.__stack.append(value)
        print (value, "has been added")
    def pop (self):
        print (self.__stack.pop(), "has been removed")

        
s1 = Stack()
Has been created
s1.push(5)
5 has been added
class Stack:
    def __init__(self):
        self.__stack = []
        print ("Has been created")
    def push (self, value):
        self.__stack.append(value)
        self.__stack.append(value)
        print (value, "has been added")
    def pop (self):
        print (self.__stack.pop(), "has been removed")
    def sate(self):
        print ("current state status is")
        print (self.__stack)

        
class Stack:
    def __init__(self):
        self.__stack = []
        print ("Has been created")
    def push (self, value):
        self.__stack.append(value)
        self.__stack.append(value)
        print (value, "has been added")
    def pop (self):
        print (self.__stack.pop(), "has been removed")
        try:
            print (self.__stack.pop(), "has been removed")
        except:
            print ("Stack is empty")
    def sate(self):
        print ("current state status is")
        print (self.__stack)

        
s1 = Stack()
Has been created
s1.push(5)
5 has been added
s1.push(10)
10 has been added
s1.push(15)
15 has been added
s1.push(20)
20 has been added
s1.sate
<bound method Stack.sate of <__main__.Stack object at 0x0000016E46A174D0>>
s1.sate()
current state status is
[5, 5, 10, 10, 15, 15, 20, 20]
class Stack:
    def __init__(self):
        self.__stack = []
        print ("Has been created")
    def push (self, value):
        self.__stack.append(value)
        print (value, "has been added")
    def pop (self):
        print (self.__stack.pop(), "has been removed")
        try:
            print (self.__stack.pop(), "has been removed")
        except:
            print ("Stack is empty")
    def state(self):
        print ("current state status is")
        print (self.__stack)

        
class AddStacjValues (Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push (self, value):
        self.__summa +=value
    def get_summa(self):
        print(self.__summa)

        
s1 = Stack()
Has been created
s1.push(5)
5 has been added
s1 = Stack(33)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    s1 = Stack(33)
TypeError: Stack.__init__() takes 1 positional argument but 2 were given
s1.push(33)TypeError: Stack.__init__() takes 1 positional argument but 2 were given
SyntaxError: invalid syntax

s1.push(33)
33 has been added
s1.state
<bound method Stack.state of <__main__.Stack object at 0x0000016E46A170E0>>
s1 = AddStacjValues()
Has been created
s1.push(33)
s1.state(5)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    s1.state(5)
TypeError: Stack.state() takes 1 positional argument but 2 were given
a = 10
b = 5
a+b
15
>>> a.__add__(b)
15
>>> c, d = 3.13, 5.7
>>> c.__add__(d)
8.83
>>> c+d
8.83
>>> 
>>> 
>>> 
>>> 
>>> class Dog:
...     def __init__(self, number):
...         self.number = number
...     def __add__(self, dog_inst):
...         return self.number + dog_inst.number
... 
...     
>>> d1,d2 = Dog(4), Dog(6)
>>> d1.__add__(d2)
10
>>> d1+d2
10
>>> class Dog:
...     def __init__(self, name, age, color, salary):
...         self.name = name
...         self.age = age
...         self.color = color
...         self.salary = salary
...     def __add__(self, next_dog):
...         return self.salary + next_dog.salary
... 
...     
>>> d1, d2 = Dog("Joy", 12, "red", 1000), Dog("Djack", 10, "black", 2000)
>>> class Dog:
...     def __init__(self, name, age, color, salary):
...         self.name = name
...         self.age = age
...         self.color = color
...         self.salary = salary
...     def __add__(self, next_dog):
...         return self.salary + next_dog.salary
...     def __len__(self):
...         return self.age
... 
...     
>>>     
d1, d2 = Dog("Joy", 12, "red", 1000), Dog("Djack", 10, "black", 2000)
d1.__add__(d2)
3000
len(d1)
12
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __len__(self):
        return self.age
    def __sub__ (self, next_dog):
        return self.salary - next_dog.salary

    
d1, d2 = Dog("Joy", 12, "red", 1000), Dog("Djack", 10, "black", 2000)
d1-d2
-1000


class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __len__(self):
        return self.age
    def __sub__ (self, next_dog):
        return self.salary - next_dog.salary
    def __eq__ (self, next_dog):
        return self.age == next_dog.age
    def __ne__ (self, next_dog):
        return self.age != next_dog.age

    
d1, d2 = Dog("Joy", 12, "red", 1000), Dog("Djack", 10, "black", 2000)
d1==d2
False
d1!=d2
True
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __len__(self):
        return self.age
    def __sub__ (self, next_dog):
        return self.salary - next_dog.salary
    def __eq__ (self, next_dog):
        return self.age == next_dog.age
    def __ne__ (self, next_dog):
        return self.age != next_dog.age
    def __pow__(self, value):
         return self.age ** value
    def __mul__(self, next_dog):
         return self.age * next_dog.age

        
d1, d2 = Dog("Joy", 12, "red", 1000), Dog("Djack", 10, "black", 2000)
d1**2
144
d1*d2
120
