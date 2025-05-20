Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class A:
    def __init__(self, f, b):
        self.f = f
        self.b = b
    def __str__(self):
        return f"A ({self.f}, {self.b})"

    
A= classA(1,5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    A= classA(1,5)
NameError: name 'classA' is not defined
A = A(435,43)

a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
A
<__main__.A object at 0x000001DB10596A50>
print (A)
A (435, 43)
class Singleton:
    __intstanse__= None
    def __init__(self):
        if Singleton._instanse is None:
            Singletone.__instance = self
        else:
            raise Exception ("У данного можетбыть только один экземпляр 1")

        
a = Singleton()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a = Singleton()
  File "<pyshell#20>", line 4, in __init__
    if Singleton._instanse is None:
AttributeError: type object 'Singleton' has no attribute '_instanse'. Did you mean: '__intstanse__'?
AttributeError: type object 'Singleton' has no attribute '_instanse'. Did you mean: '__intstanse__'?
SyntaxError: invalid syntax


class Singleton:
    __intstanse__= None
    def __init__(self):
        if Singleton._instanse is None:
            Singleton.__instance = self
        else:
            raise Exception ("У данного можетбыть только один экземпляр 1")
            


a = Singleton()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a = Singleton()
  File "<pyshell#25>", line 4, in __init__
    if Singleton._instanse is None:
AttributeError: type object 'Singleton' has no attribute '_instanse'. Did you mean: '__intstanse__'?
class Singleton:
    __intstanse__= None
    def __init__(self):
        if Singleton.__instanse is None:
            Singleton.__instance = self
        else:
            raise Exception ("У данного можетбыть только один экземпляр 1")

        
a = Singleton()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a = Singleton()
  File "<pyshell#29>", line 4, in __init__
    if Singleton.__instanse is None:
AttributeError: type object 'Singleton' has no attribute '_Singleton__instanse'


class DBCon:
    __instance = None
    def __init__ (self, db_name):
        if DBCon.__instance is None:
            DBCon.__instance = self
            self.db_name = db_name
        else:
            raise MultipleDataBaseCOnnectionError
        def __repr__(self):
            return f" Соединение с БД {self.db_name}"

        
class MultipleDataBaseCOnnectionError(Exception):
    pass

conn = DBCon("account_info.db")
print (con)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print (con)
NameError: name 'con' is not defined. Did you mean: 'conn'?
print (conn)
<__main__.DBCon object at 0x000001DB10596CF0>
print (DBCon._DBCon__instance)
<__main__.DBCon object at 0x000001DB10596CF0>
conn1 = DBCon("account2_info.db")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    conn1 = DBCon("account2_info.db")
  File "<pyshell#44>", line 8, in __init__
    raise MultipleDataBaseCOnnectionError
MultipleDataBaseCOnnectionError
class Singleton:
    __instance__= None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception ("У данного можетбыть только один экземпляр 1")

        
a = Singleton()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a = Singleton()
  File "<pyshell#54>", line 4, in __init__
    if Singleton.__instance is None:
AttributeError: type object 'Singleton' has no attribute '_Singleton__instance'
class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception ("У данного можетбыть только один экземпляр 1")

        
a = Singleton()
B = Singleton()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    B = Singleton()
  File "<pyshell#57>", line 7, in __init__
    raise Exception ("У данного можетбыть только один экземпляр 1")
Exception: У данного можетбыть только один экземпляр 1







class Creator:
    sub_list = []
    def follow(self, follower):
        sub_list.append(follower):
            
SyntaxError: invalid syntax
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(slef.sub_list)

        
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(slef.sub_list)
    def create_post(self, mes)
    
SyntaxError: expected ':'
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(slef.sub_list)
    def create_post(self, mes):
        print (self.creator_name, "опубликовал это сообщение:")
        print(mes)
        print ()

        
creator1 = Creator("My channel")
creator1.create_post("dhsh")
My channel опубликовал это сообщение:
dhsh

class Follower:
    def __init__ (self, name):
        self.follower_name = name
        def react (self):
            print (self.follower_name, "лайкает сообщение:")
        def __str__(self):
            return f"follower ({self.follower_name})"
        def __repr__(self):
            return f"follower ({self.follower_name})"

        
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(slef.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, mes):
        print (self.creator_name, "опубликовал это сообщение:")
        print(mes)
        print ()

        

creator1=Creator("1st chan")
f1= Follower("KAte")
f2= Follower("Anna")
f3= Follower("Peter")
creator1.show_followers()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    creator1.show_followers()
  File "<pyshell#90>", line 8, in show_followers
    print(slef.sub_list)
NameError: name 'slef' is not defined
class Creator:
    def __init__(self, name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, mes):
        print (self.creator_name, "опубликовал это сообщение:")
        print(mes)
        print ()

        
creator1=Creator("1st chan")
creator1.show_followers()
[]
creator1.follow(f1)
creator1.create_post("dsksf")
1st chan опубликовал это сообщение:
dsksf

f1.react()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    f1.react()
AttributeError: 'Follower' object has no attribute 'react'
class Follower:
    def __init__ (self, name):
        self.follower_name = name
        def react (self):
            print (self.follower_name, "лайкает сообщение:")
        def __str__(self):
            return f"follower ({self.follower_name})"
        def __repr__(self):
            return f"follower ({self.follower_name})"

        
#Decorator
        
def add_five(number):
    return number + 5

def change(func):
    def inner (inner_number):
        func(inner_number*2)
    return inner

@change
def add_five(number):
    return number + 5

add_five(5)

def change(func):
    def inner (inner_number):
        return func(inner_number*2)
    return inner

@change
def add_five(number):
    return number + 5

add_five(5)
15


def change(func):
    print("декоратор скушал имя функции")
    def inner (inner_number):
        print("всесто оригинала запущена inner функция")
        return func(inner_number*2)
    return inner

def add_five(number):
    print("Примеры разбор ДЗ лекции 13")
    return number + 5

@change
def add_five(number):
    return number + 5

    
декоратор скушал имя функции
add_five(5)
всесто оригинала запущена inner функция
15
add_five(10)
всесто оригинала запущена inner функция
25
def sub_five(number):
    return number - 5

sub_five(5)
0
@change
def sub_five(number):
    return number - 5

декоратор скушал имя функции
sub_five(5)
всесто оригинала запущена inner функция
5
def sub_five(number):
    print("и только тут саботал оригинал")
    return number - 5

sub_five(5)
и только тут саботал оригинал
0
@change
sub_five(number):
    print("и только тут саботал оригинал")
    return number - 5
SyntaxError: invalid syntax
@change
def sub_five(number):
    print("и только тут саботал оригинал")
    return number - 5

декоратор скушал имя функции
sub_five(5)

всесто оригинала запущена inner функция
и только тут саботал оригинал
5
sub_five(5)
всесто оригинала запущена inner функция
и только тут саботал оригинал
5


>>> 
>>> 
>>> #file +try+except+finally
>>> 
>>> 
import os #моуль для создания файлов

os.getcwd() #в какую директорию будут сохраняться файлы
#'C:\\Users\\ekol0322\\AppData\\Local\\Programs\\Python\\Python313'

fstream = open("my_first_txt_file.txt", "w")
try:
    fstream.write ("Привет мир!\n")
except:
    print ("up")
finally:
    fstream.close()
... 
...     
#up
try:
    fstream.write ("ПРивет мир!\n")
finally:
    fstream.close()

    
#Traceback (most recent call last):
#  File "<pyshell#8>", line 2, in <module>
#    fstream.write ("ПРивет мир!\n")
#ValueError: I/O operation on closed file.

with open("my_2_txt_file.txt", "w") as fstream:
    fstream.write ("1 Привет мир!\n")
    fstream.write ("2 Привет мир!\n")

    
# Traceback (most recent call last):
#   File "<pyshell#13>", line 2, in <module>
#     fstream.write ("1 Привет мир!\n")
#   File "C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\encodings\cp1252.py", line 19, in encode
#     return codecs.charmap_encode(input,self.errors,encoding_table)[0]
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 2-7: character maps to <undefined>
with open("my_2_txt_file.txt", "w", encoding="utf-8") as fstream:
    fstream.write ("1 Привет мир!\n")
    fstream.write ("2 Привет мир!\n")

    
# 14
# 14

fstream = open("my_first_txt_file.txt", "w", encoding="utf-8") #добавлена кодировка
try:
    fstream.write ("Привет мир!\n")
except:
    print ("up")
finally:
    fstream.close()

    
#12

fstream = open("my_first_txt_file.txt", "w")
try:
    fstream.write ("Hello world\n")   #сообщение на английском, пишется без проблем
except:
    print ("up")
finally:
    fstream.close()